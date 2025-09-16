---
 FF5 factor 
---

**Các bước chính để tính 5 yếu tố**

**Chia Size**: median vốn hóa → Small (S) vs Big (B).

**Chia Value (BM)**: 30% thấp = Growth (L), 30% cao = Value (H).
→ Dùng để tính HML.

**Chia Profitability (OP = Operating Profitability)**: 30% thấp = Weak (W), 30% cao = Robust (R).
→ Dùng để tính RMW.

**Chia Investment (Inv = Asset growth)**: 30% thấp = Conservative (C), 30% cao = Aggressive (A).
→ Dùng để tính CMA.

SMB được tính như trung bình SMB từ ba kiểu phân loại (Size–BM, Size–OP, Size–Inv).

```python

import pandas as pd
def fama_french_5f(df: pd.DataFrame, rf: pd.Series = None):
    """
    Tính 5 yếu tố Fama-French: MKT, SMB, HML, RMW, CMA
    
    Parameters
    ----------
    df : pd.DataFrame
        Cột bắt buộc:
        - date : datetime
        - stock_id : mã cổ phiếu
        - ret : return (decimal, vd 0.02 = 2%)
        - mktcap : market cap
        - bm : book-to-market ratio
        - op : operating profitability
        - inv : asset growth (investment)
    rf : pd.Series (optional)
        Risk-free rate theo cùng tần suất, index = date.
        
    Returns
    -------
    factors : pd.DataFrame
        DataFrame với các cột ['MKT','SMB','HML','RMW','CMA'] (+ 'MKT-RF' nếu có rf)
    """
    results = []

    for date, group in df.groupby("date"):
        g = group.copy()

        # 1. Chia Size
        size_median = g["mktcap"].median()
        g["size_port"] = g["mktcap"].apply(lambda x: "S" if x <= size_median else "B")

        # 2. Chia BM (Value)
        bm30, bm70 = g["bm"].quantile([0.3, 0.7])
        g["bm_port"] = g["bm"].apply(lambda x: "L" if x <= bm30 else ("H" if x >= bm70 else "M"))

        # 3. Chia Profitability (OP)
        op30, op70 = g["op"].quantile([0.3, 0.7])
        g["op_port"] = g["op"].apply(lambda x: "W" if x <= op30 else ("R" if x >= op70 else "M"))

        # 4. Chia Investment (Inv)
        inv30, inv70 = g["inv"].quantile([0.3, 0.7])
        g["inv_port"] = g["inv"].apply(lambda x: "C" if x <= inv30 else ("A" if x >= inv70 else "M"))

        # ===== Portfolio returns =====
        # Value portfolios
        val_port = g.groupby(["size_port","bm_port"])["ret"].mean()
        # Profitability portfolios
        op_port = g.groupby(["size_port","op_port"])["ret"].mean()
        # Investment portfolios
        inv_port = g.groupby(["size_port","inv_port"])["ret"].mean()

        # ===== Factor Construction =====
        # MKT
        vwret = (g["ret"] * g["mktcap"]).sum() / g["mktcap"].sum()

        # SMB = average(SMB from value, profitability, investment)
        smb_val = val_port.loc["S"].mean() - val_port.loc["B"].mean()
        smb_op  = op_port.loc["S"].mean() - op_port.loc["B"].mean()
        smb_inv = inv_port.loc["S"].mean() - inv_port.loc["B"].mean()
        smb = (smb_val + smb_op + smb_inv) / 3

        # HML = (SH + BH)/2 - (SL + BL)/2
        hml = 0.5*(val_port.get(("S","H"),0) + val_port.get(("B","H"),0)) - \
              0.5*(val_port.get(("S","L"),0) + val_port.get(("B","L"),0))

        # RMW = (SR + BR)/2 - (SW + BW)/2
        rmw = 0.5*(op_port.get(("S","R"),0) + op_port.get(("B","R"),0)) - \
              0.5*(op_port.get(("S","W"),0) + op_port.get(("B","W"),0))

        # CMA = (SC + BC)/2 - (SA + BA)/2
        cma = 0.5*(inv_port.get(("S","C"),0) + inv_port.get(("B","C"),0)) - \
              0.5*(inv_port.get(("S","A"),0) + inv_port.get(("B","A"),0))

        # ===== Save =====
        if rf is not None:
            row = {"date": date, "MKT": vwret, "SMB": smb, "HML": hml,
                   "RMW": rmw, "CMA": cma, "MKT-RF": vwret - rf.loc[date]}
        else:
            row = {"date": date, "MKT": vwret, "SMB": smb, "HML": hml,
                   "RMW": rmw, "CMA": cma}
        results.append(row)

    factors = pd.DataFrame(results).set_index("date").sort_index()
    return factors

``` 

