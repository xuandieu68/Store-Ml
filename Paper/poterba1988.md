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
* * **Test evaluation**: The paper evaluates different statistical tests for temporary price components
## 2.3 Evaluation 
![Ảnh chụp màn hình_13-10-2025_205828_](https://github.com/user-attachments/assets/3958fbda-0a11-4256-b958-969546a4d563)

* Recommendation: A reasonable balance between Type I and Type II errors suggests using critical values ​​above the usual 0.05 level

---

# 3. Statistical Evidence on Regression Means
## 3.1  NYSE Monthly Returns (1926-1985)
## 3.2 US Historical Data (1871-1985)
## 3.3 Equity Markets outside the United States
## 3.4 Individual Company Data (United States, post-1926)
## 3.5 Overall Summary
---

# 4. The Practical Importance of Temporary Components in Stock Prices
* **Model:** Logarithmic stock price is considered as the sum of a permanent component (following a random walk) and a temporary component (following a stationary process).
* **Explanation:** The temporary component may reflect "fads" (deviations caused by speculation) or be a consequence of changes in the required rate of return.
*  **Estimates:** For NYSE data 1926–1985, temporary components account for 43% to 99% of the variance in equally weighted monthly returns and have significant standard deviations. They also account for more than half of the monthly return variance for the value-weighted data..
* **Confirmation:** This result confirms Shiller's (1981) conclusion that models assuming constant expected returns cannot explain all the variance in stock market returns.
---
  
# 5. The Origin of the Temporary(transitory) Component in Stock Prices
* **Significance:** The temporary components in stock prices imply volatility in expected returns (ex ante returns).
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


