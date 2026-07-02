NBER WORKING PAPER SERIES

CREDIT MARKET SHOCKS AND ECONOMIC FLUCTUATIONS: EVIDENCE FROM CORPORATE BOND AND STOCK MARKETS

Simon Gilchrist Vladimir Yankov Egon Zakrajsek

Working Paper 14863 http://www.nber.org/papers/w14863

NATIONAL BUREAU OF ECONOMIC RESEARCH 1050 Massachusetts Avenue Cambridge, MA 02138 April 2009

We thank Jean Boivin, Jon Faust, Domenico Giannone, David Lucca, Michael McCracken, Roland Meeks, Zhongjun Qu, Jonathan Wright, and seminar participants at the Federal Reserve Board, the European Central Bank, and the NBER/ME Spring 2009 meeting for comments and suggestions. Isaac Laughlin and Oren Ziv provided outstanding research assistance. The views expressed in this paper are solely the responsibility of the authors and should not be interpreted as reflecting the views of the Board of Governors of the Federal Reserve System, nor anyone else associated with the Federal Reserve System, nor the National Bureau of Economic Research.

NBER working papers are circulated for discussion and comment purposes. They have not been peerreviewed or been subject to the review by the NBER Board of Directors that accompanies official NBER publications.

© 2009 by Simon Gilchrist, Vladimir Yankov, and Egon Zakrajsek. All rights reserved. Short sections of text, not to exceed two paragraphs, may be quoted without explicit permission provided that full credit, including © notice, is given to the source.

Credit Market Shocks and Economic Fluctuations: Evidence from Corporate Bond and Stock Markets Simon Gilchrist, Vladimir Yankov, and Egon Zakrajsek NBER Working Paper No. 14863 April 2009 JEL No. E32,E44,G12

### ABSTRACT

To identify disruptions in credit markets, research on the role of asset prices in economic fluctuations has focused on the information content of various corporate credit spreads. We re-examine this evidence using a broad array of credit spreads constructed directly from the secondary bond prices on outstanding senior unsecured debt issued by a large panel of nonfinancial firms. An advantage of our "ground-up'' approach is that we are able to construct matched portfolios of equity returns, which allows us to examine the information content of bond spreads that is orthogonal to the information contained in stock prices of the same set of firms, as well as in macroeconomic variables measuring economic activity, inflation, interest rates, and other financial indicators. Our portfolio-based bond spreads contain substantial predictive power for economic activity and outperform—especially at longer horizons—standard default-risk indicators. Much of the predictive power of bond spreads for economic activity is embedded in securities issued by intermediate-risk rather than high-risk firms. According to impulse responses from a structural factor-augmented vector autoregression, unexpected increases in bond spreads cause large and persistent contractions in economic activity. Indeed, shocks emanating from the corporate bond market account for more than 30 percent of the forecast error variance in economic activity at the two- to four-year horizon. Overall, our results imply that credit market shocks have contributed significantly to U.S. economic fluctuations during the 1990–2008 period.

Simon Gilchrist Department of Economics Boston University 270 Bay State Road Boston, MA 02215 and NBER sgilchri@bu.edu

Vladimir Yankov Department of Economics Boston University 270 Bay State Road Boston, MA 02215 yankov@bu.edu

Egon Zakrajsek Division of Monetary Affairs Federal Reserve Board 20th Street & Constitution Avenue, NW Washington, D.C. 20551 egon.zakrajsek@frb.gov

## 1 Introduction

After markets for securitized credit products collapsed dramatically in the second half of 2007, growth in a number of industrialized economies slowed markedly, suggesting that disruptions in ﬁnancial markets can have important macroeconomic consequences. The fact that sharp and sudden deteriorations in ﬁnancial conditions are typically followed by a prolonged period of economic weakness is a feature of a growing number of economic downturns in the U.S. and abroad. During periods of credit market turmoil, ﬁnancial asset prices, owing to their forward-looking nature, are especially informative of linkages between the real and ﬁnancial sides of economy: Movements in asset prices can provide early-warning signals for such economic downturns and can be used to gauge the degree of strains in ﬁnancial markets.

Past research on the role of asset prices in signaling future economic conditions and in propagating economic ﬂuctuations has emphasized the information content of defaultrisk indicators such as corporate credit spreads—the diﬀerence in yields between various corporate debt instruments and government securities of comparable maturity—for the state of the economy and risks to the economic outlook.1 In a recent paper, Philippon [2008] provides a theoretical framework in which the predictive content of corporate bond spreads for economic activity—absent any ﬁnancial frictions—reﬂects a general decline in economic fundamentals stemming from a reduction in the expected present value of corporate cash ﬂows prior to a cyclical downturn. Rising credit spreads can also reﬂect disruptions in the supply of credit resulting from the worsening in the quality of corporate balance sheets or from the deterioration in the health of ﬁnancial intermediaries that supply credit—the ﬁnancial accelerator mechanism emphasized by Bernanke, Gertler, and Gilchrist [1999]. In this context, a contraction in credit supply causes asset values to fall, incentives to default to increase, and yield spreads on private debt instruments to widen before economic downturns, as lenders demand compensation for the expected increase in defaults.

In terms of forecasting macroeconomic conditions, the empirical success of this vein of research is considerable. Nevertheless, results vary substantially across diﬀerent ﬁnancial

1The predictive content of various corporate credit spreads for economic activity has been analyzed, among other, by Stock and Watson [1989]; Friedman and Kuttner [1998]; Duca [1999]; Emery [1999]; Gertler and Lown [1999]; Ewing, Lynch, and Payne [2003]; Mody and Taylor [2004]; and Mueller [2007]. In addition, Stock and Watson [2002b] have pointed out the ability of credit spreads to forecast economic growth using dynamic factor analysis, and King, Levin, and Perli [2007] ﬁnd that corporate bond spread indexes contain important information about the near-term likelihood of a recession. In a related vein, an extensive empirical literature has emphasized the extent to which the slope of the yield curve—the so-called term spreadprovides a signal for forecasting economic growth or for assessing the near-term risk of recession; see, for example, Dotsey [1998], Estrella and Hardouvelis [1991], Estrella and Mishkin [1998], and Hamilton and Kim [2002]. More recent work on this topic includes Ang, Piazzesi, and Wei [2006] and Wright [2006]. A comprehensive review of the literature on the role of asset prices in forecasting macroeconomic outcomes is provided by Stock and Watson [2003a].

instruments underlying the credit spreads under consideration as well as across diﬀerent time periods. For example, the spread of yields between nonﬁnancial commercial paper and comparable-maturity Treasury bills—the so-called paper-bill spread—has lost much of its forecasting power since the early 1990s.2 In contrast, yield spreads based on indexes of highyield corporate bonds, which contain information from markets that were not in existence prior to the mid-1980s, have done particularly well at forecasting output growth during the previous decade, according to Gertler and Lown [1999] and Mody and Taylor [2004]. Stock and Watson [2003b], however, ﬁnd mixed evidence for the high-yield spread as a leading indicator during this period, largely because it falsely predicted an economic downturn in the autumn of 1998. This dichotomy of ﬁndings is perhaps not surprising, because as ﬁnancial markets evolve, the information content of speciﬁc ﬁnancial assets prices may change as well. The fragility of results may also reﬂect the fact that this research has generally relied on a single credit spread index, rather than on multiple indexes reﬂecting a broad crosssection—in terms of both default risk and maturity—of private debt instruments.

In addition to focusing on a single credit spread index, researchers often ignore the information content of other asset prices when evaluating the forecasting ability of diﬀerent default-risk indicators. Although it is straightforward to control for the general level of equity prices in such analysis, it is usually not possible to obtain equity valuations of the borrowers whose debt securities are used to construct the credit spreads under consideration.3 Such information could potentially be used to distinguish movements in corporate credit spreads that are due to general trends in ﬁnancial asset prices associated with a given class of borrowers from the movements in spreads that are speciﬁcally related to developments in credit markets.

When assessing the information content of corporate credit spreads for economic activity, it is also important to control accurately for the maturity structure of the underlying credit instruments. The widely used paper-bill spreads, for example, are based on short maturity instruments—typically between one and six months—whereas the speciﬁc maturity structure of corporate bond spread indexes such as the high-yield spread or Baa-Aaa spread—though much longer—is not generally known. In general, short-term credit instruments reﬂect near-term default risk, whereas longer-maturity instruments are likely better at capturing expectations about future economic conditions one to two years ahead, a forecast horizon typically associated with business cycle ﬂuctuations. Thus, a correct assessment of the ability of credit spreads to forecast at business cycle frequencies likely requires careful

- 2Indeed, Thoma and Gray [1998] and Emery [1999] argue that the predictive content of the paper-bill spread may reﬂect one-time events.
- 3Fama [1981], Harvey [1989], Stock and Watson [1989, 1999], and Estrella and Mishkin [1998] examine the predictive content of various stock price indexes for economic activity and compare it to other ﬁnancial and nonﬁnancial indicators.

attention to the maturity structure of securities used to construct credit spreads.

This paper considers credit spreads constructed directly from monthly data on prices of senior unsecured corporate debt traded in the secondary market over the 1990–2008 period, issued by about 900 U.S. nonﬁnancial corporations. In contrast to many other corporate ﬁnancial instruments, long-term senior unsecured bonds represent a class of securities with a long history containing a number of business cycles, an attribute that is most useful in the valuation process of debt instruments. In addition, the rapid pace of ﬁnancial innovation over the past twenty years has not aﬀected the basic structure of these securities. Thus, the information content of spreads constructed from yields on senior unsecured corporate bonds is likely to provide more consistent signals regarding economic outcomes relative to spreads based on securities with a shorter history or securities whose structure or relevant market has undergone a signiﬁcant structural change.

We exploit the cross-sectional heterogeneity of our data by constructing an array of credit-spread portfolios sorted by the issuer’s ex-ante expected probability of default and the bond’s remaining term-to-maturity. In the construction of these “bond portfolios,” we rely on the monthly ﬁrm-speciﬁc expected default frequencies (EDFs) constructed by the Moody’s/KMV corporation. Because they are based on observable information in equity markets, EDFs provide a more timely and potentially more objective assessment of credit risk compared with the issuer’s credit rating. Importantly, by building bond portfolios from the “ground up,” we can also construct portfolios of stock returns—sorted by the same credit-risk categories—corresponding to the ﬁrms that issued those bonds. These matched portfolios of stock returns, in turn, serve as controls for news about ﬁrms’ future earnings as these corporate borrowers experience shocks to their creditworthiness.

Two empirical methods are employed to assess the role of credit market factors in economic ﬂuctuations. First, the analysis documents the predictive content of corporate bond spreads in our credit-risk portfolios for measures of economic activity such as the growth of nonfarm payroll employment and industrial production, and we compare the forecasting power of credit spreads in our EDF-based bond portfolios to that of other default-risk indicators emphasized in the literature. The results show that at shorter forecast horizons, the information content of credit spreads in our EDF-based bond portfolios for these monthly measures of economic activity is comparable to that of standard credit spread indexes. At longer forecast horizons, however, our portfolios of credit spreads outperform—both insample and out-of-sample—standard default-risk indicators by almost a factor of two. The results from these forecasting exercises indicate that the predictive power of corporate bond spreads comes from the middle of the credit-quality spectrum, a result also documented by Mueller [2007] who examines the predictive content of corporate bond spread indexes across diﬀerent rating categories. Our results also indicate that at longer forecasting horizons, the

predictive power of corporate bond spreads is concentrated at long maturities. At these forecasting horizons, the predictive content of publicly-available long maturity investment-grade corporate bond spread indexes—such as those rated between BBB and AA—is comparable to that of our low-risk long maturity EDF portfolios. All told, these results imply that the forecasting ability of credit spreads is well captured by a single index that measures credit spreads of long maturity bonds issued by ﬁrms with low to medium probability of default.

The second empirical approach assesses the impact on the macroeconomy of movements in credit spreads in our EDF-based bond portfolios within a structural factoraugmented vector autoregression (FAVAR) framework proposed by Bernanke and Boivin [2003], Bernanke, Boivin, and Eliasz [2005], and Stock and Watson [2005], an approach particularly well-suited to our case given the large number of variables under consideration. Within the FAVAR framework, we identify credit market shocks from the corporate bond spreads that are orthogonal to general measures of economic activity, inﬂation, real interest rates, and various ﬁnancial indicators, as well as to equity returns of ﬁrms whose outstanding bonds were used to construct credit spreads in our EDF-based portfolios. According to the results from our FAVAR analysis, an unanticipated worsening of business credit conditions—identiﬁed through the widening of corporate bond spreads that is orthogonal to other contemporaneous information—predicts substantial and long-lasting declines in economic activity. The decomposition of the forecast error variance implies that these credit market shocks account, on average, for more than 30 percent of the variation in economic activity (as measured by industrial production) at the two- to four-year horizon. We also ﬁnd that incorporating information from the stock market does not alter any of our conclusions. Thus to the extent that equity returns capture news about ﬁrms’ future earnings, our FAVAR speciﬁcation identiﬁes shocks to credit spreads that are orthogonal to such news and hence are speciﬁc to events that lead to disruptions in the corporate bond market.4 Overall, our results suggest that disturbances speciﬁc to credit markets account for a substantial fraction of the volatility in U.S. economic activity during the 1990–2008 period.

The remainder of the paper is organized as follows. Section 2 discusses the characteristics of our underlying security-level data, the construction of portfolios based on expected default risk, and presents the key summary statistics of and statistical relationships between our EDF-based ﬁnancial indicators. Section 3 presents our forecasting exercises. Section 4 contains results of our FAVAR analysis. Section 5 concludes.

4By examining the joint behavior of stock prices and TFP, Beaudry and Portier [2006], identify a component in stock returns that captures news about future permanent changes in TFP; moreover, they show that movements in this component explains a signiﬁcant portion of U.S. business cycle ﬂuctuations. Jermann and Quadrini [2007] develop a theoretical framework in which news about future technological opportunities raises ﬁrms’ current equity valuations, which relax credit constraints, thereby boosting current investment and output.

## 2 Data Description

The key information for our analysis comes from a large sample of ﬁxed income securities issued by U.S. nonﬁnancial corporations. Speciﬁcally, for a sample of 899 publiclytraded ﬁrms covered by the Center for Research in Security Prices (CRSP), month-end secondary market prices of their outstanding long-term corporate bonds were drawn from the Lehman/Warga (LW) and Merrill Lynch (ML) databases. These two data sources include secondary market prices for a signiﬁcant fraction of dollar-denominated bonds publicly issued in the U.S. corporate cash market. The ML database is a proprietary data source of daily bond prices that starts in 1997. Focused on the most liquid securities in the secondary market, bonds in the ML database must have a remaining term-to-maturity of at least two years, a ﬁxed coupon schedule, and a minimum amount outstanding of $100 million for below investment-grade and $150 million for investment-grade issuers. By contrast, the LW database of month-end bond prices has a somewhat broader coverage and is available from 1973 through mid-1998 (see Warga [1991] for details).

