# Mean reversion in stock price 
---
# 1. Introduction
* **Importance:** The extent to which stock prices exhibit regressive mean behavior is important for evaluating asset pricing assumptions. If the market price and the fundamental value differ but are then adjusted, the stock price will return to the mean.. This implies that returns must have negative serial correlation at a certain frequency if “erroneous” market movements are to eventually be corrected..
* **Research Problem:** This study examines whether prices regress to the mean using data from the United States and 17 other countries. The researchers note that previous randomized tests were less likely to detect sustained deviations between market prices and fundamental values..
* **Preliminary finding:** Significant temporary components in stock prices are needed to explain these correlations, although temporary, cyclical changes in required returns or valuation bubbles may also contribute.
---

# 2. Methodological issues involved in testing for transitory compornent
## 2.1  Test methods 
*  **Autocorrelations** : little power
*  **Variance-Ratio Tests**: considered to be close to the strongest tests of the market efficiency hypothesis with constant required returns, compared to plausible alternative hypotheses such as the "fads" model.
* **Limitations of the Test**: Although powerful, these tests still have low power, even with 60 years of monthly data. 
* **Regression Tests:** Serial correlation analysis of multi-period returns. These tests may reject the hypothesis of serial independence of returns more strongly than the variance proportion test depending on the nature of the data..
* **Parametric Time-Series Models:** Includes **likelihood-ratio** tests. Even these strongest possible tests have little power to distinguish the random walk model from alternative models that imply temporary, but highly persistent, price components
## 2.2. Power calculations
The paper evaluates different statistical tests for temporary price components
*  **Model:** The paper uses a model that assumes that the logarithm of stock prices including the permanent component and transient components 
​
## 2.3 Evaluation 
![Ảnh chụp màn hình_13-10-2025_205828_](https://github.com/user-attachments/assets/3958fbda-0a11-4256-b958-969546a4d563)

* $\theta = 0.25$: One-quarter of the return variance comes from the temporary component.
* $\theta = 0.75$: Three-quarters of the return variance comes from the temporary component
* All tests use a significance level of 0.05 (size 0.05)

* **Recommendation:** A reasonable balance between Type I and Type II errors suggests using critical values ​​above the usual 0.05 level

---

# 3. Statistical Evidence on Regression Means
Section 3 uses the variance ratio test to analyze the degree of regression to the mean in stock prices across four main data sets

## 3.1  NYSE Monthly Returns (1926-1985)
Table 2 presents the Variance Ratios (VR) statistics for the NYSE's real returns and excess returns, calculated over different horizons (from 1 month to 96 months)
* Short-Term Serial Correlation: The VRs at the short horizon (1 month) are less than 1 (0.764 and 0.785), implying a positive serial correlation in monthly returns
 * Long-Term Series Correlation: VR declines sharply at longer horizons (especially after 60 months), indicating negative series correlation.
* The regression average is more pronounced for equal-weighted returns than for value-weighted returns.
*  The null hypothesis of serial independence is rejected at the 0.08 level for value-weighted real returns and at the 0.005 level for equally weighted excess returns
---

## 3.2 US Historical Data (1871-1985)
Table 3 extends the analysis using longer historical data (from 1871) based on the Standard and Poor's–Cowles index
* For the period before 1925, excess returns show negative serial correlation at long horizons,  indicating greater evidence of regression to the mean than for the post-1926 data.
* For the entire 1871-1985 period, both real and excess returns show negative serial correlation at long lags, but the evidence for regression averaging is weaker than for monthly CRSP data after 1925
  
## 3.3 Equity Markets outside the United States
next  presents Variance ratios for seventeen international stock markets, allowing for a robustness check of regression to the mean.
*  Study of data from Canada (since 1919), Britain (since 1939) and 15 other countries after World War II.
*  Most countries show negative serial correlations at long horizons and positive serial correlations at short horizons.
* The similarity of the results across countries reinforces the finding of significant temporary price components.
  
## 3.4 Individual Company Data (United States, post-1926)

* The results for Individual Company Data set show some long-run regression averages for individual stock prices relative to the general market or a risk-free asset.
* However, temporary factors account for a smaller portion of the relative return variation of individual stocks than of the overall market.
  
---
 
# 4. The Practical Importance of Temporary Components in Stock Prices
* This section assesses the substantive significance of the regression to the mean by decomposing the return variance into permanent and temporary components
* Estimate the standard deviation and the contribution of the temporary component to the monthly return variance.
* The temporary component can account for 65.77% to 99% of the variance in evenly balanced monthly returns, depending on the persistence assumption.
• The temporary component has a large annual standard deviation (up to 21.6% for the value-weighted return and 37.7% for the uniformly weighted return).
* This result confirms Shiller's (1981) conclusion that models assuming constant expected returns cannot explain all the variance in stock market returns.
---
  
# 5. The Origin of the Temporary(transitory) Component in Stock Prices
* Section 5 discusses whether the volatility in ex ante returns (implied by the temporary component) is better explained by changes in interest rates/risk volatility or is a by-product of noise trading.
* **Two views:** The central issue is whether the variation in expected returns is better explained by changes in interest rates and market volatility, or is a by-product of noise trading activity.
* **Difficulty in explaining by interest rate changes:**
    - **Large volatility:** There needs to be significant volatility in the required rate of return to explain the price regression meanFor example, to explain price "fads" with a standard deviation of 20%, the standard deviation of expected returns must be 5.8% per year, even if return shocks require a half-life of 2.9 years.. These estimates are very large compared to average excess returns and are difficult to explain by known risk factors..
    - **Positive then negative serial correlation:** First-order autoregressive temporary components models cannot explain both positive serial correlation at short lags and negative serial correlation at long lags. The data show no support for the hypothesis of a positive correlation between required return shocks and expected dividends..
* **Possible explanation:** Noise trading – that is, investors whose demand for securities is considered exogenous, not the result of maximizing a normal utility function using rational expectations about the distribution of returns – has been proposed as an explanation for the temporary components in stock prices . Researchers argue that noisy trading patterns can create positive, then negative, auto-correlation in expected returns.

---

# 6. Conclusion
* **Key Findings:** Stock returns show positive serial correlation over short periods and negative correlation over longer periods , confirmed by various data sets.
* **Importance:** Point estimates show that temporary price components account for a significant portion of return variance.
* **Implications for financial practice:**
    - For long-term investors, the stock market may be less risky than expected from the random walk model.
    - Recommend investment strategies, such as buying recently devalued securities (according to DeBondt and Thaler).
    - It may be justified for organizations to spend based on a weighted average of past assets rather than current market value.
* **Future research directions:**
*  There is a need to develop and test theories of noise trading, as well as risk-variance factors, to explain the characteristic autocorrelation pattern of returns.
*  This may require information beyond stock returns, such as data on fundamental value, proxies for noise trading (e.g., retail investor trading, trading volume), and indicators of risk factors (e.g., expected volatility from stock options).


---
# Menthods

### 1. Phương pháp Kiểm định Tỷ lệ Phương sai (Variance-Ratio Test)

Kiểm định tỷ lệ phương sai khai thác thực tế là nếu logarit của giá cổ phiếu đi theo một bước ngẫu nhiên (random walk), thì phương sai lợi suất sẽ tỷ lệ thuận với chân trời lợi suất (return horizon).

Công thức thống kê tỷ lệ phương sai cho lợi suất hàng tháng, so sánh sự biến thiên của lợi suất ở chân trời $k$ với sự biến thiên trong khoảng thời gian một năm (12 tháng), là:

$$\mathbf{V R(k)} = \frac{\sigma_{k}^{2}/k}{\sigma_{1}^{2}/12} \quad \text{(1)}$$

Trong đó:
*   $\sigma_{k}^{2} \equiv E R_{k t}^{2}$.
*   $R_{k t} \equiv \sum_{i=0}^{k-1} R_{t-i}$.
*   $R_t$ là tổng lợi suất trong tháng $t$.
*   Thống kê này hội tụ về 1 nếu lợi suất không tương quan theo thời gian.
*   Nếu một phần biến động giá là do các yếu tố nhất thời (transitory factors), tỷ lệ phương sai sẽ nhỏ hơn một.

Tỷ lệ phương sai cũng liên quan chặt chẽ với các kiểm định dựa trên tự tương quan (autocorrelations) ước tính.

### 2. Phương pháp Kiểm định Hồi quy (Regression Tests)

Phương pháp này, được sử dụng bởi Fama và French (1988b), hồi quy lợi suất đa kỳ hạn dựa trên lợi suất đa kỳ hạn trễ.

Nếu $\tilde{R}_k$ biểu thị lợi suất $k$-kỳ hạn đã loại trừ giá trị trung bình (de-meaned k-period return), thì hệ số hồi quy ($\beta_k$) là:

$$\boldsymbol{\beta_{k}} = \frac{\sum_{t=2 k}^{T} \tilde{R}_{t} \tilde{R}_{t-k}}{\sum_{t=k+1}^{T} \tilde{R}_{t-k}^{2}} \quad \text{(3)}$$

### 3. Phương pháp Mô hình Chuỗi Thời gian Tham số (Parametric Time-Series Models)

Phương pháp này bao gồm việc ước tính các mô hình chuỗi thời gian tham số cho lợi suất, hoặc tính toán các kiểm định tỷ số khả năng (likelihood-ratio tests).

Bài báo sử dụng mô hình giả định rằng logarit của giá cổ phiếu ($P_t$) bao gồm cả thành phần vĩnh viễn (permanent, $P_t^*$) và thành phần nhất thời (transitory, $u_t$):

$$P_{t} = P_{t}^{*} + u_{t}$$

Nếu thành phần tĩnh ($u_t$) là một quá trình tự hồi quy bậc nhất AR(1):

$$\boldsymbol{u_{t}} = \rho_{1} u_{t-1} + v_{t} \quad \text{(4)}$$

Thì lợi suất ($\Delta P_t$) đi theo quá trình ARMA(1,1):

$$\boldsymbol{\Delta P_{t}} = \epsilon_{t} + (1-L)(1-\rho_{1}L)^{-1} v_{t} \quad \text{(5)}$$

Trong đó $\epsilon_t \equiv P_t^* - P_{t-1}^*$ biểu thị sự đổi mới (innovation) đối với thành phần không dừng (nonstationary component).

### 4. Công thức Phân tách Phương sai và Ước tính Thành phần Nhất thời

Bài báo sử dụng cách tiếp cận không yêu cầu chỉ định rõ quá trình cho thành phần nhất thời, nhưng cho phép tập trung vào độ lệch chuẩn và phần trăm phương sai lợi suất một kỳ được quy cho thành phần này.

Phương sai của lợi suất $T$-kỳ hạn ($\sigma_R^2$) được biểu diễn là:

$$\boldsymbol{\sigma_{R}^{2}} = T \sigma_{\epsilon}^{2} + 2(1-\rho_{T}) \sigma_{u}^{2} \quad \text{(6)}$$

Trong đó:
*   $\sigma_{\epsilon}^{2}$ là phương sai của các đổi mới đối với thành phần giá vĩnh viễn (permanent price component).
*   $\sigma_u^2$ là phương sai của thành phần tĩnh (stationary component).
*   $\rho_T$ là tự tương quan $T$-kỳ hạn của thành phần tĩnh.

Dựa trên dữ liệu về phương sai lợi suất trong hai chân trời $T$ và $T'$ và các giả định về $\rho_T$ và $\rho_{T'}$, các ước tính về $\sigma_{\epsilon}^2$ và $\sigma_u^2$ được đưa ra bằng cách sử dụng tỷ lệ phương sai $VR(T)$ và $VR(T')$ so với lợi suất một kỳ:

Ước tính phương sai của thành phần vĩnh viễn ($\hat{\sigma}_{\epsilon}^{2}$):

$$\boldsymbol{\hat{\sigma}_{\epsilon}^{2}} = \sigma_{R}^{2} \frac{T' V R(T') (1-\rho_{T})-T V R(T) (1-\rho_{T'})}{T T'(\rho_{T'}-\rho_{T})} \quad \text{(7a)}$$

Ước tính phương sai của thành phần nhất thời ($\hat{\sigma}_{u}^{2}$):

$$\boldsymbol{\hat{\sigma}_{u}^{2}} = \sigma_{R}^{2} \frac{T'[V R(T)-V R(T')]}{2 [ ( 1 -  \frac{T}{T'} (1-\rho_{T'})) - (1-\rho_{T}) ]} \quad \text{(7b)}$$

### 5. Công thức Tính toán Phương sai Lợi suất Yêu cầu (Required Return Variance)

Trong phụ lục (Appendix), bài báo trình bày công thức tính toán phương sai lợi suất yêu cầu ($\sigma_r^2$) cần thiết để giải thích sự đảo ngược về giá trị trung bình trong giá cổ phiếu, dựa trên việc giả định lợi suất yêu cầu (required returns) đi theo quá trình AR(1).

Công thức liên hệ phương sai lợi suất yêu cầu với phương sai "fad" (thành phần nhất thời) ($\sigma_u^2$) là:

$$\boldsymbol{\sigma_{r}^{2}} = \frac{\{(1+d)(1+\rho_{1})-\rho_{1}[1+(1+d)^{2}]\}(1+g)^{2}}{[1+(1+g)- \rho_{1}(1+g)]^{2}} \sigma_{u}^{2} \quad \text{(10)}$$

Trong đó:
*   $d$ là lợi suất cổ tức trung bình (average dividend yield).
*   $g$ là tốc độ tăng trưởng cổ tức trung bình.
*   $\rho_1$ là hệ số tự tương quan bậc nhất của quá trình AR(1) đối với lợi suất yêu cầu.
*   $\sigma_u^2$ là phương sai "fad".

  

