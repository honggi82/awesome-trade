# Return and volatility transmission between world oil prices and stock markets of the GCC countries

Mohamed El Hedi Arouri LEO, University of Orléans & EDHEC Business School Rue de Blois - BP 6739, 45067 Orléans Cedex 2, France Email: mohamed.arouri@univ-orleans.fr │ Phone: +33.2.38.49.24.10 │ Fax: +33.2.38.41.73.80

Amine Lahiani LEO, University of Orléans and ESC Rennes Business School Rue de Blois - BP 6739, 45067 Orléans Cedex 2, France Email: amine.lahiani@univ-orleans.fr │ Phone: +33.2.38.49.24.10 │ Fax: +33.2.38.41.73.80

Duc Khuong Nguyen* ISC Paris School of Management 22, Boulevard du Fort de Vaux, 75017 Paris Email: dnguyen@groupeisc.com │ Phone: +33.1.40.53.99.99 │ Fax: +33.1.40.53.98.98 *Corresponding author

#### Abstract

This paper investigates the return linkages and volatility transmission between oil and stock markets in the Gulf Cooperation Council (GCC) countries over the recent period 2005-2010. We employ a recent generalized VAR-GARCH approach which allows for transmissions in return and volatility. In addition, we analyze the optimal weights and hedge ratios for oil-stock portfolio holdings. On the whole, our results point to the existence of substantial return and volatility spillovers between world oil prices and GCC stock markets, and appear to be crucial for international portfolio management in the presence of oil price risk.

Keywords: oil and stock markets, optimal hedge ratios, VAR-GARCH models JEL classifications: G12, F3, Q43

- 1. Introduction Dynamic return links and volatility transmission across capital markets are of greater and greater interest to the financial community with the increasing trend of financial globalization throughout the world. If, for example, return and volatility are found to spread from one market to another, portfolio managers and policymakers would have to adjust their actions to essentially prevent contagion risks in the event of market crashes or crises. This issue has been extensively investigated in the context of international asset markets (e.g., Forbes and Rigobon, 2002; Syriopoulos, 2007 for stock markets; Barassi et al., 2005; Wang et al., 2007 for monetary markets; and Skintzi and Refenes, 2006; Johansson, 2008 for bond markets). These studies generally find evidence of significant return and volatility spillovers across markets, and argue that the degree of spillover is highly dependent on economic and financial integration as well as on the coordination of monetary policy.

Expanding this issue to the context of oil and stock markets is also important because empirical results offer insights into building accurate asset pricing models and accurate forecasts of the volatility of both markets. In particular, all investors should know how the value of their portfolios is affected by large variations observed in oil prices over the last decade. Indeed, oil price fell to less than $20 a barrel in December 2001 following the world economic downturns, and then increased to reach more than $130 in June 2008. This continuum and rapid swings in oil prices lead to significant modifications in energy risk management and policies of almost all countries, as oil is used as a pricing benchmark for various financial instruments and plays a crucial role in international asset hedging strategies for a variety of economic agents (e.g., investors holding stocks of oil and oil-related industries, oil producers

and consumers, and so on). These stylized facts also raise the question of how oil price changes and its volatility affect both the economy and financial markets.

Even though a number of works in the literature have studied the interactions between oil prices and stock markets (Jones and Kaul, 1996; Sadorsky, 1999; Ciner, 2001; Basher and Sadorsky, 2006), very little attention is paid to the issue of return and volatility spillovers (Ewing et al., 2002; Malik and Ewing, 2009) and, to the best of our knowledge, no study has been conducted in the context of the Gulf Cooperation Council (GCC) countries. By examining whether oil and GCC stock markets are linked and how their volatility spillovers change through time and across markets over the last turbulent decade, this paper attempts to make up for this neglect. For this purpose, we use a recent multivariate econometric technique, Vector Autoregressive Moving Average - Generalized Autoregressive Conditional Heteroskedasticity (VAR-GARCH), introduced by Ling and McAleer (2003). One of the main advantages of this model is that it allows us to investigate the conditional volatility dynamics of the series as well as the conditional correlation cross effects and volatility transmission between series. It also provides meaningful estimates of the parameters with less computational complication compared to several other multivariate specifications such as the full factor GARCH model (Hammoudeh et al., 2009). Further, we are able to use our findings to compute the optimal weights of an oil-stock portfolio as well as optimal hedge ratios for analyzing hedging effectiveness. Our literature surveys show that the VAR-GARCH model has never been employed to investigate the relationships between oil prices and stock markets.

Using daily data over the period from June 7, 2005 to February 21, 2010 for the six countries members of the GCC, we mainly find evidence of significant return and volatility spillovers between oil and stock markets in the GCC region. The direct

transmission of conditional volatility across markets is, however, more apparent from oil to stock segments. Empirical results from optimal weights and hedge ratios indicate that investors operating in the GCC markets may benefit from adding the oil assets into a well-diversified portfolio of stocks, and that hedging strategies are necessary to manage the oil risk more effectively.