To ensure that the bonds yields used to construct portfolios are obtained from comparable securities, the analysis is restricted to senior unsecured issues only. For such securities with market prices in both the LW and LM databases, option-adjusted eﬀective yields at month-end—a component of the bond’s yield that is not attributable to embedded options—are spliced across the two data sources. To calculate the credit spread at each point in time, the resulting yield on each individual security issued by the ﬁrm is matched to the estimated yield on the Treasury coupon security of the same maturity. The monthend Treasury coupon yields were taken from the daily estimates of the U.S. Treasury yield curve reported in Gu¨rkaynak, Sack, and Wright [2006]. To mitigate the eﬀect of outliers, the analysis eliminates all observations with credit spreads smaller than 10 basis points and with spreads greater than 5,000 basis points; in addition, eliminated were issues with a par value of less than $1 million, as such small issues are likely plagued by signiﬁcant liquidity concerns. These selection criteria yielded a sample of 5,045 individual securities, covering the period from January 1990 to September 2008.

Table 1 contains summary statistics for the selected characteristics of bonds in our sample. Note that a typical ﬁrm has only a few senior unsecured issues outstanding at any point in time—the median ﬁrm, for example, has two such issues trading in the secondary market at any given month. This distribution, however, exhibits a signiﬁcant positive skew,

- as the average ﬁrm has almost six diﬀerent senior unsecured bond issues trading in the market at a point in time. The distribution of the market values of these issues is similarly skewed, with the range running from $1.1 million to nearly $6.7 billion. Not surprisingly, the maturity of these debt instruments is fairly long, with the average maturity at issue

Table 1: Summary Statistics of Bond Characteristics

|Bond Characteristic<br><br>|Mean SD Min P50 Max|
|---|---|
|# of bonds per ﬁrm/month Mkt. Value of Issuea ($mil.) Maturity at Issue (years) Term to Maturity (years) Duration (years) S&P Credit Rating Coupon Rate (pct.) Nominal Eﬀective Yield (pct.) Credit Spreadb (bps.)|5.66 8.42 1.00 2.00 75.0<br><br>312.0 318.8 1.11 234.5 6,657 13.7 9.3 1.0 10.0 50.0 10.8 8.67 0.01 7.54 30.0 5.95 3.27 0.00 5.40 26.4<br><br>- - D BBB1 AAA<br><br>7.60 2.00 0.00 7.38 15.9 7.46 3.16 1.20 7.08 57.4 192 299 10 114 4,995<br><br>|

Panel Dimensions Obs. = 275,880 N = 5,045 bonds Min. Tenure = 1 Median Tenure = 48 Max. Tenure = 224

Note: Sample period: Monthly data from January 1990 to September 2008 for a sample of 899 nonﬁnancial ﬁrms. Sample statistics are based on trimmed data (see text for details).

aMarket value of the outstanding issue deﬂated by the CPI. bMeasured relative to comparable maturity Treasury yield (see text for details).

of almost 14 years; the average term-to-maturity is about 11 years. Because corporate bonds typically generate signiﬁcant cash ﬂow in the form of regular coupon payments, the eﬀective duration is considerably shorter, averaging about 5.95 years over the sample period. Although our sample spans the entire spectrum of credit quality—from “single D” to “triple A”—the median bond/month observation, at BBB1, is still solidly in the investment-grade category.

The coupon rate on our sample of bonds averaged 7.60 percent during the sample period, and the average total return, as measured by the nominal eﬀective yield, was 7.46 percent per annum. Reﬂecting the wide range of credit quality, the distribution of yields is quite wide, with the minimum of about 1.2 percent and the maximum of more than 57 percent. Relative to Treasuries, an average bond in our sample generated a return of about 192 basis points above the comparable-maturity risk-free rate, with a standard deviation of 299 basis points.

A portion of observed credit spreads reﬂects compensation demanded by investors for bearing the risk that a ﬁrm who issued the bonds will default on its payment obligations. To measures this ﬁrm-speciﬁc likelihood of default at each point in time, we employ a monthly indicator that is widely used by ﬁnancial market participants—the “Expected Default Frequency” (EDF). This measure of default risk is constructed and marketed by

the Moody’s/KMV Corporation (MKMV). It measures the probability of default over the subsequent twelve-month period. The theoretical underpinnings to these probabilities of default are provided by the seminal work of Merton [1973, 1974]. According to this optiontheoretic approach, the probability that a ﬁrm will default on its debt obligations at any point in the future is determined by three major factors: the market value of the ﬁrm’s assets; asset volatility; the risk-free interest rate and the ﬁrm’s leverage.5 These factors are combined into a single measure of default risk called distance to default, deﬁned as

Distance to Default

Mkt. Value of Assets − Default

Point Mkt. Value

=

.

of Assets × Asset

Volatility

Because the market value of assets and the volatility of assets are not directly observable, they have to be computed in order to calculate the distance to default. Assuming that the ﬁrm’s assets are traded, the market value of the ﬁrm’s equity can be viewed as a call option on the ﬁrm’s assets with the strike price equal to the current book value of the ﬁrm’s total debt.6 Using this insight, MKMV “backs out” the market value and the volatility of assets from a proprietary variant of the Black-Scholes-Merton option-pricing model, employing the observed book value of liabilities and the market value of equity as inputs (see Crosbie and Bohn [2003] for details). In the ﬁnal step, MKMV transforms the distance to default into an expected probability of default—the so-called EDF—using an empirical distribution of actual defaults.

#### 2.1 Default-Risk Based Portfolios

We summarize the information contained in bond spreads and excess equity returns for our sample of ﬁrms by constructing portfolios based on expected default risk.7 These default-risk portfolios are constructed by sorting credit spreads and excess equity returns in

- 5In the original work of Merton [1974], the default point is equal to the book value of liabilities. Later structural default models relax this assumptions and allow for endogenous capital structure as well as strategic default. In these models, both the default time and default boundary are determined endogenously and depend on ﬁrm-speciﬁc as well as aggregate factors; the voluminous literature on structural default models is summarized by Duﬃe and Singleton [2003]. Recent theoretical work has examined the importance of aggregate risk and diﬀerent speciﬁcations of investors’ preferences for generating default-risk premiums and matching historical credit spreads; see, for example, Chen, Collin-Dufresne, and Goldstein [2008] and Chen [2008]. Empirically, however, MKMV has found that most defaults occur when the market value of the ﬁrm’s assets drops to the value equal to the sum of the ﬁrm’s current liabilities and one-half of long-term liabilities (i.e., Default Point = Current Liabilities + 0.5 × Long-Term Liabilities), and the default point is calibrated accordingly.
- 6The assumption that all of the ﬁrm’s assets are traded is clearly inappropriate in most cases. Nevertheless, as shown by Ericsson and Reneby [2004], this approach is still valid provided that at least one of the ﬁrm’s securities (e.g., equity) is traded.
- 7Excess equity returns, which include dividends and capital gains, are measured relative to the yield on one-month Treasury bills.

month t into ﬁve quintiles based on the distribution of EDFs in month t−1. To control for maturity, we split each EDF-based quintile of credit spreads into four maturity categories: (1) short maturity: credit spreads of bonds with the remaining term-to-maturity of less than (or equal) to 3 years; (2) intermediate maturity: credit spreads of bonds with the remaining term-to-maturity of more than 3 years but less than (or equal) 7 years; (3) long maturity: credit spreads of bonds with the remaining term-to-maturity of more than 7 years but less than (or equal) to 15 years; (4) very long maturity: credit spreads of bonds with the remaining term-to-maturity of more than 15 years. We then compute an arithmetic average of credit spreads in month t for each EDF/maturity portfolio and an arithmetic average of excess equity returns in month t for each EDF portfolio. This procedure yields 20 bond portfolios of credit spreads (ﬁve EDF quintiles and four maturity categories) and ﬁve EDF-based stock portfolios of excess equity returns.

Table 2 contains summary statistics of our variables by the ﬁve EDF quintiles. The average expected probability of default increases in a roughly linear fashion between the ﬁrst and the fourth quintiles before jumping sharply for ﬁrms in the ﬁfth quintile. Consistent with the increase in the probability of default, both the average and the median credit spread increase monotonically across the ﬁve EDF quintiles in all four maturity categories. The Sharpe ratio within each maturity category is fairly constant for the portfolio of bonds in the ﬁrst three EDF quintiles. However, the Sharpe ratio drops markedly for portfolios containing bonds issued by the riskiest ﬁrms.

The bottom panel of Table 2 examines the time-series characteristics of monthly excess equity returns of ﬁrms in our ﬁve credit-risk categories. Excess return increase monotonically across the ﬁrst four EDF quintiles, but the Sharpe ratios associated with these four stock portfolios are essentially constant. By contrast, ﬁrms in the ﬁfth EDF quintile registered considerably lower returns relative to their less risky counterparts, with an average (monthly) excess return over the 1990–2008 period of only 0.24 percent.8

## 3 Credit Spreads and Economic Activity

This section examines the predictive power of credit spreads in our EDF-based bond portfolios and compare their forecasting performance—both in-sample and out-of-sample—with several commonly used credit spread indexes. Letting Yt denote a measure of economic

8This paltry performance is especially stark when one considers the Sharpe ratio for this category of ﬁrms, which is considerably below that of the less risky portfolios. The ﬁnding is consistent with the distress risk anomaly documented by a large empirical literature that has used diﬀerent measures of default risk; see, for example, Griﬃn and Lemmon [2002] and Campbell, Hilscher, and Szilagyi [2008].

Table 2: Summary Statistics of Financial Indicators by EDF Quintile

|Financial Indicator Quintilea<br><br>|Mean SD S-Rb Min P50 Max|
|---|---|
|EDF 1<br><br>EDF 2<br><br>EDF 3<br><br>EDF 4<br><br>EDF 5<br><br><br>|0.05 0.03 - 0.01 0.04 0.14 0.12 0.09 - 0.03 0.10 0.46 0.24 0.19 - 0.05 0.19 0.90 0.55 0.42 - 0.08 0.38 2.07 4.70 3.02 - 0.61 3.76 15.5|
|Spread (under 3 yrs.) 1<br><br>Spread (under 3 yrs.) 2<br><br>Spread (under 3 yrs.) 3<br><br>Spread (under 3 yrs.) 4<br><br>Spread (under 3 yrs.) 5<br><br><br>|0.79 0.38 2.09 0.32 0.69 2.69<br>1.03 0.49 2.10 0.41 0.89 3.44 1.21 0.55 2.22 0.50 1.09 3.30 1.84 1.00 1.84 0.67 1.54 5.13 5.28 3.74 1.41 1.16 3.79 22.3<br>|
|Spread (3–7 yrs.) 1<br><br>Spread (3–7 yrs.) 2<br><br>Spread (3–7 yrs.) 3<br><br>Spread (3–7 yrs.) 4<br><br>Spread (3–7 yrs.) 5<br><br><br>|0.92 0.33 2.75 0.52 0.85 2.56<br>1.26 0.49 2.58 0.52 1.17 3.32<br><br><br>1.52 0.55 2.75 0.71 1.38 3.57<br>2.20 0.93 2.37 1.15 1.91 5.05 5.69 2.87 1.98 1.99 4.83 16.4<br>|
|Spread (7–15 yrs.) 1<br>Spread (7–15 yrs.) 2<br>Spread (7–15 yrs.) 3<br>Spread (7–15 yrs.) 4<br>Spread (7–15 yrs.) 5<br>|0.86 0.38 2.29 0.38 0.74 2.49<br><br>1.15 0.51 2.27 0.49 1.04 3.04<br><br><br>1.38 0.58 2.37 0.67 1.21 3.09<br><br>2.00 0.85 2.35 0.81 1.73 5.27<br><br><br>5.20 3.24 1.61 1.59 4.19 18.8|
|Spread (above 15 yrs.) 1<br>Spread (above 15 yrs.) 2<br>Spread (above 15 yrs.) 3<br>Spread (above 15 yrs.) 4<br>Spread (above 15 yrs.) 5<br>|1.02 0.41 2.47 0.45 0.92 2.38 1.28 0.47 2.72 0.58 1.22 3.07<br><br>1.45 0.56 2.60 0.55 1.32 2.91<br><br>2.11 0.84 2.51 0.93 1.91 4.96<br><br>3.79 2.03 1.87 1.10 3.41 12.0<br><br><br>|
|Excess Equity Return 1<br><br>Excess Equity Return 2<br><br>Excess Equity Return 3<br><br>Excess Equity Return 4<br><br>Excess Equity Return 5<br><br><br>|0.60 3.20 0.19 -11.5 0.77 11.5 0.75 3.90 0.19 -14.5 1.03 12.5 0.80 4.28 0.19 -16.3 0.92 13.1 0.90 5.19 0.17 -19.5 1.16 15.6 0.24 7.42 0.03 -28.1 0.78 30.7|

Note: Sample period: Monthly data from February 1990 to September 2008. Credit spreads are expressed in percentage points; EDFs are expressed in percent; and excess equity returns are expressed in percent.

aThe average of ﬁnancial indicators in month t in each quintile is based on the EDF distribution in month t − 1 (see text for details).

bSharpe ratio.

activity in month t, we deﬁne

1200 h

∇hYt+h ≡

ln

Yt+h Yt

,

where h denotes the forecast horizon. Nonfarm payroll employment (EMP) published monthly by the Bureau of Labor Statistics and the Federal Reserve’s monthly index of industrial production (IP) are used to gauge the state of the economy. In addition, the analysis presents forecasting results for a broader index of economic activity that summarizes the eleven indicators of economic growth employed in our FAVAR analysis.

For our ﬁrst two measures of economic activity, we estimate the following bivariate vector autoregression (VAR), augmented with two sets of credit spreads:

∇hEMPt+h = β0 +

∇hIPt+h = γ0 +

11

β1i∇EMPt−i +

i=0

11

11

γ1i∇EMPt−i +

i=0

i=0

11

β2i∇IPt−i + η1′ Z1t + η2′ Z2t + ǫ1,t+h; (1)

i=0

γ2i∇IPt−i + θ1′ Z1t + θ2′ Z2t + ǫ2,t+h. (2)

In the VAR forecasting system given by equations 1–2, Z1t denotes a vector of standard credit spreads indexes; Z2t is a vector of credit spreads in the four maturity categories associated with a particular EDF quintile; and ǫ1,t+h and ǫ2,t+h are the forecast errors.9 The following three speciﬁcations are considered: (1) a benchmark speciﬁcation that includes only the vector of standard credit spread indexes Z1t; (2) an alternative speciﬁcation that includes only the vector Z2t, elements of which correspond to credit spreads in the four maturity categories of an EDF quintile; and (3) a speciﬁcation that includes both the vector of standard credit spread indexes Z1t and the vector of spreads in a particular EDF quintile Z2t. For each speciﬁcation and a forecast horizon of 3 and 12 months, we estimate equations 1 and 2 by OLS. To take into account serial correlation induced by overlapping forecast errors, the estimated covariance matrix is computed according to Newey and West [1987], with the “lag truncation” parameter equal to h + 1.

