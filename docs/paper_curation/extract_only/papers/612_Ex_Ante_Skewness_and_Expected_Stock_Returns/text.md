# Ex Ante Skewness and Expected Stock Returns∗

## Jennifer Conrad† Robert F. Dittmar‡ Eric Ghysels§

First Draft: March 2007 This Draft: October 2008

Abstract

We use a sample of option prices, and the method of Bakshi, Kapadia and Madan (2003), to estimate the ex ante higher moments of the underlying individual securities’ risk-neutral returns distribution. We ﬁnd that individual securities’ volatility, skewness and kurtosis are strongly related to subsequent returns. Speciﬁcally, we ﬁnd a negative relation between volatility and returns in the cross-section. We also ﬁnd a signiﬁcant relation between skewness and returns, with more negatively (positively) skewed returns associated with subsequent higher (lower) returns, while kurtosis is positively related to subsequent returns. To analyze the extent to which these returns relations represent compensation for risk, we use data on index options and the underlying index to estimate the stochastic discount factor over the 1996-2005 sample period, and allow the stochastic discount factor to include higher moments. We ﬁnd evidence that, even after controlling for differences in co-moments, individual securities’ skewness matters. However, when we combine information in the risk-neutral distribution and the stochastic discount factor to estimate the implied physical distribution of industry returns, we ﬁnd little evidence that the distribution of technology stocks was positively skewed during the bubble period–in fact, these stocks have the lowest skew, and the highest estimated Sharpe ratio, of all stocks in our sample.

[Figure 1]

∗All errors are the responsibility of the authors. We thank Robert Battalio, Patrick Dennis, and Stewart Mayhew for providing data and computational code. We thank Andrew Ang, Leonce Bargeron, and Paul Pﬂeiderer for helpful comments and suggestions, as well as seminar participants at Babson College, Berkeley, Boston College, Cornell University, the Federal Reserve Bank of New York, National University of Singapore, New York University, Northern Illinois University, Queen’s University Belfast, Stanford University and the Universities of Arizona, Michigan, Texas, and Virginia. A previous version of this paper was circulated under the title “Skewness and the Bubble.”

†Department of Finance, Kenan-Flagler Business School, University of North Carolina at Chapel Hill ‡Department of Finance, Stephen Ross School of Business, University of Michigan, Ann Arbor, MI 48109 §Department of Finance, Kenan-Flagler Business School, and Department of Economics, University of North

Carolina at Chapel Hill

# 1 Introduction

What role do higher moments play in investors’ decisions about the choice of portfolios and the pricing of assets? Arditti (1967) shows that investors with decreasing risk aversion will display preference for greater skewness in asset payoffs, and Rubinstein (1973) and Kraus and Litzenberger (1976, 1983) formalize this preference in the context of a pricing model. More recently, Harvey and Siddique (2000) document empirical evidence supporting the role of skewness risk in explaining cross-sectional differences in returns, and Dittmar (2000) shows that skewness (and kurtosis) appear to play a signiﬁcant role in pricing.

The common theme in these papers is that investors discount aggregate skewness. That is, investors are willing to pay more for a security with greater co-skew with some stochastic discount factor. A more recent literature has suggested that total rather than co-skewness plays a role in informing portfolio decisions and asset prices. Barberis and Huang (2007) suggest that, under cumulative prospect theory, agents will display a preference for stocks with more skewed returns. As a result, an asset with high total skewness will appear overpriced relative to a model with standard expected utility. Similar results are obtained with a different preference structure in Brunnermeier, Gollier, and Parker (2007). The models in these papers are consistent with the evidence in Mitton and Vorkink (2007) that suggests that individual investors with undiversiﬁed portfolios hold assets and portfolios that exhibit greater idiosyncratic skewness.

In this paper we examine the effect of total skewness on the pricing of equity securities. An important feature of the approach taken in our paper is that we focus on the ex ante distribution of returns by using information contained in option prices. Under the assumption of a no-arbitrage link between options and underlying markets, we retrieve risk-neutral measures of distributional moments following the procedure in Bakhsi, Kapadia, and Madan (2001). We suggest a number of advantages to this approach, compared to alternatives that measure distributional moments from the time series of underlying market asset returns. First, as noted by Bates (1991), Rubinstein (1985, 1994), and Jackwerth and Rubinstein (1996), option prices efﬁciently capture a market-based estimate of investors’ beliefs. Second, the use of option prices eliminates the need for a long time series to reliably estimate higher moments of the distribution. This consideration is of particular importance in gauging beliefs about relatively new ﬁrms (i.e. Internet companies), or during periods in which beliefs may change relatively quickly. Third, options provide an ex ante measure of beliefs; they do not give us, as Battalio and Schultz (2006) note, the “unfair advantage of hindsight.” As Jackwerth and Rubinstein (1996) state, “not only can the nonparametric method reﬂect the possibly complex logic used by market participants to consider the signiﬁcance of extreme events, but it also implicitly

brings a much larger set of information ... to bear on the formulation of probability distributions.”

We ﬁrst examine whether dispersion in skewness generates differences in expected returns across assets. We ﬁnd that, indeed, assets with high ex ante skewness earn lower average returns than assets with low ex ante skewness. We then investigate the primary source of tension in the two streams of research discussed above; is the importance of skewness in pricing due to co-movement with some aggregate stochastic discount factor, or is is residual idiosyncratic skewness that matters in determining prices? We exploit no-arbitrage conditions in the options and cash markets to ﬁnd evidence suggestive of a residual idiosyncratic skewness risk premium after accounting for systematic skewness. Finally, we ask whether differences in views of ex ante skewness can help explain why certain types of stocks, particularly tech stocks, had such high valuations in the late 1990s and early 2000s. We ﬁnd that skewness had little to do with these valuations; rather, investors appear to have viewed these assets as good ex ante Sharpe ratio bets.

Two other recent papers also investigate measures of skewness and their relation to stock prices. Xing, Zhang, and Zhao (2007) ﬁnd that portfolios sorted on differences in the slope of the volatility smirk generate differences in average returns. Since the slope of the smirk has been related to the probability of negative jumps in price levels, as suggested in Bates (1991) and Pan (2002), one may infer that the slope of the smirk is related to negative skewness. There are several differences between our paper and theirs. First, our measure of skewness includes information about both left-skewed and right-skewed behavior, since it uses information in both out-of-the-money puts and calls. Second, the focus in our paper differs: we are interested not only in the information that the risk-neutral skew may have for future stock returns, but also in the implications for the pricing of systematic and idiosyncratic risk.

A second study, Boyer, Mitton, and Vorkink (2008), examines the role of a measure of idiosyncratic skewness in explaining differences in returns across securities. The authors use a long-horizon cross-sectional model of forecasting the skew in individual security returns, and ﬁnd a negative relation between idiosyncratic skewness and returns, as suggested by the theories discussed above. They also show that idiosyncratic skewness can help explain the role of idiosyncratic variance in generating cross-sectional dispersion in returns. Their measure of skewness is substantially different from ours, involving the use of a fairly long time-series (60 months) of ex post data; in addition, they do not explore the difference between systematic and idiosyncratic skewness.

The remainder of the paper is organized as follows. In section 2, we detail the method we employ for recovering measures of volatility, skewness, and kurtosis, following Bakshi,

Kapadia, and Madan (2003). In Section 3, we discuss the data used in our analysis and present results of empirical tests performed on portfolios formed on the basis of the volatility, skewness, and kurtosis measures. In Section 4, we use data on the market portfolio, and its options, to estimate a stochastic discount factor which includes the information in higher moments, and use this stochastic discount factor to risk-adjust the raw returns related to higher moments. In Section 5, we discuss the estimation of implied physical distributions for individual securities, and present these estimates for industry portfolios. We conclude in Section 6.

# 2 Risk-Neutral Moments and Asset Prices

Throughout our discussion, we are assuming that securities are priced to eliminate risk-free arbitrage opportunities. As discussed in Harrison and Kreps (1979), the lack of arbitrage opportunities in the market implies the existence of a probability measure that prices payoffs by discounting at the risk free rate. Formally, this risk-neutral probability measure, Q, satisﬁes

Pt = e−rτEtQ [Pt (1 + Rt+τ)]. (1)

where Pt represents the asset’s price, r is the risk free rate, τ is the holding period, and Rt+τ represents the return on the asset. Equivalently, a stochastic discount factor, Mt+τ, exists that discounts payoffs to current prices under the physical probability measure, P.

As noted in the introduction, there is a large body of theory and evidence that suggests that moments (variance, skewness, and kurtosis) of the physical distribution are important in determining investors’ portfolio choice and the pricing of assets. Equation (1) similarly suggests that moments of the risk-neutral distribution will affect investors’ pricing of assets.

We recover the risk-neutral moments above using the prices of options. Recovering riskneutral distributions from option prices has a long history in the literature (see Figlewski (2007) for a review). One of the advantages of this approach is that it recovers moments from asset prices, rather than realized returns. Thus, the estimates are representative of the ex ante moments relevant for asset pricing, allaying the criticism leveled in Battalio and Schulz (2006) of the “unfair advantage of hindsight.” Our speciﬁc approach follows Bakshi and Madan (2000) and Bakshi, Kapadia, and Madan (2003).

## 2.1 Computing Risk Neutral Moments

Bakshi and Madan (2000) show that any payoff to a security can be constructed and priced using a set of option prices with different strike prices on that security. Bakshi, Kapadia, and Madan (2003) demonstrate how to express the risk-neutral density moments in terms of quadratic, cubic, and quartic payoffs. In particular, Bakshi, Kapadia, and Madan (2003) show that one can express the τ-maturity price of a security that pays the quadratic, cubic, and quartic return on the base security as

- V (t,τ) =

∞

S(t)

2(1 − ln(K/S(t))) K2

[Figure 2]

C(t,τ;K)dK (2)

+

S(t)

0

2(1 + ln(K/S(t))) K2

[Figure 3]

P(t,τ;K)dK

- W(t,τ) =

∞

S(t)

6ln(K/S(t)) − 3(ln(K/S(t)))2) K2

[Figure 4]

C(t,τ;K)dK (3)

+

S(t)

0

6ln(K/S(t)) + 3(ln(K/S(t)))2 K2

[Figure 5]

P(t,τ;K)dK

- X(t,τ) =

12(ln(K/S(t)))2 − 4(ln(K/S(t)))3) K2

∞

C(t,τ;K)dK (4)

[Figure 6]

S(t)

S(t)

12(ln(K/S(t)))2 + 4(ln(K/S(t)))3 K2

+

P(t,τ;K)dK

[Figure 7]

0

where V (t,τ), W(t,τ), and X(t,τ) are the quadratic, cubic, and quartic contracts, respectively, and C(t,τ;K) and P(t,τ;K) are the prices of European calls and puts written on the underlying stock with strike price K and expiration τ periods from time t. As equations (2), (3) and (4) show, the procedure involves using a weighted sum of (out-of-the-money) options across varying strike prices to construct the prices of payoffs related to the second, third and fourth moments of returns.

Using the prices of these contracts, standard moment deﬁnitions suggest that the risk-

neutral moments can be calculated as

σQ(t,τ) = erτV (t,τ) − µ(t,τ)2 (5)

[Figure 8]

γQ(t,τ) =

erτW(t,τ) − 3µ(t,τ)erτV (t,τ) + 2µ(t,τ)3 [erτV (t,τ) − µ(t,τ)2]3/2

[Figure 9]

κQ(t,τ) =

erτX(t,τ) − 4µ(t,τ)W(t,τ) + 6erτµ(t,τ)2V (t,τ) − µ(t,τ)4 [erτV (t,τ) − µ(t,τ)2]2

[Figure 10]

(6)

(7)

where

µ(t,τ) = erτ − 1 − erτV (t,τ)/2 − erτW(t,τ)/6 − erτX(t,τ)/24 (8)

and r represents the risk-free rate. We follow Dennis and Mayhew (2002), and use a trapezoidal approximation to estimate the integrals in expressions (2)-(4) above using discrete data.1

## 2.2 Data

Our data on option prices are from Optionmetrics (provided through Wharton Research Data Services) . We begin with daily option price data for all out-of-the-money calls and puts for all stocks from 1996-2005.2 Closing prices are constructed as midpoint averages of the closing bid and ask prices.

Some researchers have argued that option prices and equity prices diverged during our sample period. For example, Ofek and Richardson (2003) propose that the Internet bubble is related to the ‘limits to arbitrage’ argument of Shleifer and Vishny (1997). This argument requires that investors could not, or did not, use the options market to proﬁt from mis-pricing in the underlying market, and, in fact, Ofek and Richardson (2003) also provide empirical evidence that option prices diverged from the (presumably misvalued) prices of the underlying equity during this period. However, Battalio and Schultz (2006) use a different dataset of option prices than Ofek and Richardson (2003), and conclude that shorting synthetically using the options market was relatively easy and cheap, and that short-sale restrictions are not the cause of persistently high Internet stock prices. A corollary to their results is that option prices and the prices of underlying stocks did not diverge during the ‘bubble’ period and they

[Figure 11]

- 1We are grateful to Patrick Dennis for providing us with his code to perform the estimation.
- 2We do not adjust for early exercise premia in our option prices. As Bakshi,Kapadia and Madan (2003) note,

the magnitude of such premia in OTM calls and puts is very small, and the implicit weight that options receive in the estimation declines as they get closer to at-the-money. In their empirical work, BKM show that, for their sample of OTM options, the implied volatilities from the Black-Scholes model and a model of American option pricing have negligible differences.

argue that Ofek and Richardson’s results may be a consequence of misleading or stale option prices in their data set. Note that if option and equity prices do not contain similar information, then our tests should be biased against ﬁnding a systematic relation between estimates of higher moments obtained from option prices and subsequent returns in the underlying market.3 However, motivated by the Battalio and Schultz results, we employ a number of ﬁlters to try to ensure that our results are not driven by stale or misleading prices. We eliminate option prices below 50 cents, as well as options with less than one week to maturity. At the outset, we require that an option has a minimum of ten days of quotes during any month; in later robustness checks, we impose additional constraints on the liquidity in the option. We also eliminate days in which closing quotes on put-call pairs violate no-arbitrage restrictions.

In estimating equations (5) - (7), we use equal numbers of out-of-the-money (OTM) calls and puts for each stock for each day. Thus, if there are n OTM puts with closing prices available on day t we require n OTM call prices. If there are N > n OTM call prices available on day t, we use the n OTM calls which have the most similar distance from stock to strike as the OTM puts for which we have data. We require a minimum n of 2; we perform robustness checks on our results when this minimum data constraint is increased.4 The resulting set of data consists of 3,722,700 daily observations across ﬁrms and maturities over the 1996-2005 sample period.

In Table 1, we present descriptive statistics for the sample estimates of volatility, skewness and kurtosis. We report medians, 5th and 95th percentiles across time and securities for each year during the sample period. There are clear patterns in the time series of these moments through the sample period, as well as evidence of interactions between them. Volatility peaks in 2000, during the height of the bubble period, then declines through 2005. The median riskneutral skewness is negative, indicating that the distribution is left-skewed; the median value stays relatively ﬂat through 2000 after which it declines sharply, while the median kurtosis estimate increases during that same period, more than doubling from 2000 through 2005.

[Figure 12]

- 3Robert Battalio graciously provided us with the OPRA data used in their analysis; unfortunately, these data, provided by a single dealer, do not have a sufﬁcient cross-section of data across calls and puts to allow us to estimate the moments of the risk-neutral density function in which we are interested.
- 4Dennis and Mayhew (2006) examine and estimate the magnitude of the bias induced in Bakshi-KapadiaMadan estimates of skewness which is due to discreteness in strike prices. For $ 5 ($2.50) differences in strike prices, they estimate the bias in skewness is approximately -0.07 (-0.05). Since most stocks have the same differences across strike prices, however, the relative bias should be approximately the same across securities, and should not affect either the ranking of securities into portfolios based on skewness, or the nature of the crosssectional relation between skewness and returns which we examine.

# 3 Risk-Neutral Moments and the Cross-Section of Returns

In this section, we examine whether portfolios formed on the basis of risk-neutral moments are associated with cross-sectional dispersion in subsequent returns. Data on stock returns are obtained from the Center for Research in Security Prices (again provided through Wharton Research Data Services). The basis for our analysis is the intersection of the the options data discussed above and monthly data on all individual securities with common shares outstanding.

## 3.1 Raw and Characteristic-Adjusted Returns

We begin by selecting daily observations of prices of out-of-the-money calls and puts on individual securities, which have maturities closest to 1 month, 3 months, 6 months and 12 months, and group these options into separate maturity bins. In each maturity bin, we estimate the moments of the risk-neutral density function for each individual security on a daily basis. Following Bakshi, Kapadia and Madan (2003), we average the daily estimates for each stock over time (in our case, the calendar quarter.) For each maturity bin, we further sort options into tercile portfolios based on the moment estimates (volatility, skewness or kurtosis); the ‘extreme’ portfolios contain 30% of the sample, while portfolio 2 contains 40% of the sample. We re-form portfolios each month, holding moment ranks constant over the calendar quarter. In each quarter, we also remove ﬁrms that are in the top 1% of the cross-sectional distribution of volatility, skewness or kurtosis to mitigate the effect of outliers.

In Table 2, we report results for portfolios sorted on the basis of estimated volatility (Panel A), estimated skewness (Panel B) and estimated kurtosis (Panel C). Speciﬁcally, we report the average of the subsequent raw returns of the equally-weighted moment-ranked portfolios over the next month in the ﬁrst column of data. In the next column, we report the average characteristic-adjusted return over that same month. To calculate the characteristic-adjusted return, we perform a calculation similar to that in Daniel et al.˜(1997). For each individual ﬁrm, we assess to which of the 25 Fama-French size- and book-to-market ranked portfolios the security belongs. We subtract the return of that Fama-French portfolio from the individual security return and then average the resulting excess or characteristic-adjusted ‘abnormal’ return across ﬁrms in the moment-ranked portfolio. In the next three columns, we report the average risk-neutral volatility, skewness and kurtosis estimates for each of the ranked portfolios. Finally, we report average betas, average (log) market value and average book-tomarket equity ratios of the securities in the portfolio.

Summary statistics in Panel A of Table 2 suggest a strong negative relation between

volatility and subsequent raw returns; for example, in the shortest maturity options (maturity bin 1), the returns differential between high volatility (Portfolio 3) and low volatility (Portfolio 1) securities is -32 basis points per month; longer maturities have differentials between 50 and 56 basis points per month. The columns of data which report the average characteristics of securities in the portfolio show sharp differences in beta, size and book-to-market equity ratios across these volatility-ranked portfolios. Low (high) volatility portfolios tend to contain low (high) beta ﬁrms and larger (smaller) ﬁrms, while differences in book-to-market equity ratios across portfolios are relatively small and differ across maturity bins. We adjust for these differences in size and book-to-market equity ratio in the characteristic-adjusted return column. After adjusting for the differences in size and book-to-market observed across the volatility portfolios, the return differentials are somewhat attenuated in all four maturities. However, although the differential is reduced, it remains signiﬁcant, with lowest volatility portfolios earning between 10 and 23 basis points per month more than the highest volatility portfolios in all four maturity bins.

- Panel A also indicates that there is a weak negative relation between volatility and skew-

ness; in all maturity bins, skewness has a tendency to decline as volatility increases, although the effect is not monotonic. The relation between volatility and kurtosis in Panel A is much stronger: as average volatility increases in the portfolio, kurtosis declines in all four maturity bins. Thus, the relation between volatility and returns may be confounded by the effect, if any, of other moments on returns; we examine this possibility in later sections of the paper. Finally, the average number of securities in each portfolio indicates that the portfolios should be relatively well-diversiﬁed. The top and bottom tercile portfolios average 273 ﬁrms, whereas the middle tercile portfolio averages 365 ﬁrms. Combined with the fact that we are sampling securities which have publicly traded options, this breadth should reduce the effect of outlier ﬁrms on our results.

- Panel B of Table 2 sorts securities into portfolios on the basis of estimated skewness. In-

terestingly, we see signiﬁcant differences in returns across skewness-ranked portfolios. The raw returns differential is negative for all four maturities, at 26, 43, 47 and 44 basis points per month, respectively. That is, on average, in each maturity bin the securities with lower skewness earn higher returns in the next month, while securities with less negative, or positive, skewness earn lower returns. The differentials in raw returns are of the same order of magnitude or larger than that observed in the volatility-ranked portfolios in Panel A. Compared to the volatility-ranked portfolios, the skewness-ranked portfolios show relatively little difference in their average market capitalization and betas, although differences in book-tomarket equity ratios remain. When we adjust for the size- and book-to-market characteristics of securities, the characteristic-adjusted returns are reduced only slightly, and average 28, 43,

39 and 40 basis points per month, respectively, across the maturity bins.5

In addition to the differences in returns, the table indicates that there is a negative relation between skewness and both volatility and kurtosis. That is, both volatility and kurtosis decline as we move across skewness-ranked portfolios. As in Panel A, interactions between other moments and returns could be masking or exacerbating the relation between skewness and returns. Consequently, in later tests, we control for the relation of other higher moments to returns in estimating their effect.

Finally, Panel C of Table 2 reports the results when securities are sorted on the basis of estimated kurtosis. Generally, we see a positive relation between kurtosis and subsequent raw returns; the return differential is economically signiﬁcant, at 12, 31, 35 and 37 basis points per month across the four maturities. As with the other moment-ranked portfolios, the effect is reduced after adjusting for book-to-market and market capitalization differences, but the differences are very slight and the effect remains highly signiﬁcant, at 14, 30, 35 and 36 basis points per month across maturity bins. We also observe patterns in the other estimated moments, with both volatility and skewness decreasing as kurtosis increases. Again, this emphasizes the need to control for the relation of all higher moments to returns.

The results in Table 2, Panels A-C, suggest that, on average, higher moments in the distribution of securities’ payoffs are related to subsequent returns. Consistent with the evidence in Ang, Hodrick, Xing and Zhang (2006a), we see that securities with higher volatility have lower subsequent returns. We also ﬁnd that securities with higher skewness have lower subsequent returns, while higher kurtosis is related to higher subsequent returns. As a robustness check, in the next section we use a factor-adjustment method which controls for other characteristics of the ﬁrms.

## 3.2 Factor-Adjusted Returns

In Table 2 above, we adjust for the differences in characteristics across portfolios, following Daniel et al. (1997), by subtracting the return of the speciﬁc Fama-French portfolio to which an individual ﬁrm is assigned. However, Fama and French (1993) interpret the relation between characteristics and returns as evidence of risk factors. Consequently, we also adjust for differences in characteristics across our moment-sorted portfolios by estimating a time series regression of the ‘factor-mimicking’ portfolio returns on the three factors proposed in Fama

[Figure 13]

5In a different application, Xing, Zhang and Zhao (2007) ﬁnd a positive relation between a skewness metric taken from option prices and the next month’s returns. Their measure of skewness is the absolute value of the difference in implied volatilities in out-of-the-money call option contracts, where the strike price is constrained to be within the range of 0.8S to S, and preferably in the range of 0.95S to S. Thus, their skewness measure is related to the slope of the volatility smile over a smaller range of strike prices.

and French (1993). The dependent variable in these regressions is the monthly return from portfolios re-formed each month (as in Table 2), where the portfolios consist of a long position in the portfolio of securities with the highest estimated moments, and a short position in the portfolio of securities with the lowest estimated moments. The three factors used as independent variables in the regressions are the return on the value-weighted market portfolio in excess of the risk-free rate (rMRP,t), the return on a portfolio of small capitalization stocks in excess of the return on a portfolio of large capitalization stocks (rSMB,t), and and the return on a portfolio of ﬁrms with high book-to-market equity in excess of the return on a portfolio of ﬁrms with low book-to-market equity (rHML,t). As in Table 2, ﬁrms are grouped by maturity and sorted into portfolios on the basis of estimated moments (volatility, skewness and kurtosis). We report intercepts, slope coefﬁcients for the three factors, and adjusted R-squareds. Standard errors for the coefﬁcients are presented in parentheses, and are adjusted for serial correlation and heteroskedasticity using the Newey and West (1987) procedure.

Panels A-D of Table 3 present results for options closest to one, three, six, and twelve months to maturity, respectively. The ﬁrst row of each panel contains the results for the long-short portfolio constructed from volatility-sorted portfolios. Consistent with the results in Panel A of Table 2 for characteristic-adjusted returns, we observe negative alphas in our “high-low” portfolio in all four maturity bins. The absolute magnitude of the alphas declines from 57 to 41 basis points per month across maturity bins, with t-statistics of -1.77, -1.65, -1.54 and -1.16, respectively. These results are consistent with those of Ang, Hodrick, Xing and Zhang (2006), who show that ﬁrms with high idiosyncratic volatility relative to the FamaFrench model earn “abysmally low” returns.

