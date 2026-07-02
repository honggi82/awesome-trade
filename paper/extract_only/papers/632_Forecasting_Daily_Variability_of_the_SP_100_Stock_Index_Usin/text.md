[Figure 1]

TI 2004-016/4 Tinbergen Institute Discussion Paper

# Forecasting Daily Variability of the S&P 100 Stock Index using Historical, Realised and Implied Volatility Measurements

### Siem Jan Koopmana,b Borus Jungbackera Eugenie Holc

aDepartmentof Econometrics, VrijeUniversiteit Amsterdam, bTinbergen Institute, cING GroupCredit Risk Managemen t, The Nethelands.r

|Tinbergen Institute The Tinbergen Institute is the institute for economic research of the Erasmus Universiteit Rotterdam, Universiteit van Amsterdam, and Vrije Universiteit Amsterdam.<br><br>Tinbergen Institute Amsterdam Roetersstraat 31 1018 WB Amsterdam The Netherlands Tel.: +31(0)20 551 3500 Fax: +31(0)20 551 3555<br><br>Tinbergen Institute Rotterdam Burg. Oudlaan 50 3062 PA Rotterdam The Netherlands Tel.: +31(0)10 408 8900 Fax: +31(0)10 408 9031<br><br>Please send questions and/or remarks of nonscientific nature to driessen@tinbergen.nl. Most TI discussion papers can be downloaded at http://www.tinbergen.nl.|
|---|

## Forecasting daily variability of the S&P 100 stock index using historical, realised and implied volatility measurements

Siem Jan Koopman(a,b)∗ Borus Jungbacker(a) Eugenie Hol(c) (a) Department of Econometrics, Free University Amsterdam (b) Tinbergen Institute Amsterdam (c) ING Group Credit Risk Management, The Netherlands

January 29, 2004

Abstract

The increasing availability of ﬁnancial market data at intraday frequencies has not only led to the development of improved volatility measurements but has also inspired research into their potential value as an information source for volatility forecasting. In this paper we explore the forecasting value of historical volatility (extracted from daily return series), of implied volatility (extracted from option pricing data) and of realised volatility (computed as the sum of squared high frequency returns within a day). First we consider unobserved components and long memory models for realised volatility which is regarded as an accurate estimator of volatility. The predictive abilities of realised volatility models are compared with those of stochastic volatility models and generalised autoregressive conditional heteroskedasticity models for daily return series. These historical volatility models are extended to include realised and implied volatility measures as explanatory variables for volatility. The main focus is on forecasting the daily variability of the Standard & Poor’s 100 stock index series for which trading data (tick by tick) of almost seven years is analysed. The forecast assessment is based on the hypothesis of whether a forecast model is outperformed by alternative models. In particular, we will use superior predictive ability tests to investigate the relative forecast performances of some models. Since volatilities are not observed, realised volatility is taken as a proxy for actual volatility and is used for computing the forecast error. A stationary bootstrap procedure is required for computing the test statistic and its p-value. The empirical results show convincingly that realised volatility models produce far more accurate volatility forecasts compared to models based on daily returns. Long memory models seem to provide the most accurate forecasts.

JEL classiﬁcation: C22, C53, G15.

Keywords: Generalised autoregressive conditional heteroskedasticity model, Long memory model, Realised volatility, Stochastic volatility model, Superior predictive ability, Unobserved components.

[Figure 2]

∗Corresponding author: Siem Jan Koopman, Department of Econometrics and OR, Free University Amsterdam, De Boelelaan 1105, NL-1081 HV Amsterdam, The Netherlands. http://staff.feweb.vu.nl/koopman/ We would like to thank Marius Ooms and two referees for their comments which have led to a much improved paper. An earlier version of this paper was circulated with title “Stock Index Volatility Forecasting with High Frequency Data”. All errors in the paper are ours.

#### 1 Introduction

Modelling and forecasting volatility in ﬁnancial markets has gained much interest in the ﬁnancial and economic literature. The seminal paper of Engle (1982) has started the development of a large number of so-called historical volatility models in which a time-varying volatility process is extracted from ﬁnancial returns data. Most volatility models can be regarded as variants of the generalised autoregressive conditional heteroskedasticity (GARCH) models of Bollerslev (1986), see Bollerslev, Engle, and Nelson (1994) for a review. A rival class of volatility models is associated with the stochastic volatility (SV) model, see Taylor (1986) and Harvey, Ruiz, and Shephard (1994). The overviews presented in Shephard (1996) and Ghysels, Harvey, and Renault (1996) provide an excellent introduction to historical volatility models. A more recent review of volatility models together with an assessment of their forecasting performances is given by Poon and Granger (2003).

Both GARCH and SV models are regularly used for the analysis of daily, weekly and monthly returns. From a theoretical perspective these models can also be applied to returns data measured at higher frequencies (intraday). However, it is learned from empirical studies that these models can not accomodate all information in high frequency returns. The initial work of Andersen and Bollerslev (1998) and Barndorﬀ-Nielsen and Shephard (2001) show that realised volatility (a daily volatility measure) as computed by the cumulative sum of squared intraday returns is less subject to measurement error and therefore less noisy. This empirical fact is supported by the theory that the measurement noise contained in daily squared returns prevents the observation of the volatility process while it is reduced as the sampling frequency of the return series from which volatility is calculated is increased, see Andersen, Bollerslev, Diebold, and Labys (2001) and Barndorﬀ-Nielsen and Shephard (2001, 2002). These results also justify the earlier work of French, Schwert, and Stambaugh (1987), amongst others. Andersen and Bollerslev (1998) show that daily forecasts of exchange rates based on GARCH models, when evaluated against realised volatility, are far more accurate than had been previously assumed. These ﬁndings were subsequently conﬁrmed with regards to stock index data by Blair, Poon, and Taylor (2001) and Hansen and Lunde (2003b) who examined the predictive accuracy of volatility forecasts based on GARCH models.

Volatility can be extracted from returns data but it can also be derived from option pricing data in combination with an option pricing model. Early empirical studies by Latane´ and Rendleman (1976), Chiras and Manaster (1978) and Beckers (1981) have indicated that implied volatility, when compared with historical standard deviations, can be regarded as a good predictor of future volatility. Implied volatility is often referred to as the market’s volatility forecast and is said to be forward looking as opposed to historical based methods which are by deﬁnition backward looking. More recent studies by Christensen and Prabhala (1998), Fleming (1998), Blair, Poon, and Taylor (2001) and Giot (2003) show that accurate volatility forecasts for returns on stock indices are often based on implied volatility. Moreover, their research strongly suggests that daily returns contain little or no incremental information about future volatility.

In this paper we investigate the potential gains of diﬀerent measures of volatility and diﬀerent ways of modelling these data for the purpose of volatility forecasting. For example, Blair, Poon, and Taylor (2001) and Martens (2001) suggest to incorporate realised volatility as an explanatory variable in the variance equation of a daily GARCH model. They found a considerable improvement in the forecasting performance in this way. Another possible explanatory variable for volatility is implied

volatility. We will explore this option further by incorporating such explanatory variables in both GARCH and SV models.

Realised volatility can also be modelled directly which is reminiscent of the methods adopted for monthly volatility in a number of earlier studies such as those by French, Schwert, and Stambaugh (1987) and Poon and Taylor (1992). The forecasting performance of realised volatility models has been studied, amongst others, by Andersen, Bollerslev, Diebold, and Ebens (2001) and Barndorﬀ-Nielsen and Shephard (2004a). In the ﬁrst paper, it is stressed that long memory features are present in the logarithms of realised volatility and that the autoregressive fractionally integrated moving average (ARFIMA-RV) model is eﬀective in empirical modelling. The second paper builds on BarndorﬀNielsen and Shephard (2002) where volatility is represented as a continuous time series process, the sum of independent Le´vy driven Ornstein-Uhlenbeck (OU) processes. This approach forms the basis of an unobserved components (UC-RV) model for realised volatility that consists of independent ARMA components with restricted parameters.

The empirical investigation is for the Standard & Poor’s 100 (S&P 100) stock index series over the period 6 January 1997 to 14 November 2003 with 1725 trading days. Opening and closure prices for all trading days in the sample are available in this period together with all price quotes within the days (tick by tick). Further we have obtained the S&P 100 implied volatility index from the Chicago Board Options Exchange Market volatility index (VIX) which is known to be a highly liquid options market. The forecasting performance of various volatility models for the last 525 days of the data set is the focus of the empirical study. We compare the forecasts of ARFIMA-RV, UC-RV, SV and GARCH volatility models; the latter two models are considered with and without explanatory variables. The forecasts are generated by a rolling-window of 1200 observations through the last 525 daily observations. Forecast comparison is based on four diﬀerent loss functions including the mean squared error and the mean absolute error statistics. The fact that a particular loss criterion is smallest for a particular model does not provide any information about its forecast superiority in other samples of the data set and in future samples of the data. The results in White (2000) and the important reﬁnements in Hansen (2001) constitute a framework that constructs a formal test for superior prediction ability (SPA) of a benchmark or base model relative to a set of rival models. Since volatility can never be observed, realised volatility is taken as a proxy for actual volatility and used for determining the forecast error. This may introduce inconsistencies in the ranking of forecast models but it is argued that the occurrence of such inconsistencies are unlikely in our study. The method of computing the SPA test statistic and its p-value requires bootstrap samples obtained by, for example, the stationary bootstrap procedure of Politis and Romano (1994). The construction of the test and some details of implementation are discussed.

The ﬁndings of this extensive empirical study are presented by reporting a selection of the most interesting results. The maximum likelihood estimates for the coeﬃcients of the considered models are reported for the full sample. Although these estimates are not used for forecasting since all models are re-estimated for each rolling window sample (starting from 17 October 2001), the reported estimation results provide insights about the S&P 100 data set and the eﬀectiveness of models to capture volatility information from the data. A selection of the forecasting results is also presented but most attention is paid to the SPA results. It has become clear that the realised volatility models are overwhelmingly superior and therefore making comparisons between, say, GARCH and ARFIMA-RV is not useful. We therefore concentrate on the comparison of models within the two classes of realised volatility models

and historical volatility models. It will be concluded that both the ARFIMA-RV and the SV model with realised volatility as the explanatory variable are superior within their classes for the forecasting of S&P 100 volatility.

