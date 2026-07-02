[Figure 1]

### In Search of Distress Risk

[Figure 2]

###### Citation

Campbell, John Y., Jens Hilscher, and Jan Szilagyi. 2008. In Search of Distress Risk. Journal of Finance 63, no. 6: 2899-2939.

###### Published version

https://doi.org/10.1111/j.1540-6261.2008.01416.x

###### Link

http://nrs.harvard.edu/urn-3:HUL.InstRepos:3199070

###### Terms of use

This article was downloaded from Harvard University’s DASH repository, and is made available under the terms and conditions applicable to Other Posted Material (LAA), as set forth at

https://harvardwiki.atlassian.net/wiki/external/NGY5NDE4ZjgzNTc5NDQzMGIzZWZhMGFlOWI2M2EwYTg

###### Accessibility

https://accessibility.huit.harvard.edu/digital-accessibility-policy

###### Share Your Story

The Harvard community has made this article openly available. Please share how this access benefits you. Submit a story

[Figure 3]

# H I E RR

## Harvard Institute of Economic Research

Discussion Paper Number 2081 In Search of Distress Risk by John Y. Campbell, Jens Hilscher and Jan Szilagyi

July 2005

##### Harvard University Cambridge, Massachusetts

This paper can be downloaded without charge from: http://post.economics.harvard.edu/hier/2005papers/2005list.html

The Social Science Research Network Electronic Paper Collection: http://ssrn.com/abstract=770805

#### In Search of Distress Risk

John Y. Campbell, Jens Hilscher, and Jan Szilagyi1

First draft: October 2004 This version: June 27, 2005

1Corresponding author: John Y. Campbell, Department of Economics, Littauer Center 213, Harvard University, Cambridge MA 02138, USA, and NBER. Tel 617-496-6448, email john_campbell@harvard.edu. This material is based upon work supported by the National Science Foundation under Grant No. 0214061 to Campbell. We would like to thank Robert Jarrow and Don van Deventer of Kamakura Risk Information Services (KRIS) for providing us with data on corporate bankruptcies and failures, and Stuart Gilson, John Griﬃn, Scott Richardson, Ulf von Kalckreuth, and seminar participants at Humboldt Universität zu Berlin, HEC Paris, the University of Texas, the Wharton School, and the Deutsche Bundesbank 2005 Spring Conference for helpful discussion.

Abstract

This paper explores the determinants of corporate failure and the pricing of ﬁnancially distressed stocks using US data over the period 1963 to 2003. Firms with higher leverage, lower proﬁtability, lower market capitalization, lower past stock returns, more volatile past stock returns, lower cash holdings, higher market-book ratios, and lower prices per share are more likely to ﬁle for bankruptcy, be delisted, or receive a D rating. When predicting failure at longer horizons, the most persistent ﬁrm characteristics, market capitalization, the market-book ratio, and equity volatility become relatively more signiﬁcant. Our model captures much of the time variation in the aggregate failure rate. Since 1981, ﬁnancially distressed stocks have delivered anomalously low returns. They have lower returns but much higher standard deviations, market betas, and loadings on value and small-cap risk factors than stocks with a low risk of failure. These patterns hold in all size quintiles but are particularly strong in smaller stocks. They are inconsistent with the conjecture that the value and size eﬀects are compensation for the risk of ﬁnancial distress.

###### 1 Introduction

The concept of ﬁnancial distress is often invoked in the asset pricing literature to explain otherwise anomalous patterns in the cross-section of stock returns. The idea is that certain companies have an elevated risk that they will fail to meet their ﬁnancial obligations, and investors charge a premium for bearing this risk.2

While this idea has a certain plausibility, it leaves a number of basic questions unanswered. First, how do we measure the failure to meet ﬁnancial obligations? Second, how do we measure the probability that a ﬁrm will fail to meet its ﬁnancial obligations? Third, even if we have answered these questions and thereby constructed an empirical measure of ﬁnancial distress, is it the case that the stock prices of ﬁnancially distressed companies move together in response to a common risk factor? Finally, what returns have ﬁnancially distressed stocks provided historically? Is there any evidence that ﬁnancial distress risk carries a premium?

In this paper we consider two alternative ways in which a ﬁrm may fail to meet its ﬁnancial obligations. First, we look at bankruptcy ﬁlings under either Chapter 7 or Chapter 11 of the bankruptcy code. Second, we look at failures, deﬁned more broadly to include bankruptcies, delistings, or D (“default”) ratings issued by a leading credit rating agency. The broader deﬁnition of failure allows us to capture at least some cases where ﬁrms avoid bankruptcy by negotiating with creditors out of court (Gilson, John, and Lang 1990, Gilson 1997). It also captures ﬁrms that perform so poorly that their stocks are delisted from the exchange, an event which sometimes precedes bankruptcy or formal default.

To measure the probability that a ﬁrm enters either bankruptcy or failure, we adopt a relatively atheoretical econometric approach. We estimate a dynamic panel model using a logit speciﬁcation, following Shumway (2001), Chava and Jarrow (2004), and others. We extend the previous literature by considering a wide range of explanatory variables, including both accounting and equity-market variables, and by explicitly considering how the optimal speciﬁcation varies with the horizon of the

2Chan and Chen (1991), for example, attribute the size premium to the prevalence of “marginal ﬁrms” in small-stock portfolios, and describe marginal ﬁrms as follows: “They have lost market value because of poor performance, they are ineﬃcient producers, and they are likely to have high ﬁnancial leverage and cash ﬂow problems. They are marginal in the sense that their prices tend to be more sensitive to changes in the economy, and they are less likely to survive adverse economic conditions.” Fama and French (1996) use the term “relative distress” in a similar fashion.

forecast. Some papers on bankruptcy concentrate on predicting the event that a bankruptcy will occur during the next month. Over such a short horizon, it should not be surprising that the recent return on a ﬁrm’s equity is a powerful predictor, but this may not be very useful information if it is relevant only in the extremely short run, just as it would not be useful to predict a heart attack by observing a person dropping to the ﬂoor clutching his chest. We also explore time-series variation in the number of bankruptcies, and ask how much of this variation is explained by changes over time in the variables that predict bankruptcy at the ﬁrm level.

Our empirical work begins with monthly bankruptcy and failure indicators provided by Kamakura Risk Information Services (KRIS). The bankruptcy indicator was used by Chava and Jarrow (2004), and covers the period from January 1963 through December 1998. The failure indicator runs from January 1963 through December 2003. We merge these datasets with ﬁrm level accounting data from COMPUSTAT

- as well as monthly and daily equity price data from CRSP. This gives us about 800 bankruptcies, 1600 failures, and predictor variables for 1.7 million ﬁrm months.

We start by estimating a basic speciﬁcation used by Shumway (2001) and similar to that of Chava and Jarrow (2004). The model includes both equity market and accounting data. From the equity market, we measure the excess stock return of each company over the past month, the volatility of daily stock returns over the past three months, and the market capitalization of each company. From accounting data, we measure net income as a ratio to assets, and total leverage as a ratio to assets. We obtain similar coeﬃcient estimates whether we are predicting bankruptcies through 1998, failures through 1998, or failures through 2003.

From this starting point, we make a number of contributions to the prediction of corporate bankruptcies and failures. First, we explore some sensible modiﬁcations to the variables listed above. Speciﬁcally, we show that scaling net income and leverage by the market value of assets rather than the book value, and adding further lags of stock returns and net income, can improve the explanatory power of the benchmark regression.

Second, we explore some additional variables and ﬁnd that corporate cash holdings, the market-book ratio, and a ﬁrm’s price per share contribute explanatory power. In a related exercise we construct a measure of distance to default, based on the practitioner model of KMV (Crosbie and Bohn 2001) and ultimately on the structural default model of Merton (1974). We ﬁnd that this measure adds relatively little

explanatory power to the reduced-form variables already included in our model.3 Third, we examine what happens to our speciﬁcation as we increase the horizon

- at which we are trying to predict failure. Consistent with our expectations, we ﬁnd that our most persistent forecasting variable, market capitalization, becomes relatively more important as we predict further into the future. Volatility and the market-book ratio also become more important at long horizons relative to net income, leverage, and recent equity returns.

Fourth, we study time-variation in the number of failures. We compare the realized frequency of failure to the predicted frequency over time. Although the model underpredicts the frequency of failure in the 1980s and overpredicts it in the 1990s, the model ﬁts the general time pattern quite well.

Finally, we use our ﬁtted probability of failure as a measure of ﬁnancial distress and calculate the risks and average returns on portfolios of stocks sorted by this ﬁtted probability. We ﬁnd that ﬁnancially distressed ﬁrms have high market betas and high loadings on the HML and SMB factors proposed by Fama and French (1993, 1996) to capture the value and size eﬀects. However they do not have high average returns, suggesting that the equity market has not properly priced distress risk.

There is a large related literature that studies the prediction of corporate bankruptcy. The literature varies in choice of variables to predict bankruptcy and the methodology used to estimate the likelihood of bankruptcy. Altman (1968), Ohlson (1980), and Zmijewski (1984) use accounting variables to estimate the probability of bankruptcy in a static model. Altman’s Z-score and Ohlson’s O-score have become popular and widely accepted measures of ﬁnancial distress. They are used, for example, by Dichev (1998), Griﬃn and Lemmon (2002), and Ferguson and Shockley (2003) to explore the risks and average returns for distressed ﬁrms.

Shumway (2001) estimates a hazard model at annual frequency and adds equity market variables to the set of scaled accounting measures used in the earlier literature. He points out that estimating the probability of bankruptcy in a static setting introduces biases and overestimates the impact of the predictor variables. This is because the static model does not take into account that a ﬁrm could have had unfavorable indicators several periods before going into bankruptcy. Hillegeist, Cram, Keating and

3This ﬁnding is consistent with recent results of Bharath and Shumway (2004), circulated after the ﬁrst version of this paper.

Lunstedt (2004) summarize equity market information by calculating the probability of bankruptcy implied by the structural Merton model. Adding this to accounting data increases the accuracy of bankruptcy prediction within the framework of a haz-

- ard model. Chava and Jarrow (2004) estimate hazard models at both annual and monthly frequencies and ﬁnd that the accuracy of bankruptcy prediction is greater at a monthly frequency. They also compare the eﬀects of accounting information across industries.

Duﬃe and Wang (2003) emphasize that the probability of bankruptcy depends on the horizon one is considering. They estimate mean-reverting time series processes for a macroeconomic state variable–personal income growth–and a ﬁrm-speciﬁc variable–distance to default. They combine these with a short-horizon bankruptcy model to ﬁnd the marginal probabilities of default at diﬀerent horizons. Using data from the US industrial machinery and instruments sector, they calculate term structures of default probabilities. We conduct a similar exercise using a reducedform econometric approach; we do not model the time-series evolution of the predictor variables but instead directly estimate longer-term default probabilities.