The patterns in the intercepts for skewness-sorted portfolios (row 2 of Panels A-D of Table

- 3) are also consistent with that observed in Panel B of Table 2. Alphas are negative in all four maturities, signiﬁcant at the 10% level for the one month maturity and at the 5% level or better in the other three maturities. The alphas remain roughly constant in magnitude as we move from short-maturity options to long-maturity options, at 58, 67, 64 and 62 basis points per month, respectively. The negative alphas still suggest a ‘low skewness’ premium; that is, securities with more negative skewness earn, on average, higher returns in the subsequent months, while securities with less negative, or positive skewness, earn lower returns in subsequent months.

The evidence that skewness in individual securities is negatively related to subsequent returns is consistent with the models of Barberis and Huang (2004), and Brunnermeier, Gollier and Parker (2005). In their papers, they note that investors who prefer positively skewed distributions may hold concentrated positions in (positively skewed) securities–that is, investors may trade off skewness against diversiﬁcation, since adding securities to a portfolio will in-

crease diversiﬁcation, but at the cost of reducing skewness. The preference for skewness will increase the demand for, and consequently the price of, securities with higher skewness and consequently reduce their expected returns. This evidence is also consistent with the empirical results in Boyer, Mitton and Vorkink (2008), who generate a cross-sectional model of expected skewness for individual securities and ﬁnd that portfolios sorted on expected skew generate a return differential of approximately 67 basis points per month.

In the third rows of Panels A-D of Table 3, we report the results for kurtosis-sorted portfolios. Consistent with the results in Table 2, we see positive intercepts in portfolios that are long kurtosis. Alphas are positive and both economically and statistically signiﬁcant, at 55, 62, 56 and 62 basis points per month, respectively, across the four maturities. Similar to the characteristic-adjusted returns in Table 3, there is no discernible trend in them across maturity bins. The magnitude of the alphas with respect to kurtosis is comparable to that observed in the skewness and volatility sorted portfolios.

There is one other noteworthy feature of Table 3. The explanatory power of the FamaFrench three factors is, on average, lower for the kurtosis-sorted High-Low portfolios, and much lower for the skewness-sorted portfolios, than the volatility-sorted portfolios. Some of this difference is likely due to the fact that, as Table 2 shows, skewness and kurtosissorted portfolios exhibit much lower differences in size and beta than do the volatility-sorted portfolios. However, it is also possible that there are features of the returns on moment-sorted portfolios that are not captured well by the usual ﬁrm characteristics.

## 3.3 Additional robustness checks

We perform several additional robustness checks on our results to examine the possibility that return differentials are driven by liquidity issues, either in the underlying equity returns or by stale or illiquid option prices. To examine the latter possibility, we add an additional ﬁlter to our sample, and eliminate the observation if there is no trading in any of the out-of-the-money options on a particular day. These results are presented in Appendix Table A1. The principal impact of this restriction is to substantially reduce our sample. As discussed above, on average there are 911 ﬁrms per month in our original sample (273/365/273 by tercile). Imposing the trading restriction reduces the average number of ﬁrms to 307. However, as shown in the table, with the exception of short-maturity kurtosis-sorted portfolios, the magnitude of return differentials across portfolios remains stable, or actually increases. Thus, we continue to ﬁnd that returns are negatively related to volatility and skewness, and positively related to

kurtosis.6

Second, we add the liquidity factor of Pastor and Stambaugh (2003) to our time series regression and re-estimate the factor-adjusted returns. These results are presented in Appendix Table A2. The basic results change very little. The intercepts retain negative signs for volatility and skewness and positive signs for kurtosis across all three maturity bins. Statistical signiﬁcance declines slightly; the alpha for the volatility portfolio loses its statistical signiﬁcance for all maturities, as does the alpha for the skewness portfolio only in the shortest maturity options. However, the overall conclusions are similar: high volatility and high skewness stocks earn negative excess returns, and high kurtosis stocks earn positive excess returns.

Overall, both the characteristic-adjusted returns in Table 2 and the regression results in Table 3 provide evidence that higher moments in the returns distribution are associated with differences in subsequent returns, and that not all of the return differential observed can be explained by differences in the size, book-to-market, beta or liquidity differentials of the moment-sorted portfolios. That is, on average, we see some relation between the higher moments of risk-neutral returns distributions of individual securities and subsequent returns on these stocks in the underlying market. In the next section, we allow the risk adjustment for subsequent returns to incorporate higher co-moments as well.

# 4 Higher Moment Premia, Systematic, and Idiosyncratic Risk

In the previous section, we document a negative premium for ex ante volatility and skewness in stock returns, and a positive premium for kurtosis. As discussed in the introduction, an open question is whether these premia are related to systematic or idiosyncratic risk. In this section, we address that question. Speciﬁcally, we ask whether observed premia are related to measures of ex ante co-moment risk, ex ante idiosyncratic risk, or both.

Conceptually, we consider idiosyncratic risk as that portion of a security’s return that is orthogonal to the stochastic discount factor, M(s,t,t + τ). That is, a security’s payoff can be decomposed into two components:

Ri,t+1 = Ri,ts +1 + ei,t+1 EtP [Ri,t+1Mt+1] = EtP Ri,ts +1Mt+1 = 1

[Figure 14]

6For brevity, we report only the average and characteristic-adjusted average returns to these portfolios. The remaining characteristics exhibit similar patterns to those depicted in Table 2. These results are available from the authors upon request.

where Rs is the systematic component of gross returns and ei,t+1 is the idiosyncratic component. In order to test for the presence of systematic risk, we consider the Euler equation speciﬁcation

EtP [Ri,t+1Mt+1] − 1 = ui,t+1 (9) and test the restriction that

E [ui,t+1] = α = 0 (10) As discussed in Chen and Knez (1996), this α is analogous to Jensen’s α.

Depending on one’s null, the Euler equation restriction may be viewed as a test of the presence of idiosyncratic components of returns that generate mean returns or a test of model speciﬁcation. In order to take the former view, one must assume that the stochastic discount factor, Mt+1 is the correct stochastic discount factor for pricing the assets under consideration. As made clear in Hansen and Jagannathan (1991) and Hansen and Jagannathan (1997), in an incomplete market, the presence of multiple admissible stochastic discount factors makes this claim difﬁcult to verify.

Nonetheless, we proceed by estimating a stochastic discount factor that is implied by a measure of the market portfolio. Coskewness and cokurtosis of returns with the market portfolio have been investigated in Harvey and Siddique (2000) and Dittmar (2002), and the authors ﬁnd that these measures improve upon pricing of assets relative to the Fama and French (1993) three factors. Moreover, the notion of residual skewness and kurtosis rests on the idea of measurement relative to some diversiﬁed portfolio, presumably the tangency portfolio of aggregate wealth. While pricing models that are alternative to an extended CAPM as investigated in Harvey and Siddique and Dittmar implicitly propose such a portfolio, we do not have options traded on these portfolios, rendering retrieval of risk-neutral probability measures difﬁcult. However, given the presence of index options, we have a measure of this portfolio in the context of a nonlinear CAPM. Thus, we proceed by using a market implied stochastic discount factor, with the caveat that our tests in this section may represent a test of model speciﬁcation rather than a test of the presence of idiosyncratic skewness and kurtosis premia.

## 4.1 Estimating an implied stochastic discount factor

We begin by extracting an estimate of a stochastic discount factor from a benchmark market portfolio, the S&P 500 Index. If we assume that the market portfolio and its options are priced correctly, then the relation between the risk-neutral and physical density functions for

the market for each state, s, can be expressed as:

M(s,t,t + τ) ∗ P(s,t,t + τ) = e−r(t,t+τ)Q(s,t,t + τ) (11)

where M(s,t,t + τ) is the stochastic discount factor from time t to t + τ, P(s) is the physical density function for the market portfolio over the same period, and Q(s) is the ex ante riskneutral density function for the market portfolio implied by the options market. Thus, given estimates of the densities P and Q, we can construct a market stochastic discount factor.

To calculate an estimate of M(s), we ﬁrst compute the ﬁrst four moments of the market’s risk-neutral and physical density. The risk-neutral moments are calculated using the same method as individual securities, using S&P 500 index option prices in place of individual security option prices. That is, we ﬁrst calculate equations (5) - (7) for OTM S&P 500 index options, using options closest to τ = 1 month, 3 months, 6 months, and 12 months to maturity.

Physical moments are calculated by using historical data to generate sample analogues of the physical variance (V ARP), skewness (SKEWP), and kurtosis (KURTP) of the underlying market return distribution. A number of issues arise in using historical sample data to measure conditional moments. First, Foster and Nelson (1996) address the question of optimal sample estimators for time-varying volatility, and suggest that reasonable estimates can, under most circumstances, be obtained with a calendar year of past daily returns data. There is less guidance on the appropriate window to use in calculating conditional higher moments,

- as much of the literature on sample moment estimators has focused on volatility. In their empirical work, Bakshi, Kapadia and Madan (2003) also note that skew and kurtosis may be underestimated using short windows. We therefore use a four-year period to estimate our moments, consistent with the length of historical returns data used in Jackwerth (2000) and Brown and Jackwerth (2001).

A second issue that arises is whether the sample moments can be viewed as conditional. In our application, we opt to use a four-year sample to estimate the conditional moments as of 1/31/96, and hold this physical distribution constant over our analysis period. We do so to provide a conservative view of the degree of time variation in conditional moments. In Section

- 5.1, we examine the sensitivity of our analysis to these assumptions. Speciﬁcally, we allow the moments to roll through time, so that in each period, we recalculate the physical moments, and thus the physical distribution. Additionally, we consider a parametric assumption for the moments, allowing them to follow an autoregressive process. We discuss these results further in Section 5.1, but note here that the qualitative implications of our analysis are unchanged.

Finally, estimation of the physical distribution requires a speciﬁcation of the conditional mean of the S&P 500 return. Jackwerth (2000) suggests adding the historical risk premium

of 8% to the risk-free rate observed at time t. In our analysis, we follow his suggestion and use the annualized yield on a 90-day Treasury bill, obtained from the Federal Reserve H.15 report, as our measure of the risk free rate. We experiment with alternative values of the risk premium and obtain similar results.

Once moments for both the risk-neutral and physical distribution are generated, the second step of the procedure involves estimating the density functions of both distributions using the method described in Eriksson, Forsberg and Ghysels (2004). This procedure uses the Normal Inverse Gaussian (NIG) family to estimate an unknown distribution of random variables. As they note, the appeal of the NIG family of distributions is that they can be completely characterized by the ﬁrst four moments. As a consequence, given the ﬁrst four moments, one can “ﬁll in the blanks” to obtain the entire distribution and, as they show, the method is particularly well-suited when the distribution exhibits skewness and fat tails, as it does in the returns distributions which we examine in this application. Having the market risk-neutral and physical distributions approximated with an NIG distribution, we use two methods to estimate the stochastic discount factor.

In the ﬁrst method, we simply use equation (11) to solve for M(s) as the discounted ratio of the risk-neutral probability density function to the physical density function over a range of implied relative wealth (return) levels. We call the resulting stochastic discount factor M∗. In the second method, we begin with M∗ and employ an additional step. We parameterize the stochastic discount factor from the ﬁrst step by projecting it onto a polynomial in relative wealth levels. By controlling the form of the polynomial, we can force the stochastic discount factor to include (or exclude) sequential higher moments, allowing us to examine their incremental effect on the calculation of risk-adjusted returns. For example, the stochastic discount factor MV AR includes only linear returns, while MSKEW includes linear and squared terms (similar to that used in Harvey and Siddique (2000)) and MKURT includes linear, squared and cubic terms (as in Dittmar (2002)). These stochastic discount factors more clearly indicate the role that co-moments with the aggregate market play in determining pricing.

Using each of the four stochastic discount factors, we calculate alphas following Chen and Knez (1996), who characterize pricing errors as:

T

1 T

Mˆ (t,t + τ)r(t,t + τ). (12)

αˆ =

[Figure 15]

t=1

The variable r(t,t+τ) represents overlapping τ-period returns on the (zero-cost) High-Low, or factor mimicking portfolios, for volatility, skewness, and kurtosis. As noted in Chen and Knez, under the null of zero pricing errors, α = 0. As a consequence, we perform univariate tests for

the null hypothesis using Newey-West (1987) standard errors. While the NIG class is versatile (e.g., as Eriksson, Forsberg and Ghysels (2004) note, its domain is much wider than GramCharlier or Edgeworth expansions), there are some restrictions on its use. In particular, the parameters of the NIG approximation may become imaginary and so the distribution cannot be computed. This constraint does not arise in the case of 3- and 12-month to maturity options, and arises in only one month for the 6-month maturity options. However, this condition is frequently violated in the case of 1-month to maturity options. As a result, we compute stochastic discount factors using only 3-, 6-, and 12-month maturity options.

Our data cover the period June, 1996 through December, 2005; consequently, we have 115 monthly observations for the three-month stochastic discount factor, 112 observations for the 6-month stochastic discount factor and 106 observations for the 12-month stochastic discount factor. The number of Newey-West lags used to compute standard errors reﬂects the number of overlapping months in each sample; for example, 12 lags are used in computing standard errors for the 12-month stochastic discount factor.

## 4.2 Comparing stochastic discount factors

The time series average of the four stochastic discount factors which we estimate are presented, over the range of possible market returns and the entire sample period, in Figure 1. For brevity, we focus on options closest to twelve months to maturity; results are qualitatively similar for 3- and 6-month maturities. In Part A of Figure 1, we present the four pricing kernels over the full support; in Part B, we present the three polynomial approximations MV AR, MSKEW and MKURT over a partial support to better illustrate the differences over this range.

The linear stochastic discount factor MV AR is downward sloping throughout its range, as is MSKEW. The cubic stochastic discount factor, MKURT, declines through most of its support, deviating only at extremely high and low values for the return on the market portfolio. These results are generally consistent with the behavior of investors who have declining relative risk-aversion. In contrast, note that the non-parametric stochastic discount factor M∗ presented in the top graph has a segment in the mid-range of the graph which is increasing. Although an upward sloping segment of the stochastic discount factor implied from option prices is consistent with the evidence in Jackwerth (2000) and Brown and Jackwerth (2001), it is, as these papers point out, a puzzle–it suggests that the representative investor may be risk-seeking over the upward sloping range. Brown and Jackwerth (2001) examine several possibilities for this behavior. Although we do not focus speciﬁcally on this puzzle in the current paper, it is worth noting that we obtain a similar result despite the fact that our sample period does not overlap with the sample used in the Brown and Jackwerth (2001) paper, and

the estimation methods used to estimate both the risk-neutral distribution and physical distribution are different. In addition, we observe the upward sloping segment over all three maturities (3-, 6- and 12-month maturity options) we examine. Thus, the empirical evidence suggests that the observation of an upward sloped segment in the non-parametric stochastic discount factor implied by option prices is robust to both sample and method. Moreover, the range over which Brown and Jackwerth (2001) observe their upward-sloping segment of the stochastic discount factor, at approximately 0.97 to 1.03, is associated with an upward-sloped segment in our estimation as well. 7

Although the behavior of the polynomial approximations of M exhibit clear differences from the non-parametric discount factor M∗, the ’ﬁt’ of the polynomial approximations is reasonable; the average R2’s of MV AR, MSKEW and MKURT are 5.5%, 13.2% and 16.3%, respectively. In the next section, we examine the implications of the estimated empirical stochastic discount factors for investors’ expectations of the payoffs to individual securities, and consequently to the moment-sorted portfolios in Table 2.

## 4.3 Risk-adjusted returns

In Table 4, we report estimates of alphas calculated from each of the stochastic discount factors estimated above using options closest to 3, 6, and 12 months to maturity.8 The alphas are calculated for each of the Hi-Lo moment-sorted portfolios (volatility, skewness and kurtosis) using equation (12). The results suggest that idiosyncratic skewness is important, even after allowing for the effects of higher moments on the stochastic discount factor. Speciﬁcally, the alphas for the skewness sorted portfolios have p-values of approximately 12% for 3-month options, and at the 5% level or better for 6- and 12-month options. The alphas related to skewness are economically signiﬁcant as well, ranging from 54 to 64 basis points per month. In contrast, the alphas related to volatility are not statistically signiﬁcant in any maturity bin, for any speciﬁcation of the stochastic discount factor. The alphas for the kurtosis-sorted portfolio are marginally signiﬁcant in the shortest maturity bin, but are not signiﬁcant in the samples of either 6- and 12-month options. As with volatility, these results are not sensitive to the stochastic discount factor used to calculate alphas. Thus, although we observed some differences in the previous section between the stochastic discount factors M∗, MV AR, MSKEW and MKURT, the inferences on residual returns are unaffected by this choice.

[Figure 16]

- 7Golubev et al. (2008) report a similar pattern of the pricing kernel using German DAX index data, and propose a statistical test for monotonicity. Using their test they ﬁnd statistically signiﬁcant against monotonicity; hence, their results also provide support for the presence of upward sloping segments.
- 8In the case of 6-month options, the NIG approximation assumptions were violated in only one month. This month is excluded from the calculations.

The residual importance of idiosyncratic skewness is consistent with models, such as Barberis and Huang (2004), and Brunnermeier, Gollier and Parker (2007), which suggest that investors have a preference for skewness in individual securities above and beyond their contribution to the co-skewness of the portfolio. It is also consistent with the empirical evidence in Mitton and Vorkink (2007), who ﬁnd a relation between the skewness in individual securities in individuals’ brokerage accounts and subsequent returns.

Our results do not necessarily imply that the alpha, or residual return, is an arbitrage proﬁt. The estimates of the stochastic discount factor used to construct α control only for nondiversiﬁable risk (including the risk of higher co-moments) in the context of a well-diversiﬁed portfolio. If investors have a preference for individual securities’ skewness, they may, as in Brunnermeier et al., hold concentrated portfolios and push up the price of securities which are perceived to have a higher probability of an extremely good outcome. As a consequence, the lower subsequent returns of high-skew stocks may represent an equilibrium result.

# 5 Implied Physical Probability Distributions

To this point, we have focused on the estimation of risk-neutral moments, and the relation of these moments to returns. However, the models that consider the effects on expected returns of skewness and fat tails in individual securities’ distributions deal with investors’ estimates of the physical distribution. Given an estimate of the stochastic discount factor, and riskneutral distributions of individual securities, we can construct a market-based estimate of individual securities’ physical distributions that does not rely on historical data. That is, we can directly estimate investors’ expectations regarding the returns distributions of underlying equities. To our knowledge, this is the ﬁrst time that market data have been used to construct an ex ante estimate of investors’ subjective probability estimates. Since papers such as Brunnermeier, Gollier and Parker (2007) and Barberis and Huang (2004) are models in which investors have biased beliefs, we also compare this ex ante estimate of subjective probabilities to more traditional ex post estimates of distributions constructed from historical returns.

Speciﬁcally, we take the stochastic discount factors M∗, MV AR, MSKEW and MKURT constructed from the market portfolio and its options, and, using equation (11), and individual ﬁrm options, reverse engineer an estimate of the underlying security’s physical probability distribution. That is, for each security, i, we compute

Qi (s,t,t + τ) M(s,t,t + τ)

Pi (s,t,t + τ) = e−r(t,t+τ)

. (13)

[Figure 17]

For every ﬁrm i, we compute risk-neutral moments using daily option prices and equations (5) through (7). For each horizon τ, we use the risk-neutral moments and the NIG approximation to compute the risk-neutral density Qi; using equation (11) and each of the stochastic discount factors that we have computed, we calculate implied physical distributions for ﬁrm i, for quarter t and horizon τ. We examine the differences in this measure of investors’ ex ante distributional beliefs, and implications for moments of returns, across securities and across time.

In order to consider differences across ﬁrms, we aggregate securities into industry portfolios, using the ten industry groupings available on Kenneth French’s website. We assign every individual security for which we can estimate risk-neutral moments into one of these industry groupings. The Utilities portfolio had very few ﬁrms in our sample, and some months were missing observations; consequently, we eliminate that industry portfolio as well as “Other,” and report results for eight out of ten of the industry portfolios. As results across the three polynomial approximations and the NIG approximation to the stochastic discount factor exhibit little difference, we present results only using the NIG approximation, or M∗. For brevity, we also report results only for τ equal to 12 months.

For each industry, we present the equal-weighted imputed physical distribution in Figure 2 at intervals in our sample period. That is, at the end of each calendar quarter, we compute the industry physical distribution by averaging over the densities of the ﬁrms in the industry.9 We then average the industry density over the sample depicted in each ﬁgure. The intervals presented are selected to accord roughly with interesting economic events (the Asian crisis, the ‘bubble’ period, the recession of 2000-2001 and the recovery); although the intervals we present are chosen with perfect hindsight, recall that the risk-neutral moments

- at any time t are ex ante in nature. For comparison, at each interval we present an estimate of the distribution taken from four years of historical data ending at time t for that industry portfolio.

The implied physical distributions constructed from options market data, and the estimated pricing kernel, appear much more stable than the distributions estimated from rolling historical data. For example, using historical data generates negative mean returns for three out of eight industries (Telecom, Tech, and Durables) in the fourth subperiod (Q103-Q405). This is clearly an artifact of the inclusion of the market downturn in the historical time series. In addition, skewness estimates based on historical data are much more variable, and the distributions tend to be left-skewed; approximately 70% (23/32) of the skewness estimates across subperiods and industries are negative. Although we do not report Sharpe ratios calculated

[Figure 18]

9Ideally, we would recover risk neutral moments for each industry using options on the industry indices. Unfortunately, since these contracts are not available, we employ averaging as a compromise procedure.

from historical distributions, they are extremely variable, ranging from -0.36 to 1.32. Overall, using historical data to generate estimates of investors’ subjective probabilities generates distributions which are highly sensitive to prior events, and have very different implications for investors’ opportunity sets.

In Table 5, we present estimates of the ﬁrst four moments of the implied physical distribution for each industry for the full period and for the same intervals presented in Figure 2; these estimates are constructed by integrating over market states. We also present estimates of the Sharpe ratio for each industry portfolio. There are several striking results in Table 5. First, the Sharpe ratios are comparatively stable, ranging from 0.07 to 0.26. We do, however, observe a sharp increase in the ex ante estimates of the Sharpe ratio through our sample period. In the last interval (03Q1-05Q4), Sharpe ratios in every industry grouping are at least double what they are in the earliest interval (96Q2-98Q2). Thus, Sharpe ratios in the pre-crash period are signiﬁcantly lower than Sharpe ratios in the recovery. Second, the skewness calculated from ex ante data is signiﬁcantly higher than that observed from historical returns; in fact, it is positive for every industry in every interval, varying from 0.30 to 0.51. This may be evidence of investors’ biased beliefs, such as the optimistic bias that Brunnermeier et al. (2007) discuss. In contrast, the differences in historical and implied kurtosis measures is smaller – although the implied kurtoses tends to be lower across industries than the historical estimates, the historical estimates are lower in 2 (out of 8) cases, and the magnitudes of the implied and historical kurtoses are quite similar. In fact, the average difference in the two measures is only 1.05, or approximately 22% of the average implied kurtosis across industries.

Consistent with our results in Table 2, we observe a strong negative correlation between skewness and the Sharpe ratio across industries–that is, industries which are perceived as more likely to have extreme positive outcomes also have lower ex ante Sharpe ratios. This correlation is very strongly negative throughout all four intervals examined, varying between -0.75 and -0.91, and averages -0.83 over the entire sample period. This result suggests that investors are trading off traditional risk-reward ratios for the likelihood of extreme ’good news’, and is consistent with a preference for idiosyncratic skewness. However, the surprising result in Table 5 is that ﬁrms in the Technology portfolio have the lowest skew (and the highest Sharpe ratio); this relation also holds throughout the sample period. In contrast, ﬁrms in the Durables portfolio have the highest skew and the lowest Sharpe ratio. And, the difference in skewness across these portfolios is large–for example, the percentage increase in skewness from the Tech portfolio to the other industry groupings varies from 15% to 72% across the subperiods examined.

Thus, we ﬁnd little evidence in implied physical probability distributions that the high

prices of technology ﬁrms during the Internet bubble period is related to investors’ expectations that these ﬁrms had a relatively high chance of extremely good outcomes. In fact, the comparatively high ex ante Sharpe ratios of these ﬁrms compared to ﬁrms in other industries suggests that investors believed that these ﬁrms were good ‘mean variance’ bets.

