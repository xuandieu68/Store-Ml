"""
Refactored, minimal and more robust helper module for portfolio & risk management.

Main goals:
- Keep core, most-used utilities: IO, summary stats, basic portfolio weights,
  regressions, vol models (EWMA + GARCH), VaR/CVaR summary, correlations.
- Fix bugs from original file:
  - remove duplicate functions, fix misspellings (excess_returns),
  - robust date/column handling,
  - robust list-to-DataFrame conversion,

  - use pseudo-inverse when covariance is singular,
  - consistent annual_factor inference based on index frequency.
- Simpler API and fewer side-effects (plotting off by default).
- Clear docstrings and type hints.

Notes:
- Functions that were previously marked "not available" were intentionally
  omitted or kept out-of-scope to keep this module compact and tested.
- Keep external deps minimal: pandas, numpy, statsmodels, arch (optional for GARCH).
"""
from typing import Union, List, Optional, Dict, Tuple
import math
import warnings

import numpy as np
import pandas as pd
from pandas import Timestamp
import statsmodels.api as sm

# arch is optional (only for GARCH). Import lazily in function to avoid heavy import at module load.
from scipy.stats import norm

# Formatting
pd.options.display.float_format = "{:,.6f}".format
warnings.filterwarnings("ignore")


# -------------------------
# Helpers / Input sanitation
# -------------------------
def _ensure_dataframe(x: Union[pd.Series, pd.DataFrame, List[pd.Series]]) -> pd.DataFrame:
    """
    Convert Series or list of Series into a DataFrame aligned by index.
    """
    if isinstance(x, pd.Series):
        return x.to_frame()
    if isinstance(x, list):
        # Ensure each element is Series or DataFrame
        series_list = []
        for i, s in enumerate(x):
            if isinstance(s, pd.Series):
                series_list.append(s.rename(s.name or f'series_{i}'))
            elif isinstance(s, pd.DataFrame):
                # if DataFrame, append all its columns
                for c in s.columns:
                    series_list.append(s[c].rename(c))
            else:
                raise TypeError("List elements must be pd.Series or pd.DataFrame")
        # concat on columns, align indexes
        return pd.concat(series_list, axis=1)
    if isinstance(x, pd.DataFrame):
        return x.copy()
    raise TypeError("Input must be pd.Series, pd.DataFrame or list thereof")


def _infer_annual_factor_from_index(index: pd.Index) -> int:
    """
    Try to infer periods-per-year from a DatetimeIndex frequency.
    Fallback to 12 (monthly) when unknown.
    """
    if not isinstance(index, pd.DatetimeIndex):
        return 12
    freq = pd.infer_freq(index)
    mapping = {
        'D': 252, 'B': 252, 'W': 52, 'M': 12, 'MS': 12, 'Q': 4, 'QS': 4, 'A': 1, 'AS': 1
    }
    if freq is None:
        # Sometimes infer_freq fails for irregular but likely monthly data — use heuristic:
        # if median difference >20 days -> monthly, >1 day and <7 -> daily, else monthly
        diffs = np.median(np.diff(index.view('i8'))) / 1e9 / (24 * 3600)
        if diffs > 20:
            return 12
        if diffs <= 7:
            return 252
        return 12
    # take first letter(s) only (e.g., 'BM' -> 'B')
    key = ''.join([c for c in freq if c.isalpha()])
    return mapping.get(key, 12)


def _ensure_date_index(df: Union[pd.DataFrame, pd.Series]) -> Union[pd.DataFrame, pd.Series]:
    """
    If there's a column named like 'date' (case-insensitive), set it as index.
    If index is object-like but contains datelike objects, convert to DateTimeIndex.
    """
    if isinstance(df, pd.Series):
        df = df.to_frame()
        was_series = True
    else:
        was_series = False

    # Lower-case name check
    cols_lower = [c.lower() for c in df.columns]
    if 'date' in cols_lower:
        pos = cols_lower.index('date')
        colname = df.columns[pos]
        df = df.set_index(colname)

    # Try convert index to datetime if possible
    try:
        if not isinstance(df.index, pd.DatetimeIndex):
            df.index = pd.to_datetime(df.index)
    except Exception:
        pass

    return df.iloc[:, 0] if was_series else df


