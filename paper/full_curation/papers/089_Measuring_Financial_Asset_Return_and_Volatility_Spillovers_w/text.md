[Figure 1]

Penn Institute for Economic Research Department of Economics University of Pennsylvania 3718 Locust Walk Philadelphia, PA 19104-6297 pier@econ.upenn.edu http://www.econ.upenn.edu/pier

# PIER Working Paper 07-002

“Measuring Financial Asset Return and Volatility Spillovers, with Application to Global Equity Markets”

by

Francis X. Diebold and Kamil Yilmaz

http://ssrn.com/abstract=956918

## Measuring Financial Asset Return and Volatility Spillovers, With Application to Global Equity Markets

##### Francis X. Diebold

University of Pennsylvania and NBER fdiebold@sas.upenn.edu

##### Kamil Yilmaz

###### Koc University kyilmaz@ku.edu.tr

###### This draft/print: January 2007

Abstract: We provide a simple and intuitive measure of interdependence of asset returns and/or volatilities. In particular, we formulate and examine precise and separate measures of return spillovers and volatility spillovers. Our framework facilitates study of both non-crisis and crisis episodes, including trends and bursts in spillovers, and both turn out to be empirically important. In particular, in an analysis of sixteen global equity markets from the early 1990s to the present, we find striking evidence of divergent behavior in the dynamics of return spillovers vs. volatility spillovers: Return spillovers display a gently increasing trend but no bursts, whereas volatility spillovers display no trend but clear bursts.

JEL classification: F30, G15, F36. Key words: Asset Market, Asset Return, Stock Market, Emerging Market, Market Linkage, Financial Crisis, Herd Behavior, Contagion

Acknowledgements: For helpful comments we thank (without implicating) Roberto Rigobon and Harald Uhlig, and the organizers and participants at the 2006 NBER International Seminar on Macroeconomics in Tallinn, Estonia, especially Michael Binder, Kathryn Dominguez, Jeff Frankel, Francesco Giavazzi, Eric Leeper, Lucrezia Reichlin and Ken West.

- 1. Introduction For many years but especially following the late 1990s Asian crisis, much has been made

of the nature of financial market interdependence, both in terms of returns and return volatilities (e.g., King, Sentana and Wadhwani, 1994; Forbes and Rigobon, 2002). Against this background, we propose a simple quantitative measure of such interdependence, which we call a spillover index, and associated tools that we call spillover tables and spillover plots.

The intensity of spillovers may of course vary over time, and the nature of any timevariation is of potentially great interest. We allow for it in an analysis of a broad set of global equity returns and volatilities from the early 1990s to the present, and we show that spillovers are important, spillover intensity is indeed time-varying, and the nature of the time-variation is strikingly different for returns vs. volatilities.

We proceed by proposing the spillover index in Section 2 and describing our global equity data in Section 3. We perform a full-sample spillover analysis in Section 4 and a rolling-sample analysis allowing for time-varying spillovers in Section 5. We summarize and conclude in Section 6.

- 2. The Spillover Index We base our measurement of return and volatility spillovers on vector autoregressive

(VAR) models in the broad tradition of Engle, Ito and Lin (1990). Our approach, however, is very different. We focus on variance decompositions, which allow us to aggregate spillover effects across markets, distilling a wealth of information into a single spillover measure.

The basic spillover index idea is simple and intuitive, yet rigorous and replicable, following directly from the familiar notion of a variance decomposition associated with an Nvariable vector autoregression. Roughly, for each asset i we simply add the shares of its forecast error variance coming from shocks to asset j, for all j ≠ i, and then we add across all i =1,...,N .

To minimize notational clutter, consider first the simple example of a covariance stationary first-order two-variable VAR,

xt = Φxt− 1 +εt,

where xt = (x1,t,x2,t)' and Φ is a 2x2 parameter matrix. In our subsequent empirical work, x will be either a vector of stock returns or a vector of stock return volatilities. By covariance stationarity, the moving average representation of the VAR exists and is given by

xt = Θ(L)εt ,