Two cautions are worth emphasizing. First, it may be that our requirement that ﬁrms have options traded on them prevents us from sampling the youngest, most highly skewed ﬁrms, particularly in those industries whose composition is changing the most rapidly. While the selection bias associated with option trading, and the use of option data to measure skewness, does not seem signiﬁcantly larger than the selection bias associated with data requirements related to the use of historical returns to measure skewness, it is difﬁcult to assess the extent of this selection bias for either method. We note simply that while the technology portfolio we analyze includes many ‘established’ ﬁrms such as IBM, Cisco and Microsoft, it also includes relative newcomers such as Amazon, Iomega, JDS Uniphase, Real Networks, Xilinx, etc., whose valuations during the ‘bubble period’ were quite high.

More importantly, the use of options data to infer higher moments limits us not just in the cross-section, but in the horizon over which we can estimate investors’ expectations. If investors’ expectations of moments over horizons longer than one year (the longest horizon for which we have data) are both relevant for prices, and signiﬁcantly different from the shorterhorizon moments that we have estimated, then our results may be incomplete and/or our inferences may be incorrect. For example, if investors believed that technology stocks’ extreme payoffs would occur over, say, ﬁve year intervals, then differences in ﬁve-year skewness may potentially explain high valuations.10 While we cannot rule this out, it is worth pointing out that the relation between shorter horizon skewness and Sharpe ratios in Table 5 is remarkably stable across all four intervals we examine. Since these intervals include the ‘pre-bubble’ and ‘post-bubble’ periods, any separate effect of longer horizon skewness would suggest a very marked term premium in the skew which differs dramatically across these intervals.

## 5.1 Robustness checks

The implied physical distributions in the previous section are constructed with a combination of forward-looking data from option prices, and an estimate of the market’s physical distribution estimated from historical market returns data. Since this use of historical market returns is the only instance where ex post data are used, we explore the sensitivity of our results to different choices of the historical record to estimate the market’s underlying returns distribution. First, we maintain the length of the four-year window, but allow the window to

[Figure 19]

10We are grateful to Paul Pﬂeiderer for an analysis of a setting in which this situation could arise.

roll forward with the corresponding risk-neutral distribution obtained from option prices; we still require that the four-year window end before the risk-neutral moments are calculated, by ending the window in quarter t-1 relative to the option data used to estimate moments. Second, to ensure that the window includes relatively rare ‘extreme’ events, we lengthen the window to 46 years, and use the period from 1950 to 1995 to estimate the market’s physical returns distribution. Third, we use a longer window of data and estimate a time series forecast of each of the three higher moments (volatility, skewness and kurtosis), using these forecasts as estimates of investors’ expectations regarding the corresponding physical moments. More speciﬁcally, for each quarter t, we use quarterly data beginning in March 1953 and ending in quarter t − 1 to estimate a separate AR(1)process for volatility, skewness and kurtosis, where the (quarterly) realized moments for this estimation are constructed from the previous 250, 500 and 750 days of daily market returns, respectively.

### 5.1.1 Implied Risk Aversion Measures Across Market Estimates

To compare the alternative estimates of the market’s physical distribution, we combine these different estimates with the options-based estimate of the market’s risk-neutral distribution to estimate an aggregate risk-aversion measure. In addition to highlighting the differences, if any, in inferences related to the market’s physical distribution, these estimates of riskaversion can serve as a diagnostic on the plausibility of our estimates of both the physical and risk-neutral distributions.

Following Jackwerth (2000) and Leland (1980), we estimate absolute risk aversion as:

RA = P′(s)/P(s) − Q′(s)/Q(s) (14)

where P(s) is the investors’ subjective, or physical, distribution and Q(s) is the risk-neutral distribution for the market; P′ and Q′ represent ﬁrst derivatives. As in the previous sections, we use the Bakshi et al. algorithm, and the NIG approximation, to estimate the risk-neutral distribution, while we use the four historical market return samples, including the AR(1) estimation of moments, and the NIG approximation, to estimate the market’s physical distribution. In addition to choosing different historical periods and methods to estimate variance, skewness and kurtosis, we explore the effect of setting the market risk premium at different levels. The results are presented in Table 6 and Figure 3; for brevity, we report levels of risk-aversion only for an 8% risk premium, and a risk-neutral distribution estimated from 12-month maturity options.

With an 8% risk premium, the estimated level of risk aversion is fairly reasonable, varying

between 6.3 and 19.9, depending on the interval and the market moments used to generate the physical distribution. Although the level of the risk-aversion changes somewhat depending on the historical returns used to estimate moments, and the level of risk premium assumed, the pattern of the changes in estimated risk aversion through the sample period remains remarkably constant. Speciﬁcally, it declines in the middle of the sample, reaching its lowest levels in late 2002 and early 2003; subsequently, estimated risk-aversion increases sharply through the end of the sample period in 2005.

Overall, we ﬁnd relatively little difference in estimates of aggregate risk-aversion among the different estimates of the market physical distribution which we use. However, there does appear to be evidence in the aggregate market that investors’ attitudes towards risk change sharply, with risk-aversion at relatively low levels at the height of the bubble, and increasing thereafter. The evidence that market events can change investors’ attitudes towards risk is consistent with the evidence in Jackwerth (2000) that the market crash of 1987 dramatically changed estimates of risk-aversion. The evidence that investors’ attitudes toward risk change over time also increases the advantage of using ex ante, rather than ex post, data to generate estimates of abnormal returns, as well as moments.

### 5.1.2 Implied Physical Distributions Across Market Estimates

The evidence above indicates that different estimates of the market’s physical distribution generate fairly similar levels and patterns in estimates of aggregate risk-aversion. When we use these alternative estimates of the market’s physical distribution to generate implied physical distributions across industries, the results, not surprisingly, are also fairly similar. However, there are some differences worth mentioning. While the longer estimation window of 1950-1995 generate similar estimates of volatility to those of the original 1992-1996 sample period, it generates higher estimates of skewness and kurtosis across all industries. The AR(1)estimation, in contrast, generates lower estimates of skewness and kurtosis.

There is one other interesting feature of the physical distributions imputed when the AR(1) estimation is employed on moments which is noteworthy. In the second subperiod, which extends from 9/98 through 3/2000, the implied skewness of all the industries in our sample increases sharply–in fact, on average, the skewness in each industry increases by a factor of 4 from the prior interval. Thus, there is some evidence in the data that investors perceived the distribution of payoffs as being relatively right-skewed. However, this increase in skewness is observed across all industries, and not just in the industries associated with ‘bubble’ pricing.

Overall, however, while the implied physical distributions for industries which we esti-

mate using these alternate estimates of the physical market distribution change, the crosssectional inferences we draw remain the same: technology stocks have lower skewness and kurtosis than ﬁrms in other industries. Thus, while skewness affects prices of securities, we ﬁnd no evidence that the prices of technology stocks in particular were higher in our sample period because of investors’ perception that they were more likely to be associated with extreme positive payoffs.11

# 6 Conclusion

We explore the possibility that higher moments of the returns distribution are important in explaining security returns. Using a sample of option prices from 1996-2005, we estimate the moments of the risk-neutral density function for individual securities using the methodology of Bakshi, Kapadia and Madan (2003). We analyze the relation between volatility, skewness and kurtosis and subsequent returns.

We ﬁnd a strong relation between these moments and returns. Speciﬁcally, we ﬁnd that high (low) volatility ﬁrms are associated with lower (higher) returns over the next month. This result is consistent with the results of Ang, Hodrick, Xing and Zhang (2006). We also ﬁnd that skewness has a strong negative relation with subsequent returns; ﬁrms with lower negative skewness, or positive skewness, earn lower returns. That is, investors seem to prefer positive skewness, and the returns differential associated with skewness is both economically and statistically signiﬁcant. We also ﬁnd a positive relation between kurtosis and returns. These relations are robust to controls for differences in ﬁrm characteristics, such as ﬁrm size, book-to-market ratios and betas, as well as liquidity and momentum.

We use index returns and index options to estimate an empirical stochastic discount factor, as well as polynomial approximations of the stochastic discount factor, to control for differences in higher co-moments, and their related compensation for risk. We use these stochastic discount factors to calculate risk-adjusted returns to portfolios sorted on the basis of volatility, skewness and kurtosis, where the risk-adjustment explicitly takes higher co-moments into account. After controlling for higher co-moments, we ﬁnd weak evidence that idiosyncratic kurtosis matters for short maturities, and strong evidence that idiosyncratic skewness has signiﬁcant residual predictive power for subsequent returns across maturities. This suggests that investors have a preference for skewness in individual securities, which is consistent with the models of Barberis and Huang (2004) and Brunnermeier, Gollier and Parker (2007).

Finally, we use the estimated stochastic discount factors, and the risk-neutral distribu-

[Figure 20]

11These results are available on request from the authors.

tions calculated for individual securities, to estimate implied physical distributions for securities. We ﬁnd several interesting results. First, our results suggest that implied physical distributions are much more stable than those constructed using historical data. Second, in implied physical distributions, we ﬁnd evidence of a trade-off between skewness in industry portfolios and ex ante estimates of the Sharpe ratios for the industry. That is, our results suggest a trade-off between expected returns and higher moments, with higher (lower) traditional risk-reward measures associated with lower (higher) skewness. However, we also ﬁnd that the portfolio containing technology ﬁrms has low ex ante physical skew and kurtosis, and a high Sharpe ratio. Consequently, while we ﬁnd both that higher moments matter, and that investors’ expectations of higher moments change through time, our results do not appear to be an explanation of bubble pricing in the Internet period.

# References

- [1] Abreau, D. and M. Brunnermeier, “Synchronization risk and delayed arbitrage”, 2002, Journal of Financial Economics 66, pp. 341-360.
- [2] Ait-Sahalia, Y. and M. Brandt, “Consumption and Portfolio Choice with Option-Implied State Prices”, 2007, Working Paper, Princeton University.
- [3] Ang, A., R. Hodrick, Y. Xing and X. Zhang, “The cross-section of volatility and expected returns,” 2006, Journal of Finance 51, pp. 259-299.
- [4] Ang, A., R. Hodrick, Y. Xing and X. Zhang, “High idiosyncratic volatility and low returns: International and further U.S. evidence,” 2006, forthcoming, Journal of Financial Economics.
- [5] Bakshi, G. and D. Madan, “Spanning and derivative-security valuation”, 2000, Journal of Financial Economics 55, pp. 205-238.
- [6] Bakshi, G., N. Kapadia and D. Madan, “Stock return characteristics, skew laws and the differential pricing of individual equity options”, 2003, Review of Financial Studies 16, pp. 101-143.
- [7] Barberis, N. and M. Huang, “Stocks as lotteries: The implications of probability weighting for security prices”, 2004, Unpublished manuscript, Yale University.
- [8] Bates, D., “The Crash of ’87: Was it expected? The evidence from options markets”, 1991, Journal of Finance 46, pp. 1009-1044.
- [9] Battalio, R. and P. Schultz, “Options and the bubble”, 2006, Journal of Finance 61, pp. 2071-2102.
- [10] Bekaert, G. and J. Liu, “Conditioning Information and Variance Bounds on Pricing Kernels”, 2004, Review of Financial Studies 17, 339-378.
- [11] Bekaert, G. and M. Urias, “Diversiﬁcation, Integration, and Emerging Market ClosedEnd Funds”, 1996, Journal of Finance 51, pp. 835-869.
- [12] Boyer, B., T. Mitton and K. Vorkink, “Expected Idiosyncratic Skewness”, 2008, Working Paper, Brigham Young University.
- [13] Brunnermeier, M.K., C. Gollier and J. Parker, “Optimal Beliefs, Asset Prices, and the Preference for Skewed Return”, 2007, Working Paper.

- [14] Campbell, J.Y., M. Lettau, B.G. Malkiel and Y. Xu,“Have Individual Stocks Become More Volatile? An Empirical Exploration of Idiosyncratic Risk”, 2001, Journal of Finance 56, pp. 1-43.
- [15] Carhart, M., 1997, “On persistence in mutual fund performance,” Journal of Finance 52, pp. 57-82.
- [16] Chabi-Yo, F., E. Ghysels and E. Renault, “Disentangling the Effects of Heterogeneous Beliefs and Preferences on Asset Prices”, 2006, Discussion Paper UNC.
- [17] Chen, Z. and P. Knez, 1996, “Portfolio Performance Measurement: Theory and Applications,” Review of Financial Studies 9, 511-555.
- [18] Chernov, M. and E. Ghysels, “A study towards a uniﬁed approach to the joint estimation of objective and risk neutral measures for the purpose of options valuation”, 2000, Journal of Financial Economics 56, pp. 407-458.
- [19] Daniel, K., M. Grinblatt, S. Titman, and R. Wermers, 1997, “Measuring mutual fund performance with characteristic based benchmarks,” Journal of Finance 52, 1035-1058.
- [20] Dennis, P. and S. Mayhew, “Risk-neutral skewness: Evidence from stock options”, 2002, Journal of Financial and Quantitative Analysis 37, pp. 471-493.
- [21] DeSantis, G., 1995, “Volitality bounds for stochastic discount factors: Tests and implications from international stock returns,” working paper, University of Southern California.
- [22] Dittmar, R.F., 2002, “Nonlinear pricing kernels, kurtosis preference, and evidence from the cross section of equity returns,” Journal of Finance 57, pp. 369-403.
- [23] Eriksson, A., L. Forsberg and E. Ghysels, (2004) Approximating the probability distribution of functions of random variables: A new approach, Discussion Paper, UNC.
- [24] Fama, E. and K. French, 1993, “Common risk factors in the returns on stocks and bonds,” Journal of Financial Economics 33, pp. 3-56.
- [25] Fama, E. and K. French, 1997, “Industry costs of equity,” Jouranl of Finance 52.
- [26] Ferson,W. and A.F. Siegel, “The Efﬁcient Use of Conditioning Information in Portfolios”, 2001 Journal of Finance 56, pp. 967-982.
- [27] Ferson,W. and A.F. Siegel, “Stochastic Discount Factor Bounds with Conditioning Information”, 2003, Review of Financial Studies 16, 567-595.

- [28] Foster, D.F. and D.B. Nelson,“Continuous Record Asympttics for Rolling Sample Variance Estimators”, 1996, Econometrica 64, 139-174.
- [29] Gallant, R., L.P. Hansen, and G. Tauchen, “Using Conditional Moments of Asset Payoffs to Infer the Volatility of Intertemporal Marginal Rates of Substitution”, 1990, Journal of Econometrics 45, 141-179.
- [30] Geczy, C., D. Musto and A. Reed, “Stocks are special too: An analysis of the equity lending market,” 2002, Journal of Financial Economics 66, pp. 241-269.
- [31] Gomes, J., L. Kogan, and M. Yogo, 2007, “Durability of output and expected stock returns,” Working paper, Wharton School, University of Pennsylvania.
- [32] Golubev, Y., W. Hardle,¨ and R. Timonfeev, 2008, “Testing Monotonicity of Pricing Kernels,” SFB 649 Discussion Papers, Humboldt University.
- [33] Hansen, L.P. and R. Jagannathan, “Implications of Security Market Data for Models of Dynamic Economies,” 1991, Journal of Political Economy 91, 249-265.
- [34] Harvey, C. and A. Siddique, “Conditional skewness in asset pricing tests,” 2000, Journal of Finance 55, pp. 1263-1296.
- [35] Huberman, G. and E. Kandel, “Mean-Variance Spanning”, 1987, Journal of Finance 42, pp. 873-888.
- [36] Jackwerth, J.,“Recovering Risk Aversion from Option Prices and Realized Returns”, 2000, Review of Financial Studies 13, pp. 433-451.
- [37] Jackwerth, J. and M. Rubinstein, “Recovering probability distributions from option prices”, 1996, Journal of Finance 51, pp. 1611-1631.
- [38] Mitton, T. and K. Vorkink, ”Equilibrium Underdiversiﬁcation and the Preference for Skewness”, 2007, Review of Financial Studies 20, pp. 1255-1288.
- [39] Ofek, E. and M. Richardson, 2003, “DotCom mania: The rise and fall and fall of internet stocks,” forthcoming, Journal of Finance.
- [40] Pastor, L. and R. Stambaugh, 2003, “Liquidity risk and expected stock returns,” Journal of Political Economy 111, pp. 642-685.
- [41] Rubinstein, M., “Nonparametric tests of alternative option pricing models using all reported trades and quotes on the 30 most active CBOE option classes from August 23, 1976 through August 31, 1978,” 1985, Journal of Finance 40, pp. 455-480.

- [42] Rubinstein, M., “Implied binomial trees,” 1994, Journal of Finance 49, pp. 771-818.
- [43] Shleifer, A. and R. Vishny, “The limits of arbitrage”, 1997, Journal of Finance 52, pp. 35-55.
- [44] Siegel, J., “Irrational exuberance, reconsidered,” December 6, 2006, Wall Street Journal.
- [45] Spiegel, M. and X. Wang, “Cross-sectional variation in stock returns: Liquidity and Idiosyncratic Risk,” 2006, Unpublished manuscript, Yale University.
- [46] Tversky, A., and D. Kahneman, “Advances in prospect theory: Cumulative representation of uncertainty,” 1992, Journal of Risk and Uncertainty 5, pp. 297-323.
- [47] Xing, Y., X. Zhang and R. Zhao, “What Does Individual Option Volatility Smirk Tell Us about Future Equity Returns?”, 2007, Working Paper, Rice University.

Table 1: Descriptive Statistics: Risk Neutral Moments

Entries to the table are the 5th percentile, median, and 95th percentiles of risk neutral volatility, skewness, and kurtosis across securities by year. We calculate the risk neutral moments following the procedure in Bakshi, Kapadia, and Madan (2003) using data on out of the money (OTM) puts and calls. We require at least two OTM puts and two OTM calls to calculate the moments. Further, we restrict attention to options with prices in excess of $0.50 for which we have at least 10 quotes per month and are not expiring within one week. Finally, we eliminate any options that violate put-call parity restrictions and lie in the extreme 1% of the distribution of the risk neutral moments. The sample consists of 3,722,700 option-day combinations over the time period January 1996 through December 2005.

[Figure 21]

[Figure 22]

Volatility Skewness Kurtosis Year P5 P50 P95 P5 P50 P95 P5 P50 P95

[Figure 23]

- 1996 11.404 24.283 42.289 -3.495 -0.449 0.601 1.386 4.713 20.592
- 1997 11.311 23.591 41.568 -3.834 -0.539 0.624 1.390 4.868 24.632
- 1998 12.283 24.533 45.381 -3.486 -0.464 0.695 1.444 5.012 22.684
- 1999 13.543 26.837 51.576 -3.727 -0.601 0.564 1.313 4.940 24.514
- 2000 16.140 30.942 57.531 -3.083 -0.562 0.511 1.344 4.682 20.318
- 2001 15.000 30.594 67.485 -2.959 -0.648 0.456 1.549 4.756 18.596
- 2002 14.119 27.659 67.315 -3.353 -0.742 0.539 1.658 5.515 22.356
- 2003 12.093 25.549 75.391 -4.315 -1.297 0.309 1.820 6.836 28.889
- 2004 10.276 24.021 68.945 -4.652 -1.399 0.398 2.040 8.239 34.943
- 2005 8.710 22.365 53.033 -5.164 -1.609 0.337 2.119 9.584 39.102

[Figure 24]

Table 2: Descriptive Statistics

Panels A-C present summary statistics for portfolios sorted on measures of ﬁrms’ risk-neutral moments. Firms are sorted on average risk-neutral volatility, skewness, and kurtosis within each calendar quarter into terciles based on 30th and 70th percentiles. We then form equally-weighted portfolios of these ﬁrms, holding the moment ranking constant for the subsequent calendar quarter. Risk-neutral moments are calculated using the procedure in Bakshi, Kapadia, and Madan (2003); the options used are those closest to one, three, six, and twelve months to maturity. The ﬁrst column of each panel presents mean monthly returns. The second column presents characteristic-adjusted returns, calculated by determining, for each ﬁrm, the Fama-French 5X5 size- and bookto-market portfolio to which it belongs and subtracting that return. The next three columns present the average beta, log market value and book-to-market equity ratio of the portfolio, while the next three columns present the average volatility, skewness and kurtosis of the portfolio. Monthly return data cover the period 4/96 through 12/05, for a total of 117 monthly observations.

Panel A: Volatility-Sorted Portfolios 1 Month to Maturity Rank Mean Char Adj Vol Skew Kurt Beta ln MV BM

[Figure 25]

[Figure 26]

[Figure 27]

- 1 1.213 0.268 16.104 -1.363 12.888 0.890 15.703 0.368
- 2 0.963 0.128 24.994 -0.968 8.842 1.281 14.304 0.393
- 3 0.893 0.172 44.033 -1.171 6.041 1.772 13.619 0.417

3-1 -0.320 -0.096 27.929 0.192 -6.847 0.883 -2.084 0.049

[Figure 28]

3 Months to Maturity Rank Mean Char Adj Vol Skew Kurt Beta ln MV BM

[Figure 29]

[Figure 30]

[Figure 31]

- 1 1.237 0.273 17.139 -1.180 10.812 0.837 15.675 0.386
- 2 1.061 0.190 26.458 -0.934 8.166 1.290 14.299 0.391
- 3 0.738 0.062 45.890 -1.203 5.993 1.828 13.648 0.402

3-1 -0.499 -0.211 28.751 -0.023 -4.819 0.990 -2.028 0.016

[Figure 32]

6 Months to Maturity Rank Mean Char Adj Vol Skew Kurt Beta ln MV BM

[Figure 33]

[Figure 34]

[Figure 35]

- 1 1.215 0.227 18.770 -0.713 6.621 0.816 15.617 0.397
- 2 1.137 0.266 28.656 -0.576 5.480 1.287 14.336 0.393
- 3 0.659 0.002 47.734 -0.749 4.148 1.861 13.658 0.386

3-1 -0.556 -0.225 28.964 -0.036 -2.473 1.045 -1.959 -0.012

[Figure 36]

12 Months to Maturity Rank Mean Char Adj Vol Skew Kurt Beta ln MV BM

[Figure 37]

[Figure 38]

[Figure 39]

- 1 1.237 0.227 19.353 -0.692 6.416 0.824 15.453 0.402
- 2 1.060 0.195 29.541 -0.615 5.544 1.291 14.350 0.391
- 3 0.739 0.098 49.892 -0.826 4.259 1.844 13.807 0.384

3-1 -0.498 -0.129 30.539 -0.134 -2.156 1.020 -1.646 -0.018

[Figure 40]

Table continued on next page...

Panel B: Skewness-Sorted Portfolios 1 Month to Maturity Rank Mean Char Adj Vol Skew Kurt Beta ln MV BM

[Figure 41]

[Figure 42]

[Figure 43]

- 1 1.233 0.391 26.626 -2.642 16.231 1.274 15.318 0.343
- 2 0.886 0.088 30.095 -0.975 6.847 1.365 14.351 0.398
- 3 0.975 0.110 26.699 0.116 5.365 1.228 13.961 0.436

3-1 -0.257 -0.281 0.074 2.758 -10.866 -0.046 -1.357 0.093

[Figure 44]

3 Months to Maturity Rank Mean Char Adj Vol Skew Kurt Beta ln MV BM

[Figure 45]

[Figure 46]

[Figure 47]

- 1 1.281 0.421 29.444 -2.530 14.303 1.262 15.283 0.354
- 2 0.944 0.146 31.132 -0.923 6.303 1.366 14.377 0.395
- 3 0.849 -0.009 27.345 0.131 4.992 1.242 13.961 0.429

3-1 -0.432 -0.430 -2.099 2.661 -9.311 -0.020 -1.322 0.076

[Figure 48]

6 Months to Maturity Rank Mean Char Adj Vol Skew Kurt Beta ln MV BM

[Figure 49]

[Figure 50]

[Figure 51]

- 1 1.341 0.476 32.812 -1.717 8.891 1.260 15.276 0.378
- 2 0.886 0.042 31.157 -0.527 4.181 1.318 14.444 0.390
- 3 0.867 0.085 30.353 0.190 3.614 1.311 13.874 0.412

3-1 -0.474 -0.391 -2.459 1.907 -5.277 0.051 -1.402 0.034

[Figure 52]

12 Months to Maturity Rank Mean Char Adj Vol Skew Kurt Beta ln MV BM

[Figure 53]

[Figure 54]

[Figure 55]

- 1 1.325 0.487 35.105 -1.835 9.206 1.242 15.364 0.374
- 2 0.888 0.027 32.013 -0.524 4.008 1.326 14.398 0.392
- 3 0.881 0.090 30.842 0.195 3.522 1.319 13.847 0.413