The remainder of the paper is organized as follows. Section 2 describes the construction of the data set, outlier analysis and summary statistics. Section 3 discusses our basic dynamic panel model, extensions to it, and the results from estimating the model at one-month and longer horizons. We ﬁnd that market capitalization, the market-book ratio, and equity volatility become relatively more signiﬁcant as the horizon increases. This section also considers the ability of the model to ﬁt the aggregate time-series of failures. Section 4 studies the return properties of equity portfolios formed on the ﬁtted value from our bankruptcy prediction model. We ask whether stocks with high bankruptcy probability have unusually high or low returns relative to the predictions of standard cross-sectional asset pricing models such as the CAPM or the three-factor Fama-French model. Section 5 concludes.

###### 2 Data description

In order to estimate a dynamic logit model we need an indicator of ﬁnancial distress and a set of explanatory variables. The bankruptcy indicator we use is taken from Chava and Jarrow (2004); it includes all bankruptcy ﬁlings in the Wall Street Journal Index, the SDC database, SEC ﬁlings and the CCH Capital Changes Reporter. The indicator equals one in a month in which a ﬁrm ﬁled for bankruptcy under Chapter 7 or Chapter 11, and zero otherwise; in particular, the indicator is zero if the ﬁrm disappears from the dataset for some reason other than bankruptcy such as acquisition or delisting. The data span the months from January 1963 through December 1998. We also consider a broader failure indicator, which equals one if a ﬁrm ﬁles for bankruptcy, delists, or receives a D rating, over the period January 1963 through December 2003.

Table 1 summarizes the properties of our bankruptcy and failure indicators. The ﬁrst column shows the number of active ﬁrms for which we have data in each year. The second column shows the number of bankruptcies, and the third column the corresponding percentage of active ﬁrms that went bankrupt in each year. The fourth and ﬁfth columns repeat this information for our failure series.

It is immediately apparent that bankruptcies were extremely rare until the late 1960’s. In fact, in the three years 1967—1969 there were no bankruptcies at all in our dataset. The bankruptcy rate increased in the early 1970’s, and then rose dramatically during the 1980’s to a peak of 1.5% in 1986. It remained high through the economic slowdown of the early 1990’s, but fell in the late 1990’s to levels only slightly above those that prevailed in the 1970’s.

Some of these changes through time are probably the result of changes in the law governing corporate bankruptcy in the 1970’s, and related ﬁnancial innovations such as the development of below-investment-grade public debt (junk bonds) in the 1980’s and the advent of prepackaged bankruptcy ﬁlings in the early 1990’s (Tashjian, Lease, and McConnell 1996). Changes in corporate capital structure (Bernanke and Campbell 1988) and the riskiness of corporate activities (Campbell, Lettau, Malkiel, and Xu 2001) are also likely to have played a role, and one purpose of our investigation is to quantify the time-series eﬀects of these changes.

The broader failure indicator tracks the bankruptcy indicator closely until the early 1980’s, but towards the end of the sample it begins to diverge signiﬁcantly. The

number of failures increases dramatically after 1998, reﬂecting the ﬁnancial distress of many young ﬁrms that were newly listed during the boom of the late 1990’s.

In order to construct explanatory variables at the individual ﬁrm level, we combine quarterly accounting data from COMPUSTAT with monthly and daily equity market data from CRSP. From COMPUSTAT we construct a standard measure of proﬁtability: net income relative to total assets. Previous authors have measured total assets at book value, but we ﬁnd better explanatory power when we measure the equity component of total assets at market value by adding the book value of liabilities to the market value of equities. We call this series NIMTA (Net Income to Market-valued Total Assets) and the traditional series NITA (Net Income to Total Assets). We also use COMPUSTAT to construct a measure of leverage: total liabilities relative to total assets. We again ﬁnd that a market-valued version of this series, deﬁned as total liabilities divided by the sum of market equity and book liabilities, performs better than the traditional book-valued series. We call the two series TLMTA and TLTA, respectively. To these standard measures of proﬁtability and leverage, we add a measure of liquidity, the ratio of a company’s cash and short-term assets to the market value of its assets (CASHMTA). We also calculate each ﬁrm’s market-to-book ratio (MB).

In constructing these series we adjust the book value of assets to eliminate outliers, following the procedure suggested by Cohen, Polk, and Vuolteenaho (2003). That is, we add 10% of the diﬀerence between market and book equity to the book value of total assets, thereby increasing book values that are extremely small, probably mismeasured, and create outliers when used as the denominators of ﬁnancial ratios. We also winsorize all variables at the 5th and 95th percentiles of their cross-sectional distributions. That is, we replace any observation below the 5th percentile with the 5th percentile, and any observation above the 95th percentile with the 95th percentile. We are careful to adjust each company’s ﬁscal year to the calendar year and lag the accounting data by two months. This adjustment ensures that the accounting data

- are available at the beginning of the month over which bankruptcy is measured. The Appendix to this paper describes the construction of these variables in greater detail.

We add several market-based variables to these two accounting variables. We calculate the monthly log excess return on each ﬁrm’s equity relative to the S&P 500 index (EXRET), the standard deviation of each ﬁrm’s daily stock return over the past three months (SIGMA), and the relative size of each ﬁrm measured as the log ratio of its market capitalization to that of the S&P 500 index (RSIZE). Finally,

we calculate each ﬁrm’s log price per share, truncated above at $15 (PRICE). This captures a tendency for distressed ﬁrms to trade at low prices per share, without reverse-splitting to bring price per share back into a more normal range.

###### 2.1 Summary statistics

Table 2 summarizes the properties of our ten main explanatory variables. The ﬁrst panel in Table 2 describes the distributions of the variables in almost 1.7 million ﬁrmmonths with complete data availability, the second panel describes a much smaller sample of almost 800 bankruptcy months, and the third panel describes just over 1600 failure months.4

In interpreting these distributions, it is important to keep in mind that we weight every ﬁrm-month equally. This has two important consequences. First, the distributions are dominated by the behavior of relatively small companies; value-weighted distributions look quite diﬀerent. Second, the distributions reﬂect the inﬂuence of both cross-sectional and time-series variation. The cross-sectional averages of several variables, in particular NIMTA, TLMTA, and SIGMA, have experienced signiﬁcant trends since 1963: SIGMA and TLMTA have trended up, while NIMTA has trended down. The downward trend in NIMTA is not just a consequence of the buoyant stock market of the 1990’s, because book-based net income, NITA, displays a similar trend. The inﬂuence of these trends is magniﬁed by the growth in the number of companies and the availability of quarterly accounting data over time, which means that recent years have greater inﬂuence on the distribution than earlier years. In particular, there is a scarcity of quarterly Compustat data before the early 1970’s so years before 1973 have very little inﬂuence on our empirical results.

These facts help to explain several features of Table 2. The mean level of NIMTA, for example, is almost exactly zero (in fact, very slightly negative). This is lower than the median level of NIMTA, which is positive at 0.6% per quarter or 2.4% at an annual rate, because the distribution of proﬁtability is negatively skewed. The gap between mean and median is even larger for NITA. All these measures of proﬁtability are strikingly low, reﬂecting the prevalence of small, unproﬁtable listed companies in recent years. Value-weighted mean proﬁtability is considerably higher. In addition,

4For a ﬁrm-month to be included in Table 2, we must observe leverage, proﬁtability, excess return, and market capitalization. We do not require a valid measure of volatility, and replace SIGMA with its cross-sectional mean when this variable is missing.

the distributions of NIMTA and NITA have large spikes just above zero, a phenomenon noted by Hayn (1995), suggesting that ﬁrms may be managing their earnings to avoid reporting losses.5

The average value of EXRET is -0.011 or -1.1% per month. This extremely low number reﬂects both the underperformance of small stocks during the later part of our sample period (the value-weighted mean is almost exactly zero), and the fact that we are reporting a geometric average excess return rather than an arithmetic average. The diﬀerence is substantial because individual stock returns are extremely volatile. The average value of the annualized ﬁrm-level volatility SIGMA is 56%, again reﬂecting the strong inﬂuence of small ﬁrms and recent years in which idiosyncratic volatility has been high (Campbell, Lettau, Malkiel, and Xu 2001).

A comparison of the top and the second panel of Table 2 reveals that bankrupt ﬁrms have intuitive diﬀerences from the rest of the sample. In months immediately preceding a bankruptcy ﬁling, ﬁrms typically make losses (the mean loss is 4.0% quarterly or 16% of market value of assets at an annual rate, and the median loss is 4.7% quarterly or almost 19% at an annual rate); the value of their debts is extremely high relative to their assets (average leverage is almost 80%, and median leverage exceeds 87%); they have experienced extremely negative returns over the past month (the mean is -11.5% over a month, while the median is -17% over a month); and their volatility is extraordinarily high (the mean annualized volatility is 106% and the median is 126%). Bankrupt ﬁrms also tend to be relatively small (about 7 times smaller than other ﬁrms on average, and 10 times smaller at the median), and they have only about half as much cash and short-term investments, in relation to the market value of assets, as non-bankrupt ﬁrms.

The market-book ratio of bankrupt ﬁrms has a similar mean but a much higher standard deviation than the market-book ratio of other ﬁrms. It appears that some ﬁrms go bankrupt after realized losses have driven down their book values relative to market values, while others go bankrupt after bad news about future prospects has driven down their market values relative to book values. Thus bankruptcy is associated with a wide spread in the market-book ratio.

Finally, ﬁrms that go bankrupt typically have low prices per share. The mean

5There is a debate in the accounting literature about the interpretation of this spike. Burgstahler and Dichev (1997) argue that it reﬂects earnings management, but Dechow, Richardson, and Tuna (2003) point out that discretionary accruals are not associated with the spike in the manner that would be expected if this interpretation is correct.

price per share is just over $1.50 for a bankrupt ﬁrm, while the median price per share is slightly below $1.

The third panel of Table 2 reports the summary statistics for our failure sample through December 2003. The patterns are similar to those in the second panel, but some eﬀects are stronger for failures than for bankruptcies (losses are more extreme, volatility is higher, price per share is lower, and market capitalization is considerably smaller), while other eﬀects are weaker (leverage is less extreme and cash holdings are higher).

###### 3 A logit model of bankruptcy and failure

The summary statistics in Table 2 show that bankrupt and failed ﬁrms have a number of unusual characteristics. However the number of bankruptcies and failures is tiny compared to the number of ﬁrm-months in our dataset, so it is not at all clear how useful these variables are in predicting bankruptcy. Also, these characteristics are correlated with one another and we would like to know how to weight them optimally. Following Shumway (2001) and Chava and Jarrow (2004), we now estimate the probabilities of bankruptcy and failure over the next period using a logit model.

