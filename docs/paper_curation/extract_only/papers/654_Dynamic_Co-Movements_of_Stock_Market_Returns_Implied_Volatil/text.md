# Dynamic Co-movements of Stock Market Returns, Implied Volatility and Policy Uncertainty

### Nikolaos Antonakakisa,∗, Ioannis Chatziantonioua, George Filisb

aUniversity of Portsmouth, Department of Economics and Finance, Portsmouth Business School, Richmond Building, Portland Street, Portsmouth, PO1 3DE, United Kingdom bBournemouth University, Accounting, Finance and Economics Department, 89 Holdenhurst Road, Bournemouth, Dorset, BH8 8EB, United Kingdom

## Abstract

In this paper we examine the extent of time-varying correlations among stock markets returns, stock market implied volatility and policy uncertainty based on a newly introduced uncertainty index by Baker et al. (2012). We ﬁnd that the dynamic correlations of policy uncertainty and stock market returns are consistently negative, apart from the period during the latest global ﬁnancial crisis, wherein correlations became positive. Furthermore, an increase in the volatility of the stock market and the policy uncertainty dampens stock market returns, while it increases policy uncertainty. Finally, aggregate demand oil price shocks and US recessions signiﬁcantly aﬀect the correlation between policy uncertainty and stock market returns.

Keywords: Policy uncertainty, dynamic correlation, stock market return, implied volatility, oil price shock

JEL codes: C32; E60; E66; G10; G18

## 1. Introduction

The foundations of the eﬀects of policy uncertainty on the economy have been placed for more than 30 years now (see, inter alia, Marcus, 1981; Bernanke, 1983; Aizenman and Marion, 1991; Rodrik, 1991). Nevertheless, the interest in the eﬀects of policy has resurged especially after the advent of the 2007 ﬁnancial crisis. Authors mainly focus their attention on the examination of the eﬀects of policy uncertainty on macroeconomic variables, such as growth, inﬂation and investment (see, Bloom, 2009; Baum et al., 2010; Bachmann et al., 2010; Jones and Olson, 2013, among others). Arguably, in the presence of uncertainty regarding the eﬀectiveness of the macroeconomic policies, rational agents will withhold their investment decision (considering that these investments are either completely or partly irreversible) until the uncertainty is removed. Thus, the general consensus is that uncertainty has a negative eﬀect on the level of growth and investment. The

∗Corresponding author, phone: +44 (0)23 9284 4261, fax: +44 (0)23 9284 4037. Email addresses: nikolaos.antonakakis@port.ac.uk (Nikolaos Antonakakis),

ioannis.chatziantoniou@port.ac.uk (Ioannis Chatziantoniou), gfilis@bournemouth.ac.uk (George Filis)

eﬀect of uncertainty on inﬂation is less clear-cut as it depends on international shocks, such as oil price shocks, according to Jones and Olson (2013).

The aim of this paper is to contribute towards the study of the eﬀects of macroeconomic policy uncertainty on the economy, focusing on its eﬀects on stock market performance. In particular, we explore the dynamic co-movements between macroeconomic policy uncertainty, stock market returns and stock market (implied) volatility using the newly introduced index of macroeconomic uncertainty by Baker et al. (2012) and a more elaborate measure of correlations.

To achieve that, we construct time-varying measures of correlations among policy uncertainty, stock market returns and stock market (implied) volatility based on the dynamic conditional correlation (DCC) model of Engle (2002). Taking into account both time variation and conditional heterogeneity in correlations, the proposed measure has several advantages compared to other commonly used measures. It is able to distinguish negative correlations due to episodes in single years, synchronous behavior during stable years and asynchronous behavior in turbulent years. Unlike rolling windows, an alternative way to capture time variability, the proposed measure does not suffer from the so called “ghost features”, as the eﬀects of a shock are not reﬂected in m consecutive periods, with m being the window span. In addition, under the proposed measure there is neither need to set a window span, nor loss of observations, nor is there a requirement for subsample estimation.

