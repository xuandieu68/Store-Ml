
**Kiểm định nội sinh (Endogeneity test)** là một bước quan trọng trong kinh tế lượng nhằm xác định **biến giải thích (X)** trong mô hình hồi quy có **tương quan với sai số (ε)** hay không. Nếu có, X được gọi là **nội sinh (endogenous)** – điều này làm cho ước lượng OLS **bị chệch (biased)** và **không nhất quán (inconsistent)**.

---

# 🔍 **1. Nội sinh là gì?**

Một biến giải thích là **nội sinh** khi:

* Nó bị **bỏ sót biến quan trọng** (omitted variable bias)
* Nó **cùng chiều với sai số** (ví dụ: Y ảnh hưởng ngược lại X → quan hệ hai chiều)
* Nó bị **đo lường sai (measurement error)**
* Bị ảnh hưởng bởi **vấn đề chọn mẫu (sample selection)**


# 🧪 **2. Kiểm định nội sinh để làm gì?**

Để trả lời câu hỏi:

> **Trong mô hình hồi quy, biến X có bị nội sinh hay không? OLS có còn tin cậy không?**

Nếu **có nội sinh → cần IV/2SLS, GMM…**
Nếu **không có nội sinh → OLS vẫn dùng được.**


# 🔧 **3. Những kiểm định nội sinh phổ biến**

## **(1) Hausman Test**

Dùng để kiểm tra xem OLS (không điều chỉnh nội sinh) và IV/2SLS (điều chỉnh nội sinh) khác nhau đáng kể hay không.

* Nếu **p-value < 0.05 → biến X là nội sinh**
* Nếu **p-value > 0.05 → không có nội sinh → OLS OK**

Ý tưởng:
Nếu không nội sinh, 2SLS và OLS đều **nhất quán** → giống nhau.
Nếu nội sinh, chỉ 2SLS nhất quán → 2 cái khác nhau.

## **(2) Durbin–Wu–Hausman (DWH)**

Phiên bản mở rộng, kiểm tra thêm phần dư từ bước 1 của IV.


## **(3) kiểm định dựa trên residual inclusion**

Thêm phần dư từ hồi quy X~Z vào mô hình Y~X, nếu phần dư có ý nghĩa → X nội sinh.


# 📌 **4. Vì sao cần kiểm định nội sinh?**

Vì nội sinh **phá vỡ giả định Gauss–Markov**, dẫn đến:

### ❌ OLS không còn BLUE

### ❌ Hệ số sai → giải thích sai

### ❌ Kiểm định t, F không còn chính xác

### ❌ Kết luận chính sách bị sai

Trong nghiên cứu tài chính (BE/ME, leverage, ESG…), nội sinh gần như **luôn tồn tại**.

---

# ⭐ **5. Khi nào nội sinh đặc biệt nghiêm trọng?**

* Quan hệ hai chiều (Performance ↔ ESG)
* Biến bị đo sai (Firm value, intangible assets)
* Thiếu biến quan trọng (manager ability)
* Selection bias (survivorship bias trong stock data)

Trong mô hình ML số lớn, nội sinh vẫn **ảnh hưởng diễn giải**, dù mô hình vẫn dự đoán tốt.

--- 

# Mô hình hồi quy OLS cơ bản : 
$$Y = alpha + βX + ...+ ϵ$$

Alpha là hệ số chặn (intercept)

Beta là hệ số hồi quy (coef)

ϵ là sai số ngẫu nhiên

y là biến phụ thuộc

x là biến độc lập

1. **Hệ số hồi quy (β) trong hồi quy OLS**

Hệ số hồi quy (β) thể hiện mức độ ảnh hưởng của biến độc lập X lên biến phụ thuộc Y

*  **Hệ số dương (βi > 0)**

- Khi giá trị của Xi tăng 1 đơn vị, Y tăng trung bình βi  đơn vị (giữ nguyên các biến khác).