The set of standard default-risk indicators—the vector Z1t—consists of four credit spread indexes, all of which have been used extensively to forecast real economic activity; see Stock and Watson [2003a] for a comprehensive review. Speciﬁcally, we consider: (1) paperbill spread: the diﬀerence between the yield on one-month nonﬁnancial AA-rated commercial paper and the yield on the constant maturity one-month Treasury bill; (2) Aaa corporate bond spread: the diﬀerence between the yield on an index of seasoned long-term Aaa-rated corporate bonds and the yield on the constant maturity ten-year Treasury note; (3) Baa corporate bond spread: the diﬀerence between the yield on an index of seasoned long-term Baa-rated corporate bonds and the yield on the constant maturity ten-year Trea-

9An alternative approach to the direct h-step ahead prediction method speciﬁed in equations 1–2 would be to specify a VAR—or some other joint one-step ahead model for employment growth, industrial production, and credit spreads—and then iterate this model forward h periods. If the one-period ahead joint model is correctly speciﬁed, iterated forecasts are more eﬃcient, whereas the direct h-step ahead forecasts are more robust to model misspeciﬁcation; see Marcellino, Stock, and Watson [2006] for details.

sury note; and (4) high-yield corporate bond spread: the diﬀerence between the yield on an index of long-term speculative-grade corporate bonds and the yield on the constant maturity ten-year Treasury note.10 Note that by including a paper-bill spread with spreads on longterm corporate bonds, our set of standard credit spread indexes captures the information content of default-risk indicators at both short and long horizons.11

#### 3.1 In-Sample Predictive Power of Credit Spreads

This section examines the in-sample predictive power of various credit spreads for our two measures of economic activity. The upper panel of Table 3 contains the results of this exercise for the short-run forecast horizon (3 months), whereas the lower panel contains results for the long-run forecast horizon (12 months). In both cases, we report p-values associated with the exclusion tests on the two sets of credit spreads along with the explanatory power of each forecasting equation as measured by the adjusted R2. As a benchmark, the Memo item in both panels contains the in-sample ﬁt from the VAR speciﬁcation that excludes all credit spreads.

When forecasting employment growth, the inclusion of credit spreads leads only to a modest improvement in the in-sample ﬁt at the 3-month forecast horizon. As evidenced by the p-values reported in the upper panel of Table 3, both the standard credit spread indexes and credit spreads in each EDF quintile are statistically signiﬁcant predictors of employment growth three months ahead. Moreover, when both sets of credit spreads are included in the forecasting VAR, they all tend to remain statistically signiﬁcant. Nevertheless, adding either set of credit spreads to the VAR results only in a relatively modest improvement in the explanatory power of the equation for employment growth. For example, the speciﬁcation that excludes all credit spreads yields an adjusted R2 of 69 percent, only about 9 percentage points below the adjusted R2 from a speciﬁcation that includes standard credit spread indexes and credit spreads in the second EDF quintile.

The inclusion of credit spreads in the equation for industrial production, in contrast, leads to a substantial increase in predictive accuracy at the 3-month forecast horizon. Ac-

- 10Commercial paper rates are taken from the “Commercial Paper Rates and Outstanding” Federal Reserve statistical release. The source of Treasury yields and yields on Aaa- and Baa-rated corporate bonds is “Selected Interest Rates” (H.15) Federal Reserve statistical release. To construct the high-yield spread, we use the High-Yield Master II index, a commonly used benchmark index for long-term speculative-grade corporate bonds administered by Merrill Lynch.
- 11Note that we construct our standard corporate bond spread indexes using the ten-year Treasury yield. As emphasized by Duﬀee [1998], the corporate-Treasury yield spreads can be inﬂuenced signiﬁcantly by time-varying prepayment risk premiums, reﬂecting the call provisions on corporate issues. According to Duca [1999], corporate bond spreads measured relative to the yield on Aaa-rated bonds are more reﬂective of default risk than those measured relative to comparable-maturity Treasuries, which makes the former spreads more correlated with economic downturns. For comparison, we computed the Baa and the highyield bond spread relative to the Aaa yield, and our results were virtually identical.

Table 3: In-Sample Predictive Content of Credit Spreads

Forecast Horizon h = 3 (months)

|Nonfarm Employment (EMP)|Industrial Production (IP)<br><br>|
|---|---|
|Credit Spreads Pr > W1 Pr > W2 Adj. R2<br><br>|Pr > W1 Pr > W2 Adj. R2|
|Standard 0.000 - 0.761<br><br>EDF-Q1 - 0.002 0.734<br><br>EDF-Q2 - 0.000 0.746<br><br>EDF-Q3 - 0.000 0.750<br><br>EDF-Q4 - 0.000 0.725<br><br>EDF-Q5 - 0.042 0.725<br><br><br>Standard & EDF-Q1 0.002 0.006 0.775<br><br>Standard & EDF-Q2 0.002 0.004 0.782<br><br>Standard & EDF-Q3 0.006 0.007 0.780<br><br>Standard & EDF-Q4 0.002 0.074 0.771<br><br>Standard & EDF-Q5 0.000 0.016 0.781<br><br><br>|0.000 - 0.291<br><br>- 0.000 0.370<br>- 0.000 0.361<br>- 0.000 0.337<br>- 0.000 0.304<br>- 0.000 0.343<br><br><br>0.033 0.001 0.392 0.717 0.005 0.357 0.017 0.000 0.371 0.091 0.029 0.322 0.004 0.000 0.377|
|Memo: None - - 0.695<br><br>|- - 0.169|

Forecast Horizon h = 12 (months)

|Nonfarm Employment (EMP)<br><br>|Industrial Production (IP)|
|---|---|
|Credit Spreads Pr > W1 Pr > W2 Adj. R2<br><br>|Pr > W1 Pr > W2 Adj. R2|
|Standard 0.003 - 0.665<br><br>EDF-Q1 - 0.000 0.727<br>EDF-Q2 - 0.000 0.759<br>EDF-Q3 - 0.000 0.739<br>EDF-Q4 - 0.000 0.704<br>EDF-Q5 - 0.000 0.685<br><br><br>Standard & EDF-Q1 0.000 0.000 0.809<br>Standard & EDF-Q2 0.016 0.000 0.817<br>Standard & EDF-Q3 0.000 0.000 0.816<br>Standard & EDF-Q4 0.000 0.000 0.795<br>Standard & EDF-Q5 0.000 0.000 0.791<br>|0.109 - 0.200<br><br>- 0.000 0.563<br><br>- 0.000 0.641<br><br>- 0.000 0.528<br><br>- 0.000 0.439<br><br>- 0.000 0.420<br><br><br>0.297 0.000 0.585 0.128 0.000 0.677 0.000 0.000 0.645 0.021 0.000 0.552 0.015 0.000 0.499<br><br>|
|Memo: None - - 0.537<br><br>|- - 0.042|

Note: Sample period: Monthly data from February 1990 to September 2008. Dependent variables in the VAR speciﬁcation are ∇hEMPt+h and ∇hIPt+h, where h is the forecast horizon. Each VAR speciﬁcation also includes a constant, current, and 11 lags of ∇EMPt and ∇IPt (see text for details). Pr > W1 denotes the p-value for the robust Wald test of the null hypothesis that coeﬃcients on standard credit spread indexes are jointly equal to zero; Pr > W2 denotes the p-value for the robust Wald test of the null hypothesis that coeﬃcients on EDF-based credit spreads in a particular quintile are jointly equal to zero.

cording to the Memo item, lags of industrial production and employment growth explain only about 17 percent of the variation in the growth of industrial output three months ahead. By including standard credit spread indexes in the forecasting VAR, the adjusted R2 increases to almost 30 percent. Speciﬁcations that include credit spreads in our EDF-based portfolios yield even greater improvements in the in-sample ﬁt. Note also that the best insample ﬁt comes from speciﬁcations that include credit spreads in the lowest two quintiles of the EDF distribution (EDF-Q1 and EDF-Q2).

The lower panel of Table 3 examines the in-sample explanatory power of credit spreads

- at the 12-month horizon. At this longer horizon, the information content of credit spreads for both measures of economic activity is considerable. In the case of nonfarm payroll employment, for example, standard credit spread indexes explain 66 percent of the variation in the 12-month ahead growth rate, a signiﬁcant increases in the goodness-of-ﬁt relative to the speciﬁcation that relies only on lags of employment growth and lags of the growth rate in industrial production. Credit spreads in our EDF-based bond portfolios do even better. The information content of our default-risk indicators for the growth of employment is highest for the second and third EDF quintiles (EDF-Q2 and EDF-Q3), with the average spreads in these two quintiles yielding adjusted R2s of about 75 percent. Results are even more striking in the case of industrial production, a measure of economic activity for which the explanatory power of our portfolio credit spreads signiﬁcantly exceeds that of standard default-risk indicators. Whereas standard credit spread indexes explain about 20 percent of the variation in the 12-month ahead growth of industrial production, credit spreads associated with the ﬁrst three EDF quintiles (EDF-Q1–EDF-Q3) explain over 50 percent of the variation in the 12-month ahead growth rate of industrial output.

The results in Table 3 highlight the gains in in-sample predictive accuracy for employment and industrial output growth at longer forecast horizon obtained from conditioning on credit spreads in our EDF-based bond portfolios. The results of these forecasting exercises indicate that the information content of credit spreads is concentrated in the low to medium risk categories. As we show below, the predictive content of credit spreads is also concentrated at the long end of the maturity spectrum. This result is shown graphically in Figure 1, where the two panels depict the actual 12-month ahead growth of employment and industrial production along with their respective ﬁtted values obtained from simple regressions of these two variables on the credit spreads in the very long maturity EDFQ2 portfolio—that is, the portfolio with the highest overall predictive content, according to the results in Table 3. Note that these ﬁtted values are a simple renormalization of the credit spread dated 12 months before the time period over which the growth in employment and industrial production was computed. Remarkably, this single credit spread forecasted employment growth throughout the 2001 recession and the subsequent recovery.

##### Figure 1: Long Maturity Credit Spreads and Economic Activity Indicators

Nonfarm payroll employment

12−month percent change

- 0
- 1
- 2
- 3
- 4

NBER Peak

Monthly

Actual

Fitted

−1

1991 1992 1993 1994 1995 1996 1997 1998 1999 2000 2001 2002 2003 2004 2005 2006 2007 2008

Industrial production

12−month percent change

10

NBER Peak

Monthly

Actual

Fitted

5

0

−5

1991 1992 1993 1994 1995 1996 1997 1998 1999 2000 2001 2002 2003 2004 2005 2006 2007 2008

Note: The solid lines in the two panels of the ﬁgure depict the actual 12-month growth in nonfarm payroll employment and industrial production. The dotted lines show the ﬁtted values from a regression of each variable on a 12-month lag of very long credit spreads in the second EDF quintile (EDF-Q2). Shaded vertical bars correspond to NBER-dated recessions.

It also accurately predicted the current slowdown in employment growth, which peaked in January 2006. As shown in the bottom panel of Figure 1, the ability of this long-horizon relatively low-risk credit spread to predict accurately future economic activity as measured by the 12-month ahead growth in industrial production is even more striking.

#### 3.2 Out-of-Sample Predictive Power of Credit Spreads

This section examines the predictive content of credit spreads for our two measures of economic activity using pseudo out-of-sample forecasts. Speciﬁcally, for each forecast horizon

- h, the forecasting VAR given in equations 1–2 is estimated using all available data through,

and including, November 1999. We then calculate the (annualized) h-month ahead growth rates of nonfarm payroll employment and industrial production and the associated forecast errors. The forecast origin—that is, November 1999—is then updated with an additional month of data, the VAR parameters are re-estimated using this new larger observation window, and new forecasts are generated. This procedure is repeated through the end of the sample, thereby generating a sequence of pseudo out-of-sample forecasts for the two measures of economic activity.

Tables 4 contains the results of this exercise. To quantify the pseudo out-of-sample forecasting performance of the diﬀerent VAR speciﬁcations, we report the square root of the mean squared forecast error in annualized percentage points (RMSFE) for each speciﬁcation. To compare the predictive accuracy of credit spreads in our EDF-based bond portfolios with that of standard default-risk indicators, we then compute the ratio of the mean squared forecast error (MSFE) of the VAR speciﬁcation augmented with EDF-based credit spreads with the MSFE of the speciﬁcation that includes only standard credit spread indexes; pvalues of the Diebold and Mariano [1995] test of equal predictive accuracy indicate whether the diﬀerence in predictive accuracy between these two non-nested models are statistically signiﬁcant.12

In the case of employment growth, the VAR speciﬁcations that include credit spreads in our EDF-based bond portfolios yield lower MSFEs at short-run forecast horizons than the speciﬁcation augmented with standard credit spread indexes. At the 3-month forecast horizon, the out-of-sample forecasting performance of credit spreads in the ﬁrst three EDF quintiles (EDF-Q1–EDF-Q3) for employment growth exceeds that of standard credit spread indexes by 20 to 25 percent, and these improvements in predictive accuracy are statistically signiﬁcant at the 10 to 15 percent level. The out-of-sample forecasting performance of credit spreads in our EDF-based bond portfolios for the growth of industrial production also exceeds that of standard default-risk indicators at the 3-month forecast horizon, although the diﬀerences in predictive accuracy are not statistically signiﬁcant at conventional levels.

The gain in out-of-sample predictive accuracy at the 12-month forecast horizon is especially striking, a result consistent with the in-sample analysis of the previous section. The predictive content of our portfolio credit spreads is again concentrated among ﬁrms in the ﬁrst three quintiles of the EDF distribution (EDF-Q1–EDF-Q3), which yield reductions in the MSFEs on the order of 60 percent relative to the speciﬁcation that includes the standard set of credit spread indexes. Moreover, these improvements in predictive accuract are also highly statistically signiﬁcant according to the Diebold-Mariano test.

The results reported in Table 4 point to signiﬁcant improvements in the out-of-sample

12Because the data in our forecasting VAR speciﬁcation are overlapping, the asymptotic (long-run) variance of the loss diﬀerential used to construct the Diebold-Mariano S-statistic allows for serial correlation of order h.

Table 4: Out-of-Sample Predictive Content of Credit Spreads

Forecast Horizon h = 3 (months)