The remaining part of the paper is structured as follows. Section 2 provides a short review of literature about the effects of oil price changes on the real and financial sectors. Section 3 describes the empirical methodology we use to measure shock transmission and volatility spillover effects between oil and GCC stock markets. Section 4 presents the data. Section 5 discusses the empirical results and shows their implications on oil-risk management and portfolio optimization in presence of oil assets. Concluding remarks are summarized in Section 6.

- 2. A short review of literature on the oil volatility effects Previous empirical investigations including, among others, Hamilton (1983), Cunado and Perez de Garcia (2005), and Kilian (2008) have reported that oil price shocks has a causal link on recessions, inflation, economic growth, and other economic variables in most developed and emerging countries, with however different degrees and through different mechanisms. There is also empirical evidence to suggest that economic activity and financial market returns are nonlinearly associated with oil price changes (Hamilton, 2003; Zhang, 2008; Cologni and Manera, 2009).

The strand of research examining the potential relationships between oil price shocks and stock markets has only gained ground very recently, and the focus is es-

sentially on a few net-oil importing developed countries.1 Initially, Jones and Kaul (1996) investigate the reaction of four developed stock markets to oil shocks on the basis of standard cash flow dividend valuation model and find evidence of significant impacts of oil price changes on corporate cash flows in the US and Canada. Their results were not conclusive for Japan and the UK. Subsequently, vector autoregressive models (VAR) are often employed to explore the oil-stock market relationships, but the results obtained are not always consistent across studies (Huang et al., 1996; Sadorsky, 1999). The evidence of asymmetric and nonlinear linkages has been also documented in Sadorsky (1999) and Ciner (2001) respectively. In the context of emerging stock markets, the effect of oil shocks is generally found to be significant over both the short and long run (Papapetrou, 2001; Basher and Sadorsky, 2006; Maghyereh and Al-Kandari, 2007).

However, less attention has been paid to smaller emerging markets, especially in the GCC countries where the links between oil prices and stock markets have important implications for international investments and economic policies. First, since GCC countries are major suppliers of oil in world energy markets, their stock markets are likely to be affected by changes in oil prices. Second, the GCC markets differ from those of developed and from other emerging countries in that they are largely segmented from the international markets and are highly sensitive to regional political events. Finally, the GCC markets represent very promising areas for regional and world portfolio diversification. A good understanding of the influence of oil price shocks on stock markets may really assist investors for making accurate investment decisions and policymakers for regulating stock markets more effectively.

- 1 It should be noted that in theory oil shocks may affect stock prices through their impacts on the macroeconomy and business environment which, in turn, have direct repercussions on firms’ expected future cash-flows. For example, sharp oil price changes, whatever the sign, may reduce aggregate output temporarily because they put back investments due to increasing uncertainties or induce costly resource reallocation (Guo and Kliesen, 2005).

The relationship between oil and stock markets in the GCC countries has been examined by several works. For instance, Hammoudeh and Aleisa (2004) show from VAR models and cointegration tests that there is a bidirectional relationship between Saudi stock returns and oil prices changes. Zarour (2006) employs a VAR analysis to study the oil-stock market links in the GCC countries and find evidence of predictive power of oil price changes on stock market returns in Saudi and Oman. Hammoudeh and Choi (2006) examine the long-run relationship among the GCC stock markets in the presence of the US oil market, the S&P 500 index and the US Treasury bill rate. They report that the T-bill rate has direct impact on these markets, while oil and S&P 500 have indirect effects. The findings of Maghyereh and Al-Kandari (2007) are consistent with the presence of significant nonlinear impacts of oil price changes on stock price indices in the GCC countries over the long-run. In a more recent study, Arouri and Fouquau (2009) focus on the short-run relationships between oil prices and GCC stock markets using a nonparametric method and show some evidence of nonlinearities in Qatar, Oman, and UAE. Indeed, the relationships between oil prices and stock markets in these countries are found to be asymmetric and regimeswitching with respect to the values of oil price changes. Unfortunately, the unknown analytical form of this nonlinear link does not facilitate the use of their results in portfolio management or policy decision-making process.

As noted in the introduction part, the issue of volatility transmission between oil and stock markets has been relatively less explored in the extant literature, two exceptions being Ewing et al. (2002), and Malik and Ewing (2009). Using several univariate and multivariate time-series techniques including the multivariate BEKKGARCH model to examine the volatility transmission between oil and natural gas markets, the first study finds significant direct and indirect transmission of volatility

from the natural gas sector to the oil sector. There is nevertheless only weak evidence of volatility transmission from oil sector to natural gas sector. These findings are typically explained by the differences in the volatility behavior of oil and natural gas sectors, as noted by these authors. The second study, being the most related to ours, employs a bivariate GARCH model to evaluate the volatility transmission between five different US sector indices and oil prices. It provides evidence of significant spillovers of shocks and volatility between oil prices and some of equity sectors.

This present study thus brings insights about the dynamic interdependence of world oil price and GCC stock markets in terms of both returns and conditional volatility by using a VAR-GARCH approach. It further sheds light on the potential gains of cross-market hedging as well as on the sharing of common information by market operators.

