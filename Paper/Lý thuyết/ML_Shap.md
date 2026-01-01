

### I. Các Mô hình Học Máy Cơ bản và Mô hình Tuyến tính

#### 1. Lasso (Least Absolute Shrinkage and Selection Operator)
Lasso là một phương pháp hữu hiệu để **thu hẹp các tham số** liên quan đến các biến đồng phương sai (covariate) không đáng kể về 0.

*   **Chức năng:** Lasso hoạt động như một công cụ **co rút (shrinkage) và chọn lọc mô hình (model selection)**.
*   **Đặc điểm:** Nó tạo ra một phiên bản thưa (sparse version) của mô hình hồi quy đa biến tiêu chuẩn.
*   **Mục đích:** Lasso giúp giảm thiểu hiện tượng quá khớp (overfitting) và vấn đề đa cộng tuyến (multicollinearities) khi có một tập hợp lớn các biến dự đoán. Nó cũng được sử dụng để **chọn lọc các biến quan trọng nhất**.
*   **Bản chất:** Lasso là một mô hình **tuyến tính**.
*   **Nguyên tắc:** Phương pháp này sử dụng số hạng phạt L1: $\frac{1}{2n} \|\mathbf{y} - \mathbf{X}\beta\|_2^2 + \lambda \|\beta\|_1$. Lasso có xu hướng tạo ra một **giải pháp thưa** cho dữ liệu nhiễu hoặc chất lượng thấp.

#### 2. Generalized Additive Model (GAM)
GAM là một mô hình thuộc lớp các mô hình là biến thể của mô hình tuyến tính tiêu chuẩn.

*   **Chức năng:** GAM có thể được sử dụng để ước tính **các mối quan hệ phi tuyến tính cao** giữa các biến đồng phương sai và biến phụ thuộc bằng cách sử dụng các hàm ước tính phi tham số thích hợp (chẳng hạn như splines).
*   **Lưu ý:** GAM **không đo lường mức độ quan trọng của biến** (variable importance).

#### 3. Support Vector Machines (SVM)
SVM là một kỹ thuật học máy tiên tiến được áp dụng trong tài chính và kế toán.

*   **Ứng dụng:** SVM đã cho thấy hiệu suất ngày càng quan trọng trong **phân tích chuỗi thời gian tài chính**.

### II. Các Mô hình Dựa trên Cây và Tổ hợp (Ensemble Models)

#### 1. Random Forest (RF)
Random Forest là một trong những mô hình học máy phổ biến nhất, dựa trên cấu trúc cây quyết định.

*   **Đặc điểm:** Đây là một mô hình **phi tuyến tính, không liên tục cao**.
*   **Ưu điểm:** RF thường xuyên cho thấy **hiệu suất tốt nhất** trong việc nắm bắt các tương tác phi tuyến tính và tạo ra **các dự đoán chính xác hơn** (so với các mô hình tuyến tính).
*   **Cơ sở:** RF là thuật toán dựa trên cây quyết định (Decision trees-based).

#### 2. XGBoost (Extreme Gradient Boosting)
XGBoost là một hệ thống tăng cường cây (tree boosting system) có khả năng mở rộng.

*   **Đặc điểm:** Đây là một kỹ thuật học máy tiên tiến, được chọn vì **độ chính xác cao** và khả năng xử lý hiệu quả, nắm bắt các mẫu dữ liệu phức tạp.
*   **Ưu điểm:** XGBoost vượt trội hơn các mô hình hồi quy tuyến tính truyền thống trong việc nắm bắt **các mối quan hệ phi tuyến tính** và cải thiện độ chính xác dự đoán.

#### 3. Gradient Boosting Machine (GBM)
GBM là một thuật toán dựa trên cây được thiết kế để tìm ra bộ khớp tối ưu dựa trên hàm mất mát (loss function).

*   **Chức năng:** GBM cho phép mô hình hóa **các phi tuyến tính**.
*   **Cơ sở:** GBM được mô tả là một thuật toán **dựa trên cây tuần tự**.

### III. Các Mô hình Mạng Thần kinh (Neural Networks)

