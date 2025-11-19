SHAP
---

## 🔹 1. Trước hết: SHAP là gì?

**SHAP (SHapley Additive exPlanations)** là một phương pháp dựa trên **lý thuyết trò chơi Shapley**.
Nó tính xem **mỗi biến (feature)** đóng góp **bao nhiêu vào dự đoán của từng quan sát**.
* SHAP tính toán mức độ mỗi đặc trưng (feature) đóng góp vào dự đoán của mô hình. Kỹ thuật này được thiết kế để phân bổ một cách công bằng sự đóng góp của mỗi đặc trưng vào kết quả dự đoán cuối cùng

Cụ thể:

$$\text{Prediction} = E[\text{model output}] + \sum_i \text{SHAP value}_i$$


* $$(E[\text{model output}])$$: giá trị trung bình của mô hình.
* $$(\text{SHAP value}_i)$$: đóng góp của biến (i) vào việc đẩy dự đoán lên hoặc xuống.

✅ SHAP **không giả định mô hình tuyến tính**, mà hoạt động với **mọi loại mô hình** (XGBoost, Random Forest, Neural Network...).
Do đó, nó là **công cụ giải thích phi tuyến tốt nhất hiện nay**.

---

## 🔹 2. Vậy SHAP giải thích được *tính phi tuyến* như thế nào?

Khi bạn vẽ **SHAP dependence plot**, nó thể hiện:
* Trục X: giá trị của biến (ví dụ: leverage)
* Trục Y: SHAP value (ảnh hưởng lên firm value dự đoán)

👉 Nếu đường quan hệ giữa X và SHAP value là:
* **Thẳng (linear)** → quan hệ **tuyến tính**
* **Cong (nonlinear)** → mô hình học được **tính phi tuyến**
* **Đổi dấu ở giữa** → quan hệ **phi tuyến kiểu threshold hoặc turning point**

Ví dụ minh họa (mô tả đơn giản):

| Hình dạng quan hệ SHAP | Ý nghĩa kinh tế                                                                    |
| ---------------------- | ---------------------------------------------------------------------------------- |
| Đường thẳng xuống      | leverage càng cao → firm value càng giảm tuyến tính                                |
| Đường cong chữ U       | firm value giảm khi leverage thấp/quá cao → có **ngưỡng tối ưu**                   |
| Đường sigmoid          | tác động mạnh ở vùng trung bình, yếu ở cực trị → **mối quan hệ phi tuyến bão hòa** |

---

## 🔹 3. So sánh khả năng “phát hiện phi tuyến” giữa SHAP và hồi quy truyền thống

| Đặc điểm                    | Hồi quy tuyến tính (OLS)                | Mô hình ML + SHAP                                |
| --------------------------- | --------------------------------------- | ------------------------------------------------ |
| Dạng mô hình                | Tuyến tính (βx)                         | Có thể phi tuyến (XGBoost, RF, NN)               |
| Mối quan hệ giữa X và Y     | Cố định là tuyến tính                   | Linh hoạt, có thể cong, tương tác phức tạp       |
| Phát hiện nonlinearity      | Phải thêm biến bậc hai (X², logX, v.v.) | Tự học được từ dữ liệu                           |
| Diễn giải quan hệ phi tuyến | Giới hạn                                | SHAP plot thể hiện trực tiếp                     |
| Tương tác (interaction)     | Phải thêm thủ công (X1*X2)              | SHAP interaction values có thể phát hiện tự động |

---

## 🔹 5. Tuy nhiên — SHAP không “biết” tuyến tính hay phi tuyến theo nghĩa thống kê
* SHAP **không kiểm định thống kê** như hồi quy (không có p-value, không có β).
* SHAP chỉ **phản ánh hình dạng thực tế của ảnh hưởng trong mô hình**.
  
👉 Vì thế, nếu bạn đang làm **nghiên cứu học thuật (academic)**, cách kết hợp hợp lý là:
1. Dùng ML + SHAP để **phát hiện dạng phi tuyến**,
2. Sau đó **kiểm chứng lại bằng hồi quy phi tuyến (chẳng hạn thêm bậc hai hoặc tương tác)** để có kết quả thống kê rõ ràng.

---

## 🔹 6. ✅ Kết luận tóm tắt

| So sánh             | SHAP                                                      | Hồi quy tuyến tính                 |
| ------------------- | --------------------------------------------------------- | ---------------------------------- |
| Mục tiêu            | Giải thích đóng góp biến trong mô hình ML                 | Ước lượng hệ số & ý nghĩa thống kê |
| Xử lý phi tuyến     | Rất mạnh – hiển thị dạng cong, turning point, interaction | Phải giả định sẵn dạng hàm         |
| Xử lý tuyến tính    | Tốt, thể hiện rõ ảnh hưởng đều                            | Cực kỳ rõ ràng (β tuyến tính)      |
| Diễn giải học thuật | Trực quan, nhưng không có p-value                         | Có kiểm định thống kê              |
| Kết hợp tốt nhất    | ML để phát hiện pattern phi tuyến → hồi quy để kiểm chứng |                                    |

---