Our results based on monthly data between January 1985 and January 2013 suggest that dynamic correlations between policy uncertainty and stock market returns are consistently negative, apart from the period during the latest ﬁnancial crisis, wherein dynamic correlations became positive. In addition, an increase in the volatility of the stock market and the policy uncertainty dampens stock market returns, while increases policy uncertainty. Last but not least, aggregate demand shocks are negatively associated with dynamic correlations, whereas dynamic correlations reveal heterogeneous patterns during US recessions.

The remainder of the paper is organized as follows. Section 2 discusses the methodology. Section 3 describes the data. Section 4 presents the empirical ﬁndings, and Section 5 summarizes and concludes the paper.

## 2. Methodology

In order to examine the evolution of co-movements between policy uncertainty, stock market returns and stock market (implied) volatility, we obtain a time-varying measure of correlation based on the dynamic conditional correlation (DCC) model of Engle (2002).

Let yt = [y1t,y2t] be a 2×1 vector comprising the data series. The conditional mean equations are then represented by:

A(L)yt = εt, where εt|Ωt−1 ∼ N(0,Ht), and t = 1,...,T (1)

where A is a matrix, L the lag operator and εt is the vector of innovations based on the information set, Ω, available at time t − 1. The εt vector has the following conditional variance-covariance matrix:

Ht = DtRtDt, (2) where Dt = diag√hit is a 2 × 2 matrix containing the time-varying standard deviations obtained from univariate GARCH(p,q) models and Rt = ρijt = √qii,tqij,tqjj,t where i,j = 1,2 is the 2×2 matrix comprising the conditional correlations and which are our main focus.

## 3. Data

The data used in this study are the policy uncertainty index series, the implied volatility index of S&P500 (VIX) and the S&P500 returns. The former series comes from Baker et al. (2012) and measures policy-related economic uncertainty in the United States. In particular, it’s a constructed index based on three components. The ﬁrst component quantiﬁes newspaper coverage of policy-related economic uncertainty. The second component reﬂects the number of federal tax code provisions set to expire in future years. The third component uses disagreement among economic forecasters as a proxy for uncertainty. The VIX data series is obtained from Datastream. The S&P500 returns series is obtained from FRED database and deﬁned as the annualized monthly change of the natural logarithm of S&P500 index, and given by: 1200 × (log(S&P500t) − log(S&P500t−1)). Our sample ranges from January 1985 to January 2013 (337 observations).

Figure 1 shows the evolution of the policy uncertainty index of Baker et al. (2012), the VIX and the S&P500 returns. According to this ﬁgure, we observe that peaks of the uncertainty index to be associated with abrupt changes in stock market returns. A feature which we explore further below. In addition, there is an increasing pattern in the policy uncertainty index, beginning to emerge since the outbreak of the ﬁnancial crisis in mid-2007.

Table 1 presents descriptive statistics of our data series. According to this table, we observe large variability in our main variables. The augmented Dickey-Fuller (ADF) test with just a constant indicates that S&P500 returns are stationary (as the null hypothesis of a unit root process is rejected), while uncertainty contains a unit root. Nevertheless, policy uncertainty is stationary in levels with a structural break taking place in August 2007, according to the Zivot and Andrews (1992) unit root test –a fact that was also observed informally by looking at Figure 1. The fact that the ARCH-LM test rejects the null hypothesis of homoskedasticity for each series suggests that it is appropriate to model these series as an ARCH-type process. Finally, the unconditional correlation between policy uncertainty and S&P500 returns is negative, while all remaining unconditional correlations are positive.

## 4. Estimation Results