The remainder of this paper is organised as follows. In the next section we discuss the available data sets and discuss how returns are constructed and how volatility measures are derived from these returns. In section 3 we provide some details about the realised volatility models, the UC-RV and ARFIMA-RV models. In section 4 the historical volatility models are shortly described. The forecastig methodology is discussed in section 5 and in section 6 the estimation and forecasting results are presented. Section 7 concludes.

#### 2 Stock Return Data and Volatility

##### 2.1 Daily and intradaily returns

The data for our empirical study consists of Standard & Poor’s 100 (S&P 100) stock index transaction prices during the period from 6 January 1997 to 14 November 2003 which constitutes a total of N = 1,725 trading days. The daily return Rn is deﬁned as the ﬁrst diﬀerence between the 4.00 pm closing prices on consecutive trading days, expressed in percentage terms, that is

Rn = 100(ln Pn − lnPn−1), n = 1,... ,N, (1) where Pn is the closing asset price at trading day n.

In the S&P 100 dataset, the price quotes are available for all trading days. We can therefore extract intraday returns for any interval that is usually measured in minutes. Such high-frequency returns are subject to market micro structures (bid-ask bounces, discrete price observations, etcetera) which distort the return properties of interest. The 5-minute frequency is regarded as the highest frequency at which the eﬀects of market microstructure are not too distorting. Andersen and Bollerslev (1998) also construct their intraday returns using the 5-minute frequency. A more complete discussion on the choice of frequency is given by Andersen, Bollerslev, Diebold, and Labys (2001). To construct the 5-minute return, the last transaction price is recorded before the relevant time mark and the diﬀerence is taken between successive log prices, that is

Rn,d = 100(ln Pn,d − lnPn,d−1), n = 1,... ,N, d = 1,... ,D, (2)

where Pn,d is the asset price at trading day n, at the 5-minute mark d. Note that Pn,0 is the opening price of day n.

The New York Stock Exchange opens at 9.30 am and closes at 4 pm EST. A full trading day therefore consists of D = 78 intraday returns and one overnight return. Not all trading days will have 78 5-minute quotes because the New York Stock Exchange closes early on certain days (for example, Christmas Eve). Another important reason for a diﬀerent number of 5-minute returns is the lapses in trading and in data reporting on some trading days. Various methods are used to deal with such problems. For example, Andersen, Bollerslev, Diebold, and Ebens (2001) consider linear interpolation through bid-ask quotes in order to obtain a full set of 5-minute interval returns. A ﬂexible spline interpolation method is used by Hansen and Lunde (2003b).

Following this recent literature we have used a spline method for the construction of 5-minute returns as follows. All price quotes within one trading day are ordered over the trade sequence. The duration between price quotes is measured in minutes and is strictly non-negative. In the majority of cases multiple price quotes occur in one minute. The durations of price quotes after the ﬁrst quote in a minute are set to zero. The resulting time series of price quotes is eﬀectively a non-equally spaced sequence. A nonparametric spline function is estimated through these high-frequency intraday prices. The spline function through a non-equally spaced time series can be represented as a time-varying state state space model, see Durbin and Koopman (2001, section 3.11). To attain an optimal level of smoothing, the “smoothing parameter” of the spline function is estimated via the maximisation of the (quasi) Gaussian loglikelihood function. The spline function itself is computed by the Kalman ﬁlter and an associating smoothing algorithm1. The ﬁve minute nodes of the spline are taken as the “observed” prices Pn,d for d = 0,... ,D. The price Pn,0 is deﬁned as the observed opening price which is the ﬁrst price observed after 9.29 am (even if it takes place at, say, 11.30 am). The closing price Pn,D is then the last price observed before 4.00 p.m. The overnight returns are deﬁned as

Rn,0 = 100(ln Pn,0 − lnPn−1,D), n = 1,... ,N. (3) In this way we have constructed 79 intra-daily returns for the 1,725 trading days in our dataset.

##### 2.2 Realised volatility

It is generally acknowledged that squared daily returns provide a poor approximation of actual daily volatility. It was ﬁrst pointed out by Andersen and Bollerslev (1998) that more accurate estimates could be obtained by summing squared intraday returns. They deﬁned realised volatility in the foreign exchange market as the sum of 288 5-minute squared returns. If we were to apply this method directly to the stock market, realised volatility would be deﬁned as the sum of the squared overnight and the cumulative squared 5-minute intraday returns, so

σ˜n2 = Rn,2 0 +

D

Rn,d2 , n = 1,... ,N, (4)

d=1

with Rn,d and Rn,0 as deﬁned in equations (2) and (3), respectively, and with D = 78. However, this ignores the fact that the overnight return is a special case. Stock markets, unlike foreign exchange markets, are not open 24 hours a day and the changes in the stock index price during the hours that the stock market is closed are relatively large compared to the 5-minute returns observed during trading hours. In order to account for the fact that overnight returns are presumably more volatile than intraday 5-minute returns and that a large value for Rn,0 will have a pronounced and distorting eﬀect on the realised volatility estimate σ˜n2, an alternative realised volatility measures need to be considered by excluding the ”noisy” overnight return Rn,0. This will measure the volatility during trading hours as opposed to daily volatility2. It is suggested by Martens (2002) to scale the sum of intraday returns

[Figure 3]

- 1These computations are carried out using Ox 3.3 (see Doornik (2001)) with use of the SsfPack 3.0 functions SsfGetSpline, SsfLikEx and SsfMomentEstEx (see Koopman, Shephard, and Doornik (1999)).
- 2Andersen and Bollerslev (1997) and Andersen, Bollerslev, Diebold, and Ebens (2001) use this deﬁnition of realised volatility in their stock market studies.

by

σ˜n2 =

σˆoc2 + σˆco2 σˆoc2

[Figure 4]

D

Rn,d2 , (5)

d=1

with the “open-to-close” sample variance σˆoc2 and the “close-to-open” sample variance σˆco2 computed as

N

N

10,000 N

10,000 N

σˆoc2 =

(log Pn,D − log Pn,0)2, σˆco2 =

(log Pn,0 − log Pn−1,D)2.

[Figure 5]

[Figure 6]

n=1

n=1

An alternative sample estimate of the “open-to-close” variance is the average of the realised volatitilies of (4), but without Rn,2 0, from 1 to N as considered by Hansen and Lunde (2002). However, the current proposed estimates σˆoc2 and σˆco2 are consistent with each other since they are both based on sums of N squared returns. An alternative scaling is considered by Areal and Taylor (2002) who assign diﬀerent weights to the intraday squared returns with weights depending on variance proportions. Hansen and Lunde (2003b) provide a more detailed discussion on the choice of scaling.

Other recent methods for the construction of realised volatility include the Fourier method of Malliavin and Mancino (2002), and applied by Barucci and Reno (2002) and Hansen and Lunde (2003a), and the ﬁltering method of Corsi, Zumbach, Mu¨ller, and Dacorogna (2001).

##### 2.3 Implied volatility

The implied volatility index is obtained from the Chicago Board Options Exchange Market Volatility Index3 (VIX) which is based on a highly liquid options market for the period 6 January 1997 to 14 November 2003. The VIX index is calculated from the midpoint of bid-ask option prices using a binomial method as described in Harvey and Whaley (1992) which takes account of the level and timing of dividend payments on the underlying S&P 100 stock index. The Black-Scholes model assumption of constant volatility however introduces bias into the implied volatility measure. Hull and White (1987) found that the magnitude of the bias in the Black-Scholes model was smallest for near-the-money and close-to-maturity options; also see Feinstein (1995). Therefore the index is based on implied volatilities of eight nearby-expiry call and put options4. The VIX index is then constructed as a weighted average of these implied volatilities in such a way that it represents the implied volatility of a hypothetical at-the-money OEX option with twenty-two trading days to expiration. Although the VIX represents a biased implied volatility measure, it is still a useful proxy of future volatility for the practical application of volatility forecasting. It mitigates many of the measurement errors which typically contribute to biased implied volatility measures. The VIX is constructed on a daily basis and is denoted by s2n for n = 1,... ,N.

[Figure 7]

- 3The VIX data was extracted from the CBOE on-line database.
- 4The shortest time to maturity is at least eight days in order to eliminate the increase in implied volatility observed

during the option’s last week of trading. The calendar-day implied volatilities of each of the eight options are adjusted to a trading base as in Fleming, Ostdiek, and Whaley (1995). The wildcard option implicit in the options is ignored as in Fleming and Whaley (1994).

##### 2.4 Descriptive statistics

In Figure 1 we present graphs of the time series that are used in this empirical study together with their histograms and correlograms of the time series. The summary statistics of the series are given in Table 1.

For the daily return series Rn we observe several volatile periods which occurred towards the end of 1997, during the third quarter of 1998, at the beginning and end of 2000 and during the summer of 2002. The three largest shocks to the return process took place in one of these periods and were negative. This largely contributed to the reported negative skewness coeﬃcient for the return series and the large positive skewness coeﬃcient of the squared returns. It is also seen that Rn and Rn2 exhibit excess kurtosis.

Table 1: Summary Statistics of return and volatility time series for the period from 6 January 1997 to 14 November 2003 (number of days is 1,725).

[Figure 8]

daily return realised volatility implied volatility Rn Rn2 σ˜n2 log σ˜n2 s2n log s2n

Mean 0.020 1.889 0.920 −0.612 26.46 3.253 Stand.Dev. 1.374 4.058 1.359 0.981 5.998 0.208 Skewness −0.122 7.918 5.109 0.245 1.266 0.744 Exc.Kurt. 5.621 110.8 39.80 0.524 1.482 0.135 Minimum −8.994 0 0.004 −5.484 16.84 2.834 Maximum 5.702 80.89 15.38 2.733 50.48 3.922

[Figure 9]

The realised volatility series σ˜n2 is presented in Figure 1 in levels (row 3) and logs (row 4). The distribution of the logged realised volatility appears approximately Gaussian but with a fat tail to the left due to one “inlier” in the summer of 1998. The descriptive statistics in Table 1 for realised volatility mirror earlier ﬁndings for stock market data as reported by Andersen, Bollerslev, Diebold, and Ebens (2001), Areal and Taylor (2002) and Giot and Laurent (2004).

The daily implied volatility (VIX) series s2n in levels (row 5) and logs (row 6) are also included in Figure 1 and their summary statistics are reported in Table 1. The eﬀects of some large outliers in the sample are illustrated by high values for skewness and excess kurtosis. Various changes in implied volatility can be observed and they correspond more or less with changes in realised volatilities. However, high volatility periods appear more pronounced in the implied volatility series than in the realised volatility series.