3-1 -0.444 -0.397 -4.263 2.030 -5.684 0.077 -1.518 0.039 Table continued on next page...

[Figure 56]

Panel C: Kurtosis-Sorted Portfolios 1 Month to Maturity

[Figure 57]

[Figure 58]

Rank Mean Char Adj Vol Skew Kurt Beta ln MV BM 1 1.020 0.172 35.337 -0.358 2.864 1.387 13.665 0.461 2 0.925 0.110 27.185 -0.909 6.976 1.293 14.388 0.394 3 1.137 0.309 21.876 -2.254 18.556 1.217 15.556 0.325

[Figure 59]

3-1 0.117 0.138 -13.461 -1.896 15.691 -0.170 1.891 -0.136

[Figure 60]

3 Months to Maturity Rank Mean Char Adj Vol Skew Kurt Beta ln MV BM 1 0.938 0.109 35.972 -0.346 2.775 1.418 13.650 0.452 2 0.901 0.075 28.714 -0.865 6.482 1.310 14.401 0.391 3 1.251 0.410 24.049 -2.129 16.280 1.169 15.550 0.338

[Figure 61]

[Figure 62]

[Figure 63]

3-1 0.313 0.301 -11.923 -1.782 13.505 -0.249 1.899 -0.115

[Figure 64]

6 Months to Maturity Rank Mean Char Adj Vol Skew Kurt Beta ln MV BM 1 0.860 0.029 37.226 -0.189 2.155 1.449 13.661 0.427 2 0.987 0.149 30.722 -0.499 4.249 1.324 14.426 0.386 3 1.213 0.383 26.522 -1.375 10.259 1.124 15.507 0.370

[Figure 65]

[Figure 66]

[Figure 67]

3-1 0.353 0.354 -10.704 -1.186 8.104 -0.325 1.847 -0.057

[Figure 68]

12 Months to Maturity Rank Mean Char Adj Vol Skew Kurt Beta ln MV BM 1 0.857 0.019 37.729 -0.179 2.097 1.465 13.669 0.424 2 0.980 0.158 32.052 -0.497 4.103 1.330 14.394 0.388 3 1.226 0.383 28.165 -1.496 10.502 1.102 15.542 0.369

[Figure 69]

[Figure 70]

[Figure 71]

3-1 0.369 0.364 -9.564 -1.316 8.404 -0.363 1.873 -0.055

[Figure 72]

Table 3: Time Series Regressions

The table presents the results of time series regressions of excess return differentials (Hi-Lo) between portfolios ranked on risk neutral volatility, skewness, and kurtosis on the three Fama and French (1993) factors MRP (the return on the value-weighted market portfolio in excess of a one-month T-Bill), SMB (the difference in returns on a portfolio of small capitalization and large capitalization stocks), and HML (the difference in returns on a portfolio of high and low book equity to market equity stocks). The moment-sorted portfolios are equally-weighted, formed on the basis of terciles and re-formed each quarter. The table presents point estimates of the coefﬁcients and standard errors in parentheses. Data cover the period April 1996 through December 2005 for 117 monthly observations.

Panel A: 1 Month to Maturity Panel B: 3 Months to Maturity

[Figure 73]

[Figure 74]

[Figure 75]

[Figure 76]

[Figure 77]

[Figure 78]

[Figure 79]

[Figure 80]

[Figure 81]

[Figure 82]

[Figure 83]

[Figure 84]

[Figure 85]

[Figure 86]

[Figure 87]

[Figure 88]

[Figure 89]

[Figure 90]

[Figure 91]

[Figure 92]

[Figure 93]

[Figure 94]

[Figure 95]

[Figure 96]

[Figure 97]

[Figure 98]

[Figure 99]

[Figure 100]

[Figure 101]

[Figure 102]

[Figure 103]

[Figure 104]

[Figure 105]

[Figure 106]

[Figure 107]

[Figure 108]

[Figure 109]

[Figure 110]

[Figure 111]

[Figure 112]

[Figure 113]

[Figure 114]

[Figure 115]

[Figure 116]

[Figure 117]

[Figure 118]

[Figure 119]

[Figure 120]

[Figure 121]

[Figure 122]

[Figure 123]

[Figure 124]

[Figure 125]

[Figure 126]

[Figure 127]

[Figure 128]

[Figure 129]

[Figure 130]

[Figure 131]

[Figure 132]

[Figure 133]

[Figure 134]

[Figure 135]

[Figure 136]

[Figure 137]

[Figure 138]

[Figure 139]

[Figure 140]

[Figure 141]

[Figure 142]

[Figure 143]

[Figure 144]

[Figure 145]

[Figure 146]

[Figure 147]

[Figure 148]

[Figure 149]

[Figure 150]

[Figure 151]

[Figure 152]

[Figure 153]

[Figure 154]

[Figure 155]

[Figure 156]

[Figure 157]

[Figure 158]

[Figure 159]

[Figure 160]

[Figure 161]

[Figure 162]

[Figure 163]

[Figure 164]

[Figure 165]

[Figure 166]

[Figure 167]

[Figure 168]

[Figure 169]

[Figure 170]

[Figure 171]

[Figure 172]

[Figure 173]

[Figure 174]

[Figure 175]

[Figure 176]

[Figure 177]

[Figure 178]

[Figure 179]

[Figure 180]

[Figure 181]

[Figure 182]

[Figure 183]

[Figure 184]

[Figure 185]

[Figure 186]

[Figure 187]

[Figure 188]

[Figure 189]

[Figure 190]

[Figure 191]

[Figure 192]

[Figure 193]

[Figure 194]

[Figure 195]

[Figure 196]

[Figure 197]

[Figure 198]

[Figure 199]

[Figure 200]

[Figure 201]

[Figure 202]

[Figure 203]

[Figure 204]

[Figure 205]

[Figure 206]

[Figure 207]

[Figure 208]

[Figure 209]

[Figure 210]

[Figure 211]

[Figure 212]

[Figure 213]

[Figure 214]

[Figure 215]

[Figure 216]

[Figure 217]

[Figure 218]

[Figure 219]

[Figure 220]

[Figure 221]

[Figure 222]

[Figure 223]

[Figure 224]

[Figure 225]

[Figure 226]

[Figure 227]

[Figure 228]

[Figure 229]

[Figure 230]

[Figure 231]

[Figure 232]

[Figure 233]

[Figure 234]

[Figure 235]

[Figure 236]

[Figure 237]

[Figure 238]

[Figure 239]

[Figure 240]

[Figure 241]

[Figure 242]

[Figure 243]

[Figure 244]

[Figure 245]

[Figure 246]

[Figure 247]

[Figure 248]

[Figure 249]

[Figure 250]

[Figure 251]

[Figure 252]

[Figure 253]

[Figure 254]

[Figure 255]

[Figure 256]

[Figure 257]

[Figure 258]

[Figure 259]

[Figure 260]

[Figure 261]

[Figure 262]

[Figure 263]

[Figure 264]

[Figure 265]

[Figure 266]

[Figure 267]

[Figure 268]

[Figure 269]

[Figure 270]

[Figure 271]

[Figure 272]

[Figure 273]

[Figure 274]

[Figure 275]

[Figure 276]

[Figure 277]

[Figure 278]

[Figure 279]

[Figure 280]

[Figure 281]

[Figure 282]

[Figure 283]

[Figure 284]

[Figure 285]

[Figure 286]

[Figure 287]

[Figure 288]

[Figure 289]

[Figure 290]

[Figure 291]

[Figure 292]

[Figure 293]

[Figure 294]

[Figure 295]

[Figure 296]

[Figure 297]

[Figure 298]

[Figure 299]

[Figure 300]

[Figure 301]

[Figure 302]

[Figure 303]

[Figure 304]

[Figure 305]

[Figure 306]

[Figure 307]

[Figure 308]

[Figure 309]

[Figure 310]

[Figure 311]

[Figure 312]

[Figure 313]

[Figure 314]

[Figure 315]

[Figure 316]

[Figure 317]

[Figure 318]

[Figure 319]

[Figure 320]

[Figure 321]

[Figure 322]

[Figure 323]

[Figure 324]

[Figure 325]

[Figure 326]

[Figure 327]

[Figure 328]

[Figure 329]

[Figure 330]

[Figure 331]

[Figure 332]

[Figure 333]

[Figure 334]

[Figure 335]

[Figure 336]

[Figure 337]

[Figure 338]

[Figure 339]

[Figure 340]

[Figure 341]

[Figure 342]

[Figure 343]

[Figure 344]

[Figure 345]

[Figure 346]

[Figure 347]

[Figure 348]

[Figure 349]

[Figure 350]

[Figure 351]

[Figure 352]

[Figure 353]

[Figure 354]

[Figure 355]

[Figure 356]

[Figure 357]

[Figure 358]

[Figure 359]

[Figure 360]

[Figure 361]

[Figure 362]

[Figure 363]

[Figure 364]

[Figure 365]

[Figure 366]

[Figure 367]

[Figure 368]

[Figure 369]

[Figure 370]

[Figure 371]

[Figure 372]

[Figure 373]

[Figure 374]

[Figure 375]

[Figure 376]

[Figure 377]

[Figure 378]

[Figure 379]

[Figure 380]

[Figure 381]

[Figure 382]

[Figure 383]

[Figure 384]

[Figure 385]

[Figure 386]

[Figure 387]

[Figure 388]

[Figure 389]

[Figure 390]

[Figure 391]

[Figure 392]

[Figure 393]

[Figure 394]

[Figure 395]

[Figure 396]

[Figure 397]

[Figure 398]

[Figure 399]

[Figure 400]

[Figure 401]

[Figure 402]

[Figure 403]

[Figure 404]

[Figure 405]

[Figure 406]

[Figure 407]

[Figure 408]

[Figure 409]

[Figure 410]

[Figure 411]

[Figure 412]

[Figure 413]

[Figure 414]

[Figure 415]

[Figure 416]

[Figure 417]

[Figure 418]

[Figure 419]

[Figure 420]

[Figure 421]

[Figure 422]

[Figure 423]

[Figure 424]

[Figure 425]

[Figure 426]

[Figure 427]

[Figure 428]

[Figure 429]

[Figure 430]

[Figure 431]

[Figure 432]

[Figure 433]

[Figure 434]

[Figure 435]

[Figure 436]

[Figure 437]

[Figure 438]

[Figure 439]

[Figure 440]

[Figure 441]

[Figure 442]

[Figure 443]

[Figure 444]

[Figure 445]

[Figure 446]

[Figure 447]

[Figure 448]

[Figure 449]

[Figure 450]

[Figure 451]

[Figure 452]

[Figure 453]

[Figure 454]

[Figure 455]

[Figure 456]

[Figure 457]

[Figure 458]

[Figure 459]

[Figure 460]

[Figure 461]

[Figure 462]

[Figure 463]

[Figure 464]

[Figure 465]

[Figure 466]

[Figure 467]

[Figure 468]

[Figure 469]

[Figure 470]

[Figure 471]

[Figure 472]

[Figure 473]

[Figure 474]

[Figure 475]

[Figure 476]

[Figure 477]

[Figure 478]

[Figure 479]

[Figure 480]

[Figure 481]

[Figure 482]

[Figure 483]

[Figure 484]

[Figure 485]

[Figure 486]

[Figure 487]

[Figure 488]

[Figure 489]

[Figure 490]

[Figure 491]

[Figure 492]

[Figure 493]

[Figure 494]

[Figure 495]

[Figure 496]

[Figure 497]

[Figure 498]

[Figure 499]

[Figure 500]

[Figure 501]

[Figure 502]

[Figure 503]

[Figure 504]

[Figure 505]

[Figure 506]

[Figure 507]

[Figure 508]

[Figure 509]

[Figure 510]

[Figure 511]

[Figure 512]

[Figure 513]

[Figure 514]

[Figure 515]

[Figure 516]

[Figure 517]

[Figure 518]

[Figure 519]

[Figure 520]

[Figure 521]

[Figure 522]

[Figure 523]

[Figure 524]

α βMRP βSMB βHML R2 α βMRP βSMB βHML R2 Vol -0.57 0.51 0.83 -0.55 0.76 Vol -0.56 0.56 0.89 -1.03 0.84

[Figure 525]

[Figure 526]

[Figure 527]

[Figure 528]

[Figure 529]

[Figure 530]

[Figure 531]

[Figure 532]

[Figure 533]

[Figure 534]

[Figure 535]

[Figure 536]

- -1.77 5.34 9.23 -5.29 -1.65 5.00 10.21 -8.92 Skew -0.58 0.14 -0.05 0.55 0.27 Skew -0.67 0.19 -0.13 0.37 0.17
- -1.71 1.66 -0.37 4.23 -1.99 2.34 -0.83 2.63

- Kurt 0.55 -0.20 -0.30 -0.51 0.28 Kurt 0.62 -0.30 -0.23 -0.16 0.21 2.49 -3.49 -3.17 -6.32 2.45 -4.42 -1.97 -1.37

[Figure 537]

[Figure 538]

[Figure 539]

[Figure 540]

[Figure 541]

[Figure 542]

[Figure 543]

[Figure 544]

[Figure 545]

[Figure 546]

[Figure 547]

[Figure 548]

Panel C: 6 Months to Maturity Panel D: 12 Months to Maturity

[Figure 549]

[Figure 550]

[Figure 551]

[Figure 552]

[Figure 553]

[Figure 554]

[Figure 555]

[Figure 556]

[Figure 557]

[Figure 558]

[Figure 559]

[Figure 560]

[Figure 561]

[Figure 562]

[Figure 563]

[Figure 564]

[Figure 565]

[Figure 566]

[Figure 567]

[Figure 568]

[Figure 569]

[Figure 570]

[Figure 571]

[Figure 572]

[Figure 573]

[Figure 574]

[Figure 575]

[Figure 576]

[Figure 577]

[Figure 578]

[Figure 579]

[Figure 580]

[Figure 581]

[Figure 582]

[Figure 583]

[Figure 584]

[Figure 585]

[Figure 586]

[Figure 587]

[Figure 588]

[Figure 589]

[Figure 590]

[Figure 591]

[Figure 592]

[Figure 593]

[Figure 594]

[Figure 595]

[Figure 596]

[Figure 597]

[Figure 598]

[Figure 599]

[Figure 600]

[Figure 601]

[Figure 602]

[Figure 603]

[Figure 604]

[Figure 605]

[Figure 606]

[Figure 607]

[Figure 608]

[Figure 609]

[Figure 610]

[Figure 611]

[Figure 612]

[Figure 613]

[Figure 614]

[Figure 615]

[Figure 616]

[Figure 617]

[Figure 618]

[Figure 619]

[Figure 620]

[Figure 621]

[Figure 622]

[Figure 623]

[Figure 624]

[Figure 625]

[Figure 626]

[Figure 627]

[Figure 628]

[Figure 629]

[Figure 630]

[Figure 631]

[Figure 632]

[Figure 633]

[Figure 634]

[Figure 635]

[Figure 636]

[Figure 637]

[Figure 638]

[Figure 639]

[Figure 640]

[Figure 641]

[Figure 642]

[Figure 643]

[Figure 644]

[Figure 645]

[Figure 646]

[Figure 647]

[Figure 648]

[Figure 649]

[Figure 650]

[Figure 651]

[Figure 652]

[Figure 653]

[Figure 654]

[Figure 655]

[Figure 656]

[Figure 657]

[Figure 658]

[Figure 659]

[Figure 660]

[Figure 661]

[Figure 662]

[Figure 663]

[Figure 664]

[Figure 665]

[Figure 666]

[Figure 667]

[Figure 668]

[Figure 669]

[Figure 670]

[Figure 671]

[Figure 672]

[Figure 673]

[Figure 674]

[Figure 675]

[Figure 676]

[Figure 677]

[Figure 678]

[Figure 679]

[Figure 680]

[Figure 681]

[Figure 682]

[Figure 683]

[Figure 684]

[Figure 685]

[Figure 686]

[Figure 687]

[Figure 688]

[Figure 689]

[Figure 690]

[Figure 691]

[Figure 692]

[Figure 693]

[Figure 694]

[Figure 695]

[Figure 696]

[Figure 697]

[Figure 698]

[Figure 699]

[Figure 700]

[Figure 701]

[Figure 702]

[Figure 703]

[Figure 704]

[Figure 705]

[Figure 706]

[Figure 707]

[Figure 708]

[Figure 709]

[Figure 710]

[Figure 711]

[Figure 712]

[Figure 713]

[Figure 714]

[Figure 715]

[Figure 716]

[Figure 717]

[Figure 718]

[Figure 719]

[Figure 720]

[Figure 721]

[Figure 722]

[Figure 723]

[Figure 724]

[Figure 725]

[Figure 726]

[Figure 727]

[Figure 728]

[Figure 729]

[Figure 730]

[Figure 731]

[Figure 732]

[Figure 733]

[Figure 734]

[Figure 735]

[Figure 736]

[Figure 737]

[Figure 738]

[Figure 739]

[Figure 740]

[Figure 741]

[Figure 742]

[Figure 743]

[Figure 744]

[Figure 745]

[Figure 746]

[Figure 747]

[Figure 748]

[Figure 749]

[Figure 750]

[Figure 751]

[Figure 752]

[Figure 753]

[Figure 754]

[Figure 755]

[Figure 756]

[Figure 757]

[Figure 758]

[Figure 759]

[Figure 760]

[Figure 761]

[Figure 762]

[Figure 763]

[Figure 764]

[Figure 765]

[Figure 766]

[Figure 767]

[Figure 768]

[Figure 769]

[Figure 770]

[Figure 771]

[Figure 772]

[Figure 773]

[Figure 774]

[Figure 775]

[Figure 776]

[Figure 777]

[Figure 778]

[Figure 779]

[Figure 780]

[Figure 781]

[Figure 782]

[Figure 783]

[Figure 784]

[Figure 785]

[Figure 786]

[Figure 787]

[Figure 788]

[Figure 789]

[Figure 790]

[Figure 791]

[Figure 792]

[Figure 793]

[Figure 794]

[Figure 795]

[Figure 796]

[Figure 797]

[Figure 798]

[Figure 799]

[Figure 800]

[Figure 801]

[Figure 802]

[Figure 803]

[Figure 804]

[Figure 805]

[Figure 806]

[Figure 807]

[Figure 808]

[Figure 809]

[Figure 810]

[Figure 811]

[Figure 812]

[Figure 813]

[Figure 814]

[Figure 815]

[Figure 816]

[Figure 817]

[Figure 818]

[Figure 819]

[Figure 820]

[Figure 821]

[Figure 822]

[Figure 823]

[Figure 824]

[Figure 825]

[Figure 826]

[Figure 827]

[Figure 828]

[Figure 829]

[Figure 830]

[Figure 831]

[Figure 832]

[Figure 833]

[Figure 834]

[Figure 835]

[Figure 836]

[Figure 837]

[Figure 838]

[Figure 839]

[Figure 840]

[Figure 841]

[Figure 842]

[Figure 843]

[Figure 844]

[Figure 845]

[Figure 846]

[Figure 847]

[Figure 848]

[Figure 849]

[Figure 850]

[Figure 851]

[Figure 852]

[Figure 853]

[Figure 854]

[Figure 855]

[Figure 856]

[Figure 857]

[Figure 858]

[Figure 859]

[Figure 860]

[Figure 861]

[Figure 862]

[Figure 863]

[Figure 864]

[Figure 865]

[Figure 866]

[Figure 867]

[Figure 868]

[Figure 869]

[Figure 870]

[Figure 871]

[Figure 872]

[Figure 873]

[Figure 874]

[Figure 875]

[Figure 876]

[Figure 877]

[Figure 878]

[Figure 879]

[Figure 880]

[Figure 881]

[Figure 882]

[Figure 883]

[Figure 884]

[Figure 885]

[Figure 886]

[Figure 887]

[Figure 888]

[Figure 889]

[Figure 890]

[Figure 891]

[Figure 892]

[Figure 893]

[Figure 894]

[Figure 895]

[Figure 896]

[Figure 897]

[Figure 898]

[Figure 899]

[Figure 900]

[Figure 901]

[Figure 902]

[Figure 903]

[Figure 904]

[Figure 905]

[Figure 906]

[Figure 907]

[Figure 908]

[Figure 909]

[Figure 910]

[Figure 911]

[Figure 912]

[Figure 913]

[Figure 914]

[Figure 915]

[Figure 916]

[Figure 917]

[Figure 918]

[Figure 919]

[Figure 920]

[Figure 921]

[Figure 922]

[Figure 923]

[Figure 924]

[Figure 925]

[Figure 926]

[Figure 927]

[Figure 928]

[Figure 929]

[Figure 930]

[Figure 931]

[Figure 932]

[Figure 933]

[Figure 934]

[Figure 935]

[Figure 936]

[Figure 937]

[Figure 938]

[Figure 939]

[Figure 940]

[Figure 941]

[Figure 942]

[Figure 943]

[Figure 944]

[Figure 945]

[Figure 946]

[Figure 947]

[Figure 948]

[Figure 949]

[Figure 950]

[Figure 951]

[Figure 952]

[Figure 953]

[Figure 954]

[Figure 955]

[Figure 956]

[Figure 957]

[Figure 958]

[Figure 959]

[Figure 960]

[Figure 961]

[Figure 962]

[Figure 963]

[Figure 964]

[Figure 965]

[Figure 966]

[Figure 967]

[Figure 968]

[Figure 969]

[Figure 970]

[Figure 971]

[Figure 972]

[Figure 973]

[Figure 974]

[Figure 975]

[Figure 976]

[Figure 977]

[Figure 978]

[Figure 979]

[Figure 980]

[Figure 981]

[Figure 982]

[Figure 983]

[Figure 984]

[Figure 985]

[Figure 986]

[Figure 987]

[Figure 988]

[Figure 989]

[Figure 990]

[Figure 991]

[Figure 992]

[Figure 993]

[Figure 994]

[Figure 995]

[Figure 996]

[Figure 997]

[Figure 998]

[Figure 999]

[Figure 1000]

α βMRP βSMB βHML R2 α βMRP βSMB βHML R2 Vol -0.55 0.59 0.90 -1.22 0.85 Vol -0.41 0.54 0.83 -1.29 0.85

[Figure 1001]

[Figure 1002]

[Figure 1003]

[Figure 1004]

[Figure 1005]

[Figure 1006]

[Figure 1007]

[Figure 1008]

[Figure 1009]

[Figure 1010]

[Figure 1011]

[Figure 1012]

- -1.54 5.06 10.37 -9.73 -1.16 4.70 10.20 -10.49

Skew -0.64 0.18 0.00 0.14 0.05 Skew -0.62 0.20 0.06 0.11 0.07

- -2.43 2.48 0.00 1.10 -2.42 2.83 0.42 0.88

- Kurt 0.56 -0.35 -0.26 0.10 0.44 Kurt 0.62 -0.38 -0.31 0.10 0.50 2.38 -4.25 -2.15 0.95 2.65 -4.65 -2.51 0.96

[Figure 1013]

[Figure 1014]

[Figure 1015]

[Figure 1016]

[Figure 1017]

[Figure 1018]

[Figure 1019]

[Figure 1020]

[Figure 1021]

[Figure 1022]

[Figure 1023]

[Figure 1024]

Table 4: Stochastic Discount Factor Risk Adjustments

The table presents risk adjustments for the volatility, skewness, and kurtosis factor mimicking portfolios using stochastic discount factors implied by the S&P 500 risk neutral and physical densities. The table presents returns in excess of those implied by discounting using the stochastic discount factor, calculated as

T

1 T

αˆ =

rtmt

[Figure 1025]

t=1

where rt is the return on the factor-mimicking portfolio at time t, and mt is the stochastic discount factor. Columns “Linear,” “Quad,” and “Cubic” represent discount factors obtained by projecting the density-implied discount factor onto a linear, quadratic, and cubic polynomial, respectively. Panel A presents results using overlapping quarterly returns and the discount factor implied by 3 month maturity options; Panels B and C present similar results using 6 month and 12 month horizons. Point estimates are scaled to the monthly frequency. Newey-West standard errors are presented in parentheses below the point estimates. Data in Panel A extend from June, 1996 through December, 2005 for 115 monthly observations. Data in Panel B cover the period September, 1996 through December, 2005 for 112 monthly observations. Data in Panel C cover the period March, 1996 through December, 2005 for 106 monthly observations.

Panel A: 3 Months Panel B: 6 Months

[Figure 1026]

[Figure 1027]

[Figure 1028]

[Figure 1029]

[Figure 1030]

[Figure 1031]

[Figure 1032]

[Figure 1033]

[Figure 1034]

[Figure 1035]

[Figure 1036]

[Figure 1037]

[Figure 1038]