|Nonfarm Employment (EMP)<br><br>|Industrial Production (IP)|
|---|---|
|Credit Spreads RMSFE Ratio Pr > |S||RMSFE Ratio Pr > |S||
|Standard 0.947 - -<br><br>EDF-Q1 0.824 0.757 0.106<br><br>EDF-Q2 0.842 0.791 0.160<br><br>EDF-Q3 0.826 0.761 0.069<br><br>EDF-Q4 0.946 0.999 0.996<br><br>EDF-Q5 0.956 1.019 0.902<br><br><br>Standard & EDF-Q1 0.932 0.968 -<br><br>Standard & EDF-Q2 0.924 0.953 -<br><br>Standard & EDF-Q3 0.926 0.957 -<br><br>Standard & EDF-Q4 0.951 1.010 -<br><br>Standard & EDF-Q5 0.922 0.948 -<br><br><br>|5.211 - 4.592 0.777 0.153 4.667 0.802 0.093 4.644 0.794 0.180 4.647 0.795 0.219<br><br>4.779 0.841 0.360<br><br>4.904 0.886 -<br>5.040 0.936 -<br><br><br>4.994 0.918 -<br>5.397 1.073 -<br><br><br>5.226 1.006 -<br>|
|Memo: None 0.925 - -<br><br>|5.513 - -|

Forecast Horizon h = 12 (months)

|Nonfarm Employment (EMP)<br><br>|Industrial Production (IP)|
|---|---|
|Credit Spreads RMSFE Ratio Pr > |S|<br><br>|RMSFE Ratio Pr > |S||
|Standard 1.113 - -<br><br>EDF-Q1 0.693 0.387 0.002<br>EDF-Q2 0.667 0.359 0.001<br>EDF-Q3 0.740 0.442 0.000<br>EDF-Q4 0.902 0.657 0.094<br>EDF-Q5 0.872 0.613 0.092<br><br><br>Standard & EDF-Q1 0.827 0.552 -<br>Standard & EDF-Q2 0.816 0.537 -<br>Standard & EDF-Q3 0.814 0.535 -<br>Standard & EDF-Q4 0.869 0.609 -<br>Standard & EDF-Q5 0.864 0.602 -<br>|3.676 - -<br><br>2.089 0.323 0.000 2.004 0.297 0.000 2.279 0.384 0.000 2.704 0.541 0.004 2.574 0.490 0.001<br><br>2.571 0.489 2.238 0.371 2.376 0.418 2.686 0.534 2.948 0.643 -<br><br>|
|Memo: None 1.115 - -<br><br>|3.882 - -|

Note: Sample period: Monthly data from February 1990 to September 2008. Dependent variables in the VAR speciﬁcation are ∇hEMPt+h and ∇hIPt+h, where h is the forecast horizon. Each VAR speciﬁcation also includes a constant, current, and 11 lags of ∇EMPt and ∇IPt (see text for details). “Ratio” denotes the ratio of the MSFE of each model relative to the MSFE of the model that includes standard credit spreads; Pr > |S| denotes the p-value for the Diebold and Mariano [1995] test of the null hypothesis that the diﬀerence between the MSFE from the model that includes standard credit spreads and the MSFE from the model that includes EDF-based credit spreads is equal to zero.

##### Figure 2: Out-of-Sample Forecasts of Economic Activity Indicators

Nonfarm payroll employment

12−month percent change

6

Actual employment Proj. Range of model estimates (EDF−Q1 − EDF−Q3) Average of model estimates (EDF−Q1 − EDF−Q3)

4

2

0

−2

−4

−6

−8

−10

2001 2002 2003 2004 2005 2006 2007 2008 2009

Industrial production

12−month percent change

15

Actual industrial production Proj. Range of model estimates (EDF−Q1 − EDF−Q3) Average of model estimates (EDF−Q1 − EDF−Q3)

10

5

0

−5

−10

−15

−20

−25

−30

−35

2001 2002 2003 2004 2005 2006 2007 2008 2009

Note: The panels of the ﬁgure depict pseudo out-of-sample forecasts of the 12-month growth in nonfarm payroll employment and industrial production. The solid line shows the actual data; the shaded band shows the range of forecasts based on VAR speciﬁcations augmented with credit spreads in the ﬁrst three quintiles of the EDF distribution (EDF-Q1–EDF-Q3); and the dotted line shows the average of the three forecasts (see text for details).

forecasting performance of VAR speciﬁcations that rely on corporate bond spreads constructed from the low to middle ranges of the credit-risk distribution. To assess whether these improvements are due to a speciﬁc subperiod or a “one-time” event, Figure 2 plots the realized values of the 12-month growth in nonfarm payroll employment and industrial production, along with the range of their respective out-of-sample forecasts based on the VAR speciﬁcations that include credit spreads in portfolios corresponding to the ﬁrst three EDF quintiles (EDF-Q1–EDF-Q3); the dotted line in each panel depicts the average of these forecast.

As indicated by the narrow shaded band, forecasts of employment and industrial output

growth based on credit spreads in our EDF-based bond portfolios track quite well year-overyear growth in the actual series in both recessionary and expansionary times. In addition, the predictive accuracy obtained from using credit spreads in our EDF-based portfolios does not seem to reﬂect any “one-time” event or a speciﬁc subperiod. Importantly, our EDFbased forecasts capture the slowdown in economic activity associated with the 2001 recession

- as well as the subsequent recovery. These EDF-based forecasts also predict the slowdown in economic activity that has emerged since late 2006 with a high degree of accuracy.

In light of the ongoing turmoil in ﬁnancial markets, investors and policymakers are obviously concerned with the near-term economic outlook. Figure 2 also depicts the forecasts for these two measures of economic activity through December 2009.13 The average of the three EDF-based forecasts indicates that over the 12 months ending in December 2009, U.S. nonfarm payrolls will fall about 7.5 percent, while industrial production is projected to drop around 20 percent, declines that are four times greater than those experienced during the 2001 recession.

#### 3.3 Predicting an Index of Economic Activity

The previous results focused on forecasting the growth employment and industrial output. In the FAVAR analysis below, real economic activity is summarized by a factor that relies, in addition to the growth in employment and industrial production, on nine additional macroeconomic indicators that measure economic activity. Some of these series are leading indicators, or forward-looking variables such as new manufacturing orders, whereas other series such as unemployment are relatively sluggish. To assess the ability of credit spreads to forecast this broader set of economic indicators, we construct an index of economic activity, deﬁned as the ﬁrst principal component of these 11 time-series.

Table 5 reports both the in-sample and out-of-sample results obtained from univariate forecasting speciﬁcations that include credit spread indexes along with the 12 monthly lags of the economic activity index. These results are very similar to those obtained using growth in payroll employment and industrial production: Speciﬁcations that include credit spreads in the lowest three EDF quintiles provide modest improvements in out-of-sample forecasting performance at the 3-month horizon, and quantitatively large and statistically signiﬁcant gains—both in-sample and out-of-sample—at the 12-month horizon.

As a ﬁnal exercise, we explore the extent to which the predictive content of credit spreads depends on the maturity structure of the underlying securities. Because our credit spreads rely on proprietary measures of default risk and issue-speciﬁc bond yields, we are also interested in determining whether ratings-based credit spreads yield similar forecasting

13The year-over-year forecasts for December 2009 are based on the realized values of the two forecasting variables through December 2008, but we only use data through September 2008 to compute these forecasts.

Table 5: Predictive Content of Credit Spreads for Economic Activity Index

Forecast Horizon h = 3 (months)

|In-Sample|Out-of-Sample<br><br>|
|---|---|
|Credit Spreads Pr > W1 Pr > W2 Adj. R2<br><br>|RMSFE Ratio Pr > |S||
|Standard 0.000 - 0.525<br><br>EDF-Q1 - 0.000 0.520<br><br>EDF-Q2 - 0.000 0.527<br><br>EDF-Q3 - 0.000 0.511<br><br>EDF-Q4 - 0.000 0.457<br><br>EDF-Q5 - 0.000 0.495<br><br><br>Standard & EDF-Q1 0.000 0.002 0.605<br><br>Standard & EDF-Q2 0.060 0.000 0.577<br><br>Standard & EDF-Q3 0.000 0.004 0.575<br><br>Standard & EDF-Q4 0.000 0.009 0.549<br><br>Standard & EDF-Q5 0.000 0.000 0.585<br><br><br>|0.841 - 0.716 0.726 0.135 0.722 0.739 0.096 0.730 0.754 0.107 0.874 1.081 0.626 0.780 0.860 0.410 0.763 0.824 0.820 0.951 0.820 0.951 0.864 1.056 0.762 0.821 -|
|Memo: None - - 0.393|0.852 - -|

Forecast Horizon h = 12 (months)

|In-Sample<br><br>|Out-of-Sample|
|---|---|
|Credit Spreads Pr > W1 Pr > W2 Adj. R2<br><br>|RMSFE Ratio Pr > |S||
|Standard 0.004 - 0.407<br><br>EDF-Q1 - 0.000 0.607<br>EDF-Q2 - 0.000 0.618<br>EDF-Q3 - 0.000 0.591<br>EDF-Q4 - 0.000 0.455<br>EDF-Q5 - 0.000 0.381<br><br><br>Standard & EDF-Q1 0.000 0.000 0.726<br>Standard & EDF-Q2 0.000 0.000 0.742<br>Standard & EDF-Q3 0.000 0.000 0.732<br>Standard & EDF-Q4 0.000 0.000 0.677<br>Standard & EDF-Q5 0.000 0.000 0.617<br>|1.132 - -<br><br>0.568 0.252 0.000 0.574 0.257 0.000 0.650 0.330 0.000 0.985 0.757 0.300 0.945 0.697 0.270<br><br>0.724 0.409 0.690 0.372 0.706 0.384 0.809 0.511 0.884 0.610 -<br><br>|
|Memo: None - - 0.178<br><br>|1.065 - -|

Note: Sample period: Monthly data from February 1990 to September 2008. Dependent variable is the h-month moving average of the index of real economic activity, where h is the forecast horizon. Each regression speciﬁcation includes a constant, current, and 11 lags of the economic activity index (see text for details). Pr > W1 denotes the p-value for the robust Wald test of the null hypothesis that coeﬃcients on standard credit spread indexes are jointly equal to zero; Pr > W2 denotes the p-value for the robust Wald test of the null hypothesis that coeﬃcients on EDF-based credit spreads in a particular quintile are jointly equal to zero. “Ratio” denotes the ratio of the MSFE of each model relative to the MSFE of the model that includes standard credit spreads; Pr > |S| denotes the p-value for the Diebold and Mariano [1995] test of the null hypothesis that the diﬀerence between the MSFE from the model that includes standard credit spreads and the MSFE from the model that includes EDF-based credit spreads is equal to zero.

Table 6: Credit Spreads and Index of Real Economic Activity (12-Month Forecast Horizon)

Credit Spreads (by maturity & risk) Estimate t-stat Adj. R2 Pr > SWa Short Maturity (less than 3 years)

- EDF-Q1 -0.236 -0.841 0.088 0.000
- EDF-Q2 -0.456 -1.533 0.163 0.001
- EDF-Q3 -0.573 -1.866 0.200 0.004
- EDF-Q4 -0.604 -1.976 0.235 0.000
- EDF-Q5 -0.563 -2.369 0.220 0.000 AA-rated -0.296 -1.729 0.109 0.000 BBB-rated -0.143 -0.681 0.055 0.000

Intermediate Maturity (3–7 years)

- EDF-Q1 -0.910 -3.542 0.410 0.001
- EDF-Q2 -0.604 -2.243 0.261 0.031
- EDF-Q3 -0.734 -2.634 0.313 0.059
- EDF-Q4 -0.561 -1.756 0.230 0.021
- EDF-Q5 -0.674 -2.093 0.261 0.000 AA-rated -1.489 -7.313 0.676 0.136

- BBB-rated -0.765 -2.439 0.287 0.001

Long Maturity (7–15 years)

- EDF-Q1 -1.260 -6.370 0.613 0.062
- EDF-Q2 -1.155 -5.553 0.575 0.003
- EDF-Q3 -1.183 -5.345 0.569 0.042
- EDF-Q4 -0.851 -3.468 0.424 0.191
- EDF-Q5 -0.765 -3.078 0.342 0.000 AA-rated -1.473 -6.404 0.690 0.001

- BBB-rated -1.150 -4.975 0.520 0.054

Very Long Maturity (greater than 15 years)

- EDF-Q1 -1.354 -7.326 0.655 0.143
- EDF-Q2 -1.378 -6.881 0.654 0.159
- EDF-Q3 -1.349 -6.584 0.634 0.087
- EDF-Q4 -0.669 -2.521 0.318 0.075
- EDF-Q5 -0.726 -2.987 0.353 0.001 AA-rated -1.331 -6.183 0.649 0.099 BBB-rated -1.270 -5.795 0.606 0.096

Note: Sample period: Monthly data from April 1991 to September 2008 (T = 198). The dependent variable is the 12-month moving average of the index of economic activity (see text for details). Each regression speciﬁcation includes a credit spread, a 12-month lag of the dependent variable, and a constant term (the latter two eﬀects are not reported) and is estimated by OLS. Estimates of parameters corresponding to credit spreads are standardized; t-statistics are based on a heteroscedasticity- and autocorrelation-consistent asymptotic covariance matrix computed according to Newey and West [1987].

ap-value for the Shapiro-Wilk test of the null hypothesis that the OLS residuals are normally distributed.

performance once one controls for maturity. These two issues are addressed by considering a simple in-sample forecasting exercise, in which the 12-month change in the index of economic activity is regressed on a 12-month lag of itself and a single credit spread index. We consider separately the credit spreads in our 20 bond portfolios as well as AA-rated and BBB-rated credit spreads for the same four maturity categories based on the Bloomberg Fair Value (BFV) model.14

The results of this exercise, which are reported in Table 6, again indicate that long maturity low to medium risk credit spreads provide substantial gains in predictive content relative to short maturity credit spreads. The adjusted R2’s from the regressions of the 12-month change in the economic activity index on the very long maturity credit spreads in the ﬁrst three EDF quintiles (EDF-Q1–EDF-Q3) are about 65 percent, whereas those that rely on short maturity credit spreads are below 25 percent. At shorter maturities, the information content of credit spreads in our EDF-based portfolios exceeds that of the AAand BBB-rated counterparts. At longer maturities, the information content of our EDFbased credit spreads is essentially the same as that of spreads in the two rating categories. These ﬁndings suggest that EDF-based measures of default risk provide timely information that is especially useful for forecasting at shorter horizons.

## 4 Factor-Augmented VAR Analysis

This section examines the interaction between the credit spreads in our EDF-based bond portfolios and a wide range of measures of economic activity and inﬂation, the monetary policy rate, yields on Treasury securities of various maturities, excess returns on the matched EDF-based portfolios of stocks, and other ﬁnancial indicators. We use the factor-augmented vector autoregression (FAVAR) methodology proposed by Bernanke and Boivin [2003] and Bernanke, Boivin, and Eliasz [2005] to summarize a large number of macroeconomic and ﬁnancial time series by a small number of unobservable (latent) factors. This methodology is then used to identify shocks to corporate bond spreads and trace out their dynamic eﬀect on the macroeconomy.