- 3. Econometric method As far as volatility modeling of oil and stock markets is concerned, GARCH-type models have received a particular interest from almost all previous papers (e.g., Narayan and Narayan, 2007; Kang et al., 2009; Oberndorfer, 2009; Choi and Hammoudeh, 2010). It is commonly shown that multivariate volatility models such as BEKK (full parameterization), CCC (Constant Conditional Correlation) or DCC (Dynamic Conditional Correlation) models with dynamic covariances and conditional correlations are more relevant than univariate models. These models are however subject to a major drawback that their estimation becomes extremely difficult, especially when the number of variables considered is important owing to the rapid proliferation of parameters to be estimated. Additionally, they do not explicitly allow for crossmarket volatility spillover effects, while the latter are likely to occur with the increas-

ing integration of capital markets. These reasons lead us to choose the newly developed VAR-GARCH model to explore the joint evolution of conditional returns, volatility and correlations among the oil and stock markets included in the system. Introduced by Ling and McAleer (2003), this approach was applied by, among others, Chan et al. (2005), and Hammoudeh et al. (2009) to tourism demand variations and stock markets, and appears to provide meaningful and interpretable coefficients.

Specifically, the VAR-GARCH model described in Ling and McAleer (2003) includes the multivariate CCC-GARCH model of Bollerslev (1990) as a special case where correlations between system shocks are assumed to be constant to ease the estimation and inference procedure. In this paper, we adopt the bivariate form of this model to investigate the interdependence of oil and stock markets in each country of the GCC. The specification we consider is thus a bivariate VAR(1)-GARCH(1,1) where the conditional mean is given by2

    

 1 



Y Y

t t t





 

D



t t t

where

(1)

 Yt  (rts,rto) with rts and rto being the returns on stock market and oil price indices at time t respectively;







0

  is a (2×2) matrix of coefficients of the form  

 

;

 

1



0

2

 t  (ts,to) with ts and to being the residual terms from the mean equa-

tions of stock market and oil returns respectively;

 t  (ts,to) refers to a (2×1) vector of independently and identically distri-

buted errors;

- 2 The optimal number of lags for the VAR system was chosen on the basis of commonly-used information criteria.

 and Dt  diag( hts , hto ) with hts and hto being the conditional variances of

rt and rot respectively. Their time-series dynamics are modeled in Equations

s

(2) and (3) as:

2

2 1 1

2 1

2

2 1 2

2 1

- 1

hts  Cs2  s hts s (ts )  s hto s (to ) (2)

2 1

2 1 2

2

2

2 1

2 1 1

- 2

2

hto  Co2  o hto o (to )  o hts o (ts ) (3)

1

As it can be seen, the conditional variance of the stock market (resp., oil market) depends not only on its own pasts and innovations, but also on those of the oil market (resp., stock market). This particular feature thus permits the direct transmission of volatility and shocks from one market to another. We can also express the conditional covariance, htso , as follows:

so

- s
- t

o t

ht   h h (4) where  is the conditional constant correlation.3

Taken together, the characteristics of the proposed model allow us to capture both return and volatility spillover effects between oil and stock markets. To the extent that the normality condition is often rejected for the majority of macroeconomic and financial series, we use the quasi-maximum likelihood (QML) method to estimate the model’s parameters.4 In Section 5, we will show how the estimation results from our VAR(1)-GARCH(1,1) model can be used to compute the optimal weights and hedge ratios of an oil-stock diversified portfolio.

- 3 It is worth emphasizing that the model VAR-GARCH with dynamic conditional correlations has not been analysed theoretically yet (McAleer et al., 2009).
- 4 See Ling and McAleer (2003) for further details about the asymptotic properties of the VARGARCH model and its estimation procedure.

- 4. Data and preliminary results Our study examines the return and volatility linkages for the six countries members of the GCC (Bahrain, Kuwait, Oman, Qatar, Saudi Arabia, and UAE) over the period from June 7, 2005 to February 21, 2010.5 Stock market indices are obtained from MSCI database, while world oil price data are extracted from the Energy Information Administration (EIA). Note that the Brent spot prices are used to represent the international crude-oil market since they usually serve as reference prices for pricing crude oil and many other derivatives products using oil as underlying asset. Unlike the majority of previous studies which employ low frequency data (yearly, quarterly, monthly, and weekly), we use daily data in order to adequately capture the rapidity and intensity of the dynamic interactions between oil and stock prices in the GCC region. All price data are denominated in US dollars to avoid the impacts of exchange rates and to ease the comparison across countries. Daily returns are calculated from daily price data by taking the natural logarithm of the ratio of two successive prices. The statistical and stochastic properties of the data are summarized in Table 1.