Table 2 reports the results of the three bivariate DCC models. Panels A and B present the conditional mean and variance results, respectively, while Panel C contains the Ljung-Box QStatistics on the standardized and squared standardized residuals, respectively, up to 12 lags. The choice of the lag length of the autoregressive process (AR) process of the conditional mean (CM) is based on the Akaike information criterion (AIC) and Schwarz Bayesian criterion (BIC) and serves to remove any serial correlation in the standardized residuals. The conditional variance of the series and a dummy variable, D, that equals 1 for the period of August 2007 onwards and 0 otherwise (to account for the upward trend in the uncertainty index in that period) are included whenever appropriate.

According to the results of the ﬁrst model between policy uncertainty and stock market returns in Table 2, we observe that increased stock market conditional volatility increases policy uncertainty and dampens stock markets returns, while increases in the volatility of policy uncertainty lead to negative stock market returns and increased policy uncertainty. The dummy variable is signiﬁcantly positive justifying the fact that uncertainty is higher in the post-August 2007 period.

There is an ongoing discussion on the fact that, even though the implied volatility index, VIX, has followed a declining trend since the peak of the latest ﬁnancial crisis – and which is in line with the theory that uncertainty in the stock markets is being resolved after a crash (see, for instance, Hong and Stein, 2003; Zeira, 1999; Lee, 1998; Caplin and Leahy, 1994; Romer, 1993) –, we cannot observe the same pattern for the policy uncertainty index. On the contrary, the policy uncertainty index follows an increasing trend, which may the reason be hampering the recovery in the United States. We examine the interdependencies of policy uncertainty and the VIX in model 2 of Table 2. Finally, for robustness purposes we examine interdependencies between S&P500 returns and the VIX. Model 3 in Table 2 presents these results. One lag of the S&P500 returns and the VIX was enough to ﬁlter any remaining correlation. We observe that in addition to the conditional volatility (see Model 1), the implied volatility index has a signiﬁcantly negative (positive) eﬀect on stock market returns (the VIX), as well. Finally, S&P500 returns have a signiﬁcantly positive eﬀect on S&P500 returns but no signiﬁcant impact on the VIX.1

In Figure 2, we present the dynamic conditional correlations of the three models estimated in Table 2, along with their 90% conﬁdence intervals. The time-varying correlation between policy uncertainty and stock market returns is consistently negative over time, apart from the period during the latest global ﬁnancial crisis, wherein correlations became positive. A plausible explanation why the correlation in the later part of the ﬁnancial crisis did not behave as expected can be found in the unprecedented bailout package for the US banking sector of 2008 and the stimulus package of 2009. Even though the policy uncertainty remains high after these two packages, the stock market responded favourably, considering that in the later part of the ﬁnancial crisis the market was experiencing positive returns.

Looking at the time-varying correlations between policy uncertainty and the VIX, we observe the following regularities. First, correlations ﬂuctuate substantially over the sample period. More importantly, we observe that the correlations return to, or even exceed, the pre-recession levels, following the 1991 and 2001 U.S. recessions. However, in the case of the latest recession of 2007-09, correlations are yet to reach pre-crisis levels. On the contrary, they became negative from the second half of the 2007-09 recession and until mid-2010. These developments could be explained by the fact that although stock market uncertainty (lower variation in stock market returns and lower implied volatility - see Figure 1) has declined since the latest global recession (apart from few spikes in June 2010, October 2011 and June 2012), the policy uncertainty has not followed suit. Thus, the unusually high levels of policy uncertainty might have been, among others, an important factor hampering the recovery in the United States.

Finally, the dynamic correlation between stock market returns and VIX is negative throughout the sample period and it seems to follow a declining trend. In addition, stock market crashes (Black Monday of 1987, Russian ﬁnancial crisis of 1998 and the latest ﬁnancial crisis of 2008) are associated with sharp declines in the correlation levels.

An important question that arises is what explains the evolution of these dynamic correlations. In order to tackle this issue, we apply a Fisher transformation on the estimated time-varying

