|[Figure 1]<br><br>This may be the author’s version of a work that was submitted/accepted for publication in the following source:<br><br>Mensi, Walid, Beljid, Makram, Boubaker, Adel, & Managi, Shunsuke<br><br>(2013) Correlations and volatility spillovers across commodity and stock markets: Linking energies, food, and gold. Economic Modelling, 32, pp. 15-22.<br><br>This ﬁle was downloaded from: https://eprints.qut.edu.au/75383/<br><br>© Consult author(s) regarding copyright matters<br><br>This work is covered by copyright. Unless the document is being made available under a Creative Commons Licence, you must assume that re-use is limited to personal use and that permission from the copyright owner must be obtained for all other uses. If the document is available under a Creative Commons License (or other speciﬁed license) then refer to the Licence for details of permitted re-use. It is a condition of access that users recognise and abide by the legal requirements associated with these rights. If you believe that this work infringes copyright please provide details by email to qut.copyright@qut.edu.au<br><br>License: Creative Commons: Attribution-Noncommercial-No Derivative Works 2.5<br><br>Notice: Please note that this document may not be the Version of Record (i.e. published version) of the work. Author manuscript versions (as Submitted for peer review or as Accepted for publication after peer review) can be identiﬁed by an absence of publisher branding and/or typeset appearance. If there is any doubt, please refer to the published source.<br><br>https://doi.org/10.1016/j.econmod.2013.01.023|
|---|

## Walid Mensi1, Makram Beljid 1, Adel Boubaker1

1. Department of Finance, Faculty of Management and Economic Sciences of Tunis, El Manar University, B.P. 248, C.P. 2092, Tunis Cedex, Tunisia

and

## Shunsuke Managi 2,3,4*

2. Graduate School of Environmental Studies, Tohoku University, 6-6-20 Aramaki-Aza Aoba, Aoba-Ku, Sendai 980-8579, Japan Telephone: +81-22-795-4504 / Fax: +81-22-795-4309 / Email: managi.s@gmail.com (* Corresponding author)

- 3. Graduate School of Public Policy, University of Tokyo, Japan
- 4. The Institute for Global Environmental Strategies, Hayama, Japan

## ABSTRACT

This paper employs a VAR-GARCH model to investigate the return links and volatility transmission between the S&P 500 and commodity price indices for energy, food, gold and beverages over the turbulent period from 2000-2011. Understanding the price behavior of commodity prices and the volatility transmission mechanism between these markets and the stock exchanges are crucial for each participant, including governments, traders, portfolio managers, consumers, and producers. For return and volatility spillover, the results show significant transmission among the S&P 500 and commodity markets. The past shocks and volatility of the S&P 500 strongly influenced the oil and gold markets. This study finds that the highest conditional correlations are between the S&P 500 and gold index and the S&P 500 and WTI index. We also analyze the optimal weights and hedge ratios for commodities/S&P 500 portfolio holdings using the estimates for each index. Overall, our findings illustrate several important implications for portfolio hedgers for making optimal portfolio allocations, engaging in risk management and forecasting future volatility in equity and commodity markets.

Keywords: Stock markets, Commodity prices, Volatility spillovers, Hedge ratios, VAR-GARCH models, Energy price

## 1. Introduction

Over the past two decades, international markets have become increasingly volatile after the financial liberalization and opening of economies, and this phenomenon has generated increasing interest in the analysis of market volatility. With both the increasing integration and high level of volatility of major financial markets, commodity behavior and equity prices grew more sensitive to innovations, such as deregulation, weather, war, political economic, investors’ psychological expectations (Yu et al., 2008), revolutions and unforeseen events. In recent years, commodity markets have experienced a rapid growth in liquidity and an influx of investors who are attracted to commodities purely as investments (financial assets and securities), rather than as a means to support “real” economic activity via the hedging of risks (Vivian and Wohar, 2012 p. 395). The large swings in gold, oil and wheat prices are associated with financial crashes, wars and adverse weather conditions. For example,1 the wheat unit price began trading at $107 in January 2000 and reached a high of $306 in December 2011. Brent prices have displayed a similar behavior, trading at $23.95 per barrel in January 2000 and reaching $108.09 per barrel by December 2011.

This volatility is puzzling for researchers, academicians, and portfolio managers. Understanding time-varying volatility and the volatility transmission mechanisms found across different types of markets was essential to both international investors and policy makers. Most studies test volatility spillover among different key stock markets or between the crude oil market and financial markets (e.g., Hassan and Malik, 2007; Lien and Yang, 2008; Malik and Ewing, 2009; Singh et al., 2010; Yilmaz, 2010; Du et al., 2011; He and Chen, 2011; Serra, 2011; Syllignakis et Kouretas, 2011; Arouri et al., 2012; Kumar et al., 2012; Sadorsky, 2012). Several empirical methods were used in these studies. However, a Multivariate Generalized Autoregressive Conditional Heteroskedasticity (MGARCH) model was employed to analyze the relationship between political and economic news on the conditional volatility of financial variables (Fornari et al., 2002) and the effect of macroeconomic shocks on financial sectors (Ewing et al., 2003). More recently, the vector autoregressive- Generalized Autoregressive Conditional Heteroskedasticity model (VAR-GARCH) has been commonly used to examine temporal volatility spillovers between developed and emerging stock markets (Singh et al., 2010). Studies of volatility spillovers have important implications for portfolio managers, the development of accurate asset pricing models and the forecasting of future equity and the volatility of oil price return (Malik and Hammoudeh, 2007). Moreover, previous studies focused on volatility spillovers by investigating volatility in emerging and developed financial markets (Wang and Wang, 2010; Yilmaz, 2010).

- 1 Wheat and Brent prices were extracted respectively from International Grains Council (IGC) and Energy Information Administration (EIA) websites.