In Panel A, we test for the presence of unit roots in the levels and first differences of oil and stock market price indices. The results from the Augmented Dickey Fuller (ADF) tests indicate that the price series are integrated of order one or I(1), while the returns series are stationary. We report, in Panel B, basic statistics of log returns series. Average daily returns on GCC stock market indices are all negative over our sample period under the effects of the recent global financial crisis 20072009, sparked by the US subprime crisis. Stock market in Bahrain realized the worst performance (-0.121%), followed by those in the UAE and Saudi Arabia. Inversely, oil market experienced a positive average return, which is not surprising in view of

- 5 The data used in the majority of previous studies predate the end of 2005, and as a result they missed the spectacular variations that have occurred in the GCC and oil markets over the last three years.

the increasing trend in the price of oil over the last decade. Skewness is negative for all stock markets, and positive for oil market. This means that extreme negative and positive returns are likely to realize for stock and oil markets respectively. Kurtosis coefficients are important in size and highly significant, indicating that outliers may occur with a probability higher than that of a normal distribution. Accordingly, the Jarque-Bera test statistics strongly reject the null hypothesis of normality for all series.

- Table 1 Descriptive statistics

Panel A: Augmented Dickey-Fuller (ADF) stationarity tests

Levels First difference Bahrain -2.536** (a) -32.621***(c) Kuwait -1.703 (b) -32.891*** (a) Oman -0.323 (a) -31.399*** (a) Saudi Arabia -0.776 (a) -33.879*** (a) UAE -1.231 (a) -31.186*** (a) Qatar -1.434 (a) -32.689*** (a) Oil -1.916 (c) -35.222*** (a) Panel B: Basic statistics of return series

Saudi Arabia

UAE Qatar Oil

Bahrain Kuwait Oman

Mean (%) -0.121 -0.002 -0.015 -0.043 -0.081 -0.022 0.037 Max. (%) 11.502 8.752 10.750 16.226 18.326 11.258 16.413 Min. (%) -17.983 -14.871 -17.644 -21.570 -15.497 -13.171 -12.826 Std. dev 1.588 1.783 1.634 2.244 2.207 2.008 2.768 Skewness -1.978 -1.249 -1.479 -1.508 -0.754 -0.563 0.104 Kurtosis 27.293 14.262 24.017 18.291 14.499 10.261 7.394 Jarque-Bera 30519*** 6704*** 22692*** 12238*** 6776*** 2707*** 975*** ARCH(20) 64.2*** 40.1*** 76.7*** 39.6*** 35.7** 38.4*** 59.1*** Correlation with Brent oil

0.061 0.018 0.026 0.024 0.10 0.373 -

Notes: ADF test is carried out using log prices and returns series. (a) designates a model with neither constant nor deterministic trend; (b) a model with constant and without deterministic trend; and (c) model with constant and deterministic trend. *, ** and *** denote rejection of the null hypothesis respectively at the 10%, 5% and 1% levels, respectively.

As also shown in Panel B, all the return series were found to have a leptokurtic behavior (i.e., their distributions have fatter tails than corresponding normal distributions). This suggests that each of the mean equations should be tested for the existence of conditional heteroscedasticity. By applying the Engle (1982)’s test, we observe that the null hypothesis of ARCH effects cannot be rejected at conventional le-

vels in all cases, thus confirming that GARCH modeling is adequate for capturing any persistence in the financial volatility of stock and oil markets we consider.

We also compute the unconditional correlations between GCC stock market returns and oil price changes. The results reveal that cross-market correlations are not high, but on average positive. These correlations range from 0.018 (Kuwait-Brent) to 0.373 (Qatar-Brent). This finding indicates that the presence of oil asset in a portfolio may lead to greater diversification benefits.

- 5. Empirical results and portfolio implications In what follows, we will first discuss our findings related to return linkages and volatility transmission between oil and stock markets in the GCC countries within the empirical framework of the VAR(1)-GARCH(1,1) model. Recall that the appropriate lag length for the VAR system was determined by the usual information criteria (BIC and SIC). We will then use the estimation results to compute the optimal weights of an oil-stock portfolio as well as the optimal hedge ratios.

- 5.1 Return and volatility dependencies Our VAR(1)-GARCH(1,1) estimation results are reported in Tables 2-7 for the six oil-stock market pairs. Regarding the interdependence of returns in mean equations, we find that lagged oil price returns significantly affect stock market returns in three out of six cases: Bahrain, Oman, and Qatar. The effect of oil on stock markets is positive for Oman and Qatar, but negative for Bahrain. Inversely, oil returns are only significantly related to stock market returns in Bahrain, but the link is negative. The lagged value of stock market returns is found to be significant in two stock markets (Bahrain and Qatar), indicating that their returns are predicted from past realizations, and thus they are not informationally efficient according to the weak-form efficiency

(Fama, 1991). Taken together, our findings suggest some evidence of predictability in the dynamic variations of stock market returns with respect to previous returns on oil and stock market indices for three GCC countries, Bahrain, Oman and Qatar.

- Table 2 Estimates of VAR(1)-GARCH(1,1) for Bahrain

Variables Bahrain Oil Mean equation

0.7387*** (0.1209) 0.1743** (0.0708) -0.1914*** (0.0432)

0.2989** (0.1212) -0.2359*** (0.0863)

