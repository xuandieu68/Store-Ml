---
Financial_ratios calc 
---

```python
import numpy as np
import pandas as pd

def add_financial_ratios(df: pd.DataFrame, firm_col: str = None, time_col: str = None) -> pd.DataFrame:
    """
    Tính toán các chỉ số tài chính và thêm vào DataFrame.
    Nếu thiếu cột cần thiết, công thức đó sẽ bị bỏ qua.
    
    Parameters
    ----------
    df : pd.DataFrame
        Dữ liệu gốc
    firm_col : str
        Tên cột mã công ty (dùng để groupby khi tính AG)
    time_col : str
        Tên cột thời gian (năm/quý), dùng để sort khi tính AG
    """
    
    def safe_calc(name, formula, required_cols):
        """Thêm cột mới nếu đủ dữ liệu"""
        if set(required_cols).issubset(df.columns):
            try:
                df[name] = formula()
            except Exception:
                pass  # tránh crash nếu lỗi chia 0 hoặc NA
    
    # Market-based ratios
    safe_calc("Q",   lambda: (df['debt']*1000 + df['me']*1_000_000) / (df['TA']*1000), ['debt','me','TA'])
    safe_calc("MV",  lambda: (df['me']*1_000_000 + df['Tli']*1000) / (df['TA']*1000), ['me','Tli','TA'])
    safe_calc("BM",  lambda: (df['TE']*1000) / (df['me']*1_000_000), ['TE','me'])
    safe_calc("MTB", lambda: df['me']*1_000_000 / ((df['TA'] - df['Tli'])*1000), ['me','TA','Tli'])
    safe_calc("Q1",  lambda: (df['me']*1_000_000 + df['Tli']*1000) / (df['short_debt']*1000 + df['long_debt']*1000), 
              ['me','Tli','short_debt','long_debt'])
    
    # Price/share ratios
    safe_calc("MPS", lambda: df['me']*100000 / df['outstanding'], ['me','outstanding'])
    safe_calc("BPS", lambda: df['TE']*1000 / df['outstanding'], ['TE','outstanding'])
    safe_calc("BP",  lambda: df['BPS'] / df['MPS'], ['BPS','MPS'])
    
    # Firm characteristics
    safe_calc("size",  lambda: np.log(df['TA']), ['TA'])
    safe_calc("size1", lambda: np.log(df['me']), ['me'])
    safe_calc("TANG",  lambda: df['PPE'] / df['TA'], ['PPE','TA'])
    safe_calc("CH",    lambda: df['cash'] / df['TA'], ['cash','TA'])
    safe_calc("DIV",   lambda: df['divident'] / df['TA'], ['divident','TA'])
    safe_calc("RD",    lambda: df['R&D'] / df['sale'], ['R&D','sale'])
    safe_calc("ROA",   lambda: df['NI'] / df['TA'], ['NI','TA'])
    safe_calc("ROE",   lambda: df['EBIT'] / df['TE'], ['EBIT','TE'])
    safe_calc("lev",   lambda: df['Tli'] / df['TA'], ['Tli','TA'])
    safe_calc("NPM",   lambda: df['NI'] / df['sale'], ['NI','sale'])
    safe_calc("FCF",   lambda: df['cashflow'] / df['TA'], ['cashflow','TA'])
    safe_calc("liq",   lambda: df['CA'] / df['CL'], ['CA','CL'])
    safe_calc("netinpay", lambda: (df['interet_income'] - df['expence']) / df['TA'], 
              ['interet_income','expence','TA'])
    
    # Leverage
    safe_calc("lev_long",  lambda: df['long_debt'] / df['TA'], ['long_debt','TA'])
    safe_calc("lev_short", lambda: df['short_debt'] / df['TA'], ['short_debt','TA'])
    
    # Capital structure
    safe_calc("CS", lambda: df['Tli'] / df['TE'], ['Tli','TE'])
    
    # Asset growth (yoy)
    if firm_col and time_col and {'TA', firm_col, time_col}.issubset(df.columns):
        try:
            df = df.sort_values([firm_col, time_col])
            df['AG'] = df.groupby(firm_col)['TA'].pct_change()
        except Exception:
            pass
    
    return df
```