whereΘ(L) = (I −ΦL)−1. It will prove useful to rewrite the moving average representation as

xt = A(L)ut , where A(L) = Θ(L)Qt−1, ut = Qtεt, E(utut,) = I, and Qt−1is the unique lower-triangular Cholesky factor of the covariance matrix of εt .

Now consider 1-step-ahead forecasting. Immediately, the optimal forecast (more precisely, the Wiener-Kolmogorov linear least-squares forecast) is

xt+1,t = Φxt , with corresponding 1-step-ahead error vector

a a u e x x A u

⎡ ⎤ ⎡ ⎤ = − = = ⎢ ⎥ ⎢ ⎥

t t t t t t t ,

0,11 0,12 1, 1 1, 1 1, 0 1

+

+ + + +

a a u

⎣ ⎦ ⎣ ⎦ which has covariance matrix

t

0,21 0,22 2, 1

+

' '

E(et+1,tet+1,t) = A0A0. Hence, in particular, the variance of the 1-step-ahead error in forecasting x1t isa0,112 + a0,122 , and the variance of the 1-step-ahead error in forecasting x2t isa0,212 + a0,222 .

Variance decompositions allow us to split the forecast error variances of each variable into parts attributable to the various system shocks. More precisely, for the example at hand, they answer the questions: What fraction of the 1-step-ahead error variance in forecasting x1 is due to shocks to x1? Shocks to x2? And similarly, what fraction of the 1-step-ahead error variance in forecasting x2 is due to shocks to x1? Shocks to x2?

Let us define own variance shares to be the fractions of the 1-step-ahead error variances in forecasting xi due to shocks to xi , for i=1, 2, and cross variance shares, or spillovers, to be the fractions of the 1-step-ahead error variances in forecasting xi due to shocks to xj , for i, j=1, 2, i ≠ j. There are two possible spillovers in our simple two-variable example: x1tshocks that affect the forecast error variance of x2t (with contributiona0,212 ), and x2t shocks that affect the forecast error variance of x1t (with contribution a0,122 ). Hence the total spillover is a0,122 + a0,212 . We can convert total spillover to an easily-interpreted index by expressing it relative to total forecast error variation, which is a0,112 + a0,122 + a0,212 + a0,222 = trace(A0A0' ) . Expressing the ratio as a percent, the Spillover Index is

2 2 0,12 0,21

a a S

+

= i .

100 ( )

' 0 0

trace A A

Having illustrated the Spillover Index in a simple first-order two-variable case, it is a simple matter to generalize it to richer dynamic environments. In particular, for a pth-order Nvariable VAR (but still using 1-step-ahead forecasts) we immediately have

N

∑

2 0,

a S

ij

i j i j

, 1

=

= ≠

100 ( )

i ,

' 0 0

trace A A

and for the fully general case of a pth-order N-variable VAR, using H-step-ahead forecasts, we have

H N

1

−

### ∑ ∑ ∑

2

a S

h ij h i j

, 0 , 1

= =

i j H

≠ −

i .

100 ( )

=

1

' 0

trace A A

h h h

=

Such generality is often useful. In the empirical work that follows, for example, we use secondorder 16-variable VARs with 10-step-ahead forecasts.

###### 3. Global Equity Market Return and Volatility Data

Our underlying data are daily nominal local-currency stock market indices, January 1992 September 2005, taken from Datastream and Global Financial Data. We use four major indices: The Dow Jones Industrial Average for the New York Stock Exchange, the FTSE-100 index for the London Stock Exchange, the Hang Seng index for the Hong Kong Stock Exchange, and the Nikkei 225 index for the Tokyo Stock Exchange. Similarly, we use daily nominal local-currency stock market indices for twelve emerging markets: Indonesia, South Korea, Malaysia, Philippines, Singapore, Taiwan, Thailand, Argentina, Brazil, Chile, Mexico and Turkey.

We calculate returns as the change in log price, Wednesday-to-Wednesday. When price data for Wednesday are not available due to a holiday, we use Thursday. We then convert weekly returns from nominal to real terms using monthly consumer price indices from the IMF’s International Financial Statistics. To do so we assume that the weekly inflation rate πt is constant within the month, in which case we can calculate it simply as the 1/4th power of the monthly inflation rate, and we then calculate the weekly real return as

i

1

+

, where it is the

1 1

−

t

+

π

t

weekly nominal return. We provide a variety of descriptive statistics for returns in Table 1.

We assume that volatility is fixed within periods (in this case, weeks) but variable across periods. Then, following Garman and Klass (1980) and Alizadeh, Brandt and Diebold (2002), we can use weekly high, low, opening and closing prices obtained from underlying daily high/low/open/close data to estimate weekly stock return volatility:

[ ]

σ2 = 0.511(Ht − Lt )2 − 0.019 (Ct − Ot )(Ht + Lt − 2Ot ) − 2(Ht − Ot )(Lt − Ot ) − 0.383(Ct − Ot )2,

where H is the Monday-Friday high, L is the Monday-Friday low, O is the Monday open and C is the Friday close (all in natural logarithms). We provide descriptive statistics for volatilities in Table 2.

###### 4. Full-Sample Analysis: Spillover Tables

Here we provide a full-sample analysis of global stock market return and volatility spillovers. As part of that analysis, we propose decomposing the Spillover Index into all of the forecast error variance components for variable i coming from shocks to variable j, for all i and j.

We begin by characterizing return and volatility spillovers over the entire sample, January 1992-September 2005. Subsequently we will track time variation in spillovers via rolling window estimation.) We report Spillover Indexes for returns and volatility in the lower right corners of Tables 3 and 4, respectively. Before discussing them, however, let us describe the rest of the two tables, which we call Spillover Tables. The ijth entry in the table is the estimated contribution to the forecast error variance of country i (returns in Table 3, volatility in Table 4) coming from innovations to country j (again, returns in Table 3, volatility in Table 4).1 Hence the off-diagonal column sums (labeled Contributions to Others) or row sums (labeled Contributions from Others), when totaled across countries, give the numerator of the Spillover Index. Similarly, the column sums or row sums (including diagonals), when totaled across countries, give the denominator of the Spillover Index.