C Bahrain(1) Oil(1)

0.0781* (0.0457) Variance equation

- -0.077 (9.7740)
- -0.0025 (3.3908)
- -0.0373 (0.2574)
- -0.9411*** (0.1179) 0.2772 (0.2907)

0.2979 (0.2326)

C

2 (ts1)

-0.0019 (5.0112) 0.1752*** (0.0404)

2 (to1)

s ht1

0.2830 (0.3308)

0.9567*** (0.0710) Constant conditional correlation

o ht1

Bahrain Oil

1.0000

0.1918*** (0.0557) 1.0000 Log likelihood AIC SIC

-5253.606 8.7697 8.8417

Notes: The optimal lag order for the VAR model is selected using the SIC information criterion. Standard errors are given in parenthesis. *, ** and *** denote rejection of the null hypothesis at the 10%, 5% and 1% levels, respectively.

As for the estimates of ARCH and GARCH coefficients in the conditional variance equations, they are significant at conventional levels in most cases. The sensitivity to past own conditional volatility (GARCH-term) appears to be significant for all countries, except for Qatar. This finding typically suggests that past values of the conditional volatility in a particular stock market can be employed to forecast future volatility. The results also show that the current conditional volatility of GCC stock markets also depends on past shocks affecting return dynamics since ARCH-terms are highly significant for all countries considered, with an exception for Bahrain.

#### Figure 1. Time-variations of conditional volatility for GCC stock markets

[Figure 1]

A closer inspection of the above coefficients reveals that in general conditional volatility does not change very rapidly as the ARCH-terms measuring the impact of past shocks on conditional volatility are relatively small in size. On the other hand, the GARCH-terms, which capture the impact of past volatility on current volatility, are substantially large, indicating gradual fluctuations over time. These properties can be further apprehended through Figure 1 where we plot the time-variations of conditional volatility for the six stock markets under investigation. It should be finally noted that the similar conclusions hold for oil price volatility.

- Table 3 Estimates of VAR-GARCH for Kuwait

Variables Kuwait Oil Mean equation

0.1390** (0.0549)

0.0374 (0.0518) 0.0511 (0.0368)

C Kuwait(1) Oil(1)

- -0.0359 (0.0437)
- -0.0322 (0.0252)

-0.0096 (0.0257)

Variance equation

- -0.0004 (26.2900)
- -0.0881*** (0.0304)
- -0.0144 (0.1989)

C

0.1605 (0.1086)

-0.0925* (0.0557) 0.2033*** (0.0235)

2 (ts1)

2 (to1)

0.9519*** (0.0242) 0.2180*** (0.0682)

0.2576* (0.1502) 0.9538*** (0.0259)

s ht1

o ht1

Constant conditional correlation

Kuwait Oil

1.0000

0.0685** (0.0283) 1.0000 Log likelihood AIC SIC

-4904.386 8.1886 8.2606

Notes: The optimal lag order for the VAR model is selected using the SIC information criterion. Standard errors are given in parenthesis. *, ** and *** denote rejection of the null hypothesis at the 10%, 5% and 1% levels, respectively.

Turning out to the volatility spillover effects between oil and stock markets in the GCC countries, we first observe that there is no direct transmission of volatility from oil market to Bahraini and Qatari stock markets (Tables 2 and 5). For the four remaining countries (Tables 3-4 and 6-7), the cross-volatility coefficients (return innovation and volatility) are significant at conventional levels. More precisely, past oil shocks have significant effects on stock market volatility in Saudi Arabia, while past oil volatility strongly affects stock market volatility in Kuwait, Oman and the UAE. However, the effects of past shocks and past volatility of oil returns on volatility of stock markets in GCC countries should be moderated since their estimated coefficients are much smaller than those of past own shocks and volatilities. Oil price volatility is affected, on the one hand, by past market shocks in Kuwait, and on the other hand by past stock market volatility in Oman and the UAE. Therefore, direct volatility spillover is more widespread from oil to stock markets in the GCC countries than

the inverse case. Investors should then keep a close watch on what is going on in the oil market in order to make accurate investment decisions.

- Table 4 Estimates of VAR-GARCH for Oman

Variables Oman Oil Mean equation

C Oman(1) Oil(1)

0.0021 (0.0809)

0.0700 (0.074) 0.0959*** (0.0348)

0.0522 (0.0830) 0.0104 (0.0687) 0.0067 (0.0358)

Variance equation

C

2 (ts1)

2 (to1)

s ht1

o ht1

0.2360 (0.1450) -0.3730*** (0.0635)

0.0022 (3.0922) 0.9052*** (0.0334) 0.2458*** (0.0784)

0.3226*** (0.0893)

-0.0265 (0.8341) 0.2252*** (0.0317)

0.2350* (0.1346) 0.9551*** (0.0180)

Constant conditional correlation

Bahrain Oil

1.0000

0.3163*** (0.0425) 1.0000 Log likelihood AIC SIC

-4878.672 8.1458 8.2178