---
 FF3 factor 
---
Chia size theo median → Small (S) vs Big (B).

Chia BM theo phân vị 30%–70% → Low (Growth), Medium, High (Value).

Tạo 6 danh mục (S/L, S/M, S/H, B/L, B/M, B/H).

Tính SMB = trung bình return của nhóm Small – nhóm Big.

Tính HML = trung bình High BM – trung bình Low BM.

Tính MKT = lợi nhuận toàn thị trường (value-weighted). Nếu có risk-free (RF) → MKT-RF.


```python
import pandas as pd

def fama_french_3f(df: pd.DataFrame, rf: pd.Series = None):
    """
    Tính 3 yếu tố Fama-French: MKT-RF, SMB, HML từ DataFrame panel.

    Parameters
    ----------
    df : pd.DataFrame
        Cột bắt buộc:
        - date : datetime
        - stock_id : mã cổ phiếu
        - ret : return (lợi nhuận kỳ đó, đã ở dạng số thập phân, ví dụ 0.02 = 2%)
        - mktcap : market capitalization tại đầu kỳ
        - bm : book-to-market ratio
    rf : pd.Series (optional)
        Risk-free rate theo cùng tần suất, index = date.

    Returns
    -------
    factors : pd.DataFrame
        DataFrame với các cột ['MKT', 'SMB', 'HML'] (và 'MKT-RF' nếu rf không None)
    """
    factors = []

    for date, group in df.groupby("date"):
        # 1. Chia size: median của mktcap
        size_median = group["mktcap"].median()
        group["size_port"] = group["mktcap"].apply(lambda x: "S" if x <= size_median else "B")

        # 2. Chia value: 30% thấp = Growth, 30% cao = Value
        bm30 = group["bm"].quantile(0.3)
        bm70 = group["bm"].quantile(0.7)

        def bm_bucket(x):
            if x <= bm30:
                return "L"   # Low BM (Growth)
            elif x >= bm70:
                return "H"   # High BM (Value)
            else:
                return "M"
        group["bm_port"] = group["bm"].apply(bm_bucket)

        # 3. Tạo 6 danh mục size*bm
        portfolios = group.groupby(["size_port", "bm_port"])["ret"].mean()

        # 4. SMB = (S/H + S/M + S/L)/3 - (B/H + B/M + B/L)/3
        smb = portfolios.loc["S"].mean() - portfolios.loc["B"].mean()

        # 5. HML = (H/S + H/B)/2 - (L/S + L/B)/2
        # thực ra dùng size*bm: (SH + BH)/2 - (SL + BL)/2
        hml = 0.5 * (portfolios.get(("S","H"),0) + portfolios.get(("B","H"),0)) - \
              0.5 * (portfolios.get(("S","L"),0) + portfolios.get(("B","L"),0))

        # 6. MKT = giá trị thị trường toàn bộ
        vwret = (group["ret"] * group["mktcap"]).sum() / group["mktcap"].sum()
        if rf is not None:
            mktrf = vwret - rf.loc[date]
            row = {"date": date, "MKT": vwret, "SMB": smb, "HML": hml, "MKT-RF": mktrf}
        else:
            row = {"date": date, "MKT": vwret, "SMB": smb, "HML": hml}

        factors.append(row)

    factors = pd.DataFrame(factors).set_index("date").sort_index()
    return factors
```