14The BFV model provides daily estimates of the corporate bond yield curve utilizing prices of bonds with similar characteristics (i.e., currency, market type, industry, and credit rating). For comparability with our bond-level data, the sample is restricted to dollar-denominated bonds issued by industrial ﬁrms. For this segment of the corporate bond market, zero-coupon yields for AA- and BBB-rating categories at the maturities of 3-month, 6-month, 1-year, 2-year, 3-year, 4-year, 5-year, 7-year, 10-year, 15-year, 20-year, and 30-year were obtained from the Bloomberg BFV data base. These two rating categories represent the highest and lowest ratings for which spreads at all maturities are available since April 1991, the starting date of the Bloomberg data. Credit spreads at all maturities are computed by utilizing daily Treasury yields of the same maturities, derived from the estimates of the zero-coupon Treasury yield curve (see G¨urkaynak, Sack, and Wright [2006]). For each rating categories, we then constructed the same four maturity categories as for our EDF-based portfolio and averaged the spreads in each maturity category.

#### 4.1 Speciﬁcation, Identiﬁcation, and Estimation

Let Xt, t = 1,2,...,T, denote a (n × 1) vector of observations on all the variables in the FAVAR system in month t. We assume that Xt can be partitioned as Xt = [X1′t X2′t]′, where X1t is the (n1 × 1) vector whose elements correspond to measures of economic activity and inﬂation, Treasury yields, excess equity returns, and other ﬁnancial indicators, and elements of the (n2×1) vector X2t correspond to credit spreads in our EDF-based bond portfolios. We assume that the information in the vector of observable variables Xt can be summarized by a set of latent factors denoted by the (k×1) vector Ft, with k < n. The following assumption are made with regards to this latent factor structure: A subset of factors—denoted by the (k1 ×1) vector F1t—spans all the information contained in the observed vector Xt, whereas the remaining factors, denoted by the (k2 × 1) vector F2t, are speciﬁc to credit spreads in our EDF-based portfolios—the so-called credit factors.

The relationship between the observed variables in Xt and the latent factors Ft = [F1′t F2′t]′ is linear and is given by the observation equation:

X1t X2t

=

Λ11 Λ12 Λ21 Λ22

- F1t
- F2t

+

- ν1t
- ν2t

, (3)

where Λij, i,j = 1,2, are conformable matrices of factor loadings, and νt = [ν1′t ν2′t]′ denotes the (n×1) vector of idiosyncratic measurement errors.15 The dynamics of the latent factors are described by an autoregressive process of the form

- F1t
- F2t

= Φ(L)

- F1,t−1
- F2,t−1

+

- ǫ1t
- ǫ2t

, (4)

where Φ(L) denotes a matrix polynomial in the lag operator L of ﬁnite order p, and ǫt = [ǫ′1t ǫ′2t]′ is the (k × 1) vector of reduced-form VAR disturbances with a covariance matrix Σ = E[ǫtǫ′t]; following standard practices, we assume that the idiosyncratic measurement errors are uncorrelated with VAR innovations—that is, E[νitǫjt] = 0, for t = 1,...,T;

- i = 1,...,n; and j = 1,...,k. To identify the vector of credit factors F2t, we impose the following restrictions on

the system of equation 3 and 4. First, we assume that Λ12 = 0 in equation 3. This restriction on the factor loadings implies that once we have conditioned on the factors in F1t, the remaining information content of credit spreads in our EDF-based portfolios

15Consistent with the assumptions underlying approximate factor models, the process for the vector of measurement errors νt can be weakly serially correlated and exhibit some degree of cross-sectional dependence (see, for example, Bai and Ng [2002]). Because the latent factors enter equation 3 without lags, the above speciﬁcation corresponds to the static form of a dynamic factor model. However, as discussed by Stock and Watson [2005], this is not a restrictive assumption, because the static factors can, in principle, contain an arbitrary number of lags of some underlying dynamic factors.

has a systematic component speciﬁc to the corporate bond market that is reﬂected in its own factor structure. Although the credit factors in F2t have no contemporaneous eﬀect on the vector X1t, they aﬀect the factors in F1t—and, by extension, the vector of observed variables X1t—with a lag through the dynamics of the VAR equation 4. The second identifying assumption is that the factors in F1t and F2t are orthogonal, an assumption that separates the residual information content from the corporate bond market from the factors summarizing the state of the economy.

A ﬁve-step estimation procedure that is computationally easy to implement and that imposes the speciﬁed restrictions is used to estimate and identify the credit factors. First, the (T × k1) matrix of factors F1 is estimated as the ﬁrst k1 principle components of the (T ×n1) data matrix X1 corresponding to the vector of variables X1t. Second, each column of the (T × n2) data matrix X2 corresponding to the vector of variables in X2t—that is, credit spreads associated with our EDF-based bond portfolios—is regressed on the k1 factors in F1, with E denoting the corresponding (T × n2) matrix of OLS residuals. Third, the (T × k2) matrix of factors F2 is estimated as the ﬁrst k2 principle components of the data matrix E from the second step. Fourth, factor loadings are estimated by regressing each column of the (T × n) data matrix X on the estimated factors F1 and F2, imposing the restriction Λ12 = 0. And ﬁfth, the VAR(p) model in equation 4 is estimated by OLS using the estimated factors.16

Structural shocks aﬀecting the vector of credit factors F2t are identiﬁed using the Cholesky decomposition of Σ, the covariance matrix of the reduced-form VAR disturbances in equation 4. In computing the Cholesky decomposition, the credit factors are ordered last, and the individual components of F2t are ordered in descending order with respect to their associated eigenvalues. Thus identiﬁed “credit market shocks” correspond to unexpected movements in corporate bond spreads that are contemporaneously uncorrelated with indicators of economic activity and inﬂation, interest rates, and other ﬁnancial indicators as summarized by the vector of factors F1t.

As noted above, the vector X1t contains a broad set of macroeconomic and ﬁnancial variables, whereas elements of the vector X2t correspond to credit spreads in our EDFbased bond portfolios. The variables included in X1t can be classiﬁed into ﬁve broad categories: economic activity indicators, inﬂation indicators, risk-free interest rates, equity market indicators, and other ﬁnancial indicators. In particular, the following 11 monthly indicators of economic activity are included in our FAVAR speciﬁcation: (1) the diﬀerence of the civilian unemployment rate; (2) the log-diﬀerence of nonfarm payroll employment; (3)

16The latent factors F1 and F2 are estimated using asymptotic principal components, the method whose properties are discussed in detail by Stock and Watson [2002a] and Bai and Ng [2002]. Note that the residuals from the second step, by construction, orthogonal to F1, implying that the estimated factors F2 are also orthogonal to F1.

the log-diﬀerence of industrial production index; (4) the diﬀerence in capacity utilization index; (5) the log-diﬀerence of real durable goods orders; (6) the log-diﬀerence of real nondurable good orders; (7) the Institute for Supply Management (ISM) diﬀusion index of activity in the manufacturing sector; (8) the log-diﬀerence of real personal consumption expenditures (retail control category); (9) the log-diﬀerence of real disposable personal income; (10) the log-diﬀerence of housing starts; (11) and the log-diﬀerence of Conference Board’s leading economic indicator index.

Price developments are summarized by the following six inﬂation indicators: (1) the log-diﬀerence of the Consumer Price index (CPI); (2) the log-diﬀerence of the core CPI; (3) the log-diﬀerence of the Producer Price index (PPI); (4) the log-diﬀerence of the core PPI; (5) the log-diﬀerence of the Journal of Commerce index of (spot) commodity prices; (6) the log-diﬀerence of the price of oil as measured by price of a barrel of West Texas Intermediate (WTI) crude.

Our FAVAR speciﬁcation also includes the entire term structure of interest rates, starting

- at the short end with the eﬀective federal funds rate and continuing with the constant maturity Treasury yields at 6-month, 1-year, 2-year, 3-year, 5-year, and 10-year horizons, for a total of seven interest rates. Because nominal yields exhibit a discernible downward trend over our sample period (1990–2008), they are converted into real terms to ensure their approximate stationarity.17

Developments in equity markets are summarized by the following eight series: (1) the total value-weighted excess market return from CRSP; (2) the excess equity returns of ﬁrms in our ﬁve EDF-based stock portfolios; and (3) the Fama-French “SMB” and “HML” factors to account for the diﬀerent dynamics of equity returns in our EDF-based stock portfolios. The ﬁnal group of variables in the vector X1t—six series—includes: (1) the implied volatility on the S&P 500 index options (VIX) to capture uncertainty in the equity market;

- (2) the implied volatilities on Eurodollar and ten-year Treasury note futures, measures of uncertainty associated with movements in short- and long-term interest rates, respectively;
- (3) the log-diﬀerence of the trade-weighted exchange value of the dollar against major cur-

17To do so, we utilize both the realized inﬂation and survey measures of inﬂation expectations reported by the Survey of Professional Forecasters (SPF). Because the SPF is conducted at a quarterly frequency, monthly estimates of inﬂation expectations are obtained from a linear interpolation of quarterly values. Speciﬁcally, the real federal funds rate is measured as the diﬀerence between the nominal rate and realized inﬂation, where the realized inﬂation is given by the the diﬀerence between the log of the core CPI price index and its lagged value 12 months earlier. The real 6-month Treasury yield is measured as the diﬀerence between the nominal yield and the equally-weighted average of the realized inﬂation given above and the oneyear ahead expected CPI inﬂation as reported in the SPF. For the remaining Treasury yields, the expected inﬂation at each speciﬁc horizon is constructed by calculating the appropriately weighted average of the oneyear ahead and the ten-year ahead expected CPI inﬂation reported in the SPF. For example, in calculating the 5-year real Treasury yield, we employ a simplifying assumption that the expected inﬂation over the next ﬁve years is equal to an equally-weighted average of one-year ahead and ten-year ahead expected inﬂation

- as reported in the SPF.

rencies to control for the international dimension of the U.S. ﬁnancial system; and (4) two standard measures of liquidity—namely, the diﬀerence in the yields between the “oﬀ-therun” and “on-the-run” 10-year Treasury note and the diﬀerence between the 5-year swap rate and the yield on the 5-year Treasury note.

Thus in our baseline speciﬁcation, the vector X1t contains 38 monthly macroeconomic and ﬁnancial time series, and the 20 elements of vector X2t correspond to the average credit spreads in the 20 corporate bond portfolios classiﬁed by maturity and default risk. With this speciﬁcation, our assumptions identify credit market shocks that are orthogonal to the excess equity returns of ﬁrms whose outstanding bonds are used to construct the EDFbased bond portfolios underlying the information content of the vector X2t. Hence, the FAVAR traces out the eﬀect of a shock to corporate bond spreads that is unrelated to news contained in stock returns of the same set of ﬁrms.

The remaining question concerns the number of latent factors (k1 and k2) and the order of the VAR system p. In our baseline speciﬁcation, k1 = 4 and k2 = 2.18 Under this parametrization, four common factors—denoted by F1t = [F11t F12t F13t F14t]′—are assumed to summarize the information contained in the vector X1t, whereas the residual component of credit spreads in our EDF-based bond portfolios can be represented by two factors, denoted by F2t = [F21t F22t]′. The order of the VAR system is set to p = 6, a lag length chosen according to the Akaike information criterion (AIC).

#### 4.2 Shocks to Corporate Bond Spreads

Before turning to our main results, we brieﬂy discuss the estimates of the factors F1t = [F11t F12t F13t F14t]′ and credit factors F2t = [F11t F12t]′ from the baseline speciﬁcation. The ﬁrst four panels of Figure 3 depict the four factors associated with macroeconomic and ﬁnancial variables contained in the vector X1t, and the bottom two panels show the estimates of the two credit factors identiﬁed using the information from the corporate bond market. (Tables summarizing correlations between the six factors and all the variables in Xt are shown in Appendix A.)

According to the correlations between the estimated factors and macroeconomic variables, the ﬁrst four factors shown in Figure 3 have a clear economic interpretation: Factor 1

18Recently, Bai and Ng [2002, 2007] and Stock and Watson [2005] have proposed several methods of how to select formally the number of factors in such models. Because of the added complexity reﬂecting our identiﬁcation procedure, we adopted a more informal approach. Speciﬁcally, employing reasoning similar to that of Forni, Giannone, Lippi, and Reichlin [2005] and Giannone, Reichlin, and Sala [2005], k1 was chosen by looking at the increase in the explained variation of the 38 macroeconomic and ﬁnancial series in X1t that resulted from increasing the number of factors in F1t. Given our choice of k1, the number of credit factors k2 was selected using the same approach. As a robustness check, we increased the number of factors extracted from the data matrix X1 from four to ﬁve, and to six, and we increased the number of factors extracted from the data matrix X2 to three. None of the resulting FAVAR speciﬁcations yielded materially diﬀerent conclusions.

##### Figure 3: Macroeconomic and Credit Market Factors (Baseline Speciﬁcation)

Macroeconomic factor 1

Std. deviations

0.4

NBER Peak

0.2

0.0

−0.2

−0.4

1992 1996 2000 2004 2008

Macroeconomic factor 2

Std. deviations

0.4

|NBER Peak| |
|---|---|
| | |

0.2

0.0

−0.2

−0.4

1992 1996 2000 2004 2008

Macroeconomic factor 3

Std. deviations

0.4

NBER Peak

0.2

0.0

−0.2

−0.4

1992 1996 2000 2004 2008

Macroeconomic factor 4

Std. deviations

0.4

NBER Peak

0.2

0.0

−0.2

−0.4

1992 1996 2000 2004 2008

Credit market factor 1

Std. deviations

0.4

NBER Peak

0.2

0.0

−0.2

−0.4

1992 1996 2000 2004 2008

Credit market factor 2

Std. deviations

0.4

|NBER Peak| |
|---|---|
| | |

0.2

0.0

−0.2

−0.4

1992 1996 2000 2004 2008

Note: The panels of the ﬁgure depict estimates of the six factors from the baseline FAVAR speciﬁcation. The ﬁrst four factors summarize the 38 macroeconomic and ﬁnancial variables included in the vector X1t, and the last two factors summarize the residual information content of credit spreads in the 20 EDF-based bond portfolios included in the vector X2t (see text for details). Shaded vertical bars correspond to NBER-dated recessions.

is most highly correlated with real short-term interest rates; Factor 2 captures the excess stock market return; Factor 3 summarizes the various measures of economic activity; and Factor 4 is a summary statistics for inﬂation developments. The ﬁrst credit factor corresponds most closely to credit spreads in the long-maturity bond portfolios in the middle of the credit-quality spectrum. Recall that these are the portfolios that contained the greatest

##### Figure 4: Response of Corporate Bond Spreads (Baseline Speciﬁcation)

Short maturity credit spreads by EDF quintile*

Percentage points

- Quintile 1