def read_excel_default(excel_name: str, index_col: int = 0, parse_dates: bool = True,
                       print_sheets: bool = False, sheet_name: Optional[Union[str, int]] = None,
                       **kwargs) -> Optional[pd.DataFrame]:
    """
    Read excel (wrapper). If print_sheets True prints sheets and returns None.
    Ensures index named 'date' (if possible).
    """
    if print_sheets:
        n = 0
        while True:
            try:
                sheet = pd.read_excel(excel_name, sheet_name=n)
                print(f'Sheet {n}: {list(sheet.columns)[:10]}')
                print(sheet.head(2))
                n += 1
                print()
            except Exception:
                return None
    sheet_name = 0 if sheet_name is None else sheet_name
    df = pd.read_excel(excel_name, index_col=index_col, parse_dates=parse_dates,
                       sheet_name=sheet_name, **kwargs)
    # normalize index name
    try:
        if df.index.name and str(df.index.name).lower() in ('date', 'dates'):
            df.index.name = 'date'
        elif isinstance(df.index[0], (pd.Timestamp, pd.DatetimeTZDtype, pd.Timestamp.__class__)) or hasattr(df.index[0], 'year'):
            df.index.name = 'date'
    except Exception:
        pass
    return df


# -------------------------
# Returns helpers
# -------------------------
def calc_cumulative_returns(returns: Union[pd.Series, pd.DataFrame],
                            as_percent: bool = True) -> pd.DataFrame:
    """
    Compute cumulative returns: (1+rt).cumprod() - 1
    Returns DataFrame aligned with input.
    """
    df = _ensure_dataframe(returns)
    df = _ensure_date_index(df)
    df = df.apply(pd.to_numeric, errors='coerce')
    cum = (1 + df).cumprod() - 1
    if as_percent:
        return cum
    return cum


# -------------------------
# Volatility models
# -------------------------
def calc_ewma_volatility(excess_returns: pd.Series,
                         theta: float = 0.94,
                         initial_vol: float = 0.2,
                         periods_per_year: Optional[int] = None) -> pd.Series:
    """
    EWMA volatility. initial_vol provided as annualized volatility by default.
    Returns series of annualized vol (to match other outputs). If you want daily vol,
    set periods_per_year accordingly.
    """
    if periods_per_year is None:
        if isinstance(excess_returns.index, pd.DatetimeIndex):
            periods_per_year = _infer_annual_factor_from_index(excess_returns.index)
        else:
            periods_per_year = 252
    # convert annualized initial_vol to per-period variance
    var_t0 = (initial_vol ** 2) / periods_per_year
    ewma_var = []
    var = var_t0
    for x in excess_returns.fillna(0).values:
        var = theta * var + (1 - theta) * (x ** 2)
        ewma_var.append(var)
    # convert back to annualized vol
    ewma_vol = np.sqrt(np.array(ewma_var) * periods_per_year)
    return pd.Series(ewma_vol, index=excess_returns.index, name='EWMA_vol')


def calc_garch_volatility(excess_returns: pd.Series,
                          p: int = 1, q: int = 1) -> pd.Series:
    """
    Fit a GARCH(p,q) model (using arch). Return conditional volatility as annualized
    (multiplying by sqrt(periods_per_year) when index frequency inferred).
    Requires 'arch' package.
    """
    try:
        from arch import arch_model  # local import
    except Exception as e:
        raise ImportError("arch package required for GARCH. Install via `pip install arch`") from e

    # If excess_returns has NA at start, arch may fail; dropna for fitting then reindex
    er = excess_returns.dropna()
    if er.empty:
        # return series of NaNs
        return pd.Series(index=excess_returns.index, dtype=float, name='GARCH_vol')

    model = arch_model(er, vol='Garch', p=p, q=q, rescale=False)
    res = model.fit(disp='off')
    cond_vol = res.conditional_volatility  # per-period
    # infer frequency
    per_year = _infer_annual_factor_from_index(excess_returns.index)
    # annualize
    cond_vol_annual = cond_vol * math.sqrt(per_year)
    return pd.Series(cond_vol_annual, index=cond_vol.index).reindex(excess_returns.index)