*  **Hệ số âm (βi<0)**

- Khi Xi tăng 1 đơn vị, Y giảm trung bình βi  đơn vị.

*  **Hệ số bằng 0**

- Biến Xi không có tác động đến Y trong mô hình.
- Nếu kiểm định thống kê (p-value) lớn hơn mức ý nghĩa (ví dụ: 0.05), ta có thể không sử dụng biến này.
- trị tuyệt đói của beta càng lớn , tác động của X đối vs Y càng cao , Nếu p-value nhỏ (thường là nhỏ hơn 0.05), có thể xác định hệ số hồi quy có ý nghĩa thống kê( đáng tin cậy ), tức là tác động của biến độc lập đó lên Y là đáng kể.

## P-value

**P-value** là một chỉ số quan trọng trong kiểm định giả thuyết thống kê, cho biết mức độ phù hợp của dữ liệu với giả thuyết gốc (null hypothesis). P-value giúp đánh giá xem kết quả thử nghiệm có đủ mạnh để bác bỏ giả thuyết không.

P-value là xác suất nhận được kết quả ít nhất cũng cực đoan như dữ liệu thực tế, giả sử giả thuyết gốc đúng. Nó được tính toán từ giá trị thống kê (ví dụ: t-statistic, F-statistic).

- **P-value nhỏ (thường là p<0.05 = 5%)**: Bác bỏ giả thuyết gốc, vì kết quả quá khác biệt so với giả thuyết gốc.
- **P-value lớn (thường là p≥0.05 )**: Không bác bỏ giả thuyết gốc, vì kết quả không đủ mạnh để chứng minh sự khác biệt.

**Kiểm định giả thuyết trong hồi quy OLS**

- **Giả thuyết gốc (Null hypothesis)**: H0: βi=0 (Biến độc lập không có tác động đến biến phụ thuộc).
- **Giả thuyết thay thế (Alternative hypothesis)**: H1: βi≠0 (Biến độc lập có tác động đến biến phụ thuộc).

*  Nếu p nhỏ hơn mức ý nghĩa (ví dụ: 0.05), bác bỏ H0 và kết luận rằng biến độc lập có tác động đáng kể.

*  Nếu p lớn hơn mức ý nghĩa, không bác bỏ H0  và kết luận rằng không có bằng chứng đủ mạnh để nói rằng biến độc lập có tác động đến biến phụ thuộc.

*  **Khi p-value < 0.01**: Bác bỏ giả thuyết gốc với mức độ tin cậy 99%. Có đủ bằng chứng để kết luận rằng biến độc lập có ảnh hưởng đáng kể đến biến phụ thuộc.

*  **Khi p-value ≥ 0.01**: Không bác bỏ giả thuyết gốc. Không có đủ bằng chứng để kết luận rằng biến độc lập có ảnh hưởng đáng kể.

| **Mức ý nghĩa (α)** | **p-value < α  (Bác bỏ H0)** | **p-value ≥ α Không bác bỏ H0** |
| --- | --- | --- |
| **0.01** | Bác bỏ H0  với mức độ tin cậy 99% | Không bác bỏ H0H_0H0 (có thể có lỗi loại II) |
| **0.05** | Bác bỏ Ho với mức độ tin cậy 95% | Không bác bỏ H0H_0H0 |
| **0.10** | Bác bỏ Hovới mức độ tin cậy 90% | Không bác bỏ H0H_0H0 |

## Hệ số xác định R^2 và Adj R^2

**R2 (R-squared)**: Đo lường mức độ mà mô hình giải thích được biến động của biến phụ thuộc. cho biết mức độ phù hợp của mô hình với dữ liệu.

*  SSresidual là tổng bình phương sai số (residual sum of squares), đo lường sự chênh lệch giữa giá trị thực tế và giá trị dự đoán của mô hình.

*  SStotal là tổng bình phương tổng thể (total sum of squares), đo lường sự chênh lệch giữa giá trị thực tế và giá trị trung bình của biến phụ thuộc.

