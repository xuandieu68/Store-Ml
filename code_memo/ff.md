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


** Hàm Python ** 
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

** Hàm python**
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