correlations, ρt, between policy uncertainty, VIX and stock market returns according to DCt = log((1+ρt)/(1−ρt)), so as to ensure our dependent variable is not conﬁned to the interval [−1,1],2

- 1All three model speciﬁcations in Table 2 do not suﬀer from serial correlation in the squared (standardized) residuals according to the misspeciﬁcation tests in Panel C of Table 2.
- 2The results are not sensitive to this transformation though.

and estimate various speciﬁcations of the following model: DCt = α + βDCt−1 + γOil Shockst + δDomestic Shockst + θUS Recessionst + t, (3)

where α is a constant, Oil Shockst is a vector of three oil price shocks3, Domestic Shockst is a vector of domestic shocks, namely, US industrial production growth and inﬂation so as to account for changes in the real economy not captured by the oil shock variables, US Recessionst is a dummy variable that equals 1 during US recessions, as deﬁned by NBER, and 0 otherwise, and

t is the innovation. Finally, one lag of the dependent variable, DCt−1, is included to account for ﬁrst-order serial correlation in our transformed variable.

Table 3 presents the results of the various forms of model (3). Under Columns (1)–(4), we examine the eﬀects of oil price shocks without including any of the domestic shocks or US recessions dummy variables. We ﬁnd that only the aggregate demand shocks have a negative and signiﬁcant eﬀect on dynamic correlation, suggesting that this speciﬁc oil price shock pushes the correlation to lower values. This is plausible as positive aggregate demand shocks (which result due to global economic growth) would decrease the policy uncertainty of the macroeconomic policies and increase stock returns. Under Columns (5)–(12), we also add the domestic shocks to account for changes in the real economy not captured by international factors. We ﬁnd that even after controling for domestic factors the results remain robust. Finally, under columns (13)–(14), we include dummy variables for the US recessions.4 Our results reveal that US recessions do not seem to impact the dynamic correlation unless we isolate the eﬀects of individual recession periods. Interestingly, the impact of the latest ﬁnancial crisis is positive and signiﬁcant, while the reverse holds true for the 1991 and 2001 recessions. This is indicative of the unique features of the 2007–09 ﬁnancial crisis (Claessens et al., 2010; Antonakakis, 2012).5

## 5. Conclusion

The focal point of this study is the extent of time-varying correlations among stock market returns, implied volatility and policy uncertainty. In particular, we employ the S&P500 returns, the VIX and the policy uncertainty index of Baker et al. (2012) that has recently gained considerable attention. Results show that the dynamic correlation between policy uncertainty and stock market returns is consistently negative over time, apart from the latest ﬁnancial crisis. Moreover, an increase in the volatility of the stock market and the policy uncertainty dampens stock market returns, while it increases policy uncertainty. Finally, aggregate demand shocks are negatively associated with dynamic correlations, whereas dynamic correlations reveal heterogeneous patterns during US recessions.

A potential avenue for future research is to examine whether a similar pattern can be observed for European economies.

- 3Oil price shocks have been estimated using the framework developed by Kilian (2009). Kilian (2009) identiﬁes three oil price shocks (namely, supply-side shocks, aggregate demand shocks and oil speciﬁc demand shocks). Supplyside shocks are associated with changes in the world oil production, aggregate demand shocks are associated with changes in the global economic activity and oil speciﬁc demand shocks are associated with concerns about the future availability of oil.
- 4To achieve that, we include a dummy variable reﬂecting all three recessions, and three individual dummy variables for the 1991, 2001 and 2007 US recessions, in Table 3 under speciﬁcations (13) and (14), respectively.
- 5As a robustness analysis, we repeated the estimation with the remaining two time-varying correlations. Our main conclusions remain similar. These results are available upon request.

## References