Ví dụ: Nếu R^2=0.80 , điều này có nghĩa là 80% sự biến động của biến phụ thuộc có thể được giải thích bởi mô hình, còn lại 20% là do yếu tố khác ngoài mô hình.

**R2 điều chỉnh**: Điều chỉnh R2 để tránh bị ảnh hưởng bởi số lượng biến độc lập. Có ý nghĩa hơn R^2 khi so sánh mô hình có số biến độc lập khác nhau.

- n là số quan sát (số mẫu).
- ppp là số lượng biến độc lập trong mô hình.
- R^2 là hệ số xác định (đã tính toán từ mô hình).

*  adj-**R2** có thể giảm nếu mô hình có nhiều biến độc lập không giải thích được sự biến động của biến phụ thuộc.

*  adj-**R^2**  là một cách điều chỉnh R^2 sao cho bạn có thể đánh giá được sự phù hợp của mô hình, đặc biệt là khi bạn làm việc với mô hình có nhiều biến độc lập.

Ex : Nếu mô hình có 3 biến độc lập và R2=0.80 , nhưng khi thêm một biến không có ý nghĩa vào mô hình, adj-R^2  có thể giảm để phản ánh sự thay đổi không phù hợp với mô hình.

**📌 Phân tích kết quả của mô hình Panel OLS (Fixed Effects)**

1. **R-squared (Hệ số xác định)**

| **Chỉ số** | **Ý nghĩa** |
| --- | --- |
| **R-squared (0.0004)** | Phần trăm biến động của Z_Score được giải thích bởi ESG_Score và các biến kiểm soát. **Giá trị rất nhỏ** → Mô hình có thể chưa giải thích được nhiều. |
| **R-squared (Within) (0.0004)** | Đo lường mức độ giải thích biến động **trong cùng một thực thể (firm)** theo thời gian. |
| **R-squared (Between) (-0.0024)** | Đo lường mức độ giải thích **khác biệt giữa các thực thể (firm)**. Giá trị âm → Có thể biến ESG_Score không có ảnh hưởng đáng kể giữa các công ty. |
| **R-squared (Overall) (0.0021)** | Tổng mức độ giải thích của mô hình cho tất cả dữ liệu. |
- Tất cả các R-squared đều **rất nhỏ**, điều này cho thấy mô hình có thể không giải thích tốt sự biến động của Z_Score.
- Có thể cần xem lại biến độc lập hoặc thêm biến kiểm soát khác để cải thiện mô hình

**🔹 2. Số lượng quan sát & thực thể**

| **Chỉ số** | **Ý nghĩa** |
| --- | --- |
| **No. Observations: 8392** | Tổng số dòng dữ liệu được sử dụng trong mô hình. |
| **Entities: 1135** | Số lượng công ty khác nhau trong dữ liệu. |
| **Avg Obs per entity: 7.3938** | Trung bình mỗi công ty có khoảng 7.39 quan sát. |
| **Time periods: 11** | Dữ liệu trải dài trong 11 năm. |
| **Min/Max Obs per entity: 1 - 11** | Có công ty chỉ có 1 quan sát, có công ty có đủ 11 năm dữ liệu. |
- Một số công ty chỉ có **1 quan sát** → Cần kiểm tra có bị thiếu dữ liệu không.
- Trung bình mỗi công ty có **~7 quan sát trên tổng số 11 năm** → Có thể không phải công ty nào cũng báo cáo đầy đủ.

**🔹 4. Kiểm định ý nghĩa mô hình**