---
with diff char
---
```python
import numpy as np
import pandas as pd

def add_additional_ratios(df: pd.DataFrame, firm_col: str = None, time_col: str = None, industry_col: str = None) -> pd.DataFrame:
    """
    Hàm tính toán các biến bổ sung theo mô tả trong yêu cầu.
    Các biến sẽ chỉ được tính khi đủ dữ liệu.
    
    Parameters
    ----------
    df : pd.DataFrame
        DataFrame chứa dữ liệu
    firm_col : str
        Tên cột định danh công ty (dùng cho groupby)
    time_col : str
        Tên cột thời gian (năm/quý)
    industry_col : str
        Tên cột ngành của công ty
    
    Returns
    -------
    df : pd.DataFrame có thêm các biến tính toán
    """
    
    def safe_calc(name, formula, required_cols):
        if set(required_cols).issubset(df.columns):
            try:
                df[name] = formula()
            except Exception:
                pass
    
    # AGE = số năm niêm yết (year - năm niêm yết đầu tiên)
    if firm_col and time_col and 'list_year' in df.columns:
        try:
            df['AGE'] = df[time_col] - df['list_year']
        except Exception:
            pass
    
    # SIZE = log(TA)
    safe_calc("SIZE", lambda: np.log(df['TA']), ['TA'])
    
    # LEV = Tli / TA
    safe_calc("LEV", lambda: df['Tli'] / df['TA'], ['Tli','TA'])
    
    # ROE = NI / ((TA_open + TA_close)/2)
    if {'NI','TA_open','TA_close'}.issubset(df.columns):
        safe_calc("ROE", lambda: df['NI'] / ((df['TA_open'] + df['TA_close'])/2), ['NI','TA_open','TA_close'])
    
    # VROE = phương sai ROE 3 năm gần nhất
    if firm_col and time_col and 'ROE' in df.columns:
        try:
            df = df.sort_values([firm_col, time_col])
            df['VROE'] = df.groupby(firm_col)['ROE'].rolling(3).var().reset_index(level=0, drop=True)
        except Exception:
            pass
    
    # MTB = ME / Net assets
    safe_calc("MTB", lambda: df['me'] / df['TE'], ['me','TE'])
    
    # VOL = shares traded / outstanding
    safe_calc("VOL", lambda: df['shares_traded'] / df['outstanding'], ['shares_traded','outstanding'])
    
    # INDNUM = log(số công ty trong ngành)
    if industry_col:
        try:
            df['INDNUM'] = df.groupby([industry_col, time_col])[firm_col].transform("nunique")
            df['INDNUM'] = np.log(df['INDNUM'])
        except Exception:
            pass
    
    # INDSIZE = log(tổng tài sản các công ty trong ngành)
    if industry_col and 'TA' in df.columns:
        try:
            df['INDSIZE'] = df.groupby([industry_col, time_col])['TA'].transform("sum")
            df['INDSIZE'] = np.log(df['INDSIZE'])
        except Exception:
            pass
    
    # DD = dividend dummy
    if 'divident' in df.columns:
        df['DD'] = (df['divident'] > 0).astype(int)
    
    # DIVER = đa ngành (giả định có cột num_segments)
    if 'num_segments' in df.columns:
        df['DIVER'] = (df['num_segments'] > 1).astype(int)
    
    # LMVE = log(Market cap = price * shares_outstanding)
    if {'price','outstanding'}.issubset(df.columns):
        safe_calc("LMVE", lambda: np.log(df['price'] * df['outstanding']), ['price','outstanding'])
    
    # MERGER = dummy cho M&A (giả định có cột merger_event)
    if 'merger_event' in df.columns:
        df['MERGER'] = (df['merger_event'] == 1).astype(int)
    
    # INST = institutional ownership
    safe_calc("INST", lambda: df['inst_shares'] / df['outstanding'], ['inst_shares','outstanding'])
    
    # TURN = log(shares traded / outstanding)
    safe_calc("TURN", lambda: np.log(df['shares_traded'] / df['outstanding']), ['shares_traded','outstanding'])
    
    # RET = market-adjusted return (giả định có cột stock_return, market_return)
    if {'stock_return','market_return'}.issubset(df.columns):
        safe_calc("RET", lambda: df['stock_return'] - df['market_return'], ['stock_return','market_return'])
    
    # ISSUE = dummy if equity issued
    if 'equity_issued' in df.columns:
        df['ISSUE'] = (df['equity_issued'] == 1).astype(int)
    
    # LIQUIDITY = mean(|daily return| / daily trading value)
    if {'abs_daily_return','daily_trading_value'}.issubset(df.columns):
        safe_calc("LIQUIDITY", lambda: (df['abs_daily_return'] / df['daily_trading_value']).groupby([df[firm_col], df[time_col]]).transform("mean"), 
                  ['abs_daily_return','daily_trading_value'])
    
    return df
```


Bạn có muốn mình viết thêm lựa chọn **chỉ tính một nhóm chỉ số** (ví dụ chỉ market-based, chỉ profitability) để dễ kiểm soát không?