The time series properties are revealed by the sample autocorrelation functions or correlograms which are presented in the third column of the graphs in Figure 1. Positive serial correlation is present in the squared daily return series but is not strong as the volatility dynamics are subject to measurement error. This is reduced considerably for realised volatility and more correlation structure in the series appears as a result, both for levels and logs. Most notably, long memory features are apparent in logged realised volatility. The most persistent correlation structure appears in the implied volatility series.

8

10

0.4

- 0

- 1

0

0.2

1997 1999 2001 2003

−10 −5 0 5

0 20 40

0.50

- 0

- 1

100

0.25

50

1997 1999 2001 2003

0 25 50 75

0 20 40

20

1.0

- 0

- 1

10

0.5

1997 1999 2001 2003

0 5 10 15

0 20 40

0.50

1.0

5

0

0.25

0.5

−5

1997 1999 2001 2003

−5 0

0 20 40

1.0

60

0.10

40

0.5

0.05

20

1997 1999 2001 2003

20 40

0 20 40

4.0

- 1

- 2

- 3

1.0

3.5

0.5

3.0

1997 1999 2001 2003 3.0 3.5 4.0

0 20 40

Figure 1: Six daily time series with observations (ﬁrst column), histogram (second column) and correlogram (third column): (i) daily returns Rn; (ii) squared daily returns; (iii) realised volatility σ˜n2; (iv) realised volatility in logs; (v) implied volatility s2n; (vi) implied volatility in logs. The time series are related to the Standard & Poor’s 100 stock index for the period from 6 January 1997 to 14 November 2003 (1,725 days).

- 3 Realised Volatility Models The spot price of an asset is denoted by P(t) and its return is deﬁned as

R(t) = log P(t) − log P(0), t > 0. (6)

Motivated by ﬁnancial economic theory the dynamic stochastic process of returns can be represented by the continuous time process

dR(t) = µ(t)dt + σ(t)dW(t), t > 0, (7)

where µ(t) is a drift process, σ(t) is the spot volatility and W(t) is a standard Brownian motion process. The drift term µ(t) is included for completeness but will be of no importance below. For the introduction of various volatility models below we further assume that the mean and variance of spot volatility are given by

E σ2(t) = ξ, var σ2(t) = ω2. The actual volatility for the n-th day interval of length h is then deﬁned as

σn2 = σ∗(hn) − σ∗ ((n − 1)h) , where σ∗(t) =

t

σ2(s)ds.

0

##### 3.1 Unobserved components model for realised volatility

It has been argued that realised volatility σ˜n2 is an accurate estimator of actual volatility σn2; see, for example, Andersen and Bollerslev (1998). Barndorﬀ-Nielsen and Shephard (2002) provide an excellent

discussion of the statistical properties of this estimator and its error σn2 − σ˜n2. They also show with a Monte-Carlo study that using a model for the spot volatility σ2(t) can signiﬁcantly improve estimates of actual volatility. A candidate model for σ2(t) is based on the superposition of Ornstein-Uhlenbeck (OU) processes τj(t), that is

J

σ2(t) =

τj(t), dτj(t) = −λjτj(t)dt + dzj(λjt), (8)

j=1

where zj(t) is an independent Le´vy process with non-negative increments (also known as a subordinator) and λj is an unknown ﬁxed parameter for j = 1,... ,J with J as the number of factors. In this case the stochastic diﬀerential equation deﬁning τj(t) permits its autocorrelation function to be expressed as

corr τj(t),τj(t + s) = e−λj|s|.

By assuming E(τj(t)) = wjξ and var(τj(t)) = wjω2, where wj > 0 and wj = 1, a convenient and intuitively appealing form for the autocorrelation function for σ2(t) can be derived and is given by

corr σ2(t),σ2(t + s) =

J

wje−λj|s|.

j=1

where we refer to Barndorﬀ-Nielsen and Shephard (2001, 2002) for more details on this approach to modelling volatility. Using the expression of the autocorrelation corr(τj(t),τj(t + s)) and after some

calculus, it can be shown that the autocorrelation function of the j-th component of actual volatility τnj ≡ ( nhn−1)h τj(t)dt is given by

(1 − e−λjh)2 2(e−λjh − 1 + λjh)

corr(τnj,τnj+m) =

e−λjh(m−1), m = 1,2... ,

[Figure 10]

where h is the length of the day interval. This convenient result implies that τnj permits the ARMA(1,1) representation

τnj+1 = wjξ + φj(τnj − wjξ) + θjηnj−1 + ηnj, ηnj ∼ WN(0,ση2j), (9)

where WN(0,σ2) refers to a white noise process with zero mean and variance σ2. It follows that the autoregressive parameter φj equals e−λjh while Meddahi (2003) shows that

[Figure 11]

1 − 1 − 4ϑ2j 2ϑj

corr(τnj,τnj+1) − φj (1 + φ2j) − 2φjcorr(τnj,τnj+1)

θj =

, with ϑj =

, (10)

[Figure 12]

[Figure 13]

where θj has the typical value of 0.26; see also Barndorﬀ-Nielsen and Shephard (2004b). The key to modelling realised volatility is the set of results in Barndorﬀ-Nielsen and Shephard (2001, section 2.3)

in which they deﬁne the estimation error as un = σn2 − σ˜n2 and, assuming that the return process (7) is valid, they establish it to be a (weak) white noise sequence with mean zero and variance

 (ξh/Dn)2 +

J

σu,n2 = 2Dn

j=1

 , (11)

2wjω2 λ2j

(e−λjh/Dn − 1 + λjh/Dn)

[Figure 14]

where Dn is the number of intra-daily intervals used to calculate σ˜n2. By assuming that the model for spot volatility is correctly speciﬁed, the model for realised volatility is then ﬁnally obtained as

J

σ˜n2 =

τnj + un, τnj ∼ ARMA(1,1), un ∼ WN(0,σu,n2 ), (12)

j=1

which in eﬀect is an unobserved ARMA components (UC) model.

An unobserved ARMA components model can be represented in the state space formulation and methods based on the Kalman ﬁlter can be used for the quasi-maximum likelihood estimation of ﬁxed parameters such as λj and for the signal extraction of spot volatility conditional on realised volatility σ˜n2 which takes account of the implied dynamic structure of spot volatility. More importantly, the model framework allows model-based forecasting of tomorrow’s spot volatility based on the unobserved ARMA components model. It should be noted that the analysis is based on quasi-maximum likelihood estimation because distributional properties for un and ηnj are not established.

##### 3.2 Long memory ARFIMA model

In empirical work on realised volatility it is pointed out that the realised volatility series σ˜n2 can be modelled by a Gaussian dynamic process after it is transformed into logs. The dynamic properties of log realised volatility exhibit features known as long memory, that is, the correlogram decays less

than exponentially as the lag length increases. The correlograms of the realised volatility series in levels and logs are presented in Figure 1 to illustrate that this empirical fact also applies to our S&P 100 dataset. To model the long memory properties, the autoregressive fractionally integrated moving average (ARFIMA) model is adopted following Andersen, Bollerslev, Diebold, and Ebens (2001) and Andersen, Bollerslev, Diebold, and Labys (2003).

The ARFIMA(1,d,1) model with mean µ for realised volatility can be given by

(1 − φL)(1 − L)d(˜σn2 − µ) = (1 + θL)εn, (13)

where L is the lag operator (Lσ˜n2 = σ˜n2−1), coeﬃcients d, φ and θ are ﬁxed and unknown and εn is Gaussian white noise with mean zero and variance σ2. The following restrictions on the parameters apply,

0 < d < 0.5, |φ| < 1, |θ| < 1, σ2 > 0.

In the context of volatility modelling, the ARFIMA model for the logs of realised volatility is empirically investigated, for example, by Andersen, Bollerslev, Diebold, and Labys (2003).

The parameters of the ARFIMA model, including mean µ, can be estimated by the method of maximum likelihood; for details, see, for example, Sowell (1992) and Doornik and Ooms (2003). However, the estimation is not without hurdles. It is, for example, pointed out by Brodsky and Hurvich (1999) and Bos, Franses, and Ooms (2002) that standard ARMA(1,1) models can also capture long memory features and that, depending on the sample spectrum of the data, not all parameters of an ARFIMA(1,d,1) can be empirically identiﬁed from the data. This typically applies to the case of realised volatility. For example, Andersen, Bollerslev, Diebold, and Labys (2003) estimate the d parameter using a log-periodogram estimator and ﬁx d as estimated in their long memory vector autoregressive model of order 1. However, we estimate the d parameter simultaneously with other coeﬃcients of the model. Since diﬀerent ARFIMA model speciﬁcations produce rather similar results, we consider the ARFIMA(1,d,0) model in the empirical study5.

Forecasting can be carried out by extrapolating the series in which the correlation structure implied by the estimated ARFIMA model is taken into account. Details of how these computations can be implemented elegantly for ARFIMA models are given by Doornik and Ooms (2003).

#### 4 Daily Time-Varying Volatility Models

In this section we discuss daily time-varying volatility models where volatility is explicitly modelled as the second moment of daily returns. This class of so-called historical volatility models is wellestablished and includes stochastic volatility (SV) and generalised autoregressive conditional heteroskedasticity (GARCH) classes of models. In addition to standard formulations we also consider extensions to both models with realised and implied volatility measures incorporated in the variance equation.

[Figure 15]

5The required computations are implemented using the ARFIMA package of Doornik and Ooms (2001) within the programming environment of Ox; see Doornik (2001).

##### 4.1 Stochastic volatility model

The stochastic volatility model is deduced from the continuous time process for the returns (6). By discretising the continuous process (7) at daily intervals and by assuming an autoregressive process for log-volatility, we obtain the stochastic volatility model for daily returns as given by

Rn = µ + σnεn, εn ∼ NID(0,1), n = 1,... ,N, σn2 = σ∗2 exp(hn),

(14)

hn+1 = φhn + σηηn, ηn ∼ NID(0,1), h1 ∼ NID(0,ση2/{1 − φ2}),

