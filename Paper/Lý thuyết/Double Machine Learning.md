#  **Double Machine Learning (DML)**

---

## 🧠 1. Trực giác: DML giải quyết vấn đề gì?

Trong kinh tế lượng, khi ta muốn **ước lượng tác động nhân quả (causal effect)** của một biến ( D ) (chẳng hạn leverage) lên ( Y ) (firm value), ta thường lo ngại rằng:

* ( D ) có thể tương quan với các biến nhiễu ( X ),
* và mô hình phi tuyến hoặc tương tác phức tạp khiến OLS bị **thiên lệch (biased)**.

👉 Double Machine Learning được tạo ra để:

> “Tách riêng phần nhân quả khỏi phần dự đoán phức tạp của machine learning, để ước lượng hiệu ứng nhân quả chính xác ngay cả khi có nhiều biến kiểm soát (high-dimensional controls).”

---

## 🧩 2. Cấu trúc cơ bản của DML

Giả sử ta có mô hình nhân quả:
[
Y = \theta D + g(X) + \varepsilon
]
và ( D ) phụ thuộc vào ( X ):
[
D = m(X) + \nu
]

Trong đó:

* ( Y ): biến phụ thuộc (ví dụ: firm value),
* ( D ): biến xử lý (treatment, ví dụ: leverage),
* ( X ): tập biến kiểm soát (ví dụ: size, growth, profitability,...),
* ( g(X) ), ( m(X) ): hàm phi tuyến, có thể học bằng ML (Random Forest, XGBoost, Lasso,...).

---

## ⚙️ 3. Các bước thực hiện Double Machine Learning

### 🔹 Bước 1: Cross-fitting (điểm mấu chốt)

Chia dữ liệu thành K-fold (thường K=2 hoặc 5).

### 🔹 Bước 2: Dự đoán phần dư bằng ML

Với từng fold:

1. Huấn luyện mô hình ML trên tập train để ước lượng ( \hat{g}(X) ) và ( \hat{m}(X) ),
2. Trên tập test:

   * Lấy **phần dư outcome:**
     [
     \tilde{Y} = Y - \hat{g}(X)
     ]
   * Lấy **phần dư treatment:**
     [
     \tilde{D} = D - \hat{m}(X)
     ]

### 🔹 Bước 3: Hồi quy phần dư

Sau đó ước lượng hệ số nhân quả:
[
\hat{\theta} = \frac{\text{Cov}(\tilde{Y}, \tilde{D})}{\text{Var}(\tilde{D})}
]
hoặc đơn giản là OLS của (\tilde{Y}) lên (\tilde{D}).

---

## 🧩 4. Vì sao gọi là “Double” Machine Learning?

Bởi vì:

* Ta dùng ML **hai lần**: một lần cho outcome ((Y)) và một lần cho treatment ((D)),
* Nhằm loại bỏ phần phi tuyến và tương tác phức tạp của các biến kiểm soát.

Kết quả là phần còn lại (residuals) đại diện cho mối quan hệ **nhân quả thuần túy** giữa (D) và (Y).

---

## 📊 5. Ứng dụng trong tài chính

DML rất hữu ích trong các nghiên cứu kiểu:

* “Tác động của leverage lên firm value” (với nhiều biến kiểm soát),
* “Ảnh hưởng của ESG score đến performance”,
* “Causal effect of liquidity, R&D, or investment on firm growth”,
* Khi bạn muốn tách biệt phần **causal effect** khỏi phần **predictive noise** trong mô hình phi tuyến.

---

## 🧩 6. Công cụ và thư viện phổ biến

* **Python:**

  * `EconML` của Microsoft (hỗ trợ DML, DRLearner, CausalForest, ...),
  * `DoubleML` (thư viện chuyên cho DML, syntax rất chuẩn).

Ví dụ (Python – DoubleML):