Notes: The optimal lag order for the VAR model is selected using the SIC information criterion. Standard errors are given in parenthesis. *, ** and *** denote rejection of the null hypothesis at the 10%, 5% and 1% levels respectively.

- Table 5 Estimates of VAR-GARCH for Qatar

Variables Qatar Oil Mean equation

C Qatar(1) Oil(1)

-0.0529 (0.3190) 0.2127** (0.0913)

0.2257 (0.2425) 0.0930 (0.0789)

0.3115*** (0.0865) Variance equation

0.2006* (0.1141)

2.4520 (7.6177)

C

2.5835 (7.3489) 0.4966*** (0.1585) -0.0447 (1.3988) 0.4950 (0.4584) 0.0662 (360.250)

2 (ts1)

- -0.1189 (0.2522) 0.0088 (6.2466)
- -0.2344 (1.0028) 0.4814 (4.9435)

2 (to1)

s ht1

o ht1

Constant conditional correlation

Qatar Oil

1.0000

0.2804*** (0.0871) 1.0000 Log likelihood AIC SIC

-865.8705 10.4481 10.7630

Notes: The optimal lag order for the VAR model is selected using the SIC information criterion. Standard errors are given in parenthesis. *, ** and *** denote rejection of the null hypothesis at the 10%, 5% and 1% levels, respectively.

#### Table 6 Estimates of VAR-GARCH for Saudi

Variables Saudi Arabia Oil Mean equation

0.1328** (0.0585) -0.0180 (0.0310) -0.0238 (0.0296)

0.0506 (0.0511) -0.0125 (0.0433) 0.0297 (0.0259)

C Saudi(1) Oil(1)

Variance equation

0.1434*** (0.0365) 0.2895*** (0.0163)

-0.3103*** (0.0685) 0.0262 (0.1145) 0.2909*** (0.0213) 0.0004 (8.2154)

C

2 (ts1)

2 (to1)

-0.0894*** (0.0219) 0.9580*** (0.0046) -0.0006 (4.6107)

s ht1

0.9485*** (0.0085) Constant conditional correlation

o ht1

Saudi Oil

1.0000

0.0628** (0.0288) 1.0000 Log likelihood AIC SIC

-5192.234 8.6676 8.6947

Notes: The optimal lag order for the VAR model is selected using the SIC information criterion. Standard errors are given in parenthesis. *, ** and *** denote rejection of the null hypothesis at the 10%, 5% and 1% levels, respectively.

#### Table 7 Estimates of VAR-GARCH for UAE

Variables UAE Oil Mean equation

0.1113* (0.0661) 0.0501 (0.0375) 0.0127 (0.0283)

C UAE(1) Oil(1)

-0.1629 (0.1040) 0.0651 (0.0459) 0.0323 (0.0404)

Variance equation

0.3593*** (0.1123) 0.2057*** (0.0226)

0.2577* (0.1396) 0.0005 (10.8785)

C

2 (ts1)

2 (to1)

0.2193*** (0.0273)

-0.0030 (2.5591) 0.9456*** (0.0230)

s ht1

0.2176** (0.1011) 0.9421*** (0.0238)

0.2548** (0.0992)

o ht1

Constant conditional correlation

UAE Oil

1.0000

0.1155*** (0.0370) 1.0000 Log likelihood AIC SIC

-5292.651 8.8346 8.9067

Notes: The optimal lag order for the VAR model is selected using the SIC information criterion. Standard errors are given in parenthesis. *, ** and *** denote rejection of the null hypothesis at the 10%, 5% and 1% levels, respectively.

As expected, the estimates for constant conditional correlations between oil and stock markets in the GCC countries are all positive. They are small in general,

suggesting the existence of potential gains from investing in both stock markets and oil.

Summarizing all, the empirical VAR(1)-GARCH(1,1) model appears to satisfactorily capture the return linkages and volatility transmission for the six pairs of markets we consider. Stock market returns are significantly influenced by oil returns in three out of six cases, and they only affect oil returns in Bahrain. The analysis of volatility interdependence shows significant volatility spillovers from oil to stock markets, while oil volatility is sensitive to stock market volatility in only two countries.

- 5.2 Portfolio management with oil-risk hedging strategies Our previous findings suggest that potential gains from diversification are substantial by investing in both oil and stock markets. Their return and volatility spillovers require however portfolio managers to quantify the optimal weights and hedging ratios in order to deal adequately with the oil risk. To illustrate this purpose, we now consider a portfolio composed of oil and stocks for which we attempt to minimize the risk without reducing expected returns. According to Kroner and Ng (1998), the optimal weight of holdings of the two assets (oil and the stock market index) is given by:

- s
- t

os t

 

h h w

, 2

os t h h h

o t

os t

- s
- t

 

and,

(5)



 

0, 0

if w w (6)

 

, ,

os t os t

 

, 0 1

w if w

, ,

os t os t





1, 1

if w

,

os t

where wos,t refers to the weight of oil in a one-dollar tow-asset portfolio at time t;

and htos the conditional covariance between oil and stock market returns at time t.