We assume that the marginal probability of bankruptcy or failure over the next period follows a logistic distribution and is given by

1 1 + exp(−α − βxi,t−1)

(1)

Pt−1 (Yit = 1) =

where Yit is an indicator that equals one if the ﬁrm goes bankrupt or fails in month t, and xi,t−1 is a vector of explanatory variables known at the end of the previous month. A higher level of α + βxi,t−1 implies a higher probability of bankruptcy or failure.

Table 3 reports logit regression results for various alternative speciﬁcations. In the ﬁrst three columns we follow Shumway (2001) and Chava and Jarrow (2004), and estimate a model with ﬁve standard variables: NITA, TLTA, EXRET, SIGMA, and RSIZE. This model measures assets in the conventional way, using annual book values from COMPUSTAT. It excludes ﬁrm age, a variable which Shumway (2001) considered but found to be insigniﬁcant in predicting bankruptcy. Column 1 estimates the model for bankruptcy over the period 1963-1998, column 2 estimates it for failure over the same period, and column 3 looks at failure over the entire 1963-2003 period.

All ﬁve of the included variables in the Shumway (2001) bankruptcy model enter signiﬁcantly and with the expected sign. As we broaden the deﬁnition of ﬁnancial distress to failure, and as we include more recent data, the eﬀects of market capitalization and volatility become stronger, while the eﬀects of losses, leverage, and recent past returns become slightly weaker.

In columns 4, 5, and 6 we report results for an alternative model that modiﬁes the Shumway speciﬁcation in several ways. First, we replace the traditional accounting

ratios NITA and TLTA that use the book value of assets, with our ratios NIMTA and TLMTA that use the market value of assets. These measures are more sensitive to new information about ﬁrm prospects since equity values are measured using monthly market data rather than quarterly accounting data.

Second, we add lagged information about proﬁtability and excess stock returns. One might expect that a long history of losses or a sustained decline in stock market value would be a better predictor of bankruptcy than one large quarterly loss or a sudden stock price decline in a single month. Exploratory regressions with lagged values conﬁrm that lags of NIMTA and EXRET enter signiﬁcantly, while lags of the other variables do not. As a reasonable summary, we impose geometrically declining weights on these lags. We construct

1 − φ3 1 − φ12 ¡

¢

NIMTAt−1,t−3 + ... + φ9NIMTAt−9,t−12

,(2)

NIMTAAV Gt−1,t−12 =

1 − φ 1 − φ12

(EXRETt−1 + ... + φ11EXRETt−12), (3)

EXRETAV Gt−1,t−12 =

where the coeﬃcient φ = 2−13, implying that the weight is halved each quarter. When lagged excess returns or proﬁtability are missing, we replace them with their cross-sectional means in order to avoid losing observations. The data suggest that this parsimonious speciﬁcation captures almost all the predictability obtainable from lagged proﬁtability and stock returns.

Third, we add the ratio of cash and short-term investments to the market value of total assets, CASHMTA, in order to capture the liquidity position of the ﬁrm. A ﬁrm with a high CASHMTA ratio has liquid assets available to make interest payments, and thus may be able to postpone bankruptcy with the possibility of avoiding it altogether if circumstances improve.

Fourth, the market to book ratio, MB, captures the relative value placed on the ﬁrm’s equity by stockholders and by accountants. Our proﬁtability and leverage ratios use market value; if book value is also relevant, then MB may enter the regression

- as a correction factor, increasing the probability of bankruptcy when market value is unusually high relative to book value.6

6Chacko, Hecht, and Hilscher (2004) discuss the measurement of credit risk when the market-tobook ratio is inﬂuenced both by cash ﬂow expectations and discount rates.

Finally, we add the log price per share of the ﬁrm, PRICE. We expect this variable to be relevant for low prices per share, particularly since both the NYSE and the Nasdaq have a minimum price per share of $1 and commonly delist stocks that fail to meet this minimum (Macey, O’Hara, and Pompilio 2004). Reverse stock splits are sometimes used to keep stock prices away from the $1 minimum level, but these often have negative eﬀects on returns and therefore on market capitalization, suggesting that investors interpret reverse stock splits as a negative signal about company prospects (Woolridge and Chambers 1983, Hwang 1995). Exploratory analysis suggested that price per share is relevant below $15, and so we truncate price per share at this level before taking the log.

All the new variables in our model enter the logit regression with the expected sign and are highly statistically signiﬁcant. After accounting for diﬀerences in the scaling of the variables, there is little eﬀect on the coeﬃcients of the variables already included in the Shumway model, with the important exception of market capitalization. This variable is strongly correlated with log price per share; once price per share is included, market capitalization enters with a weak positive coeﬃcient, probably as an ad hoc correction to the negative eﬀect of price per share.

To get some idea of the relative impact of changes in the diﬀerent variables, we compute the proportional impact on the failure probability of a one-standarddeviation increase in each predictor variable for a ﬁrm that initially has sample mean values of the predictor variables. Such an increase in proﬁtability reduces the probability of failure by 44% of its initial value; the corresponding eﬀects are a 156% increase for leverage, a 28% reduction for past excess return, a 64% increase for volatility, a 17% increase for market capitalization, a 21% reduction for cash holdings, a 9% increase for the market-book ratio, and a 56% reduction for price per share. Thus variations in leverage, volatility, price per share, and proﬁtability are more important for failure risk than movements in market capitalization, cash, or the market-book ratio. These magnitudes roughly line up with the t statistics reported in Table 3.

Our proposed model delivers a noticeable improvement in explanatory power over the Shumway model. We report McFadden’s pseudo R2 coeﬃcient for each speciﬁcation, calculated as 1−L1/L0, where L1 is the log likelihood of the estimated model and L0 is the log likelihood of a null model that includes only a constant term. The pseudo R2 coeﬃcient increases from 0.26 to 0.30 in predicting bankruptcies or failures over 1963—1998, and from 0.27 to 0.31 in predicting failures over 1963—2003.

###### 3.1 Forecasting at long horizons

At the one month horizon our best speciﬁcation captures about 30% of the variation in bankruptcy risk. We now ask what happens as we try to predict bankruptcies further into the future. In Table 4 we estimate the conditional probability of bankruptcy in six months, one, two and three years. We again assume a logit speciﬁcation but allow the coeﬃcients on the variables to vary with the horizon of the prediction. In particular we assume that the probability of bankruptcy in j months, conditional on survival in the dataset for j − 1 months, is given by

1 1 + exp

¡−αj − βjxi,t−1

¢. (4)

Pt−1 (Yi,t−1+j = 1 | Yi,t−2+j = 0) =

