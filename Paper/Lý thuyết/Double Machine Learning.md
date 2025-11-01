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
Y = \theta D + g(X) + \varepsilon

và ( D ) phụ thuộc vào ( X ):
[D = m(X) + \nu]

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

## 🔹 1. Ý nghĩa của (g(X)) và (m(X))

* g(X) : mô tả **mối quan hệ phi tuyến giữa biến kiểm soát (X)** và outcome (Y).
  → Ví dụ: firm value có thể phi tuyến với firm size hoặc profitability.

*  m(X) : mô tả **cách biến xử lý (D)** (ví dụ leverage) **phụ thuộc vào các biến kiểm soát (X)**.
  → Ví dụ: leverage bị ảnh hưởng bởi size, tangibility, liquidity, v.v.
---


## 🔹 3. Vậy chọn mô hình nào cho (g(X)) và (m(X))?

Phụ thuộc vào **đặc trưng dữ liệu** và **mức độ phi tuyến**. Dưới đây là bảng hướng dẫn:

| Tình huống dữ liệu              | Gợi ý mô hình cho (g(X)), (m(X))  | Đặc điểm                          |
| ------------------------------- | --------------------------------- | --------------------------------- |
| Dữ liệu nhỏ (n < 2000)          | Lasso / Ridge                     | Giữ đơn giản, dễ diễn giải        |
| Dữ liệu trung bình (2000–10000) | Random Forest / Gradient Boosting | Học được quan hệ phi tuyến mượt   |
| Dữ liệu lớn (≥ 10000)           | XGBoost / LightGBM / Neural Net   | Bắt tương tác mạnh, hiệu suất cao |
| Muốn giải thích được            | Lasso hoặc RandomForest + SHAP    | Xem được biến nào quan trọng      |

👉 Thực tế, **Random Forest** là lựa chọn rất phổ biến trong nghiên cứu tài chính khi dùng DML, vì:

* không cần tuning nhiều,
* ổn định với nhiễu,
* cho phép phi tuyến và tương tác bậc cao.

---

## 🔹 4. Cách kiểm tra xem g(X), m(X) có hợp lý không

DML không yêu cầu bạn phải biết chính xác hàm (g) hay (m), nhưng bạn **có thể kiểm tra tính hợp lý** của ước lượng bằng:

1. **Performance check**

   * Kiểm tra (R^2) của mô hình (Y \sim X) và (D \sim X):
     Nếu (R^2) quá thấp → (X) không giải thích được (Y) hoặc (D) → phần causal có thể bị nhiễu.

2. **Variable importance / SHAP values**

   * Kiểm tra xem biến nào ảnh hưởng mạnh đến (Y) và (D).
     Nếu biến chính như size, profitability có trọng số cao → mô hình học hợp lý.

3. **Cross-validation error**

   * Dùng cross-fitting hoặc k-fold CV để đảm bảo không overfit.

---

## 🔹 5. Diễn giải trực giác


* (g(X)): mọi yếu tố khác ảnh hưởng đến firm value như size, growth, profitability, industry, year,...
* (m(X)): mọi yếu tố ảnh hưởng đến leverage như tangibility, liquidity, profitability,...

Nếu không loại bỏ phần (g(X)) và (m(X)), ta sẽ **lẫn lộn giữa correlation và causation**, vì leverage bị ảnh hưởng bởi chính những biến cũng ảnh hưởng đến firm value.

DML dùng ML để **học tự động** hai mối quan hệ này và loại bỏ chúng ra trước khi ước lượng hiệu ứng thật của leverage lên firm value.
Kết quả sau khi fit() mô hình sẽ trả về coef của biến độc lập sau khi loại bỏ phần phi tuyến trong g(X) 
---


---