# -------------------------
# Summary statistics & VaR/CVaR
# -------------------------
def calc_summary_statistics(returns: Union[pd.Series, pd.DataFrame, List[pd.Series]],
                            annual_factor: Optional[int] = None,
                            rf: Optional[Union[pd.Series, pd.DataFrame]] = None,
                            provided_excess_returns: Optional[bool] = None,
                            var_quantile: Union[float, List[float]] = 0.05,
                            return_tangency_weights: bool = False) -> pd.DataFrame:
    """
    Core summary statistics for returns (per column):
    Mean, Annualized Mean, Vol, Annualized Vol, Sharpe, Min, Max, Skew, Kurtosis,
    Historical VaR/CVaR for quantile(s), Max Drawdown, Peak/Bottom/Recovery dates.
    - returns: Series/DataFrame or list of Series
    - annual_factor: if None, infer from index; default fallback = 12
    - rf: risk-free series (aligned) to compute true Sharpe if provided and provided_excess_returns=False
    """
    df = _ensure_dataframe(returns)
    df = _ensure_date_index(df)
    df = df.apply(pd.to_numeric, errors='coerce').dropna(how='all', axis=1)

    if annual_factor is None:
        annual_factor = _infer_annual_factor_from_index(df.index)

    if provided_excess_returns is None:
        # assume input are total returns by default (safer) => not excess
        provided_excess_returns = False

    result = pd.DataFrame(index=df.columns)

    # Basic moments
    mean = df.mean()
    std = df.std(ddof=1)
    result['Mean'] = mean
    result['Annualized Mean'] = mean * annual_factor
    result['Vol'] = std
    result['Annualized Vol'] = std * math.sqrt(annual_factor)

    # Sharpe
    try:
        if not provided_excess_returns:
            if rf is None:
                # can't compute true excess Sharpe without rf; compute mean/std
                result['Sharpe'] = mean / std
            else:
                rf_s = rf.copy()
                if isinstance(rf_s, pd.DataFrame):
                    rf_s = rf_s.iloc[:, 0]
                rf_s = _ensure_date_index(rf_s)
                # align
                aligned = df.join(rf_s.rename('rf'), how='inner')
                er = aligned.iloc[:, :-1].subtract(aligned['rf'], axis=0)
                result['Sharpe'] = er.mean() / aligned.iloc[:, :-1].std(ddof=1)
        else:
            result['Sharpe'] = mean / std
    except Exception:
        result['Sharpe'] = np.nan

    result['Annualized Sharpe'] = result['Sharpe'] * math.sqrt(annual_factor)

    # Range & higher moments
    result['Min'] = df.min()
    result['Max'] = df.max()
    result['Skewness'] = df.skew()
    result['Excess Kurtosis'] = df.kurtosis()

    # VaR / CVaR
    if isinstance(var_quantile, (float, int)):
        var_quantile = [float(var_quantile)]
    for q in var_quantile:
        key_var = f'Historical VaR ({q:.2%})'
        key_cvar = f'Historical CVaR ({q:.2%})'
        result[key_var] = df.quantile(q)
        # CVaR: mean of losses beyond quantile (for left tail)
        cvar_vals = []
        for col in df.columns:
            series = df[col].dropna()
            if series.empty:
                cvar_vals.append(np.nan)
                continue
            thr = series.quantile(q)
            cvar_vals.append(series[series <= thr].mean())
        result[key_cvar] = cvar_vals

    # Drawdowns and recovery
    wealth_index = 1_000 * (1 + df).cumprod()
    previous_peaks = wealth_index.cummax()
    drawdowns = (wealth_index - previous_peaks) / previous_peaks
    result['Max Drawdown'] = drawdowns.min()
    bottoms = drawdowns.idxmin()
    peaks = []
    recovery = []
    for col in wealth_index.columns:
        b = bottoms[col]
        try:
            # peak prior to bottom
            prev_peak = previous_peaks.loc[:b, col].idxmax()
            peaks.append(prev_peak)
            # recovery
            prev_max = previous_peaks.loc[:b, col].max()
            rec_idx = wealth_index.loc[b:, col][wealth_index.loc[b:, col] >= prev_max]
            recovery.append(rec_idx.index.min() if not rec_idx.empty else pd.NaT)
        except Exception:
            peaks.append(pd.NaT)
            recovery.append(pd.NaT)
    result['Peak'] = peaks
    result['Bottom'] = bottoms
    result['Recovery'] = recovery
    # Duration in days when possible
    try:
        result['Duration (days)'] = (result['Recovery'] - result['Bottom']).apply(
            lambda x: int(x.days) if pd.notna(x) and isinstance(x, pd.Timestamp) else np.nan
        )
    except Exception:
        result['Duration (days)'] = np.nan

    return result