The aim of this paper is to investigate the joint evolution of conditional returns, the correlation and volatility spillovers between the markets for beverages, agricultural commodities, crude oil, and metal and the stock exchange in the last twelve turbulent years. To the best of our knowledge, this study is the first to simultaneously examine the volatility transmission among these markets. The S&P 500 index and gold, crude oil, wheat and beverage markets are the main representatives of the large commodity markets, and it is of fundamental practical significance to analyze how volatility and shocks are transmitted among these markets. Volatile metal, oil, and agricultural commodity prices concern governments, traders, producers, and consumers. To perform this analysis, a developed econometric methodology was used; thus, a VAR-GARCH model that was introduced by Ling and McAleer (2003) was used for the S&P 500 index, oil spot prices, and the commodity indexes for beverages, food and metal from January 3, 2000 to December 31, 2011. One of the main advantages of this model is that it allows us to investigate the shock transmissions, the dynamics of conditional volatility and volatility spillovers between series. The model also provides meaningful estimates of the unknown parameters with less computational complications than several other multivariate specifications, such as the full-factor multivariate GARCH model (Hammoudeh et al., 2009). This aspect of this model allows us to observe the impact of commodity market events or news on the S&P 500 index returns, as well as the impact of market events or news on commodity market returns. The empirical results support evidence of transmission volatility among commodity markets and the stock exchanges.

This paper is structured as follows: Section 2 presents recent empirical studies. Section 3 specifies the VAR-GARCH model used in this study. The data and reports on the empirical results are described in Section 4, and Section 5 provides the economic implications of the results for designing optimal portfolios and formulating optimal hedging strategies. Summary conclusions are presented in Section 6.

## 2. Literature review

Liberalization and cointegration were the main elements of transmission shocks and volatility between markets. However, market participants were mostly concerned with volatility spillovers between commodity markets and equity markets. There is a body of literature devoted to the interactions between international markets and across sectors (see Hassan and Malik, 2007; Malik and Ewing 2009; Sadorsky, 2012). Maghyereh and Al-Kandari (2007) used nonparametric rank tests for nonlinear co-integration analysis and concluded that oil prices directly impact the stock price indices in the GCC countries in a nonlinear fashion. Using daily closing spot prices from 1994 to 2001 and a multivariate GARCH model with BEKK parameterization on US equity, the global crude oil market, and the equity markets of Saudi Arabia, Kuwait, and Bahrain, Malik and Hammoudeh (2007) tested the volatility and shock transmission mechanism and found significant

volatility spillovers between the US equity market and global oil markets. Their results also revealed that equity markets in the Gulf receive volatility spillovers from the oil market, with the exception of Saudi Arabia, for which their data indicated a significant volatility spillover from the Saudi market to the oil market. Moreover, Park and Ratti (2008) looked into the effect of the shocks that occurred in oil prices on stock exchange returns in USA and 13 other European countries using VAR model and the data between 1986 and 2005. They found that the oil price shocks had a strong effect on stock returns with the exception of USA. In other work, Malik and Ewing (2009) employed bivariate GARCH models to test the volatility transmission between five US sector indexes2 and the oil market from January 1, 1992 to April 30, 2008, which provided evidence for the significant transmission of shocks and volatility between oil prices and some of the market sectors.

Lien and Yang (2008) tested dynamic minimum variance hedge ratios (MVHRs) using a bivariate GARCH model for ten commodity futures contracts3 from January 1, 1980 to December 31, 1999, suggesting that the positive basis has a greater impact on the variance and covariance structure than the negative basis. Separating the effect of the positive and negative bases on the time-varying variance-covariance in spot and futures markets provides better descriptions of the joint dynamic behaviors of commodity prices and plays an important role in determining optimal hedging strategies.

Applying the cointegration test approach and an error correction model, Zhang and Wei (2010) tested the relation between the crude oil and gold markets from January 2000 to March 2008, and their results suggested that there were trends between the two markets with significant positive correlation coefficient of 0.929 (see also Aruga and Managi, 2011). Chan et al. (2011) used a Markov switching model to measure the level of interdependence across financial assets, commodities and real estate assets using monthly data from January 1987 to December 2008. Consistent with the results of earlier research, the following two distinct regimes were detected: a ‘tranquil’ regime, which is characterized by low volatility and significantly positive stock returns, and a ‘crisis’ regime, which is characterized by high volatility and sharply negative stock returns, coupled with evidence of contagion between stocks, oil and real estate. Using Bayesian Markov Chain Monte Carlo methods and weekly crude oil, corn, and wheat futures prices from November 1998 to January 2009, Du et al. (2011) tested the factors that have a potential influence on the volatility of

- 2 They used financial, industrial, consumer, services, health care, and technology.
- 3 The futures contracts are the CBOT corn (CN) and soybeans contracts (SOY); the NYBOT cotton (CT) and coffee (COF) contracts; the CME frozen pork bellies (PB) and lean hog (LH) contracts; and the NYMEX heating oil (HO), light sweet crude oil (CL), Copper (CP), and Silver (SIL) contracts.

crude oil prices and the relationship between this volatility and agricultural commodity markets. They found evidence of a volatility spillover among crude oil, corn, and wheat markets after the fall of 2006. The obtained results were explained by the tightened interdependence between crude oil and these commodity markets that was induced by ethanol production. Serra (2011) used a semiparametric GARCH approach to test the volatility transmission between crude oil, ethanol, and sugar prices in Brazil from July 2000 to November 2009. The author provides evidence for strong volatility dependences between the markets in the study. Further, Serra et al. (2011) find that agricultural commodity prices (corn, cotton, and soybeans, but not wheat) are linked to energy prices.