| **Chỉ số** | **Giá trị** | **Ý nghĩa** |
| --- | --- | --- |
| **F-statistic** | 3.0005 | Kiểm tra xem các biến có tác động tổng thể hay không. |
| **P-value của F-statistic** | 0.0833 | Nếu p < 0.05, mô hình có ý nghĩa. Ở đây, p > 0.05 → Mô hình chưa đủ mạnh. |
| **Log-likelihood** | -5912.1 | Giá trị hàm hợp lý (càng cao càng tốt). |
| **F-test for Poolability** | 28.894 | Kiểm tra xem có nên dùng Fixed Effects không. |
| **P-value của Poolability** | **0.0000** | P-value nhỏ → Cần dùng Fixed Effects thay vì OLS. |
- **P-value của F-test = 0.0833** → Mô hình có **một số ảnh hưởng**, nhưng chưa đủ mạnh.
- **F-test for Poolability có p-value = 0.0000** → **Chứng minh rằng Fixed Effects là cần thiết!**
- **Nên thử thêm các biến kiểm soát hoặc cách tiếp cận khác (GMM, Random Effects, Robust Estimator)** để có kết quả chính xác hơn.

## **T-value (giá trị t)**

là một thống kê quan trọng trong hồi quy tuyến tính và kiểm định giả thuyết, dùng để đánh giá xem **một hệ số hồi quy (β) có khác biệt có ý nghĩa thống kê với 0 hay không**.

---

### 📌 **Ý nghĩa của T-value**

T-value =

![image.png](attachment:d90dcbfc-4bbb-4414-975b-1f66c3837d73:image.png)

---

### ✅ **Diễn giải**

- **|T| càng lớn → khả năng hệ số đó có ý nghĩa thống kê càng cao.**
- Nếu T-value vượt qua ngưỡng tới hạn (từ bảng t Student, theo mức ý nghĩa α và bậc tự do), ta **bác bỏ H₀ (giả thuyết hệ số = 0)**.

---

### 📊 **Mối liên hệ với P-value**

- **T-value càng lớn ⇒ P-value càng nhỏ.**
- Nếu P-value < 0.05 (ở mức ý nghĩa 5%) → **kết luận rằng hệ số có ý nghĩa thống kê** (có ảnh hưởng thực sự).

## **Correlation Matrix**

1. (Ma trận tương quan) là một bảng (matrix) cho thấy mức độ tương quan giữa các cặp biến trong một tập dữ liệu. Mỗi phần tử trong ma trận tương quan thể hiện hệ số tương quan (correlation coefficient) giữa hai biến.

Công thức phổ biến để tính hệ số tương quan là **Pearson correlation coefficient** (hệ số tương quan Pearson), có giá trị từ -1 đến 1:

- **1**: Mối quan hệ hoàn toàn đồng biến (positive correlation)., càng gần 1 càng dễ xảy ra vấn đề đa cộng tuyến (multicollinearity)
- **0**: Không có mối quan hệ (no correlation).
- **1**: Mối quan hệ hoàn toàn nghịch biến (negative correlation).

**상관행렬**은 변수 간 Pearson 상관계수를 행렬 형태로 보여주는 도표로, 다음을 나타냅니다:

- +1: 완전한 양의 상관관계
- 1: 완전한 음의 상관관계
- 0: 상관 없음