def calc_var_cvar_summary(returns: Union[pd.Series, pd.DataFrame],
                          quantile: float = 0.05,
                          window: int = 60,
                          ewma_theta: float = 0.94,
                          ewma_initial_vol: float = 0.2,
                          garch_p: int = 1, garch_q: int = 1,
                          normal_vol_formula: bool = False) -> pd.DataFrame:
    """
    Simple VaR/CVaR generator with columns:
    - Expanding Historical VaR, Rolling Historical VaR
    - Expanding/Rolling Vol (sample or RMS), EWMA Vol, GARCH Vol (if arch installed)
    - Parametric versions using normal quantile
    Returns DataFrame indexed by time with same index as input returns (if Series input uses first column).
    """
    df = _ensure_dataframe(returns)
    df = _ensure_date_index(df)
    series = df.iloc[:, 0].dropna()

    if series.empty:
        return pd.DataFrame()

    per_year = _infer_annual_factor_from_index(series.index)
    z = norm.ppf(quantile)

    summary = pd.DataFrame(index=series.index)
    # Expanding & rolling historical VaR
    summary[f'Expanding {window} Hist VaR ({quantile:.2%})'] = series.expanding(min_periods=window).quantile(quantile)
    summary[f'Rolling {window} Hist VaR ({quantile:.2%})'] = series.rolling(window=window, min_periods=window).quantile(quantile)

    # Volatility measures
    if normal_vol_formula:
        summary[f'Expanding {window} Vol'] = series.expanding(min_periods=window).std()
        summary[f'Rolling {window} Vol'] = series.rolling(window=window, min_periods=window).std()
    else:
        summary[f'Expanding {window} Vol'] = np.sqrt((series ** 2).expanding(min_periods=window).mean())
        summary[f'Rolling {window} Vol'] = np.sqrt((series ** 2).rolling(window=window, min_periods=window).mean())

    summary[f'EWMA theta={ewma_theta} Vol'] = calc_ewma_volatility(series, theta=ewma_theta,
                                                                    initial_vol=ewma_initial_vol,
                                                                    periods_per_year=per_year)
    try:
        garch_vol = calc_garch_volatility(series, p=garch_p, q=garch_q)
        summary[f'GARCH({garch_p},{garch_q}) Vol'] = garch_vol
    except Exception:
        summary[f'GARCH({garch_p},{garch_q}) Vol'] = np.nan

    # Parametric VaR (vol * z)
    summary[f'Expanding {window} Param VaR ({quantile:.2%})'] = summary[f'Expanding {window} Vol'] * z
    summary[f'Rolling {window} Param VaR ({quantile:.2%})'] = summary[f'Rolling {window} Vol'] * z
    summary[f'EWMA Param VaR ({quantile:.2%})'] = summary[f'EWMA theta={ewma_theta} Vol'] * z
    summary[f'GARCH Param VaR ({quantile:.2%})'] = summary.get(f'GARCH({garch_p},{garch_q}) Vol', pd.Series(np.nan)) * z

    # CVaR parametric approximations using normal tail formula
    summary[f'Param CVaR ({quantile:.2%})'] = - norm.pdf(z) / quantile * summary[f'Rolling {window} Vol']

    return summary