#### 1. Neural Networks (NN / NNET) / Multilayer Perceptron (MLP)
Mạng thần kinh nhân tạo (ANN hoặc NNET) là các kỹ thuật phân tích được **lấy cảm hứng từ sinh học** (tế bào thần kinh trong não người).

*   **Cấu trúc:** Mạng thần kinh bao gồm **lớp đầu vào, lớp đầu ra và nhiều lớp ẩn**.
*   **Khả năng:** NN có khả năng **mô hình hóa các hàm phi tuyến tính rất phức tạp**.
*   **MLP:** Multilayer Perceptron là một mô hình mạng thần kinh nhân tạo **kết nối đầy đủ**. MLP được coi là **"bộ xấp xỉ phổ quát" (universal approximator)** — một khái niệm lý thuyết rằng một số ANN có thể xấp xỉ bất kỳ hàm liên tục nào trong một phạm vi xác định, dẫn đến các ánh xạ dự đoán trơn tru.
*   **Đặc điểm NNET:** Trong khuôn khổ NNET, các biến dự đoán được đưa vào một lớp ẩn, lớp này biến đổi các biến dự đoán theo cách **phi tuyến tính và tương tác**.
*   **Phân bổ Trọng số:** NNET có xu hướng **phân bổ tầm quan trọng của biến một cách đồng đều hơn** so với RF, GBM và Lasso.

### IV. Các Mô hình Học Máy Nguyên nhân (Causal ML) Nâng cao

#### 1. Double/Debiased Machine Learning (DML)
DML là một phương pháp kinh tế lượng hiện đại được phát triển để ước tính **hiệu ứng nhân quả** của một biến mục tiêu.

*   **Mục đích:** DML giải quyết **thiên vị biến bị bỏ sót (omitted variable bias)** của các mô hình kinh tế lượng truyền thống.
*   **Cơ chế:** DML sử dụng **hai lần** các phương pháp học máy trong bước ước tính các hàm phiền phức (nuisance functions).
*   **Ưu điểm:** DML tạo ra một ước tính **không thiên vị, gần như phân phối chuẩn và nhất quán** cho tham số quan tâm.
*   **Khả năng:** Nó có thể kết hợp các phương pháp ML hiệu quả như GBM để tính toán **các cấu trúc phi tuyến tính** có thể có trong dữ liệu.

#### 2. Causal Forest (CF)
Causal Forest là một thuật toán được sử dụng để phân tích **tác động chi tiết (granular impact)** của một biến (ví dụ: chi phí cơ hội giữ tiền) lên một kết quả (ví dụ: tiền mặt nắm giữ).

*   **Chức năng:** Thay vì chỉ xem xét một ước tính trung bình cho toàn bộ dân số, CF cho phép điều tra **độ nhạy ở cấp độ công ty** (ước tính cá nhân hóa).
*   **Cơ sở:** Phương pháp này dựa trên ý tưởng về **hiệu ứng xử lý trung bình có điều kiện (conditional average treatment effect)**.
*   **Ứng dụng:** CF đặc biệt hữu ích để làm sáng tỏ **các phát hiện thực nghiệm mâu thuẫn**.

| Mô hình | Lớp Mô hình | Đặc điểm Nổi bật |
| :--- | :--- | :--- |
| **Lasso** | Tuyến tính/Co rút | Chọn lọc biến; Co rút tham số về 0; Tạo giải pháp thưa. |
| **MLP/NNET** | Mạng thần kinh | Mô hình phi tuyến phức tạp; "Bộ xấp xỉ phổ quát"; Sử dụng lan truyền ngược. |
| **RF** | Dựa trên cây/Ensemble | Phi tuyến tính, không liên tục cao; Thường có hiệu suất dự đoán tốt nhất. |
| **XGBoost/GBM** | Dựa trên cây/Ensemble | Hệ thống tăng cường cây có khả năng mở rộng; Nắm bắt các mối quan hệ phi tuyến tính. |
| **DML** | Học máy nhân quả | Ước tính hiệu ứng nhân quả; Giải quyết thiên vị biến bị bỏ sót; Sử dụng ML hai lần. |
| **CF** | Học máy nhân quả | Ước tính tác động chi tiết (cấp độ công ty); Phát hiện tính không đồng nhất của hiệu ứng. |