Aizenman, J., Marion, N., 1991. Policy Uncertainty, Persistence and Growth. NBER Working Papers 3848, National Bureau of Economic Research, Inc. Antonakakis, N., 2012. Business Cycle Synchronization During US Recessions Since the Beginning of the 1870s. Economics Letters 117 (2), 467–472. Bachmann, R., Elstner, S., Sims, E. R., 2010. Uncertainty and Economic Activity: Evidence from Business Survey Data. NBER Working Papers 16143, National Bureau of Economic Research, Inc. Baker, S., Bloom, N., Davis, S., 2012. Measuring Economic Policy Uncertainty. Working Paper Series, Stanford University. Baum, C. F., Caglayan, M., Talavera, O., 2010. On the Sensitivity of Firms’ Investment to Cash Flow and Uncertainty. Oxford Economic Papers 62 (2), 286–306. Bernanke, B. S., 1983. Irreversibility, Uncertainty, and Cyclical Investment. The Quarterly Journal of Economics

98 (1), 85–106. Bloom, N., 2009. The Impact of Uncertainty Shocks. Econometrica 77 (3), 623–685. Caplin, A., Leahy, J., 1994. Business as Usual, Market Crashes, and Wisdom after the Fact. American Economic

Review 84 (3), 548–565. Claessens, S., Kose, M. A., Terrones, M. E., 2010. The Global Financial Crisis: How Similar? How Diﬀerent? How Costly? Journal of Asian Economics 21 (3), 247–264. Engle, R., 2002. Dynamic Conditional Correlation: A Simple Class of Multivariate Generalized Autoregressive Conditional Heteroskedasticity Models. Journal of Business & Economic Statistics 20 (3), 339–350. Hong, H., Stein, J. C., 2003. Diﬀerences of Opinion, Short-Sales Constraints, and Market Crashes. Review of Financial Studies 16 (2), 487–525. Jones, P. M., Olson, E., 2013. The Time-Varying Correlation between Uncertainty, Output, and Inﬂation: Evidence from a DCC-GARCH Model. Economics Letters 118 (1), 33–37. Kilian, L., 2009. Not All Oil Price Shocks Are Alike: Disentangling Demand and Supply Shocks in the Crude Oil

Market. American Economic Review 99 (3), 1053–1069. Lee, I. H., 1998. Market Crashes and Informational Avalanches. Review of Economic Studies 65 (4), 741–59. Marcus, A. A., 1981. Policy Uncertainty and Technological Innovation. The Academy of Management Review 6 (3),

443–448. Rodrik, D., 1991. Policy Uncertainty and Private Investment in Developing Countries. Journal of Development

Economics 36 (2), 229–242. Romer, D., 1993. Rational Asset-Price Movements without News. American Economic Review 83 (5), 1112–1130. Zeira, J., 1999. Informational Overshooting, Booms, and Crashes. Journal of Monetary Economics 43 (1), 237–257. Zivot, E., Andrews, D. W. K., 1992. Further Evidence on the Great Crash, the Oil-Price Shock, and the Unit-Root

Hypothesis. Journal of Business & Economic Statistics 10 (3), 251–270.

#### Figure 1: Baker et al. (2012) Uncertainty index, S&P500 Returns and Implied Volatility Index (VIX)

|Uncertainty Index - Baker et al. (2012)|
|---|

200

100

1985 1990 1995 2000 2005 2010

|Implied Volatility Index - VIX|
|---|

50

25

1985 1990 1995 2000 2005 2010

200

|Stock Market Returns - S&P500|
|---|

0

-200

1985 1990 1995 2000 2005 2010

#### Figure2:DynamicconditionalcorrelationsofUncertaintyandS&P500Returns

198519901995200020052010

198519901995200020052010

198519901995200020052010

|DynamicCorrelation between Policy Uncertainty andStockMarketReturnsUpper90%CILower90%CI<br><br>|
|---|

DynamicCorrelation between Policy Uncertainty andStockMarketReturnsUpper90%CILower90%CI

|DynamicCorrelation Between StockMarketReturnsandVIXUpper90%CILower90%CI<br><br>|
|---|