where Rn is computed as in equation (1) and constant µ is treated as ﬁxed and zero in our empirical study. The choice of a ﬁrst-order autoregressive process for the daily log-volatility hn is common. Note that some weak serial correlation in Rn2 exists as conﬁrmed by the ﬁrst correlogram of Figure 1. The actual volatility σn2 is modelled by the product of a scaling factor σ∗2 > 0 and the exponential of the stochastic process hn. The persistence parameter φ of the autoregressive process is restricted to be positive and smaller than one to ensure stationarity. We further assume that εn and ηn are mutually uncorrelated, contemporaneously and at all lags, and with h1. More theoretical details about the SV model are discussed by Shephard (1996).

The nonlinear relation between the unobserved log-volatility hn and the observed dependent variable Rn does not allow the computation of the likelihood by linear methods such as the Kalman ﬁlter. However, the likelihood function of the SV model can be constructed using simulation methods such as the ones developed by Shephard and Pitt (1997) and Durbin and Koopman (1997). These developments allow the exact maximum likelihood estimation of parameters of the SV model using Monte Carlo importance sampling techniques, see also Sandmann and Koopman (1998).

For the SV model we can express the likelihood function as

L(ψ) = p(y|ψ) = p(y,θ|ψ)dθ = p(y|θ,ψ)p(θ|ψ)dθ, (15)

where y = (y1,... ,yN)′ and

ψ = (φ,ση,σ∗)′, θ = (h1,... ,hN)′.

An eﬃcient way of evaluating such expressions is by using importance sampling; see Ripley (1987, Chapter 5). A simulation device is required to sample from an importance density p˜(θ|y,ψ) which we prefer to be as close as possible to the true density p(θ|y,ψ). It is common to take a conditional Gaussian density g(θ|y,ψ) as the importance density since it is relatively straightforward to sample from it using simulation smoothers such as the ones developed by de Jong and Shephard (1995) and Durbin and Koopman (2002). Guidelines for the construction of Gaussian importance sampling devices for the SV model are discussed in Lee and Koopman (2003). It can be shown that the Monte Carlo estimate of the likelihood function can be computed as

Lˆ(ψ) = LG(ψ)D−1

D

p(y|θj,ψ) g(y|θj,ψ)

dj, dj =

,

[Figure 16]

j=1

where θj is a draw (realisation) of g(θ|y,ψ) as obtained from the simulation smoother for j = 1,... ,D. The likelihood function can be computed for a given value of parameter vector ψ and can be numerically

maximised with respect to ψ by using the same source of random deviates for computing Lˆ(ψ) for the diﬀerent values of ψ. In this way maximum likelihood estimates of ψ are obtained6. The one-step ahead daily volatility forecast for the SV model is computed as

σˆN2 +1 = σˆ∗2 exp(hˆN+1|N + 0.5pN+1|N), (16)

where σˆ∗2 is the maximum likelihood estimate of σ∗2, ˆhN+1|N is the estimator of hN+1 given all N observed daily returns and pN+1|N is its mean squared error. The latter two values are computed by

djhN+1|N(θj) j dj

djpN+1|N(θj) j dj

hˆN+1|N = j

, pN+1|N = j

,

[Figure 17]

[Figure 18]

where hN+1|N(θj) and pN+1|N(θj) are obtained from the Kalman ﬁlter applied to the approximating model that is used as part of the Gaussian importance sampling device and is based on the draw θj from g(θ|y,ψ). Further details of this approach are discussed in Durbin and Koopman (2000).

The SV model can be extended by the inclusion of an explanatory variable in the log-variance equation for hn in (14), that is

hn = φhn−1 + γ(1 − φL)xn−1 + σηηn, n = 1,... ,N, (17)

where xn = lnσ˜n2 for realised volatility or xn = lns2n for implied volatility. An equivalent speciﬁcation for model (17) is given by

hn = γxn−1 + ηn∗, ηn∗ = φηn∗−1 + σηηn,

which is a regression model with autoregressive disturbances. Although φ is restricted to be positive for model (14), for model (17) the standard stationary condition −1 < φ < 1 applies. For other volatility models, similar extensions have been considered, see Martens (2001) and Blair, Poon, and Taylor (2001), amongst others. Replacing the equation (17) for hn in (14) does not aﬀect the nonlinear relationship between daily return Rn and unobserved volatility hn. Therefore the estimation and forecasting methods for the SV model as described earlier can be applied straightforwardly. The regression coeﬃcient γ in (17) is estimated by numerically maximising the simulated likelihood function with respect to γ and jointly with respect to the other coeﬃcients. One-step ahead forecasts for the extended model are obtained using the same methods as for the SV model although it requires the value of xN.

##### 4.2 Generalised autoregressive conditional heteroskedasticity model

An alternative to the SV model and more common in its use of modelling time-varying volatility is the generalised autoregressive conditional heteroskedasticity (GARCH) model which in its most simplest form is given by

Rn = σnεn, εn ∼ NID(0,1), n = 1,... ,N, σn2 = ω + αRn2−1 + βσn2−1,

(18)

[Figure 19]

6The SV model is estimated using a program written in the Ox language of Doornik (2001) using SsfPack by Koopman, Shephard, and Doornik (1999). The Ox programs can be obtained from http://staff.feweb.vu.nl/koopman/sv/.

with parameter restrictions ω > 0, α ≥ 0, β ≥ 0 and α + β < 1. The parameter vector ψ consists of ω, α and β in this case. The persistence of daily volatility is measured by α + β in GARCH models. More lags of Rn2 and σn2 can be added to the volatility equation of the GARCH model but in empirical studies the model (18) has proven to work eﬀectively in forecasting volatility, see, for example, Andersen and Bollerslev (1998) and Hansen and Lunde (2003b). The time-varying variance is formulated conditional on the lagged observed return Rn−1 and therefore the variance σn2 is known conditional on past observed returns and parameter vector ψ. The predictive observation density is given by

Rn+1|R1,... ,Rn,ψ ∼ NID(0,ω + αRn2 + βσn2). The prediction error decomposition allows the construction of the likelihood function in a straightforward way, see Bollerslev (1986). When the assumption of normality for εn is droppped, estimation can be referred to as quasi-maximum likelihood. Estimation procedures for the GARCH model are implemented in many standard econometric software packages7. Interesting surveys on GARCH models are written by Bollerslev, Chou, and Kroner (1992), Bera and Higgins (1993) and Bollerslev, Engle, and Nelson (1994). Finally it follows directly that the one-day ahead volatility forecast at time N can be computed as

σˆN2 +1 = ωˆ + αRˆ N2 + βˆσˆN2 , (19) where ωˆ, αˆ and βˆ denote maximum likelihood estimates of ω, α and β, respectively.

The daily GARCH model can also be extended to include an explanatory variable by incorporating it in the variance equation, so the volatility process σn2 in equation (18) can be rewritten as

σn2 = ω + αRn2−1 + βσn2−1 + γs2n−1, (20)

where s2n represents implied volatility but can be exchanged with realised volatility σ˜n2. We note that the inclusion of s2n in the volatility equation (20) is diﬀerent from its inclusion in (17) and therefore the regression coeﬃcients have diﬀerent implications for forecasting. Most econometric packages have options to specify explanatory variables for the volatility equation (20) because estimation of these coeﬃcients is relatively straightforward. As for the standard GARCH model, all information for the calculation of the one-day ahead volatility forecast σˆN2 +1 is available at time N and is given by

σˆN2 +1 = ωˆ + αRˆ N2 + βˆσˆN2 + γsˆ 2N, (21) where γˆ is the maximum likelihood estimate of γ.

#### 5 Forecasting methodology

In the next section the results are presented of an out-of-sample forecasting study in which we compare the forecasting performances of the various volatility models described in sections 3 and 4. This forecasting study is carried out as follows. The volatility models are estimated 525 times based on 525 samples of 1,200 observations. The ﬁrst sample starts 6 January 1997 and ends 16 October 2001. A forecast of volatility is generated for 17 October 2001 based on the estimated model for the

[Figure 20]

7In this paper a program for estimating the parameters of the GARCH model is written in Ox, the programming environment of Doornik (2001), using functions of the G@RCH package of Laurent and Peters (2002).

ﬁrst sample. The second sample, starting 7 January 1997 and ending 17 October 2001, is used to forecast the volatility of 18 October 2001 based on the estimated model for the second sample. These estimation and forecasting steps can be repeated 525 times for the available sample from 6 January 1997 to 14 November 2003. More speciﬁcally, we produce the 525 one-day ahead forecasts σˆm2 where

σˆm2 is forecast of σm2 based on information Rm−1200,... ,Rm−1,ψ,ˆ (22)

for m = N +1,... ,N +M and ψˆ refers to the maximum likelihood estimate of the parameter vector ψ. In the case of realised volatility models the conditioning also refers to the intraday returns associated with trading days m = N + 1,... ,N + M. The range of the day index m reﬂects the period from 17 October 2001 to 14 November 2003. The forecasts are based on a “rolling window” procedure: in each case the sample is rolled forward by one trading day while the size of the sample is kept constant at 1,200.

The volatility is not observable and as a result the forecast error is also not observable. It is

argued earlier that realised volatility (5), denoted by σ˜m2 , is an accurate estimator and therefore σ˜m2 is the variable to forecast for m = N + 1,... ,N + M. The volatility forecast obtained from model

Mk is denoted by σˆk,m2 and is deﬁned as in (22). It is diﬃcult to determine whether, say, model M1 outperforms model M2. This is a subjective matter that depends on the choice of a criterion. Various forecasting criteria can be considered to assess the predictive accuracy of a volatility model. In this paper we use the following accuracy statistics or loss functions for a particular model Mk:

The squared error L1,k,m = (˜σm2 − σˆk,m2 )2,

The absolute error L2,k,m = |σ˜m2 − σˆk,m2 |,

The squared error adjusted for heteroskedasticity L3,k,m = (1 − σ˜k,m−2 σˆm2 )2,

The absolute error adjusted for heteroskedasticity L4,k,m = |1 − σ˜k,m−2 σˆm2 |. Some of these loss functions are also considered by Andersen, Bollerslev, and Lange (1999), Martens

(2002) and Hansen and Lunde (2003b).

When a particular loss function is smaller for model M1 than for model M2, say, we can clearly not conclude that the forecasting performance of model M1 is superior to that of model M2. Such a conclusion can not be made on the basis of just one criterion and just one sample. Recent work has focused on a testing framework for determining whether a particular model is outperformed by another model, see, for example, Diebold and Mariano (1995), West (1996) and White (2000). A further development of the White framework is known as the Superior Predictive Ability (SPA) test and is proposed by Hansen (2001) where it is also shown that SPA has good power properties and is robust. We adopt the SPA test to investigate the relative performance of various volatility models. A similar study is carried out by Hansen and Lunde (2003b) for a range of daily volatility models, mainly variants of GARCH models. In this study we focus on the comparison of the forecast abilities of models based on high-frequency measures of volatility and models based on daily returns.

