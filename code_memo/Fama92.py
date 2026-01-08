

import pandas as pd
import numpy as np
import statsmodels.api as sm
from typing import List, Optional

# =============================================================================
# 1. CÁC HÀM TIỆN ÍCH VÀ HỖ TRỢ CHUNG (UTILITIES)
# =============================================================================

def _infer_return_scale(s: pd.Series) -> str:
    """Tự động nhận diện quy mô của tỷ suất sinh lời (Returns)"""
    x = pd.to_numeric(s, errors="coerce").dropna()
    if x.empty:
        return "decimal"
    
    p_in_gross_band = x.between(0.8, 1.2).mean()
    p_abs_gt1 = (x.abs() > 1).mean()
    
    if p_in_gross_band >= 0.6:
        return "gross"
    if p_abs_gt1 >= 0.2:
        return "percent"
    return "decimal"

def _to_decimal_returns(s: pd.Series, scale: str) -> pd.Series:
    """Chuyển đổi returns về dạng thập phân chuẩn ."""
    if scale == "gross":
        return s.astype(float) - 1.0
    if scale == "percent":
        return s.astype(float) / 100.0
    return s.astype(float)

def add_port_year_keys(df: pd.DataFrame, date_col: str = "date") -> pd.DataFrame:
    """Thêm các khóa thời gian phục vụ phân loại danh mục (tháng 7 đến tháng 6 năm sau) ."""
    out = df.copy()
    dm = pd.to_datetime(out[date_col])
    out["year"] = dm.dt.year
    out["month"] = dm.dt.month
    out["date_m"] = dm.dt.to_period("M").dt.to_timestamp("M")
    # port_year bắt đầu từ tháng 7 năm t đến tháng 6 năm t+1
    out["port_year"] = np.where(out["month"] >= 7, out["year"], out["year"] - 1)
    return out

def _make_lagged(series: pd.Series, nlags: int = 1, prefix: str = "mkt") -> pd.DataFrame:
    """Tạo các biến trễ cho chuỗi thời gian ."""
    df = pd.DataFrame({f"{prefix}": series})
    for L in range(1, nlags + 1):
        df[f"{prefix}_lag{L}"] = series.shift(L)
    return df

def _sum_beta(y: pd.Series, mkt: pd.DataFrame, min_obs: int = 24) -> Optional[float]:
    """Tính tổng hệ số Beta từ hồi quy OLS bao gồm cả các biến trễ ."""
    df = pd.concat([y, mkt], axis=1).dropna()
    if len(df) < min_obs:
        return np.nan
    
    X = sm.add_constant(df[mkt.columns])
    try:
        res = sm.OLS(df[y.name], X).fit()
        # Tổng các hệ số của mkt và mkt_lag
        beta = float(sum(res.params[col] for col in mkt.columns if col.startswith("mkt")))
    except Exception:
        beta = np.nan
    return beta

# =============================================================================
# 2. TÍNH TOÁN PRE-RANKING BETA [1]
# =============================================================================

def compute_pre_ranking_beta(
    df: pd.DataFrame,
    symbol_col: str = "symbol",
    date_col: str = "date",
    ret_col: str = "ret",
    mkt_col: str = "rm",
    rf_col: str = "rf",
    min_obs: int = 24,
    max_obs: int = 60,
    nlags: int = 1
) -> pd.DataFrame:
    """Tính Pre-ranking Beta dựa trên cửa sổ 24-60 tháng kết thúc vào tháng 6 ."""
    d = add_port_year_keys(df, date_col=date_col).copy()
    d["xret"] = d[ret_col] - d[rf_col]
    d["xrm"] = d[mkt_col] - d[rf_col]
    
    # Lấy các dòng tại tháng 6 làm điểm mốc tái cơ cấu
    june_rows = d.loc[d["month"] == 6, [symbol_col, "port_year", "date_m"]].drop_duplicates()
    d = d.sort_values([symbol_col, "date_m"])
    
    out = []
    for sym, g in d.groupby(symbol_col, sort=False):
        jr = june_rows[june_rows[symbol_col] == sym]
        for _, row in jr.iterrows():
            py = int(row["port_year"])
            # Cửa sổ tính toán kết thúc vào tháng 6 năm py
            end = pd.Timestamp(py, 6, 1).to_period("M").to_timestamp("M")
            start = end - pd.DateOffset(months=max_obs - 1)
            
            win = g[(g["date_m"] >= start) & (g["date_m"] <= end)].dropna(subset=["xret", "xrm"])
            
            if len(win) < min_obs:
                out.append([sym, py, np.nan])
                continue
            
            if len(win) > max_obs:
                win = win.iloc[-max_obs:].copy()
            
            mkt_df = _make_lagged(win["xrm"], nlags=nlags, prefix="mkt")
            beta = _sum_beta(win["xret"], mkt_df, min_obs=min_obs)
            out.append([sym, py, beta])
            
    return pd.DataFrame(out, columns=[symbol_col, "port_year", "pre_beta"])