The Spillover Table, then, provides an “input-output” decomposition of the Spillover Index. For example, we learn from Spillover Table 3 (for returns) that innovations to U.S. returns are responsible for 18.1 percent of the error variance in forecasting 10-week-ahead Mexican returns, but only 3.1 percent of the error variance in forecasting 10-week-ahead Turkish returns. That is, return spillovers from the U.S. to Mexico are larger than for the U.S. to Turkey. As another example, we see from Table 4 (volatility) that total volatility spillovers from Hong Kong to others (that is, Hong Kong Contributions to Others) are much large than total volatility spillovers from others to Hong Kong (Hong Kong Contributions from Others).

The key substantive summary result to emerge from Tables 3 and 4 is that, distilling all of the various cross-country spillovers into a single Spillover Index for our full 1992-2005 data sample, we find that approximately thirty percent of forecast error variance comes from spillovers, both for returns (29 percent) and volatilities (31 percent). Hence spillovers are important in both returns and volatilities, and on average – that is, unconditionally – return and volatility spillovers are of the same magnitude.

However, at any given point in time – that is, conditionally – return and volatility spillovers may be very different, and more generally, their dynamics may be very different. We

1 The results are based on weekly vector autoregressions of order 2 (selected using the Schwarz criterion), identified using a Cholesky factorization with the ordering as shown in the column heading, and 10-week-ahead forecasts.

now substantiate these assertions by moving from a static full-sample analysis to a dynamic rolling-sample analysis.

###### 5. Rolling-Sample Analysis: Spillover Plots

Clearly, many changes took place during the years in our sample, 1992-2005. Some are well-described as more-or-less continuous evolution, such as increased linkages among global financial markets and increased mobility of capital, due to globalization, the move to electronic trading, and the rise of hedge funds. Others are better described as bursts that subsequently subside, such as the various Asian currency crises around 1997.