We consider K + 1 diﬀerent models Mk for k = 0,1,... ,K and which are discussed in sections

- 3 and 4. For each model Mk we generate M volatility forecasts σˆm,k2 for m = N + 1,... ,N + M. For every forecast we calculate the loss function Li,m,k as given above with i = 1,... ,4. A particular

model M0 is taken as the benchmark model. The loss function relative to the benchmark model is deﬁned as

Xk,m ≡ Li,0,m − Li,k,m, (23) for some choice of loss function i. The unobserved actual volatility σm2 is the object of forecasting while realised volatility σ˜m2 is taken as its proxy for assessing the relative forecast accuracy of models. Hansen and Lunde (2003a) argue that the use of a proxy may lead to inconsistencies in the comparison of models with respect to forecast accuracy. Consistency requires moment conditions and dependence structures for relative forecast losses Xk,m. These conditions are weak and likely to be fulﬁlled for at least L1,k,m and L2,k,m. Further, the results in Hansen and Lunde (2003a) imply that the inconsistencies are proportionate with the precision of the proxy. The results in Barndorﬀ-Nielsen and Shephard (2002) support the fact that realised volatility is a precise estimator of actual volatility. Assuming that models can be ranked consistenly, λk ≡ E(Xk,m) is well deﬁned. When the benchmark or base model M0 outperforms all other models, we have λk < 0 for all models k = 1,... ,K. Therefore the base model is not outperformed when it rejects the null hypothesis

λk ≤ 0. (24) The associated test statistic proposed by Hansen (2001) is given by

max

k=1,...,K

√MX¯k ωˆkk

[Figure 21]

T = max

, (25)

[Figure 22]

k=1,...,K

with ωˆkk2 as a consistent estimate of ωkk2 and where

X¯k =

N+M

1 M

Xk,m, ωkk2 = lim

var(

[Figure 23]

M→∞

m=N+1

√

MX¯k). (26)

[Figure 24]

A consistent estimator of ωkk and the p-value of test statistic T can be obtained via a bootstrap procedure that is outlined below.

We apply the stationary bootstrap of Politis and Romano (1994) to compute the test statistic T and to assess its distributional properties. This procedure consists of building new samples for Xk,m of length M which are constructed by randomly choosing subsamples of diﬀerent lengths and putting these together. The lengths of the subsamples are independent and are drawn from a geometric distribution with mean q. The random lengths are ideally small but suﬃciently large to reﬂect the serial dependence in the Xk,m series. After the inspection of correlograms of Xk,m for diﬀerent models Mk we have taken q = 0.5. The resulting bootstrap samples for Xk,m are denoted by Xk,mi and we consider B bootstraps, i = 1,... ,B. The empirical distribution implied by the bootstrap samples is taken as the distribution that has generated Xk,m. For each bootstrap the sample mean is computed as

M

1 M

X¯ki =

Xk,mi , i = 1,... ,B. (27)

[Figure 25]

m=1

The variation within these bootstrapped means is taken as the estimator of ωkk, that is

1 B

ωˆkk =

[Figure 26]

B

1 B

(X¯ki − X¯k)2, X¯k =

[Figure 27]

i=1

B

X¯ki. (28)

i=1

The bootstrap estimate of ωkk allows the computation of the test statistic T in (25). Finally, the distribution of T under the null hypothesis can be empirically identiﬁed as follows. Deﬁne Z¯ki as

Z¯ki = X ¯ki − X¯k × 1{X¯

k>−Ak}, (29) where Ak = 14M−4ωˆkk and 1{·} is an indicator function. The empirical distribution of

[Figure 28]

√MZ¯ki ωˆkk

[Figure 29]

Ti = max

, (30)

[Figure 30]

k=1,...,K

converges to the distribution of T under the null hypothesis; see Hansen (2001) for more details. It follows directly that the p-value of T can be empirically identiﬁed as

B

1 B

1{Ti>T}. (31)

[Figure 31]

i=1

More details of this procedure are detailed in Hansen (2001) and Hansen and Lunde (2003b).

#### 6 Empirical Results

##### 6.1 Parameter estimation

The estimation results obtained from realised and historical volatility models as described in sections

- 3 and 4, respectively, are presented in Table 2. The results are based on observations from the full sample period 6 January 1997 to 14 November 2003. All models indicate high persistency in volatility dynamics as it is expected from stock index prices. Unobserved ARMA component models (UC-RV)

are estimated with one (UC-RV1) and two (UC-RV2) factors. The coeﬃcients µ, φ1, φ2, ση21 and ση22 are estimated and standard errors are provided while the coeﬃcients σu2, θ1 and θ2 are functions of the estimated coeﬃcients as is apparent from equations (10) and (11). The ARMA factor in UC-RV1 with autoregressive coeﬃcient 0.45 and moving average coeﬃcient 0.26 does not imply the persistent dynamic structure as indicated by the sample correlogram of realised volatility σ˜n2 given in Figure 1. However, a higher level of volatility persistency is obtained when two ARMA factors are considered. The second factor in UC-RV2 has a higher persistency with autoregressive coeﬃcient 0.98. The loglikelihood function is larger for the two factor UC-RV2 model than for the one factor UC-RV1 model which is conﬁrmed by a lower Akaike criterion (AIC) value for UC-RV2. More ARMA factors have also been considered but two factors have proved to be suﬃcient for this dataset. Both UC-RV models are successfull in capturing the dynamics in the series given the relatively small values of the Box-Ljung Q statistics.

The fractional integration parameter of the ARFIMA model is estimated as 0.408 for realised volatility in levels and as 0.478 for logged realised volatility. In the latter case, the d estimate exceeds the estimate found by Andersen, Bollerslev, Diebold, and Labys (2003) who report the value 0.441. It should be noted that this and related studies employ diﬀerent ARFIMA model speciﬁcations, diﬀerent estimation methods and diﬀerent datasets8. Further, in the case of logged realised volatility,

[Figure 32]

8Andersen, Bollerslev, Diebold, and Labys (2003) do not estimate the fractional parameter but obtain the d value from a prior analysis and ﬁx it for the estimation of the other parameters in their vector autoregressive fractional model for three exchange rates.

the process may not be covariance-stationary as the estimate of d is close to the boundary value of 0.5. Some evidence of nonstationarity is also found in the high persistency implied by the second ARMA component in the UC-RV2 model. From these in-sample results we may conclude that a parsimonious and eﬀective description of the dynamics in the S&P 100 realised volatility is provided by the ARFIMA(1,d,0) model. The dynamics of realised volatility seem to be best captured by the ARFIMA model since it has the lowest Box-Ljung test statistic. The ARFIMA log-likelihood value and AIC for logged realised volatility can not be compared with the other realised volatility models since it refers to diﬀerent values of the dependent variable. The Box-Ljung statistic is the highest for the log ARFIMA model but this is probably due to the fact that logged series have usually less atypical observations (outliers). Aberrant observations in a time series have a destructive eﬀect on the serial correlation structure.

Volatility persistency for the historical SV and GARCH models are estimated as statistically signiﬁcant and close to unity with φˆ = 0.967 and αˆ + βˆ equal to 0.963 which conﬁrms earlier ﬁndings in the literature with regard to daily stock index return series. The estimated SV model with a higher log-likelihood value is preferred since it indicates a better ﬁt compared to the GARCH model. However, one should be careful in comparing likelihood values since the involved computations for SV and GARCH models are very diﬀerent and models are non-nested9.

The inclusion of the realised volatility series in the volatility equation of the SV model has a signiﬁcant eﬀect on the ﬁt of the model as is shown by a decrease of 27.8 in the AIC value and by the signiﬁcance of the estimated regression coeﬃcient γ. The estimate of the persistence parameter φ has not changed signiﬁcantly. The change in the estimated values for σ∗2 and ση2 can be explained by the necessary rescaling due to the inclusion of the regression variable log σ˜n2. Similar conclusions can be made for the inclusion of implied volatility in logs, that is log s2n, in the log-volatility equation of the SV model. However the eﬀect is even stronger since the AIC decreases by 37.8 in relation to the standard SV model. Also the regression coeﬃcient is more signiﬁcant compared to the signiﬁcance of γ in the realised volatility case. Therefore the SV model with implied volatility in the volatility equation may be preferred based on these in-sample results.

The estimation results for the GARCH model are typical for stock index series and can be found elsewhere in the literature. It is noticable that within the GARCH framework, the inclusion of realised or implied volatility as explanatory variables for volatility has a large impact, larger than in the SV case. The AIC value decreases by 61.6 and 64.6 for the two volatilities. Also in both cases the regression coeﬃcients are signiﬁcant. However, the inclusion of these regressors diminishes the persistency of the volatility dynamics. The estimated coeﬃcient β remains signiﬁcant in both cases. In the case where implied volatility is included, the estimated α coeﬃcient is not signiﬁcant. This case implies that the daily (squared) returns do not play a role in the estimation of σn2 which in fact only depends on past values of implied volatilities, that is

∞

βˆj−1s2n−j.

σˆn2 = γˆ

j=1

[Figure 33]

9The estimation results for the GARCH model conﬁrm the empirical results of Blair, Poon, and Taylor (2001) who examine Standard & Poor’s 100 stock index returns over the earlier 1987 to 1992 period and ﬁnd values for γ similar to ours. In contrast, Martens (2002) reports on much smaller and statistically insigniﬁcant γ estimates for returns on Standard & Poor’s 500 futures, see also Taylor and Xu (1997).

19

Table 2: Estimation results of realised and historical volatility models using the Standard & Poor 100 stock index data set for the period 6 January 1997 to 15 November 2003

[Figure 34]

[Figure 35]

[Figure 36]

model UC ARMA model ARFIMA model Stochastic volatility model GARCH model UC-RV1 UC-RV2 level log with RV with IV with RV with IV

[Figure 37]

[Figure 38]

[Figure 39]

[Figure 40]

[Figure 41]

[Figure 42]

[Figure 43]

[Figure 44]

[Figure 45]

[Figure 46]

[Figure 47]

[Figure 48]

[Figure 49]

[Figure 50]

[Figure 51]

[Figure 52]