[Figure 1039]

[Figure 1040]

[Figure 1041]

[Figure 1042]

[Figure 1043]

[Figure 1044]

[Figure 1045]

[Figure 1046]

[Figure 1047]

[Figure 1048]

[Figure 1049]

[Figure 1050]

[Figure 1051]

[Figure 1052]

[Figure 1053]

[Figure 1054]

[Figure 1055]

[Figure 1056]

[Figure 1057]

[Figure 1058]

[Figure 1059]

[Figure 1060]

[Figure 1061]

[Figure 1062]

[Figure 1063]

[Figure 1064]

[Figure 1065]

[Figure 1066]

[Figure 1067]

[Figure 1068]

[Figure 1069]

[Figure 1070]

[Figure 1071]

[Figure 1072]

[Figure 1073]

[Figure 1074]

[Figure 1075]

[Figure 1076]

[Figure 1077]

[Figure 1078]

[Figure 1079]

[Figure 1080]

[Figure 1081]

[Figure 1082]

[Figure 1083]

[Figure 1084]

[Figure 1085]

[Figure 1086]

[Figure 1087]

[Figure 1088]

[Figure 1089]

[Figure 1090]

[Figure 1091]

[Figure 1092]

[Figure 1093]

[Figure 1094]

[Figure 1095]

[Figure 1096]

[Figure 1097]

[Figure 1098]

[Figure 1099]

[Figure 1100]

[Figure 1101]

[Figure 1102]

[Figure 1103]

[Figure 1104]

[Figure 1105]

[Figure 1106]

[Figure 1107]

[Figure 1108]

[Figure 1109]

[Figure 1110]

[Figure 1111]

[Figure 1112]

[Figure 1113]

[Figure 1114]

[Figure 1115]

[Figure 1116]

[Figure 1117]

[Figure 1118]

[Figure 1119]

[Figure 1120]

[Figure 1121]

[Figure 1122]

[Figure 1123]

[Figure 1124]

[Figure 1125]

[Figure 1126]

[Figure 1127]

[Figure 1128]

[Figure 1129]

[Figure 1130]

[Figure 1131]

[Figure 1132]

[Figure 1133]

[Figure 1134]

[Figure 1135]

[Figure 1136]

[Figure 1137]

[Figure 1138]

[Figure 1139]

[Figure 1140]

[Figure 1141]

[Figure 1142]

[Figure 1143]

[Figure 1144]

[Figure 1145]

[Figure 1146]

[Figure 1147]

[Figure 1148]

[Figure 1149]

[Figure 1150]

[Figure 1151]

[Figure 1152]

[Figure 1153]

[Figure 1154]

[Figure 1155]

[Figure 1156]

[Figure 1157]

[Figure 1158]

[Figure 1159]

[Figure 1160]

[Figure 1161]

[Figure 1162]

[Figure 1163]

[Figure 1164]

[Figure 1165]

[Figure 1166]

[Figure 1167]

[Figure 1168]

[Figure 1169]

[Figure 1170]

[Figure 1171]

[Figure 1172]

[Figure 1173]

[Figure 1174]

[Figure 1175]

[Figure 1176]

[Figure 1177]

[Figure 1178]

[Figure 1179]

[Figure 1180]

[Figure 1181]

[Figure 1182]

[Figure 1183]

[Figure 1184]

[Figure 1185]

[Figure 1186]

[Figure 1187]

[Figure 1188]

[Figure 1189]

[Figure 1190]

[Figure 1191]

[Figure 1192]

[Figure 1193]

[Figure 1194]

[Figure 1195]

[Figure 1196]

[Figure 1197]

[Figure 1198]

[Figure 1199]

[Figure 1200]

[Figure 1201]

[Figure 1202]

[Figure 1203]

[Figure 1204]

[Figure 1205]

[Figure 1206]

[Figure 1207]

[Figure 1208]

[Figure 1209]

[Figure 1210]

[Figure 1211]

[Figure 1212]

[Figure 1213]

[Figure 1214]

[Figure 1215]

[Figure 1216]

[Figure 1217]

[Figure 1218]

[Figure 1219]

[Figure 1220]

[Figure 1221]

[Figure 1222]

[Figure 1223]

[Figure 1224]

[Figure 1225]

[Figure 1226]

[Figure 1227]

[Figure 1228]

[Figure 1229]

[Figure 1230]

[Figure 1231]

[Figure 1232]

[Figure 1233]

[Figure 1234]

[Figure 1235]

[Figure 1236]

[Figure 1237]

[Figure 1238]

[Figure 1239]

[Figure 1240]

[Figure 1241]

[Figure 1242]

[Figure 1243]

[Figure 1244]

[Figure 1245]

[Figure 1246]

[Figure 1247]

[Figure 1248]

[Figure 1249]

[Figure 1250]

[Figure 1251]

[Figure 1252]

[Figure 1253]

[Figure 1254]

[Figure 1255]

[Figure 1256]

[Figure 1257]

[Figure 1258]

[Figure 1259]

[Figure 1260]

[Figure 1261]

[Figure 1262]

[Figure 1263]

[Figure 1264]

[Figure 1265]

[Figure 1266]

[Figure 1267]

[Figure 1268]

[Figure 1269]

[Figure 1270]

[Figure 1271]

[Figure 1272]

[Figure 1273]

[Figure 1274]

[Figure 1275]

[Figure 1276]

[Figure 1277]

[Figure 1278]

[Figure 1279]

[Figure 1280]

[Figure 1281]

[Figure 1282]

[Figure 1283]

[Figure 1284]

[Figure 1285]

[Figure 1286]

[Figure 1287]

[Figure 1288]

[Figure 1289]

[Figure 1290]

[Figure 1291]

[Figure 1292]

[Figure 1293]

[Figure 1294]

[Figure 1295]

[Figure 1296]

[Figure 1297]

[Figure 1298]

[Figure 1299]

[Figure 1300]

[Figure 1301]

[Figure 1302]

[Figure 1303]

[Figure 1304]

[Figure 1305]

[Figure 1306]

[Figure 1307]

[Figure 1308]

[Figure 1309]

[Figure 1310]

[Figure 1311]

[Figure 1312]

[Figure 1313]

[Figure 1314]

[Figure 1315]

[Figure 1316]

[Figure 1317]

[Figure 1318]

[Figure 1319]

[Figure 1320]

[Figure 1321]

[Figure 1322]

[Figure 1323]

[Figure 1324]

[Figure 1325]

[Figure 1326]

[Figure 1327]

[Figure 1328]

[Figure 1329]

[Figure 1330]

[Figure 1331]

[Figure 1332]

[Figure 1333]

[Figure 1334]

[Figure 1335]

[Figure 1336]

[Figure 1337]

[Figure 1338]

[Figure 1339]

[Figure 1340]

[Figure 1341]

[Figure 1342]

[Figure 1343]

[Figure 1344]

[Figure 1345]

[Figure 1346]

[Figure 1347]

[Figure 1348]

[Figure 1349]

[Figure 1350]

[Figure 1351]

[Figure 1352]

[Figure 1353]

[Figure 1354]

[Figure 1355]

[Figure 1356]

[Figure 1357]

[Figure 1358]

[Figure 1359]

[Figure 1360]

[Figure 1361]

[Figure 1362]

[Figure 1363]

[Figure 1364]

[Figure 1365]

[Figure 1366]

[Figure 1367]

[Figure 1368]

[Figure 1369]

[Figure 1370]

[Figure 1371]

[Figure 1372]

[Figure 1373]

[Figure 1374]

[Figure 1375]

[Figure 1376]

[Figure 1377]

[Figure 1378]

[Figure 1379]

[Figure 1380]

[Figure 1381]

[Figure 1382]

[Figure 1383]

[Figure 1384]

[Figure 1385]

[Figure 1386]

[Figure 1387]

[Figure 1388]

[Figure 1389]

[Figure 1390]

[Figure 1391]

[Figure 1392]

[Figure 1393]

[Figure 1394]

[Figure 1395]

[Figure 1396]

[Figure 1397]

[Figure 1398]

[Figure 1399]

[Figure 1400]

[Figure 1401]

[Figure 1402]

[Figure 1403]

[Figure 1404]

[Figure 1405]

[Figure 1406]

[Figure 1407]

[Figure 1408]

[Figure 1409]

[Figure 1410]

[Figure 1411]

[Figure 1412]

[Figure 1413]

[Figure 1414]

[Figure 1415]

[Figure 1416]

[Figure 1417]

[Figure 1418]

[Figure 1419]

[Figure 1420]

[Figure 1421]

[Figure 1422]

[Figure 1423]

[Figure 1424]

[Figure 1425]

[Figure 1426]

[Figure 1427]

[Figure 1428]

[Figure 1429]

[Figure 1430]

[Figure 1431]

[Figure 1432]

[Figure 1433]

[Figure 1434]

[Figure 1435]

[Figure 1436]

[Figure 1437]

[Figure 1438]

[Figure 1439]

[Figure 1440]

[Figure 1441]

[Figure 1442]

[Figure 1443]

[Figure 1444]

[Figure 1445]

[Figure 1446]

[Figure 1447]

[Figure 1448]

[Figure 1449]

[Figure 1450]

[Figure 1451]

[Figure 1452]

[Figure 1453]

[Figure 1454]

[Figure 1455]

[Figure 1456]

[Figure 1457]

[Figure 1458]

[Figure 1459]

NIG Linear Quad Cubic NIG Linear Quad Cubic Vol -0.405 -0.358 -0.437 -0.192 Vol -0.081 -0.285 -0.089 0.645 SE (0.844) (0.893) (0.895) (0.797) SE (1.180) (1.182) (1.265) (1.205)

[Figure 1460]

[Figure 1461]

[Figure 1462]

[Figure 1463]

[Figure 1464]

[Figure 1465]

[Figure 1466]

[Figure 1467]

[Figure 1468]

[Figure 1469]

Skew -0.594 -0.620 -0.619 -0.597 Skew -0.631 -0.626 -0.636 -0.631

SE (0.381) (0.401) (0.402) (0.377) SE (0.283) (0.281) (0.293) (0.303) Kurt 0.479 0.456 0.512 0.450 Kurt 0.345 0.403 0.367 0.118

SE (0.254) (0.254) (0.263) (0.265) SE (0.321) (0.327) (0.335) (0.294)

[Figure 1470]

[Figure 1471]

[Figure 1472]

[Figure 1473]

[Figure 1474]

[Figure 1475]

[Figure 1476]

[Figure 1477]

[Figure 1478]

[Figure 1479]

Panel C: 12 Months

[Figure 1480]

[Figure 1481]

[Figure 1482]

[Figure 1483]

[Figure 1484]

[Figure 1485]

[Figure 1486]

[Figure 1487]

[Figure 1488]

[Figure 1489]

[Figure 1490]

[Figure 1491]

[Figure 1492]

[Figure 1493]

[Figure 1494]

[Figure 1495]

[Figure 1496]

[Figure 1497]

[Figure 1498]

[Figure 1499]

[Figure 1500]

[Figure 1501]

[Figure 1502]

[Figure 1503]

[Figure 1504]

[Figure 1505]

[Figure 1506]

[Figure 1507]

[Figure 1508]

[Figure 1509]

[Figure 1510]

[Figure 1511]

[Figure 1512]

[Figure 1513]

[Figure 1514]

[Figure 1515]

[Figure 1516]

[Figure 1517]

[Figure 1518]

[Figure 1519]

[Figure 1520]

[Figure 1521]

[Figure 1522]

[Figure 1523]

[Figure 1524]

[Figure 1525]

[Figure 1526]

[Figure 1527]

[Figure 1528]

[Figure 1529]

[Figure 1530]

[Figure 1531]

[Figure 1532]

[Figure 1533]

[Figure 1534]

[Figure 1535]

[Figure 1536]

[Figure 1537]

[Figure 1538]

[Figure 1539]

[Figure 1540]

[Figure 1541]

[Figure 1542]

[Figure 1543]

[Figure 1544]

[Figure 1545]

[Figure 1546]

[Figure 1547]

[Figure 1548]

[Figure 1549]

[Figure 1550]

[Figure 1551]

[Figure 1552]

[Figure 1553]

[Figure 1554]

[Figure 1555]

[Figure 1556]

[Figure 1557]

[Figure 1558]

[Figure 1559]

[Figure 1560]

[Figure 1561]

[Figure 1562]

[Figure 1563]

[Figure 1564]

[Figure 1565]

[Figure 1566]

[Figure 1567]

[Figure 1568]

[Figure 1569]

[Figure 1570]

[Figure 1571]

[Figure 1572]

[Figure 1573]

[Figure 1574]

[Figure 1575]

[Figure 1576]

[Figure 1577]

[Figure 1578]

[Figure 1579]

[Figure 1580]

[Figure 1581]

[Figure 1582]

[Figure 1583]

[Figure 1584]

[Figure 1585]

[Figure 1586]

[Figure 1587]

[Figure 1588]

[Figure 1589]

[Figure 1590]

[Figure 1591]

[Figure 1592]

[Figure 1593]

[Figure 1594]

[Figure 1595]

[Figure 1596]

[Figure 1597]

[Figure 1598]

[Figure 1599]

[Figure 1600]

[Figure 1601]

[Figure 1602]

[Figure 1603]

[Figure 1604]

[Figure 1605]

[Figure 1606]

[Figure 1607]

[Figure 1608]

[Figure 1609]

[Figure 1610]

[Figure 1611]

[Figure 1612]

[Figure 1613]

[Figure 1614]

[Figure 1615]

[Figure 1616]

[Figure 1617]

[Figure 1618]

[Figure 1619]

[Figure 1620]

[Figure 1621]

[Figure 1622]

[Figure 1623]

[Figure 1624]

[Figure 1625]

[Figure 1626]

[Figure 1627]

[Figure 1628]

[Figure 1629]

[Figure 1630]

[Figure 1631]

[Figure 1632]

[Figure 1633]

[Figure 1634]

[Figure 1635]

[Figure 1636]

[Figure 1637]

[Figure 1638]

[Figure 1639]

[Figure 1640]

[Figure 1641]

[Figure 1642]

[Figure 1643]

[Figure 1644]

[Figure 1645]

[Figure 1646]

[Figure 1647]

[Figure 1648]

[Figure 1649]

[Figure 1650]

[Figure 1651]

[Figure 1652]

[Figure 1653]

[Figure 1654]

[Figure 1655]

[Figure 1656]

[Figure 1657]

[Figure 1658]

[Figure 1659]

[Figure 1660]

[Figure 1661]

[Figure 1662]

[Figure 1663]

[Figure 1664]

[Figure 1665]

[Figure 1666]

[Figure 1667]

[Figure 1668]

[Figure 1669]

[Figure 1670]

[Figure 1671]

[Figure 1672]

[Figure 1673]

[Figure 1674]

[Figure 1675]

[Figure 1676]

[Figure 1677]

[Figure 1678]

[Figure 1679]

[Figure 1680]

[Figure 1681]

[Figure 1682]

[Figure 1683]

[Figure 1684]

[Figure 1685]

[Figure 1686]

[Figure 1687]

[Figure 1688]

[Figure 1689]

[Figure 1690]

[Figure 1691]

[Figure 1692]

[Figure 1693]

[Figure 1694]

[Figure 1695]

[Figure 1696]

[Figure 1697]

[Figure 1698]

[Figure 1699]

NIG Linear Quad Cubic Vol -0.130 -0.283 -0.228 0.371 SE (0.557) (0.561) (0.570) (0.528)

[Figure 1700]

[Figure 1701]

[Figure 1702]

[Figure 1703]

[Figure 1704]

Skew -0.555 -0.544 -0.543 -0.619

SE (0.278) (0.265) (0.277) (0.321) Kurt 0.411 0.477 0.473 0.160

SE (0.304) (0.302) (0.315) (0.290)

[Figure 1705]

[Figure 1706]

[Figure 1707]

[Figure 1708]

[Figure 1709]

Table 5: Imputed Physical Moments

The table presents moments of imputed physical distributions of eight industry portfolios. Distributions are imputed by letting the physical distribution, fP(x,s,τ) be related to the risk neutral distribution, fQ(x,s,τ) by

fQ(x,s,τ) m(x,s,τ)

fP(x,s,τ) = e−rfτ

[Figure 1710]

where m(x,s,τ) is the stochastic discount factor implied by the S&P 500 index. The risk neutral distribution is the equally-weighted risk neutral distribution across ﬁrms implied by risk neutral moments retrieved from option prices and the NIG probability density. We calculate the moments for four subperiods: 1996 Q2 - 1998 Q2, 1998 Q3 - 2000 Q1, 2000 Q2 - 2002 Q4, and 2003 Q1 - 2005 Q4.

Panel A: Mean Subperiod NonDur Dur Mfg Energy Tech Telecom Wh/Ret Health

[Figure 1711]

[Figure 1712]

[Figure 1713]

- I 0.0739 0.0753 0.0786 0.0770 0.0917 0.0859 0.0845 0.0882
- II 0.0702 0.0720 0.0792 0.0859 0.0982 0.0940 0.0818 0.0893
- III 0.0825 0.0860 0.0882 0.0886 0.1093 0.0947 0.0897 0.0988
- IV 0.0834 0.0747 0.0884 0.0918 0.1004 0.0858 0.0863 0.0982

[Figure 1714]

- Panel B: Volatility Subperiod NonDur Dur Mfg Energy Tech Telecom Wh/Ret Health

[Figure 1715]

[Figure 1716]

[Figure 1717]

- I 0.2724 0.2787 0.2856 0.2852 0.3422 0.3119 0.3222 0.3348
- II 0.2730 0.2742 0.2801 0.2959 0.3294 0.3109 0.3079 0.3221
- III 0.2811 0.2925 0.2936 0.2925 0.3625 0.3282 0.3063 0.3345
- IV 0.2684 0.2601 0.2799 0.2729 0.3266 0.3019 0.2905 0.3205

[Figure 1718]

- Panel C: Skewness Subperiod NonDur Dur Mfg Energy Tech Telecom Wh/Ret Health

[Figure 1719]

[Figure 1720]

[Figure 1721]

- I 0.4785 0.4918 0.4696 0.4861 0.3589 0.4339 0.3871 0.3544
- II 0.6171 0.5555 0.4997 0.3823 0.3612 0.3905 0.4705 0.4238
- III 0.4007 0.4507 0.4061 0.3690 0.2869 0.4062 0.3901 0.3613
- IV 0.4328 0.5507 0.2784 0.2019 0.2135 0.3667 0.2824 0.2511

[Figure 1722]

- Panel D: Kurtosis NonDur Dur Mfg Energy Tech Telecom Wh/Ret Health

[Figure 1723]

[Figure 1724]

[Figure 1725]

- I 6.0171 5.6818 5.3311 5.2650 2.9991 4.3173 3.6724 3.1631
- II 6.8163 6.3679 6.0763 4.9900 3.6533 4.4124 4.6471 4.0329
- III 5.6132 5.3446 5.1082 5.0510 2.5129 3.7166 4.4912 3.4917
- IV 6.7235 7.3218 5.1764 5.7343 3.2445 4.7178 4.7419 3.5187

[Figure 1726]

Sharpe Ratio NonDur Dur Mfg Energy Tech Telecom Wh/Ret Health

[Figure 1727]

[Figure 1728]

[Figure 1729]

- I 0.0770 0.0807 0.0899 0.0859 0.1136 0.1065 0.0975 0.1056
- II 0.0707 0.0784 0.1008 0.1186 0.1444 0.1400 0.1010 0.1193
- III 0.1721 0.1777 0.1850 0.1848 0.2054 0.1830 0.1811 0.1926
- IV 0.2353 0.2059 0.2392 0.2605 0.2414 0.2109 0.2227 0.2388

[Figure 1730]

Table 6: Imputed Risk Aversion

The table presents subperiod estimates of imputed risk aversion. Risk aversion is calculated using estimates of the physical and risk neutral estimates of the probability density function following Leland (1980) and Jackwerth

(2000):

RA(s) = P′(s)/P(s) − Q′(s)/Q(s)

where P is the physical probability measure and Q is the risk neutral measure. We choose the state, s to correspond to an 8% market risk premium. Both probability measures are calculated using the NIG approximation in Eriksson, Forsberg, and Ghysels (2004), which takes as its arguments the mean, variance, skewness, and kurtosis of the density. Risk neutral moments are retrieved from option prices on the S&P 500 closest to 12 months to maturity. Physical moments are calculated in one of four ways. “Fixed” indicates that the moments are sample moments computed over daily returns on the S&P 500 index over the period 1/92 - 12/95. “Roll” indicates that the moments are computed over a rolling lagged four year sample period. “Roll AR(1)” moments are computed by estimating an AR(1) on the S&P 500 four year sample moments over the period 1950-1995 and forecasting next period’s moment on the basis of the current four year sample moment. “Unconditional” uses the unconditional moments estimated over the 1950-1995 time period. We average moments over four subperiods: I. 1996 Q2 - 1998 Q2, II. 1998 Q3 - 2000 Q1, III. 2000 Q2 - 2002 Q4, and IV. 2003 Q1 - 2005 Q4.

[Figure 1731]

[Figure 1732]

Subperiod Fixed Roll Roll AR(1) Uncond.

[Figure 1733]

- I 16.27 15.65 15.42 17.43
- II 7.99 6.32 6.55 9.14
- III 9.84 6.44 6.91 10.99
- IV 18.73 14.91 15.04 19.88

[Figure 1734]

Figure 1: Stochastic Discount Factors

The plots depict stochastic discount factors formed using risk neutral moments of S&P 500 index options at the 12-month maturity. The plot labeled ‘NIG’ represents stochastic discount factors, m(x,s,tau), formed as

fQ (x,s,τ) fP (x,s,τ)

m(x,s,τ) = e−rfτ

[Figure 1735]

where f(·) is the NIG probability density function, Q denotes the risk-neutral probability measure, and P denotes the physical measure. The risk neutral measure is calculated using risk neutral moments retrieved from option prices and the physical measure using the historical moments of the S&P 500 index from 1992 through 1995. ’Linear,’ ’Quadratic,’ and ’Cubic’ represent linear, quadratic, and cubic polynomial ﬁts to the NIG kernel. Subﬁgure A depicts plots of the average stochastic discount factor for all four kernels; Subﬁgure B depicts the polynomial kernels over a smaller range.

Figure A

2.2

|Linear<br><br>Quadratic<br><br>Cubic<br><br>NIG<br><br>|
|---|

- 1.8

- 2

1.6

1.4

1.2

- 0.8

- 1

0.6

0.4

0.2

0 0.5 1 1.5 2

..

Figure B

- 0.8 0.85 0.9 0.95 1 1.05 1.1 1.15 1.2

- 1.1

- 1.2

- 1.3

- 1.4

- 1.5

- 1.6

- 1.7

- 1.8

- 1.9

|Linear<br><br>Quadratic<br><br>Cubic<br><br>|
|---|

..

Figure 2: Imputed and Historical Probability Densities

The plots depict the probability densities for eight industry portfolios implied by historical and imputed moments. Historical moments are calculated from equally-weighted daily returns on each industry portfolio over the past four years, updated quarterly. Imputed moments are obtained by imputing the physical probability density for the industry portfolio using its risk neutral probability measure and the stochastic discount factor obtained from the S&P 500 index. Averages of moments over the relevant time periods are then used to calculate the NIG density function, evaluated at these moments. For each industry, we examine densities over four subperiods: 1996 Q2 1998 Q2, 1998 Q3 - 2000 Q1, 2000 Q2 - 2002 Q4, and 2003 Q1 - 2005 Q4.

Nondurables

|Historical<br><br>Imputed<br><br>|
|---|

|Historical<br><br>Imputed<br><br>|
|---|

- 0

- 0.5

- 1

1.5

2

- 2.5

- 3

3.5

4

- 4.5

- 5

- 0

- 0.5

- 1

1.5

2

- 2.5

- 3

3.5

4

- 4.5

- 5

0 0.5 1 1.5 2 2.5 3

0 0.5 1 1.5 2 2.5 3

(a) 1996 Q2 - 1998 Q2

(b) 1998 Q3 - 2000 Q1

|Historical<br><br>Imputed<br><br>|
|---|

|Historical<br><br>Imputed<br><br>|
|---|

- 0

- 0.5

- 1

1.5

2

- 2.5

- 3

3.5

4

- 4.5

- 5

- 0

- 0.5

- 1

1.5

2

- 2.5

- 3

3.5

4

- 4.5

- 5

0 0.5 1 1.5 2 2.5 3

0 0.5 1 1.5 2 2.5 3

(c) 2000 Q2 - 2002 Q3

(d) 2003 Q1 - 2005 Q4