Given this background of financial market evolution and turbulence, it seems unlikely that any single fixed-parameter model would apply over the entire sample. Hence the full-sample Spillover Tables and Spillover Indexes obtained earlier, although providing a useful summary of “average” behavior, likely miss the potentially important secular and cyclical movements in spillovers. To address this issue, we now estimate the models using 200-week rolling samples, and we assess the extent and nature of spillover variation over time via the corresponding time series of Spillover Indexes, which we examine graphically in Spillover Plots.

In Figure 1, we present the Spillover Plot for returns. It is largely uneventful, displaying a gently increasing trend, but little else. Notice that even as the estimation window moves beyond the mid-1990s, the Spillover Plot never declines to its early lower range. This is consistent with a maintained increase in financial market integration.

The Spillover Plot for volatilities, which we present in Figure 2, is radically different. It ranges widely and responds to economic events. Some of those events are major, such as the East Asian currency crises in late 1997 (the devaluation of Thai Baht in July 1997, the spread to Hong Kong in October 1997, and further spread to other major economies in the region such as South Korea, Malaysia and Indonesia through January 1998). Another example is the June-August 1998 Russian crisis (the first wave was controlled by the IMF’s announcement of a support package in June 1998, and the final outbreak occurred in August 1998). Both of these crises produced a large spike in volatility spillovers.

Interestingly, volatility spillovers also respond to less major (but nevertheless important and well-known) crises. For example, comparatively minor emerging market crises are reflected in small spikes in the volatility spillover measures. Indeed, during our sample period there were nine widely-acknowledged crisis events: (1) The Mexican crisis of December 1994 - January 1995, (2) the East Asian crisis of October - December 1997, (3) the Russian crisis of August September 1998, (4) the Brazilian crisis of January 1999, (5) the Turkish Crisis of December 2000 - February 2001, (6) the U.S. terrorist attack of September 11, 2001, (7) the Argentinean Crisis of November 2001, (8) the downgrading to junk status of GM and Ford debt, followed by a short-lived reversal of international capital flows from emerging market economies, of March 2005, (9) the intense reversal of capital flows from emerging markets of May-June 2006. All of these events generated increases in volatility spillovers, as shown in Figure 2, whereas none generated movements in return spillovers.

###### 6. Summary and Concluding Remarks

We have proposed a simple framework for measuring linkages in asset returns and return volatilities. In particular, we have formulated and examined precise measures of return spillovers and volatility spillovers based directly on the familiar notion of vector autoregressive variance decompositions. Our spillover measures have the appealing virtue of conveying important and useful information while nevertheless sidestepping the contentious issue of definition and existence of episodes of “contagion” so vigorously debated in recent literature such as Forbes and Rigobon (2002).

Our framework facilitates study of both crisis and non-crisis episodes, including trends as well as bursts in spillovers. In an analysis of sixteen global equity markets from the early 1990s to the present, we find striking evidence of divergent behavior in the dynamics of return spillovers vs. volatility spillovers. Return spillovers display no bursts but a gently increasing trend, presumably associated with the gradually increasing financial market integration of the last fifteen years. Volatility spillovers, in contrast, display no trend but clear bursts associated with readily-identified “crisis” events.

Although we have not reported them here in order to conserve space, we have performed several variations on the basic theme reported here, and our results appear robust. Such

###### variations include but are not limited to the VAR lag order, the width of the rolling VAR estimation window, and the forecast horizon for variance decompositions.

###### References

Alizadeh, Sassan, Michael W. Brandt and Francis X. Diebold (2002), “Range-Based Estimation of Stochastic Volatility Models,” Journal of Finance, 57, 1047-1092.

Engle, Robert F., Takatoshi Ito and Wen-Ling Lin (1990), “Meteor Showers or Heat Waves? Heteroskedastic Intra-Daily Volatility in the Foreign Exchange Market,” Econometrica, 58, 525542.

Forbes, Kristen J. and Roberto Rigobon (2002), “No Contagion, Only Interdependence: Measuring Stock Market Comovements,” Journal of Finance, 57, 2223-2261.

Garman, Mark B. and Michael J. Klass (1980), “On the Estimation of Security Price Volatilities from Historical Data,” Journal of Business, 53, 67-78.