- Quintile 2

- Quintile 3

- Quintile 4

- Quintile 5

0 12 24 36 48

Months after shock

* Bonds with term to maturity under 3 years.

0.6

0.5

0.4

0.3

0.2

0.1

0.0

Intermediate maturity credit spreads by EDF quintile*

Percentage points

0.5

- Quintile 1

- Quintile 2

- Quintile 3

- Quintile 4

- Quintile 5

0.4

0.3

0.2

0.1

0.0

0 12 24 36 48

Months after shock

* Bonds with term to maturity 3−7 years.

Long maturity credit spreads by EDF quintile*

Percentage points

- Quintile 1

- Quintile 2

- Quintile 3

- Quintile 4

- Quintile 5

0 12 24 36 48

Months after shock

* Bonds with term to maturity 7−15 years.

0.6

0.5

0.4

0.3

0.2

0.1

0.0

Very long maturity credit spreads by EDF quintile*

Percentage points

- Quintile 1

- Quintile 2

- Quintile 3

- Quintile 4

- Quintile 5

0 12 24 36 48

Months after shock

* Bonds with term to maturity above 15 years.

0.5

0.4

0.3

0.2

0.1

0.0

Note: The panels of the ﬁgure depict the eﬀect of an orthogonalized one standard deviation shock to credit factor 1 on corporate bond spreads in the 20 EDF-based bond portfolios (see text for details).

predictive power for the growth of employment and industrial production at longer forecast horizons, according to the results of our forecasting analysis. The second credit factor appears to capture diﬀerences between high- and low-risk ﬁrms and diﬀerences between nearand longer-term credit risk.

Figure 4 depicts responses of credit spreads in the 20 bond portfolios to a one standard deviation orthogonalized shock to the ﬁrst credit factor. (Impulse responses for all the variables in our baseline speciﬁcation, along with their respective 95-percent conﬁdence

intervals, are shown in Appendix B.19) This credit market shock widens corporate bond spreads across the entire spectrum of credit quality and across all maturities. The response of credit spreads associated with riskier bond portfolios is signiﬁcantly greater than that of the less risky portfolios and is also more persistent. Furthermore, the jump in the riskiest corporate bond spreads is somewhat more pronounced at the short end of the maturity spectrum.

The impact of this credit shock on selected macroeconomic variables is shown in Figure 5. A shock to the ﬁrst credit factor is clearly contractionary, as evidenced by the fact that industrial production declines about 1 percentage points over a 24-month period.20 In addition to being statistically signiﬁcant, the cumulative contraction in industrial output in response to a credit shock is economically signiﬁcant, especially given that the response of credit spreads is in the order of only 10-50 basis points for most of the credit-risk distribution. The increasing slack in resource utilization following a shock to the corporate bond market is associated with a modest decline in the level of core CPI prices. These macroeconomic developments, in turn, lead to a fall in the general level of real interest rates. In particular, real short-term interest rates decline about 15 basis points at the trough, but longer-term real Treasury yields fall somewhat less along the path, implying a steepening of the real Treasury yield curve in response to the innovation in the corporate bond spreads.

The contractionary eﬀects of this credit market shock implies a cumulative decline in the excess stock market return of about 2 percentage points over the horizon shown. The cumulative excess equity returns of the least and the most risky ﬁrms also fall initially, though the latter eﬀect is statistically indistinguishable from zero. The impact of this adverse credit market shock is also reﬂected in stock market uncertainty, as the optionimplied volatility on the S&P 500 (VIX) increases notably in the ﬁrst six months after the shock. In summary, a shock to the ﬁrst credit factor implies a modest increase in the overall level of corporate bond spreads that leads to a sizable contraction in industrial output, a deceleration in core prices, lower real interest rates and equity returns, and a rise in stock

- 19The conﬁdence intervals of the impulse response functions are based on a two-stage bootstrap procedure that takes into account both the serial correlation and cross-sectional dependence of the measurement errors in equation 3. In particular, we ﬁrst estimate the factors and factor loadings following the estimation procedure described above. We then perform a sieve bootstrap on the residuals of the observation equation 3. For each bootstrapped sample, we also re-estimate the factors F1 and F2, thereby taking into account that the factors appear as generated regressors in equation 4. Second, for each bootstrap loop of the observation equation, we apply the “bootstrap-after-bootstrap” procedure of Kilian [1998] to the state-space equation 4 using the bootstrapped factors. This procedure is designed to take into account the small sample bias, the lack of scale invariance, and the skewness of the distribution of the impulse response functions of the VAR system.
- 20As discussed above, the macroeconomic and ﬁnancial variables contained in the vector X1t were, if necessary, transformed using log or simple diﬀerencing to ensure their stationarity. In such a case, we cumulate their impulse responses to depict the impact of the credit market shock on levels of these variables; similarly, we compute and show the cumulative responses of both the excess market return and the excess equity returns of ﬁrms in the ﬁve EDF quintiles.

Figure 5: Response of Selected Macroeconomic and Financial Variables (Baseline Speciﬁcation)

Industrial production

Percentage points

0.5

0.0

−0.5

−1.0

−1.5

−2.0

−2.5

0 12 24 36 48

Months after shock

Real federal funds rate

Percentage points

0.10

0.05

0.00

−0.05

−0.10

−0.15

−0.20

−0.25

−0.30

0 12 24 36 48

Months after shock

Cumulative excess stock market return

Percentage points

- 0
- 1
- 2

−1

−2

−3

−4

−5

−6

0 12 24 36 48

Months after shock

Core CPI

Percentage points

0.1

0.0

−0.1

−0.2

−0.3

−0.4

0 12 24 36 48

Months after shock

Real 10−year Treasury yield

Percentage points

0.05

0.00

−0.05

−0.10

−0.15

−0.20

0 12 24 36 48

Months after shock

S&P 500 implied volatility (VIX)

Percentage points

1.0

0.8

0.6

0.4

0.2

0.0

−0.2

−0.4

−0.6

0 12 24 36 48

Months after shock

Cumulative excess stock return EDF Quintile 1

Percentage points

- 0
- 1
- 2

−1

−2

−3

−4

−5

0 12 24 36 48

Months after shock

Cumulative excess stock return EDF Quintile 5

Percentage points

6

4

2

0

−2

−4

0 12 24 36 48

Months after shock

Note: The panels of the ﬁgure depict the eﬀect of an orthogonalized one standard deviation shock to credit factor 1 on selected macroeconomic and ﬁnancial variables (see text for details). The shaded bands represent the 95-percent conﬁdence intervals computed using a sieve bootstrap with 10,000 replications.

Figure 6: Forecast Error Variance Decomposition of a Credit Market Shock (Baseline Speciﬁcation)

Industrial production

Percent

0 12 24 36 48

Forecast horizon (months)

70

60

50

40

30

20

10

0

Core CPI

Percent

0 12 24 36 48

Forecast horizon (months)

70

60

50

40

30

20

10

0

Real federal funds rate

Percent

0 12 24 36 48

Forecast horizon (months)

70

60

50

40

30

20

10

0

Real 10−year Treasury yield

Percent

0 12 24 36 48

Forecast horizon (months)

70

60

50

40

30

20

10

0

Cumulative excess stock market return

Percent

0 12 24 36 48

Forecast horizon (months)

70

60

50

40

30

20

10

0

S&P 500 implied volatility (VIX)

Percent

0 12 24 36 48

Forecast horizon (months)

70

60

50

40

30

20

10

0

Cumulative excess stock return EDF Quintile 1

Percent

0 12 24 36 48

Forecast horizon (months)

70

60

50

40

30

20

10

0

Cumulative excess stock return EDF Quintile 5

Percent

0 12 24 36 48

Forecast horizon (months)

70

60

50

40

30

20

10

0

Note: The panels of the ﬁgure depict the fraction of the forecast error variance for selected macroeconomic and ﬁnancial variables that is attributed to an orthogonalized one standard deviation shock to credit factor 1. The shaded bands represent the 95-percent conﬁdence intervals computed using a sieve bootstrap with 10,000 replications.

market uncertainty.21

To examine the economic importance of credit market shocks, we calculate the proportion of the forecast error variance attributable to the innovations associated with the ﬁrst credit market factor. Figure 6 reports the average proportion of the forecast error variance

- at diﬀerent horizons for selected variables in our FAVAR speciﬁcation that is explained by our identiﬁed credit market shock, along with the respective 95-percent conﬁdence intervals. According to results in Figure 6, shocks to corporate bond spreads account, on average, for more than 30 percent of the variation in the growth of industrial production at the twoto four-year forecast horizon. The shock to the ﬁrst credit factor also explains a signiﬁcant fraction of the variation in both short- and long-term real interest rates and accounts for 30 percent of the forecast error variance in the excess equity returns. This credit market shock also accounts for a large fraction of the variation in corporate bond spreads but at a higher frequency. Thus, variation in corporate bond spreads at the one- to two-year horizon appears to explain a substantial fraction of the variation in both real activity and real interest rates at the two- to four-year forecast horizon, a result consistent with the predictive power for economic activity of corporate bond spread at long-run forecast horizons.

#### 4.3 Shocks to Excess Equity Returns

The baseline FAVAR speciﬁcation analyzed the information content of corporate bond spreads that is orthogonal to both the aggregate stock market return and the average of excess returns of ﬁrms in our EDF-based stock portfolios. As a point of comparison, this section examines whether excess equity returns in our EDF-based stock portfolios also contain information regarding economic activity that is not captured by either standard macroeconomic indicators or the aggregate stock market return.

To do so, we consider an alternative FAVAR speciﬁcation that relies only on excess equity returns in our EDF-based stock portfolios to identify a shock to ﬁnancial markets. Speciﬁcally, instead of the 20 credit spreads associated with our EDF-based bond portfolios, the elements of the vector X2t in this alternative speciﬁcation correspond to the (average) excess equity returns in our ﬁve EDF-based stock portfolios. The elements of the vector X1t, except for removing the excess equity returns in the ﬁve EDF-based portfolios, are left unchanged.22 This alternative FAVAR speciﬁcation thus identiﬁes shocks to ﬁrms’ earnings contained in our EDF-based stock portfolios that are orthogonal to indicators of economic activity and inﬂation, real interest rates, and aggregate stock market developments.23

- 21In contrast, the orthogonalized shock to the second credit factor has a statistically and economically insigniﬁcant eﬀect on real economic activity.
- 22The same identiﬁcation scheme as in the baseline speciﬁcation is employed to identify credit shocks; in addition, k1 = 4, k2 = 2, and p = 6, exactly the same as in the baseline case.
- 23We have also considered a speciﬁcation that that includes both the stock returns and the corporate bond

##### Figure 7: Response of Excess Equity Returns (Alternative Speciﬁcation)

Cumulative excess stock returns by EDF quintile

Percentage points

- 0
- 1

−1

−2

−3

- Quintile 1

- Quintile 2

- Quintile 3

- Quintile 4

- Quintile 5

−4

−5

−6

0 12 24 36 48

Months after shock

Note: The panels of the ﬁgure depict the eﬀect of an orthogonalized one standard deviation shock to ﬁnancial factor 1 on excess equity returns in the ﬁve EDF-based stock portfolios (see text for details).

Figure 7 depicts the eﬀect of a one standard deviation orthogonalized shock to the ﬁrst factor—identiﬁed using excess stock returns—on the average excess equity return in each of the ﬁve quintiles of the credit-risk distribution. This shock has clear negative implications for stock returns of ﬁrms across the spectrum of credit quality. Upon its impact, excess stock returns in our EDF-based stock portfolios fall between 2 and 4 percentage points, with returns of the riskiest ﬁrms registering the largest decline. As shown in Figure 8, the macroeconomic implications of this shock—given the width of the 95-percent conﬁdence intervals—are ambiguous, a result suggesting that the two factors extracted from the residual component of excess equity returns have little systematic component and largely reﬂect idiosyncratic news about earnings growth.

spreads in the vector X2t. These results are very similar to our baseline speciﬁcation, a result that provides further evidence that corporate bond spreads contain unique information not captured by other ﬁnancial asset prices.

Figure 8: Response of Selected Macroeconomic and Financial Variables (Alternative Speciﬁcation)

Industrial production

Percentage points

0.6

0.4

0.2

0.0

−0.2

−0.4

−0.6

0 12 24 36 48

Months after shock

Core CPI

Percentage points

0.10

0.05

0.00

−0.05

−0.10

0 12 24 36 48

Months after shock

Real federal funds rate

Percentage points

0.10

0.05

0.00

−0.05

−0.10

0 12 24 36 48

Months after shock

Real 10−year Treasury yield

Percentage points

0.06

0.04

0.02

0.00

−0.02

−0.04

−0.06

0 12 24 36 48

Months after shock

Cumulative excess stock market return

Percentage points

2.0

1.5

1.0

0.5

0.0

−0.5

−1.0

−1.5

0 12 24 36 48

Months after shock

S&P 500 implied volatility (VIX)

Percentage points

1.0

0.8

0.6

0.4

0.2

0.0

−0.2

−0.4

−0.6

−0.8

0 12 24 36 48

Months after shock

Note: The panels of the ﬁgure depict the eﬀect of an orthogonalized one standard deviation shock to ﬁnancial factor 1 on selected macroeconomic and ﬁnancial variables (see text for details). The shaded bands represent the 95-percent conﬁdence intervals computed using a sieve bootstrap with 10,000 replications.

## 5 Conclusion

Our results indicate that credit spreads on senior unsecured corporate debt have a substantial predictive power for future economic activity relative to that of previously used default-risk indicators such as the paper-bill spread or the high-yield credit spread. This improvement in forecasting performance reﬂects the information content of spreads on longermaturity bonds issued by ﬁrms at the high-end and middle of the credit-quality spectrum.

According to our FAVAR results, shocks to corporate bond spreads lead to quantitatively large swings in economic activity and real interest rates. Such credit market shocks explain a sizable fraction of the variance in economic activity at the two- to four-year horizon. These ﬁndings are consistent with the notion that an unexpected worsening of conditions in credit markets can cause a long-lasting economic downturn and that shocks to credit markets have played an important role in business cycle ﬂuctuations during the previous decade and a half.

The fact that credit market shocks generate such large eﬀects may come as a bit of surprise. One possibility is that credit markets provide better signals regarding future prospects of ﬁrms than does the stock market. In that case, a shock to credit markets may still reﬂect news regarding underlying cash ﬂows rather than a disruption in the supply of credit. But we are then left with the puzzle as to why stock prices do not incorporate all the relevant information about the ﬁrms’ proﬁt opportunities? Although various theories of stock market behavior that emphasize departures from the standard eﬃcient markets paradigm may help justify these ﬁndings, our results imply developments in corporate credit markets provide important information regarding the future course of economic activity.24