µ 0.955 0.953 0.813 −.797 σ∗2 1.473 1.775 0.040 α 0.102 −.047 0.016

[Figure 53]

[Figure 54]

[Figure 55]

[Figure 56]

[Figure 57]

0.058 0.224 0.779 1.434 0.180 0.166 0.024 0.010 0.019 0.017

- φ1 0.451 0.422 0.051 −.109 φ 0.967 0.964 0.934 β 0.861 0.448 0.252 0.025 0.130 0.040 0.031 0.011 0.018 0.029 0.016 0.070 0.103

[Figure 58]

[Figure 59]

[Figure 60]

[Figure 61]

[Figure 62]

[Figure 63]

[Figure 64]

[Figure 65]

[Figure 66]

[Figure 67]

- φ2 0.976 γ 0.279 1.127 γ 0.908 0.126 0.009 0.053 0.181 0.113 0.018

[Figure 68]

[Figure 69]

[Figure 70]

[Figure 71]

[Figure 72]

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

d 0.408 0.477

[Figure 83]

[Figure 84]

[Figure 85]

[Figure 86]

[Figure 87]

0.031 0.020

- ση21 1.103 0.030 ση2 0.026 0.014 0.028 ω 0.075 0.312 −2.000 0.040 0.012 0.008 0.007 0.012 0.017 0.065 0.284

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

- ση22 0.439 0.079

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

σu2 1.002 1.003 1.069 0.489

- θ1 0.259 0.257

[Figure 113]

[Figure 114]

[Figure 115]

[Figure 116]

[Figure 117]

- θ2 0.268

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

lnL −2616.3 −2506.4 −2506.1 −1834.86 −2876.3 −2861.2 −2856.2 −2895.1 −2833.5 −2830.5 AIC 5238.6 5022.7 5018.3 3675.72 5758.2 5730.4 5720.4 5796.3 5675.0 5669.0 Q(12) 14.14 14.02 12.28 20.01 22.05 22.19 20.61 17.36 20.11 18.14

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

Parameter estimates are reported together with asymptotic 95% standard errors which are obtained using the delta method since some coeﬃcients are transformed for estimation. The Akaike information criterion AIC is calculated as -2(ln L) + 2p where p is the number of coeﬃcients that is estimated. The Box-Ljung portmanteau statistic Q(ℓ) is for the observation errors and is asymptotically χ2 distributed with ℓ degrees of freedom.

Here β is estimated as βˆ = 0.25 implying that eﬀectively only s2n−1 and, to a smaller extent, s2n−2 determine σˆn2.

- 6.2 Some forecasting results Volatility forecasts are constructed for realised and historical volatility models as described in section

- 5. The evaluation period ranges from 17 October 2001 to 14 November 2003. In this period, for each trading day n a volatility forecast is generated for each considered model which is estimated using information from the last 1,200 days (n − 1,... ,n − 1200). The one-step ahead forecasts for the evaluation period are presented in Figure 2 together with realised volatility (displayed as dots). Some interesting aspects of the forecast results can be observed since in this sample a small group of days displays high volatility while most other days have low volatility. The GARCH and SV forecasts are clearly biased when volatility is low. The GARCH forecasts are also too high for days when volatility is relatively high. The positive and persistent forecast bias may be explained from the fact that the GARCH and SV forecasts are extracted from daily returns that are subject to measurement noise. The volatility estimates are not corrected for this measurement variance and therefore the forecast bias is positive. In contrast, the realised volatility models appear to produce forecasts without positive forecast bias. The log ARFIMA-RV forecasts are clearly the least sensitive to jumps in volatility.

15 2002 2003

10

5

15 2002 2003

10

5

15

15

10

10

5

5

- Figure 2: One-day ahead volatility forecasts from (i) GARCH, (ii) SV, (iii) UC-RV2 and (iv) log ARFIMA-RV models for the period between 17 October 2001 and 14 November 2003 (525 days).

Table 3 presents the forecast accuracy statistics that consist of the means of four loss functions: L1,k,m, mean squared error (MSE); L2,k,m, mean absolute error (MAE); L3,k,m, heteroskedastic adjusted MSE (HMSE); L4,k,m, heteroskedastic adjusted MAE (HMAE)10. In terms of MSE, the UC-RV2

[Figure 144]

10For example, we deﬁne the MSE for model Mk by M−1 m N+=MN+1 L1,k,m.

and ARFIMA-RV models produce the smallest values for this sample. In terms of the other criteria, the log ARFIMA-RV and UC-RV2 models produce the smallest values. The heteroskedastic corrected versions of MSE and MAE give relatively less weight to forecast errors associated with high values of realised volatility while the MSE give relatively more weight to these errors. Therefore both of these statistics are of interest on their own merits. In case of value-at-risk applications, one may be more interested in the accurate forecasting of high volatility rather than low volatility. This implies that the MSE criterion is the relevant loss function for applications in risk management.

Realised volatity models provide more accurate forecasts compared to the historical SV and GARCH models that are based on daily returns. Within the group of historical models, the SV model with either realised or implied volatility as an explanatory variable for volatility is providing the most accurate forecasts. This holds when considering the diﬀerent loss functions. The accuracy of GARCH forecasts vary but overall their forecasts are less accurate. Within the group of realised volatility models, their is a clear distinction in accuracy. For the MSE loss function, the ARFIMA-RV and UC-RV2 models produce the smallest values while for the other loss functions, the log ARFIMARV model clearly outperforms the other models in forecasting accuracy.

For completeness we also report the goodness-of-ﬁt measure R2 for regressing σ˜m on a constant and the volatility forecast σˆm for m = N + 1,... ,N + M. This so-called Mincer-Zarnowitz regression is used in many volatility forecast studies. The goodness-of-ﬁt statistics conﬁrm the earlier conclusions although the GARCH and SV models produce relatively high R2 values, especially the GARCH model with realised volatility. This can be explained from the fact that the R2 measure corrects for the bias in forecast errors since it compares the total ﬁt of the Mincer-Zarnowitz regression with the sum of squared mean deviations of forecast errors. Therefore it shows that the pattern of one-step ahead forecasts obtained from the GARCH model with realised volatility is close to the pattern of volatility itself. The realised volatility models however produce overall the highest R2 values. These results conﬁrm similar ﬁndings reported in Andersen, Bollerslev, Diebold, and Labys (2003) for exchange rate data.

Finally, to get some insight in how forecasts evolve over time in our study, in Figure 3 we have zoomed in on the one-step ahead forecasts between 9 September 2002 and 18 November 2002 (51 trading days). The forecasts of GARCH and SV respond slowly to the changes from high to low and from low to high volatility. The forecasts of these models are obtained from weighted averages of past squared returns with relatively long exponentially declining weight patterns. This may explain the slow response of the forecasts to changes in volatility and, together with the volatility measurement error in daily squared returns, it may provide an explanation for the relatively poor performance of historical models in volatility forecasting. The inclusion of realised volatility shows an improvement in both the GARCH and SV model. Especially in the latter case it can be observed from Figure 3 that the forecasts are more responsive to changes in volatility. The positive forecast bias is reduced when volatility is low and it produces more accurate forecasts when volatility is high.

In the case of realised volatility models it is shown that the more successfull models in forecasting are the ones that produce a smoother series of forecasts (UC-RV2 and log ARFIMA-RV). It is surprising to notice that relative smooth forecast patterns are a virtue in forecasting volatility.

- Table 3: Out-of-sample forecasting criteria (evaluated against σ˜m2 ) for the Standard & Poor’s 100 evaluation period 17 October 2001 to 14 November 2003

[Figure 145]

Model Mk Forecast loss functions

[Figure 146]

MSE MAE HMSE HMAE R2 UC-RV1 1.248 0.613 2.495 1.240 0.522 UC-RV2 0.996 0.505 1.546 0.792 0.593 ARFIMA-RV 0.991 0.508 1.610 0.813 0.598 ARFIMA-RV (log) 1.149 0.472 1.030 0.555 0.597

[Figure 147]

[Figure 148]

[Figure 149]

[Figure 150]

[Figure 151]

[Figure 152]

[Figure 153]

SV 2.433 1.240 5.080 2.948 0.386 SV RV 2.256 1.037 3.368 2.063 0.437 SV IV 3.132 1.082 3.422 2.048 0.343 GARCH 2.837 1.348 5.339 3.174 0.405 GARCH RV 3.134 1.228 4.603 2.738 0.605 GARCH IV 2.872 1.297 5.079 2.720 0.419

[Figure 154]

[Figure 155]

[Figure 156]

[Figure 157]

[Figure 158]

The MSE for model Mk is deﬁned as M−1 m N+=MN+1 L1,k,m. In a similar way, MAE (based on L2,k,m), HMSE (based on L3,k,m) and HMAE (based on L4,k,m) are deﬁned. The goodness-of-ﬁt R2 statistic is based on the OLS regression applied to σ˜m = a + bσˆm + um where a and b are regression coeﬃcients and with realised volatility σ˜m, forecast σˆm as deﬁned in (22) and error um for m = N + 1, ...,N + M and M = 525. In a similar forecasting context, these so-called Mincer-Zarnowitz regressions are also carried out by Andersen, Bollerslev, Diebold, and Labys (2003).

- 5.0

7.5

Sep 2002 Nov 2002

2.5

5.0

7.5

Sep 2002 Nov 2002

2

4

- 6

2.5

6

4

2

- Figure 3: Realised volatility (as dots) and one-day ahead volatility forecasts from (i) GARCH (solid) and GARCH with RV (dashed), (ii) SV (solid) and SV with RV (dashed), (iii) UC-RV1 (solid) and UC-RV2 (dashed) and (iv) ARFIMA-RV (solid) and log ARFIMA-RV (dashed) models for the period between 9 September 2002 and 18 November 2002 (day 225 to 275).

##### 6.3 Superiority prediction tests

Although the forecasting results have clearly shown that the ARFIMA model for logged realised volatility is the best model for prediction and that the SV model with realised volatility as an explanatory variable in the volatility equation produces the best forecasts within the class of historical volatility models. However, these results only apply to one selected sample. To assess whether the same outcomes are obtained for similar samples, we need to apply the methodology of White (2000) and Hansen (2001) as discussed in section 5. The computation of superior predictive ability (SPA) test

