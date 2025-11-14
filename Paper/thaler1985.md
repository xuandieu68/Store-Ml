
### I. Cơ sở Lý thuyết và Quan sát

#### 1. Hành vi Cá nhân và Quy tắc Bayes
Nghiên cứu trong tâm lý học thực nghiệm chỉ ra rằng hầu hết mọi người có xu hướng vi phạm quy tắc Bayes khi sửa đổi niềm tin của mình. Cụ thể, các cá nhân có xu hướng **đánh giá quá cao thông tin gần đây** và **đánh giá thấp dữ liệu cơ sở (prior or base rate)**. Hành vi này là một ví dụ của *representativeness heuristic* (nguyên tắc đại diện). Phản ứng thái quá được so sánh ngầm với mức độ phản ứng được coi là phù hợp, thường được quy định bởi quy tắc Bayes trong các vấn đề sửa đổi xác suất.

#### 2. Quan sát Thị trường Lịch sử
Khái niệm về sự phản ứng thái quá trên thị trường đã được quan sát từ sớm:
*   **J. M. Keynes** nhận xét rằng những biến động hàng ngày trong lợi nhuận của các khoản đầu tư hiện tại, mặc dù có tính chất phù du và không đáng kể, lại có **ảnh hưởng quá mức, thậm chí phi lý, đối với thị trường**.
*   **Williams** lưu ý rằng giá cả quá phụ thuộc vào khả năng kiếm tiền hiện tại và quá ít vào khả năng chi trả cổ tức dài hạn.
*   **Arrow** kết luận rằng công trình của Kahneman và Tversky "đặc trưng hóa rất chính xác phản ứng thái quá đối với thông tin hiện tại" trong các thị trường chứng khoán và hợp đồng tương lai.

Phản ứng thái quá có thể liên quan đến các vấn đề tài chính khác như **biến động giá chứng khoán quá mức (excess volatility)** (Shiller) và **sự bất thường của tỷ lệ Giá/Thu nhập (P/E anomaly)**. Một giải thích hành vi thay thế cho sự bất thường của P/E là **giả thuyết tỷ lệ giá (price-ratio hypothesis)**: các công ty có P/E rất thấp bị coi là *tạm thời bị định giá thấp* do nhà đầu tư quá bi quan sau chuỗi báo cáo lợi nhuận xấu, và ngược lại, các công ty có P/E rất cao bị *định giá quá cao*.

### II. Kiểm định Thực nghiệm

#### 1. Giả thuyết Phản ứng Thái quá
Nếu giá cổ phiếu có xu hướng vượt quá mức (overshoot) một cách có hệ thống, thì sự đảo chiều của chúng phải có thể dự đoán được chỉ dựa vào dữ liệu lợi nhuận trong quá khứ. Nghiên cứu đề xuất hai giả thuyết chính, cả hai đều ngụ ý một sự **vi phạm hiệu quả thị trường dạng yếu (weak-form market efficiency)**:
1.  Các biến động cực đoan về giá cổ phiếu sẽ được theo sau bởi các biến động giá tiếp theo theo hướng ngược lại.
2.  Biến động giá ban đầu càng cực đoan, sự điều chỉnh tiếp theo sẽ càng lớn.

### Method (Phương pháp)

#### 1. Thiết kế Kiểm tra (Empirical Tests)
Quy trình kiểm tra là một biến thể của thiết kế ban đầu của Beaver và Landsman. Điểm khác biệt là nghiên cứu này kiểm tra mức độ mà hành vi lợi nhuận phi zero có hệ thống *sau* khi thành lập danh mục (t > 0) liên quan đến lợi nhuận phi zero có hệ thống trong giai đoạn *trước* khi thành lập danh mục (t < 0).

#### 2. Định hình Danh mục (Portfolio Formation)
*   **Cơ sở hình thành:** Danh mục được hình thành dựa trên **lợi nhuận vượt trội trong quá khứ** (past excess returns), chứ không phải dựa trên biến thông tin do công ty tạo ra như lợi nhuận (earnings).
*   **Phân loại:** Các danh mục **"Người thắng" (Winner, W)** và **"Người thua" (Loser, L)** được tạo thành dựa trên lợi nhuận vượt trội tích lũy ($\text{CU}_j$) trong các giai đoạn trước đó.
    *   Ví dụ điển hình: Sử dụng 16 giai đoạn ba năm không chồng chéo. Các công ty nằm trong 35 cổ phiếu đứng đầu (hoặc decile trên cùng) về $\text{CU}_j$ được gán vào danh mục W; 35 cổ phiếu dưới cùng được gán vào danh mục L.
*   **Thời gian:**
    *   **Giai đoạn Hình thành Danh mục (Formation Period):** Lên đến 5 năm, với giai đoạn chuẩn là **36 tháng** (từ tháng 49 đến 84).
    *   **Giai đoạn Kiểm tra (Test Period):** **36 tháng** sau khi thành lập danh mục (từ t = 1 đến t = 36).