We oﬀer two alternative explanations for our results. First, the recent empirical and theoretical asset pricing literature has emphasized the inability of standard structural models of default to explain both the level and movements in credit spreads (see, for example, Collin-Dufresne, Goldstein, and Martin [2001]). According to this literature, a large part of the variation in credit spreads is due to macroeconomic factors, particularly to liquidity and risk premiums. In the corporate bond market, the key investors are banks, insurance companies, and other ﬁnancial intermediaries. To the extent that ﬁnancial markets are segmented, the risk attitude of the marginal corporate bond investor may reﬂect the willingness or ability of these institutions to bear risk. Thus, as conditions in the ﬁnancial sector deteriorate, the premium on the risk of default rises, which causes a drop in investment spending and a contraction in future economic activity, an argument consistent with the results of Philippon [2008] who ﬁnds that corporate bond spreads do particularly well at forecasting business ﬁxed investment.

Second, the ﬁnancial sector creates direct linkages between the banking sector and nonbank ﬁnancial activity. For example, the ability of nonﬁnancial corporations to ﬁnance short-term liquidity needs by issuing commercial paper relies importantly on the ability of these ﬁrms to obtain back-up lines of credit from banks. As monetary policy tightens, or ﬁnancial conditions in the banking sector deteriorate, banks may be forced to cut back on their lines of credit. More generally, the process of credit disintermediation may increase

24See Philippon [2008] for an overview of such theories and their potential implications for the information content of stock and bond returns.

liquidity risk for nonﬁnancial ﬁrms, which, in the case of a severe deterioration in economic and ﬁnancial conditions, may turn into insolvency risk. Again, disturbances emanating from the ﬁnancial sector would cause a rise in the cost of credit for nonﬁnancial ﬁrms. In addition, to the extent that monetary policy shocks are not fully summarized by movements in the Federal funds rate, these credit market disturbances may also reﬂect the anticipated tightening of monetary policy, which manifests itself in the disintermediation process sooner than it is reﬂected in the observable movements in standard indicators of monetary policy. This alternative is consistent with the ﬁndings of Gertler and Lown [1999] and Mueller [2007] who document a close relationship between changes in bank lending standards and credit market conditions over the course of the business cycle.

As emphasized by Primiceri, Schaumburg, and Tambalotti [2006], there is strong empirical evidence supporting the notion that “intertemporal disturbances” are a major source of business cycle ﬂuctuations. In dynamic stochastic general equilibrium models that allow for ﬁnancial accelerator mechanisms, such as those developed by Kiyotaki and Moore [1997] and Bernanke, Gertler, and Gilchrist [1999], these disturbances may be linked directly to changes in credit conditions. The rich amount of information contained in corporate bond spreads may be particularly useful for measuring and identifying the importance of these ﬁnancial mechanisms. To understand the inter-related eﬀects of movements in risk premiums, changes in the health of ﬁnancial institutions, and economic activity would require extending these models to include ﬁnancial market participants and changing risk attitudes in a fully-speciﬁed general equilibrium framework.

## References

Ang, A., M. Piazzesi, and M. Wei (2006): “What Does the Yield Curve Tell Us About GDP Growth?,” Journal of Econometrics, 131, 359–403.

Bai, J., and S. Ng (2002): “Determining the Number of Factors in Approximate Factor Models,” Econometrica, 70, 191–221.

(2007): “Determining the Number of Primitive Shocks in Factor Models,” Journal of Business and Economic Statistics, 25, 52–60.

Beaudry, P., and F. Portier (2006): “Stock Prices, News, and Economic Fluctuations,” American Economic Review, 94, 1293–1307.

Bernanke, B. S., and J. Boivin (2003): “Monetary Policy in a Data-Rich Environment,” Journal of Monetary Economics, 50, 525–546.

Bernanke, B. S., J. Boivin, and P. Eliasz (2005): “Measuring the Eﬀects of Monetary Policy: A Factor-Augmented Vector Autoregressive (FAVAR) Approach,” Quarterly Journal of Economics, 120, 387–422.

Bernanke, B. S., M. Gertler, and S. Gilchrist (1999): “The Financial Accelerator in a Quantitative Business Cycle Framework,” in The Handbook of Macroeconomics, ed. by J. B. Taylor, and M. Woodford, pp. 1341–1393. Elsevier Science B.V., Amsterdam.

Campbell, J. Y., J. Hilscher, and J. Szilagyi (2008): “In Search of Distress Risk,” Journal of Finance, 63, 2321–2350.

Chen, H. (2008): “Macroeconomic Conditions and the Puzzles of Credit Spreads and Capital Structure,” Mimeo, Sloan School of Management, MIT.

Chen, L., P. Collin-Dufresne, and R. S. Goldstein (2008): “On the Relation Between the Credit Spread Puzzle and the Equity Premium Puzzle,” Review of Financial Studies forthcoming.

Collin-Dufresne, P., R. S. Goldstein, and J. S. Martin (2001): “The Determinants of Credit Spread Changes,” Journal of Finance, 56, 2177–2207.

Crosbie, P. J., and J. R. Bohn (2003): “Modeling Default Risk,” Research Report, Moody’s|K·M·V Corporation.

Diebold, F. X., and R. S. Mariano (1995): “Comparing Predictive Accuracy,” Journal of Business and Economic Statistics, 13, 253–263.

Dotsey, M. (1998): “The Predictive Content of the Interest Rate Term Spread for Future Economic Growth,” Federal Reserve Bank of Richmond Economic Quarterly, 84, 31–51.

Duca, J. V. (1999): “An Overview of What Credit Market Indicators Tell Us,” Economic and Financial Review, Federal Reserve Bank of Dallas, Third Quarter, 2–13.

Duffee, G. R. (1998): “The Relation Between Treasury Yields and Corporate Bond Yield Spreads,” Journal of Finance, 53, 225–241.

Duffie, D., and K. J. Singleton (2003): Credit Risk. Princeton University Press, Princeton, NJ.

Emery, K. M. (1999): “The Information Content of the Paper-Bill Spread,” Journal of Business and Economic Statistics, 48, 1–10.

Ericsson, J., and J. Reneby (2004): “A Note on Contingent Claims Pricing with NonTraded Assets,” Finance Letters, 2, No. 3.

Estrella, A., and G. A. Hardouvelis (1991): “The Term Structure as Predictor of Real Economic Activity,” Journal of Finance, 46, 555–576.

Estrella, A., and F. S. Mishkin (1998): “Predicting U.S. Recessions: Financial Variables as Leading Indicators,” Review of Economics and Statistics, 80, 45–61.

Ewing, B. T., G. J. Lynch, and J. E. Payne (2003): “The Paper-Bill Spread and Real Output: What Matters More, a Change in the Paper Rate or a Change in the Bill Rate?,” Journal of Financial Economics, 12, 233–246.

Fama, E. F. (1981): “Stock Returns, Real Activity, Inﬂation and Money,” American Economic Review, 71, 545–565.

Forni, M., D. Giannone, M. Lippi, and L. Reichlin (2005): “Opening the Black Box: Structural Factor Models with Large Cross-Sections,” CEPR Discussion Paper No. 4133.

Friedman, B. M., and K. N. Kuttner (1998): “Indicator Properties of the PaperBill Spread: Lessons From Recent Experience,” Review of Economics and Statistics, 80, 34–44.

Gertler, M., and C. S. Lown (1999): “The Information in the High-Yield Bond Spread for the Business Cycle: Evidence and Some Implications,” Oxford Review of Economic Policy, 15, 132–150.

Giannone, D., L. Reichlin, and L. Sala (2005): “Monetary Policy in Real Time,” in NBER Macroeconomics Annual, ed. by M. Gertler, and K. Rogoﬀ, pp. 161–200. The MIT Press, Cambridge.

Griffin, J. M., and M. L. Lemmon (2002): “Does Book-to-Market Equity Proxy for Distress Risk?,” Journal of Finance, 57, 2317–2336.

Gurkaynak,¨ R. S., B. Sack, and J. H. Wright (2006): “The U.S. Treasury Yield Curve: 1961 to the Present,” Finance and Economics Discussion Series Paper No. 28, Federal Reserve Board.

Hamilton, J. D., and D. H. Kim (2002): “A Reexamination of the Predictability of Economic Activity Using the Yield Spread,” Journal of Money, Credit, and Banking, 34, 340–360.

Harvey, C. R. (1989): “Forecasts of Economic Growth from the Bond and Stock Market,” Financial Analysts Journal, 45, 38–45.

Jermann, U. J., and V. Quadrini (2007): “Stock Market Boom and the Productivity Gains of the 1990s,” Journal of Monetary Economics, 54, 413–432.

Kilian, L. (1998): “Small-Sample Conﬁdence Intervals for Impulse Response Functions,” Review of Economics and Statistics, 80, 218–230.

King, T. B., A. T. Levin, and R. Perli (2007): “Financial Market Perceptions of Recession Risk,” Finance and Economics Discussion Series Paper No. 57, Federal Reserve Board.

Kiyotaki, N., and J. H. Moore (1997): “Credit Cycles,” Journal of Political Economy, 105, 211–248.

Marcellino, M., J. H. Stock, and M. W. Watson (2006): “A Comparison of Direct and Iterated Multistep AR Methods for Forecasting Macroeconomic Time Series,” Journal of Econometrics, 135, 499–526.

Merton, R. C. (1973): “A Rational Theory of Option Pricing,” Bell Journal of Economics and Management Science, 4, 141–183.

(1974): “On the Pricing of Corporate Debt: The Risk Structure of Interest Rates,” Journal of Finance, 29, 449–470.

Mody, A., and M. P. Taylor (2004): “Financial Predictors of Real Activity and the Financial Accelerator,” Economic Letters, 82, 167–172.

Mueller, P. (2007): “Credit Spreads and Real Activity,” Mimeo, Columbia Business School.

Newey, W. K., and K. D. West (1987): “A Simple, Positive Semi-Deﬁnite, Heteroskedasticity and Autocorrelation Consistent Covariance Matrix,” Econometrica, 55, 703–708.

Philippon, T. (2008): “The Bond Market’s Q,” Quarterly Journal of Economics forthcoming.

Primiceri, G. E., E. Schaumburg, and A. Tambalotti (2006): “Intertemporal Disturbances,” NBER Working Paper No. 12243.

Stock, J. H., and M. W. Watson (1989): “New Indexes of Coincident and Leading Economic Indicators,” in NBER Macroeconomics Annual, ed. by O. J. Blanchard, and S. Fischer, pp. 351–394. The MIT Press, Cambridge.

(1999): “Business Cycle Fluctuations in U.S. Macroeconomic Time Series,” in Handbook of Macroeconomics, ed. by J. B. Taylor, and M. Woodford, pp. 3–64. NorthHolland, Elsevier, New York.

- (2002a): “Forecasting Using Principal Components from a Large Number of Pre-

dictors,” Journal of the American Statistical Association, 97, 1167–1179.

- (2002b): “Macroeconomic Forecasting Using Diﬀusion Indexes,” Journal of Busi-

ness and Economic Statistics, 20, 147–162.

- (2003a): “Forecasting Output and Inﬂation: The Role of Asset Prices,” Journal

of Economic Literature, 41, 788–829.

- (2003b): “How Did Leading Indicators Forecasts Perform During the 2001 Reces-

sions?,” Federal Reserve Bank of Richmond Economic Quarterly, 89, 71–90.

(2005): “Implications of Dynamic Factor Models for VAR Analysis,” NBER Working Paper No. 11467.

Thoma, M. A., and J. A. Gray (1998): “Financial Market Variables Do Not Predict

Real Activity,” Economic Inquiry, 36, 522–539. Warga, A. D. (1991): “A Fixed Income Database,” Mimeo, University of Houston. Wright, J. H. (2006): “The Yield Curve and Predicting Recessions,” Finance and Eco-

nomics Discussion Series Paper No. 7, Federal Reserve Board.

# Appendices

## A Factors and Macroeconomic and Financial Variables

- Table A-1 contains correlations between the six latent factors and the 38 macroeconomic and ﬁnancial time series included in the vector X1t in the baseline FAVAR speciﬁcation;
- Table A-2 contain correlations between the six latent factors and credit spreads in the

20 EDF-based bond portfolios included in the vector X2t. All correlations are computed over the sample period from February 1990 to September 2008.

##### Table A-1: Correlations between Estimated Factors and Macroeconomic Series (Baseline FAVAR Speciﬁcation)

|Variable (data transformation)|F11 F12 F13 F14 F21 F22<br><br>|
|---|---|
|Unemployment Rate (∆) Payroll Employment (∆ln) Capacity Utilization (∆) Industrial Production (∆ln) ISM Mfg. Activity Index Leading Indicator Index (∆ln) Real Durable Goods Orders (∆ln) Real Nondurable Goods Orders (∆ln) Real PCE (∆ln) Real DPI (∆ln) Housing Starts (∆ln) Consumer Price Index (∆ln) Core Consumer Price Index (∆ln) Producer Price Index (∆ln) Core Producer Price Index (∆ln) Commodity Price Index (∆ln) Price of WTI Crude (∆ln) Real Federal Funds Rate Real 6-month Treasury Yield<br><br>Real 1-year Treasury Yield<br><br>Real 2-year Treasury Yield<br><br>Real 3-year Treasury Yield Real 5-year Treasury Yield Real 10-year Treasury Yield<br><br><br>Excess Equity Return EDF-Q1<br><br>Excess Equity Return EDF-Q2<br><br>Excess Equity Return EDF-Q3<br><br>Excess Equity Return EDF-Q4<br><br>Excess Equity Return EDF-Q5 Excess Market Return Fama-French HML Factor Fama-French SMB Factor S&P 500 Implied Volatility (VIX) 3-month Eurodollar Implied Volatility 10-year Treasury Note Implied Volatility Exchange Value of the Dollar (∆ln) On/Oﬀ-the-run Treasury Premium (10-year) Swap-Treasury Spread (5-year)<br><br><br>|0.01 0.07 -0.54 0.12 -0.13 -0.01 0.20 0.11 0.71 -0.01 -0.02 -0.06<br><br>-0.13 -0.23 0.75 -0.08 0.18 0.13 0.06 -0.18 0.74 -0.14 0.15 0.09<br>-0.12 -0.08 0.71 0.10 -0.05 -0.07<br>-0.34 0.17 0.46 -0.36 0.08 0.09<br>-0.05 -0.02 0.34 -0.16 0.15 0.04<br>-0.06 -0.16 0.31 0.44 0.09 0.04<br>-0.09 -0.04 0.22 0.44 0.08 -0.07 0.01 0.08 0.07 -0.25 0.01 -0.06<br>-0.14 -0.03 0.05 -0.12 -0.05 -0.03 0.19 -0.22 0.00 0.75 -0.07 0.12 0.42 0.06 -0.13 0.05 -0.14 0.37 0.03 -0.24 0.08 0.84 0.04 0.02 0.18 0.05 -0.05 0.41 -0.09 0.09<br>-0.12 0.02 0.25 0.25 0.13 -0.03 0.01 -0.14 0.16 0.36 0.01 -0.02 0.83 0.14 0.03 0.07 0.09 -0.30 0.90 0.20 0.09 0.05 0.12 -0.25<br><br>0.94 0.22 0.07 0.02 0.07 -0.14 0.96 0.22 0.10 -0.02 0.03 -0.06<br>0.95 0.22 0.10 -0.05 -0.01 0.02 0.92 0.19 0.08 -0.08 -0.05 0.16 0.82 0.14 0.03 -0.10 -0.09 0.32<br><br><br>-0.16 0.87 0.05 0.03 0.01 0.01<br>-0.25 0.89 0.01 0.07 0.10 -0.01<br>-0.27 0.89 0.01 0.09 0.14 -0.02<br>-0.30 0.89 -0.01 0.08 0.11 -0.01<br>-0.27 0.81 0.01 0.14 -0.01 0.07<br>-0.20 0.90 0.01 0.09 -0.02 0.04<br>-0.02 -0.28 0.09 -0.13 0.12 -0.05<br>-0.15 0.19 -0.08 0.10 0.01 0.04 0.11 -0.33 -0.42 -0.09 0.30 -0.09 0.75 0.11 -0.06 -0.04 -0.09 0.39<br>-0.29 -0.18 -0.14 -0.05 0.07 0.26 0.17 -0.03 0.01 -0.43 -0.01 -0.06<br>-0.16 -0.11 -0.22 -0.07 0.26 0.25 0.29 -0.09 -0.44 0.09 0.65 -0.14<br>|