- (25) requires the stationary bootstrap of loss series Li,k,m over the sample m = N + 1,... ,N + M for a speciﬁc loss function i and for a range of models Mk with k = 0,... ,K. Computing X¯k in equation
- (26) is based on the actual forecasts while computing ωˆkk in equation (28) requires the bootstraps. The computation of the p-values as in (31) also requires the bootstraps.

Tables 4 and 5 present the SPA results for the two classes of volatility models. The individual X¯k is reported for each model that is considered as a base model M0 while the remaining models are treated as rival models Mk. All considered models in this study are consecutively taken as base models. Further, the various statistics are reported for the four diﬀerent loss functions. As a result, and in the way the X¯k statistics are presented, the tables (apart from the last column) consist of four blocks of skewed symmetric matrices. The last columns of Tables 4 and 5 report the p-values of the SPA tests for each considered base model. A high p-value rejects the null hypothesis (24) of ”no superiority” of the base model. The earlier forecast results have seen a large diﬀerence in forecast accuracy of historical and realised volatility models. Therefore the SPA results are presented separately for these two classes of models.

In Table 4 the SPA results for the realised volatility models are presented. The average of daily squared forecast error diﬀerences between UC-RV1 and UC-RV2 models is 2.21, which means that the squared forecast error of UC-RV1 was on average higher than of UC-RV2. The average values for UC-RV1 in relation to the rival ARFIMA and log ARFIMA models are 2.39 and 1.15, respectively. This result is not good for UC-RV1 as is also reﬂected by its p-value of zero for the SPA test. Overall

- Table 4 shows that for all loss functions, the UC-RV2 and ARFIMA models are very close in their good forecasting performance. However, the log ARFIMA model is clearly the preferred model when we

rely on the loss functions L2, L3 and L4. This is particularly noticable when we consider the p-value of the SPA test. For the last three loss functions its p-value is unity implying it is superior to all other models that are considered. The ﬁrst loss function (squared forecast error) however shows that ARFIMA and UC-RV2 forecasts are to be preferred which conﬁrms the earlier ﬁndings from Table 3.

Finally, in Table 5 the results are even more dramatic in its clarity. For all loss functions it can be concluded that forecasts from the SV class of models are to be preferred. Overall the SV model with logged realised volatility as an explanatory variable for log-volatility is the outstanding model within its class.

These forecasting results show the importance of realised volatility as a predictor of future volatility. We conﬁrm the ﬁndings of Christensen and Prabhala (1998), Fleming (1998), Blair, Poon, and Taylor (2001) and Giot (2003) that forecasts of volatility extracted from models for daily returns are less accurate than forecasts based on implied volatility. However, in this study we have found that models based on realised volatility outperform models with implied volatility when forecasting the volatility in the S&P 100 index series. The importance of realised volatility for forecasting is also found by

- Table 4: Superior predictive ability (SPA) test λk for realised volatility models and the Standard & Poor’s 100 evaluation period 17 October 2001 to 14 November 2003

[Figure 159]

Loss Base model Alternative models UC-RV1 UC-RV2 ARFIMA ARF.log p-value T∗

[Figure 160]

[Figure 161]

[Figure 162]

[Figure 163]

[Figure 164]

MSE UC-RV1 – 2.21 2.39 1.15 0.028 UC-RV2 −2.21 – 0.38 −0.99 0.564 ARFIMA −2.39 −0.38 – −1.07 1† ARFIMA log −1.15 0.99 1.07 – 0.197

[Figure 165]

[Figure 166]

[Figure 167]

[Figure 168]

[Figure 169]

[Figure 170]

[Figure 171]

[Figure 172]

[Figure 173]

MAE UC-RV1 – 7.05 7.28 9.08 0.000 UC-RV2 −7.05 – −0.79 1.58 0.053 ARFIMA −7.28 0.79 – 2.20 0.019 ARFIMA log −9.08 −1.85 −2.20 – 1†

[Figure 174]

[Figure 175]

[Figure 176]

[Figure 177]

[Figure 178]

[Figure 179]

[Figure 180]

[Figure 181]

[Figure 182]

HMSE UC-RV1 – 2.80 2.97 2.89 0.011 UC-RV2 −2.80 – −1.21 3.05 0.007 ARFIMA −2.97 1.21 – 2.63 0.023 ARFIMA log −2.89 −3.05 −2.63 – 1†

[Figure 183]

[Figure 184]

[Figure 185]

[Figure 186]

[Figure 187]

[Figure 188]

[Figure 189]

[Figure 190]

[Figure 191]

HMAE UC-RV1 – 7.96 7.82 8.78 0.000 UC-RV2 −7.96 – −2.64 8.84 0.000 ARFIMA −7.82 2.64 – 8.64 0.000 ARFIMA log −8.78 −8.84 −8.64 – 1†

[Figure 192]

[Figure 193]

[Figure 194]

[Figure 195]

[Figure 196]

[Figure 197]

A positive value in column of an alternative model Mk indicates it is superior to the base model according to a speciﬁc loss function. Final column has p-value of T∗ test and can be interpreted as the intensity of the base model producing superior forecasts. † A unity value indicates here that the test is not computed since the model outperformed all others.

- Table 5: Superior predictive ability (SPA) test λk for daily SV models and the Standard & Poor’s 100 evaluation period 17 October 2001 to 14 November 2003

[Figure 198]

Loss Base model Alternative models SV SV RV SV IV GARCH GA.RV GA.IV p-value T∗

[Figure 199]

[Figure 200]

[Figure 201]

[Figure 202]

[Figure 203]

MSE SV – 0.73 −1.26 −2.42 −1.02 −1.91 0.604 SV RV −0.73 – −1.68 −3.72 −1.34 −2.06 1† SV IV 1.26 1.68 – 0.60 −0.00 0.44 0.089 GARCH 2.42 3.72 −0.60 – −0.45 −0.13 0.002 GARCH RV 1.02 1.34 0.00 0.45 – 0.37 0.164 GARCH IV 1.91 2.06 −0.44 0.13 −0.37 – 0.027

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

MAE SV – 5.86 2.42 −5.32 0.21 −1.02 0.000 SV RV −5.86 – −0.76 −10.5 −3.41 −4.05 1† SV IV −2.42 0.76 – −4.50 −1.79 −2.69 0.400 GARCH 5.32 10.5 4.50 – 2.05 0.80 0.000 GARCH RV −0.21 3.41 1.79 −2.05 – −0.89 0.004 GARCH IV 1.02 4.05 2.69 −0.80 0.89 – 0.000

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

HMSE SV – 2.01 1.94 −6.00 0.94 0.04 0.070 SV RV −2.01 – −0.55 −2.32 −3.07 −1.90 1† SV IV −1.94 0.55 – −2.26 −3.06 −1.83 0.575 GARCH 6.00 2.32 2.26 – 1.45 1.15 0.000 GARCH RV −0.94 3.07 3.06 −1.46 – −0.80 0.009

[Figure 230]

[Figure 231]

[Figure 232]

[Figure 233]

[Figure 234]

[Figure 235]

[Figure 236]

[Figure 237]

- GARCH IV −0.04 1.90 1.83 −1.15 0.80 – 0.089

[Figure 238]

[Figure 239]

[Figure 240]

HMAE SV – 7.76 7.99 −10.1 2.26 1.77 0.000 SV RV −7.76 – 0.25 −9.11 −5.46 −4.39 0.405 SV IV −7.99 −0.25 – −9.66 −6.69 −4.48 1† GARCH 10.1 9.11 9.66 – 4.77 3.17 0.000 GARCH RV −2.26 5.46 6.69 −4.77 – 0.11 0.000

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

- GARCH IV −1.77 4.39 4.48 −3.17 −0.11 – 0.000

[Figure 251]

[Figure 252]

A positive value in column of an alternative model Mk means it is superior to the base model according to a speciﬁc loss function. Final column has p-value of T∗ test and can be interpreted as the intensity of the base model producing superior forecasts. † A unity value indicates here that model outperformed all others.

Andersen, Bollerslev, Diebold, and Labys (2003) although the empirical part of their study is based on various GARCH and (trivariate) ARFIMA models for exchange rates while this study considers univariate ARFIMA models together with unobserved component models (based on Le´vy driven OU processes) for a stock index time series.

#### 7 Summary and Conclusions

In this paper we examine the predictive abilities of four classes of volatility models by comparing the forecasts with realised volatility measures that are deﬁned as scaled sums of squared intraday returns. Time series of realised volatility can be modelled by unobserved components (UC-RV) and by autoregressive fractionally integrated moving average (ARFIMA-RV) models. Forecasts can be generated from these models after they are estimated using relatively straightforward methods. Daily returns can be modelled by stochastic volatility (SV) and generalised autoregressive conditional heteroskedasticity (GARCH) models from which volatity estimates and forecasts can be obtained. In the case of GARCH models, estimation and forecasting belong to the standard toolbox of many applied workers. More involved statistical procedures are required for estimating and forecasting volatility on the basis of SV models. We empirically investigate the one-step ahead forecasting performance of the various models for the Standard & Poor’s 100 stock index over the period 17 October 2001 to 14 November 2003. The most accurate forecasts are obtained with the log ARFIMA-RV model and closely followed by the UC-RV model. Within the classes of historical volatility models, the SV model with realised volatility incorporated as an explanatory variable in the volatility equation is best. These conclusions are not only based on a standard forecasting accuracy assessment using mean squared forecast error and mean absolute forecast error statistics, formal prediction superiority tests are also carried out. The implementation closely follows the developments reported in White (2000) and Hansen (2001). This extensive study may have shed some light on the discussion which model is mostly suited for the forecasting of volatility. In this respect we would like to stress the importance of realised volatility in empirical work. Recent work by Andersen, Bollerslev, Diebold and Ebens (2001), Barndorﬀ-Nielsen and Shephard (2001, 2002), Andersen, Bollerslev, Diebold and Labys (2003) and work in progress on realised volatility is therefore higly relevant for the forecasting of volatility.

#### References

- Andersen, T.G. and T. Bollerslev (1997), Intraday seasonality and volatility persistence in foreign exchange and equity markets, Journal of Empirical Finance 4, 115–158.
- Andersen, T.G. and T. Bollerslev (1998), Answering the skeptics: Yes, standard volatility models do provide accurate forecasts, International Economic Review 39, 885–905.