```python
from doubleml import DoubleMLData, DoubleMLPLR
from sklearn.ensemble import RandomForestRegressor

dml_data = DoubleMLData(df, y_col='Y', d_cols='D', x_cols=X_cols)

ml_g = RandomForestRegressor()
ml_m = RandomForestRegressor()

dml_plr = DoubleMLPLR(dml_data, ml_g, ml_m)
dml_plr.fit()

print("Causal effect (theta):", dml_plr.coef)
```

---

## ⚠️ 7. Những điều cần lưu ý

| Chủ đề                               | Giải thích                                                       |
| ------------------------------------ | ---------------------------------------------------------------- |
| **Không thay thế ML thông thường**   | DML không nhằm dự đoán Y, mà để ước lượng **hiệu ứng nhân quả**. |
| **Cross-fitting là bắt buộc**        | Nếu không chia fold, ước lượng sẽ bị overfit → sai lệch.         |
| **Giả định unconfoundedness**        | Cần tin rằng mọi yếu tố gây nhiễu đều nằm trong X.               |
| **Không phải “black box” hoàn toàn** | ML chỉ xử lý phần nuisance (g(X), m(X)), phần causal vẫn là OLS. |
| **Phải đủ dữ liệu**                  | ML cần đủ mẫu để học tốt phần nuisance functions.                |

---

## 💡 8. Tóm tắt dễ nhớ

| Mục      | Ý chính                                                                   |
| -------- | ------------------------------------------------------------------------- |
| Mục tiêu | Ước lượng tác động nhân quả trong môi trường nhiều biến và phi tuyến      |
| Ý tưởng  | Dùng ML để loại bỏ phần ảnh hưởng của X trước khi ước lượng causal effect |
| “Double” | ML được dùng cho cả outcome và treatment                                  |
| Lợi ích  | Giảm bias, vẫn cho phép dùng mô hình phi tuyến                            |
| Hạn chế  | Cần nhiều dữ liệu, không tự động kiểm tra giả định nhân quả               |

---
````python
import pandas as pd
import numpy as np
import shap
import statsmodels.api as sm
import matplotlib.pyplot as plt

from doubleml import DoubleMLData, DoubleMLPLR
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LassoCV, RidgeCV
from sklearn.model_selection import train_test_split

# Optional: for gradient boosting
from xgboost import XGBRegressor
from lightgbm import LGBMRegressor

