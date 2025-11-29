

## 🧩 1️⃣ Dấu hiệu nhận biết overfitting cơ bản

| Dấu hiệu                                                        | Giải thích                                                   |
| --------------------------------------------------------------- | ------------------------------------------------------------ |
| **Train R² rất cao**, nhưng **Test R² thấp**                    | Mô hình học quá kỹ dữ liệu huấn luyện, không khái quát được. |
| **Train RMSE rất nhỏ**, nhưng **Test RMSE lớn**                 | Sai số trên test cao → mô hình khớp noise.                   |
| **SHAP hoặc feature importance biến động mạnh** giữa train/test | Mô hình “đoán mò” hơn là học pattern ổn định.                |
| **Residual plot có pattern rõ ràng**                            | Không random → mô hình chưa phù hợp dữ liệu.                 |

---

## ⚙️ 2️⃣ Cách kiểm tra nhanh trong code

Nếu bạn dùng hàm `evaluate_model()` như ở trên, chỉ cần nhìn **Train_R² vs Test_R²** là biết ngay.
Nhưng ta có thể **thêm cảnh báo tự động** 👇

```python
def check_overfitting(metrics, threshold=0.15):
    """
    Kiểm tra mức độ overfitting dựa trên chênh lệch R² train-test.
    threshold: ngưỡng chênh lệch cho phép (thường 0.1–0.2)
    """
    diff = metrics["Train_R2"] - metrics["Test_R2"]
    if diff > threshold:
        print(f"⚠️ Warning: Possible overfitting detected! (ΔR² = {diff:.3f})")
    else:
        print(f"✅ Model generalizes well (ΔR² = {diff:.3f})")
```

---

## 📊 3️⃣ Trực quan hoá (visual check)

### (a) So sánh phân phối y_pred giữa train & test

```python
import matplotlib.pyplot as plt

def plot_pred_distributions(model, X_train, y_train, X_test, y_test):
    plt.figure(figsize=(7,4))
    plt.hist(model.predict(X_train), bins=30, alpha=0.6, label='Train predictions')
    plt.hist(model.predict(X_test), bins=30, alpha=0.6, label='Test predictions')
    plt.legend()
    plt.title("Distribution of Predictions (Train vs Test)")
    plt.show()
```

→ Nếu hai phân phối quá khác nhau ⇒ overfit.

---

### (b) Residual Plot

```python
def plot_residuals(model, X_test, y_test):
    y_pred = model.predict(X_test)
    residuals = y_test - y_pred
    plt.figure(figsize=(6,4))
    plt.scatter(y_pred, residuals, alpha=0.5)
    plt.axhline(0, color='red', linestyle='--')
    plt.xlabel("Predicted")
    plt.ylabel("Residuals")
    plt.title("Residual Plot")
    plt.show()
```

→ Residual nên **phân bố ngẫu nhiên quanh 0**. Nếu có dạng cong hoặc lệch ⇒ mô hình chưa ổn hoặc overfit.

---

## 🧠 4️⃣ Khi phát hiện overfit thì xử lý thế nào?

| Giải pháp                                                              | Áp dụng cho       |
| ---------------------------------------------------------------------- | ----------------- |
| **Giảm độ phức tạp** (`max_depth`, `n_estimators`, `min_child_weight`) | XGBoost, RF       |
| **Regularization** (`reg_alpha`, `reg_lambda`, `l1_ratio`)             | XGB, Lasso, Ridge |
| **Cross-validation nghiêm ngặt hơn** (n_splits ↑)                      | ML model          |
| **Feature selection / PCA / SHAP pruning**                             | Giảm nhiễu biến   |
| **Tăng kích thước dữ liệu** hoặc rolling window rộng hơn               | Panel/Time-series |

---