Therefore, the optimal weight of the stock market index in the considered portfolio is

1 wos,t .

- Table 8 Weights and hedge ratios

Bahrain Kuwait Oman Saudi UAE Qatar wos,t 0.6172 0.6534 0.7028 0.5778 0.4686 0.3997 os,t 0.2328 0.0924 0.4289 0.0782 0.1099 0.2430

Notes: The table reports average optimal weights and hedge ratios in an oil-stock market portfolio.

The average values of wso,t (optimal weights) for the six GCC countries are reported in Table 8. They vary from 39.97% for Qatar to 70.28% for Oman. This suggests that for the Qatari case the optimal holding of oil in a one-dollar oil-stock market portfolio should be 39.97%, and the remaining budget of 60.03% is invested in stock market. For the Omani case, these optimal investment weights are 70.28% and 29.72% respectively. Overall, our results point to the fact that except for Qatar and the UAE, investors holding assets in the GCC countries should have more oil than stocks in their portfolios in order to minimize the risk without lowering the expected return.

As for hedge ratios, Kroner and Suktan (1993) consider a portfolio of two assets (oil and market stock index in our case). To minimize the risk of this portfolio, a long position of one dollar in the oil market should be hedged by a short position of t dollars in the stock market index, that is:

os t

h

 ,  (7)

os t h

- s
- t

Table 8 reports average values of the hedge ratios computed by using Equation (7) over the estimation period. As we can see, these ratios are low in general suggesting that hedging effectiveness involving oil and stock markets in the GCC countries

is quite good, as compared to that in other developed markets (e.g., Hassan and Malik, 2007). They range from 0.0782 in Saudi Arabia to 0.4289 in Oman. Accordingly, one dollar long in oil should be shorted by about 8% and 42% of stocks in Saudi Arabia and Oman respectively. Our results are thus consistent with the view that inclusion of oil into a diversified portfolio of stocks increases the risk-adjusted performance of the resulting portfolio.

- 6. Concluding remarks This paper investigates the return informational linkages and volatility transmission between oil and stock markets of the GCC countries over the last turbulent decade. We employ a VAR-GARCH approach which allows for spillover effects in both returns and conditional volatilities. We also analyze the optimal weights and hedge ratios for oil-stock portfolio holdings. Overall, our results point to the existence of significant volatility spillovers between oil and stock markets in three out of six GCC countries, with the volatility transmission being more apparent from oil to stock markets. For these markets, the rise in oil price volatility caused by shocks and policy changes affecting oil supply- and demand-side would directly increase their volatility. They further suggest that adding the oil assets into a well-diversified portfolio of stocks issued by GCC markets leads to improve its overall risk-adjusted return performance and that oil price risk can be hedged more effectively in the GCC context.

The findings of the study offer several avenues for future research. First, the link between oil and stock markets in GCC countries can be expected to vary across different economic sectors. A sector analysis of this link would be more informative and generate more accurate implications for portfolio management. Second, further evidence drawn from international equity markets should be produced to examine the

robustness of the findings. Third, the methodology applied in this article could be used to investigate the effects of other energy products such as natural gas on aggregate and sector equity returns. Finally, further research on the oil-stock return and volatility linkages could compare their causality across GCC countries and other oilexporting as well as oil-importing countries.

## References

- [1] Arouri, M., Fouquau, J., 2009. On the short-term influence of oil price changes on stock markets in GCC countries: linear and nonlinear analyses. Economics Bulletin, 29, 806-815.
- [2] Barassi, M.R., Caporale, G.M., Hall, S.G., 2005. Interest rate linkages: a Kalman filter approach to detecting structural change. Economic Modelling, 22, 253-284.
- [3] Basher, S.A., Sadorsky, P., 2006. Oil price risk and emerging stock markets. Global Finance Journal, 17, 224-251.
- [4] Bollerslev, T., 1990. Modelling the coherence in short-run nominal exchange rate: A multivariate generalized ARCH approach. Review of Economics and Statistics, 72, 498-505.
- [5] Chan, F., Lim, C., McAleer, M., 2005. Modelling multivariate international tourism demand and volatility. Tourism Management, 26, 459-471.
- [6] Choi, K., Hammoudeh, S., 2010. Volatility behavior of oil, industrial commodity and stock markets in a regime-switching environment. Energy Policy, 38, 4388-4399.
- [7] Ciner, C., 2001. Energy shock and financial market nonlinear linkages. Studies in Nonlinear Dynamics and Econometrics, 5, 203-212.
- [8] Cologni, M., Manera, M., 2008. Oil prices, inflation and interest rates in a structural cointegrated VAR model for the G-7 countries. Energy Economics, 30, 856-888.
- [9] Cologni, M., Manera, M., 2009. The asymmetric effects of oil shocks on output growth: A Markov-switching analysis for the G-7 countries. Economic Modelling, 26, 1-29.
- [10] Cunado, J., Perez de Garcia, F., 2005. Oil prices, economic activity and inflation: evidence for some Asian countries. Quarterly Review of Economics and Finance, 45, 65-83.
- [11] Engle, R.F., 1982. Autoregressive conditional heteroscedasticity with estimates of the variance of United Kingdom inflation. Econometrica, 50, 987-1007.