Figure continued on next page...

Durables

|Historical<br><br>Imputed<br><br>|
|---|

|Historical<br><br>Imputed<br><br>|
|---|

- 0

- 0.5

- 1

1.5

2

- 2.5

- 3

3.5

4

- 4.5

- 5

- 0

- 0.5

- 1

1.5

2

- 2.5

- 3

3.5

4

- 4.5

- 5

0 0.5 1 1.5 2 2.5 3

0 0.5 1 1.5 2 2.5 3

(a) 1996 Q2 - 1998 Q2

(b) 1998 Q3 - 2000 Q1

|Historical<br><br>Imputed<br><br>|
|---|

|Historical<br><br>Imputed<br><br>|
|---|

- 0

- 0.5

- 1

1.5

2

- 2.5

- 3

3.5

4

- 4.5

- 5

- 0

- 0.5

- 1

1.5

2

- 2.5

- 3

3.5

4

- 4.5

- 5

0 0.5 1 1.5 2 2.5 3

0 0.5 1 1.5 2 2.5 3

(c) 2000 Q2 - 2002 Q3

(d) 2003 Q1 - 2005 Q4

Figure continued on next page...

Manufacturing

5

5

|Historical<br><br>Imputed<br><br>|
|---|

|Historical<br><br>Imputed<br><br>|
|---|

4.5

4.5

4

4

3.5

3.5

3

3

2.5

2.5

2

2

1.5

1.5

1

1

0.5

0.5

0

0

0 0.5 1 1.5 2 2.5 3

0 0.5 1 1.5 2 2.5 3

(a) 1996 Q2 - 1998 Q2

(b) 1998 Q3 - 2000 Q1

5

5

|Historical<br><br>Imputed<br><br>|
|---|

|Historical<br><br>Imputed<br><br>|
|---|

4.5

4.5

4

4

3.5

3.5

3

3

2.5

2.5

2

2

1.5

1.5

1

1

0.5

0.5

0

0

0 0.5 1 1.5 2 2.5 3

0 0.5 1 1.5 2 2.5 3

(c) 2000 Q2 - 2002 Q3

(d) 2003 Q1 - 2005 Q4

Figure continued on next page...

Energy

5

5

|Historical<br><br>Imputed<br><br>|
|---|

|Historical<br><br>Imputed<br><br>|
|---|

4.5

4.5

4

4

3.5

3.5

3

3

2.5

2.5

2

2

1.5

1.5

1

1

0.5

0.5

0

0

0 0.5 1 1.5 2 2.5 3

0 0.5 1 1.5 2 2.5 3

(a) 1996 Q2 - 1998 Q2

(b) 1998 Q3 - 2000 Q1

5

5

|Historical<br><br>Imputed<br><br>|
|---|

|Historical<br><br>Imputed<br><br>|
|---|

4.5

4.5

4

4

3.5

3.5

3

3

2.5

2.5

2

2

1.5

1.5

1

1

0.5

0.5

0

0

0 0.5 1 1.5 2 2.5 3

0 0.5 1 1.5 2 2.5 3

(c) 2000 Q2 - 2002 Q3

(d) 2003 Q1 - 2005 Q4

Figure continued on next page...

Tech

5

5

|Historical<br><br>Imputed<br><br>|
|---|

|Historical<br><br>Imputed<br><br>|
|---|

4.5

4.5

4

4

3.5

3.5

3

3

2.5

2.5

2

2

1.5

1.5

1

1

0.5

0.5

0

0

0 0.5 1 1.5 2 2.5 3

0 0.5 1 1.5 2 2.5 3

(a) 1996 Q2 - 1998 Q2

(b) 1998 Q3 - 2000 Q1

5

5

|Historical<br><br>Imputed<br><br>|
|---|

|Historical<br><br>Imputed<br><br>|
|---|

4.5

4.5

4

4

3.5

3.5

3

3

2.5

2.5

2

2

1.5

1.5

1

1

0.5

0.5

0

0

0 0.5 1 1.5 2 2.5 3

0 0.5 1 1.5 2 2.5 3

(c) 2000 Q2 - 2002 Q3

(d) 2003 Q1 - 2005 Q4

Figure continued on next page...

Telecom

5

5

|Historical<br><br>Imputed<br><br>|
|---|

|Historical<br><br>Imputed<br><br>|
|---|

4.5

4.5

4

4

3.5

3.5

3

3

2.5

2.5

2

2

1.5

1.5

1

1

0.5

0.5

0

0

0 0.5 1 1.5 2 2.5 3

0 0.5 1 1.5 2 2.5 3

(a) 1996 Q2 - 1998 Q2

(b) 1998 Q3 - 2000 Q1

5

5

|Historical<br><br>Imputed<br><br>|
|---|

|Historical<br><br>Imputed<br><br>|
|---|

4.5

4.5

4

4

3.5

3.5

3

3

2.5

2.5

2

2

1.5

1.5

1

1

0.5

0.5

0

0

0 0.5 1 1.5 2 2.5 3

0 0.5 1 1.5 2 2.5 3

(c) 2000 Q2 - 2002 Q3

(d) 2003 Q1 - 2005 Q4

Figure continued on next page...

Wholesale/Retail

5

5

|Historical<br><br>Imputed<br><br>|
|---|

|Historical<br><br>Imputed<br><br>|
|---|

4.5

4.5

4

4

3.5

3.5

3

3

2.5

2.5

2

2

1.5

1.5

1

1

0.5

0.5

0

0

0 0.5 1 1.5 2 2.5 3

0 0.5 1 1.5 2 2.5 3

(a) 1996 Q2 - 1998 Q2

(b) 1998 Q3 - 2000 Q1

5

5

|Historical<br><br>Imputed<br><br>|
|---|

|Historical<br><br>Imputed<br><br>|
|---|

4.5

4.5

4

4

3.5

3.5

3

3

2.5

2.5

2

2

1.5

1.5

1

1

0.5

0.5

0

0

0 0.5 1 1.5 2 2.5 3

0 0.5 1 1.5 2 2.5 3

(c) 2000 Q2 - 2002 Q3

(d) 2003 Q1 - 2005 Q4

Figure continued on next page...

Healthcare

5

5

|Historical<br><br>Imputed<br><br>|
|---|

|Historical<br><br>Imputed<br><br>|
|---|

4.5

4.5

4

4

3.5

3.5

3

3

2.5

2.5

2

2

1.5

1.5

1

1

0.5

0.5

0

0

0 0.5 1 1.5 2 2.5 3

0 0.5 1 1.5 2 2.5 3

(a) 1996 Q2 - 1998 Q2

(b) 1998 Q3 - 2000 Q1

5

5

|Historical<br><br>Imputed<br><br>|
|---|

|Historical<br><br>Imputed<br><br>|
|---|

4.5

4.5

4

4

3.5

3.5

3

3

2.5

2.5

2

2

1.5

1.5

1

1

0.5

0.5

0

0

0 0.5 1 1.5 2 2.5 3

0 0.5 1 1.5 2 2.5 3

(c) 2000 Q2 - 2002 Q3

(d) 2003 Q1 - 2005 Q4

Figure 3: Risk Aversion

The plots depict the probability densities for eight industry portfolios implied by historical and imputed moments. Historical moments are calculated from equally-weighted daily returns on each industry portfolio over the past four years, updated quarterly. Imputed moments are obtained by imputing the physical probability density for the industry portfolio using its risk neutral probability measure and the stochastic discount factor obtained from the S&P 500 index. Averages of moments over the relevant time periods are then used to calculate the NIG density function, evaluated at these moments. For each industry, we examine densities over four subperiods: 1996 Q2 1998 Q2, 1998 Q3 - 2000 Q1, 2000 Q2 - 2002 Q4, and 2003 Q1 - 2005 Q4.

30

25

20

15

10

5

0

Jan96 Jan98 Jan00 Jan02 Jan04 Jan06

..

(a) Unconditional Moments

30

25

20

15

10

5

0

Jan96 Jan98 Jan00 Jan02 Jan04 Jan06

..

(b) Fixed Physical Moments

30

25

20

15

10

5

0

Jan96 Jan98 Jan00 Jan02 Jan04 Jan06

..

(c) Rolling Physical Moments

30

25

20

15

10

5

0

Jan96 Jan98 Jan00 Jan02 Jan04 Jan06

..

(d) AR(1) Physical Moments

## Appendix

- 48

Table A1: Summary Statistics with Volume Screens

Panels A-C present summary statistics for portfolios sorted on measures of ﬁrms’ risk-neutral moments. Firms are sorted on average risk-neutral volatility, skewness, and kurtosis within each calendar quarter into terciles based on 30th and 70th percentiles. We then form equally-weighted portfolios of these ﬁrms, holding the moment ranking constant for the subsequent calendar quarter. Risk-neutral moments are calculated using the procedure in Bakshi, Kapadia, and Madan (2003); the options used are those closest to one, three, six, and twelve months to maturity. We eliminate ﬁrms that do not have trading volume in at least one OTM put and OTM call in a calendar month. The ﬁrst column of each panel presents mean monthly returns. The second column presents characteristic-adjusted returns, calculated by determining, for each ﬁrm, the Fama-French 5X5 sizeand book-to-market portfolio to which it belongs and subtracting that return. Monthly return data cover the period 4/96 through 12/05, for a total of 117 monthly observations.

Panel A: Volatility-Ranked Portfolios 1 Month Maturity 3 Month Maturity 6 Month Maturity 12 Month Maturity Rank Mean Char Adj Rank Mean Char Adj Rank Mean Char Adj Rank Mean Char Adj

[Figure 1736]

[Figure 1737]

[Figure 1738]

[Figure 1739]

[Figure 1740]

[Figure 1741]

[Figure 1742]

[Figure 1743]

[Figure 1744]

[Figure 1745]

[Figure 1746]

[Figure 1747]

[Figure 1748]

[Figure 1749]

[Figure 1750]

[Figure 1751]

[Figure 1752]

[Figure 1753]

[Figure 1754]

[Figure 1755]

[Figure 1756]

[Figure 1757]

[Figure 1758]

[Figure 1759]

[Figure 1760]

[Figure 1761]

[Figure 1762]

[Figure 1763]

[Figure 1764]

[Figure 1765]

[Figure 1766]

[Figure 1767]

[Figure 1768]

[Figure 1769]

[Figure 1770]

[Figure 1771]

[Figure 1772]

[Figure 1773]

[Figure 1774]

[Figure 1775]

[Figure 1776]

[Figure 1777]

[Figure 1778]

[Figure 1779]

[Figure 1780]

[Figure 1781]

[Figure 1782]

[Figure 1783]

[Figure 1784]

[Figure 1785]

[Figure 1786]

[Figure 1787]

[Figure 1788]

[Figure 1789]

[Figure 1790]

[Figure 1791]

[Figure 1792]

[Figure 1793]

[Figure 1794]

[Figure 1795]

[Figure 1796]

[Figure 1797]

[Figure 1798]

[Figure 1799]

[Figure 1800]

[Figure 1801]

[Figure 1802]

[Figure 1803]

[Figure 1804]

[Figure 1805]

[Figure 1806]

[Figure 1807]

[Figure 1808]

[Figure 1809]

[Figure 1810]

[Figure 1811]

[Figure 1812]

[Figure 1813]

[Figure 1814]

[Figure 1815]

[Figure 1816]

[Figure 1817]

[Figure 1818]

[Figure 1819]

[Figure 1820]

[Figure 1821]

[Figure 1822]

[Figure 1823]

[Figure 1824]

[Figure 1825]

[Figure 1826]

[Figure 1827]

[Figure 1828]

[Figure 1829]

[Figure 1830]

[Figure 1831]

[Figure 1832]

[Figure 1833]

[Figure 1834]

[Figure 1835]

[Figure 1836]

[Figure 1837]

[Figure 1838]

[Figure 1839]

[Figure 1840]

[Figure 1841]

[Figure 1842]

[Figure 1843]

[Figure 1844]

[Figure 1845]

[Figure 1846]

[Figure 1847]

[Figure 1848]

[Figure 1849]

[Figure 1850]

[Figure 1851]

[Figure 1852]

[Figure 1853]

[Figure 1854]

[Figure 1855]

[Figure 1856]

[Figure 1857]

[Figure 1858]

[Figure 1859]

[Figure 1860]

[Figure 1861]

[Figure 1862]

[Figure 1863]

[Figure 1864]

[Figure 1865]

[Figure 1866]

[Figure 1867]

[Figure 1868]

[Figure 1869]

[Figure 1870]

[Figure 1871]

[Figure 1872]

[Figure 1873]

[Figure 1874]

[Figure 1875]

[Figure 1876]

[Figure 1877]

[Figure 1878]

[Figure 1879]

[Figure 1880]

[Figure 1881]

[Figure 1882]

[Figure 1883]

[Figure 1884]

[Figure 1885]

[Figure 1886]

[Figure 1887]

[Figure 1888]

[Figure 1889]

[Figure 1890]

[Figure 1891]

[Figure 1892]

[Figure 1893]

[Figure 1894]

[Figure 1895]

[Figure 1896]

[Figure 1897]

[Figure 1898]

[Figure 1899]

[Figure 1900]

[Figure 1901]

[Figure 1902]

[Figure 1903]

[Figure 1904]

[Figure 1905]

[Figure 1906]

[Figure 1907]

[Figure 1908]

[Figure 1909]

[Figure 1910]

[Figure 1911]

[Figure 1912]

[Figure 1913]

[Figure 1914]

[Figure 1915]

[Figure 1916]

[Figure 1917]

[Figure 1918]

[Figure 1919]

[Figure 1920]

[Figure 1921]

[Figure 1922]

[Figure 1923]

[Figure 1924]

[Figure 1925]

[Figure 1926]

[Figure 1927]

[Figure 1928]

[Figure 1929]

[Figure 1930]

[Figure 1931]

[Figure 1932]

[Figure 1933]

[Figure 1934]

[Figure 1935]

[Figure 1936]

[Figure 1937]

[Figure 1938]

[Figure 1939]

[Figure 1940]

[Figure 1941]

[Figure 1942]

[Figure 1943]

[Figure 1944]

[Figure 1945]

[Figure 1946]

[Figure 1947]

[Figure 1948]

[Figure 1949]

[Figure 1950]

[Figure 1951]

[Figure 1952]

[Figure 1953]

[Figure 1954]

[Figure 1955]

[Figure 1956]

[Figure 1957]

[Figure 1958]

[Figure 1959]

[Figure 1960]

[Figure 1961]

[Figure 1962]

[Figure 1963]

[Figure 1964]

[Figure 1965]

[Figure 1966]

[Figure 1967]

[Figure 1968]

[Figure 1969]

[Figure 1970]

[Figure 1971]

[Figure 1972]

[Figure 1973]

[Figure 1974]

[Figure 1975]

[Figure 1976]

[Figure 1977]

[Figure 1978]

[Figure 1979]

[Figure 1980]

[Figure 1981]

[Figure 1982]

[Figure 1983]

[Figure 1984]

[Figure 1985]

[Figure 1986]

[Figure 1987]

[Figure 1988]

[Figure 1989]

[Figure 1990]

[Figure 1991]

[Figure 1992]

[Figure 1993]

[Figure 1994]

[Figure 1995]

[Figure 1996]

[Figure 1997]

[Figure 1998]

[Figure 1999]

[Figure 2000]

[Figure 2001]

[Figure 2002]

[Figure 2003]

[Figure 2004]

[Figure 2005]

[Figure 2006]

[Figure 2007]

[Figure 2008]

[Figure 2009]

[Figure 2010]

[Figure 2011]

[Figure 2012]

[Figure 2013]

[Figure 2014]

[Figure 2015]

[Figure 2016]

[Figure 2017]

[Figure 2018]

[Figure 2019]

[Figure 2020]

[Figure 2021]

[Figure 2022]

[Figure 2023]

[Figure 2024]

[Figure 2025]

[Figure 2026]

[Figure 2027]

[Figure 2028]

[Figure 2029]

[Figure 2030]

[Figure 2031]

[Figure 2032]

[Figure 2033]

[Figure 2034]

[Figure 2035]

[Figure 2036]

[Figure 2037]

[Figure 2038]

[Figure 2039]

[Figure 2040]

[Figure 2041]

[Figure 2042]

[Figure 2043]

[Figure 2044]

[Figure 2045]

[Figure 2046]

[Figure 2047]

[Figure 2048]

[Figure 2049]

[Figure 2050]

[Figure 2051]

[Figure 2052]

[Figure 2053]

[Figure 2054]

[Figure 2055]

[Figure 2056]

[Figure 2057]

[Figure 2058]

[Figure 2059]

[Figure 2060]

[Figure 2061]

[Figure 2062]

[Figure 2063]

[Figure 2064]

[Figure 2065]

[Figure 2066]

[Figure 2067]

[Figure 2068]

[Figure 2069]

[Figure 2070]

[Figure 2071]

[Figure 2072]

[Figure 2073]

[Figure 2074]

[Figure 2075]

[Figure 2076]

[Figure 2077]

[Figure 2078]

[Figure 2079]

[Figure 2080]

[Figure 2081]

[Figure 2082]

[Figure 2083]

[Figure 2084]

[Figure 2085]

[Figure 2086]

[Figure 2087]

[Figure 2088]

[Figure 2089]

[Figure 2090]

[Figure 2091]

[Figure 2092]

[Figure 2093]

[Figure 2094]

[Figure 2095]

[Figure 2096]

[Figure 2097]

[Figure 2098]

[Figure 2099]

[Figure 2100]

[Figure 2101]

[Figure 2102]

[Figure 2103]

[Figure 2104]

[Figure 2105]

[Figure 2106]

[Figure 2107]

[Figure 2108]

[Figure 2109]

[Figure 2110]

[Figure 2111]

[Figure 2112]

[Figure 2113]

[Figure 2114]

[Figure 2115]

[Figure 2116]

[Figure 2117]

[Figure 2118]

[Figure 2119]

[Figure 2120]

[Figure 2121]

[Figure 2122]

[Figure 2123]

[Figure 2124]

[Figure 2125]

[Figure 2126]

[Figure 2127]

[Figure 2128]

[Figure 2129]

[Figure 2130]

[Figure 2131]

[Figure 2132]

[Figure 2133]

[Figure 2134]

[Figure 2135]

[Figure 2136]

[Figure 2137]

[Figure 2138]

[Figure 2139]

[Figure 2140]

[Figure 2141]

[Figure 2142]

[Figure 2143]

[Figure 2144]

[Figure 2145]

[Figure 2146]

[Figure 2147]

[Figure 2148]

[Figure 2149]

[Figure 2150]

[Figure 2151]

[Figure 2152]

[Figure 2153]

[Figure 2154]

[Figure 2155]

[Figure 2156]

[Figure 2157]

[Figure 2158]

[Figure 2159]

[Figure 2160]

[Figure 2161]

[Figure 2162]

[Figure 2163]

[Figure 2164]

[Figure 2165]

[Figure 2166]

[Figure 2167]

[Figure 2168]

[Figure 2169]

[Figure 2170]

[Figure 2171]

[Figure 2172]

[Figure 2173]

[Figure 2174]

[Figure 2175]

[Figure 2176]

[Figure 2177]

[Figure 2178]

[Figure 2179]

[Figure 2180]

[Figure 2181]

[Figure 2182]

[Figure 2183]

[Figure 2184]

[Figure 2185]

[Figure 2186]

[Figure 2187]

[Figure 2188]

[Figure 2189]

[Figure 2190]

[Figure 2191]

[Figure 2192]

[Figure 2193]

[Figure 2194]

[Figure 2195]

[Figure 2196]

[Figure 2197]

[Figure 2198]

[Figure 2199]

[Figure 2200]

[Figure 2201]

[Figure 2202]

[Figure 2203]

[Figure 2204]

[Figure 2205]

[Figure 2206]

[Figure 2207]

[Figure 2208]

[Figure 2209]

[Figure 2210]

[Figure 2211]

[Figure 2212]

[Figure 2213]

[Figure 2214]

[Figure 2215]

[Figure 2216]

[Figure 2217]

[Figure 2218]

[Figure 2219]

[Figure 2220]

[Figure 2221]

[Figure 2222]

[Figure 2223]

[Figure 2224]

[Figure 2225]

[Figure 2226]

[Figure 2227]

[Figure 2228]

[Figure 2229]

[Figure 2230]

[Figure 2231]

[Figure 2232]

[Figure 2233]

[Figure 2234]

[Figure 2235]

[Figure 2236]

[Figure 2237]

[Figure 2238]

[Figure 2239]

[Figure 2240]

[Figure 2241]

[Figure 2242]

[Figure 2243]

[Figure 2244]

[Figure 2245]

[Figure 2246]

[Figure 2247]

[Figure 2248]

[Figure 2249]

[Figure 2250]

[Figure 2251]

[Figure 2252]

[Figure 2253]

[Figure 2254]

[Figure 2255]

[Figure 2256]

[Figure 2257]

[Figure 2258]

[Figure 2259]

[Figure 2260]

[Figure 2261]

[Figure 2262]

[Figure 2263]

[Figure 2264]

[Figure 2265]

[Figure 2266]

[Figure 2267]

- 1 1.331 0.395 1 1.289 0.375 1 1.297 0.405 1 1.339 0.432
- 2 0.861 0.012 2 1.007 0.107 2 1.026 0.134 2 0.995 0.088
- 3 0.972 0.226 3 0.819 0.101 3 0.782 0.049 3 0.781 0.090

3-1 -0.360 -0.169 3-1 -0.470 -0.274 3-1 -0.515 -0.355 3-1 -0.558 -0.342

[Figure 2268]

[Figure 2269]

[Figure 2270]

[Figure 2271]

[Figure 2272]

[Figure 2273]

[Figure 2274]

[Figure 2275]

[Figure 2276]

[Figure 2277]

[Figure 2278]

[Figure 2279]

Panel B: Skewness-Ranked Portfolios 1 Month Maturity 3 Month Maturity 6 Month Maturity 12 Month Maturity Rank Mean Char Adj Rank Mean Char Adj Rank Mean Char Adj Rank Mean Char Adj

[Figure 2280]

[Figure 2281]

[Figure 2282]

[Figure 2283]

[Figure 2284]

[Figure 2285]

[Figure 2286]

[Figure 2287]

[Figure 2288]

[Figure 2289]

[Figure 2290]

[Figure 2291]

[Figure 2292]

[Figure 2293]

[Figure 2294]

[Figure 2295]

[Figure 2296]

[Figure 2297]

[Figure 2298]

[Figure 2299]

[Figure 2300]

[Figure 2301]

[Figure 2302]

[Figure 2303]

[Figure 2304]

[Figure 2305]

[Figure 2306]

[Figure 2307]

[Figure 2308]

[Figure 2309]

[Figure 2310]

[Figure 2311]

[Figure 2312]

[Figure 2313]

[Figure 2314]

[Figure 2315]

[Figure 2316]

[Figure 2317]

[Figure 2318]

[Figure 2319]

[Figure 2320]

[Figure 2321]

[Figure 2322]

[Figure 2323]

[Figure 2324]

[Figure 2325]

[Figure 2326]

[Figure 2327]

[Figure 2328]

[Figure 2329]

[Figure 2330]

[Figure 2331]

[Figure 2332]

[Figure 2333]

[Figure 2334]

[Figure 2335]

[Figure 2336]

[Figure 2337]

[Figure 2338]

[Figure 2339]

[Figure 2340]

[Figure 2341]

[Figure 2342]

[Figure 2343]

[Figure 2344]

[Figure 2345]

[Figure 2346]

[Figure 2347]

[Figure 2348]

[Figure 2349]

[Figure 2350]

[Figure 2351]

[Figure 2352]

[Figure 2353]

[Figure 2354]

[Figure 2355]

[Figure 2356]

[Figure 2357]

[Figure 2358]

[Figure 2359]

[Figure 2360]

[Figure 2361]

[Figure 2362]

[Figure 2363]

[Figure 2364]

[Figure 2365]

[Figure 2366]

[Figure 2367]

[Figure 2368]

[Figure 2369]

[Figure 2370]

[Figure 2371]

[Figure 2372]

[Figure 2373]

[Figure 2374]

[Figure 2375]

[Figure 2376]

[Figure 2377]

[Figure 2378]

[Figure 2379]

[Figure 2380]

[Figure 2381]

[Figure 2382]

[Figure 2383]

[Figure 2384]

[Figure 2385]

[Figure 2386]

[Figure 2387]

[Figure 2388]

[Figure 2389]

[Figure 2390]

[Figure 2391]

[Figure 2392]

[Figure 2393]

[Figure 2394]

[Figure 2395]

[Figure 2396]

[Figure 2397]