# -------------------------
# Correlations
# -------------------------
import seaborn as sns
import matplotlib.pyplot as plt


def calc_correlations(returns: Union[pd.DataFrame, pd.Series],
                      plot: bool = False,
                      figsize: Tuple[float, float] = (8, 6),
                      annot: bool = True) -> pd.DataFrame:
    """
    Compute correlation matrix. Optionally plot a heatmap (requires matplotlib/seaborn).
    Returns correlation DataFrame.
    """
    df = _ensure_dataframe(returns)
    df = _ensure_date_index(df)
    corr = df.corr()
    if plot:
        plt.figure(figsize=figsize)
        sns.heatmap(corr, annot=annot, cmap='coolwarm', vmin=-1, vmax=1)
        plt.title("Correlation matrix")
        plt.show()
    return corr


# -------------------------
# Portfolio weights
# -------------------------
def calc_tangency_weights(returns: Union[pd.DataFrame, pd.Series],
                          annual_factor: Optional[int] = None,
                          expected_returns: Optional[Union[pd.Series, pd.DataFrame]] = None,
                          regularization: Optional[float] = None) -> pd.DataFrame:
    """
    Tangency portfolio weights (maximize Sharpe assuming no risk-free in solver).
    - returns: DataFrame of returns
    - expected_returns: optional expected returns (per-period). If None will use sample mean.
    - regularization: between 0 and 1; 0 -> diag-only covariance (risk parity-ish), 1 -> sample cov.
    Returns DataFrame indexed by asset names with column 'Tangency Weights'.
    """
    df = _ensure_dataframe(returns)
    df = _ensure_date_index(df)
    if annual_factor is None:
        annual_factor = _infer_annual_factor_from_index(df.index)

    mu = None
    if expected_returns is not None:
        mu = _ensure_dataframe(expected_returns).iloc[:, 0]
    else:
        mu = df.mean() * annual_factor

    cov = df.cov() * annual_factor
    if regularization is None or regularization >= 1:
        cov_used = cov
    else:
        diag = np.diag(np.diag(cov))
        cov_used = regularization * cov + (1 - regularization) * pd.DataFrame(diag, index=cov.index, columns=cov.columns)

    # invert (use pseudo-inverse for numerically stable)
    try:
        cov_inv = np.linalg.inv(cov_used.values)
    except np.linalg.LinAlgError:
        cov_inv = np.linalg.pinv(cov_used.values)
    ones = np.ones(len(mu))
    # compute tangency weights (unnormalized)
    w_unnorm = cov_inv @ mu.values
    # scale such that weights sum to 1
    w = w_unnorm / (ones @ w_unnorm)
    return pd.DataFrame(w, index=df.columns, columns=['Tangency Weights'])


def calc_gmv_weights(returns: Union[pd.DataFrame, pd.Series]) -> pd.DataFrame:
    """
    Global Minimum Variance portfolio (weights sum to 1, unconstrained).
    """
    df = _ensure_dataframe(returns)
    df = _ensure_date_index(df)
    cov = df.cov()
    try:
        cov_inv = np.linalg.inv(cov.values)
    except np.linalg.LinAlgError:
        cov_inv = np.linalg.pinv(cov.values)
    ones = np.ones(cov.shape[0])
    w = cov_inv @ ones
    w = w / (ones @ w)
    return pd.DataFrame(w, index=df.columns, columns=['GMV Weights'])


def calc_equal_weights(returns: Union[pd.DataFrame, pd.Series]) -> pd.DataFrame:
    df = _ensure_dataframe(returns)
    cols = df.columns
    w = np.repeat(1.0 / len(cols), len(cols))
    return pd.DataFrame(w, index=cols, columns=['Equal Weights'])


def calc_risk_parity_weights(returns: Union[pd.DataFrame, pd.Series]) -> pd.DataFrame:
    """
    Simple proxy risk parity: inverse variance weights normalized to sum to 1.
    """
    df = _ensure_dataframe(returns)
    df = _ensure_date_index(df)
    inv_var = 1 / df.var()
    w = inv_var / inv_var.sum()
    return pd.DataFrame(w.values, index=df.columns, columns=['Risk Parity Weights'])