Andersen, T.G., T. Bollerslev, F.X. Diebold, and H. Ebens (2001), The distribution of realized stock return volatility, Journal of Financial Economics 61, 43–76. Andersen, T.G., T. Bollerslev, F.X. Diebold, and P. Labys (2001), The distribution of exchange rate volatility, Journal of the American Statistical Association 96, 42–55. Andersen, T.G., T. Bollerslev, F.X. Diebold, and P. Labys (2003), Modeling and forecasting realized volatility, Econometrica 71, 579–625.

Andersen, T.G., T. Bollerslev, and S. Lange (1999), Forecasting ﬁnancial market volatility: sample frequency vis-`-vis forecast horizon, Journal of Empirical Finance 6, 457–477. Areal, N.M.P.C. and S.J. Taylor (2002), The realized volatility of FTSE-100 futures prices, Journal of Futures Markets 22, 627–648.

- Barndorﬀ-Nielsen, O.E. and N. Shephard (2001), Non-Gaussian OU based models and some of their uses in ﬁnancial economics (with discussion), Journal of the Royal Statistical Society, Series

- B 63, 167–241.

Barndorﬀ-Nielsen, O.E. and N. Shephard (2002), Econometric analysis of realised volatility and its use in estimating Stochastic Volatility models, Journal of the Royal Statistical Society, Series

- B 64, 253–280.

- Barndorﬀ-Nielsen, O.E. and N. Shephard (2004a), Measuring and forecasting ﬁnancial variability using realised variance, In A.C. Harvey, S.J. Koopman, and N. Shephard (Eds.), State space and unobserved components models: theory and applications, Cambridge University Press, Cambridge.
- Barndorﬀ-Nielsen, O.E. and N. Shephard (2004b), Power and bipower variation with stochastic volatility and jumps (with discussion), Journal of Financial Econometrics 3, Forthcoming.

Barucci, E. and R. Reno (2002), On measuring volatility of diﬀusion processes with high frequency data, Economic Letters 74, 371–378. Beckers, S. (1981), Standard deviations implied in options prices as predictors of future stock price variability, Journal of Banking and Finance 5, 363–381. Bera, A.K. and M.L. Higgins (1993), ARCH models: properties, estimation and testing, Journal of Economic Surveys 7, 305–366.

Blair, B.J., S.H. Poon, and S.J. Taylor (2001), Forecasting S&P 100 volatility: the incremental information content of implied volatilities and high frequency returns, Journal of Econometrics 105, 5–26.

Bollerslev, T. (1986), Generalized autoregressive conditional heteroskedasticity, Journal of Econometrics 31, 307–327. Bollerslev, T., R.Y. Chou, and K.F. Kroner (1992), ARCH modeling in Finance: a review of the theory and empirical evidence, Journal of Econometrics 52, 5–59. Bollerslev, T., R.F. Engle, and D.B. Nelson (1994), ARCH models, In R.F. Engle and D.L. McFad-

den (Eds.), Handbook of Econometrics, Volume 4, pp. 2959–3038, Elsevier Science, Amsterdam. Bos, C.S., P.H. Franses, and M. Ooms (2002), Inﬂation, forecast intervals and long memory regres-

sion models, International Journal of Forecasting 18, 243–264. Brodsky, J. and C.M. Hurvich (1999), Multi-step forecasting for long-memory processes, Journal of Forecasting 18, 59–75. Chiras, D.P. and S. Manaster (1978), The information content of options prices and a test of market eﬃciency, Journal of Financial Economics 6, 213–234. Christensen, B.J. and N.R. Prabhala (1998), The relation between implied and realized volatility, Journal of Financial Economics 50, 125–150.

Corsi, F., G. Zumbach, U. Mu¨ller, and M. Dacorogna (2001), Consistent high-precision volatility from high-frequency data, Economic Notes 30, 183–204. de Jong, P. and N. Shephard (1995), The simulation smoother for time series models, Biometrika 82, 339–350. Diebold, F.X. and R.S. Mariano (1995), Comparing predictive accuracy, Journal of Business and Economic Statistics 13, 253–263. Doornik, J.A. (2001), Ox: Object Oriented Matrix Programming, 3.0, London: Timberlake Consultants Press. Doornik, J.A. and M. Ooms (2001), A package for estimating, forecasting and simulating Arﬁma models: Arﬁma package 1.01 for Ox, Working Paper, Nuﬃeld College, Oxford.

Doornik, J.A. and M. Ooms (2003), Computational aspects of maximum likelihood estimation of autoregressive fractionally integrated moving average models, Computational Statistics and Data Analysis 42, 333–348.

Durbin, J. and S.J. Koopman (1997), Monte Carlo maximum likelihood estimation for bon-Gaussian state space models, Biometrika 84, 669–684.

- Durbin, J. and S.J. Koopman (2000), Time series analysis of non-Gaussian observations based on state space models from both classical and Bayesian perspectives (with discussion), Journal of the Royal Statistical Society, Series B 62, 3–56.
- Durbin, J. and S.J. Koopman (2001), Time series analysis by state space methods, Oxford University Press, Oxford.
- Durbin, J. and S.J. Koopman (2002), A simple and eﬃcient simulation smoother for state space time series analysis, Biometrika 89, 603–616.

Engle, Robert F (1982), Autoregressive conditional heteroskedasticity with estimates of the variance of the United Kingdom Inﬂation, Econometrica 50, 987–1007.

Feinstein, S.P. (1995), The Black-Scholes formula is nearly linear in σ for at-the-money options; therefore implied volatilities from at-the-money options are virtually unbiased, Working Paper, Boston University.

Fleming, J. (1998), The quality of market volatility forecast implied by S&P 100 index option prices, Journal of Empirical Finance 5, 317–345. Fleming, J., B. Ostdiek, and R.E. Whaley (1995), Predicting stock market volatility: a new measure, Journal of Futures Markets 15, 265–302.

Fleming, J. and R.E. Whaley (1994), The value of wildcard options, Journal of Finance 49, 215–236. French, K.R., G.W. Schwert, and R.F. Stambaugh (1987), Expected stock returns and volatility,

Journal of Financial Economics 19, 3–29.

Ghysels, E., A.C. Harvey, and E. Renault (1996), Stochastic Volatility, In G.S. Maddala and C.R. Rao (Eds.), Handbook of Statistics, Volume 14, Statistical Methods in Finance, pp. 119–191, North-Holland, Amsterdam.

Giot, P. (2003), The information content of implied volatility in agricultural commodity markets, Journal of Futures Markets 23, 441–454.

Giot, P. and S. Laurent (2004), Modelling daily Value-at-Risk using realized volatility and ARCH type models, Journal of Empirical Finance 11, forthcoming.

Hansen, P.R. (2001), A test for superior predictive ability, Discussion Paper, Brown University Working Paper 2001-06.

- Hansen, P.R. and A. Lunde (2002), Volatility estimation using high frequency data with partial availability, Discussion Paper, Brown University Working Paper.
- Hansen, P.R. and A. Lunde (2003a), Consistent preordering with an estimated criterion function, with an application to the evaluation and comparison of volatility models, Discussion Paper, Brown University Working Paper 2003-01.

Hansen, P.R. and A. Lunde (2003b), A forecast comparison of volatility models: does anything beat a GARCH(1,1)?, Discussion Paper, Brown University Working Paper. Harvey, A.C., E. Ruiz, and N. Shephard (1994), Multivariate Stochastic Variance models, Review of Economic Studies 61, 247–264. Harvey, C.R. and R.E. Whaley (1992), Dividends and S&P 100 index option valuation, Journal of Futures Markets 12(2), 123–137. Hull, J. and A. White (1987), The pricing of options on assets with stochastic volatilities, Journal of Finance 42, 281–300. Koopman, S.J., N. Shephard, and J. Doornik (1999), Statistical algorithms for models in state space using SsfPack 2.2, Econometrics Journal 2, 113–166. Latane´, H.A. and R.J. Rendleman (1976), Standard deviations of stock price ratios implied in option prices, Journal of Finance 31, 369–381. Laurent, S. and J.P. Peters (2002), G@RCH 2.2: an Ox package for estimating and forecasting various ARCH models, Journal of Economic Surveys 16, 447–484. Lee, K.M. and S.J. Koopman (2003), Estimating Stochastic Volatility models: a comparison of two importance samplers, Discussion Paper, Free University Amsterdam. Malliavin, P. and M.E. Mancino (2002), Fourier series method for measurment of multivariate volatilities, Finance and Stochastics 6, 49–61.

- Martens, M. (2001), Forecasting daily exchange rate volatility using intraday returns, Journal of International Money and Finance 20, 1–23.
- Martens, M. (2002), Measuring and forecasting S&P 500 index-futures volatility using highfrequency data, Journal of Futures Markets 22, 497–518.

Meddahi, N. (2003), ARMA representation of integrated and realized variances, Econometrics Journal 6, 335–356.

Politis, D.N. and J.P. Romano (1994), The stationary bootstrap, Journal of the American Statistical Association 89, 1303–1313. Poon, S.H. and C. Granger (2003), Forecasting volatility in ﬁnancial markets: a review, Journal of Economic Literature 41, 478–539.

Poon, S.H. and S.J. Taylor (1992), Stock returns and volatility: an empirical study of the UK stock

market, Journal of Banking and Finance 16, 37–59. Ripley, B.D. (1987), Stochastic simulation, Wiley, New York. Sandmann, G. and S.J. Koopman (1998), Estimation of Stochastic Volatility models via Monte

Carlo maximum likelihood, Journal of Econometrics 87, 271–301.

Shephard, N. (1996), Statistical aspects of ARCH and Stochastic Volatility, In D.R. Cox, D.V. Hinkley, and O.E. Barndorﬀ-Nielsen (Eds.), Time Series Models in Econometrics, Finance and Other Fields, Number 65 in Monographs on Statistics and Applied Probability, pp. 1–67, Chapman and Hall, London.

Shephard, N. and M.K. Pitt (1997), Likelihood analysis of non-Gaussian measurement time series, Biometrika 84, 653–667. Sowell, F. (1992), Maximum likelihood estimation of stationary univariate fractionally integrated

time series models, Journal of Econometrics 53, 165–188. Taylor, S.J. (1986), Modelling ﬁnancial time series, John Wiley and Sons, Chichester. Taylor, S.J. and X. Xu (1997), The incremental volatility information in one million foreign exchange

quotations, Journal of Empirical Finance 4, 317–340. West, K.D. (1996), Asymptotic inference about predictive ability, Econometrica 64, 1067–1084. White, H. (2000), A reality check for data snooping, Econometrica 68, 1097–1126.