[Figure 2398]

[Figure 2399]

[Figure 2400]

[Figure 2401]

[Figure 2402]

[Figure 2403]

[Figure 2404]

[Figure 2405]

[Figure 2406]

[Figure 2407]

[Figure 2408]

[Figure 2409]

[Figure 2410]

[Figure 2411]

[Figure 2412]

[Figure 2413]

[Figure 2414]

[Figure 2415]

[Figure 2416]

[Figure 2417]

[Figure 2418]

[Figure 2419]

[Figure 2420]

[Figure 2421]

[Figure 2422]

[Figure 2423]

[Figure 2424]

[Figure 2425]

[Figure 2426]

[Figure 2427]

[Figure 2428]

[Figure 2429]

[Figure 2430]

[Figure 2431]

[Figure 2432]

[Figure 2433]

[Figure 2434]

[Figure 2435]

[Figure 2436]

[Figure 2437]

[Figure 2438]

[Figure 2439]

[Figure 2440]

[Figure 2441]

[Figure 2442]

[Figure 2443]

[Figure 2444]

[Figure 2445]

[Figure 2446]

[Figure 2447]

[Figure 2448]

[Figure 2449]

[Figure 2450]

[Figure 2451]

[Figure 2452]

[Figure 2453]

[Figure 2454]

[Figure 2455]

[Figure 2456]

[Figure 2457]

[Figure 2458]

[Figure 2459]

[Figure 2460]

[Figure 2461]

[Figure 2462]

[Figure 2463]

[Figure 2464]

[Figure 2465]

[Figure 2466]

[Figure 2467]

[Figure 2468]

[Figure 2469]

[Figure 2470]

[Figure 2471]

[Figure 2472]

[Figure 2473]

[Figure 2474]

[Figure 2475]

[Figure 2476]

[Figure 2477]

[Figure 2478]

[Figure 2479]

[Figure 2480]

[Figure 2481]

[Figure 2482]

[Figure 2483]

[Figure 2484]

[Figure 2485]

[Figure 2486]

[Figure 2487]

[Figure 2488]

[Figure 2489]

[Figure 2490]

[Figure 2491]

[Figure 2492]

[Figure 2493]

[Figure 2494]

[Figure 2495]

[Figure 2496]

[Figure 2497]

[Figure 2498]

[Figure 2499]

[Figure 2500]

[Figure 2501]

[Figure 2502]

[Figure 2503]

[Figure 2504]

[Figure 2505]

[Figure 2506]

[Figure 2507]

[Figure 2508]

[Figure 2509]

[Figure 2510]

[Figure 2511]

[Figure 2512]

[Figure 2513]

[Figure 2514]

[Figure 2515]

[Figure 2516]

[Figure 2517]

[Figure 2518]

[Figure 2519]

[Figure 2520]

[Figure 2521]

[Figure 2522]

[Figure 2523]

[Figure 2524]

[Figure 2525]

[Figure 2526]

[Figure 2527]

[Figure 2528]

[Figure 2529]

[Figure 2530]

[Figure 2531]

[Figure 2532]

[Figure 2533]

[Figure 2534]

[Figure 2535]

[Figure 2536]

[Figure 2537]

[Figure 2538]

[Figure 2539]

[Figure 2540]

[Figure 2541]

[Figure 2542]

[Figure 2543]

[Figure 2544]

[Figure 2545]

[Figure 2546]

[Figure 2547]

[Figure 2548]

[Figure 2549]

[Figure 2550]

[Figure 2551]

[Figure 2552]

[Figure 2553]

[Figure 2554]

[Figure 2555]

[Figure 2556]

[Figure 2557]

[Figure 2558]

[Figure 2559]

[Figure 2560]

[Figure 2561]

[Figure 2562]

[Figure 2563]

[Figure 2564]

[Figure 2565]

[Figure 2566]

[Figure 2567]

[Figure 2568]

[Figure 2569]

[Figure 2570]

[Figure 2571]

[Figure 2572]

[Figure 2573]

[Figure 2574]

[Figure 2575]

[Figure 2576]

[Figure 2577]

[Figure 2578]

[Figure 2579]

[Figure 2580]

[Figure 2581]

[Figure 2582]

[Figure 2583]

[Figure 2584]

[Figure 2585]

[Figure 2586]

[Figure 2587]

[Figure 2588]

[Figure 2589]

[Figure 2590]

[Figure 2591]

[Figure 2592]

[Figure 2593]

[Figure 2594]

[Figure 2595]

[Figure 2596]

[Figure 2597]

[Figure 2598]

[Figure 2599]

[Figure 2600]

[Figure 2601]

[Figure 2602]

[Figure 2603]

[Figure 2604]

[Figure 2605]

[Figure 2606]

[Figure 2607]

[Figure 2608]

[Figure 2609]

[Figure 2610]

[Figure 2611]

[Figure 2612]

[Figure 2613]

[Figure 2614]

[Figure 2615]

[Figure 2616]

[Figure 2617]

[Figure 2618]

[Figure 2619]

[Figure 2620]

[Figure 2621]

[Figure 2622]

[Figure 2623]

[Figure 2624]

[Figure 2625]

[Figure 2626]

[Figure 2627]

[Figure 2628]

[Figure 2629]

[Figure 2630]

[Figure 2631]

[Figure 2632]

[Figure 2633]

[Figure 2634]

[Figure 2635]

[Figure 2636]

[Figure 2637]

[Figure 2638]

[Figure 2639]

[Figure 2640]

[Figure 2641]

[Figure 2642]

[Figure 2643]

[Figure 2644]

[Figure 2645]

[Figure 2646]

[Figure 2647]

[Figure 2648]

[Figure 2649]

[Figure 2650]

[Figure 2651]

[Figure 2652]

[Figure 2653]

[Figure 2654]

[Figure 2655]

[Figure 2656]

[Figure 2657]

[Figure 2658]

[Figure 2659]

[Figure 2660]

[Figure 2661]

[Figure 2662]

[Figure 2663]

[Figure 2664]

[Figure 2665]

[Figure 2666]

[Figure 2667]

[Figure 2668]

[Figure 2669]

[Figure 2670]

[Figure 2671]

[Figure 2672]

[Figure 2673]

[Figure 2674]

[Figure 2675]

[Figure 2676]

[Figure 2677]

[Figure 2678]

[Figure 2679]

[Figure 2680]

[Figure 2681]

[Figure 2682]

[Figure 2683]

[Figure 2684]

[Figure 2685]

[Figure 2686]

[Figure 2687]

[Figure 2688]

[Figure 2689]

[Figure 2690]

[Figure 2691]

[Figure 2692]

[Figure 2693]

[Figure 2694]

[Figure 2695]

[Figure 2696]

[Figure 2697]

[Figure 2698]

[Figure 2699]

[Figure 2700]

[Figure 2701]

[Figure 2702]

[Figure 2703]

[Figure 2704]

[Figure 2705]

[Figure 2706]

[Figure 2707]

[Figure 2708]

[Figure 2709]

[Figure 2710]

[Figure 2711]

[Figure 2712]

[Figure 2713]

[Figure 2714]

[Figure 2715]

[Figure 2716]

[Figure 2717]

[Figure 2718]

[Figure 2719]

[Figure 2720]

[Figure 2721]

[Figure 2722]

[Figure 2723]

[Figure 2724]

[Figure 2725]

[Figure 2726]

[Figure 2727]

[Figure 2728]

[Figure 2729]

[Figure 2730]

[Figure 2731]

[Figure 2732]

[Figure 2733]

[Figure 2734]

[Figure 2735]

[Figure 2736]

[Figure 2737]

[Figure 2738]

[Figure 2739]

[Figure 2740]

[Figure 2741]

[Figure 2742]

[Figure 2743]

[Figure 2744]

[Figure 2745]

[Figure 2746]

[Figure 2747]

[Figure 2748]

[Figure 2749]

[Figure 2750]

[Figure 2751]

[Figure 2752]

[Figure 2753]

[Figure 2754]

[Figure 2755]

[Figure 2756]

[Figure 2757]

[Figure 2758]

[Figure 2759]

[Figure 2760]

[Figure 2761]

[Figure 2762]

[Figure 2763]

[Figure 2764]

[Figure 2765]

[Figure 2766]

[Figure 2767]

[Figure 2768]

[Figure 2769]

[Figure 2770]

[Figure 2771]

[Figure 2772]

[Figure 2773]

[Figure 2774]

[Figure 2775]

[Figure 2776]

[Figure 2777]

[Figure 2778]

[Figure 2779]

[Figure 2780]

[Figure 2781]

[Figure 2782]

[Figure 2783]

[Figure 2784]

[Figure 2785]

[Figure 2786]

[Figure 2787]

[Figure 2788]

[Figure 2789]

[Figure 2790]

[Figure 2791]

[Figure 2792]

[Figure 2793]

[Figure 2794]

[Figure 2795]

[Figure 2796]

[Figure 2797]

[Figure 2798]

[Figure 2799]

[Figure 2800]

[Figure 2801]

[Figure 2802]

[Figure 2803]

[Figure 2804]

[Figure 2805]

[Figure 2806]

[Figure 2807]

[Figure 2808]

[Figure 2809]

[Figure 2810]

[Figure 2811]

- 1 1.314 0.391 1 1.392 0.494 1 1.393 0.496 1 1.407 0.535
- 2 0.945 0.138 2 0.958 0.173 2 0.978 0.182 2 1.022 0.200
- 3 0.877 0.069 3 0.782 -0.099 3 0.751 -0.115 3 0.678 -0.183

3-1 -0.437 -0.322 3-1 -0.611 -0.593 3-1 -0.642 -0.611 3-1 -0.729 -0.718

[Figure 2812]

[Figure 2813]

[Figure 2814]

[Figure 2815]

[Figure 2816]

[Figure 2817]

[Figure 2818]

[Figure 2819]

[Figure 2820]

[Figure 2821]

[Figure 2822]

[Figure 2823]

Panel C: Kurtosis-Ranked Portfolios 1 Month Maturity 3 Month Maturity 6 Month Maturity 12 Month Maturity Rank Mean Char Adj Rank Mean Char Adj Rank Mean Char Adj Rank Mean Char Adj

[Figure 2824]

[Figure 2825]

[Figure 2826]

[Figure 2827]

[Figure 2828]

[Figure 2829]

[Figure 2830]

[Figure 2831]

[Figure 2832]

[Figure 2833]

[Figure 2834]

[Figure 2835]

[Figure 2836]

[Figure 2837]

[Figure 2838]

[Figure 2839]

[Figure 2840]

[Figure 2841]

[Figure 2842]

[Figure 2843]

[Figure 2844]

[Figure 2845]

[Figure 2846]

[Figure 2847]

[Figure 2848]

[Figure 2849]

[Figure 2850]

[Figure 2851]

[Figure 2852]

[Figure 2853]

[Figure 2854]

[Figure 2855]

[Figure 2856]

[Figure 2857]

[Figure 2858]

[Figure 2859]

[Figure 2860]

[Figure 2861]

[Figure 2862]

[Figure 2863]

[Figure 2864]

[Figure 2865]

[Figure 2866]

[Figure 2867]

[Figure 2868]

[Figure 2869]

[Figure 2870]

[Figure 2871]

[Figure 2872]

[Figure 2873]

[Figure 2874]

[Figure 2875]

[Figure 2876]

[Figure 2877]

[Figure 2878]

[Figure 2879]

[Figure 2880]

[Figure 2881]

[Figure 2882]

[Figure 2883]

[Figure 2884]

[Figure 2885]

[Figure 2886]

[Figure 2887]

[Figure 2888]

[Figure 2889]

[Figure 2890]

[Figure 2891]

[Figure 2892]

[Figure 2893]

[Figure 2894]

[Figure 2895]

[Figure 2896]

[Figure 2897]

[Figure 2898]

[Figure 2899]

[Figure 2900]

[Figure 2901]

[Figure 2902]

[Figure 2903]

[Figure 2904]

[Figure 2905]

[Figure 2906]

[Figure 2907]

[Figure 2908]

[Figure 2909]

[Figure 2910]

[Figure 2911]

[Figure 2912]

[Figure 2913]

[Figure 2914]

[Figure 2915]

[Figure 2916]

[Figure 2917]

[Figure 2918]

[Figure 2919]

[Figure 2920]

[Figure 2921]

[Figure 2922]

[Figure 2923]

[Figure 2924]

[Figure 2925]

[Figure 2926]

[Figure 2927]

[Figure 2928]

[Figure 2929]

[Figure 2930]

[Figure 2931]

[Figure 2932]

[Figure 2933]

[Figure 2934]

[Figure 2935]

[Figure 2936]

[Figure 2937]

[Figure 2938]

[Figure 2939]

[Figure 2940]

[Figure 2941]

[Figure 2942]

[Figure 2943]

[Figure 2944]

[Figure 2945]

[Figure 2946]

[Figure 2947]

[Figure 2948]

[Figure 2949]

[Figure 2950]

[Figure 2951]

[Figure 2952]

[Figure 2953]

[Figure 2954]

[Figure 2955]

[Figure 2956]

[Figure 2957]

[Figure 2958]

[Figure 2959]

[Figure 2960]

[Figure 2961]

[Figure 2962]

[Figure 2963]

[Figure 2964]

[Figure 2965]

[Figure 2966]

[Figure 2967]

[Figure 2968]

[Figure 2969]

[Figure 2970]

[Figure 2971]

[Figure 2972]

[Figure 2973]

[Figure 2974]

[Figure 2975]

[Figure 2976]

[Figure 2977]

[Figure 2978]

[Figure 2979]

[Figure 2980]

[Figure 2981]

[Figure 2982]

[Figure 2983]

[Figure 2984]

[Figure 2985]

[Figure 2986]

[Figure 2987]

[Figure 2988]

[Figure 2989]

[Figure 2990]

[Figure 2991]

[Figure 2992]

[Figure 2993]

[Figure 2994]

[Figure 2995]

[Figure 2996]

[Figure 2997]

[Figure 2998]

[Figure 2999]

[Figure 3000]

[Figure 3001]

[Figure 3002]

[Figure 3003]

[Figure 3004]

[Figure 3005]

[Figure 3006]

[Figure 3007]

[Figure 3008]

[Figure 3009]

[Figure 3010]

[Figure 3011]

[Figure 3012]

[Figure 3013]

[Figure 3014]

[Figure 3015]

[Figure 3016]

[Figure 3017]

[Figure 3018]

[Figure 3019]

[Figure 3020]

[Figure 3021]

[Figure 3022]

[Figure 3023]

[Figure 3024]

[Figure 3025]

[Figure 3026]

[Figure 3027]

[Figure 3028]

[Figure 3029]

[Figure 3030]

[Figure 3031]

[Figure 3032]

[Figure 3033]

[Figure 3034]

[Figure 3035]

[Figure 3036]

[Figure 3037]

[Figure 3038]

[Figure 3039]

[Figure 3040]

[Figure 3041]

[Figure 3042]

[Figure 3043]

[Figure 3044]

[Figure 3045]

[Figure 3046]

[Figure 3047]

[Figure 3048]

[Figure 3049]

[Figure 3050]

[Figure 3051]

[Figure 3052]

[Figure 3053]

[Figure 3054]

[Figure 3055]

[Figure 3056]

[Figure 3057]

[Figure 3058]

[Figure 3059]

[Figure 3060]

[Figure 3061]

[Figure 3062]

[Figure 3063]

[Figure 3064]

[Figure 3065]

[Figure 3066]

[Figure 3067]

[Figure 3068]

[Figure 3069]

[Figure 3070]

[Figure 3071]

[Figure 3072]

[Figure 3073]

[Figure 3074]

[Figure 3075]

[Figure 3076]

[Figure 3077]

[Figure 3078]

[Figure 3079]

[Figure 3080]

[Figure 3081]

[Figure 3082]

[Figure 3083]

[Figure 3084]

[Figure 3085]

[Figure 3086]

[Figure 3087]

[Figure 3088]

[Figure 3089]

[Figure 3090]

[Figure 3091]

[Figure 3092]

[Figure 3093]

[Figure 3094]

[Figure 3095]

[Figure 3096]

[Figure 3097]

[Figure 3098]

[Figure 3099]

[Figure 3100]

[Figure 3101]

[Figure 3102]

[Figure 3103]

[Figure 3104]

[Figure 3105]

[Figure 3106]

[Figure 3107]

[Figure 3108]

[Figure 3109]

[Figure 3110]

[Figure 3111]

[Figure 3112]

[Figure 3113]

[Figure 3114]

[Figure 3115]

[Figure 3116]

[Figure 3117]

[Figure 3118]

[Figure 3119]

[Figure 3120]

[Figure 3121]

[Figure 3122]

[Figure 3123]

[Figure 3124]

[Figure 3125]

[Figure 3126]

[Figure 3127]

[Figure 3128]

[Figure 3129]

[Figure 3130]

[Figure 3131]

[Figure 3132]

[Figure 3133]

[Figure 3134]

[Figure 3135]

[Figure 3136]

[Figure 3137]

[Figure 3138]

[Figure 3139]

[Figure 3140]

[Figure 3141]

[Figure 3142]

[Figure 3143]

[Figure 3144]

[Figure 3145]

[Figure 3146]

[Figure 3147]

[Figure 3148]

[Figure 3149]

[Figure 3150]

[Figure 3151]

[Figure 3152]

[Figure 3153]

[Figure 3154]

[Figure 3155]

[Figure 3156]

[Figure 3157]

[Figure 3158]

[Figure 3159]

[Figure 3160]

[Figure 3161]

[Figure 3162]

[Figure 3163]

[Figure 3164]

[Figure 3165]

[Figure 3166]

[Figure 3167]

[Figure 3168]

[Figure 3169]

[Figure 3170]

[Figure 3171]

[Figure 3172]

[Figure 3173]

[Figure 3174]

[Figure 3175]

[Figure 3176]

[Figure 3177]

[Figure 3178]

[Figure 3179]

[Figure 3180]

[Figure 3181]

[Figure 3182]

[Figure 3183]

[Figure 3184]

[Figure 3185]

[Figure 3186]

[Figure 3187]

[Figure 3188]

[Figure 3189]

[Figure 3190]

[Figure 3191]

[Figure 3192]

[Figure 3193]

[Figure 3194]

[Figure 3195]

[Figure 3196]

[Figure 3197]

[Figure 3198]

[Figure 3199]

[Figure 3200]

[Figure 3201]

[Figure 3202]

[Figure 3203]

[Figure 3204]

[Figure 3205]

[Figure 3206]

[Figure 3207]

[Figure 3208]

[Figure 3209]

[Figure 3210]

[Figure 3211]

[Figure 3212]

[Figure 3213]

[Figure 3214]

[Figure 3215]

[Figure 3216]

[Figure 3217]

[Figure 3218]

[Figure 3219]

[Figure 3220]

[Figure 3221]

[Figure 3222]

[Figure 3223]

[Figure 3224]

[Figure 3225]

[Figure 3226]

[Figure 3227]

[Figure 3228]

[Figure 3229]

[Figure 3230]

[Figure 3231]

[Figure 3232]

[Figure 3233]

[Figure 3234]

[Figure 3235]

[Figure 3236]

[Figure 3237]

[Figure 3238]

[Figure 3239]

[Figure 3240]

[Figure 3241]

[Figure 3242]

[Figure 3243]

[Figure 3244]

[Figure 3245]

[Figure 3246]

[Figure 3247]

[Figure 3248]

[Figure 3249]

[Figure 3250]

[Figure 3251]

[Figure 3252]

[Figure 3253]

[Figure 3254]

[Figure 3255]

[Figure 3256]

[Figure 3257]

[Figure 3258]

[Figure 3259]

[Figure 3260]

[Figure 3261]

[Figure 3262]

[Figure 3263]

[Figure 3264]

[Figure 3265]

[Figure 3266]

[Figure 3267]

[Figure 3268]

[Figure 3269]

[Figure 3270]

[Figure 3271]

[Figure 3272]

[Figure 3273]

[Figure 3274]

[Figure 3275]

[Figure 3276]

[Figure 3277]

[Figure 3278]

[Figure 3279]

[Figure 3280]

[Figure 3281]

[Figure 3282]

[Figure 3283]

[Figure 3284]

[Figure 3285]

[Figure 3286]

[Figure 3287]

[Figure 3288]

[Figure 3289]

[Figure 3290]

[Figure 3291]

[Figure 3292]

[Figure 3293]

[Figure 3294]

[Figure 3295]

[Figure 3296]

[Figure 3297]

[Figure 3298]

[Figure 3299]

[Figure 3300]

[Figure 3301]

[Figure 3302]

[Figure 3303]

[Figure 3304]

[Figure 3305]

[Figure 3306]

[Figure 3307]

[Figure 3308]

[Figure 3309]

[Figure 3310]

[Figure 3311]

[Figure 3312]

[Figure 3313]

[Figure 3314]

[Figure 3315]

[Figure 3316]

[Figure 3317]

[Figure 3318]

[Figure 3319]

[Figure 3320]

[Figure 3321]

[Figure 3322]

[Figure 3323]

[Figure 3324]

[Figure 3325]

[Figure 3326]

[Figure 3327]

[Figure 3328]

[Figure 3329]

[Figure 3330]

[Figure 3331]

[Figure 3332]

[Figure 3333]

[Figure 3334]

[Figure 3335]

[Figure 3336]

[Figure 3337]

[Figure 3338]

[Figure 3339]

[Figure 3340]

[Figure 3341]

[Figure 3342]

[Figure 3343]

[Figure 3344]

[Figure 3345]

[Figure 3346]

[Figure 3347]

[Figure 3348]

[Figure 3349]

[Figure 3350]

[Figure 3351]

[Figure 3352]

[Figure 3353]

[Figure 3354]

[Figure 3355]

- 1 1.119 0.329 1 0.944 0.128 1 0.699 -0.159 1 0.691 -0.177
- 2 0.905 0.103 2 0.994 0.172 2 1.142 0.330 2 1.158 0.353
- 3 1.124 0.196 3 1.180 0.282 3 1.226 0.345 3 1.212 0.324

3-1 0.005 -0.133 3-1 0.236 0.154 3-1 0.527 0.505 3-1 0.521 0.501

[Figure 3356]

[Figure 3357]

[Figure 3358]

[Figure 3359]

[Figure 3360]

[Figure 3361]

[Figure 3362]

[Figure 3363]

[Figure 3364]

[Figure 3365]

[Figure 3366]

[Figure 3367]

- 49

Table A2: Time Series Regressions

The table presents the results of time series regressions of excess return differentials (Hi-Lo) between portfolios ranked on risk neutral volatility, skewness, and kurtosis on the three Fama and French (1993) factors MRP (the return on the value-weighted market portfolio in excess of a onemonth T-Bill), SMB (the difference in returns on a portfolio of small capitalization and large capitalization stocks) HML (the difference in returns on a portfolio of high and low book equity to market equity stocks), and LIQ, the liquidity factor from Pastor and Stambaugh (2001). The moment-sorted portfolios are equally-weighted, formed on the basis of terciles and re-formed each month. The table presents point estimates of the coefﬁcients and standard errors in parentheses. Data cover the period January 1996 through December 2004 for 107 monthly observations.

Panel A: 1 Month to Maturity Panel B: 3 Months to Maturity

[Figure 3368]

[Figure 3369]

[Figure 3370]

[Figure 3371]

[Figure 3372]

[Figure 3373]

[Figure 3374]

[Figure 3375]

[Figure 3376]

[Figure 3377]

[Figure 3378]

[Figure 3379]

[Figure 3380]

[Figure 3381]

[Figure 3382]

[Figure 3383]

[Figure 3384]

[Figure 3385]

[Figure 3386]

[Figure 3387]

[Figure 3388]

[Figure 3389]

[Figure 3390]

[Figure 3391]

[Figure 3392]

[Figure 3393]

[Figure 3394]

[Figure 3395]

[Figure 3396]

[Figure 3397]

[Figure 3398]

[Figure 3399]

[Figure 3400]

[Figure 3401]

[Figure 3402]

[Figure 3403]

[Figure 3404]

[Figure 3405]

[Figure 3406]

[Figure 3407]

[Figure 3408]

[Figure 3409]

[Figure 3410]

[Figure 3411]

[Figure 3412]

[Figure 3413]

[Figure 3414]

[Figure 3415]

[Figure 3416]

[Figure 3417]

[Figure 3418]

[Figure 3419]

[Figure 3420]

[Figure 3421]

[Figure 3422]

[Figure 3423]

[Figure 3424]

[Figure 3425]

[Figure 3426]

[Figure 3427]

[Figure 3428]

[Figure 3429]

[Figure 3430]

[Figure 3431]