- [12] Ewing, B.T., Malik, F., Ozfidan, O., 2002. Volatility transmission in the oil and natural gas markets. Energy Economics, 24, 525-538.
- [13] Fama, E.F., 1991. Efficient capital markets II. Journal of Finance, 46, 1575-1617.
- [14] Forbes, K., Rigobon, R., 2002. No contagion, only interdependence: measuring stock market comovements. Journal of Finance, 57, 2223-2261.
- [15] Guo, H., Kevin, L., 2005. Oil price volatility and US macroeconomic activity? Federal Reserve Bank of St. Louis Review, 87, 669-683.
- [16] Hamilton, J.D., 1983. Oil and the macroeconomy since World War II. Journal of Political Economy, 91, 228-248.
- [17] Hamilton, J.D., 2003. What is an oil shock? Journal of Econometrics, 113, 363-398.
- [18] Hammoudeh, S., Aleisa, E., 2004. Dynamic relationship among GCC stock markets and NYMEX oil futures. Contemporary Economic Policy, 22, 250-269.
- [19] Hammoudeh, S., Choi, K., 2006. Behavior of GCC stock markets and impacts of US oil and financial markets. Research in International Business and Finance, 20, 22-44.
- [20] Hammoudeh, S., Yuan, Y., McAleer, M., 2009. Shock and volatility spillovers among equity sectors of the Gulf Arab stock markets. Quarterly Review of Economics and Finance, 49, 829842.
- [21] Hassan, H., Malik, F., 2007. Multivariate GARCH model of sector volatility transmission. Quarterly Review of Economics and Finance, 47, 470-480.
- [22] Huang, R.D., Masulis, R.W., Stoll, H.R., 1996. Energy shocks and financial markets. Journal of Futures Markets, 16, 1-27.
- [23] Johansson, A.C., 2008. Interdependencies among Asian bond markets. Journal of Asian Economics, 19, 101-116.
- [24] Jones, C.M., Kaul, G., 1996. Oil and the stock markets. Journal of Finance, 51, 463-491.
- [25] Kang, S.H., Kang, S.M., Yoon, S.M., 2009. Forecasting volatility of crude oil markets. Energy Economics, 31, 119-125.
- [26] Kilian, L., 2008. Exogenous oil supply shocks: how big are they and how much do they matter for the US economy? Review of Economics and Statistics, 90, 216-240.
- [27] Kroner, K.F., Ng, V.K., 1998. Modeling asymmetric movements of asset prices, Review of Financial Studies, 11, 844-871.

- [28] Kroner, K.F., Sultan, J., 1993. Time-varying distributions and dynamic hedging with foreign currency futures. Journal of Financial and Quantitative Analysis, 28, 535-551.
- [29] Ling, S., McAleer, M., 2003. Asymptotic theory for a vector ARMA-GARCH model. Econometric Theory, 19, 278-308.
- [30] Maghyereh, M., Al-Kandari, A. Oil prices and stock markets in GCC countries: new evidence from nonlinear cointegration analysis. Managerial Finance, 33, 449-460.
- [31] Malik, F., Ewing, B.T., 2009. Volatility transmission between oil prices and equity sector returns. International Review of Financial Analysis, 18, 95-100.
- [32] McAleer, M., Hoti, S., Chan, F., 2009. Structure and asymptotic theory for multivariate asymmetric conditional volatility. Econometric Reviews, 28, 422-440.
- [33] Narayan, P.K., Narayan, S., 2007. Modelling oil price volatility. Energy Policy, 35, 6549-6553.
- [34] Oberndorfer, U., 2009. Energy prices, volatility, and the stock market: Evidence from the Eurozone. Energy Policy, 37, 5787-5795.
- [35] Papapetrou, E., 2001. Oil price shocks, stock market, economic activity and employment in Greece. Energy Economics, 23, 511-532.
- [36] Sadorsky, P., 1999. Oil price shocks and stock market activity. Energy Economics, 2, 449-469.
- [37] Skintzi, V., Refenes, A., 2006. Bond volatility spillovers and dynamic correlation in European bond markets. Journal of International Financial Markets, Institutions and Money, 16, 23-40.
- [38] Syriopoulos, T., 2007. Dynamic linkages between emerging European and developed stock markets: has the EMU any impact? International Review of Financial Analysis, 16, 41-60.
- [39] Wang, Z., Yang, J., Li, Q., 2007. Interest rate linkages in the Eurocurrency market: contemporaneous and out-of- sample Granger causality tests. Journal of International Money and Finance, 26, 86-103.
- [40] Zarour, B.A., 2006. Wild oil prices, but brave stock markets! The case of GCC stock markets. Operational Research, 6, 145-162.
- [41] Zhang, D., 2008. Oil shock and economic growth in Japan: a nonlinear approach. Energy Economics, 30, 2374-2390.