# =============================================================================
# 3. PHÂN CHIA DANH MỤC (PORTFOLIO FORMATION) 
# =============================================================================

def assign_size_port(
    df: pd.DataFrame, 
    me_col: str = 'me_size', 
    port_col: str = 'size_port', 
    rebalance_month: int = 7, 
    start_year: int = 2001, 
    end_year: int = 2024
) -> pd.DataFrame:
    """Chia cổ phiếu vào 10 danh mục quy mô (size deciles) hàng năm ."""
    df = df.copy()
    df['year'] = pd.to_datetime(df['date']).dt.year
    df['month'] = pd.to_datetime(df['date']).dt.month
    
    # Xác định port_year để giữ nguyên danh mục từ tháng 7 đến tháng 6 năm sau
    df['port_year'] = np.where(df['month'] >= rebalance_month, df['year'], df['year'] - 1)
    df[port_col] = np.nan
    
    for year in range(start_year, end_year + 1):
        mask = df['port_year'] == year
        subset = df.loc[mask]
        
        valid_me = subset[me_col].dropna()
        if len(valid_me) < 10:
            continue
            
        try:
            # Phân chia 10 nhóm dựa trên thứ hạng (rank) 
            ports = pd.qcut(valid_me.rank(method='first'), 10, labels=False, duplicates='drop')
            df.loc[valid_me.index, port_col] = ports
        except Exception as e:
            print(f"> Error in {year}: {e}")
            
    return df


def assign_prebeta_within_size(df, beta_col='pre_beta', q=10):
    """Trong mỗi nhóm Size, chia tiếp thành 10 nhóm dựa trên Pre-beta ."""
    df['pre_beta_port'] = df.groupby(['port_year', 'size_port'])[beta_col].transform(
        lambda x: pd.qcut(x.rank(method='first'), q, labels=False) if len(x.dropna()) >= q else np.nan
    )
    return df

def assign_post_beta_to_df(df: pd.DataFrame, post_df: pd.DataFrame, 
                           group_cols: List[str] = ["size_port", "pre_beta_port"]) -> pd.DataFrame:
    """Gộp Post-ranking Beta vào bảng dữ liệu chính ."""
    return df.merge(post_df, on=group_cols, how="left")



# =============================================================================
# 4. TỔNG HỢP BẢNG THỐNG KÊ (TABLE GENERATION) 
# =============================================================================

def make_table1_ff92(
    df_in: pd.DataFrame,
    ret_col: str = "ret",
    lnme_col: str = "ln_ME",
    beta_col: str = "post_beta",
    size_col: str = "size_port",
    preb_col: str = "pre_beta_port",
    input_unit: str = "auto",
    restrict_to_holding: bool = True
):
    """Tạo bảng thống kê Panel (c) theo Fama-French 1992 ."""
    d = df_in.copy()
    d = d.dropna(subset=[size_col, preb_col])
    
    # Lọc theo giai đoạn nắm giữ (tháng 7 năm t đến tháng 6 năm t+1) 
    if restrict_to_holding and {"date", "port_year"}.issubset(d.columns):
        dt = pd.to_datetime(d["date"])
        start = pd.to_datetime(d["port_year"].astype(int).astype(str) + "-07-01")
        end = pd.to_datetime((d["port_year"] + 1).astype(int).astype(str) + "-07-01")
        d = d[(dt >= start) & (dt < end)]
        
    unit = _infer_return_scale(d[ret_col]) if input_unit == "auto" else input_unit
    d["_ret_dec"] = _to_decimal_returns(d[ret_col], unit)
    
    # Gom nhóm theo thời gian, quy mô và pre-beta 
    monthly_2d = (d.groupby(["date", size_col, preb_col], as_index=False)
                  .agg(Return=("_ret_dec", "mean"),
                       Beta=(beta_col, "mean"),
                       lnME=(lnme_col, "mean")))
    
    # Thống kê tổng hợp theo hàng và cột
    monthly_size = (d.groupby(["date", size_col], as_index=False)
                    .agg(Return=("_ret_dec", "mean"),
                         Beta=(beta_col, "mean"),
                         lnME=(lnme_col, "mean")))
    
    monthly_preb = (d.groupby(["date", preb_col], as_index=False)
                    .agg(Return=("_ret_dec", "mean"),
                         Beta=(beta_col, "mean"),
                         lnME=(lnme_col, "mean")))
    
    return monthly_2d, monthly_size, monthly_preb