DynamicCorrelation Between StockMarketReturnsandVIXUpper90%CILower90%CI

|DynamicCorrelation between Policy Uncertainty andVIXUpper60%CILower60%CI<br><br>|
|---|

DynamicCorrelationeen Policy Uncertainty andVIXUpper60%CILower60%CI

0.25

0.00

0.50

0.25

0.00

-0.25

-0.50

-0.75

Note:Blue,redandgreensolidlinesarethedynamicconditionalcorrelationsbetweenPolicyUncertaintyandStockmarketReturns,PolicyUncertainty

andtheImpliedVolatilityIndex,andbetweenStockMarketReturnsandtheImpliedVolatilityIndex(VIX),respectively.Dottedlinesarethe90%

conﬁdenceintervals.ShadingdenotesUSrecessionsasdeﬁnedbyNBER.

Table 1: Descriptive statistics

# Uncertainty VIX S&P500 Returns Min 57.519 10.31 -296.21 Mean 107.38 20.697 7.8428 Max 246.47 68.51 175.34 Std 33.13 7.8615 56.222 ADFa (constant) -2.3530 -4.1506** -7.4227** Zivot-Andrewsb -5.3401** ARCH(12) LM Test 74.873** 30.707** 4.2361**

# Unconditional Correlations Uncertainty 1.0000 VIX 0.4274 1.0000 S&P500 Returns -0.1830 -0.4082 1.0000

Note:

- a The 5% and 1% critical values are -2.86 and -3.43, respectively.
- b The estimated break date is August 2007.

* and ** indicate signiﬁcance at 5% and 1% level, respectively.

Table 2: Estimation results of bivariate DCC-GARCH models, Period: 1985M1 – 2013M1

- Panel A: Conditional mean Model 1: Model 2: Model 3:

Uncertainty & S&P500 Uncertainty & VIX S&P500 & VIX ut spt ut vixt spt vixt

Cons 13.838*** -9.644 Cons 15.719*** 3.730*** Cons 0.003 3.42*** (3.264) (11.973) (3.743) (0.779) (1.716) (0.147)

- ut−1 0.702*** -0.595*** ut−1 0.647*** 0.065*** spt−1 0.084** -0.000 (0.062) (0.138) (0.051) (0.011) (0.041) (0.003)
- ut−2 0.106 0.143 ut−2 0.110* -0.006 vixt−1 -0.412*** 0.822*** (0.068) (0.184) (0.065) (0.013) (0.041) (0.006)
- ut−3 -0.199*** 0.561*** ut−3 -0.119** -0.042*** (0.065) (0.159) (0.056) (0.011)
- ut−4 0.214*** 0.065 ut−4 0.146*** -0.030 (0.046) (0.135) (0.049) (0.010)

hut 0.002*** -0.068*** vixt−1 0.259* 0.004*** (0.005) (0.017) (0.13) (0.001)

hspt 0.001*** -0.008*** hut -0.001 0.798***

(0.001) (0.003) (0.005) (0.032) D 12.633*** D 13.697***

(2.430) (2.529)

- Panel B: Conditional variance: Ht = Γ Γ + A t−1 t−1A + B Ht−1B γ 29.401** 1395.664*** 35.514** 5.344*** 98.280*** 7.929***

(11.863) (175.353) (15.783) (1.157) (19.932) (0.222) α1 0.312*** 0.271*** 0.336*** 0.709*** 0.137*** 0.155*** (0.071) (0.073) (0.070) (0.159) (0.009) (0.022) β2 0.631*** 0.221*** 0.614*** 0.187*** 0.823*** 0.373*** (0.065) (0.054) (0.066) (0.068) (0.006) (0.014)

- a 0.077*** (0.061) 0.065** (0.031) 0.025*** (0.001)
- b 0.849*** (0.127) 0.933*** (0.033) 0.975*** (0.001)