Giống như việc lắp ráp một chiếc kính hiển vi phức tạp, các mô hình học máy (ML) tiên tiến như DML hay Causal Forest không chỉ giúp chúng ta nhìn thấy bức tranh tổng thể (như hồi quy tuyến tính truyền thống) mà còn cho phép phân tích chi tiết từng hạt bụi (tác động cá nhân hóa) và loại bỏ được các vết bẩn (thiên vị do biến bị bỏ sót) để có được cái nhìn sắc nét và chính xác hơn về mối quan hệ nhân quả trong dữ liệu tài chính.

---
# Các kỹ thuật giải thích mô hình (Explainable AI - XAI)

### 1. VIP (Variable Importance in the Projection - Tầm quan trọng của biến)
VIP là một kỹ thuật cung cấp cái nhìn **tổng thể (global)** về mức độ ảnh hưởng của các đặc trưng đầu vào đối với dự đoán của mô hình.

*   **Cơ chế:** VIP định lượng đóng góp của từng tính năng dựa trên quá trình chiếu hoặc phân rã các trọng số của mô hình,. Trong các mô hình dựa trên cây (như Random Forest), tầm quan trọng thường được đo bằng mức độ giảm độ tinh khiết (impurity decrease) trung bình qua các lần chia,.
*   **Đặc điểm:** 
    *   Kết quả thường được chuẩn hóa trên thang điểm từ **0 đến 100**, trong đó 100 là biến quan trọng nhất,.
    *   Nó cho phép xác định thứ tự xếp hạng của các yếu tố quyết định (ví dụ: quy mô công ty, ROA trong dự báo giá trị doanh nghiệp),.
    *   **Hạn chế:** VIP chỉ cung cấp giá trị quan trọng chung cho toàn bộ tập dữ liệu mà không cho biết hướng tác động (tích cực hay tiêu cực) đối với từng trường hợp cụ thể.

### 2. LIME (Local Interpretable Model-agnostic Explanations)
LIME là kỹ thuật tập trung vào việc giải thích **cục bộ (local)** cho từng dự đoán đơn lẻ của mô hình.

*   **Cơ chế:** LIME tạo ra các **mô hình thay thế tuyến tính (surrogate models)** đơn giản xung quanh một điểm dữ liệu cụ thể để xấp xỉ hành vi của mô hình phức tạp tại khu vực đó.
*   **Ưu điểm:** 
    *   Rất phù hợp cho các quy trình ra quyết định mang tính cá nhân hóa hoặc theo từng thương vụ (như đầu tư vốn mạo hiểm - VC), nơi người dùng cần biết lý do cụ thể cho một kết quả duy nhất,.
    *   Có tính chất **"mô hình độc lập" (model-agnostic)**, nghĩa là có thể áp dụng cho bất kỳ thuật toán nào từ hồi quy đến mạng nơ-ron,.
*   **Hạn chế:** LIME có thể thể hiện sự **không ổn định** trong các bối cảnh dữ liệu có số chiều cao hoặc mẫu nhỏ.

### 3. SHAP (SHapley Additive exPlanations)
SHAP là một khung giải thích mạnh mẽ kết hợp cả khả năng giải thích **cục bộ và toàn cầu**.

*   **Cơ chế:** Dựa trên **lý thuyết trò chơi hợp tác (Shapley values)**, SHAP phân giải một dự đoán thành tổng các đóng góp của từng đặc trưng đầu vào,. Nó tính toán giá trị đóng góp công bằng cho mỗi biến bằng cách xem xét tất cả các tổ hợp có thể có của các biến đó.
*   **Ưu điểm vượt trội:**
    *   **Hướng và Độ lớn:** Khác với VIP, SHAP nắm bắt được cả **hướng tác động** (biến đó làm tăng hay giảm giá trị dự báo) và **độ lớn** của đóng góp đó.
    *   **Tính nhất quán:** SHAP cung cấp các đảm bảo về tính nhất quán toán học mạnh mẽ hơn so với LIME.
    *   **Phù hợp với trực giác:** Cách trình bày của SHAP thường dễ hiểu và phù hợp với cách suy luận của con người hơn,.