King, Mervyn, Enrique Sentana and Sushil Wadhwani (1994), “Volatility and Links Between National Stock Markets,” Econometrica, 62, 901-933.

###### Table 1 Descriptive Statistics, Global Stock Market RETURNS, 1/1992 – 9/2005

United States US

United Kingdom UK

Hong Kong HKG

South Korea KOR

Japan JPN

Indonesia IDN

Malaysia MYS

Philippines PHL

Mean 0.00112 0.00057 0.00130 -0.00079 -0.00033 0.00011 0.00014 -0.00056 Median 0.00186 0.00156 0.00219 0.00041 0.00142 -0.0007 0.00040 -0.00091 Maximum 0.0976 0.1349 0.1370 0.1205 0.1684 0.1657 0.2791 0.1349 Minimum -0.0932 -0.1035 -0.1423 -0.1024 -0.1304 -0.1797 -0.2101 -0.1550 Std. Dev. 0.0211 0.0228 0.0349 0.0302 0.0353 0.0427 0.0361 0.0364 Skewness -0.1607 0.2515 -0.4493 0.0388 -0.0965 -0.0495 0.4289 0.1019 Kurtosis 5.18 6.90 4.48 4.21 5.62 4.76 11.80 4.51

Singapore SGP

Taiwan TAI

Thailand THA

Argentina ARG

Brazil BRA

Chile CHL

Mexico MEX

Turkey TUR

Mean 0.00067 0.00006 -0.00070 0.00008 0.00187 0.00080 0.00087 0.00050 Median -0.00018 0.00167 0.00036 0.00429 0.00734 0.00102 0.00154 0.00191 Maximum 0.1467 0.1485 0.1930 0.2571 0.3054 0.0946 0.1739 0.2589 Minimum -0.1165 -0.1160 -0.1397 -0.2216 -0.2786 -0.1136 -0.1319 -0.3313 Std. Dev. 0.0300 0.0371 0.0412 0.0546 0.0593 0.0210 0.0382 0.0680 Skewness 0.0674 0.0498 0.2416 -0.3485 -0.5742 -0.0109 -0.0140 -0.2868 Kurtosis 5.43 3.98 4.41 4.84 7.40 6.02 4.55 5.55

Notes: Returns are in real terms and measured weekly, Wednesday-to-Wednesday. The sample size is 717. See text for details.

###### Table 2 Descriptive Statistics, Global Stock Market VOLATILITY, 1/1992 – 9/2005

###### US UK HKG JPN IDN KOR MYS PHL

Mean 0.00043 0.00051 0.00106 0.00076 0.00091 0.00138 0.00093 0.00066 Median 0.00025 0.00025 0.00057 0.00053 0.00036 0.00069 0.00027 0.00033 Maximum 0.00595 0.00926 0.03794 0.00798 0.02074 0.01869 0.04592 0.01798 Minimum 1.98E-05 1.14E-05 1.55E-05 1.88E-05 3.97E-07 8.22E-10 4.41E-06 4.74E-06 Std. Dev. 0.00058 0.00083 0.00216 0.00082 0.00178 0.00204 0.00306 0.00145

- Skewness 4.330 5.248 9.839 3.473 4.918 3.63574 9.9146 8.06104 Kurtosis 29.221 41.012 141.313 21.203 36.495 20.574 121.400 85.161

SGP TAI THA ARG BRA CHL MEX TUR

Mean 0.00045 0.00085 0.00118 0.00204 0.00225 0.00018 0.00104 0.00344 Median 0.00018 0.00053 0.00063 0.00096 0.00115 8.21E-05 0.00053 0.00165 Maximum 0.0105 0.01376 0.01699 0.03371 0.06133 0.00816 0.02871 0.07689 Minimum 6.21E-07 9.38E-06 5.22E-05 6.41E-06 1.22E-08 1.77E-07 7.18E-07 6.67E-07 Std. Dev. 0.00082 0.00104 0.0017 0.00344 0.00445 0.00043 0.00189 0.00572