[Figure 3432]

[Figure 3433]

[Figure 3434]

[Figure 3435]

[Figure 3436]

[Figure 3437]

[Figure 3438]

[Figure 3439]

[Figure 3440]

[Figure 3441]

[Figure 3442]

[Figure 3443]

[Figure 3444]

[Figure 3445]

[Figure 3446]

[Figure 3447]

[Figure 3448]

[Figure 3449]

[Figure 3450]

[Figure 3451]

[Figure 3452]

[Figure 3453]

[Figure 3454]

[Figure 3455]

[Figure 3456]

[Figure 3457]

[Figure 3458]

[Figure 3459]

[Figure 3460]

[Figure 3461]

[Figure 3462]

[Figure 3463]

[Figure 3464]

[Figure 3465]

[Figure 3466]

[Figure 3467]

[Figure 3468]

[Figure 3469]

[Figure 3470]

[Figure 3471]

[Figure 3472]

[Figure 3473]

[Figure 3474]

[Figure 3475]

[Figure 3476]

[Figure 3477]

[Figure 3478]

[Figure 3479]

[Figure 3480]

[Figure 3481]

[Figure 3482]

[Figure 3483]

[Figure 3484]

[Figure 3485]

[Figure 3486]

[Figure 3487]

[Figure 3488]

[Figure 3489]

[Figure 3490]

[Figure 3491]

[Figure 3492]

[Figure 3493]

[Figure 3494]

[Figure 3495]

[Figure 3496]

[Figure 3497]

[Figure 3498]

[Figure 3499]

[Figure 3500]

[Figure 3501]

[Figure 3502]

[Figure 3503]

[Figure 3504]

[Figure 3505]

[Figure 3506]

[Figure 3507]

[Figure 3508]

[Figure 3509]

[Figure 3510]

[Figure 3511]

[Figure 3512]

[Figure 3513]

[Figure 3514]

[Figure 3515]

[Figure 3516]

[Figure 3517]

[Figure 3518]

[Figure 3519]

[Figure 3520]

[Figure 3521]

[Figure 3522]

[Figure 3523]

[Figure 3524]

[Figure 3525]

[Figure 3526]

[Figure 3527]

[Figure 3528]

[Figure 3529]

[Figure 3530]

[Figure 3531]

[Figure 3532]

[Figure 3533]

[Figure 3534]

[Figure 3535]

[Figure 3536]

[Figure 3537]

[Figure 3538]

[Figure 3539]

[Figure 3540]

[Figure 3541]

[Figure 3542]

[Figure 3543]

[Figure 3544]

[Figure 3545]

[Figure 3546]

[Figure 3547]

[Figure 3548]

[Figure 3549]

[Figure 3550]

[Figure 3551]

[Figure 3552]

[Figure 3553]

[Figure 3554]

[Figure 3555]

[Figure 3556]

[Figure 3557]

[Figure 3558]

[Figure 3559]

[Figure 3560]

[Figure 3561]

[Figure 3562]

[Figure 3563]

[Figure 3564]

[Figure 3565]

[Figure 3566]

[Figure 3567]

[Figure 3568]

[Figure 3569]

[Figure 3570]

[Figure 3571]

[Figure 3572]

[Figure 3573]

[Figure 3574]

[Figure 3575]

[Figure 3576]

[Figure 3577]

[Figure 3578]

[Figure 3579]

[Figure 3580]

[Figure 3581]

[Figure 3582]

[Figure 3583]

[Figure 3584]

[Figure 3585]

[Figure 3586]

[Figure 3587]

[Figure 3588]

[Figure 3589]

[Figure 3590]

[Figure 3591]

[Figure 3592]

[Figure 3593]

[Figure 3594]

[Figure 3595]

[Figure 3596]

[Figure 3597]

[Figure 3598]

[Figure 3599]

[Figure 3600]

[Figure 3601]

[Figure 3602]

[Figure 3603]

[Figure 3604]

[Figure 3605]

[Figure 3606]

[Figure 3607]

[Figure 3608]

[Figure 3609]

[Figure 3610]

[Figure 3611]

[Figure 3612]

[Figure 3613]

[Figure 3614]

[Figure 3615]

[Figure 3616]

[Figure 3617]

[Figure 3618]

[Figure 3619]

[Figure 3620]

[Figure 3621]

[Figure 3622]

[Figure 3623]

[Figure 3624]

[Figure 3625]

[Figure 3626]

[Figure 3627]

[Figure 3628]

[Figure 3629]

[Figure 3630]

[Figure 3631]

[Figure 3632]

[Figure 3633]

[Figure 3634]

[Figure 3635]

[Figure 3636]

[Figure 3637]

[Figure 3638]

[Figure 3639]

[Figure 3640]

[Figure 3641]

[Figure 3642]

[Figure 3643]

[Figure 3644]

[Figure 3645]

[Figure 3646]

[Figure 3647]

[Figure 3648]

[Figure 3649]

[Figure 3650]

[Figure 3651]

[Figure 3652]

[Figure 3653]

[Figure 3654]

[Figure 3655]

[Figure 3656]

[Figure 3657]

[Figure 3658]

[Figure 3659]

[Figure 3660]

[Figure 3661]

[Figure 3662]

[Figure 3663]

[Figure 3664]

[Figure 3665]

[Figure 3666]

[Figure 3667]

[Figure 3668]

[Figure 3669]

[Figure 3670]

[Figure 3671]

[Figure 3672]

[Figure 3673]

[Figure 3674]

[Figure 3675]

[Figure 3676]

[Figure 3677]

[Figure 3678]

[Figure 3679]

[Figure 3680]

[Figure 3681]

[Figure 3682]

[Figure 3683]

[Figure 3684]

[Figure 3685]

[Figure 3686]

[Figure 3687]

[Figure 3688]

[Figure 3689]

[Figure 3690]

[Figure 3691]

[Figure 3692]

[Figure 3693]

[Figure 3694]

[Figure 3695]

[Figure 3696]

[Figure 3697]

[Figure 3698]

[Figure 3699]

[Figure 3700]

[Figure 3701]

[Figure 3702]

[Figure 3703]

[Figure 3704]

[Figure 3705]

[Figure 3706]

[Figure 3707]

[Figure 3708]

[Figure 3709]

[Figure 3710]

[Figure 3711]

[Figure 3712]

[Figure 3713]

[Figure 3714]

[Figure 3715]

[Figure 3716]

[Figure 3717]

[Figure 3718]

[Figure 3719]

[Figure 3720]

[Figure 3721]

[Figure 3722]

[Figure 3723]

[Figure 3724]

[Figure 3725]

[Figure 3726]

[Figure 3727]

[Figure 3728]

[Figure 3729]

[Figure 3730]

[Figure 3731]

[Figure 3732]

[Figure 3733]

[Figure 3734]

[Figure 3735]

[Figure 3736]

[Figure 3737]

[Figure 3738]

[Figure 3739]

[Figure 3740]

[Figure 3741]

[Figure 3742]

[Figure 3743]

[Figure 3744]

[Figure 3745]

[Figure 3746]

[Figure 3747]

[Figure 3748]

[Figure 3749]

[Figure 3750]

[Figure 3751]

[Figure 3752]

[Figure 3753]

[Figure 3754]

[Figure 3755]

[Figure 3756]

[Figure 3757]

[Figure 3758]

[Figure 3759]

[Figure 3760]

[Figure 3761]

[Figure 3762]

[Figure 3763]

[Figure 3764]

[Figure 3765]

[Figure 3766]

[Figure 3767]

[Figure 3768]

[Figure 3769]

[Figure 3770]

[Figure 3771]

[Figure 3772]

[Figure 3773]

[Figure 3774]

[Figure 3775]

[Figure 3776]

[Figure 3777]

[Figure 3778]

[Figure 3779]

[Figure 3780]

[Figure 3781]

[Figure 3782]

[Figure 3783]

[Figure 3784]

[Figure 3785]

[Figure 3786]

[Figure 3787]

[Figure 3788]

[Figure 3789]

[Figure 3790]

[Figure 3791]

[Figure 3792]

[Figure 3793]

[Figure 3794]

[Figure 3795]

[Figure 3796]

[Figure 3797]

[Figure 3798]

[Figure 3799]

[Figure 3800]

[Figure 3801]

[Figure 3802]

[Figure 3803]

[Figure 3804]

[Figure 3805]

[Figure 3806]

[Figure 3807]

[Figure 3808]

[Figure 3809]

[Figure 3810]

[Figure 3811]

[Figure 3812]

[Figure 3813]

[Figure 3814]

[Figure 3815]

[Figure 3816]

[Figure 3817]

[Figure 3818]

[Figure 3819]

[Figure 3820]

[Figure 3821]

[Figure 3822]

[Figure 3823]

[Figure 3824]

[Figure 3825]

[Figure 3826]

[Figure 3827]

[Figure 3828]

[Figure 3829]

[Figure 3830]

[Figure 3831]

[Figure 3832]

[Figure 3833]

[Figure 3834]

[Figure 3835]

[Figure 3836]

[Figure 3837]

[Figure 3838]

[Figure 3839]

[Figure 3840]

[Figure 3841]

[Figure 3842]

[Figure 3843]

[Figure 3844]

[Figure 3845]

[Figure 3846]

[Figure 3847]

[Figure 3848]

[Figure 3849]

[Figure 3850]

[Figure 3851]

[Figure 3852]

[Figure 3853]

[Figure 3854]

[Figure 3855]

[Figure 3856]

[Figure 3857]

[Figure 3858]

[Figure 3859]

[Figure 3860]

[Figure 3861]

[Figure 3862]

[Figure 3863]

[Figure 3864]

[Figure 3865]

[Figure 3866]

[Figure 3867]

[Figure 3868]

[Figure 3869]

[Figure 3870]

[Figure 3871]

[Figure 3872]

[Figure 3873]

[Figure 3874]

[Figure 3875]

[Figure 3876]

[Figure 3877]

[Figure 3878]

[Figure 3879]

[Figure 3880]

[Figure 3881]

[Figure 3882]

[Figure 3883]

[Figure 3884]

[Figure 3885]

[Figure 3886]

[Figure 3887]

[Figure 3888]

[Figure 3889]

[Figure 3890]

[Figure 3891]

α βMRP βSMB βHML βLIQ R2 α βMRP βSMB βHML βLIQ R2 Vol -0.57 0.52 1.01 -0.61 -0.26 0.81 Vol -0.63 0.57 1.01 -1.06 -0.16 0.86

[Figure 3892]

[Figure 3893]

[Figure 3894]

[Figure 3895]

[Figure 3896]

[Figure 3897]

[Figure 3898]

[Figure 3899]

[Figure 3900]

[Figure 3901]

[Figure 3902]

[Figure 3903]

[Figure 3904]

[Figure 3905]

- -1.61 4.66 10.01 -5.15 -4.35 -1.62 4.46 9.31 -8.18 -2.31 Skew -0.50 0.13 0.16 0.47 -0.35 0.54 Skew -0.61 0.18 0.06 0.29 -0.33 0.42
- -1.64 2.01 1.67 4.00 -5.39 -1.89 2.71 0.56 2.21 -4.17 Kurt 0.49 -0.19 -0.45 -0.45 0.23 0.49 Kurt 0.57 -0.29 -0.36 -0.11 0.20 0.33

2.21 -3.78 -6.74 -5.91 6.08 2.04 -4.00 -3.65 -0.96 3.13

[Figure 3906]

[Figure 3907]

[Figure 3908]

[Figure 3909]

[Figure 3910]

[Figure 3911]

[Figure 3912]

[Figure 3913]

[Figure 3914]

[Figure 3915]

[Figure 3916]

[Figure 3917]

[Figure 3918]

[Figure 3919]

Panel C: 6 Months to Maturity Panel D: 12 Months to Maturity α βMRP βSMB βHML βLIQ R2 α βMRP βSMB βHML βLIQ R2

[Figure 3920]

[Figure 3921]

[Figure 3922]

[Figure 3923]

[Figure 3924]

[Figure 3925]

[Figure 3926]

[Figure 3927]

[Figure 3928]

[Figure 3929]

[Figure 3930]

[Figure 3931]

[Figure 3932]

[Figure 3933]

[Figure 3934]

[Figure 3935]

[Figure 3936]

[Figure 3937]

[Figure 3938]

[Figure 3939]

[Figure 3940]

[Figure 3941]

[Figure 3942]

[Figure 3943]

[Figure 3944]

[Figure 3945]

[Figure 3946]

[Figure 3947]

[Figure 3948]

[Figure 3949]

[Figure 3950]

[Figure 3951]

[Figure 3952]

[Figure 3953]

[Figure 3954]

[Figure 3955]

[Figure 3956]

[Figure 3957]

[Figure 3958]

[Figure 3959]

[Figure 3960]

[Figure 3961]

[Figure 3962]

[Figure 3963]

[Figure 3964]

[Figure 3965]

[Figure 3966]

[Figure 3967]

[Figure 3968]

[Figure 3969]

[Figure 3970]

[Figure 3971]

[Figure 3972]

[Figure 3973]

[Figure 3974]

[Figure 3975]

[Figure 3976]

[Figure 3977]

[Figure 3978]

[Figure 3979]

[Figure 3980]

[Figure 3981]

[Figure 3982]

[Figure 3983]

[Figure 3984]

[Figure 3985]

[Figure 3986]

[Figure 3987]

[Figure 3988]

[Figure 3989]

[Figure 3990]

[Figure 3991]

[Figure 3992]

[Figure 3993]

[Figure 3994]

[Figure 3995]

[Figure 3996]

[Figure 3997]

[Figure 3998]

[Figure 3999]

[Figure 4000]

[Figure 4001]

[Figure 4002]

[Figure 4003]

[Figure 4004]

[Figure 4005]

[Figure 4006]

[Figure 4007]

[Figure 4008]

[Figure 4009]

[Figure 4010]

[Figure 4011]

[Figure 4012]

[Figure 4013]

[Figure 4014]

[Figure 4015]

[Figure 4016]

[Figure 4017]

[Figure 4018]

[Figure 4019]

[Figure 4020]

[Figure 4021]

[Figure 4022]

[Figure 4023]

[Figure 4024]

[Figure 4025]

[Figure 4026]

[Figure 4027]

[Figure 4028]

[Figure 4029]

[Figure 4030]

[Figure 4031]

[Figure 4032]

[Figure 4033]

[Figure 4034]

[Figure 4035]

[Figure 4036]

[Figure 4037]

[Figure 4038]

[Figure 4039]

[Figure 4040]

[Figure 4041]

[Figure 4042]

[Figure 4043]

[Figure 4044]

[Figure 4045]

[Figure 4046]

[Figure 4047]

[Figure 4048]

[Figure 4049]

[Figure 4050]

[Figure 4051]

[Figure 4052]

[Figure 4053]

[Figure 4054]

[Figure 4055]

[Figure 4056]

[Figure 4057]

[Figure 4058]

[Figure 4059]

[Figure 4060]

[Figure 4061]

[Figure 4062]

[Figure 4063]

[Figure 4064]

[Figure 4065]

[Figure 4066]

[Figure 4067]

[Figure 4068]

[Figure 4069]

[Figure 4070]

[Figure 4071]

[Figure 4072]

[Figure 4073]

[Figure 4074]

[Figure 4075]

[Figure 4076]

[Figure 4077]

[Figure 4078]

[Figure 4079]

[Figure 4080]

[Figure 4081]

[Figure 4082]

[Figure 4083]

[Figure 4084]

[Figure 4085]

[Figure 4086]

[Figure 4087]

[Figure 4088]

[Figure 4089]

[Figure 4090]

[Figure 4091]

[Figure 4092]

[Figure 4093]

[Figure 4094]

[Figure 4095]

[Figure 4096]

[Figure 4097]

[Figure 4098]

[Figure 4099]

[Figure 4100]

[Figure 4101]

[Figure 4102]

[Figure 4103]

[Figure 4104]

[Figure 4105]

[Figure 4106]

[Figure 4107]

[Figure 4108]

[Figure 4109]

[Figure 4110]

[Figure 4111]

[Figure 4112]

[Figure 4113]

[Figure 4114]

[Figure 4115]

[Figure 4116]

[Figure 4117]

[Figure 4118]

[Figure 4119]

[Figure 4120]

[Figure 4121]

[Figure 4122]

[Figure 4123]

[Figure 4124]

[Figure 4125]

[Figure 4126]

[Figure 4127]

[Figure 4128]

[Figure 4129]

[Figure 4130]

[Figure 4131]

[Figure 4132]

[Figure 4133]

[Figure 4134]

[Figure 4135]

[Figure 4136]

[Figure 4137]

[Figure 4138]

[Figure 4139]

[Figure 4140]

[Figure 4141]

[Figure 4142]

[Figure 4143]

[Figure 4144]

[Figure 4145]

[Figure 4146]

[Figure 4147]

[Figure 4148]

[Figure 4149]

[Figure 4150]

[Figure 4151]

[Figure 4152]

[Figure 4153]

[Figure 4154]

[Figure 4155]

[Figure 4156]

[Figure 4157]

[Figure 4158]

[Figure 4159]

[Figure 4160]

[Figure 4161]

[Figure 4162]

[Figure 4163]

[Figure 4164]

[Figure 4165]

[Figure 4166]

[Figure 4167]

[Figure 4168]

[Figure 4169]

[Figure 4170]

[Figure 4171]

[Figure 4172]

[Figure 4173]

[Figure 4174]

[Figure 4175]

[Figure 4176]

[Figure 4177]

[Figure 4178]

[Figure 4179]

[Figure 4180]

[Figure 4181]

[Figure 4182]

[Figure 4183]

[Figure 4184]

[Figure 4185]

[Figure 4186]

[Figure 4187]

[Figure 4188]

[Figure 4189]

[Figure 4190]

[Figure 4191]

[Figure 4192]

[Figure 4193]

[Figure 4194]

[Figure 4195]

[Figure 4196]

[Figure 4197]

[Figure 4198]

[Figure 4199]

[Figure 4200]

[Figure 4201]

[Figure 4202]

[Figure 4203]

[Figure 4204]

[Figure 4205]

[Figure 4206]

[Figure 4207]

[Figure 4208]

[Figure 4209]

[Figure 4210]

[Figure 4211]

[Figure 4212]

[Figure 4213]

[Figure 4214]

[Figure 4215]

[Figure 4216]

[Figure 4217]

[Figure 4218]

[Figure 4219]

[Figure 4220]

[Figure 4221]

[Figure 4222]

[Figure 4223]

[Figure 4224]

[Figure 4225]

[Figure 4226]

[Figure 4227]

[Figure 4228]

[Figure 4229]

[Figure 4230]

[Figure 4231]

[Figure 4232]

[Figure 4233]

[Figure 4234]

[Figure 4235]

[Figure 4236]

[Figure 4237]

[Figure 4238]

[Figure 4239]

[Figure 4240]

[Figure 4241]

[Figure 4242]

[Figure 4243]

[Figure 4244]

[Figure 4245]

[Figure 4246]

[Figure 4247]

[Figure 4248]

[Figure 4249]

[Figure 4250]

[Figure 4251]

[Figure 4252]

[Figure 4253]

[Figure 4254]

[Figure 4255]

[Figure 4256]

[Figure 4257]

[Figure 4258]

[Figure 4259]

[Figure 4260]

[Figure 4261]

[Figure 4262]

[Figure 4263]

[Figure 4264]

[Figure 4265]

[Figure 4266]

[Figure 4267]

[Figure 4268]

[Figure 4269]

[Figure 4270]

[Figure 4271]

[Figure 4272]

[Figure 4273]

[Figure 4274]

[Figure 4275]

[Figure 4276]

[Figure 4277]

[Figure 4278]

[Figure 4279]

[Figure 4280]

[Figure 4281]

[Figure 4282]

[Figure 4283]

[Figure 4284]

[Figure 4285]

[Figure 4286]

[Figure 4287]

[Figure 4288]

[Figure 4289]

[Figure 4290]

[Figure 4291]

[Figure 4292]

[Figure 4293]

[Figure 4294]

[Figure 4295]

[Figure 4296]

[Figure 4297]

[Figure 4298]

[Figure 4299]

[Figure 4300]

[Figure 4301]

[Figure 4302]

[Figure 4303]

[Figure 4304]

[Figure 4305]

[Figure 4306]

[Figure 4307]

[Figure 4308]

[Figure 4309]

[Figure 4310]

[Figure 4311]

[Figure 4312]

[Figure 4313]

[Figure 4314]

[Figure 4315]

[Figure 4316]

[Figure 4317]

[Figure 4318]

[Figure 4319]

[Figure 4320]

[Figure 4321]

[Figure 4322]

[Figure 4323]

[Figure 4324]

[Figure 4325]

[Figure 4326]

[Figure 4327]

[Figure 4328]

[Figure 4329]

[Figure 4330]

[Figure 4331]

[Figure 4332]

[Figure 4333]

[Figure 4334]

[Figure 4335]

[Figure 4336]

[Figure 4337]

[Figure 4338]

[Figure 4339]

[Figure 4340]

[Figure 4341]

[Figure 4342]

[Figure 4343]

[Figure 4344]

[Figure 4345]

[Figure 4346]

[Figure 4347]

[Figure 4348]

[Figure 4349]

[Figure 4350]

[Figure 4351]

[Figure 4352]

[Figure 4353]

[Figure 4354]

[Figure 4355]

[Figure 4356]

[Figure 4357]

[Figure 4358]

[Figure 4359]

[Figure 4360]

[Figure 4361]

[Figure 4362]

[Figure 4363]

[Figure 4364]

[Figure 4365]

[Figure 4366]

[Figure 4367]

[Figure 4368]

[Figure 4369]

[Figure 4370]

[Figure 4371]

[Figure 4372]

[Figure 4373]

[Figure 4374]

[Figure 4375]

[Figure 4376]

[Figure 4377]

[Figure 4378]

[Figure 4379]

[Figure 4380]

[Figure 4381]

[Figure 4382]

[Figure 4383]

[Figure 4384]

[Figure 4385]

[Figure 4386]

[Figure 4387]

[Figure 4388]

[Figure 4389]

[Figure 4390]

[Figure 4391]

[Figure 4392]

[Figure 4393]

[Figure 4394]

[Figure 4395]

[Figure 4396]

[Figure 4397]

[Figure 4398]

[Figure 4399]

[Figure 4400]

[Figure 4401]

[Figure 4402]

[Figure 4403]

[Figure 4404]

[Figure 4405]

[Figure 4406]

[Figure 4407]

[Figure 4408]

[Figure 4409]

[Figure 4410]

[Figure 4411]

[Figure 4412]

[Figure 4413]

[Figure 4414]

[Figure 4415]

[Figure 4416]

[Figure 4417]

[Figure 4418]

[Figure 4419]

[Figure 4420]

[Figure 4421]

[Figure 4422]

[Figure 4423]

[Figure 4424]

[Figure 4425]

[Figure 4426]

[Figure 4427]

[Figure 4428]

[Figure 4429]

[Figure 4430]

[Figure 4431]

[Figure 4432]

[Figure 4433]

[Figure 4434]

[Figure 4435]

[Figure 4436]

[Figure 4437]

[Figure 4438]

[Figure 4439]

[Figure 4440]

[Figure 4441]

[Figure 4442]

[Figure 4443]

[Figure 4444]

[Figure 4445]

[Figure 4446]

[Figure 4447]

[Figure 4448]

[Figure 4449]

[Figure 4450]

[Figure 4451]

[Figure 4452]

[Figure 4453]

[Figure 4454]

[Figure 4455]

[Figure 4456]

[Figure 4457]

Vol -0.61 0.60 1.00 -1.26 -0.14 0.87 Vol -0.45 0.55 0.92 -1.32 -0.12 0.86

- -1.52 4.55 8.88 -8.96 -1.86 -1.13 4.23 8.55 -9.67 -1.71

Skew -0.64 0.17 0.15 0.07 -0.26 0.27 Skew -0.62 0.19 0.21 0.04 -0.26 0.28

- -2.47 2.57 1.57 0.57 -3.72 -2.39 3.00 2.25 0.36 -3.78

Kurt 0.56 -0.33 -0.36 0.17 0.18 0.52 Kurt 0.61 -0.37 -0.42 0.16 0.20 0.58 2.10 -3.61 -3.85 1.64 3.07 2.32 -3.97 -4.64 1.72 3.38

[Figure 4458]

[Figure 4459]

[Figure 4460]

[Figure 4461]

[Figure 4462]

[Figure 4463]

[Figure 4464]

[Figure 4465]

[Figure 4466]

[Figure 4467]

[Figure 4468]

[Figure 4469]

[Figure 4470]

[Figure 4471]