##### Table A-2: Correlations between Estimated Factors and Credit Spreads (Baseline FAVAR Speciﬁcation)

|EDF Quintile/Maturity Category<br><br>|F11 F12 F13 F14 F21 F22|
|---|---|
|EDF-Q1/Short Maturity<br><br>EDF-Q2/Short Maturity<br><br>EDF-Q3/Short Maturity<br><br>EDF-Q4/Short Maturity<br><br>EDF-Q5/Short Maturity<br><br><br>EDF-Q1/Intermediate Maturity<br><br>EDF-Q2/Intermediate Maturity<br><br>EDF-Q3/Intermediate Maturity<br><br>EDF-Q4/Intermediate Maturity<br><br>EDF-Q5/Intermediate Maturity<br><br><br>EDF-Q1/Long Maturity<br><br>EDF-Q2/Long Maturity<br><br>EDF-Q3/Long Maturity<br><br>EDF-Q4/Long Maturity<br><br>EDF-Q5/Long Maturity<br><br><br>EDF-Q1/Very Long Maturity<br><br>EDF-Q2/Very Long Maturity<br><br>EDF-Q3/Very Long Maturity<br><br>EDF-Q4/Very Long Maturity<br><br>EDF-Q5/Very Long Maturity<br><br><br>|-0.13 -0.16 -0.39 0.01 0.35 0.76<br>-0.26 -0.23 -0.53 -0.02 0.51 0.51<br>-0.18 -0.21 -0.58 -0.08 0.54 0.43<br>-0.31 -0.30 -0.54 -0.01 0.62 0.17<br>-0.17 -0.20 -0.54 -0.04 0.60 -0.05<br>-0.05 -0.22 -0.58 0.01 0.67 0.32<br>-0.17 -0.22 -0.53 0.03 0.62 0.42<br>-0.22 -0.26 -0.56 -0.01 0.67 0.25<br>-0.36 -0.26 -0.53 -0.01 0.67 -0.05<br>-0.29 -0.21 -0.54 -0.11 0.58 -0.16 0.19 -0.16 -0.46 0.03 0.78 -0.12 0.10 -0.16 -0.43 0.12 0.76 -0.13 0.04 -0.19 -0.48 0.02 0.77 -0.22<br>-0.11 -0.21 -0.45 0.02 0.77 -0.27<br>-0.13 -0.23 -0.51 -0.08 0.61 -0.30 0.47 -0.06 -0.38 0.04 0.70 -0.14 0.34 -0.12 -0.47 0.09 0.70 -0.20 0.32 -0.11 -0.5 0.04 0.71 -0.19<br>-0.23 -0.24 -0.45 0.07 0.68 -0.29<br>-0.18 -0.16 -0.47 0.13 0.61 -0.27<br>|

## B Impulse Response Functions

Figures B-1–B-4 depict the impact of an orthogonalized one standard deviation shock to credit factor 1 on the 38 macroeconomic and ﬁnancial time series included in the vector X1t in the baseline FAVAR speciﬁcation; Figures B-5–B-6 depict the impact of an orthogonalized one standard deviation shock to credit factor 1 on credit spreads in the 20 EDF-based bond portfolios included in the vector X2t. The shaded bands represent the 95-percent conﬁdence intervals computed using a nonparametric sieve bootstrap with 10,000 replications (see main text for details).

Figure B-1: Economic Activity Indicators (Baseline FAVAR Speciﬁcation)

Unemployment rate

Percentage points

0 12 24 36 48

Months after shock

0.4

0.3

0.2

0.1

0.0

Payroll employment

Percentage points

0.1

0.0

−0.1

−0.2

−0.3

−0.4

−0.5

−0.6

−0.7

0 12 24 36 48

Months after shock

Industrial production

Percentage points

0.5

0.0

−0.5

−1.0

−1.5

−2.0

−2.5

0 12 24 36 48

Months after shock

Capacity utilization

Percentage points

0.2

0.0

−0.2

−0.4

−0.6

−0.8

−1.0

−1.2

0 12 24 36 48

Months after shock

Durable goods orders

Percentage points

- 0
- 1
- 2

−1

−2

−3

−4

−5

0 12 24 36 48

Months after shock

Nondurable goods orders

Percentage points

1.0

0.5

0.0

−0.5

−1.0

−1.5

0 12 24 36 48

Months after shock

Manufacturing activity (ISM)

Percentage points

0.006

0.004

0.002

0.000

−0.002

−0.004

−0.006

0 12 24 36 48

Months after shock

Housing starts

Percentage points

0 12 24 36 48

Months after shock

10

8

6

4

2

0

−2

Consumption spending

Percentage points

0.6

0.4

0.2

0.0

−0.2

−0.4

−0.6

0 12 24 36 48

Months after shock

Index of leading indicators

Percentage points

0.8

0.6

0.4

0.2

0.0

−0.2

−0.4

−0.6

0 12 24 36 48

Months after shock

Disposable personal income

Percentage points

0.004

0.002

0.000

−0.002

−0.004

−0.006

−0.008

−0.010

0 12 24 36 48

Months after shock

Figure B-2: Inﬂation Indicators and the Exchange Value of the Dollar (Baseline FAVAR Speciﬁcation)

CPI

Percentage points

0.2

0.1

0.0

−0.1

−0.2

0 12 24 36 48

Months after shock

Core CPI

Percentage points

0.1

0.0

−0.1

−0.2

−0.3

−0.4

0 12 24 36 48

Months after shock

###### PPI

Percentage points

0.8

0.6

0.4

0.2

0.0

−0.2

0 12 24 36 48

Months after shock

Core PPI

Percentage points

0.2

0.1

0.0

−0.1

−0.2

0 12 24 36 48

Months after shock

Commodity prices

Percentage points

- 0
- 1
- 2

−1

−2

0 12 24 36 48

Months after shock

Price of oil (WTI)

Percentage points

6

4

2

0

−2

−4

−6

0 12 24 36 48

Months after shock

Foreign exchange value of the dollar

Percentage points

1.0

0.5

0.0

−0.5

−1.0

−1.5

−2.0

0 12 24 36 48

Months after shock

Figure B-3: Interest Rates, Interest Rate Uncertainty, and Liquidity Indicators (Baseline FAVAR Speciﬁcation)

Real federal funds rate

Percentage points

0.10

0.05

0.00

−0.05

−0.10

−0.15

−0.20

−0.25

−0.30

0 12 24 36 48

Months after shock

Real 6−month Treasury yield

Percentage points

0.10

0.05

0.00

−0.05

−0.10

−0.15

−0.20

−0.25

−0.30

0 12 24 36 48

Months after shock

Real 1−year Treasury yield

Percentage points

0.1

0.0

−0.1

−0.2

−0.3

0 12 24 36 48

Months after shock

Real 2−year Treasury yield

Percentage points

0.10

0.05

0.00

−0.05

−0.10

−0.15

−0.20

−0.25

−0.30

0 12 24 36 48

Months after shock

Real 3−year Treasury yield

Percentage points

0.10

0.05

0.00

−0.05

−0.10

−0.15

−0.20

−0.25

−0.30

0 12 24 36 48

Months after shock

Real 5−year Treasury yield

Percentage points

0.10

0.05

0.00

−0.05

−0.10

−0.15

−0.20

−0.25

0 12 24 36 48

Months after shock

Real 10−year Treasury yield

Percentage points

0.05

0.00

−0.05

−0.10

−0.15

−0.20

0 12 24 36 48

Months after shock

On/Off−the−run Treasury premium

Percentage points

0.8

0.6

0.4

0.2

0.0

−0.2

0 12 24 36 48

Months after shock

Short−term interest rate uncertainty

Percentage points

0.10

0.05

0.00

−0.05

−0.10

−0.15

0 12 24 36 48

Months after shock

Swap−Treasury spread

Percentage points

0.025

0.020

0.015

0.010

0.005

0.000

−0.005

−0.010

0 12 24 36 48

Months after shock

Long−term interest rate uncertainty

Percentage points

0.20

0.15

0.10

0.05

0.00

−0.05

0 12 24 36 48

Months after shock

Figure B-4: Equity Market Indicators (Baseline FAVAR Speciﬁcation)

Cumulative excess equity return EDF Quintile 1

Percentage points

- 0
- 1
- 2

−1

−2

−3

−4

−5

−6

0 12 24 36 48

Months after shock

Cumulative excess equity return EDF Quintile 2

Percentage points

- 0
- 1
- 2

−1

−2

−3

−4

0 12 24 36 48

Months after shock

Cumulative excess equity return EDF Quintile 3

Percentage points

- 0
- 1
- 2
- 3

−1

−2

−3

−4

0 12 24 36 48

Months after shock

Cumulative excess equity return EDF Quintile 4

Percentage points

- 0
- 1
- 2
- 3

−1

−2

−3

−4

−5

0 12 24 36 48

Months after shock

Cumulative excess equity return EDF Quintile 5

Percentage points

4

2

0

−2

−4

0 12 24 36 48

Months after shock

Cumulative excess stock market return

Percentage points

- 0
- 1
- 2

−1

−2

−3

−4

−5

−6

0 12 24 36 48

Months after shock

S&P 500 implied volatility (VIX)

Percentage points

1.0

0.8

0.6

0.4

0.2

0.0

−0.2

−0.4

−0.6

0 12 24 36 48

Months after shock

Fama−French HML factor

Percentage points

0.3

0.2

0.1

0.0

−0.1

−0.2

−0.3

0 12 24 36 48

Months after shock

Fama−French SMB factor

Percentage points

0.4

0.3

0.2

0.1

0.0

−0.1

−0.2

0 12 24 36 48

Months after shock

Figure B-5: Short and Intermediate Maturity Credit Spreads (Baseline FAVAR Speciﬁcation)

Short term credit spreads

- EDF Quintile 1

0 12 24 36 48

−0.02

0.00

0.02

0.04

0.06

0.08

Percentage points

Months after shock

Short term credit spreads EDF Quintile 2

0 12 24 36 48

−0.02

0.00

0.02

0.04

0.06

0.08

0.10

0.12

Percentage points

Months after shock

Short term credit spreads EDF Quintile 3

0 12 24 36 48

−0.04

−0.02

0.00

0.02

0.04

0.06

0.08

0.10

0.12

0.14

Percentage points

Months after shock

Short term credit spreads

- EDF Quintile 4

0 12 24 36 48

−0.05

0.00

0.05

0.10

0.15

0.20

0.25

Percentage points

Months after shock

Short term credit spreads EDF Quintile 5

0 12 24 36 48

−0.2

0.0

0.2

0.4

0.6

0.8

Percentage points

Months after shock

Intermediate term credit spreads EDF Quintile 1

0 12 24 36 48

−0.02

0.00

0.02

0.04

0.06

0.08

Percentage points

Months after shock

Intermediate term credit spreads EDF Quintile 2

0 12 24 36 48

−0.04

−0.02

0.00

0.02

0.04

0.06

0.08

0.10

0.12

Percentage points

Months after shock

Intermediate term credit spreads EDF Quintile 3

0 12 24 36 48

−0.04

−0.02

0.00

0.02

0.04

0.06

0.08

0.10

0.12

0.14

Percentage points

Months after shock

Intermediate term credit spreads EDF Quintile 4

0 12 24 36 48

−0.05

0.00

0.05

0.10

0.15

0.20

0.25

Percentage points

Months after shock

Intermediate term credit spreads

- EDF Quintile 5

Percentage points

0.6

0.5

0.4

0.3

0.2

0.1

0.0

−0.1

0 12 24 36 48

Months after shock

Figure B-6: Long and Very Long Maturity Credit Spreads (Baseline FAVAR Speciﬁcation)

Long term credit spreads

- EDF Quintile 1

0 12 24 36 48

−0.02

0.00

0.02

0.04

0.06

0.08

0.10

Percentage points

Months after shock

Long term credit spreads EDF Quintile 2

0 12 24 36 48

−0.04

−0.02

0.00

0.02

0.04

0.06

0.08

0.10

0.12

Percentage points

Months after shock

Long term credit spreads EDF Quintile 3

0 12 24 36 48

−0.05

0.00

0.05

0.10

0.15

Percentage points

Months after shock

Long term credit spreads

- EDF Quintile 4

0 12 24 36 48

−0.05

0.00

0.05

0.10

0.15

0.20

0.25

Percentage points

Months after shock

Long term credit spreads EDF Quintile 5

0 12 24 36 48

−0.2

0.0

0.2

0.4

0.6

0.8

Percentage points

Months after shock

| | |
|---|---|
| | |

Very long term credit spreads EDF Quintile 1

0 12 24 36 48

−0.04

−0.02

0.00

0.02

0.04

0.06

0.08

0.10

Percentage points

Months after shock

Very long term credit spreads EDF Quintile 2

0 12 24 36 48

−0.04

−0.02

0.00

0.02

0.04

0.06

0.08

0.10

0.12

Percentage points

Months after shock

Very long term credit spreads EDF Quintile 3

0 12 24 36 48

−0.05

0.00

0.05

0.10

0.15

Percentage points

Months after shock

Very long term credit spreads EDF Quintile 4

0 12 24 36 48

−0.05

0.00

0.05

0.10

0.15

0.20

Percentage points

Months after shock

Very long term credit spreads

- EDF Quintile 5

Percentage points

0.4

0.3

0.2

0.1

0.0

−0.1

0 12 24 36 48

Months after shock