Recently, Vivian and Wohar (2012) investigated the existence of structural breaks in commodity spot return volatility using an iterative cumulative sum of squares procedure and a GARCH model of a broad cross-section of 28 different commodities from January 1985 to July

- 2010. The empirical results showed high commodity volatility persistence for many commodity returns, even after structural breaks. Arouri et al. (2012) tested the volatility spillovers between oil and sector stock prices in Europe from January 1998 to December 2009 using a VAR-GARCH model and found that there were significant volatility spillovers between oil prices and sector stock returns.

On the other hand, Kumar et al. (2012) argued that the variation in the indices of clean energy stocks is explained by past movements in oil prices, the stock prices of high technology firms and interest rates. More recently, Awartani and Maghyereh (2013) investigate return and volatility spillover effects between oil and equities in the Gulf Cooperation Council Countries during the period from 2004 to 2012. Information flow from oil returns and volatilities to the Gulf Cooperation Council stock exchanges is found to be important. They show these trends were more pronounced in the aftermath of the Global Financial Crisis in 2008 as the net contribution of oil that has intensified after a burst during the crisis. Ewing and Malik (2013) employed univariate and bivariate GARCH models to analyze the volatility spillovers between gold and oil futures incorporating structural breaks using daily returns from July 1, 1993 to June 30, 2010. The authors supported strong evidence of significant transmission of volatility between gold and oil returns when structural breaks in variance are accounted for in the model.

As mentioned above, the relationship between oil and commodity prices is complicated and suggests the need to take stock, energy, metal and agricultural markets integration into account. Moreover, the literature on stock and commodity market linkages shows that price transmission between stock and commodity prices is extensively examined using different econometric techniques. It is now well known that stock and commodity markets are recently characterized by more volatile dynamics that call for deeper analyses of volatility spillover between these markets.

- 3. Econometric methodology

According to the empirical literature, the information flow across markets through returns (correlation in the first moment) may not be significant and visible; however, it may a have high volatility effect (correlation in the second moment). Volatility has been considered a better proxy of information by Clark (1973), Tauchen and Pitts (1983) and Ross (1983). The ARCH model, which was developed by Engle (1982) and later generalized by Bollerslev (1986), is one of the most popular methods for modeling the volatility of high-frequency financial time series data. Multivariate GARCH models with dynamic covariances and conditional correlation, such as the BEKK parameterization (Baba, Engle, Kraft, and Kroner), CCC (constant conditional correlation) or DCC (dynamic conditional correlation) models, have been shown to be more useful in studying volatility spillover mechanisms than univariate models. The estimation procedure in univariate models becomes extremely difficult, especially in cases with a large number of variables, due to the rapid proliferation of parameters to be estimated (see McALeer, 2005 for more details). Furthermore, these models do not allow for a cross-market volatility spillover effect, which is likely to occur with increasing market integration.

Given the failures of the MGARCH model, the VAR-GARCH model was chosen to allow for a focus on the interdependence of the conditional returns, conditional volatility and conditional correlations between the S&P 500 and different commodity markets. VAR(k)-GARCH(p,q) was proposed by Ling and McALeer (2003) and later applied by several researchers, such as Chan et al. (2005), Hammoudeh et al. (2009) and Arouri et al. (2011). This model includes the multivariate CCC-GARCH of Bollerslev (1990) as a special case in which correlations between system shocks are assumed to be constant to ease the estimation and inference procedure.4 This method enables an investigation of the conditional volatility and conditional correlation cross effects with meaningful estimated parameters and less computational complications relative to the other methods. In this research, the bivariate VAR(1)-GARCH(1,1) model5 was used to explore the joint evolution of conditional returns, volatility and correlations among the S&P 500 and commodity markets. The stock market shock is represented by the S&P 500 index returns, while the commodity shocks are represented by the return indices of the commodity markets.

The conditional mean equation of the VAR(1)-GARCH(1, 1) system is given by:

[Figure 2]

(1)

- 4 See, among others, Engle (2002) and McAleer et al. (2008) for more information.
- 5 The optimal number of lags for the bivariate VAR-GARCH model was chosen on the basis of BIC and AIC information criterion.

where

= ’, in which and are the commodity return and S&P 500 return indexes at time t, respectively.

[Figure 3]

[Figure 4]

[Figure 5]

[Figure 6]

’, where and are the residual of the mean equations for the commodities and S&P 500 return indexes, respectively.

[Figure 7]

[Figure 8]

[Figure 9]

’ refers to the innovation and is an i.i.d. distributed random vector.

[Figure 10]

[Figure 11]

[Figure 12]

[Figure 13]

, where and are the conditional variances of

[Figure 14]

[Figure 15]

and , respectively, given by

[Figure 16]

- (2)

[Figure 17]

- (3)

Eqs. (2) and (3) show how volatility is transmitted over time across the S&P 500 and commodity indexes. The cross value of the error terms and represents the return innovations in the S&P 500 index across the corresponding commodity markets at time

[Figure 18]

[Figure 19]

[Figure 20]

and represents short run persistence (or the ARCH effect of past shocks), which captures the impact of the direct effects of shock transmission. The presence of and captures the volatility spillovers or interdependencies between commodity markets and the stock exchanges. It is the contribution to the long-run persistence (or the GARCH effects of past volatilities). The above specification allows for the cross-sectional correlation of conditional volatility between the S&P 500 and commodity markets. The past shock and volatility of one market’s indices are allowed to impact the future volatilities of other markets in addition to its own future volatility.

[Figure 21]

[Figure 22]

The conditional covariance between the S&P 500 returns and commodity index returns is as follows:

[Figure 23]

(4)

[Figure 24]

where is the constant conditional correlation. To examine the return and volatility spillover mechanism across the considered markets, the quasi-maximum likelihood (QML) method6 was employed to estimate the parameters of the VAR(1)-GARCH(1, 1) model.