- Skewness 5.201 4.648 4.393 4.761 7.331 11.232 7.694 6.442 Kurtosis 44.325 43.029 30.862 32.769 74.263 178.011 89.782 66.010

Notes: Volatilities are for Monday-to-Friday returns. The mnemonics are as in Table 1. We calculate Chile’s volatility using the Santiago Stock Exchange IGPA Index for 1/1992 – 5/2004 and the Santiago Stock Exchange IPSA index for 6/2004 – 9/2005. The sample size is 717. See text for details.

###### Table 3 Spillover Table, Global Stock Market RETURNS, 1/1992-9/2005

F R O M

Contribution From Others

US UK HKG JPN IDN KOR MYS PHL SGP TAI THA ARG BRA CHL MEX TUR

US 95.4 0.4 1.0 0.4 0.0 0.4 0.1 0.8 0.3 0.1 0.2 0.4 0.2 0.2 0.0 0.1 5 UK 39.1 57.8 0.2 0.5 0.3 0.1 0.2 0.7 0.0 0.1 0.4 0.0 0.1 0.0 0.1 0.4 42 HKG 16.0 9.0 70.9 0.3 0.2 0.4 1.0 0.1 0.1 0.6 0.4 0.1 0.5 0.4 0.0 0.1 29 JPN 11.4 3.4 2.2 79.4 0.1 0.4 0.4 0.2 0.0 0.5 0.5 0.0 0.0 1.2 0.3 0.1 21 IDN 6.4 1.9 5.7 1.0 79.0 1.3 0.3 0.6 0.4 0.2 0.7 0.9 0.5 0.3 0.6 0.2 21 KOR 6.8 3.7 6.6 4.2 1.4 75.5 0.1 0.5 0.0 0.1 0.4 0.4 0.2 0.1 0.1 0.1 24 MYS 4.1 1.5 11.0 0.5 7.6 1.0 72.8 0.1 0.1 0.1 0.1 0.2 0.5 0.1 0.1 0.0 27 PHL 8.8 1.7 7.1 0.2 7.5 1.5 2.3 66.0 0.3 0.8 1.8 1.5 0.0 0.1 0.2 0.1 34 SGP 15.8 5.6 18.8 1.5 4.0 1.6 6.9 1.7 41.4 0.5 0.7 0.6 0.6 0.2 0.0 0.0 59 TAI 7.7 1.5 4.9 2.5 0.3 1.5 1.9 0.2 0.7 77.7 0.2 0.1 0.0 0.2 0.3 0.2 22 THA 7.9 3.3 7.9 0.1 9.7 3.7 3.6 1.2 0.9 0.3 59.2 1.1 0.2 0.4 0.3 0.1 41 ARG 7.5 2.0 1.8 0.9 0.7 0.2 0.2 0.6 0.7 1.2 0.5 82.6 0.1 0.3 0.6 0.2 17 BRA 12.8 0.9 1.9 1.3 0.1 0.8 1.0 0.6 0.2 0.2 0.2 7.6 71.6 0.2 0.4 0.2 28 CHL 8.2 1.0 4.9 0.9 1.8 0.1 0.5 0.2 0.9 0.6 1.6 4.0 5.7 68.3 1.0 0.2 32 MEX 18.1 3.9 3.8 0.8 0.2 0.6 0.1 0.2 0.2 0.3 0.5 9.2 4.0 1.2 56.8 0.1 43

###### T O

TUR 3.1 1.9 0.5 1.0 0.8 0.4 0.3 0.1 0.6 0.3 0.7 0.4 0.7 0.4 0.5 88.1 12 Contribution To Others

174 42 78 16 35 14 19 8 6 6 9 26 13 5 5 2 458

Contribution Including Own

Spillover Index = 29%

269 100 149 96 114 89 92 74 47 84 68 109 85 74 61 90

Notes: We present variance decompositions based upon a weekly vector autoregression of order 2 identified using a Cholesky factorization with the ordering as shown in the column heading. The (i, j)-th value is the estimated contribution TO the variance of the 10-week-ahead real stock return forecast error of country i coming FROM innovations to real stock returns of country j. The mnemonics are defined as in Table 1.