# -------------------------
# Regression utilities
# -------------------------
def calc_regression(y: Union[pd.Series, pd.DataFrame],
                    X: Union[pd.Series, pd.DataFrame],
                    intercept: bool = True,
                    annual_factor: Optional[int] = None,
                    return_model: bool = False,
                    return_fitted: bool = False) -> Union[pd.DataFrame, sm.regression.linear_model.RegressionResultsWrapper]:
    """
    Simple wrapper for OLS regression using statsmodels.
    - Returns DataFrame summary of parameters and some diagnostics unless return_model True.
    - If return_fitted True returns fitted values as Series/DataFrame.
    """
    y_df = _ensure_dataframe(y)
    X_df = _ensure_dataframe(X)
    y_df = _ensure_date_index(y_df)
    X_df = _ensure_date_index(X_df)

    # align by index
    df = y_df.join(X_df, how='inner').dropna()
    if df.shape[0] < 4:
        raise ValueError("Not enough observations after alignment")

    y_col = df.columns[0]
    X_cols = df.columns[1:] if df.shape[1] > 1 else X_df.columns

    Y = df[[y_col]]
    Xmat = df[X_cols]
    if intercept:
        Xmat = sm.add_constant(Xmat)

    model = sm.OLS(Y, Xmat, missing='drop')
    res = model.fit()
    if return_model:
        return res
    params = res.params
    summary = pd.DataFrame(params).T
    # add a few metrics
    summary['R-Squared'] = res.rsquared
    summary['Residual Std'] = res.resid.std(ddof=1)
    if return_fitted:
        fitted = res.fittedvalues
        return fitted
    return summary


def calc_iterative_regression(multiple_y: Union[pd.DataFrame, List[pd.Series]],
                              X: Union[pd.DataFrame, pd.Series],
                              intercept: bool = True) -> pd.DataFrame:
    """
    Run calc_regression for each column in multiple_y against same X.
    Returns concatenated summary DataFrame.
    """
    Y = _ensure_dataframe(multiple_y)
    X_df = _ensure_dataframe(X)
    X_df = _ensure_date_index(X_df)
    Y = _ensure_date_index(Y)
    summaries = []
    for col in Y.columns:
        try:
            s = calc_regression(Y[[col]], X_df, intercept=intercept)
            s.index = [col]
            summaries.append(s)
        except Exception:
            continue
    if summaries:
        return pd.concat(summaries, axis=0)
    return pd.DataFrame()


# -------------------------
# Portfolio creation
# -------------------------
def create_portfolio(returns: Union[pd.DataFrame, pd.Series],
                     weights: Union[Dict[str, float], List[float]],
                     port_name: Optional[str] = None) -> pd.DataFrame:
    """
    Create portfolio returns given weights (dict keyed by column name or list aligned to columns order).
    """
    df = _ensure_dataframe(returns)
    df = _ensure_date_index(df)

    if isinstance(weights, list):
        if len(weights) != df.shape[1]:
            raise ValueError("Weights length must equal number of assets in returns")
        w = pd.Series(weights, index=df.columns)
    else:
        w = pd.Series(weights)
        # ensure same order as df
        w = w.reindex(df.columns).fillna(0.0)

    port = df @ w
    name = port_name or " + ".join([f"{n}({v:.2%})" for n, v in w.items()])
    return pd.DataFrame(port.rename(name))


# -------------------------
# Misc
# -------------------------
def calc_negative_pct(returns: Union[pd.Series, pd.DataFrame, List[pd.Series]],
                      positive: bool = False) -> pd.DataFrame:
    """
    Compute percentage of negative (or positive) returns, number of returns and number of negative/positive.
    """
    df = _ensure_dataframe(returns)
    df = _ensure_date_index(df)
    df = df.dropna(how='all')
    if positive:
        flags = df > 0
    else:
        flags = df < 0
    stats = pd.concat([
        flags.mean().rename('% Positive' if positive else '% Negative'),
        flags.count().rename('N Returns'),
        flags.sum().rename('N Positive' if positive else 'N Negative')
    ], axis=1)
    return stats