- Panel C: Misspeciﬁcation tests Q(12) 18.4657 8.0964 17.9388 16.4735 8.2212 8.7899

[0.1023] [0.7776] [0.1176] [0.1705] [0.7676] [0.7208] Q2(12) 8.4881 6.0645 7.7822 4.2535 5.0293 5.3973

[0.7459] [0.9128] [0.8019] [0.9784] [0.9570] [0.9412]

Note: ut, spt, vixt, hut and hspt denote policy uncertainty, S&P500 returns, implied volatility index (VIX), conditional variance of uncertainty and conditional variance of S&P500 returns, respectively, at time t. D is a dummy variable that equals one for t ≥ August 2007 and zero otherwise. Q(12) and Q2(12) are the Ljung-Box Q-Statistics on the standardized and squared standardized residuals, respectively, up to 12 lags. Standard Errors in parenthesis and p-values in square brackets. ***, ** and * denote statistical signiﬁcance at the 1 percent, 5 percent and the 10 percent level, respectively.

Table3:Dynamiccorrelationsandtheroleofoilpriceshocks

Constant-0.0169***-0.0171***-0.0178***-0.0161***-0.0148***-0.0158***-0.0151***-0.0149***-0.0145***-0.0156***-0.0148***-0.0145***-0.0144***-0.0197***

(0.0048)(0.0047)(0.0047)(0.0047)(0.0049)(0.0048)(0.0049)(0.0050)(0.0050)(0.0048)(0.0050)(0.0050)(0.0053)(0.0054)

Variable(1)(2)(3)(4)(5)(6)(7)(8)(9)(10)(11)(12)(13)(14)

DC0.8954***0.8947***0.8956***0.8941***0.8934***0.8935***0.8937***0.8933***0.8916***0.8920***0.8919***0.8915***0.8917***0.8671***−t1

(0.0247)(0.0244)(0.0248)(0.0244)(0.0247)(0.0244)(0.0247)(0.0245)(0.0248)(0.0245)(0.0248)(0.0246)(0.0250)(0.0251)

shock(0.2115)(0.2091)(0.2114)(0.2098)(0.2120)(0.2103)(0.2110)(0.2063)t

SupplySide-0.2309-0.2301-0.2102-0.2168-0.2223-0.2277-0.2272-0.2258

Aggregate-0.2202***-0.2202***-0.2025***-0.2017***-0.2015***-0.1992***-0.1991***-0.2267***

Demandshock(0.0717)(0.0718)(0.0741)(0.0750)(0.0742)(0.0751)(0.0752)(0.0741)t

shock(0.0203)(0.0200)(0.0230)(0.0230)(0.0232)(0.0233)(0.0233)(0.0228)t

OilSpecific-0.0053-0.00550.01370.00400.01680.00700.00700.0049

(0.0563)(0.0575)(0.0638)(0.0661)(0.0563)(0.0575)(0.0640)(0.0664)(0.0666)(0.0655)

Inflation-0.0907-0.0543-0.1120*-0.0563-0.0906-0.0547-0.1162*-0.0606-0.0608-0.0412t

Production(0.0284)(0.0281)(0.0287)(0.0285)(0.0321)(0.0316)t

Industrial-0.0240-0.0205-0.0251-0.0239-0.0246-0.0073

(0.0081)

US-0.0004rec

US-0.0264*rec91

(0.0140)

US-0.0270**rec01

(0.0139)

US0.0294***rec07

(0.0107)

2R0.80030.80520.79960.80470.80120.80510.80090.80460.80110.80480.80070.80440.80380.8126

Note:Ineachspeciﬁcation,thedependentvariable,DC,isthetransformedcorrelationbasedontheFishertransformation.Heteroskedasticityrobustt

standarderrorsarereportedinparenthesis.***,**and*denotestatisticalsigniﬁcanceatthe1percent,5percentandthe10percentlevel,respectively.