###### Table 4 Spillover Table, Global Stock Market VOLATILITY, 1/1992-9/2005

F R O M US UK HKG JPN IDN KOR MYS PHL SGP TAI THA ARG BRA CHL MEX TUR

Contribution From Others

US 69.1 17.2 5.6 0.2 0.3 1.4 0.8 0.6 1.7 0.2 0.1 0.2 0.1 0.1 0.1 2.3 31 UK 28.9 57.1 7.8 0.5 0.4 1.0 0.5 0.1 1.2 0.2 0.2 0.5 0.3 0.2 0.4 0.7 43 HKG 1.7 0.5 89.0 0.1 0.5 1.2 0.5 1.6 3.0 0.6 0.7 0.0 0.1 0.0 0.1 0.3 11 JPN 3.4 3.2 1.8 84.8 0.0 0.7 1.0 0.2 1.0 0.2 0.0 0.5 0.3 0.1 0.0 2.7 15 IDN 2.3 0.7 6.6 0.5 73.4 7.1 2.2 2.8 2.2 0.7 0.1 0.0 0.1 0.3 0.1 0.9 27 KOR 4.1 0.7 9.0 1.1 10.6 68.5 1.2 1.1 1.6 0.7 0.3 0.1 0.2 0.0 0.1 0.7 31 MYS 1.1 0.6 7.6 1.2 0.9 1.5 72.1 3.3 4.8 0.4 0.5 1.1 0.7 0.2 1.8 2.3 28 PHL 1.3 0.3 9.2 0.4 8.9 3.3 6.4 67.1 1.2 0.1 0.3 0.3 0.3 0.2 0.3 0.5 33 SGP 10.1 3.9 13.5 1.0 8.0 7.6 2.6 1.6 47.1 0.7 0.2 1.1 0.6 0.0 0.5 1.5 53 TAI 9.3 0.3 2.6 0.6 0.6 8.8 0.8 2.0 0.5 71.4 0.5 0.3 0.9 0.1 0.5 0.9 29 THA 0.6 0.8 11.4 0.3 4.5 3.5 0.4 1.3 7.5 0.5 67.5 0.1 0.5 0.1 0.8 0.2 32 ARG 2.8 1.3 3.0 0.5 0.3 0.1 2.2 0.2 0.4 0.3 0.7 85.0 1.0 0.3 0.7 1.1 15 BRA 2.7 2.3 13.7 0.3 1.0 0.3 10.4 0.8 2.5 0.5 0.2 14.0 48.2 0.1 1.9 1.0 52 CHL 0.5 0.6 4.3 0.1 1.0 0.2 3.2 0.1 0.7 0.3 0.2 5.4 7.4 75.8 0.2 0.1 24 MEX 5.8 1.2 27.1 0.3 0.5 0.5 2.7 0.4 1.5 0.2 0.7 7.4 3.0 0.6 47.2 1.0 53

###### T O

TUR 3.2 1.5 4.1 0.4 0.4 1.0 2.7 0.5 0.7 3.8 0.1 0.8 0.2 0.4 1.3 79.0 21 Contribution To Others

78 35 127 7 38 38 38 17 30 9 5 32 16 3 9 16 498

Contribution Including Own

Spillover Index = 31%

147 92 216 92 111 107 110 84 77 81 72 117 64 79 56 95

Notes: We present variance decompositions based upon a weekly vector autoregression of order 2 identified using a Cholesky factorization with the ordering as shown in the column heading. The (i, j)-th value is the estimated contribution TO the variance of the 10-week-ahead stock return volatility forecast error of country i coming FROM innovations to the stock return volatility of country j. We calculate Chile’s volatility using the Santiago Stock Exchange IGPA Index for January 1992-May 2004, and the Santiago Stock Exchange IPSA index for June 2004-September 2005. The mnemonics are defined as in Table 1.

-13-

###### Figure 1 Spillover Plot, Global Stock Market RETURNS, 11/1995-9/2005

90