## 4. Empirical results and discussion

- 4.1. Data and descriptive statistics

We consider daily close returns from January 3, 2000 to December 31, 2011. In this analysis, we used the S&P 500, beverage price, wheat price, gold price indexes and two crude oil benchmarks: Cushing West Texas Intermediate (WTI), the reference crude oil for the USA, and Europe Brent, the reference crude oil for the North Sea. The data were collected from the US Energy Information Administration, International Grains Council, and S&P 500 websites. The period of time we chose to study allows us to investigate the sensitivity of commodity market returns to the following major effects: the terrorist attacks of September 11, 2001, the Gulf War, which was initiated on March 20, 2003, and the recent US subprime mortgage crisis of 2007-2008.

The continuously compounded daily returns are computed using the following logarithmic filter:

[Figure 25]

(5)

[Figure 26]

[Figure 27]

[Figure 28]

### where and denote the daily return in percentage and the closing price of index on day t, respectively.

- 6 See Ling and McAleer (2003) for the estimation procedure of the VAR-GARCH model.

1,600

1,400

1,200

1,000

800

600

400

200

| | |
|---|---|
| | |

| | |
|---|---|
| | |

| | |
|---|---|
| | |

0

00 01 02 03 04 05 06 07 08 09 10 11

|WHEAT BRENT BEVERAGE<br><br>GOLD S&P500 WTI<br><br>|
|---|

Fig. 1. Time variations in the daily S&P 500 and commodity price indices.

- Fig. 1 depicts the daily movements in the S&P 500 and commodity price indexes from January

2000 to December 2011. The figure clearly shows that the price indices vary over time. Moreover, there have been increases in the correlation between equity and commodity prices. However, the past decade was characterized by large fluctuations in commodity prices. First, the figure indicates that the Brent and WTI price indexes behaved in a similar manner. Behaviors of indexes are affected by major events, such as the subprime mortgage crisis. The increase in commodity prices was followed by a steep decline during the financial crisis in the second semester of 2008. Volatility rose sharply during the fall in commodity prices during 2008. Since the first quarter of 2009, the prices of all of the indexes have increased.

The descriptive statistics for all of the daily return series are reported in Table 1. The data suggest that the gold commodity index offers the highest average daily return over the sample period (0.065%). However, this commodity index also has the highest risk, as approximated by a standard deviation of 2.78%, followed by the WTI index (2.61%). The skewness value is both positive and negative. The positively skewed returns are found in the GOLD and BEVERAGE commodity prices, while the negatively skewed returns are found in the S&P 500, WHEAT, BRENT and WTI indexes. Thus, there is a higher probability for the investor to see positive returns from the GOLD and BEVERAGE commodity indices rather than negative returns. Furthermore, the kurtosis values of the index returns are over three times the value of the normal distribution, indicating that the return indices have peaks relative to the normal distribution. All of the indices

also exhibit significant departures from the normal distribution when submitted to the Jarque-Bera test. We also applied the Ljung-Box test and found significant autocorrelations in all of the cases (with the exception of Gold index).

- Table 1 Descriptive statistics for each daily return series

S&P 500 WTI BRENT GOLD WHEAT BEVERAGE Mean (%) -0.0484 0.0449 0.0494 0.0657 0.0337 0.0336 Median (%) 0.0005 0.0013 0.0009 -0.0002 0.0000 0.0002 Maximum (%) 10.9572 16.4137 18.1297 24.2534 7.5315 12.9971 Minimum (%) -9.4695 -17.0918 -19.8906 -17.8195 -8.1283 -10.6038 S.D (%) 1.39 2.61 2.41 2.78 1.61 1.48 Skewness -0.1524 -0.2593 -0.2772 0.2121 -0.0037 0.0720 Kurtosis 10.0330 7.2776 8.1776 8.3934 5.1102 10.675 Jarque-Bera 6231.78 2327.87 3445.89 3680.59 578.91 7410.10 P-value 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 Q(14) 66.41

(0.001)

47.25 (0.001)

38.78 (0.001)

13.80 (0.456)

43.39 (0.000)

37.96 (0.000)

Notes: Q (14) is the Ljung-Box statistic for serial correlation. The p-values of the Q-statistic are given in parenthesis.

A stationary process of the return series is tested using the ADF and PP unit root tests. The results of these tests are shown in panel A of Table 2. The null hypothesis was rejected, indicating that the return series was a stationary process. Panel B of Table 1 indicates the presence of the ARCH effects and therefore estimation of a GARCH model is appropriate.

- Table 2 Unit root tests, ARCH-LM test, and unconditional correlations.

S&P 500 WTI BRENT GOLD WHEAT BEVERAGE

- Panel A: Unit root tests ADF I(0) -42.89*** -54.72*** -53.42*** -54.69*** -52.23*** -40.79*** PP -58.98*** -54.94*** -53.42*** -55.08*** -52.24*** -54.57***

- Panel B: ARCH-LM test F-statistic 275.8*** 98.17*** 20.81*** 73.18** 77.12*** 166.12*** LM-statistic 463.1*** 183.9*** 39.47*** 170.8** 147.63*** 299.80***

- Panel C: Unconditional correlations S&P 500 1 0.001 0.022 0.002 0.023 -0.038

Notes: The 1% critical values are -3.432 and -3.961 for the ADF and PP tests, respectively. ** and *** denotes statistical significance at the 5% and 1% level, respectively.

Panel C reports the correlation values between the daily returns for the commodity markets and the S&P 500 index. First, all of the correlations are low, ranging from -0.038 to 0.023. The highest correlation is between the S&P 500 and the WHEAT price index. Second, the correlation between the S&P 500 and the beverage commodity index is negative, illustrating the benefits of diversification in the short run. A portfolio that includes stocks from the beverage commodity index will have a lower variance.