class DMLUtilityPro:
    def __init__(self, data, y_col, d_col, x_cols,
                 model_name='rf', n_folds=5, random_state=42,
                 ml_g=None, ml_m=None):
        """
        Double Machine Learning Utility Class (Pro version)
        ----------------------------------------------------
        Cho phép linh hoạt chọn ML model và phân tích SHAP.
        """

        self.data = data.copy()
        self.y_col = y_col
        self.d_col = d_col
        self.x_cols = x_cols
        self.n_folds = n_folds
        self.random_state = random_state
        self.model_name = model_name.lower()
        self.results = {}

        # === chọn model ===
        self.ml_g = ml_g or self._get_model()
        self.ml_m = ml_m or self._get_model()

        # === chuẩn bị dữ liệu cho DML ===
        self.dml_data = DoubleMLData(self.data, y_col=y_col,
                                     d_cols=d_col, x_cols=x_cols)
        self.dml_model = None
        self.ols_model = None

    # ===========================================================
    # Model selector
    # ===========================================================
    def _get_model(self):
        """Chọn model theo tên"""
        if self.model_name == 'rf':
            return RandomForestRegressor(
                n_estimators=300, max_depth=6, random_state=self.random_state)
        elif self.model_name == 'xgb':
            return XGBRegressor(
                n_estimators=300, learning_rate=0.05,
                max_depth=6, subsample=0.8, colsample_bytree=0.8,
                random_state=self.random_state)
        elif self.model_name == 'lgbm':
            return LGBMRegressor(
                n_estimators=300, learning_rate=0.05,
                max_depth=-1, random_state=self.random_state)
        elif self.model_name == 'lasso':
            return LassoCV(cv=5, random_state=self.random_state)
        elif self.model_name == 'ridge':
            return RidgeCV(cv=5)
        else:
            raise ValueError(f"Model '{self.model_name}' không được hỗ trợ.")

    # ===========================================================
    # FIT DML
    # ===========================================================
    def fit_dml(self):
        """Huấn luyện Double Machine Learning"""
        self.dml_model = DoubleMLPLR(self.dml_data, self.ml_g, self.ml_m,
                                     n_folds=self.n_folds)
        self.dml_model.fit()

        coef = self.dml_model.coef[0]
        se = self.dml_model.se[0]
        tval = coef / se
        pval = 2 * (1 - sm.stats.norm.cdf(abs(tval)))

        self.results['DML'] = {
            'coef': coef,
            'se': se,
            't': tval,
            'p': pval
        }
        return self.results['DML']

    # ===========================================================
    # FIT OLS
    # ===========================================================
    def fit_ols(self):
        """Hồi quy OLS để so sánh"""
        X = self.data[[self.d_col] + self.x_cols]
        X = sm.add_constant(X)
        y = self.data[self.y_col]
        ols = sm.OLS(y, X).fit()

        self.results['OLS'] = {
            'coef': ols.params[self.d_col],
            'se': ols.bse[self.d_col],
            't': ols.tvalues[self.d_col],
            'p': ols.pvalues[self.d_col],
            'r2': ols.rsquared
        }
        self.ols_model = ols
        return self.results['OLS']

    # ===========================================================
    # COMPARE
    # ===========================================================
    def compare(self, round_digits=4):
        """So sánh DML vs OLS"""
        if 'DML' not in self.results:
            self.fit_dml()
        if 'OLS' not in self.results:
            self.fit_ols()

        comp = pd.DataFrame([
            {
                'Model': 'OLS',
                'Coef': self.results['OLS']['coef'],
                'SE': self.results['OLS']['se'],
                't': self.results['OLS']['t'],
                'p': self.results['OLS']['p'],
                'R2': self.results['OLS']['r2']
            },
            {
                'Model': 'DML',
                'Coef': self.results['DML']['coef'],
                'SE': self.results['DML']['se'],
                't': self.results['DML']['t'],
                'p': self.results['DML']['p'],
                'R2': np.nan
            }
        ])
        return comp.round(round_digits)

    # ===========================================================
    # SHAP Analysis
    # ===========================================================
    def shap_analysis(self, mode='g', max_display=10):
        """
        Phân tích SHAP cho g(X) hoặc m(X).
        mode = 'g' => Y ~ X
        mode = 'm' => D ~ X
        """
        if mode not in ['g', 'm']:
            raise ValueError("mode phải là 'g' hoặc 'm'.")

        # chọn model và target
        target = self.y_col if mode == 'g' else self.d_col
        model = self.ml_g if mode == 'g' else self.ml_m

        X = self.data[self.x_cols]
        y = self.data[target]

        # fit model (vì DoubleML không lưu trực tiếp estimator)
        model.fit(X, y)

        explainer = shap.Explainer(model, X)
        shap_values = explainer(X)

        title = f"SHAP Summary for {'g(X): Y~X' if mode=='g' else 'm(X): D~X'} ({self.model_name})"
        shap.summary_plot(shap_values, X, max_display=max_display, show=False)
        plt.title(title)
        plt.tight_layout()
        plt.show()

    # ===========================================================
    # SUMMARY
    # ===========================================================
    def summary(self):
        print("="*65)
        print(f"Double Machine Learning Summary ({self.model_name.upper()})")
        print("="*65)
        print(self.compare())
        print("\nNotes:")
        print("- DML: học phi tuyến g(X), m(X) bằng ML.")
        print("- OLS: giả định tuyến tính hoàn toàn.")
        print("- SHAP: giúp giải thích hàm g(X) và m(X).")
        print("="*65)



   
````
