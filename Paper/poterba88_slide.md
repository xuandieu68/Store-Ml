

 # Mean reversion in stock price: Evidence and Implications
Poterba, 1988\
2025/10/18\
팜티수안유
 
---

# Content
1. Introduction
2. Methodological Issues
3. Evidence of Mean Reversion
4. The Practical Importance of Temporary Components in Stock Prices
5. The Origin of the Temporary Component in Stock Prices
6. Conclusion
---

# 1. Introduction
* **Importance:**
     * Understanding whether stock prices revert to the mean is crucial for evaluating asset pricing models.
     * When market prices deviate from fundamental values but later adjust, returns must show negative serial correlation — indicating correction of “erroneous” price movements.
* **Research Problem:**
     * This study examines whether prices regress to the mean using data from the United States and 17 other countries
     * Prior random-walk tests often lacked power to detect persistent deviations from fundamentals.
* **Preliminary finding:**
     * Significant temporary components in stock prices are needed to explain these correlations
     * Temporary, cyclical changes in required returns or valuation bubbles may also contribute.
---

# 2.  **Methodological Issues**
**Goal:** Evaluate statistical power to detect *temporary deviations* from fundamentals.
## 2.1  Test methods 
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

## 2.2. Power calculations 

* **Model:** ARMA(1,1) with permanent $P_t^*$ & transitory components $u_t$, using Monte Carlo simulation
* **Sample:** 25,000 monthly return series (720 obs.)

**Table 1: Simulated Type II Error Rates**

![Ảnh chụp màn hình_13-10-2025_205828_](https://github.com/user-attachments/assets/3958fbda-0a11-4256-b958-969546a4d563)

**Findings:**
 * All tests have **low statistical power**
 * Type II error very high (0.76–0.94)
 * Suggest using **higher significance level**

**Implication:**
Traditional tests may fail to detect mean reversion even when temporary component exists.

---

# 3. Evidence of Mean Reversion

## **Data Sets:**
1. NYSE Monthly (1926–1985)
2. Historical U.S. Data (1871–1985)
3. International Markets (Canada, U.K., 15 others)
4. Individual Stocks (82 firms)

## Variance Ratio Test (VR(k))
$$\mathbf{V R(k)} = \frac{\sigma_{k}^{2}/k}{\sigma_{1}^{2}/12} \quad \text{(1)}$$

*   $\sigma_{k}^{2} \equiv E R_{k t}^{2}$.
*   $R_{k t} \equiv \sum_{i=0}^{k-1} R_{t-i}$.
*   $R_t$ is the total yield for the month $t$.

---

## 3.1  NYSE Monthly Returns (1926-1985)

**Table 2: Variance Rate for NYSE Monthly Data, 1926–1985**

![Ảnh chụp màn hình_13-10-2025_234033_](https://github.com/user-attachments/assets/50842e37-d44e-4ccb-abbc-bfe06b4d61e7)
* **Short-horizon:** Positive serial correlation in monthly returns
* **Long-horizon:**  Negative autocorrelation → strong mean reversion
* **Equal-weighted > Value-weighted** in mean reversion strength


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
* **Canada:**   VR(96m) = 0.585
* **U.K.:**     VR(96m) = 0.794
* **Germany, France:** VR(96m) < 0.5 → strong mean reversion
* **Pooled Mean:** VR(96m) ≈ 0.754
  → Similar global pattern: short-term momentum, long-term reversal

## 3.4 Individual Company Data (United States, post-1926)

* 82 U.S. firms (1926–1985)
* Results in table 5 : Average 96-month VR
     * Excess Returns - risk-free rate: 0.880
     * Excess Return  - VW NYSE:  0.875
     * Market-model residuals: 0.985

* Mean reversion exists but weaker than market-level data
* Transitory shocks explain **smaller portion** of firm-specific variance
  
---
# 4. The Practical Importance of Temporary Components in Stock Prices

* **Economic Significance**
    * Transitory component accounts for **65.7–99%** of variance (equal-weighted returns)
    * Annualized std. dev. of transitory: **9.7–21.6%** for VW, **16.8-37.7%** for EW 

  ![Ảnh chụp màn hình_17-10-2025_22048_](https://github.com/user-attachments/assets/532bd65a-6204-4078-9b29-b628200dff9e)

*  **Confirms:** models assuming constant expected returns **cannot explain all the variance** 

---

# 5. The Origin of the Temporary Component in Stock Prices

* **Statistical tests** : the volatility in ex ante returns is better explained by changes in interest rates/risk volatility or is a by-product of noise trading
* **Difficulty with Risk-Based Explanation**
   * **Large Variability of Required Returns:**
      * To explain “fads” with 20% std. dev. → expected returns must fluctuate **≈ 5.8% per year** (half-life ≈ 2.9 years).
      * Too large compared with mean excess return (≈ 8.9%/yr).
      * Hard to justify by known **risk factors**.
      
   * **Serial correlation mismatch:**
 
      * AR(1) models explain negative autocorrelation only.
      * Data show: **positive (short-term)** + **negative (long-term)** serial correlation.
      → Inconsistent with pure risk-premium changes.
      
* **Conclusion:** Evidence favors **noise-trading hypothesis** over changing risk premia.


---

# 6. Conclusion

**Empirical Findings:**
* **Short-term:** Positive serial correlation (momentum)
* **Long-term:** Negative serial correlation (mean reversion)
* Temporary price components explain **large share of return variance**

 **Practical Implications:**
* For **long-term investors** → Market may be **less risky** than random walk suggests
* Supports **contrarian strategies** (buy losers, sell winners – *DeBondt & Thaler, 1985*)
* Firms may value assets using **average past prices**, not current market prices


 **Future Research Directions**
1. Develop & test **noise-trading theories**
2. Investigate **risk-variance factors** further
3. Use **additional data** beyond returns:
   * *Fundamental value measures*
   * *Proxies for noise trading* (retail trading, volume, sentiment)
   * *Expected volatility* (from options)




---