- 4.2. Return and volatility dependencies

Using the six indexes under investigation, we estimate five bivariate VAR(1)-GARCH(1,1) systems, each containing daily S&P 500 returns and daily returns on the commodity indices. The estimation results of the VAR(1)-GARCH(1, 1) model are reported in Table 4. The symbols

[Figure 29]

[Figure 30]

and denote the conditional variances for the S&P 500 and commodity markets at time , respectively. The error terms and represent the effect of “news” (unexpected shocks) on the S&P 500 and commodity markets, respectively, at time .

[Figure 31]

[Figure 32]

[Figure 33]

[Figure 34]

In Table 4, regarding the return-generating process, the one period lagged values of the commodity return indexes are largely determined by their current values at different levels. This influence suggests that past returns can be used to forecast future returns in these markets, indicating short-term predictability in commodity price changes. For the S&P 500 index, the past returns influence the current return. In terms of the information transmission through returns, the WTI, BRENT, GOLD and WHEAT returns are affected by the S&P 500 returns. However, the coefficient of one day of past returns of the S&P 500 is significant for these markets. The effect of the S&P 500 on these markets is positive. The highest market’s reaction to the S&P 500 price change is observed in GOLD, followed by WTI and WHEAT, with estimated coefficients of 0.1610, 0.123 and 0.0981, respectively. While the BEVERAGE and BRENT returns are significantly affected by past S&P 500 returns, the effect of the S&P 500 on the Brent and Beverage indexes is weak, with estimated coefficients of 0.0057 and 0.0043, respectively, and significance at the 10% level. This result indicates that information flows from the S&P 500 to commodity markets. Inversely, the effects of the commodity market returns on the S&P 500 returns are significant in all of the cases. The analysis indicates that the oil, Gold and Wheat returns are more related and influenced by the S&P 500 return index.

Turning to the conditional variance equations, the estimated results of the ARCH and GARCH coefficients are significant at conventional levels in all of the markets. Sensitivity to their past

[Figure 35]

conditional volatility ( ) appears to be significant for the commodity indexes. The WHEAT index is the most volatile (0.954), followed by the BRENT (0.921), BEVERAGE (0.919) and GOLD (0.909) indexes, while the WTI index at the tail end of the volatility ranking (0.84). This finding suggests that former conditional volatility values of these markets can be employed to forecast future volatility, and a GARCH(1, 1) model is adequate for capturing any persistence in the commodity markets’ volatility. Alternately, the current conditional volatility of the commodity indices also depends on past shocks or news affecting return dynamics because is significant for all markets. is much smaller for each market than , the commodity market’s volatility, suggesting that a commodity market’s former volatilities are more important in predicting future volatility than past shocks. Fig. 2 showed these properties by plotting the variations in the conditional variance over time for the S&P 500 and commodity indices over the study period.

[Figure 36]

[Figure 37]

[Figure 38]

Consider the volatility spillover effect between the S&P 500 and commodity markets. The results show that past S&P 500 shocks have significant effects on stock market volatility in the GOLD, WTI and BEVERAGE volatilities, with estimated coefficients of 0.069, 0.036 and 0.023, respectively. Past S&P 500 volatility affects market volatility in the WTI, BRENT, GOLD and BEVERAGE volatilities, with estimated coefficients of 0.067, 0.027, 0.058 and 0.0096, respectively. The analysis of volatility interdependence shows significant volatility spillovers between oil and stock markets. These spillovers have substantially increased during the crisis period under the effects of important financial instability and economic uncertainties (Arouri et al.,

- 2011). Our results are in line with the findings of some studies such as Malik and Hammoudeh

(2007), Park and Ratti (2008), Arouri and Christophe (2011), Arouri et al. (2011) Mohanty et al. (2011), and Silvennoinen and Thorp (2013). However, the obtained result contradicts Hammoudeh and Choi (2006)’s study, which found that changes in oil prices have no significant impact on equity indices. In contrast, we found that the past S&P 500 shocks have no effect on the BRENT or WHEAT volatility. Our empirical results support the notion of significant volatility spillover across equity and commodity markets. Similar to the result regarding return interdependency, volatility transmission takes place from the S&P 500 to commodity markets, where the GOLD and WTI markets are mostly affected by the S&P 500 index.

As shown in Table 4, the estimates for constant conditional correlations (CCC) between the stock exchange and commodity market indexes are all positive. However, the estimates demonstrate that the highest CCC is between the S&P 500 and GOLD, WTI, and WHEAT, with estimate coefficients of 0.081, 0.361, and 0.213, respectively, suggesting more mutual responses in the economic factors between these markets than other markets. In contrast, the CCC estimates between the S&P 500 and BRENT and between the S&P 500 and BEVERAGE are small, with

values of 0.011 and 0.0016, respectively, suggesting that there are potential gains from investing in the S&P 500 and these markets.

- 0
- 1
- 2
- 3
- 4
- 5

8

| |BEVERAGE|
|---|---|
| | |

| |BRENT|
|---|---|
| | |

6

4

2

0

00 01 02 03 04 05 06 07 08 09 10

00 01 02 03 04 05 06 07 08 09 10

2.5

15.0

| |WHEAT|
|---|---|
| | |

| |GOLD|
|---|---|
| | |

12.5

2.0

10.0

1.5

7.5

1.0

5.0

0.5

2.5

0.0

0.0

00 01 02 03 04 05 06 07 08 09 10

00 01 02 03 04 05 06 07 08 09 10

- 0
- 1
- 2
- 3
- 4
- 5

10

| |S&P500|
|---|---|
| | |

| |WTI|
|---|---|
| | |

8

6

4

2

0

00 01 02 03 04 05 06 07 08 09 10

00 01 02 03 04 05 06 07 08 09 10