#### 3. Phương pháp Tính toán Lợi nhuận Vượt trội (Residuals)
Nghiên cứu dựa trên ba loại lợi nhuận vượt trội (residuals): lợi nhuận vượt trội điều chỉnh theo thị trường (market-adjusted excess returns), residuals mô hình thị trường (market model residuals), và lợi nhuận vượt trội so với mô hình CAPM của Sharpe-Lintner.

*   **Phương pháp được Báo cáo:** Nghiên cứu chủ yếu báo cáo kết quả dựa trên **lợi nhuận vượt trội đã điều chỉnh theo thị trường** ($\mathbf{U_{jt} = R_{jt} - R_{mt}}$).
*   **Lý do lựa chọn:** Việc sử dụng lợi nhuận vượt trội điều chỉnh theo thị trường chỉ điều chỉnh rủi ro theo chuyển động chung của thị trường và được cho là có xu hướng **thiên vị thiết kế nghiên cứu ngược lại với giả thuyết phản ứng thái quá**.
*   **Tính toán CAR:** Lợi nhuận vượt trội trung bình tích lũy $\text{ACAR}_{W,t}$ và $\text{ACAR}_{L,t}$ được tính toán cho danh mục W và L trong suốt giai đoạn kiểm tra.


### III. Kết quả Thực nghiệm Chính

#### 1. Bằng chứng về Sự đảo chiều Giá
*   Trong nửa thế kỷ qua, 36 tháng sau khi hình thành danh mục (dựa trên giai đoạn hình thành 3 năm), **danh mục người thua** (35 cổ phiếu) vượt trội so với thị trường trung bình là **19.6%**.
*   Ngược lại, **danh mục người thắng** kiếm được ít hơn thị trường khoảng **5.0%**.
*   Sự khác biệt về lợi nhuận vượt trội tích lũy giữa hai danh mục cực đoan, ($\text{ACAR}_{L,36} - \text{ACAR}_{W,36}$), là **24.6%** (với t-statistic là 2.20).
*   **Tính bất đối xứng:** Hiệu ứng phản ứng thái quá lớn hơn nhiều đối với nhóm người thua so với nhóm người thắng.
*   **Tính cực đoan:** Kết quả khẳng định giả thuyết rằng biến động ban đầu càng lớn thì sự điều chỉnh giá sau đó càng rõ rệt. Khi giai đoạn hình thành danh mục được kéo dài (từ một lên ba hoặc năm năm), sự đảo chiều giá sau đó càng lớn. Đối với giai đoạn hình thành chỉ một năm, không thấy có sự đảo chiều nào.
*   Hiện tượng này chủ yếu xảy ra trong năm thứ hai và thứ ba của giai đoạn kiểm tra, phù hợp với tuyên bố của Benjamin Graham.

#### 2. Hiệu ứng Tháng Giêng (January Effect)
Một khía cạnh đáng chú ý của kết quả là hầu hết lợi nhuận vượt trội được thực hiện vào tháng Giêng.
*   Danh mục người thua kiếm được lợi nhuận vượt trội đặc biệt lớn vào các tháng $t=1, t=13$, và $t=25$ (lần lượt là 8.1%, 5.6%, và 4.0%).
*   Điều đáng ngạc nhiên là hiệu ứng Tháng Giêng này vẫn được quan sát thấy **muộn nhất là năm năm sau khi hình thành danh mục**.
*   Hiệu ứng Tháng Giêng cực kỳ lớn, tích cực, kiếm được bởi danh mục người thua là một khía cạnh vẫn chưa có lời giải thích thỏa đáng. Hiện tượng này đặt ra những câu hỏi mới đối với giả thuyết bán cổ phiếu để giảm thuế (tax-loss selling hypothesis).


### Main Results and Implications (Kết quả Chính và Hàm ý)

#### 1. Kết quả Chính: Bằng chứng về Phản ứng Thái quá và Đảo chiều Giá
Kết quả thực nghiệm **nhất quán** với giả thuyết phản ứng thái quá.
*   **Lợi nhuận Chênh lệch:** 36 tháng sau khi thành lập danh mục (dựa trên giai đoạn hình thành 3 năm), sự khác biệt trong lợi nhuận vượt trội tích lũy trung bình giữa hai danh mục cực đoan, $\mathbf{[ACAR_{L,36} - ACAR_{W,36}]}$, là **24.6%** (với t-statistic là 2.20).
    *   **Danh mục Người thua (L):** Vượt trội thị trường trung bình **19.6%**.
    *   **Danh mục Người thắng (W):** Kiếm được ít hơn thị trường khoảng **5.0%**.