Note that this assumption does not imply a cumulative probability of bankruptcy that is logit. If the probability of bankruptcy in j months did not change with the horizon j, that is if αj = α and βj = β, and if ﬁrms exited the dataset only through bankruptcy, then the cumulative probability of bankruptcy over the next j periods would be given by 1 − (exp(−α − βxi)/(1 + exp(−α − βxi))j, which no longer has the logit form. Variation in the parameters with the horizon j, and exit from the dataset through mergers and acquisitions, only make this problem worse. In principle we could compute the cumulative probability of bankruptcy by estimating models for each horizon j and integrating appropriately; or by using our one-period model and making auxiliary assumptions about the time-series evolution of the predictor variables in the manner of Duﬃe and Wang (2003). We do not pursue these possibilities here, concentrating instead on the conditional probabilities of default at particular dates in the future.

As the horizon increases in Table 4, the coeﬃcients, signiﬁcance levels, and overall ﬁt of the logit regression decline as one would expect. Even at three years, however, almost all the variables remain statistically signiﬁcant.

Three predictor variables are particularly important at long horizons. The coeﬃcient and t statistic on volatility SIGMA are almost unchanged as the horizon increases; the coeﬃcient and t statistic on the market-to-book ratio MB increase with the horizon; and the coeﬃcient on relative market capitalization RSIZE switches sign, becoming increasingly signiﬁcant with the expected negative sign as the horizon increases. These variables, market capitalization, market-to-book ratio, and volatility, are persistent attributes of a ﬁrm that become increasingly important measures of

ﬁnancial distress at long horizons. Log price per share also switches sign, presumably as a result of the previously noted correlation between this variable and market capitalization.

Leverage and past excess stock returns have coeﬃcients that decay particularly rapidly with the horizon, suggesting that these are primarily short-term signals of ﬁnancial distress. Proﬁtability and cash holdings are intermediate, with eﬀects that decay more slowly.

In Table 4 the number of observations and number of failures vary with the horizon, because increasing the horizon forces us to drop observations at both the beginning and end of the dataset. Failures that occur within the ﬁrst j months of the sample cannot be related to the condition of the ﬁrm j months previously, and the last j months of the sample cannot be used to predict failures that may occur after the end of the sample. Also, many ﬁrms exit the dataset for other reasons between dates t−1 and t−1+j. On the other hand, as we lengthen the horizon we can include failures that are immediately preceded by missing data. We have run the same regressions for a subset of ﬁrms for which data are available at all the diﬀerent horizons. This allows us to compare R2 statistics directly across horizons. We obtain very similar results to those reported in Table 4, suggesting that variation in the available data is not responsible for our ﬁndings.

###### 3.2 Comparison with distance to default

A leading alternative to the reduced-form econometric approach we have implemented in this paper is the structural approach of Moody’s KMV (Crosbie and Bohn 2001), based on the structural default model of Merton (1974). This approach uses the Merton model to construct “distance to default”, DD, a measure of the diﬀerence between the asset value of the ﬁrm and the face value of its debt, scaled by the standard deviation of the ﬁrm’s asset value. Taken literally, the Merton model implies a deterministic relationship between DD and the probability of default, but in practice this relationship is estimated by a nonparametric regression of a bankruptcy or failure indicator on DD. That is, the historical frequency of bankruptcy is calculated for ﬁrms with diﬀerent levels of DD, and this historical frequency is used as an estimate of the probability of bankruptcy going forward.

To implement the structural approach, we calculate DD in the manner of Hil-

legeist, Keating, Cram, and Lunstedt (2004) by solving a system of two nonlinear equations. The details of the calculation are described in the Appendix. Table 5 compares the predictive power of the structural model with that of our best reducedform model. The top panel reports the coeﬃcients on DD in a simple regression of our failure indicator on DD, and in a multiple regression on DD and the variables included in our reduced-form model. DD enters with the expected negative sign and is highly signiﬁcant in the simple regression. In the multiple regression, however, it enters with a perverse positive sign at a short horizon, presumably because the reduced-form model already includes volatility and leverage, which are the two main inputs to the calculation of DD. The coeﬃcient on DD only becomes negative and signiﬁcant when the horizon is extended to one or three years.

The bottom panel of Table 5 reports the pseudo R2 statistics for these regressions. While the structural model achieves a respectable R2 of 16% for short-term failure prediction, our reduced-form model almost doubles this number. Adding DD to the reduced-form model has very little eﬀect on the R2, which is to be expected given the presence of volatility and leverage in the reduced-form model. These results hold both when we calculate R2 in-sample, using coeﬃcients estimated over the entire period 1963-2003, and when we calculate it out-of-sample, using coeﬃcients each year from 1981 onwards that were estimated over the period up to but not including that year. The two sets of R2 are very similar because most failures occur towards the end of the dataset, when the full-sample model and the rolling model have very similar coeﬃcients.

The structural approach is designed to forecast default at a horizon of one year. This suggests that it might perform relatively better as we forecast failure further into the future. It is true that DD enters our model signiﬁcantly with the correct sign at longer horizons, but Table 5 shows that the relative performance of DD and our econometric model is relatively constant across forecast horizons.

We conclude that the structural approach captures important aspects of the process determining corporate failure. The predictive power of DD is quite impressive given the tight restrictions on functional form imposed by the Merton model. If one’s goal is to predict failures, however, it is clearly better to use a reduced-form econometric approach that allows volatility and leverage to enter with free coeﬃcients and that includes other relevant variables. Bharath and Shumway (2004), in independent recent work, reach a similar conclusion.

###### 3.3 Other time-series and cross-sectional eﬀects

As we noted in our discussion of Table 1, there is considerable variation in the failure rate over time. We now ask how well our model ﬁts this pattern. We ﬁrst calculate the ﬁtted probability of failure for each company in our dataset using the coeﬃcients from our best reduced-form model. We then average over all the predicted probabilities to obtain a prediction of the aggregate failure rate among companies with data available for failure prediction.

Figure 1 shows annual averages of predicted and realized failures, expressed as a fraction of the companies with available data.7 Our model captures much of the broad variation in corporate failures over time, including the strong and long-lasting increase in the 1980’s and cyclical spikes in the early 1990’s and early 2000’s. However it somewhat overpredicts failures in 1974-5, underpredicts for much of the 1980’s, and then overpredicts in the early 1990’s.

We have explored the possibility that there are industry eﬀects on bankruptcy and failure risk. The Shumway (2001) and Chava-Jarrow (2004) speciﬁcation appears to behave somewhat diﬀerently in the ﬁnance, insurance, and real estate (FIRE) sector. That sector has a lower intercept and a more negative coeﬃcient on proﬁtability. However there is no strong evidence of sector eﬀects in our best model, which relies more heavily on equity market data.

We have also used market capitalization and leverage as interaction variables, to test the hypotheses that other explanatory variables enter diﬀerently for small or highly indebted ﬁrms than for other ﬁrms. We have found no clear evidence that such interactions are important.

7The realized failure rate among these companies is slightly diﬀerent from the failure rate reported in Table 1, which includes all failures and all active companies, not just those with data available for failure prediction.

###### 4 Risks and average returns on distressed stocks

We now turn our attention to the asset pricing implications of our failure model. Recent work on the distress premium has tended to use either traditional risk indices such as the Altman Z-score or Ohlson O-score (Dichev 1998, Griﬃn and Lemmon 2002, Ferguson and Shockley 2003) or the distance to default measure of KMV (Vassalou and Xing 2004, Da and Gao 2004). To the extent that our reduced-form model more accurately measures the risk of failure at short and long horizons, we can more accurately measure the premium that investors receive for holding distressed stocks.

Before presenting the results, we ask what results we should expect to ﬁnd. On the one hand, if investors accurately perceive the risk of failure they may demand a premium for bearing it. The frequency of failure shows strong variation over time, as illustrated in Figure 1; even though much of this time-variation is explained by timevariation in our ﬁrm-level predictive variables, it still generates common movement in stock returns that might command a premium.

Of course, a risk can be pervasive and still be unpriced. If the standard implementation of the CAPM is exactly correct, for example, then each ﬁrm’s risk is fully captured by its covariation with the market portfolio of equities, and distress risk is unpriced to the extent that it is uncorrelated with that portfolio. However it seems plausible that corporate failures may be correlated with declines in unmeasured components of wealth such as human capital (Fama and French 1996) or debt securities (Ferguson and Shockley 2003), in which case distress risk will carry a positive risk premium.8 This expectation is consistent with the high failure risk of small ﬁrms that have depressed market values, since small value stocks are well known to deliver high average returns.

8Fama and French (1996) state the idea particularly clearly: “Why is relative distress a state variable of special hedging concern to investors? One possible explanation is linked to human capital, an important asset for most investors. Consider an investor with specialized human capital tied to a growth ﬁrm (or industry or technology). A negative shock to the ﬁrm’s prospects probably does not reduce the value of the investor’s human capital; it may just mean that employment in the ﬁrm will grow less rapidly. In contrast, a negative shock to a distressed ﬁrm more likely implies a negative shock to the value of human capital since employment in the ﬁrm is more likely to contract. Thus, workers with specialized human capital in distressed ﬁrms have an incentive to avoid holding their ﬁrms’ stocks. If variation in distress is correlated across ﬁrms, workers in distressed ﬁrms have an incentive to avoid the stocks of all distressed ﬁrms. The result can be a state-variable risk premium in the expected returns of distressed stocks.” (p.77).

An alternative possibility is that investors have not understood the relation between our predictive variables and failure risk, and so have not discounted the prices of high-risk stocks enough to oﬀset their failure probability. In this case we will ﬁnd that failure risk appears to command a negative risk premium during our sample period. This expectation is consistent with the high failure risk of volatile stocks, since Ang, Hodrick, Xing, and Zhang (2005) have recently found negative average returns for stocks with high idiosyncratic volatility.

We measure the premium for ﬁnancial distress by sorting stocks according to their failure probabilities, estimated using the 12-month-ahead model of Table 4. Each January from 1981 through 2003, the model is reestimated using only historically available data to eliminate look-ahead bias. We then form ten value-weighted portfolios of stocks that fall in diﬀerent regions of the failure risk distribution. We minimize turnover costs and the eﬀects of bid-ask bounce by eliminating stocks with prices less than $1 at the portfolio construction date, and by holding the portfolios for a year, allowing the weights to drift with returns within the year rather than rebalancing monthly in response to updated failure probabilities.9 Our portfolios contain stocks in percentiles 0—5, 5—10, 10—20, 20—40, 40—60, 60—80, 80—90, 90—95, 95—99, and 99—100 of the failure risk distribution. This portfolio construction procedure pays greater attention to the tails of the distribution, where the distress premium is likely to be more relevant, and particularly to the most distressed ﬁrms. We also construct long-short portfolios that go long the 10% or 20% of stocks with the lowest failure risk, and short the 10% or 20% of stocks with the highest failure risk.

Because we are studying the returns to distressed stocks, it is important to handle carefully the returns to stocks that are delisted and thus disappear from the CRSP database. In many cases CRSP reports a delisting return for the ﬁnal month of the ﬁrm’s life; we have 6,481 such delisting returns in our sample and we use them where they are available. Otherwise, we use the last available full-month return in CRSP. In some cases this eﬀectively assumes that our portfolios sell distressed stocks

- at the end of the month before delisting, which imparts an upward bias to the returns on distressed-stock portfolios (Shumway 1997, Shumway and Warther 1999).10 We assume that the proceeds from sales of delisted stocks are reinvested in each portfolio in proportion to the weights of the remaining stocks in the portfolio. In a few cases,

- 9In the ﬁrst version of this paper we calculated returns on portfolios rebalanced monthly, and

obtained similar results to those reported here.

- 10In the ﬁrst version of this paper we did not use CRSP delisting returns. The portfolio results

were similar to those reported here.

stocks are delisted and then re-enter the database, but we do not include these stocks in the sample after the ﬁrst delisting. We treat ﬁrms that fail as equivalent to delisted ﬁrms, even if CRSP continues to report returns for these ﬁrms. That is, our portfolios sell stocks of companies that fail and we use the latest available CRSP data to calculate a ﬁnal return on such stocks.

Table 6 reports the results. Each portfolio corresponds to one column of the table. Panel A reports average returns in excess of the market, in annualized percentage points, with t statistics below in parentheses, and then alphas with respect to the CAPM, the three-factor model of Fama and French (1993), and a four-factor model proposed by Carhart (1997) that also includes a momentum factor. Panel B reports estimated factor loadings for excess returns on the three Fama-French factors, again with t statistics. Panel C reports some relevant characteristics for the portfolios: the annualized standard deviation and skewness of each portfolio’s excess return, the value-weighted mean standard deviation and skewness of the individual stock returns in each portfolio, and value-weighted means of RSIZE, market-book, and estimated failure probability for each portfolio. Figures 2 and 3 graphically summarize the behavior of factor loadings and alphas.

The average excess returns reported in the ﬁrst row of Table 6 are strongly and almost monotonically declining in failure risk. The average excess returns for the lowest-risk 5% of stocks are positive at 3.4% per year, and the average excess returns for the highest-risk 1% of stocks are signiﬁcantly negative at -17.0% per year. A long-short portfolio holding the safest decile of stocks and shorting the most distressed decile has an average return of 10.0% per year and a standard deviation of 26%, so its Sharpe ratio is comparable to that of the aggregate stock market.

There is striking variation in factor loadings across the portfolios in Table 6. The low-failure-risk portfolios have negative market betas for their excess returns (that is, betas less than one for their raw returns), negative loadings on the value factor HML, and negative loadings on the small ﬁrm factor SMB. The high-failure-risk portfolios have positive market betas for their excess returns, positive loadings on HML, and extremely high loadings on SMB, reﬂecting the role of market capitalization in predicting bankruptcies at medium and long horizons.

These factor loadings imply that when we correct for risk using either the CAPM or the Fama-French three-factor model, we worsen the anomalous poor performance of distressed stocks rather than correcting it. A long-short portfolio that holds the safest decile of stocks and shorts the decile with the highest failure risk has an average

excess return of 10.0% with a t statistic of 1.9; it has a CAPM alpha of 12.4% with a t statistic of 2.3; and it has a Fama-French three-factor alpha of 22.7% with a t statistic of 6.1. When we use the Fama-French model to correct for risk, all portfolios beyond the 60th percentile of the failure risk distribution have statistically signiﬁcant negative alphas.

One of the variables that predicts failure in our model is recent past return. This suggests that distressed stocks have negative momentum, which might explain their low average returns. To control for this, Table 6 also reports alphas from the Carhart (1997) four-factor model including a momentum factor. This adjustment cuts the alpha for the long-short decile portfolio roughly in half, from 22.7% to 12.0%, but it remains strongly statistically signiﬁcant.

Figure 4 illustrates the performance over time of the long-short portfolios that hold the safest decile (quintile) of stocks and short the most distressed decile (quintile). Performance is measured both by cumulative return, and by cumulative alpha or riskadjusted return from the Fama-French three-factor model. For comparison, we also plot the cumulative return on the market portfolio. Raw returns to these portfolios are concentrated in the late 1980’s and late 1990’s, with negative returns in the last few years; however the alphas for these portfolios are much more consistent over time.

The bottom panel of Table 6 reports characteristics of these portfolios. There is a wide spread in failure risk across the portfolios. Stocks in the safest 5% have an average failure probability of about 1 basis point, while stocks in the riskiest 5% have a failure probability of 34 basis points and the 1% of riskiest stocks have a failure probability of 80 basis points.

Stocks with a high risk of failure are highly volatile, with average standard deviations of almost 80% in the 5% most distressed stocks and 95% in the 1% most distressed stocks. This volatility does not fully diversify at the portfolio level.11 The excess return on the portfolio containing the 5% of stocks with the lowest failure risk has an annual standard deviation of 11%, while the excess return for the portfolio containing the 5% of stocks with the highest failure risk has a standard deviation of 26%, and the concentrated portfolio containing the 1% most distressed stocks has a

11On average there are slightly under 500 stocks for each 10% of the failure risk distribution, so purely idiosyncratic ﬁrm-level risk should diversify well, leaving portfolio risk to be determined primarily by common variation in distressed stock returns.

standard deviation of almost 40%. The returns on distressed stocks are also positively skewed, both at the portfolio level and particularly at the individual stock level.

Distressed stocks are much smaller than safe stocks. The value-weighted average size of the 5% safest stocks, reported in the table, is over 16 times larger than the value-weighted average size of the 5% most distressed stocks, and the equal-weighted size is about 9 times larger. Market-book ratios are high at both extremes of the failure risk distribution, and lower in the middle. This implies that distressed stocks have the market-book ratios of growth stocks, but the factor loadings of value stocks, since they load positively on the Fama-French value factor.

The wide spread in ﬁrm characteristics across the failure risk distribution suggests the possibility that the apparent underperformance of distressed stocks results from their characteristics rather than from ﬁnancial distress per se. For example, it could be the case that extremely small stocks underperform in a manner that is not captured by the Fama-French three-factor model. To explore this possibility, in Table 7 we double-sort stocks, ﬁrst on size using NYSE quintile breakpoints, and then on failure risk. In Table 8 we double-sort, ﬁrst on the book-market ratio using NYSE quintile breakpoints, and then on failure risk.

- Table 7 shows that distressed stocks underperform whether they are small stocks or large stocks. The underperformance is, however, considerably stronger among small stocks. The average return diﬀerence between the safest and most distressed quintiles is three times larger when the stocks are in the smallest quintile as opposed to the largest quintile. If we correct for risk using the Fama-French three-factor model, the alpha diﬀerence between the safest and most distressed quintiles is about 50% greater in the smallest quintile than in the largest quintile. The table also shows that in this sample period, there is only a weak size eﬀect among safe stocks, and among distressed stocks large stocks outperform small stocks.
- Table 8 shows that distressed stocks underperform whether they are growth stocks or value stocks. The raw underperformance is more extreme and statistically significant among growth stocks, but this diﬀerence disappears when we correct for risk using the Fama-French three-factor model. The value eﬀect is absent in the safest stocks, similar to a result reported by Griﬃn and Lemmon (2002) using Ohlson’s Oscore to proxy for ﬁnancial distress. However this result may result from diﬀerences in three-factor loadings, as it largely disappears when we correct for risk using the three-factor model.

As a ﬁnal speciﬁcation check, we have sorted stocks on our measure of distance to default. Contrary to the ﬁndings of Vassalou and Xing (2004), this sort also generates low returns for distressed stocks, particularly after correction for risk using the Fama-French three-factor model.

Overall, these results are discouraging for the view that distress risk is positively priced in the US stock market. We ﬁnd that stocks with a high risk of failure have low average returns, despite their high loadings on small-cap and value risk factors.

###### 5 Conclusion

This paper makes two main contributions to the literature on ﬁnancial distress. First, we carefully implement a reduced-form econometric model to predict corporate bankruptcies and failures at short and long horizons. Our best model has greater explanatory power than the existing state-of-the-art models estimated by Shumway (2001) and Chava and Jarrow (2004), and includes additional variables with sensible economic motivation. We believe that models of the sort estimated here have meaningful empirical advantages over the bankruptcy risk scores proposed by Altman (1968) and Ohlson (1980). While Altman’s Z-score and Ohlson’s O-score were seminal early contributions, better measures of bankruptcy risk are available today. We have also presented evidence that failure risk cannot be adequately summarized by a measure of distance to default inspired by Merton’s (1974) pioneering structural model. While our distance to default measure is not exactly the same as those used by Crosbie and Bohn (2001) and Vassalou and Xing (2004), we believe that this result, similar to that reported independently by Bharath and Shumway (2004), is robust to alternative measures of distance to default.

Second, we show that stocks with a high risk of failure tend to deliver anomalously low average returns. We sort stocks by our 12-month-ahead estimate of failure risk, calculated from a model that uses only historically available data at each point in time. We calculate returns and risks on portfolios sorted by failure risk over the period 1981-2003. Distressed portfolios have low average returns, but high standard deviations, market betas, and loadings on Fama and French’s (1993) small-cap and value risk factors. Thus, from the perspective of any of the leading empirical asset pricing models, these stocks have negative alphas. This result is a signiﬁcant challenge to the conjecture that the value and size eﬀects are proxies for a ﬁnancial distress premium. More generally, it is a challenge to standard models of rational asset pricing in which the structure of the economy is stable and well understood by investors.

Some previous authors have reported evidence that distressed stocks underperform the market, but results have varied with the measure of ﬁnancial distress that is used. Our results are consistent with the ﬁndings of Dichev (1998), who uses Altman’s Z-score and Ohlson’s O-score to measure ﬁnancial distress, and Garlappi, Shu, and Yan (2005), who obtain default risk measures from Moody’s KMV. Vassalou and Xing (2004) calculate distance to default; they ﬁnd some evidence that distressed stocks with a low distance to default have higher returns, but this evidence

comes entirely from small value stocks. Da and Gao (2004) argue that Vassalou and Xing’s distressed-stock returns are biased upwards by one-month reversal and bid-ask bounce. Griﬃn and Lemmon (2002), using O-score to measure distress, ﬁnd that distressed growth stocks have particularly low returns. Our measure of ﬁnancial distress generates underperformance among distressed stocks in all quintiles of the size and value distributions, but the underperformance is more dramatic among small stocks.

What can explain the anomalous underperformance of distressed stocks? Perhaps the most obvious explanation is that stock market investors underreact to negative information about company prospects. Hong, Lim, and Stein (2000) have argued that corporate managers have incentives to withhold bad news, which therefore reaches the market only gradually. Equity analysts can speed up the ﬂow of information, but do so only for larger companies with better analyst coverage. To test whether this hypothesis explains the distress anomaly, one could ask whether the underperformance of distressed stocks is more extreme for companies with low analyst coverage. According to this view, the distress anomaly is related to the momentum eﬀect and to the underperformance of companies with underfunded pension plans (Franzoni and Marin 2005).

Some investors may understand the poor average returns oﬀered by distressed stocks, but hold them anyway. von Kalckreuth (2005) argues that majority owners of distressed companies can extract private beneﬁts, for example by buying the company’s output or assets at bargain prices. The incentive to extract such beneﬁts is greater when the company is unlikely to survive and generate future proﬁts for its shareholders. Thus majority owners may hold distressed stock, rather than selling it, because they earn a greater return than the return we measure to outside shareholders.

Barberis and Huang (2004) model the behavior of investors whose preferences satisfy the cumulative prospect theory of Tversky and Kahneman (1992). Such investors have a strong desire to hold positively skewed portfolios, and may even hold undiversiﬁed positions in positively skewed assets. Barberis and Huang argue that this eﬀect can explain the high prices and low average returns on IPO’s, whose returns are positively skewed. It is striking that both individual distressed stocks and our portfolios of distressed stocks also oﬀer returns with strong positive skewness.

These hypotheses have the potential to explain why some investors hold distressed stocks despite their low average returns, but they do not explain why other rational

investors fail to arbitrage the distress anomaly. Some distressed stocks may be unusually expensive or diﬃcult to short, but more important limits to arbitrage are likely to be the reluctance of some investors to short stocks and the limited capital that arbitrageurs have available.

Finally, the distress anomaly may result from the preferences of institutional investors, together with a shift of assets from individuals to institutions during our sample period. Kovtunenko and Sosner (2003) have documented that institutions prefer to hold proﬁtable stocks, and that this preference helped institutional performance during the 1980’s and 1990’s because proﬁtable stocks outperformed the market. It is possible that the strong performance of proﬁtable stocks in this period was endogenous, the result of increasing demand for these stocks by institutions. If institutions more generally prefer stocks with low failure risk, and tend to sell stocks that enter ﬁnancial distress, then a similar mechanism could drive our results. This hypothesis implies that the underperformance of distressed stocks is a transitional and temporary phenomenon. It can be tested by relating the performance of distressed stocks over time to the changing institutional share of equity ownership and the characteristics of institutional portfolios.

###### Appendix

In this appendix we discuss issues related to the construction of our dataset. All variables are constructed using COMPUSTAT and CRSP data. Relative size, excess return, and accounting ratios are deﬁned as follows:

¶

RSIZEi,t = log µ

Firm Market Equityi,t Total S&P500 Market V aluet

EXRETi,t = log(1 + Ri,t) − log(1 + RS&P500,t) NITAi,t =

Net Incomei,t Total Assets(adjusted)i,t TLTAi,t =

Total Liabilitiesi,t Total Assets(adjusted)i,t NIMTAi,t =

Net Incomei,t (Firm Market Equityi,t + Total Liabilitiesi,t) TLMTAi,t =

Total Liabilitiesi,t (Firm Market Equityi,t + Total Liabilitiesi,t) CASHMTAi,t =

Cash and Short Term Investmentsi,t (Firm Market Equityi,t + Total Liabilitiesi,t)

The COMPUSTAT quarterly data items used are Data44 for total assets, Data69 for net income, and Data54 for total liabilities.

To deal with outliers in the data, we correct both NITA and TLTA using the diﬀerence between book equity (BE) and market equity (ME) to adjust the value of total assets:

Total Assets (adjusted)i,t = TAi,t + 0.1 ∗ (BEi,t − MEi,t)

Book equity is as deﬁned in Davis, Fama and French (2000) and outlined in detail in Cohen, Polk and Vuolteenaho (2003). This transformation helps with the values of total assets that are very small, probably mismeasured and lead to very large values of NITA. After total assets are adjusted, each of the seven explanatory variables is winsorized using a 5/95 percentile interval in order to eliminate outliers.

To measure the volatility of a ﬁrm’s stock returns, we use a proxy, centered around zero rather than the rolling three-month mean, for daily variation of returns computed

as an annualized three-month rolling sample standard deviation:

 252 ∗

 

- 1

- 2

1 N − 1 X

ri,k2

SIGMAi,t−1,t−3 =

k∈{t−1,t−2,t−3}

To eliminate cases where few observations are available, SIGMA is coded as missing if there are fewer than ﬁve non-zero observations over the three months used in the rolling-window computation. In calculating summary statistics and estimating regressions, we replace missing SIGMA observations with the cross-sectional mean of SIGMA; this helps us avoid losing some failure observations for infrequently traded companies. A dummy for missing SIGMA does not enter our regressions signiﬁcantly. We use a similar procedure for missing lags of NIMTA and EXRET in constructing the moving average variables NIMTAAVG and EXRETAVG.

In order to calculate distance to default we need to estimate asset value and asset volatility, neither of which are directly observable. We construct measures of these variables by solving two equations simultaneously.

First, in the Merton model equity is valued as a European call option on the value of the ﬁrm’s assets. Then:

ME = TADDN (d1) − BD exp(−RBILLT)N (d2) d1 =

BD ¢

¡

¢

¡TA

RBILL + 12SIGMA2DD

+

T SIGMADD√T

log

DD

√

d2 = d1 − SIGMADD

T,

where TADD is the value of assets, SIGMADD is the volatility of assets, ME is the value of equity, and BD is the face value of debt maturing at time T. Following convention in the literature on the Merton model (Crosbie and Bohn 2001, Vassalou and Xing 2004), we assume T = 1, and use short term plus one half long term book debt to proxy for the face value of debt BD. This convention is a simple way to take account of the fact that long-term debt may not mature until after the horizon of the distance to default calculation. We measure the risk free rate RBILL as the Treasury bill rate.

The second equation is a relation between the volatility of equity and the volatility of assets, often referred to as the optimal hedge equation:

TADD ME

SIGMADD.

SIGMA = N (d1)

As starting values for asset value and asset volatility, we use TADD = ME+BD, and SIGMADD = SIGMA(ME/(ME + BD)).12 We iterate until we have found values for TADD and SIGMADD that are consistent with the observed values of ME, BD, and SIGMA.

Finally, we compute distance to default as

DD = −log(BD/TADD) + 0.06 + RBILL − 12SIGMA2DD SIGMADD

.

The number 0.06 appears in the formula as an empirical proxy for the equity premium. Vassalou and Xing (2004) instead estimate the average return on each stock, while Hillegeist, Keating, Cram, and Lunstedt (2004) calculate the drift as the return on assets during the previous year. If the estimated expected return is negative, they replace it with the riskfree interest rate. We believe that it is better to use a common expected return for all stocks than a noisily estimated stock-speciﬁc number.

12If BD is missing, we use BD = median(BD/TL) ∗ TL, where the median is calculated for the entire data set. This captures the fact that empirically, BD tends to be much smaller than TL. If BD = 0, we use BD = median(BD/TL) ∗ TL, where now we calculate the median only for small but nonzero values of BD (0 < BD < 0.01). If SIGMA is missing, we replace it with its cross sectional mean. Before calculating asset value and volatility, we adjust BD so that BD/(ME+BD) is winsorized at the 0.5% level. We also winsorize SIGMA at the 0.5% level. This signiﬁcantly reduces instances in which the search algorithm does not converge.

###### References

Altman, Edward I., 1968, Financial ratios, discriminant analysis and the prediction of corporate bankruptcy, Journal of Finance 23, 589—609.

Ang, Andrew, Robert J. Hodrick, Yuhang Xing, and Xiaoyan Zhang, 2005, The cross-section of volatility and expected returns, forthcoming Journal of Finance.

Asquith, Paul, Robert Gertner, and David Scharfstein, 1994, Anatomy of ﬁnancial distress: An examination of junk-bond issuers, Quarterly Journal of Economics 109, 625—658.

Barberis, Nicholas and Ming Huang, 2004, Stocks as lotteries: The implications of probability weighting for security prices, unpublished paper, Yale University and Stanford University.

Bernanke, Ben S. and John Y. Campbell, 1988, Is there a corporate debt crisis?, Brookings Papers on Economic Activity 1, 83—139.

Bharath, Sreedhar and Tyler Shumway, 2004, Forecasting default with the KMVMerton model, unpublished paper, University of Michigan.

Burgstahler, D.C. and I.D. Dichev, 1997, Earnings management to avoid earnings decreases and losses, Journal of Accounting and Economics 24, 99—126.

Campbell, John Y., Martin Lettau, Burton Malkiel, and Yexiao Xu, 2001, Have individual stocks become more volatile? An empirical exploration of idiosyncratic risk, Journal of Finance 56, 1—43.

Carhart, Mark, 1997, On persistence in mutual fund performance, Journal of Finance 52, 57—82.

Chacko, George, Peter Hecht, and Jens Hilscher, 2004, Time varying expected returns, stochastic dividend yields, and default probabilities, unpublished paper, Harvard Business School.

Chan, K.C. and Nai-fu Chen, 1991, Structural and return characteristics of small and large ﬁrms, Journal of Finance 46, 1467—1484.

Chava, Sudheer and Robert A. Jarrow, 2004, Bankruptcy prediction with industry eﬀects, Review of Finance 8, 537—569.

Cohen, Randolph B., Christopher Polk and Tuomo Vuolteenaho, 2003, The value spread, Journal of Finance 58, 609—641.

Crosbie, Peter J. and Jeﬀrey R. Bohn, 2001, Modeling Default Risk, KMV, LLC, San Francisco, CA.

Da, Zhi and Pengjie Gao, 2004, Default risk and equity return: macro eﬀect or micro noise?, unpublished paper, Northwestern University.

Davis, James L., Eugene F. Fama and Kenneth R. French, 2000, Characteristics, covariances, and average returns: 1929 to 1997, Journal of Finance 55, 389406.

Dechow, Patricia M., Scott A. Richardson, and Irem Tuna, 2003, Why are earnings kinky? An examination of the earnings management explanation, Review of Accounting Studies 8, 355—384.

Dichev, Ilia, 1998, Is the risk of bankruptcy a systematic risk?, Journal of Finance 53, 1141—1148.

Duﬃe, Darrell, and Ke Wang, 2004, Multi-period corporate failure prediction with stochastic covariates, NBER Working Paper No. 10743.

Fama, Eugene F. and Kenneth R. French, 1993, Common risk factors in the returns on stocks and bonds, Journal of Financial Economics 33, 3—56.

Fama, Eugene F. and Kenneth R. French, 1996, Multifactor explanations of asset pricing anomalies, Journal of Finance 51, 55—84.

Ferguson, Michael F. and Richard L. Shockley, 2003, Equilibrium “anomalies”, Journal of Finance 58, 2549—2580.

Franzoni, Francesco and Jose M. Marin, 2005, Pension plan funding and stock market eﬃciency, forthcoming Journal of Finance.

Garlappi, Lorenzo, Tao Shu, and Hong Yan, 2005, Default risk and stock returns, unpublished paper, University of Texas at Austin.

Gilson, Stuart C., Kose John, and Larry Lang, 1990, Troubled debt restructurings: An empirical study of private reorganization of ﬁrms in default, Journal of Financial Economics 27, 315—353.

Gilson, Stuart C., 1997, Transactions costs and capital structure choice: Evidence from ﬁnancially distressed ﬁrms, Journal of Finance 52, 161—196.

Griﬃn, John M. and Michael L. Lemmon, 2002, Book-to-market equity, distress risk, and stock returns, Journal of Finance 57, 2317—2336.

Hayn, C., 1995, The information content of losses, Journal of Accounting and Economics 20, 125—153.

Hwang, C.Y., 1995, Microstructure and reverse splits, Review of Quantitative Finance and Accounting 5, 169—177.

Hillegeist, Stephen A., Elizabeth Keating, Donald P. Cram and Kyle G. Lunstedt, 2004, Assessing the probability of bankruptcy, Review of Accounting Studies 9, 5—34.

Hong, Harrison, Terence Lim, and Jeremy C. Stein, 2000, Bad news travels slowly: Size, analyst coverage, and the proﬁtability of momentum strategies, Journal of Finance 55, 265—295.

Kovtunenko, Boris and Nathan Sosner, 2003, Sources of institutional performance, unpublished paper, Harvard University.

Macey, Jonathan, Maureen O’Hara, and David Pompilio, 2004, Down and out in the stock market: the law and ﬁnance of the delisting process, unpublished paper, Yale University and Cornell University.

Merton, Robert C., 1974, On the pricing of corporate debt: the risk structure of interest rates, Journal of Finance 29, 449—470.

Mossman, Charles E., Geoﬀrey G. Bell, L. Mick Swartz, and Harry Turtle, 1998, An empirical comparison of bankruptcy models, Financial Review 33, 35—54.

Ohlson, James A., 1980, Financial ratios and the probabilistic prediction of bankruptcy, Journal of Accounting Research 18, 109—131.

Opler, Tim and Sheridan Titman, 1994, Financial distress and corporate performance, Journal of Finance 49, 1015—1040.

Shumway, Tyler, 1997, The delisting bias in CRSP data, Journal of Finance 52, 327—340.

Shumway, Tyler, 2001, Forecasting bankruptcy more accurately: a simple hazard model, Journal of Business 74, 101—124.

Shumway, Tyler and Vincent A. Warther, 1999, The delisting bias in CRSP’s Nasdaq data and its implications for the size eﬀect, Journal of Finance 54, 2361—2379.

Tashjian, Elizabeth, Ronald Lease, and John McConnell, 1996, Prepacks: An empirical analysis of prepackaged bankruptcies, Journal of Financial Economics 40, 135—162.

Tversky, Amos and Daniel Kahneman, 1992, Advances in prospect theory: Cumula-

tive representation of uncertainty, Journal of Risk and Uncertainty 5, 297—323. Vassalou, Maria and Yuhang Xing, 2004, Default risk in equity returns, Journal of

Finance 59, 831—868. von Kalckreuth, Ulf, 2005, A ‘wreckers theory’ of ﬁnancial distress, Deutsche Bundesbank discussion paper. Woolridge, J.R. and D.R. Chambers, 1983, Reverse splits and shareholder wealth, Financial Management 5—15.

Zmijewski, Mark E., 1984, Methodological issues related to the estimation of ﬁnancial distress prediction models, Journal of Accounting Research 22, 59—82.

###### Table 1: Number of bankruptcies and failures per year

The table lists the total number of active firms (Column 1), total number of bankruptcies (Column 2) and failures (Column 4) for every year of our sample period. The number of active firms is computed by averaging over the numbers of active firms across all months of the year.

###### Year Active Firms Bankruptcy (%) Failure (%)

- 1963 1281 0 0.00 0 0.00
- 1964 1357 2 0.15 2 0.15
- 1965 1436 2 0.14 2 0.14
- 1966 1513 1 0.07 1 0.07
- 1967 1598 0 0.00 0 0.00
- 1968 1723 0 0.00 0 0.00
- 1969 1885 0 0.00 0 0.00
- 1970 2067 5 0.24 5 0.24
- 1971 2199 4 0.18 4 0.18
- 1972 2650 8 0.30 8 0.30
- 1973 3964 6 0.15 6 0.15
- 1974 4002 18 0.45 18 0.45
- 1975 4038 5 0.12 5 0.12
- 1976 4101 14 0.34 14 0.34
- 1977 4157 12 0.29 12 0.29
- 1978 4183 14 0.33 15 0.36
- 1979 4222 14 0.33 14 0.33
- 1980 4342 26 0.60 26 0.60
- 1981 4743 23 0.48 23 0.48
- 1982 4995 29 0.58 29 0.58
- 1983 5380 50 0.93 50 0.93
- 1984 5801 73 1.26 74 1.28
- 1985 5912 76 1.29 77 1.30
- 1986 6208 95 1.53 95 1.53
- 1987 6615 54 0.82 54 0.82
- 1988 6686 84 1.26 85 1.27
- 1989 6603 74 1.12 78 1.18
- 1990 6515 80 1.23 82 1.26
- 1991 6571 70 1.07 73 1.11
- 1992 6914 45 0.65 50 0.72
- 1993 7469 36 0.48 39 0.52
- 1994 8067 30 0.37 33 0.41
- 1995 8374 43 0.51 45 0.54
- 1996 8782 32 0.36 34 0.39
- 1997 9544 44 0.46 61 0.64
- 1998 9844 49 0.50 150 1.52
- 1999 9675 . . 209 2.16
- 2000 9426 . . 167 1.77
- 2001 8817 . . 324 3.67
- 2002 8242 . . 221 2.68
- 2003 7833 . . 167 2.13

shortterminvestmentsoverthemarketvalueoftotalassets(CASHMTA),market-to-bookvalueofthefirm(MB)andlogofpricepersharewinsorizedabove$15

Thetablesincludethefollowingvariables(variousadjustmentsaredescribedinthedatadescriptionsection):netincomeoverbookvalueoftotalassets(NITA),

(TLMTA),logofgrossexcessreturnovervalueweightedS&P500return(EXRET)annualized,i.e.log(1+simpleexcessreturn),logoffirm’smarketequityover

NITANIMTATLTATLMTAEXRETRSIZESIGMACASHMTAMBPRICE

NITANIMTATLTATLMTAEXRETRSIZESIGMACASHMTAMBPRICE

NITANIMTATLTATLMTAEXRETRSIZESIGMACASHMTAMBPRICE

Median-0.054-0.0470.8720.861-0.171-12.8761.2550.0211.018-0.065

Median-0.066-0.0620.8210.842-0.179-13.5681.3530.0290.751-0.065

Min-0.102-0.0690.0830.036-0.243-13.5680.1530.0020.358-0.065

(PRICE).Marketvalueoftotalassetswascomputedbyaddingmarketvalueoffirmequitytoitstotalliabilities.Thefirstgroupreportssummarystatisticsforall

Max0.0390.0280.9310.9230.218-6.7731.3530.3586.4712.708

Mean-0.0010.0000.5060.445-0.011-10.4560.5620.0842.0412.019

Mean-0.054-0.0400.7960.763-0.115-12.4161.0610.0442.4300.432

Mean-0.059-0.0440.7380.731-0.105-12.8321.1670.0722.1040.277

St.Dev0.0340.0230.2520.2800.1171.9220.3320.0971.5790.883

St.Dev0.0430.0300.1740.2100.1481.3450.3520.0622.5090.760

St.Dev0.0430.0300.2280.2390.1621.1680.3030.0992.3890.643

Median0.0070.0060.5110.427-0.009-10.5700.4710.0451.5572.474

firm-monthobservationsandtheothertwoforbankruptcyandfailuregrups.Wehaveatotalof1,695,036observations,ofwhich797arebankruptcyand1614

thetotalvaluationofS&P500(RSIZE),squarerootofasumofsquaredfirmstockreturnsoverathree-monthperiod(annualized)(SIGMA),stockofcashand

netincomeovermarketvalueoftotalassets(NIMTA),totalliabilitiesoverbookvalueoftotaltssets(TLTA),totalliabilitiesovermarketvalueoftotalassets

arefailureevents.Inbothcases,thepanelsonlycontainstatisticsforvalueswhereallvariableswerenon-missing.

###### Table2:Summarystatistics

Observations:1,695,036

Observations:1614

Bankruptcygroup

Observations:797

Entiredataset

Failuregroup

###### Table 3: Logit regressions on predictor variables

This table reports results from logit regressions of the bankruptcy and failure indicator on predictor variables. The value of the predictor variable is known at the beginning of the month over which bankruptcy is measured. Net income and total liabilities are scaled by accounting and market total assets.

(1) (2) (3) (4) (5) (6)

Dep variable: Bankruptcy Failure Failure Bankruptcy Failure Failure Sample period: 1963-1998 1963-1998 1963-2003 1963-1998 1963-1998 1963-2003

NITA -14.05 -13.79 -12.782

(16.03)** (17.06)** (21.26)**

NIMTAAVG -32.518 -32.457 -29.672

(17.65)** (19.01)** (23.37)** TLTA 5.378 4.62 3.744

(25.91)** (26.28)** (32.32)**

TLMTA 4.322 3.865 3.36

(22.82)** (23.39)** (27.80)** EXRET -3.297 -2.903 -2.319

(12.12)** (11.81)** (13.57)**

EXRETAVG -9.51 -8.819 -7.35

(12.05)** (12.08)** (14.03)** SIGMA 2.148 2.28 2.763 0.92 1.15 1.482

(16.40)** (18.34)** (26.63)** (6.66)** (8.79)** (13.54)** RSIZE -0.188 -0.253 -0.374 0.246 0.169 0.082

(5.56)** (7.60)** (13.26)** (6.18)** (4.32)** (2.62)** CASHMTA -4.888 -3.218 -2.401

(7.96)** (6.59)** (8.64)** MB 0.099 0.095 0.054

(6.72)** (6.76)** (4.87)** PRICE -0.882 -0.807 -0.937

(10.39)** (10.09)** (14.77)** Constant -15.214 -15.41 -16.576 -7.648 -8.45 -9.079

(39.45)** (40.87)** (50.92)** (13.66)** (15.63)** (20.84)** Observations 1282853 1302564 1695036 1282853 1302564 1695036 Failures 797 911 1614 797 911 1614 Pseudo R sq 0.260 0.258 0.270 0.299 0.296 0.312 Absolute value of z statistics in parentheses

* significant at 5%; ** significant at 1%

Table 4: Logit regressions on lagged variables

The table below takes our best-model variables and tests their predictive power as we lag them by 6, 12, 24, and 36 months. The dependent variable is failure and the sample period is 1963-2003.

(1) (2) (3) (4) (5) Lag (months) 0 6 12 24 36 NIMTAAVG -29.672 -23.915 -20.264 -13.232 -14.061

(23.37)** (21.82)** (18.09)** (10.50)** (9.77)** TLMTA 3.36 2.057 1.416 0.917 0.643

(27.80)** (22.63)** (16.23)** (9.85)** (6.25)** EXRETAVG -7.35 -7.792 -7.129 -5.607 -2.564

(14.03)** (15.97)** (14.15)** (10.14)** (4.14)** SIGMA 1.482 1.268 1.411 1.515 1.334

(13.54)** (14.57)** (16.49)** (16.92)** (13.54)** RSIZE 0.082 0.047 -0.045 -0.132 -0.18

(2.62)** (2.02)* (2.09)* (6.19)** (8.03)** CASHMTA -2.401 -2.397 -2.132 -1.37 -1.414

(8.64)** (9.77)** (8.53)** (5.09)** (4.61)** MB 0.054 0.047 0.075 0.108 0.125

(4.87)** (4.22)** (6.33)** (7.92)** (8.17)** PRICE -0.937 -0.468 -0.058 0.212 0.279

(14.77)** (10.36)** (1.40) (4.96)** (6.00)** Constant -9.079 -8.069 -9.164 -10.233 -10.534

(20.84)** (25.00)** (30.89)** (34.48)** (33.53)** Observations 1695036 1642006 1565634 1384951 1208610 Failures 1614 2008 1968 1730 1467 Pseudo R sq 0.312 0.188 0.114 0.061 0.044 Absolute value of z statistics in parentheses

* significant at 5%; ** significant at 1%

###### Table 5: Distance to default and our best model

In panel A we report the coefficients on distance to default variable in a logit regression by itself and included in our best model. The dependent variable is failure and the sample period is 1963-2003. Regression results are reported for various horizons: 0, 12, and 36 months. Panel B reports the in-sample and out-of-sample pseudo-R squared for the regressions from panel A.

###### Panel A - Coefficients

(1) (2) (3) Lag (months) 0 12 36 DD only -0.883 -0.345 -0.165

(39.73)** (33.73)** (20.88)** DD in best model 0.048 -0.091 -0.09

(2.62)** (7.52)** (8.09)** Observations 1695036 1565634 1208610 Failures 1614 1968 1467

###### Panel B - R squared

(1) (2) (3) In-sample (1963 - 2003)

DD only 0.159 0.066 0.026 Best model 0.312 0.114 0.044 DD in Best model 0.312 0.117 0.045 Out-of-sample (1981 - 2003)

DD only 0.156 0.064 0.025 Best model 0.310 0.108 0.039

###### Table 6: Returns on distressed stock portfolios

We sorted all stocks based on the predicted 12-month probability of failure and divided them into 10 portfolios based on percentile cutoffs. For example, 0 to 5th percentile (0005) and 99th to 100th percentile (9900). In the table below we show results from regressions of excess returns over the market on a constant, market return (RM), as well as three (RM, HML, SMB) and four (RM, HML, SMB, UMD) FF factor regressions. Panel A shows monthly alphas (in annualized percent units) from these regressions and the corresponding t-stat below. Panel B shows loadings on the three factors, as well as corresponding t-stats below, from the 3-factor regression. Panel C reports annualized standard deviation and skewness of individual and portfolio returns, mean relative size (RSIZE), market-to-book (MB), and probability of failure (Phat) values for each portfolio.

- Panel A - Portfolio alphas Portfolios 0005 0510 1020 2040 4060 6080 8090 9095 9599 9900 LS1090 LS2080 Mean excess return 3.44 2.38 1.31 0.98 0.58 -0.09 -4.35 -7.87 -6.30 -16.95 10.00 6.65

(1.47) (1.08) (1.11) (1.08) (0.39) (0.04) (1.23) (1.68) (1.17) (2.05)* (1.86) (1.51) CAPM alpha 2.80 2.05 1.45 1.55 0.54 -1.45 -6.58 -10.77 -9.22 -19.32 12.44 8.92

- (1.19) (0.93) (1.22) (1.75) (0.36) (0.64) (1.92) (2.36)* (1.74) (2.33)* (2.34)* (2.06)*

- 3-factor alpha 5.76 5.31 2.71 0.82 -2.06 -5.70 -12.63 -17.95 -15.87 -24.89 22.72 17.37

(2.97)** (2.86)** (2.40)* (1.02) (1.66) (3.22)** (4.60)** (5.69)** (3.85)** (3.42)** (6.10)** (5.39)**

- 4-factor alpha 2.43 2.67 1.56 2.07 0.73 -1.14 -5.72 -9.80 -7.98 -21.07 12.01 8.14 (1.22) (1.38) (1.30) (2.50)* (0.59) (0.66) (2.13)* (3.19)** (1.90) (2.71)** (3.40)** (2.66)**

- Panel B - 3-factor regression coefficients Portfolios 0005 0510 1020 2040 4060 6080 8090 9095 9599 9900 LS1090 LS2080 RM -0.083 -0.111 -0.058 -0.028 0.104 0.334 0.480 0.477 0.443 0.249 -0.568 -0.554

(2.21)* (3.09)** (2.64)** (1.79) (4.34)** (9.78)** (9.05)** (7.83)** (5.56)** (1.77) (7.89)** (8.90)** HML -0.474 -0.499 -0.177 0.121 0.379 0.612 0.849 0.916 0.829 0.612 -1.394 -1.182

(9.67)** (10.61)** (6.17)** (5.98)** (12.12)** (13.69)** (12.22)** (11.49)** (7.94)** (3.33)** (14.79)** (14.51)** SMB 0.212 0.037 -0.118 -0.091 0.121 0.262 0.590 1.466 1.535 1.973 -1.394 -0.833

(3.89)** (0.70) (3.69)** (4.04)** (3.49)** (5.27)** (7.64)** (16.52)** (13.23)** (9.63)** (13.30)** (9.19)**

- Panel C - Portfolio characteristics Portfolios 0005 0510 1020 2040 4060 6080 8090 9095 9599 9900 LS1090 LS2080 Portfolio SD 0.112 0.105 0.057 0.044 0.071 0.111 0.169 0.225 0.258 0.396 0.258 0.211 Portfolio skewness 1.105 0.327 0.419 -0.265 -0.137 -0.278 1.038 1.746 2.371 1.832 Individual SD 0.361 0.351 0.305 0.289 0.308 0.371 0.511 0.685 0.793 0.949 Individual skewness 0.645 0.751 0.595 1.363 1.676 0.841 1.948 3.790 2.960 2.395 Mean RSIZE -7.786 -7.479 -7.236 -7.172 -7.371 -7.803 -8.744 -10.000 -10.584 -11.273 Mean MB 2.648 3.089 2.945 2.499 2.117 1.989 2.256 2.611 3.114 3.783 Mean Phat 0.011% 0.014% 0.018% 0.024% 0.036% 0.057% 0.11% 0.19% 0.34% 0.80%

###### Table 7: Double sorting on size and distress

This table reports mean excess returns over the market and 3-factor alphas for portfolios sorted on size (ME) and fitted 12-month fitted probability of failure (Phat). We first sort stocks into size quintiles using NYSE breakpoints (following Fama-French) and then, within each quintile, sort stocks into predicted failure probability quintiles. All returns are in annualized percent units.

- Panel A - mean excess return

|ME\Phat|Low High Low - High| |
|---|---|---|
|Large<br><br>Small<br><br>Large - Small|3.94 -1.48 -0.27 0.43 0.93<br><br>(2.02)* (1.18) (0.18) (0.29) (0.41)<br><br>4.14 0.29 2.07 0.80 1.10<br><br>(2.03)* (0.20) (1.42) (0.59) (0.43) 4.65 2.98 -0.22 1.04 0.43<br><br><br><br><br>(2.01)* (1.54) (0.15) (0.65) (0.17) 6.21 2.56 1.68 1.11 -2.40 (2.51)* (1.21) (0.80) (0.57) (0.86)<br><br>3.77 -0.30 -3.38 -5.96 -10.62 (2.18)* (1.27) (1.20) (0.29) (1.22)|3.01<br><br>(0.77)<br><br>3.04<br><br>(0.78)<br><br><br>4.22<br><br>(1.25) 8.62<br>(2.91)** 10.87<br>(3.07)**<br>|
| |-1.39 -4.63 -3.15 -0.43 6.47 (0.48) (1.47) (0.97) (0.12) (1.33)| |

- Panel B - 3-factor alpha

|ME\Phat|Low High Low - High| |
|---|---|---|
|Large<br><br>Small<br><br>Large - Small|7.51 0.30 0.39 -1.58 -4.08 (4.83)** (0.27) (0.35) (1.40) (2.42)* 6.20 0.97 1.48 -0.58 -5.37<br><br>(3.96)** (0.78) (1.05) (0.48) (2.82)** 6.13 4.10 -1.15 -0.87 -5.84<br>(4.02)** (3.11)** (1.02) (0.69) (3.85)** 6.70 2.51 0.65 -0.93 -8.52<br>(5.06)** (2.07)* (0.58) (0.85) (5.89)** 5.30 2.96 1.11 -3.02 -12.19<br><br><br>(4.36)** (2.41)* (0.93) (1.87) (4.15)**|11.59<br><br>(4.07)** 11.57<br><br>(4.05)** 11.97<br>(5.02)** 15.22<br><br><br>(7.07)** 17.49<br><br>(5.81)**<br>|
| |2.21 -2.66 -0.71 1.44 8.11 (1.23) (1.63) (0.45) (0.75) (2.61)**| |

- Table 8: Double sorting on value and distress

This table reports mean excess returns over the market and 3-factor alphas for portfolios sorted on book-tomarket (BM) and fitted 12-month fitted probability of failure (Phat). We first sort stocks into book-to-market quintiles using NYSE breakpoints (following Fama-French) and then, within each quintile, sort stocks into predicted failure probability quintiles. All returns are in annualized percent units.

- Panel A - mean excess return

|BM\Phat|Low High Low - High| |
|---|---|---|
|High<br><br>Low<br><br>High - Low|4.36 3.10 6.44 -1.09 -4.37<br><br>(2.41)* (1.33) (2.06)* (0.26) (0.81)<br><br>5.69 3.88 3.26 6.71 -0.66<br><br><br>(2.82)** (1.90) (1.56) (2.45)* (0.16) 2.55 2.15 2.25 1.12 -4.43 (1.57) (1.25) (1.29) (0.47) (1.30)<br><br>2.70 -0.27 -0.42 -0.84 -3.26<br><br>(1.33) (0.23) (0.29) (0.34) (0.90)<br><br>3.77 -0.30 -3.38 -5.96 -10.62<br><br><br>(1.72) (0.19) (1.76) (2.29)* (2.81)**|8.74 (1.51) 6.35 (1.28) 6.98 (1.83) 5.96 (1.23) 14.39 (3.01)**|
| |0.59 3.40 9.82 4.86 6.24 (0.18) (1.07) (2.80)** (1.16) (1.43)| |

- Panel B - 3-factor alpha

|BM\Phat|Low High Low - High| |
|---|---|---|
|High<br><br>Low<br><br>High - Low|4.02 0.39 0.58 -10.41 -15.48<br><br>(2.56)* (0.22) (0.23) (3.11)** (4.07)**<br><br>5.82 3.30 0.68 0.86 -9.19<br><br>(3.33)** (2.41)* (0.41) (0.43) (2.80)** 2.96 2.40 0.24 -3.18 -11.88<br><br>(1.91) (1.67) (0.16) (1.61) (4.33)** 4.53 -0.74 -2.27 -5.21 -10.46<br>(2.70)** (0.62) (1.61) (2.35)* (3.34)** 7.27 1.15 -5.12 -10.39 -18.02<br><br><br>(4.50)** (0.80) (2.70)** (4.54)** (5.96)**<br><br><br>|19.50 (4.66)** 15.01<br><br>(3.59)** 14.84<br>(4.54)** 14.99<br><br><br>(3.58)** 25.28 (6.79)**|
| |-3.24 -0.76 5.71 -0.02 2.54 (1.41) (0.33) (1.85) (0.01) (0.63)| |

###### Figure1:Predictedvs.actualfailurerates

| | |Actualfailures<br><br>Predictedfailures| | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |

- 1972
- 1973
- 1974
- 1975
- 1976
- 1977
- 1978
- 1979
- 1980
- 1981
- 1982
- 1983
- 1984
- 1985
- 1986
- 1987
- 1988
- 1989
- 1990
- 1991
- 1992
- 1993
- 1994
- 1995
- 1996
- 1997
- 1998
- 1999
- 2000
- 2001
- 2002
- 2003

0.03

0.02

0.01

0

0.035

0.025

0.015

0.005

###### Figure2:Alphasofdistressedstockportfolios

0005051010202040406060808090909595999900

3-factor

CAPM

Mean

5

0

-5

10

-10

-15

-20

-25

-30

(%)

###### Figure3:Factorloadingsofdistressedstockportfolios

0005051010202040406060808090909595999900

|RM<br><br>HML<br><br>SMB|
|---|

SMB

RM

HM

2.500

2.000

1.500

1.000

0.500

0.000

-0.500

-1.000

###### Figure4:Returnsonlong-shortdistressedstockportfolios

- 1981m1
- 1982m1
- 1983m1
- 1984m1
- 1985m1
- 1986m1
- 1987m1
- 1988m1
- 1989m1
- 1990m1
- 1991m1
- 1992m1
- 1993m1
- 1994m1
- 1995m1
- 1996m1
- 1997m1
- 1998m1
- 1999m1
- 2000m1
- 2001m1
- 2002m1
- 2003m1

Marketreturn

Alpha1090

Alpha2080

LS1090

LS2080

1

0

10

100

1000

$