- Fig. 2. Time-variations in the conditional variance for the S&P 500 and commodity indices.

- Table 4 Estimates of the bivariate VAR(1)-GARCH(1, 1) model for the S&P 500 and commodity indices. Variables WTI BRENT GOLD WHEAT BEVERAGE

S&P 500 COM S&P 500 COM S&P 500 COM S&P 500 COM S&P 500 COM

Mean equation S&P 500(1) -0.112***

(0.054)

COM(1) 0.0715** (0.0342)

0.123*** (0.052)

0.0794** (0.047)

0.0045** (0.028)

-0.00016 (0.0195)

0.00577* (0.0014)

-0.1172** (0.0403)

-0.0334* (0.024)

0.0236** (0.021)

0.168*** (0.019)

-0.0524** (0.0478)

0.0013** (0.0091)

-0.0297 (0.0313)

0.0981** (0.011)

0.04550* (0.0410)

0.0201** (0.025)

0.0128 (0.054)

0.00431* (0.052)

-0.1537** (0.0517)

Variance equation C 0.0007

[Figure 39]

[Figure 40]

[Figure 41]

[Figure 42]

(0.0345)

0.078*** (0.0078)

0.0018* (0.0011)

0.9102*** (0.0085)

0.0022** (0.0010)

0.0614** (0.00342)

0.0369* (0.0237)

0.0882 (0.0094)

0.0677*** (0.025)

0.842*** (0.0190)

0.0025*** (0.00069)

0.0809** (0.00078)

0.00227** (0.00093)

0.919*** (0.00093)

-0.00027 (0.00076)

0.0166 (0.00408)

0.00067 (0.0143)

0.0553** (0.00512)

0.027*** (0.00072)

0.921*** (0.00789)

0.000895 (0.0104)

0.0803*** (0.00812)

-0.0013 (0.00692)

0.9072*** (0.00876)

0.00236** (0.001154)

0.0320*** (0.0066)

0.0696*** (0.0226)

0.0526*** (0.00692)

0.0587*** (0.0166)

0.9092*** (0.01150)

0.0016*** (0.00063)

0.0779*** (0.00077)

0.0015 (0.00236)

0.9138*** (0.00821)

0.00181* (0.00136)

0.0023*** (0.00075)

0.000450 (0.00374)

0.0406*** (0.00469)

0.0013 (0.00148)

0.9540*** (0.00509)

0.0020*** (0.00049)

0.0807** (0.00907)

0.0027 (0.00365)

0.891*** (0.0113)

0.0149*** (0.0037)

0.0033** (0.00038)

0.0232*** (0.0033)

0.0622*** (0.0054)

0.0096** (0.0037)

0.919*** (0.00605)

CCC between S&P 500 and commodities indices

0.0361*** (0.00375)

0.0114*** (0.00213)

0.0812*** (0.00195)

0.0213*** (0.00256)

0.0016*** (0.00031)

Log-likelihood -1197.24 -1377.80 -1107.27 -1106.37 -920.164 AIC 4.020 4.623 3.721 3.717 3.095 H-Q 4.072 4.675 3.771 3.768 3.147

###### Note. The bivariate VAR(1)-GARCH(1,1) model is estimated for each country from January 3, 2000 to December 27, 2011. The optimal lag order for the VAR model is selected using the AIC and SIC information criteria. *, **, and *** denote significance levels of 10%, 5% and 1%, respectively. The standard errors are given in parentheses.

## 5. Implications for Portfolio Designs and Hedging Strategies

Building an optimal portfolio by making risk management decisions and portfolio allocation decisions requires a preliminary, accurate estimation of the temporal covariance matrix. To understand the importance of the covariance matrix regarding these financial decisions, we provide two examples using the estimates of our bivariate VAR(1)-GARCH(1,1) models for portfolio design and hedging strategies.

- 5.1. Portfolio weights

In the first example, we follow the diligence outlined by Kroner and Ng (1998), which considers a portfolio that minimizes risk without lowering expected returns. Given the context of frequent fluctuations in commodity indexes and substantial volatility spillovers between the S&P 500 and commodity indexes, we suppose that an investor is holding a set of stocks in the S&P 500 index and wishes to hedge his stock position against unfavorable effects from commodity price fluctuations. The portfolio weight of the holdings of commodity indices /S&P 500 index is given by:

[Figure 43]

- (6)

[Figure 44]

- (7)

[Figure 45]

where is the weight of commodities in one dollar of two assets (commodities, the S&P 500) at time t and the term shows the conditional covariance between the commodities and S&P 500 indexes at time t. The weight of the S&P 500 index in the considered portfolio is . The summary statistics for the portfolio weight computed from the VAR(1)-GARCH(1, 1) models are reported in Table 5. The data show that the average weight for the WTI/S&P 500 portfolio is 0.23, indicating that for a $1 portfolio, 23 cents should be invested in the WTI index, and 77 cents should be invested in the S&P 500 index. The average weight for the BRENT/S&P 500 portfolio indicates that 43 cents should be invested in BRENT, and 57 cents should be invested in the S&P 500. The average weight for the WHEAT/S&P 500 portfolio is 0.25, indicating that for a $1 portfolio, 25 cents should be invested in the WHEAT index, and 75 cents should be invested in the S&P 500 index. The average weight for the BEVERAGE/S&P 500 portfolio indicates that 47 cents should be invested in the BEVERAGE index, and 53 cents should be invested in the S&P 500 index. This result shows how VAR-GARCH models could be used by participants in the financial market for making optimal portfolio allocation decisions.

[Figure 46]

[Figure 47]

- 5.2. Hedge ratios