---
Trọng số 
--- 
```python
def wmean(x, wgt, var):
    """
    Tính trung bình có trọng số.

    Parameters
    ----------
    x : DataFrame
        Dữ liệu đầu vào, phải chứa các cột tương ứng với `wgt` và `var`.
    wgt : str
        Tên cột dùng làm trọng số.
    var : str
        Tên cột chứa biến cần tính trung bình.

    Returns
    -------
    float
        Giá trị trung bình có trọng số.
    """
    num = (x[wgt] * x[var]).sum()  # Tổng tích giữa trọng số và biến
    den = x[wgt].sum()  # Tổng trọng số
    return num / den
```

---
Simulation portfolio with 2 factor 
---
```python
def simul_100_ports(df, factor1, factor2, nport=10, wgt='ew', ret='fxret'):
    # Xử lý các giá trị bị thiếu
    df = df.dropna(subset=[factor1, factor2])

    # Xếp hạng các cổ phiếu dựa trên 2 yếu tố (factor1 và factor2)
    rank1 = (df.groupby('date')[factor1]
                .transform(pd.qcut, q=nport, labels=range(1, nport + 1)))
    rank2 = (df.groupby('date')[factor2]
                .transform(pd.qcut, q=nport, labels=range(1, nport + 1)))
    
    # Tạo bảng với các port từ hai yếu tố
    df['port'] = (df['rank1'] - 1) * nport + df['rank2']
    
    # Tính toán lợi suất theo cách tính trọng số
    if wgt == 'ew':
        port_xret = df.groupby(['date', 'port'])[ret].mean()
    elif wgt == 'vw':
        port_xret = df.groupby(['date', 'port']).apply(wmean, 'me', ret)
    else:
        print("weight scheme should be either 'ew' or 'vw'.")
        return

    port_xret = port_xret.unstack().shift()

    # Đếm số lượng cổ phiếu trong mỗi port
    port_count = df.groupby(['date', 'port'])[ret].count()
    port_count = port_count.unstack().shift()

    # Tính toán đặc điểm của các port
    port_character = df.groupby(['date', 'port']).mean(numeric_only=True).groupby(level=1).shift().groupby(level=1).mean()

    return port_xret, port_count, port_character
```


--- 
Hồi quy OLS for CAPM, FF3,FF5 
---
```python 
import numpy as np
import pandas as pd
import statsmodels.api as sm

def est_params(df: pd.DataFrame, model_type: str = None):
    '''
    CAPM, FF3, FF5 모형에 대해 alpha와 모든 계수 및 t-value를 추정하는 함수
    새로운 출력 형식: coef (t-value)

    Parameters
    ----------
    df : DataFrame
        반드시 포함해야 하는 컬럼:
            - 'xret'
            - 'MKT'
        선택적으로:
            - 'SMB','HML' (FF3, FF5)
            - 'RMW','CMA' (FF5)

    model_type : str, optional
        None  : 단순 평균 alpha (평균 초과수익률)
        'CAPM': CAPM 회귀
        'FF3' : Fama-French 3 factor 회귀
        'FF5' : Fama-French 5 factor 회귀

    Returns
    -------
    DataFrame
        index = 변수명 (const, MKT, SMB, HML, RMW, CMA)
        columns = ['coef'] : "coef\n(t-value)" 형식
    '''
    y = df['xret']

    if model_type == 'CAPM':
        X = df[['MKT']]
    elif model_type == 'FF3':
        X = df[['MKT','SMB','HML']]
    elif model_type == 'FF5':
        X = df[['MKT','SMB','HML','RMW','CMA']]
    else:
        # 단순 평균 alpha
        alpha = np.mean(y)
        t_val = alpha / (np.std(y, ddof=1) / np.sqrt(len(y)))
        res = pd.DataFrame({'coef':[f"{alpha:.4f}\n({t_val:.2f})"]}, index=['const'])
        return res

    X = sm.add_constant(X)
    model = sm.OLS(y, X).fit()

    # hệ số và t-value format
    formatted = []
    for var in model.params.index:
        coef = model.params[var]
        tval = model.tvalues[var]
        formatted.append(f"{coef:.4f}\n({tval:.2f})")

    res = pd.DataFrame({'coef': formatted}, index=model.params.index)
    return res
```