> 상관계수(Pearson's r)는 선형 관계의 강도와 방향을 측정합니다.
> 

| 상관계수 (r) | 해석 |
| --- | --- |
| 0.0 ~ ±0.1 | 거의 무시해도 될 수준 |
| ±0.1 ~ ±0.3 | 약한 상관 |
| ±0.3 ~ ±0.5 | 중간 정도 상관 |
| ±0.5 ~ ±0.7 | 강한 상관 |
| ±0.7 ~ 1.0 | 매우 강한 상관 (다중공선성 의심) |

## **VIF (Variance Inflation Factor)**

: Đo lường mức độ tăng độ biến thiên của ước lượng hệ số hồi quy do đa cộng tuyến. VIF cao cho thấy một biến độc lập có thể bị phụ thuộc quá mức vào các biến độc lập khác, điều này có thể làm giảm tính đáng tin cậy của các ước lượng trong mô hình

VIF"는 **Variance Inflation Factor (분산 팽창 계수)**의 약자로, **다중공선성(multicollinearity)**을 진단하는 데 사용하는 대표적인 통계 지표입니다.

---

### 🔍 VIF (Variance Inflation Factor)란?

**VIF는 하나의 독립변수가 다른 독립변수들과 얼마나 상관되어 있는지를 측정**합니다. 쉽게 말해, 회귀모형 내에서 독립변수들 간의 **중복성** 또는 **상관관계**가 높을수록 VIF 값이 커집니다.

---

### 📐 수식

![image.png](attachment:ec25fda2-7876-4e7d-be02-fd5b25255e28:image.png)

---

### 🔢 VIF 해석 기준

| VIF 값 범위 | 해석 |  |
| --- | --- | --- |
| 1 | 전혀 다중공선성이 없음 |  |
| 1 ~ 5 | 허용 가능한 수준의 다중공선성 |  |
| 5 ~ 10 | 다중공선성 우려 있음 (주의 필요) |  |
| > 10 | 심각한 다중공선성 (모형 재설계 고려) |  |

---
Skewness
---

Độ lệch chuẩn (skewness) cho biết mức độ không đối xứng của phân phối dữ liệu. Khi giá trị của độ lệch chuẩn quá lớn, có thể có một số vấn đề cần lưu ý:

1. **Lệch phân phối (Skewness cao)**:

   * **Skewness dương** (độ lệch chuẩn > 0): Điều này có nghĩa là phân phối dữ liệu bị lệch về phía bên phải, với một đuôi dài ở phía bên phải. Dữ liệu có thể có nhiều giá trị nhỏ nhưng có vài giá trị cực lớn (outliers). Điều này có thể gây khó khăn trong việc phân tích và mô hình hóa vì mô hình có thể bị "vượt qua" bởi các giá trị cực lớn.
   * **Skewness âm** (độ lệch chuẩn < 0): Điều này có nghĩa là phân phối dữ liệu bị lệch về phía bên trái, với một đuôi dài ở phía bên trái. Dữ liệu có thể có nhiều giá trị lớn nhưng có vài giá trị cực nhỏ (outliers).

2. **Vấn đề trong phân tích và mô hình hóa**:

   * **Dữ liệu lệch có thể ảnh hưởng đến kết quả phân tích thống kê**. Nhiều phương pháp thống kê giả định rằng dữ liệu có phân phối chuẩn (hoặc gần chuẩn). Khi độ lệch chuẩn quá lớn, phân phối dữ liệu có thể không tuân theo giả định này, dẫn đến các kết quả không chính xác.
   * **Giới hạn trong việc áp dụng các mô hình học máy**: Các mô hình như hồi quy tuyến tính hoặc các thuật toán học máy yêu cầu dữ liệu gần với phân phối chuẩn. Khi có độ lệch lớn, mô hình có thể không hoạt động tốt hoặc cần phải thực hiện chuyển đổi dữ liệu như chuẩn hóa hoặc log transformation.

3. **Cần xử lý**:

   * **Chuyển đổi dữ liệu**: Bạn có thể áp dụng các phép biến đổi như logarithmic transformation (`log`), square root transformation (`sqrt`), hoặc Box-Cox transformation để làm giảm độ lệch và đưa dữ liệu gần hơn với phân phối chuẩn.
   * **Xử lý outliers**: Nếu độ lệch chuẩn quá lớn là do sự hiện diện của các giá trị ngoại lai (outliers), bạn có thể cân nhắc loại bỏ hoặc xử lý các giá trị này để cải thiện phân phối của dữ liệu.
   * **Sử dụng mô hình robust**: Nếu bạn không thể xử lý độ lệch chuẩn, bạn có thể chuyển sang các mô hình ít nhạy cảm với dữ liệu lệch như mô hình hồi quy robust hoặc các thuật toán học máy không yêu cầu phân phối chuẩn.
---