For a second example, we follow Kroner and Sultan (1993) regarding risk-minimizing hedge ratios and consider a portfolio of two assets (commodities and S&P 500). To minimize the risk of a portfolio that is $1 long in first assets (commodities), the investor should short $ of the second asset (S&P 500). The risk minimizing hedge ratio is given as:

[Figure 48]

[Figure 49]

(8)

[Figure 50]

where is the conditional covariance between the commodity and S&P 500 indices and is the conditional variance for the S&P 500 index at time t. As shown in Table 5, the hedge ratios are typically low, suggesting that hedging effectiveness involving commodity and stock markets is quite good, which is consistent with the view that the inclusion of commodities in a diversified portfolio of stocks increases the risk-adjusted performance of the resulting portfolio. This result confirms the findings obtained by Arouri et al. 2011 and Hassan and Malik, 2007.

[Figure 51]

- Table 5 Summary statistics for the portfolio weights and hedge ratio

[Figure 52]

[Figure 53]

WTI/S&P 500 0.230 0.167 BRENT/S&P 500 0.431 0.203 GOLD/S&P 500 0.200 0.134 WHEAT/S&P 500 0.250 0.103 BEVERAGE/S&P 500 0.470 0.116

The values of the hedge ratio between the commodity and S&P 500 indices range from 0.10 in the WHEAT/S&P 500 portfolio to 0.20 in the BRENT/S&P 500 portfolio. These results are important in establishing that a $1 long position in WTI (Brent) can be hedged for 16 (20) cents with a short position in the S&P 500 index. For the GOLD index, a $1 long position can be hedged for 13 cents with a short position in the S&P 500 index, while a $1 long position in WHEAT can be hedged for 10 cents with a short position in the S&P 500 index. Finally, for the BEVERAGE index, a $1 long position can be hedged for 11 cents with a short position in the S&P 500 index. We can conclude that the cheapest hedge is long WHEAT and short S&P 500, whereas long BRENT and short S&P 500 represent the most expensive hedge.

- 6. Conclusions

Confusion regarding volatility spillovers is a matter of great concern for economists, and further explanation is required, particularly across financial and commodity markets, the participants of which hold a significant interest in the matter. Analyzing the volatility and correlations that exist between metal, crude oil, agricultural and stock exchanges can provide useful information for investors, traders and government agencies who are concerned with the commodity and stock markets, particularly with optimal hedging across these markets. This paper investigated the correlation and transmission of volatility between equity and commodity markets. Daily returns from January 3, 2000 to December 31, 2011 of the Brent, WTI, Wheat, Gold, and Beverage spot prices and the S&P 500 stock index returns were analyzed using the VAR-GARCH model.

Nevertheless, the empirical results of the volatility spillover mechanism between the markets analyzed in this study showed significant correlation and volatility transmission across commodity and equity markets. Our findings corroborate previous studies showing significant volatility spillovers between oil price and equity markets, such as Arouri et al. (2011), Arouri et al. (2012), and Hassan and Malik (2007). We also examined the optimal weights and hedge ratios for commodity-stock portfolio holdings. The results showed the importance of adding commodities to a stock-diversified portfolio, improving its overall risk-adjusted return performance.

Our results are crucial for financial market participants and portfolio managers in particular for building an optimal portfolio and forecasting future stock return volatility. This research can be extended to exchange markets or used to analyze the transmission of volatility among spot, forward and futures markets.

## Acknowledgments

The authors would like to acknowledge the International Grains Council for supporting the work presented in this paper. We would like to show our sincere gratitude to two anonymous reviewers for their helpful suggestions and comments which greatly improve the quality of this paper.

## References

Arouri, M., Jouini, J., Nguyen, D.K., 2012. On the impacts of oil price fluctuations on European equity markets: Volatility spillover and hedging effectiveness. Energy Economics 34, 611−617.

Arouri, M., Lahiani, A., Nguyen, D.K., 2011. Return and volatility transmission between world oil prices and stock markets of the GCC countries. Economic Modelling 28, 1815–1825.

Aruga, K., Managi, S., 2011. Tests on price linkage between the U.S. and Japanese gold and silver futures markets, Economics Bulletin, 31(2), 1038-1046.

Awartani, B., Maghyereh, A.I., 2013. Dynamic spillovers between oil and stock markets in the Gulf Cooperation Council Countries. Energy Economics 36, 28–42.

Bollerslev, T., 1986. Generalized Autoregressive Conditional Heteroskedasticity. Journal of Econometrics 31, 307-327.

Bollerslev, T., 1990. Modelling the coherence in short-run nominal exchange rates: A multivariate generalized ARCH approach. Review of Economics and Statistics 72, 498−505.

Chan, K.F., Karuna, S.T., Brooks, R., Gray, S., 2011. Asset market linkages: Evidence from financial, commodity and real estate assets. Journal of Banking & Finance 35, 1415−1426.

Chan, F., Lim, C., McAleer, M., 2005. Modelling multivariate international tourism demand and volatility. Tourism Management, 26, 459−471.

Clark, P.K., 1973. A Subordinated stochastic process model with finite variances for speculative prices. Econometrica 41, 135−155.

Du, X., Yu, C.L., Hayes, D.J., 2011. Speculation and volatility spillover in the crude oil and agricultural commodity markets: A Bayesian analysis. Energy Economics 33, 497−503.

Engle, R.F., 1982. Autoregressive Conditional Heteroscedasticity with estimates of the variance of United Kingdom inflation. Econometrica 50, 987–1007.

Engle, R.F., 2002. Dynamic conditional correlation: A simple class of multivariate generalized autoregressive conditional heteroskedasticity models. Journal of Business and Economic Statistics 20, 339350.

Ewing, B.T., Forbes, S.M., Payne, J.E., 2003. The effects of macroeconomic shocks on sector-specific returns. Applied Economics 35, 201−207.