*   **Thiếu hiệu quả Thị trường:** Sự khác biệt 24.6% này cho thấy **sự thiếu hiệu quả thị trường dạng yếu đáng kể (Substantial weak-form market inefficiencies)**.
*   **Tính Bất đối xứng (Asymmetry):** Hiệu ứng phản ứng thái quá **lớn hơn nhiều đối với nhóm người thua** so với nhóm người thắng.
*   **Mức độ cực đoan:** Kết quả khẳng định giả thuyết rằng biến động ban đầu càng lớn, sự điều chỉnh giá sau đó càng rõ rệt. Ví dụ, khi giai đoạn hình thành danh mục tăng từ một lên ba hoặc năm năm, lợi nhuận đảo chiều sau đó càng lớn; không có sự đảo chiều nào được quan sát đối với giai đoạn hình thành chỉ một năm.
*   **Thời gian xuất hiện:** Hiện tượng phản ứng thái quá chủ yếu xảy ra trong **năm thứ hai và thứ ba** của giai đoạn kiểm tra, phù hợp với tuyên bố của Benjamin Graham.

#### 2. Vấn đề Rủi ro (Risk Issue)
*   **Phân tích Beta:** Danh mục người thắng có **beta trung bình lớn hơn đáng kể** so với danh mục người thua (ví dụ: 1.369 so với 1.026).
*   **Hàm ý:** Điều này có nghĩa là, nếu mô hình CAPM là chính xác, **danh mục người thua không chỉ vượt trội hơn danh mục người thắng mà còn ít rủi ro hơn đáng kể**. Việc sử dụng lợi nhuận vượt trội điều chỉnh theo thị trường có xu hướng **đánh giá thấp** cả quy mô và ý nghĩa thống kê của hiệu ứng phản ứng thái quá.

#### 3. Hiệu ứng Tháng Giêng (January Effect)
*   **Lợi nhuận tập trung:** Hầu hết lợi nhuận vượt trội được thực hiện vào **Tháng Giêng**.
*   **Đặc điểm của Losers:** Danh mục người thua kiếm được lợi nhuận vượt trội **cực kỳ lớn** vào các tháng $t=1, t=13$, và $t=25$ (lần lượt là 8.1%, 5.6%, và 4.0%).
*   **Thời gian kéo dài:** Điều đáng ngạc nhiên là hiệu ứng Tháng Giêng này vẫn được quan sát thấy **muộn nhất là năm năm sau khi thành lập danh mục**.
*   **Mối liên hệ với Tax-Loss Selling:** Danh mục người thua có xu hướng giảm giá (so với thị trường) giữa tháng 10 và tháng 12, phù hợp với giả thuyết bán cổ phiếu để giảm thuế (tax-loss selling hypothesis). Tuy nhiên, việc hiệu ứng Tháng Giêng vẫn xuất hiện sau nhiều năm đặt ra những câu hỏi mới đối với giả thuyết này.

#### 4. Hàm ý đối với các Bất thường khác
*   **Hiệu ứng Công ty Nhỏ (Small Firm Effect):** Kết quả củng cố quan điểm rằng hiệu ứng công ty nhỏ có thể được định nghĩa lại là **"hiệu ứng công ty thua lỗ" (losing firm effect) vào thời điểm giao năm**, mặc dù các công ty trong danh mục cực đoan không khác biệt về vốn hóa thị trường.
*   **Hiệu ứng P/E:** Kết quả hỗ trợ **giả thuyết tỷ lệ giá**, ngụ ý rằng hiệu ứng P/E cũng chủ yếu là một hiện tượng Tháng Giêng, mặc dù tại thời điểm nghiên cứu chưa có bằng chứng trực tiếp xác nhận điều này.


### Main Variables (Biến số Chính)

| Biến số | Mô tả |
| :--- | :--- |
| $\mathbf{R_{jt}}$ | Lợi nhuận của chứng khoán $j$ tại thời điểm $t$. |
| $\mathbf{R_{mt}}$ | Lợi nhuận của chỉ số thị trường (equally weighted arithmetic average rate of return on all CRSP listed securities). |
| $\mathbf{U_{jt}}$ | Lợi nhuận vượt trội (Residual return) của chứng khoán $j$ tại $t$, tính bằng $\mathbf{R_{jt} - R_{mt}}$ (market-adjusted excess returns). |
| $\mathbf{CU_j}$ | Lợi nhuận vượt trội tích lũy (Cumulative excess returns) của cổ phiếu $j$ trong giai đoạn hình thành danh mục. |
| $\mathbf{ACAR_{W,t}}$ | Lợi nhuận vượt trội trung bình tích lũy (Average Cumulative Average Residuals) của danh mục Người thắng tại tháng $t$ trong giai đoạn kiểm tra. |
| $\mathbf{ACAR_{L,t}}$ | Lợi nhuận vượt trội trung bình tích lũy của danh mục Người thua tại tháng $t$ trong giai đoạn kiểm tra. |
| $\mathbf{\beta}$ (Beta) | Hệ số rủi ro CAPM của danh mục (được ước tính nhưng không phải là biến chính trong công thức tính $\text{U}_{jt}$ được báo cáo). |


#
* Nghiên cứu này đưa ra kết luận rằng beta của doanh nghiệp nhỏ càng nhỏ hơn , tức là rủi ro càng ít hơn, thị trường chứng tỏ ít hiệu quả hơn , ngược lại với nhận định thj trường hiệu quả, cho thấy lợi nhuận cao hơn không phải là sự bù đắp cho rủi ro hệ thống (systematic risk).
* 