### So sánh tóm tắt giữa các kỹ thuật

| Tiêu chí | VIP | LIME | SHAP |
| :--- | :--- | :--- | :--- |
| **Phạm vi giải thích** | Toàn cầu (Global) | Cục bộ (Local) | Cả hai (Global & Local) |
| **Thông tin cung cấp** | Chỉ độ lớn (tầm quan trọng) | Đóng góp cục bộ của biến | Cả hướng (+/-) và độ lớn |
| **Nền tảng lý thuyết** | Trọng số mô hình/Cây chia | Mô hình thay thế tuyến tính | Lý thuyết trò chơi (Shapley) |
| **Độ ổn định** | Cao | Thấp hơn (dễ biến động) | Cao (nhất quán hơn) |

**Ví dụ tương dụ:**
Hãy tưởng tượng việc đánh giá hiệu suất của một đội bóng. **VIP** giống như việc xem bảng thống kê cả mùa giải để biết ai là cầu thủ quan trọng nhất đội. **LIME** giống như việc phân tích riêng một trận đấu cụ thể để xem vì sao cầu thủ đó chơi tốt trong 90 phút đó. Còn **SHAP** giống như một hệ thống phân tích chi tiết không chỉ cho biết ai giỏi nhất trận mà còn tính toán chính xác cầu thủ đó đã đóng góp bao nhiêu phần trăm vào bàn thắng, bao gồm cả việc chuyển hướng bóng có lợi hay có hại cho tình huống đó,.


# SHAP

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

## 🔹 3. So sánh khả năng “phát hiện phi tuyến” giữa SHAP và hồi quy truyền thống

| Đặc điểm                    | Hồi quy tuyến tính (OLS)                | Mô hình ML + SHAP                                |
| --------------------------- | --------------------------------------- | ------------------------------------------------ |
| Dạng mô hình                | Tuyến tính (βx)                         | Có thể phi tuyến (XGBoost, RF, NN)               |
| Mối quan hệ giữa X và Y     | Cố định là tuyến tính                   | Linh hoạt, có thể cong, tương tác phức tạp       |
| Phát hiện nonlinearity      | Phải thêm biến bậc hai (X², logX, v.v.) | Tự học được từ dữ liệu                           |
| Diễn giải quan hệ phi tuyến | Giới hạn                                | SHAP plot thể hiện trực tiếp                     |
| Tương tác (interaction)     | Phải thêm thủ công (X1*X2)              | SHAP interaction values có thể phát hiện tự động |



## 🔹 5. Tuy nhiên — SHAP không “biết” tuyến tính hay phi tuyến theo nghĩa thống kê
* SHAP **không kiểm định thống kê** như hồi quy (không có p-value, không có β).
* SHAP chỉ **phản ánh hình dạng thực tế của ảnh hưởng trong mô hình**.
  
👉 Vì thế, nếu bạn đang làm **nghiên cứu học thuật (academic)**, cách kết hợp hợp lý là:
1. Dùng ML + SHAP để **phát hiện dạng phi tuyến**,
2. Sau đó **kiểm chứng lại bằng hồi quy phi tuyến (chẳng hạn thêm bậc hai hoặc tương tác)** để có kết quả thống kê rõ ràng.


## 🔹 6. ✅ Kết luận tóm tắt

| So sánh             | SHAP                                                      | Hồi quy tuyến tính                 |
| ------------------- | --------------------------------------------------------- | ---------------------------------- |
| Mục tiêu            | Giải thích đóng góp biến trong mô hình ML                 | Ước lượng hệ số & ý nghĩa thống kê |
| Xử lý phi tuyến     | Rất mạnh – hiển thị dạng cong, turning point, interaction | Phải giả định sẵn dạng hàm         |
| Xử lý tuyến tính    | Tốt, thể hiện rõ ảnh hưởng đều                            | Cực kỳ rõ ràng (β tuyến tính)      |
| Diễn giải học thuật | Trực quan, nhưng không có p-value                         | Có kiểm định thống kê              |
| Kết hợp tốt nhất    | ML để phát hiện pattern phi tuyến → hồi quy để kiểm chứng |                                    |

---


