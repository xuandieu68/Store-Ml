

# 2.  **Methodological Issues**
**Goal:** Evaluate statistical power to detect *temporary deviations* from fundamentals.
## 2.1  Test methods 
**Main Tests:**
1. **Autocorrelations**: little power
2. **Variance-Ratio Test (VR):** considered to be the closest to the strongest tests against plausible alternative hypotheses, such as the "fads" model
   * Random walk → variance ∝ horizon
   * Mean reversion → VR < 1
3. **Regression Test:**
   * Multi-period return regressions
   * Detects both short-term & long-term correlations
4. **Likelihood-Ratio Test:**
   * Theoretically most powerful (Neyman–Pearson)

---

## 2.2. Power calculations (Monte Carlo)

* **Model:** ARMA(1,1) with permanent & transitory components, using Monte Carlo model
* **Sample:** 25,000 monthly return series (720 obs.)

**Table 1: Simulated Type II Error Rates**
![Ảnh chụp màn hình_13-10-2025_205828_](https://github.com/user-attachments/assets/3958fbda-0a11-4256-b958-969546a4d563)
* $\theta = 0.25$: One-quarter of the return variance comes from the temporary component.
* $\theta = 0.75$: Three-quarters of the return variance comes from the temporary component
* All tests use a significance level of 0.05 (size 0.05)

**Findings:**
 * All tests have **low statistical power**
 * Type II error very high (0.76–0.94)
 * Suggest using **higher significance level**

**Implication:**
→ Traditional tests may fail to detect mean reversion even when it exists.

---

# 3. Evidence of Mean Reversion

**Data Sets:**

1. NYSE Monthly (1926–1985)
2. Historical U.S. Data (1871–1985)
3. International Markets (Canada, U.K., 15 others)
4. Individual Stocks (82 firms)

---

## 3.1  NYSE Monthly Returns (1926-1985)

**Table 2: Variance Rate for NYSE Monthly Data, 1926–1985**
![Ảnh chụp màn hình_13-10-2025_234033_](https://github.com/user-attachments/assets/50842e37-d44e-4ccb-abbc-bfe06b4d61e7)
* **Short-horizon:** Positive serial correlation in monthly returns
* **Long-horizon:**  Negative autocorrelation → strong mean reversion
* **Equal-weighted > Value-weighted** in mean reversion strength
* **Excluding 1930s:** Weakens but does not remove effect

---

## 3.2 US Historical Data (1871-1985)
**Table 3: Variance Rates for US Data, 1871–1985**
![Ảnh chụp màn hình_13-10-2025_234051_](https://github.com/user-attachments/assets/11bdd094-cdea-4fff-9a35-d7acc146d7bd)
 * Period before 1925 (1871–1925):
    * Excess yield: 96-month VR is 0.441 .
    * Real yield: 96-month VR is 0.807 .
    * Regression to the mean appears to be larger in the pre-1925 period for excess returns than in the post-1926 CRSP data.
 * The Whole Period (1871–1985):
    * Excess yield: 96-month VR is 0.833 .
    * Real yield: 96-month VR is 0.781 .
    * The full-sample data show evidence of regression to the mean, although to a weaker extent than the post-1926 monthly CRSP data

---

## 3.3 Equity Markets outside the United States
* **Canada:** VR(96 months) = 0.585
* **U.K.:** VR(96 months) = 0.794
* **Germany, France:** VR < 0.5 → strong mean reversion
* **Pooled Mean:** VR(96m) ≈ 0.754
  → Similar global pattern: short-term momentum, long-term reversal

---

## 3.4 Individual Company Data (United States, post-1926)

* 82 U.S. firms (1926–1985)
* Mean reversion exists but weaker than market-level data
* Transitory shocks explain **smaller portion** of firm-specific variance
  
---
# 4. The Practical Importance of Temporary Components in Stock Prices

* **Model:** Logarithmic stock price is considered as the sum of a permanent component (following a random walk) and a temporary component (following a stationary process).
* **Explanation:** The temporary component may reflect "fads" (deviations caused by speculation) or be a consequence of changes in the required rate of return.
*  **Estimates:** For NYSE data 1926–1985, temporary components account for 43% to 99% of the variance in equally weighted monthly returns and have significant standard deviations. They also account for more than half of the monthly return variance for the value-weighted data..
* **Confirmation:** This result confirms Shiller's (1981) conclusion that models assuming constant expected returns cannot explain all the variance in stock market returns.

#  Economic Significance 

* Transitory component accounts for **43–99%** of variance (equal-weighted returns)
* Annualized std. dev. of transitory part: **9.7–21.6%**

**Implication:**
→ Market prices deviate substantially from fundamentals.

---

##  Interpretation & Takeaways

* **Statistical tests** → weak power, but consistent negative autocorrelations
* **Economic meaning:**

  * Long-term *mean reversion* → overreaction or *noise trading*
  * Short-term *momentum* → investor behavior, market frictions
* **Conclusion:** Evidence favors **noise-trading hypothesis** over changing risk premia.



---