Ewing, B.T., Malik, F., 2013. Volatility transmission between gold and oil futures under structural breaks. International Review of Economics and Finance 25, 113–121.

Fornari, F., Monticelli, C., Pericoli, M., Tivegna, M., 2002. The impact of news on the exchange rate of the lir and long-term interest rates. Economic Modelling 19, 2655−2673.

Hammoudeh, S., Choi, K., 2006. Behavior of GCC stock markets and impacts of US oil and financial markets. Research in International Business and Finance 20, 22–44.

Hammoudeh, S., Yuan, Y., McAleer, M., 2009. Shock and volatility spillovers among equity sectors of the Gulf Arab stock Markets. Quarterly Review of Economics and Finance 49, 829-842

Hassan, S.A., Malik, F., 2007. Multivariate GARCH modeling of sector volatility transmission. The Quarterly Review Economics and Finance 47, 470−480.

He, L., Chen, S., 2011. Nonlinear bivariate dependency of price–volume relationships in agricultural commodity futures markets: A perspective from Multifractal Detrended Cross-Correlation Analysis. Physica A 390, 297−308.

Jarque, C.M., Bera, A.K., 1980. Efficient tests for normality, homoscedasticity and serial independence of regression residuals. Economics Letters 6, 255–259.

Kroner, K.F., Ng, V.K., 1998. Modeling asymmetric movements of asset prices. Review of Financial Studies 11, 844–871.

Kroner, K.F., Sultan, J., 1993. Time dynamic varying distributions and dynamic hedging with foreign currency futures. Journal of Financial and Quantitative Analysis 28, 535–551.

Kumar, S., Managi, S., Matsuda, A., 2012. Stock prices of clean energy firms, oil and carbon markets: A vector autoregressive analysis. Energy Economics 34, 215−226.

Leeves, G., 2007. Asymmetric volatility of stock returns during the Asian crisis: Evidence from Indonesia. International Review of Economics and Finance 16, 272−286.

Lien, D., Yang, L., 2008. Asymmetric effect of basis on dynamic futures hedging:Empirical evidence from commodity markets. Journal of Banking & Finance 32, 187−198.

Ling, S., McAleer, M., 2003. Asymptotic theory for a vector ARMA-GARCH model. Econometric Theory 19, 278−308.

Ljung, G.M., Box, G.E.P., 1978. On a Measure of a Lack of Fit in Time Series Models. Biometrika 65, 297–303.

Maghyereh, A., Al-Kandari, A., 2007. Oil prices and stock markets in GCC countries: new evidence from nonlinear cointegration analysis. Managerial Finance 33, 449–460.

Malik, F., Ewing, B.T., 2009. Volatility transmission between oil prices and equity sector returns. International Review of Financial Analysis 18, 95−100.

Malik, F., Hammoudeh, S., 2007. Shock and volatility transmission in the oil, US and Gulf equity markets. International Review of Economics and Finance 16, 357−368.

McAleer, M., 2005. Automated inference and learning in modeling financial volatility. Econometric Theory 21, 232−261.

McAleer. M., Chan, F., Hoti, S., Lieberman, O., 2008. Generalized autoregressive conditional correlation. Econometric Theory, 26, 1554−1583.

Mohanty, S., Nandh, M., Turkistani, A.Q., Alaitani, M.Y., 2011. Oil price movements and stock market returns: Evidence from Gulf Cooperation Council (GCC) countries. Global Finance Journal 22, 42–55.

Ozdemir, Z.A., 2009. Linkages between international stock markets: A multivariate long-memory approach. Physica A 388, 2461−2468.

Park, J., Ratti, R.A., 2008. Oil price shocks and stock markets in the US and 13 European countries. Energy Economics 30, 2587–2608.

Ross, S.A., 1983. Information and volatility: The no-arbitrage martingale approach to timing and resolution irrelevancy. Journal of Finance 45, 1−17.

Sadorsky, P., 2012. Correlations and volatility spillovers between oil prices and the stock prices of clean energy and technology companies. Energy Economics 34, 248−255.

Serra, T., 2011. Volatility spillovers between food and energy markets: A semiparametric approach. Energy Economics 33, 1155−1164.

Serra, T., Zilberman, D., Gil, J., Goodwin, B., 2011. Nonlinearities in the U.S. corn–ethanol– oil–gasoline price system. Agricultural Economics 42, 35–45.

Silvennoinen, A., Thorp, S., 2013. Financialization, crisis and commodity correlation dynamics. Journal of International Financial Markets, Institutions & Money 24, 42– 65.

Singh, P., Kumar, B., Pandey, A., 2010. Price and volatility spillovers across North American, European, and Asian stock markets. International Review of Financial Analysis, 19, 55−64.

Syllignakis, M.N., Kouretas, G.P., 2011. Dynamic correlation analysis of financial contagion: Evidence from the Central and Eastern European markets. International Review of Economics and Finance 20, 717−732.

Tauchen, G. E., Pitts, M., 1983. The price variability−volume relationship on speculative markets. Econometrica 51, 485−505.

Vivian, A., Wohar, M.E., 2012. Commodity volatility breaks. Journal of International Financial Markets, Institutions & Money 22, 395−422.

Wang, P., Wang, P., 2010. Price and volatility spillovers between the Greater China Markets and the developed markets of US and Japan. Global Finance Journal 21, 304−317.

Yilmaz, K., 2010. Return and volatility spillovers among the East Asian equity markets. Journal of Asian Economics 21, 304−313.

Yu, L., Wang, S., Lai, K.K., 2008. Forecasting crude oil price with an EMD-based neural network ensemble learning paradigm. Energy Economics 30, 2623−2635.

Zhang, Y.J., Wei, Y.M., 2010. The crude oil market and the gold market: Evidence for cointegration, causality and price discovery. Resources Policy 35, 168−177.