| | | | | | | | | |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |

80

70

Index

60

50

40

30

11/95 11/96 11/97 11/98 11/99 11/00 11/01 11/02 11/03 11/04

Ending Date of Window

Notes: The return Spillover Index is the sum of all variance decomposition “contributions to others” from Table 3, estimated using a 200-week rolling window. See text for details.

###### Figure 2 Spillover Plot, Global Stock Market VOLATILITY, 11/1995-9/2005

Virus spread

90

|Cri Tha<br><br>Virus to Hong<br><br>to|sis in iland<br><br>spread Kong<br><br>other EA markets|Russ crisi<br><br>|Brazil crisis<br><br>ian s|ian<br><br>Tur cr|kish isis<br><br>te<br><br>|9/11 rrorist<br><br>attacks|Russian cri data out<br><br>Rever Fed In<br><br>rate p stan|sis<br><br>sal in terest olicy<br><br>ce<br><br>GM<br><br>bonds junk-bon|9/11 out<br><br>/Ford given d status<br><br>|
|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | |

data

80

70

Index

60

50

40

30

11/95 11/96 11/97 11/98 11/99 11/00 11/01 11/02 11/03 11/04

Ending Date of Window

Notes: The volatility Spillover Index is the sum of all variance decomposition “contributions to others” from Table 4, estimated using a 200-week rolling window. See text for details.

[Figure 2]

[Figure 3]

[Figure 4]

[Figure 5]

[Figure 6]

[Figure 7]

[Figure 8]

[Figure 9]

[Figure 10]

[Figure 11]

[Figure 12]

###### Hello PIER (Penn Institute for Econ). (If you are not PIER (Penn Institute for Econ) Submitter, click here.)

#### Measuring Financial Asset Return and Volatility Spillovers, With Application to Global Equity Markets

[Figure 13]

FRANCIS X. DIEBOLD University of Pennsylvania - Department of Economics; National Bureau of Economic Research (NBER) KAMIL YILMAZ Koc University - Department of Economics

Paper Stats: Abstract Views: 1 Downloads: 0

PIER Working Paper No. 07-002

Abstract:

We provide a simple and intuitive measure of interdependence of asset returns and/or volatilities. In particular, we formulate and examine precise and separate measures of return spillovers and volatility spillovers. Our framework facilitates study of both non-crisis and crisis episodes, including trends and bursts in spillovers, and both turn out to be empirically important. In particular, in an analysis of sixteen global equity markets from the early 1990s to the present, we find striking evidence of divergent behavior in the dynamics of return spillovers vs. volatility spillovers: Return spillovers display a gently increasing trend but no bursts, whereas volatility spillovers display no trend but clear bursts.

Keywords: : Asset Market, Asset Return, Stock Market, Emerging Market, Market Linkage, Financial Crisis, Herd Behavior, Contagion

JEL Classifications: F30, G15, F36 Accepted Paper Series

Contact Information for FRANCIS X. DIEBOLD (Contact Author) Email address for FRANCIS X. DIEBOLD

University of Pennsylvania - Department of Economics 3718 Locust Walk Philadelphia , PA 19104 United States 215-898-1507 (Phone) 215-573-4217 (Fax)

(No e-mail address available for FRANCIS X. DIEBOLD National Bureau of Economic Research (NBER) 1050 Massachusetts Avenue Cambridge , MA 02138 United States

Contact Information for KAMIL YILMAZ Email address for KAMIL YILMAZ

Koc University - Department of Economics Rumeli Feneri Yolu Sariyer 80910, Istanbul Turkey

+90 212 338 1458 (Phone)

+90 212 338 1653 (Fax)

###### Email Abstract or URL

[Figure 14]

SSRN Resources To search for other abstracts in the SSRN archival database, click here. To order a membership to an SSRN Network or to subscribe to one or more of SSRN's journals, go to our online subscription request form. To go to SSRN's main web site (www.ssrn.com), click here.

###### © 2007 Social Science Electronic Publishing, Inc. All Rights Reserved. Terms of Use This page was served by hermes3 in 0.47 seconds.

