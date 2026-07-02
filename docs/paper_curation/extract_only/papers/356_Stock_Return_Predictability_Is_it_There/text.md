# 1 Introduction

A large body of empirical work has accumulated documenting excess stock return predictability. Among the most popular predictors are the nominal interest rate and the dividend yield.1 The dividend yield appears to be the most popular stock return predictor used in applied work, but more recently Lamont (1998) and Campbell and Shiller (1988) argue that the earnings yield, has independent forecasting power for excess stock returns in addition to the dividend yield.

The debate on what drives the predictability continues. It may reﬂect irrational investor behavior and hence be exploitable in trading strategies (see Cutler, Poterba and Summers (1989)); it may reﬂect time-varying risk premiums (Kandel and Stambaugh (1990)), Campbell and Cochrane (1999), Bekaert and Grenadier (2000)); or it may simply not be present in the data. This last possibility gains credulity considering the long list of authors criticizing the statistical methodologies in the predictability literature. The coefﬁcients on the predictor variables are biased, since these variables are typically persistent, endogenous regressors correlated with returns innovations (Stambaugh (1999)). The standard focus on long-horizon regressions is problematic from a number of different perspectives. The distributions of the (Kirby (1997)) and the t-statistics on the coefﬁcients, (Richardson and Stock (1989), Richardson and Smith

- (1991), Hodrick (1992) and Valkanov (2000)) in long-horizon regressions are severely shifted to the right, leading to over-rejection of the no-predictability null. Researchers often forget to properly interpret various tests over different horizons by providing joint tests (Richardson

(1993)). Finally, the possibility of decades of data mining clouds any inference regarding predictability for US stock returns (Lo and MacKinlay (1990), Foster, Smith and Whaley (1997) and Bossaerts and Hillion (1999)).

In this paper, we re-examine the case for the predictability of short and long-horizon stock returns. We start by proposing a simple price earnings model, in which the variation in the price-earnings ratio and expected returns on equities is driven by three stochastic state variables, the payout ratio, earnings growth and the short rate. In this model, the earnings yield, the dividend yield and the short rate jointly capture any potential predictability, motivating a simple multivariate regression of excess stock returns over various horizons on these three variables as the main predictability regression. When certain parameter restrictions are met, the model has a (near) constant expected excess return variant, in which the expected gross return on equity equals a constant multiple of the short rate.

[Figure 1]

- 1 For predictability of excess stock returns by the nominal interest rate see, among others, Fama and Schwert

(1977), Campbell (1987), Breen, Glosten and Jagannathan (1989), Shiller and Beltratti (1992), and Lee (1992). Among those examining the predictive power of the dividend yield on excess stock returns are Fama and French (1988), Campbell and Shiller (1988, 1989), Goetzmann and Jorion (1993, 1995), Hodrick (1992), Goyal and Welch (1999) and Valkanov (2000).

Given the considerable statistical challenges in establishing predictability, we preceed our analysis of the data with an extensive Monte Carlo analysis under the null of no predictability. Our analysis incorporating earnings yields largely corroborates the results of Boudoukh and Richardson (1993), Hodrick (1992), and Richardson and Smith (1991) who suggested that the ﬁnite sample properties of the long-horizon regression t-statistics improve dramatically by removing the moving average structure in the error terms, induced by summing returns over long horizons, in constructing the standard errors. For brevity, we will refer to these alternative standard errors as Hodrick (1992) standard errors. As Goetzmann and Jorion (1993, 1995) point out, standard Monte Carlo analysis ignores the fact that yield variables involve the inverse of price, an endogenous variable, which is also present in the denominator of the return on the left hand side. They conduct bootstrap exercises that impose this constraint, but their bootstrap keeps dividends non-stochastic at their data levels and therefore ignores the cointegration relation between dividends and price levels that characterizes rational pricing. By simulating the constant expected return variant of our earnings model, we accommodate this endogeneity constraint in an entirely coherent way.2 It remains true that the Hodrick standard errors are far superior in conducting inference and have negligible size distortions, whereas Ordinary Least Squares (OLS) or Hansen-Hodrick (1980) standard errors lead to severe over-rejections of the no predictability null at long horizons.

Armed with well-behaved t-statistics, we establish that the predictability evidence for US returns is surprisingly weak. In fact, the only variable retaining signiﬁcance is the short rate, and it is only signiﬁcant at short horizons. To mitigate data snooping concerns, we investigate analogous predictability regressions for four other countries, France, Germany, Japan and the UK. Interestingly, we ﬁnd that the predictability coefﬁcients are not robust across countries in sign or magnitude, except for the short rate effect. When we pool the regression across countries, the short rate remains the only signiﬁcant predictor of excess stock returns.

Finally, we also investigate a number of cross-country predictability regressions, examining whether any predictors have predictive power across countries. Unlike Bekaert and Hodrick

- (1992) and Ferson and Harvey (1993), we only ﬁnd evidence of strong predictability when we pool across countries. With cross-sectional information from international data we ﬁnd that US instruments are strong predictors of foreign equity returns, unlike local instruments. The local short rate effect is subsumed by the predictive power of the US short rate. We also conﬁrm and extend Bekaert and Hodrick (1992)’s ﬁnding that yield variables have predictive power for excess returns in the foreign exchange market. We conclude that the current predictability

[Figure 2]

2 Bollerslev and Hodrick (1996) provide a detailed Monte Carlo analysis in the context of a present value model with constant and time-varying expected return variants which also imposes this constraint, but their solution to the present value model is only approximately true.

debate focuses on the wrong horizon (long-run instead of short-run), the wrong instruments (yield variables instead of interest rates) and the wrong setting (US segmented market instead of a globally integrated market).

The remainder of the paper is organized as follows. Section 2 sets out the empirical framework, including the present value earnings model and the predictability regressions. Section 3 describes the econometric estimation, the Monte Carlo analysis and describes the data. Section 4 considers the predictability in US returns, whereas Section 5 investigates and compares predictability in all 5 countries. Section 6 investigates predictability across countries. Section 7 concludes and offers an interpretation of our results.

# 2 Theoretical and Econometric Framework

## 2.1 A Simple Present Value Model

Modern predictability regressions consider the predictability of excess stock returns, the return on equity over and above the return on a nominally risk-free security of the same holding period, which is known one period in advance. Since there is substantial time-variation in interest rates, and it is likely that expected stock returns vary with the interest rate, the hypothesis of interest is the constancy of the conditional equity premium, not the constancy of expected stock returns. Building present value models that imply constant excess stock returns, but allow time-varying interest rates is a non-trivial matter. Most of the recent work on present value models with timevarying discount rates builds on Campbell and Shiller (1989) who, by linearizing returns around steady state log price dividend ratios, obtain a tractable linear present value model in which it is straightforward to impose the constancy of expected excess returns while allowing for variation in interest rates. More recently, the term structure models in the afﬁne class (see Dufﬁe and Kan (1996)) have been applied to stock pricing to yield tractable pricing equations in many settings without linearization (see Ang and Liu (2001) and Bekaert and Grenadier (2000)). We deviate from this literature by presenting a model for price earnings ratios.

Stock returns from time to can always be decomposed as:

[Figure 3]

[Figure 4]

[Figure 5]

where is the stock price at time , is the dividend paid at time , is the payout ratio of dividends to earnings , is the price-earnings ratio. Deﬁning as log growth in earnings and as the log payout ratio ,

we have:

[Figure 6]

(1)

In this pricing framework, we have decomposed dividend growth into earnings growth and a payout ratio. From a theoretical perspective, dividend growth should sufﬁce to price stocks, but our decomposition may yield more accurate pricing formulas in ﬁnite samples. First, in ﬁnite samples using dividends may be problematic, since they are often manipulated, smoothed, or set to zero, making them poor indicators of the true value-relevant cashﬂows in the future. It is no surprise that in the real world analysts almost entirely focus on earnings growth. Second, the decomposition simply increases the information set for prediction, and will include a model that features only dividend growth as a special case.

The model has three state variables, the short rate , log earnings growth and the log payout ratio . Denote which we assume to follow a ﬁrst-order Vector Autoregression:

- (2)

where . To price equity, we use the Dividend Discount Model:

- (3)

where is the stochastic discount factor applying to payoffs at time . To ensure the absence of arbitrage (Harrison and Kreps (1979)) we model the one-period log pricing kernel

, such that:

[Figure 7]

(4)

where is a 3 1 vector containing the prices of risk and the discount factor can be written as:

We also impose conditions on the parameters vec vech so that the transversality condition

is satisﬁed, ruling out bubbles.

Proposition 2.1 In this economy the price-earnings ratio is given by:

[Figure 8]

where is a 3 1 vector of zeros with a 1 in the th place.

- (5)

where and are given by the recursive relations:

[Figure 9]

- (6)

with starting values:

[Figure 10]

- (7)

The term reveals that an increase in the short rate decreases the price earnings ratio, unless it simultaneously predicts higher earnings growth in the future with a feedback coefﬁcient larger than 1 ( where subscripts denote matrix elements). Similarly, if earnings growth shows positive persistence, higher earnings growth leads, ceteris paribus, to higher price earnings ratios.

Since only dividend growth can be priced, we must link the price of risk of dividend growth to the price of risk of the payout ratio and earnings growth. Using the fact that log dividend growth can be written as , this is accomplished by setting:

cov cov

Observation 2.1 For the three-factor system to yield the same pricing relation as a two-factor model using the prices of risk of dividend growth, earnings growth and log payout ratio ( , and respectively) must satisfy:

(8)

Intuitively, both an increase in earnings growth or an increase in the payout ratio increase dividend growth by the same amount. Hence the price of risk ought to be the same for earnings growth and log payout. We can then impose the constraint .

The expected excess simple return and volatility will be a constant multiple of the gross short rate in this economy under the following sufﬁcient conditions stated in the following two corollaries:

- Corollary 2.1 Suppose the companion matrix in the Vector Autoregression for takes the form:

(9)

Then the conditional expected simple risk premium is a multiple of the gross short rate and given by:

- (10)

where . The unconditional expected simple return is given by:

[Figure 11]

- (11)

where and are the unconditional mean and variance of respectively.

The simple expected excess return is a multiple of the nominal rate. Hence, a regression of on the nominal rate would actually yield a positive coefﬁcient equal to . However, the scaled expected return, is constant and equal to . The constant

is a function of the correlation between dividend growth innovations (the sum of the earnings growth and payout ratio innovations) with the pricing kernel. The predictability regressions typically run in the literature do not correspond to any of these two concepts, since they use log returns, . It is straightforward to show that up to second order terms, the expected log risk premium will be constant in this homoskedastic model. We also veriﬁed this result by simulation.

It turns out we can also solve for the conditional and unconditional volatility of equity returns and the risk premium, under the restrictions of equation (9).

- Corollary 2.2 If the companion matrix takes the form in equation (9) then the conditional volatility of the simple risk premium is a multiple of the gross short rate and given by:

var (12)

where . The unconditional variance of the simple risk premium is given by:

var var (13)

where and are the unconditional mean and variance of respectively, and the unconditional variance of the simple gross return var is given by:

Equation (12) shows two characteristics of the conditional volatility of equity returns. First, the conditional volatility of equity returns is related to the level of interest rate. Many studies have empirically documented a strong link between the conditional volatility of equity returns and interest rates (see for example, Glosten, Jagannathan and Runkle (1993)). However, note that this effect would disappear if we measure the return as or in logs. Second, the conditional variance is positively related to the conditional covariance between the pricing kernel and dividend growth, and to the conditional variance of dividend growth

.

The model with the restrictions in equation (9) will serve as the data generating process (DGP) under the null and will also help us interpret our empirical results. If the restrictions are not imposed, expected returns vary through time, but since the model is homoskedastic, the time-variation is likely to be modest in magnitude. Note there are no restrictions on .

What do the restrictions in equation (9) actually mean? Imposing the restrictions from equation (9) allows the conditional mean for log earnings growth and log payout ratio to be written as:

(14)

Note that log dividend growth . Hence under this economy, expected conditional dividend growth is equal to a constant plus the current short rate:

(15)

Normally, when interest rates move away from their unconditional mean the resulting change in discount rates and prices would induce predictable components in returns. The restriction on the companion form engineers an opposite cashﬂow effect that neutralizes the price-decrease induced by the interest rate change. This effect would also happen in a standard equilibrium Lucas (1978)-type economy. In an equilibrium setting the constant would be related to the degree of risk aversion of the representative agent.

## 2.2 Predictability Regressions The main regression we consider is:

(16) where

is the annualized -month excess return for the aggregate stock market, and is the excess 1 month return from time to . All returns are continuously compounded. Our Present Value Model implies that is constant and hence is zero for all . The error term follows a process under the null of no predictability because of overlapping observations. The instruments consist of the log dividend yield , the log earnings yield , and continuously compounded monthly short rate . The superscript indicates that the dividend (earnings) yields use dividends (earnings) summed over the past 12 months in their construction.

The log payout ratio is linearly related to the dividend yield and earnings yield

. The three predictive instruments are endogenous instruments in our Present Value Model. However, they should capture the predictability present under the null of the present value model, because there is a one-to-one (albeit non-linear) mapping between earnings yield, dividend yield and the short rate and our three state variables. One reason variables such as dividend yields may predict future returns more generally is the presence of price in the denominator. On the one hand, the presence of price on both sides of the regression may worsen small sample biases in the regressions (see Goetzmann and Jorion (1993)). On the other hand, since price reﬂects all information about future expected returns and cashﬂow growth rates, its presence may capture genuine predictability. If the Present Value Model we present is truth, price would not be necessary to capture time-variation in expected returns, and all information should be captured by the three state variables, or transformations of them.

In a globally integrated world, predictability is likely also to extend across borders. In Section 6, following Bekaert and Hodrick (1992), we consider cross-country regressions of the form:

(17)

where are -period annualized excess equity returns in local currency for country , and are k-period annualized exchange rate returns USD per foreign currency for foreign country

. The instruments in we consider are log dividend yields for the US, log earnings yields for the US, and one-month risk-free rates for the US, and the foreign country counterparts of these variables. Note that as we use continuously compounded returns .

The regressions in equations (16) and (17) can be estimated by OLS. We consider three estimators of the standard errors. First, OLS standard errors are appropriate if there is no serial correlation of the error term and the error terms are homoskedastic. These are the standard errors used by Lamont (1998) and we use them as a benchmark even when , in which case they will likely underestimate the true sampling error. Second, to account for the overlap in the residuals for and to capture potential heteroskedasticity in returns, we use a

heteroskedastic extension of Hansen and Hodrick (1980) standard errors. Using GMM the parameters in equation (16) have an asymptotic distribution (see Hodrick (1992))

where , , and is estimated by:

[Figure 12]

(18)

where

[Figure 13]

and . This estimator of is not guaranteed to be positive semi-deﬁnite. If it is not, we use a Newey-West (1987) estimate of with lags. We will refer to these standard errors as Robust Hansen-Hodrick (1980) standard errors.

Finally, we report what we will call Hodrick (1992) standard errors. This estimator exploits covariance stationarity to remove the overlapping nature of the error terms in the standard error computation. Instead of summing into the future to obtain an estimate of , Hodrick (1992) sums into the past:

[Figure 14]

(19)

where

In our Monte Carlo analysis we run a horse race between these three estimators. We ﬁnd Hodrick standard errors to be far superior, and most of our results will exclusively focus on t-statistics computed with the Hodrick standard errors. Readers not interested in the details of the Monte Carlo analysis can skip Section 3, although we feel that it contains some important results.

Apart from running univariate regressions, we are mindful of Richardson’s (1993) critique of predictability tests testing for only one particular horizon and we provide a number of joint tests across horizons. To test if the predictability coefﬁcients are statistically signiﬁcant across

horizons we set up the simultaneous equations:

.

(20)

Denote the vector of coefﬁcients . In practice, an estimate of is obtained by performing OLS on each equation. Appendix E details the construction of joint tests across horizons accomodating Hodrick standard errors.

When we consider predictability in multiple countries, we also provide joint tests of no predictability across countries and we estimate pooled coefﬁcients across countries. Such a pooled estimation mitigates the data mining problem plaguing US data and increases efﬁciency and power under the null of no predictability. Here we estimate the system:

(21)

for countries, subject to the restriction , but imposing no restrictions on across countries. We take = US, UK, France, Germany, Japan. The econometrics underlying the pooled estimation is detailed in Appendix F.

## 2.3 Data Description

Our data set consists of equity total return (price plus dividend) indices from Morgan Stanley Capital International (MSCI) for the US, Japan, UK, Germany and France. The short-term interest rates we use are 1 month EURO rates from Datastream. The sample period is from February 1975 to December 1999 for the US, UK, France and Germany and from January 1978 to December 1999 for Japan. MSCI provide dividend and earnings yields which use dividend and earnings summed over the past 12 months. Although this is restrictive, monthly earnings levels are impossible to use because they are dominated by seasonal components, given that most ﬁrms have a December-end calendar year.

Table (1) reports summary statistics of returns and instruments. The historical log equity premium is around 7.5% in the Anglo-Saxon countries, 6.9% in France and Germany and only 3.6% in Japan. Excess return volatility is over 18% in all countries, except for the US where it is only 15%. All three instruments - the log dividend yields , log earnings yield and short rates are highly persistent.

As Bekaert and Hodrick (1992) discuss, MSCI report price (capital appreciation) and total returns (including income). The total return is an estimate constructed from annualized dividends (summed over the previous twelve months). For some countries there is a discrepancy between the MSCI dividend yield and the implied annualized dividend yield constructed from the price and total return indices due to a differential tax treatment across the two series.3

[Figure 15]

3 For a discussion on how taxes are treated see MSCI Methodology and Index Policy, 1999. The MSCI dividend yield series and the implied annualized dividend yield from the price and total return indices are identical for the US and Japan, but differ for the UK, France and Germany.

We checked our results by re-constructing the total return using the MSCI dividend yield with the price return and found them to be unchanged.

# 3 Finite Sample Properties of Various Estimators

Our analysis of the small sample properties of the estimators proceeds in two steps. In the ﬁrst sub-section, we describe the results of a Monte Carlo analysis on returns, earnings yields, payout ratios and short rates that sufﬁces to mimic the regressions in Lamont (1998). Since Lamont (1998) used OLS standard errors to establish strong predictability results, it is important to ascertain that they survive small sample biases. In the second sub-section, we calibrate our Present Value Model of the price-earnings ratio and use it as the DGP for a Monte Carlo analysis. We solely use US data for the Monte Carlo analyses, but the results are so clearcut that there is little reason to suspect they would not extend to DGP’s calibrated using other country’s data. All Monte Carlo experiments use 5,000 replications.

## 3.1 An Empirical Trivariate Model

Lamont (1998) regresses excess stock returns on dividend yields, earnings yields and payout ratios, both univariately and bivariately since the three variables are totally linearly dependent. In some regressions, he adds the Treasury bill rate as a regressor, but does not ﬁnd it to be signiﬁcant. To examine the small sample performance of these regression tests, we investigate the following DGP:4

(22)

where is the 1 month excess return, denotes the annualized short rate, is the log earnings yield and is the log payout ratio. The errors IID , with correlation matrix .

We estimate this model on US MSCI data and use it to generate small samples of the same length (299) as the data sets used in the empirical work in the other sections. We then run regressions of the form:

[Figure 16]

- 4 We also examined a simpler DGP eliminating the short rate equation. The small sample properties of the

various estimates and the OLS biases were similar to what is reported here.

where are the cumulated and annualized -month ahead excess returns, and are predictor instruments. We set , 12 and 60. We take (dividend yield regression),

(earnings yield regression), (Lamont (1998)’s regression) and

(trivariate regression). To conserve space, we relegate the tables which contain the estimation results for the DGP, the simulation results on the coefﬁcients (to examine ﬁnite sample bias) and the simulation results on the t-statistics (to examine size distortions) in the above regressions to an Appendix, which is available upon request. Here we report the main results.

Since our instruments and returns are likely to be negatively correlated, regressions of excess returns on any of our instruments would suffer from the well-known persistent regressor bias (see Stambaugh (2000)), which will bias the regression coefﬁcients upward. This is most obvious for the yield instruments because of the presence of price in their denominator but short rate innovations and return innovations are also negatively correlated (correlation = -0.1107). However, in multivariate regressions, it is no longer possible to sign the bias and it may well be the case that the bias is less severe.

Our results reveal that the coefﬁcients on all regressors in virtually all regressions are upwardly biased. The univariate upward bias is larger for the earnings yield than for the dividend yield, as the earnings yield is slightly more persistent than the dividend yield, and it varies between 0.07 and 0.11 depending on horizon. In bivariate regressions, the earnings yield bias worsens but the dividend yield bias becomes tiny. When the short rate is added, the roles are reversed with large upward biases for the dividend yield coefﬁcient (between 0.07 and 0.16), virtually no bias for the earnings yield, and a substantial upward bias for the short rate coefﬁcient (between 0.09 and 0.17 depending on horizon).

Second, all three estimators show very small size distortions for . Hence, the use of the heteroskedasticity-correction, unnecessary given the homoskedastic DGP, does not lead to size distortions. For and , the OLS estimator, which fails to correct for serial correlation, not surprisingly performs very poorly. For example, for , more than 50% of the simulated samples yield OLS t-statistics higher than the 5% asymptotic critical value, with that number going up to 78% or more for . The heteroskedasticity-consistent Hansen-Hodrick standard error estimator behaves better for with empirical sizes for 5% tests varying between 12.6%, and 15.9% but for , the empirical sizes exceed 49%. In contrast, the Hodrick standard errors show virtually no size distortion for and , but are slightly conservative for . The worst size distortion occurs for the earnings yield coefﬁcient in the trivariate regression, where only 2.2% of the experiments yield t-stats higher than the 5% critical value.

Taken together, our Monte Carlo analysis of the different estimators overwhelmingly sug-

gests using Hodrick standard errors. It also suggests that the use of OLS or Hansen-Hodrick standard errors may frequently lead to the wrong inference, in particular their use may lead to the false rejection of the null of no predictability.

## 3.2 The Present Value Model Empirical Results

The DGP in the previous section ignores the fact that price appears both on the right hand side and the left hand side of the regression. Allowing for correlation in the innovations is helpful, but does not fully capture the relation between the left hand and right hand side variables. The Present Value Model presented in Section 2 under the parameter restrictions that ensure the absence of predictability (see Corollary 2.1), accomplishes the full endogeneity of price.

To perform the Monte Carlo analysis we have to estimate the parameters . We proceed in two steps. First, we estimate the VAR parameters . Second, we calibrate to ﬁt the observed equity premium in the data. We can do so because (See Observation 2.1) and we set the price of interest rate risk to zero, so that is a scalar. The latter assumption is motivated by the failure of most term structure studies to reject that prices of risk for interest rate factors are zero (see the discussion in Ang and Piazzesi (2000)).

We turn ﬁrst to the VAR parameter estimation, which is complicated by the fact that our MSCI data uses earnings and dividends summed up over the past year (we observe earnings growth rates and log payout ratios ) but our Present Value Model requires monthly earnings and dividends (we do not unobserve monthly growth rates and log payout ratios

).5 If denotes monthly earnings, then is related to by:

[Figure 17]

[Figure 18]

- (23)

In addition, if denotes monthly dividends then is related to by:

[Figure 19]

[Figure 20]

- (24)

[Figure 21]

5 We construct at a monthly frequency from earnings yields using .

Equations (23) and (24) show that the relation between monthly growth rates and payout ratios and their counterparts using earnings and dividends summed over the past year is highly nonlinear. In particular, the use of summing past earnings and dividends over the past twelve months will potentially induce very high autocorrelation up to 11 lags.

To estimate the VAR on we use Simulated Method of Moments (SMM) (Dufﬁe and Singleton (1993)). We use a two-step SMM procedure and impose a restricted companion form

where . The latter assumption is motivated by an analysis of a VAR on

, in which we fail to reject that no variables Granger-cause interest rates.6 In the ﬁrst step, we estimate the equation for on US EURO 1 month rates since we have monthly data on interest rates. In the second step, holding the parameters for ﬁxed, we estimate the remaining parameters in , and using the ﬁrst and second moments of and . We also use the moments in relating to and . The lag length is set at 12 since the ﬁrst 11 lags are affected by the autocorrelation induced by the non-linear ﬁlters in equations (23) and (24). We compute the weighting matrix using the data, so we need not iterate on the weighting matrix.

Table (2) reports our results. We report two estimations, an Alternative Model which is exactly identiﬁed, and the Null Model which is estimated subject to the restrictions ensuring constant expected returns in Corollary 2.1. Focusing ﬁrst on the Alternative Model, payout ratios are close to a random walk with no other signiﬁcant feedback coefﬁcients. Earnings growth on the other hand shows little persistence with the coefﬁcient on past earnings growth barely signiﬁcantly different from zero. However, high current payout ratios predict high future earnings growth, perhaps because they reﬂect permanent rather than transitory earnings. High short rates signiﬁcantly reduce future expected earnings growth. A 1% increase in interest rates leads to a 25 basis point decrease in expected earnings growth.

When we estimate the covariance parameters of the Null Model on the moments of the Alternative Model, we obtain a singular covariance matrix, as the correlation of and approaches -1. Therefore we hold the covariance matrix from the Alternative Model ﬁxed, and estimate and a restricted companion matrix using the ﬁrst the and cross-moments of the Alternative Model estimation. Using a test, we fail to reject the Null Model versus the Alternative Model with a p-value of 0.9252. The Null Model retains the important feedback from interest rates to earnings growth but makes the interest rate feedback to payout ratios much larger than before. The feedback from payout ratios to earnings growth rates remains intact as well, but the earnings growth rate is no longer persistent.

The estimation of the covariance matrix has two important features. First, the conditional volatility of innovations to is much more volatile than innovations to (0.0647 versus

[Figure 22]

6 This preliminary data analysis is reported in an unpublished Appendix table available upon request.

0.0233 from an unreported VAR on ). The ﬁlter in equations (23) and (24) smooths out some of the volatility in earnings growth by summing earnings over the past twelve months. This implies that equity returns will be more volatile using monthly earnings than summed annual earnings. Second, shocks to and are negatively correlated (-0.8496), which is true in the annual data as well. This might be due to the unusual smoothing that occurs in most corporate dividend policies. High temporary earnings are not paid out, so they decrease the payout ratio.

The constrained VAR ties down most of the parameters, but we still have to determine the price of risk for dividend growth. Figure (1) calibrates to the observed equity premium in the sample. The log risk premium is produced by simulation using 100,000 observations, while the simple risk premium is calculated using equation Corollary 2.1 (and checked by simulation). Setting , we match both the log and the simple risk premium. The annualized volatility of the log (simple) excess return corresponding to is 0.1367 (0.1387), which is slightly below the annualized volatility in the sample 0.1477 (0.1472). The main source of equity return volatility in the model is the volatility of payout ratios and earnings growth rates, since the risk premium is constant. In fact, the implied estimate of the conditional volatility of dividend growth is , which is 0.1368 annualized.

[Figure 23]

With the fully calibrated model we simulate 5000 samples of 299 observations to examine the empirical distribution of the various test statistics. We construct dividend yields and earnings yields using summed dividends and earnings over the past year as in the actual data:

[Figure 24]

[Figure 25]

[Figure 26]

[Figure 27]

- (25)

Focusing ﬁrst on the earnings yield:

[Figure 28]

[Figure 29]

[Figure 30]

[Figure 31]

[Figure 32]

[Figure 33]

- (26)

we note that can be evaluated using Proposition 2.1, and

[Figure 34]

[Figure 35]

[Figure 36]

[Figure 37]

[Figure 38]

- (27)

allowing us to evaluate each term in equation (26). The dividend yield can be written as:

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

- (28)

where and can be evaluated using equation (27). The dividend and earnings yields used in the regressions are and respectively.

In Table (3) we report the mean and standard deviation of the empirical distribution for the coefﬁcients in the various regressions we consider. First, in the dividend regression, we continue to ﬁnd substantial upward bias. Interestingly, the bias is not worse than what we ﬁnd for the DGP that does not explicitly consider the endogeneity of price in Section 3.1. Goetzmann and Jorion (1993) claim that considering price endogeneity explicitly considerably worsens the bias. However, their comparison is strained since in their DGP with explicit endogeneity, the dividend yield implicitly follows a random walk and Hodrick (1992) also ﬁnds stronger biases for a DGP in which dividend yields follow a random walk. Our results indicate that modeling the price endogeneity explicitly does not lead to larger biases.

Second, in the earnings regression we now ﬁnd a downward bias, instead of the upward bias we reported above. Why might this be the case? In our price-earnings model with constant expected returns, the variation in returns is dominated by variation in earnings growth rates. The price-earnings ratio is not constant but is completely driven by the payout ratio (see Proposition 2.1 and Corollary 2.1). This implies that the earnings yield, even when summed over 12 periods, is likely to be primarily negatively correlated with the payout ratio, but in the DGP (see Table

- (2)), earnings growth rates and payout ratios are highly negatively correlated, so that returns and earnings yield innovations end up being positively correlated, reversing the sign of the bias. This is not true for dividend yields, since the log dividend yield can be written as the sum of the log payout ratio (negatively correlated with the earnings growth rate and hence with return innovations) and the log earnings yield, and the ﬁrst effect dominates. Note that the small sample coefﬁcient in the dividend yield regression has the same positive sign that the dividend yield predictability literature ﬁnds (Fama and French (1988) and Hodrick (1992)), while the negative small sample coefﬁcient on the earnings yield is what Lamont (1998) ﬁnds.

Third, in the bivariate regressions, the univariate biases are accentuated, with the bias on the dividend yield coefﬁcient reaching 0.19 for . The biases decrease slightly with the horizon. Lamont (1998) ﬁnds positive signs on the dividend yield and negative signs on the earnings yield in a bivariate regression. Our biases are exactly the same sign as his result. Finally, in the trivariate regression, the biases for the earnings and dividend yield coefﬁcients become larger still in absolute magnitude (0.24 for the dividend yield coefﬁcient; -0.11 for the earnings yield coefﬁcient). However, the bias on the short rate coefﬁcient is negligible.

In Table (4) we examine the size properties of signiﬁcance tests. We report empirical sizes for tests of size 10% and of size 5%, but we focus our discussion on the 5% tests. The price endogeneity also alters the absolute performance of the various test statistics, but not their

relative performance. In particular, at , the univariate regressions display negligible size distortions, but for the bivariate and trivariate regressions, all tests slightly over-reject at asymptotic critical values and the empirical sizes exceed the nominal sizes. The worst distortion occurs for the dividend yield coefﬁcient in the trivariate regression, with the nominal size being 8.6% for the OLS estimator, and 8.9% for the robust Hansen-Hodrick and Hodrick estimators (which coincide for ). For longer horizons, the performance of the OLS estimator rapidly deteriorates with the empirical size exceeding 54% for a 5% test in the dividend regression and exceeding 72% in all other regressions at . Accounting for the overlap in the error terms using Hansen-Hodrick standard errors improves the small sample performance but not enough to yield a reliable test. The empirical size for a 5% test at is at least 39.1% in the case of the dividend regression.

Table (4) shows that Hodrick standard errors are far superior to OLS and Hansen-Hodrick standard errors. For , there is negligible size distortion for the univariate regressions, whereas for the bivariate and trivariate regressions, the size distortion is at most 4.9% for the dividend yield coefﬁcient in the trivariate regression (a 9.9% empirical size). Note that the Hodrick test now also over-rejects. For , the size distortions actually become smaller, with the worst size distortion occurring again for the dividend yield coefﬁcient in the trivariate regression (a 7.9% empirical size for the 5% test). For the earnings yield regression, the Hodrick test is conservative with an empirical size of 3.6%. In sum, the Hodrick standard errors display overall far superior small sample properties, and using the asymptotic p-values is unlikely to dramatically affect statistical inference. For that reason, we will report the Hodrick standard errors for all of our empirical tests.

# 4 Predictability in US Excess Stock Returns

Table (5) contains our main results regarding the predictability of US excess stock returns. To allow comparison with Lamont (1998)’s article, we report univariate and bivariate yield regressions in addition to our main trivariate speciﬁcation. We report t-statistics in parentheses based on Hodrick standard errors. For the full sample and looking over three horizons, the yield regressions produce only one signiﬁcant coefﬁcient, the dividend yield. This appears to be a signiﬁcant predictor of excess stock returns in the bivariate regression, but its sign is negative, not positive! Lamont on the other hand ﬁnds positive coefﬁcients for both yield variables in univariate regressions, but a positive coefﬁcient on dividend yields and a negative coefﬁcient on the earnings yield in the bivariate regression. His main point is that the predictive power of the dividend yield stems from the role of dividends in capturing the permanent component of prices, whereas the negative coefﬁcient on the earnings yield is due to earnings being a good

measure of business conditions which captures counter-cyclical risk aversion. According to Lamont there is information in earnings and dividends over and above price. Unfortunately, our results appear rather inconsistent with this story. Only for do the regression coefﬁcients have the sign predicted by Lamont’s analysis, but for long horizons Lamont ﬁnds that only price mattered. In the trivariate regression, the same sign pattern appears for the yield variables: negative on dividends and positive on earnings which reverses for .

Note that accounting for biases would not help recover the Lamont pattern. In the univariate regressions, the bias-corrected dividend yield coefﬁcient would be even more negative since the bias is positive, and the negative bias in the earnings yield regression is too small to reverse the sign of the coefﬁcients. For the bivariate and trivariate regressions, accounting for biases would make the pattern we observe (and which is opposite to what Lamont ﬁnds) even more striking.

Figure (2) shows the pattern over different horizons more clearly for both the univariate and bivariate regressions (the inclusion of the interest rate does not change the pattern very much). In both univariate regressions, the coefﬁcients on the dividend or earnings yield turn increasingly more negative until around the 30 month horizon after which they start to increase without becoming positive. In the bivariate regression, we clearly see how the “Lamont-pattern” of positive dividend yield coefﬁcients and negative earnings coefﬁcients requires setting equal to 50 months or higher. The right hand side of the three panels shows the corresponding t-statistics for OLS, Robust Hansen-Hodrick and Hodrick standard errors. Given the general lack of statistical signiﬁcance, it is clearly pointless to try and interpret the sign changes. Interestingly, if we had relied on the OLS or Robust Hansen-Hodrick standard errors, we would have concluded there was signiﬁcant predictive power in the dividend yield variable, which again drives home the importance of the simulation experiments in Section 3.

Goyal and Welch (1999) point out that the dividend yield predictability is not robust to the addition of the last decade of high returns coinciding with low dividend yields and is actually highly unstable in general. Therefore, two additional panels in Table (5) report results for shorter sub-samples eliminating either the last 5 or the last 8 years in the sample. Whereas the sign of the coefﬁcients now better corresponds to what Lamont (1998) ﬁnds, statistical signiﬁcance is still lacking. Lettau and Ludvigson (2001) also ﬁnd that the Lamont-pattern does not hold with late 1990’s data with a quarterly sampling frequency.

The results described so far are pretty bleak if ﬁnding predictability were the objective of this study. However, there is yet another regressor in our fundamental regression, the short rate. Whatever the sample period we use, the short rate enters signiﬁcantly at the 99% level in the regression and its impact on the equity premium is remarkably robust in terms of magnitude across the various sample periods. A 1% increase in the annualized short rate decreases the equity premium by about 3.7%. The predictive power of the short rate dissipates

quickly for longer horizons. The coefﬁcient slowly becomes less negative and eventually even slightly positive.

We also conduct joint tests across regressors. Joint tests across the and regressors in the Lamont regression yield p-values of 0.2294, 0.3760 and 0.1788 for horizons , 12 and 60 respectively. Joint tests across , and in the trivariate regression yield p-values of 0.0139, 0.3723 and 0.0985 for horizons . In this regression for , the dividend yield and earnings yield are also individually signiﬁcant at the 5% level.

Finally, following the lead of Richardson (1993), Table (6) reports tests of predictability over three horizons, , 12 and 60, simultaneously. The table also lists results for four other countries, which will be discussed in the following section. If we now focus on the ﬁrst column, the US results, we see that there is only strong evidence for yield predictability, if we consider the joint predictability of earnings yields and dividend yields in the trivariate speciﬁcation. Despite the short-lived nature of the predictable patterns, the short rate still signiﬁcantly (at the

- 5% level) predicts excess returns at the one month, 12 month and 5 year horizons.

# 5 Predictability of Excess Stock Returns in Five Countries

Our previous results suggest that the predictability patterns formerly found in US data appear not to be robust to the addition of the last few years and that statistical signiﬁcance only occurs when the short rate is used as a predictor. It is conceivable that the lack of predictive power is simply a small sample phenomenon, due to the very special nature of the last decade for the US stock market. It is equally probable that the previous results of strong predictability and interesting predictability patterns are a statistical ﬂuke. International evidence should help us sort out these two interpretations of the data. If we cannot conﬁrm the previous predictability patterns for any countries, and if yield variables do not appear to predict stock returns in other counties, it seems likely that data mining and other statistical problems have led researchers in the US astray regarding the predictive power of the yield variables. We can also increase or decrease our conﬁdence in the short rate as a robust predictor of equity returns using international stock return data. Finally, pooled estimation across countries can lead to powerful evidence on the robustness and magnitude of predictability patterns across countries.

We begin by summarizing the patterns in univariate and bivariate yield regressions. Figure

- (3) displays the dividend yield coefﬁcients and their t-statistics using Hodrick standard errors The UK coefﬁcient pattern is strikingly similar to that of the US but, as in the US, not a single t-statistic reaches higher than 2.00 and it is not surprising that the joint tests for , 12 and 60 in Table (6) fail to reject the null of no predictability. The coefﬁcient patterns in the three other countries are more akin to these prevalent in the US in earlier samples, in that the coefﬁcients

increase with horizon, but in both France and Germany they start out negative. In Japan, the individual coefﬁcient for is borderline signiﬁcant in the univariate regression and the joint test across horizons in Table (6) rejects at the 10% level.

In Figure (4), we repeat the same graphs for the earnings yield regression. The earnings yield predictability coefﬁcients again are similar for the US and the UK, following a reverse J-pattern. For France and Germany they have a U-shaped pattern, whereas they increase monotonically with the horizon for Japan. Individual signiﬁcance again only occurs for certain horizons in Japan, but nowhere else. Joint tests in Table (6) fail to reject the null of no predictability in France and Germany but there is a borderline rejection in Japan (at the 5.7% level) and a rejection at the 5% level in the UK. Inspection of the UK coefﬁcients in Figure (4) reveals that the

, 12, 60 choice very fortunately avoids the lowest spot in the t-statistics curve and might somewhat overstate the true predictability. We conclude that the univariate yield predictability patterns are not terribly robust across countries and not very signiﬁcant statistically.

Do we observe the Lamont pattern of positive dividend yield and negative earnings yield coefﬁcients in international data? Figure (5) simply shows the coefﬁcient patterns. Again (not reported), the individual t-statistics using Hodrick standard errors barely ever reach signiﬁcance. Two countries, Japan and France, show a pattern somewhat reminiscent of the Lamont ﬁndings, with negative coefﬁcients for the earnings variable and positive ones for the dividend yield at short horizons. In France, the coefﬁcients further diverge as the horizon lengthens, whereas in Japan they converge. The UK pattern of the coefﬁcients is similar to that in France but the initial earnings yield coefﬁcient is actually slightly positive. In Germany, the sign pattern and its evolution over horizons matches the one we found for the US, with positive (negative) earnings yield (dividend yield) coefﬁcients eventually switching sign, but the switch occurs much earlier than in the US. Joint tests across horizons reveal no signiﬁcant rejections of the null of no predictability, except in the case of Japan, where earnings and dividend yields jointly predict stock returns at the 5% level (see Table (6)). However, this may be due to a multicollinearity problem in the regression for Japan (see below).

The coefﬁcient patterns for the yield variables that we observe for the bivariate regressions qualitatively persist for the trivariate regressions (except for Japan) and hence we do not show

- them in a ﬁgure. However, the t-statistics are generally somewhat larger, resulting in joint rejections of the null of no predictive power for the yield variables in three countries, the US, the UK and Japan at the 1% level. So the yield variables appear to have some predictive power when considered together and over three horizons simultaneously. However, the pattern in coefﬁcients we see is very different across countries and differs from what Lamont found, except in Japan.7

[Figure 53]

7 For Japan, we observe a Lamont pattern at short horizons (less than 15 months) but at horizons longer than 15 months the earnings yield coefﬁcients become positive. The dividend yield coefﬁcients are less than the earnings

Figure (6) displays the coefﬁcient patterns for the annualized short rate and its associated t-statistics in the trivariate regression. Strikingly, this coefﬁcient pattern is much more robust across countries and a similar shape for the coefﬁcient patterns appear for univariate regressions (not reported). For all countries, the one-month coefﬁcient is negative between -3.73 for the US and -0.97 for Japan. For 4 of the 5 countries, the coefﬁcient increases monotonically with horizon, leveling off at around 0.55 for the US, France, and Germany and at slightly less than zero for the UK (-.55). In Japan, the coefﬁcient never reaches zero, but the horizon dependence is not monotonically increasing. The t-statistics are generally larger in absolute magnitude for short horizons with the exception again being Japan. At the one-month horizon the short rate coefﬁcients are statistically signiﬁcant only for the US and UK. When we pool across horizons in Table (6), only the US short rate retains signiﬁcant predictive power at the 5% level, which is not surprising given the pattern of the coefﬁcients and t-statistics in Figure (6). What is surprising is the very high p-value for Japan. Inspection of the graph reveals than the joint test happens to select two ’s out of only a small set of ’s that yield coefﬁcients close to zero.

We conclude that the international evidence on predictability does not support Lamont’s ﬁndings regarding the predictability of earnings and dividend yields. There is only weak evidence in favor of it in three countries, and the international data do not reveal a consistent, interpretable data pattern. However, the short rate robustly predicts excess stock returns, but its effect is limited to the short forecasting horizon (mostly one month). The short rate coefﬁcient is not signiﬁcantly different from zero for all countries. Table (6) reports joint tests of predictability for the three coefﬁcients. The null of no predictability is rejected at the 10% level in Germany, and at the 5% level in the US and UK. It is also rejected at the 1% level in Japan which is surprising given the lack of signiﬁcance of the individual coefﬁcients. However, this is mainly due to multicolinearity in the regressions, and a near-singular covariance matrix of the regressor coefﬁcients.

One way to come to more clear-cut conclusions regarding the magnitudes and signiﬁcance of the coefﬁcients is to pool the estimation across countries. Under the null of no predictability, the pooled estimation should enhance efﬁciency considerably given that the correlation of returns across countries is not very high. Unfortunately, we have to exclude Japan, because of the considerable difference in data coverage both in terms of sample size and in terms of variables (we use levels of earnings yields rather than log earnings yields, because of the presence of negative earnings in the Japanese series). Table (7) reports pooled predictability coefﬁcients, t-statistics and joint tests. We also report a test of the over-identifying restrictions, described

[Figure 54]

yield coefﬁcients between horizons 20 and 40 months. At long horizons (40-60 months) both dividend and earnings yields are positive, with the dividend yield coefﬁcients greater than the earnings yield coefﬁcients. This ﬁgure is available upon request.

in Appendix F. For all of our speciﬁcations, this test fails to reject the restrictions imposed by equal coefﬁcients across countries. In the Lamont regressions with only the yield variables, we fail to ﬁnd statistical signiﬁcance for the yield variables, both when tested individually and jointly. The coefﬁcients get closer to signiﬁcant levels at longer horizons. In terms of sign at , the dominant pattern appears to be negative dividend yield coefﬁcients and positive earnings yield coefﬁcients, a pattern opposite to that found by Lamont (1998).

In the trivariate system, both the dividend yield and earnings yield coefﬁcients are positive for , but the earnings yield coefﬁcient turns negative at longer horizons. Consequently, the Lamont pattern again fails to show. Moreover, none of the coefﬁcients is individually signiﬁcant, although the t-statistics increase with horizon. A joint test on the yield variables also fails to reject the null of zero coefﬁcients. On the other hand, the short rate coefﬁcient is -1.7334 at the one month horizon and signiﬁcant at the 5% level. The coefﬁcient increases to -0.34 at

but loses statistical signiﬁcance. Joint tests across the three variables fail to reject the null of no predictability for all three horizons at the 5% level, but the test would reject at the 10% level for . We conclude that the only robust and signiﬁcant predictor of excess stock returns in 5 countries appears to be the short rate.

# 6 Cross-Country Predictability

The previous discussion implicitly considered our 5 countries to be segmented markets and did not allow the possibility of cross-country inﬂuences. However, in an integrated market, global discount rates should price equity returns on all markets, and we may ﬁnd common components in the predictable components of returns. To investigate this, we extend our trivariate regression to a 6 variable regression, looking at pairs of countries. This set-up is an extension of the regressions run by Bekaert and Hodrick (1992), who regressed equity and foreign exchange returns on the dividend yields in two countries and the forward premium. Since the forward premium is the interest differential through Covered Interest Parity, our regression frees up an implicit constraint on the interest rate coefﬁcients in the Bekaert and Hodrick regressions. Like Bekaert and Hodrick, we also investigate the predictability of foreign exchange returns. Our main contribution here is to examine the added role earnings yields may play.

Table (8) reports the main results for the predictability of equity excess returns by local and US instruments. A number of striking results emerge. First, there is not a single signiﬁcant coefﬁcient for the 12 and 60-month horizons, conﬁrming once again that predictability is not a long-horizon phenomenon. Second, the only signiﬁcant coefﬁcients we report are US dividend yields signiﬁcantly predicting returns in France at the 5% level and in Germany at the 1% level. Hence, the strongest predictability pattern is a cross-country effect. The sign of the coefﬁcient

is negative as it is in the other countries. Moreover, the US earnings yield consistently carries a positive sign but fails to reach statistical signiﬁcance. The local yield variables mostly have positive but insigniﬁcant coefﬁcients. Third, the local short rate is no longer signiﬁcant and increases in value, relative to its value in the domestic trivariate regression we studied before. For France and Germany, it even becomes positive. However, the US short rate enters with a negative sign in every regression and the magnitude of the coefﬁcient is large, varying between -2.00 in Japan to -4.17 in Germany. Although the coefﬁcients are never signiﬁcant at the 5% level, the t-statistics are all 1.00 or larger.

These coefﬁcient patterns suggest that cross-country predictability may be stronger than domestic predictability. This may be the case in an integrated world where perhaps shocks affecting global discount rates are best reﬂected in the instruments of the dominant stock market, the US. To examine this further, Table (9) reports p-values from a series of joint tests of predictability. The ﬁrst set, labeled with US as ”Base,” concerns the regressions of Table (8). The base predictability column contains a test of the null of zero coefﬁcients for the base instrument, in this case, the US instruments. The local predictability column reports p-values for tests of predictability using only the local instruments. This column is likely to conﬁrm the results of the trivariate regressions we reported earlier. The US instruments jointly only signiﬁcantly predict German excess returns. In the other sub-panels, we make other countries the base country. For example, in the second set we look at excess returns in the US, France, Germany and Japan and our predictor instruments comprise local and UK instruments.

We ﬁnd a number of interesting signiﬁcant predictability patterns in Table (9). First, no foreign country instruments predict US returns. However, in the presence of foreign instruments which have no predictive power, there is still signiﬁcant predictive power of US domestic instruments, in particular the short rate, for US excess returns. Second, we ﬁnd only two significant base country predictors: US instruments predict German returns, and German instruments predict Japanese returns. Finally, the local predictability results conﬁrm the rejections we found for the US in Table (6), no matter which foreign instruments are included in the regression. For the UK, we no longer reject, which may reﬂect a loss of power due to the introduction of three new regressors. For Japan, we also no longer reject, which simply indicates that the inclusion of the foreign instruments resolved the singularity problem we faced with the regular estimation.

The results in Table (9) may be weak because of the inclusion of too many highly correlated regressors. Therefore, Table (10) reports predictability results using only US instruments, including a pooled estimation. The results are indeed stronger than what we reported in Table (8). First, long-horizon predictability remains rather weak to non-existent. Second, the yield variables retain their sign patterns (a reverse Lamont pattern) and are now signiﬁcant in both France and Germany. The US short rate consistently has a negative sign and is now signiﬁcant

in the UK and Germany. Overall, the US instruments predict excess equity returns in these countries better than the local instruments! When we pool the estimation across countries, we ﬁnd very strong results, with all three coefﬁcients being signiﬁcant at the 1% level.8 A 1% increase in the US dividend yield reduces the equity premium in other countries by about 50 basis points, an increase in the earnings yield increases international risk premiums by about 65 basis points, whereas an increase in the US short rate of 1% decreases the equity premium by almost 3.5%. It may be that US factors dominate global discount rates and that this leads to the observed pattern, but it seems hard to come up with an international asset-pricing model that would explain these predictability patterns.

Such an international model would also have to capture predictability patterns in exchange rate returns. We measure the exchange rate return for a US based investor, using the logarithmic exchange rate change (in dollars per foreign currency) plus the foreign-US interest rate differential. This return is the topic of the vast literature on the Unbiasedness Hypothesis in international ﬁnance. If no instruments predict this return, the interest differential or forward premium is an unbiased predictor of future exchange rate changes. Whereas earlier work ﬁnds very strong rejections of this hypothesis, recent tests yield weaker results (see Bekaert and Hodrick (2001)). In Table (11) we report regressions of foreign exchange returns on the US instruments and the instruments of the currency’s country. Since France and Germany now share a common currency as of 1 January, 1999, and were included in the EMS during the 1990’s we include only the US Dollar-Deutsch Mark exchange rate.

In the Unbiasedness literature it is customary to regress foreign exchange returns or exchange rate changes onto the forward premium or interest differential, an exercise which typically results in strong negative slope coefﬁcients. In our framework, this would correspond to ﬁnding negative coefﬁcients on the US interest rate and positive ones on the foreign interest rate. This pattern is only valid for the pound; in the other countries the US interest rate enters with a positive sign and is not statistically signiﬁcantly different from zero. In the UK both interest variables are signiﬁcantly different from zero, whereas the only other signiﬁcant interest rate coefﬁcient is the Japanese interest rate for the yen equation. Perhaps surprisingly, some of the yield variables do seem to have predictive power for foreign exchange returns, but no clear pattern emerges. For example, the US earnings yield is only signiﬁcant in the pound equation, and

- then only for , whereas the dividend yield is signiﬁcant for the Deutsche Mark equation at both and . Local instruments are also signiﬁcant. For example, UK dividend yields predict pound foreign exchange returns, and German dividend yields predict Mark foreign exchange rates. Perhaps such complex patterns are not surprising in a globally integrated world. An international pricing model will typically require the exchange rate change to be the

[Figure 55]

8 We pool UK, French and German returns and exclude Japan because of its smaller sample size.

difference of the two pricing kernels in the two countries, so that factors driving equity prices in both countries may affect exchange rates as well.

To obtain more powerful tests, we also conduct a number of joint tests in the bottom panel of Table (11) across horizons , 12 and 60 months. For all of our tests, we ﬁnd strong rejections of the null of no predictability for the Japanese foreign exchange returns, but these are hard to interpret because of the collinearity problems that plague the covariance matrix in this case. Therefore we focus our discussion on the pound and Mark returns. First, we contrast the predictive power of local versus US instruments. We fail to ﬁnd signiﬁcant rejections of the null of no predictability in both cases, but local instruments seem to have more predictive power than US instruments. Second, we contrast the predictive power of the interest rate instruments, with the predictive power of the yield variables. Surprisingly, the yield variables are signiﬁcant at the 5% level in the pound return regression and at the 1% level in the Mark return regression, but the interest rate variables are not signiﬁcant. Whereas the literature has typically focused on interest rate instruments to predict returns, they do not appear strong predictors, relative to yield variables. Third, joint tests strongly reject the null of no predictability in both regressions. We conclude that for foreign exchange predictability returns, there is strong predictability by yield variables but not by interest rates, the instruments used in the standard literature.

# 7 Conclusions

The predictable components in equity returns uncovered in empirical work over the last 20 years have had a dramatic effect on ﬁnance research. Theoretical research on equilibrium models uses the predictability evidence as a stylized fact to be matched. The partial equilibrium dynamic asset allocation literature investigates the impact of the predictability on hedging demands. Much of the focus has been on the predictive prowess of the dividend yield, especially at long horizons, but Lamont (1998) shows that earnings yields have independent predictive power. In this article, we pose the question whether this predictability is real. After carefully accounting for small sample properties of standard tests, our answer is surprising but important. We show that the standard predictability patterns are not statistically signiﬁcant, not robust across countries or sample periods and fail to conform to the economic interpretation given by Lamont (1998). Moreover, there is no evidence of long-horizon predictability in any of the 5 countries we examine. In this sense, the predictability that has been the focus of most recent ﬁnance research is simply not there.

Nevertheless, we do ﬁnd that stock returns are predictable, calling for a re-focus of the predictability debate in three directions. First, our results suggest that predictability is mainly a short-horizon, not a long-horizon, phenomenon. Second, the strongest predictability comes

from the short rate and not from yield variables with price in the denominator. The result that the short rate predicts equity returns goes back to at least Fama and Schwert (1977), but somehow recent research has failed to address what might account for this predictability and has mostly focused on dividend yield predictability. Third, there are tantalizing cross-country predictability patterns that appear stronger than domestic predictability patterns. The emergence of a globally integrated capital market over the last 20 years should refocus research towards determinants of global discount rates.

We hope that our results will, in the short run, affect the asset allocation literature, which often has taken predictability of the dividend yield variable as given, and in the longer run, will stimulate research on theoretical models that might explain the predictability patterns we demonstrate, particularly short rate predictability at short horizons and across countries.

# Appendix

# A Proof of Proposition 2.1

From the Dividend Discount Model we can write:

[Figure 56]

[Figure 57]

[Figure 58]

(A-1)

where and . We claim that:

(A-2) which we show by induction.

The initial conditions are given by:

[Figure 59]

[Figure 60]

(A-3) where

[Figure 61]

and

To prove the recursive relation, assume this relation holds for . Then using iterative expectations:

[Figure 62]

[Figure 63]

(A-4) where

[Figure 64]

and

Hence the price-earnings ratio is given by:

(A-5)

# B Proof of Observation 2.1

We would like pricing kernel variability with earnings growth and log payout to be the same if were to use dividend growth. Denote . In particular, we would like cov in a system with state variables as cov in our system with state variables . We note that

[Figure 65]

cov

Denoting as the 2 2 covariance matrix under the dividend growth system, and as the 2 1 vector of prices of risk under this system, then

cov Imposing equality between these two expressions we have the following relation:

(B-1)

where from our three-factor earnings growth and log payout system and from a dividend growth system. Note that

cov and

cov Hence we can re-write equation (B-1) as:

(B-2) This relation is satisﬁed if .

# C Proof of Corollary 2.1

Lemma C.1 Under the restriction for in equation (9) the coefﬁcients . Proof: From the initial condition for in equation (7) we have:

We can verify that in the recursive relation in equation (6) by direct substitution. Using equation (1) we can write:

[Figure 66]

[Figure 67]

- (C-1)

noting that from Lemma C.1. The term is given by:

[Figure 68]

[Figure 69]

- (C-2)

where we substitute and is given by:

[Figure 70]

which is zero if . The unconditional risk premium is:

- (C-3)

Hence the expected simple total return is:

- (C-4)

where . The simple risk premium is given by:

- (C-5)

(C-6) where and are the unconditional mean and variance of respectively.

[Figure 71]

Note that we can also write the expected simple total return as:

[Figure 72]

- (C-7)

where is given by:

Equating equation (C-4) and the expression for in equation (C-7) allows us to obtain an expression for :

[Figure 73]

[Figure 74]

or substituting for :

[Figure 75]

Hence

[Figure 76]

- (C-8)

# D Proof of Corollary 2.2

The conditional squared simple total return is given by:

[Figure 77]

[Figure 78]

- (D-1)

where

- (D-2)

where is given by equation (C-2),

- (D-3)

where is given by equation (C-8) and

- (D-4)

Hence the conditional expectation of the squared simple total return is:

[Figure 79]

[Figure 80]

- (D-5)

where the last expression results from substituting in the conditional simple total return given in equation (C-7). We can write the conditional variance of the simple total return as:

var

(D-6) where . This is also the conditional variance of the simple risk premium. Note that

is the conditional variance of dividend growth but expressed in earnings growth and log payout ratios.

To look at unconditional variances we use the formula:

var var var The ﬁrst term is given by:

var (D-7) where and are the unconditional mean and variance of respectively. The second term is given by:

var var

(D-8) Combining equations (D-7) and (D-8) we have:

var (D-9) The unconditional variance of the simple risk premium is:

var var cov var

var var (D-10) where var is given in equation (D-9) and var .

# E Testing Predictability Across Horizons

The moment conditions for the system in equation (20) are:

. . (E-1)

where , a vector and . From standard GMM with , and

[Figure 81]

- (E-2)

The Hodrick (1992) estimate of is given by:

[Figure 82]

- (E-3)

where is a matrix where is given by , and , , is:

since under the null of no predictability the one-step ahead errors are uncorrelated and

. Denoting , , an estimate of is given by:

(E-4)

(E-5) To test the hypothesis we use the Newey (1985) test:

[Figure 83]

rank (E-6) with .

# F Testing Predictability Pooling Cross-Sectional Information

Let the dimension of be so there will be a total of regressors, including the constant terms for each of countries. In equation (21) denote the free parameters , and the unrestricted parameters stacked by each equation . We can estimate the system in equation (21) subject to the restriction that , where C is a matrix of the form:

.

(F-1)

where is a vector of zeros, is a matrix of zeros, and is a rank identity matrix. Denote

... (F-2)

Then the system can be written as:

(F-3)

subject to . To write in compact notation let , , . Then the compact system can be written as:

subject to (F-4) A consistent estimate of is given by:

(F-5) with . This gives us an estimate of .

The moment conditions of the system in equation (F-3) are:

- (F-6)

By standard GMM has distribution

[Figure 84]

- (F-7)

with

[Figure 85]

- (F-8)

and

- (F-9)

The Hodrick (1992) estimate of is given by:

[Figure 86]

- (F-10)

where ( ) is

- (F-11)

Under the null hypothesis of no predictability where are the 1-step ahead serially uncorrelated errors. This is the SUR equivalent of the Hodrick (1992) estimate for univariate OLS regressions.

An estimate of is given by:

with

[Figure 87]

[Figure 88]

[Figure 89]

(F-12)

... (F-13)

The estimate has distribution

[Figure 90]

- (F-14)

There are free parameters in with moment conditions. This gives over-identifying restrictions. The Hansen (1982) J-test of over-identifying restrictions is given by:

- (F-15)

with

[Figure 91]

- (F-16)

# References

- [1] Ang, A., and J. Liu, 2001, “A General Afﬁne Earnings Valuation Model,” forthcoming Review of Accounting Studies.
- [2] Ang, A., and M. Piazzesi, 2000, “A No-Arbitrage Vector Autoregression of Term Structure Dynamics with Macroeconomic and Latent Variables,” working paper.
- [3] Bekaert, G., and S. Grenadier, 2000, “Predictability of Bond and Stock Returns in Afﬁne Models,” working paper.
- [4] Bekaert, G., and R. J. Hodrick, 2001, “Expectations Hypothesis Tests,” forthcoming Journal of Finance.
- [5] Bekaert, G., and R. J. Hodrick, 1992, “Characterizing Predictable Components in Excess Returns on Equity and Foreign Exchange Markets,” The Journal of Finance, 47, 2, 467-509.
- [6] Bollerslev, T., and R. J. Hodrick, 1996, “Financial Market Efﬁciency Tests,” in Pesaran, M. H., and M. R. Wickens, eds, 1996, The Handbook of Applied Econometrics Vol 1, Macroeconomics, Blackwell, 415-458.
- [7] Bossaerts, P., and P. Hillion, 1999, “Implementing Statistical Criteria to Select Return Forecasting Models: What do we Learn?,” Review of Financial Studies, 12, 405-428.
- [8] Boudoukh, J., and M. Richardson, 1993, “The Statistics of Long-Horizon Regressions,” Mathematical Finance, 4, 2, 103-120.
- [9] Breen, W., L. R. Glosten and R. Jagannathan, 1989, “Economic Signiﬁcance of Predictable Variations in Stock Index Returns,” Journal of Finance, 44, 5, 1177-89.
- [10] Campbell, J. Y., 1987, “Stock Returns and the Term Structure,” Journal of Financial Economics, 18, 373-399.
- [11] Campbell, J. Y., and J. H. Cochrane, 1999, “By Force of Habit: A Consumption-Based Explanation of Aggregate Stock Market Behavior,” Journal of Political Economy, 107, 205-251.
- [12] Campbell, J. Y., and R. J. Shiller, 1988, “Stock Prices, Earnings and Expected Dividends,” Journal of Finance, 43, 3, 661-676.
- [13] Campbell, J. Y., and R. J. Shiller, 1989, “The Dividend-Price Ratio and Expectations of Future Dividends and Discount Factors,” Review of Financial Studies, 1, 3, 195-228.
- [14] Cutler, D. M., J. M. Poterba, and L. H. Summers, 1989, “What Moves Stock Prices?” Journal of Portfolio Management, 15, 3, 4-12.
- [15] Dufﬁe, D. and R. Kan, 1996, “A Yield-Factor Model of Interest Rates,” Mathematical Finance, 6, 4, 379-406.
- [16] Dufﬁe, D., and K. J. Singleton, 1993, “Simulated Moments Estimation of Markov Models of Asset Prices,” Econometrica, 61, 4, 929-952.
- [17] Fama, E., and G. W. Schwert, 1977, “Asset Returns and Inﬂation,” Journal of Financial Economics, 5, 115146.
- [18] Fama, E., and F. French, 1988, “Dividend Yields and Expected Stock Returns,” Journal of Financial Economics, 22, 3-26.
- [19] Ferson, W. E., and C. R. Harvey, 1993, “The Risk and Predictability of International Equity Returns,” Review of Financial Studies, 6, 527-566.
- [20] Foster, F. D., T. Smith, and R. E. Whaley, 1997, “Assessing Goodness-of-Fit of Asset Pricing Models: The Distribution of the Maximal R-Squared,” Journal of Finance, 52, 2, 591-607.
- [21] Glosten, L. R., R. Jagannathan, and D. E. Runkle, 1993, “On the Relation between the Expected Value and the Volatility of the Nominal Excess Return on Stocks,” Journal of Finance, 48, 5, 1779-1801.
- [22] Goetzmann, W. N., and P. Jorion, 1993, “Testing the Predictive Power of Dividend Yields,” Journal of Finance, 48, 2, 663-679.
- [23] Goetzmann, W. N., and P. Jorion, 1995, “A Longer Look at Dividend Yields,” Journal of Business, 68, 483-508.
- [24] Goyal, A., and I. Welch, 1999, “The Myth of Predictability: Does the Dividend Yield Forecast the Equity Premium?” working paper.

- [25] Hansen, L., 1982, “Large Sample Properties of Generalized Method of Moments Estimators,” Econometrica, 50, 1029-1054.
- [26] Hansen, L., and R. Hodrick, 1980, “Forward Exchange Rates as Optimal Predictors of Future Spot Rates: An Econometric Analysis,” Journal of Political Economy, 88, 829-853.
- [27] Harrison, J. M., and D. M. Kreps, 1979, “Martingales and Arbitrage in Multiperiod Securities Markets,” Journal of Economic Theory, 2, 3, 381-408.
- [28] Hodrick, R., 1992, “Dividend Yields and Expected Stock Returns: Alternative Procedures for Inference and Measurement,” Review of Financial Studies, 5, 3, 357-386.
- [29] Kandel, S., and R. F. Stambaugh, 1990, “Expectations and Volatility of Consumption and Asset Returns,” Review of Financial Studies, 3, 2, 207-32.
- [30] Kirby, C., 1997, “Measuring the Predictable Variation in Stock and Bond Returns,” Review of Financial Studies, 10, 3, 579-630.
- [31] Lamont, O., 1998, “Earnings and Expected Returns,” Journal of Finance, 53, 5, 1563-1587.
- [32] Lee, B. S., 1992, “Causal Relations Among Stock Returns, Interest Rates, Real Activity and Inﬂation,” Journal of Finance, 48, 1591-1603.
- [33] Lettau, M., and S. Ludvigson, 2001, “Consumption, Aggregate Wealth and Expected Stock Returns”, forthcoming Journal of Finance.
- [34] Lo, A., and A. C. MacKinlay, 1990, “Data-Snooping Biases in Tests of Financial Asset Pricing Models,” Review of Financial Studies, 3, 431-468.
- [35] Lucas, R., 1978, “Asset Prices in an Exchange Economy,” Econometrica, 46, 1419-1446.
- [36] Newey, W., 1985, “Generalized Method of Moments Speciﬁcation Testing,” Journal of Econometrics, 29, 3, 229-56.
- [37] Newey, W., and K. West, 1987, “A Simple, Positive Semi-Deﬁnite, Heteroskedasticity and Autocorrelation Consistent Covariance Matrix,” Econometrica, 55, 703-708.
- [38] Patelis, A. D., 1997, “Stock Return Predictability and the Role of Monetary Policy,” Journal of Finance, 52, 5, 1951-1972.
- [39] Richardson, M., 1993, “Temporary Components of Stock Prices: A Skeptic’s View,” Journal of Business and Economic Statistics, 11, 2, 199-207.
- [40] Richardson, M., and T. Smith, 1991, “Tests of Financial Models in the Presence of Overlapping Observations,” Review of Financial Studies, 4, 2, 227-254.
- [41] Richardson, M., and J. H. Stock, 1989, “Drawing Inferences from Statistics Based on Multiyear Asset Returns,” Journal of Financial Economics, 25, 323-348.
- [42] Shiller, R. J., and A. E. Beltratti, 1992, “Stock Prices and Bond Yields: Can Their Comovements Be Explained in Terms of Present Value Models?” Journal of Monetary Economics, 30, 25-46.
- [43] Stambaugh, R. F., 1999, “Predictive Regressions,” Journal of Financial Economics, 54, 375-421.
- [44] Valkanov, R., 2000, “Long-Horizon Regressions: Theoretical Results and Applications to the Expected Returns/Dividend Yields and Fisher Effect Relations,” working paper.

Table 1: Sample Moments of Returns and Instruments

US

mean 0.0766 -3.3632 -2.6271 0.0769 0.0689 -0.7364 stdev 0.1477 0.4059 0.3915 0.0340 0.0819 0.1596

-0.0080 0.9819 0.9839 0.9699 0.0940 0.9871 UK

mean 0.0765 -3.0780 -2.4601 0.1027 stdev 0.1848 0.2556 0.3608 0.0347

-0.0154 0.9601 0.9690 0.9521 France

- mean 0.0689 -3.2192 -2.8219 0.0948 stdev 0.2088 0.4085 0.6171 0.0473

0.0795 0.9803 0.9473 0.8464 Germany

- mean 0.0690 -3.3512 -2.7435 0.0576 stdev 0.1880 0.3324 0.4757 0.0245

0.0582 0.9794 0.9812 0.9806 Japan

mean 0.0358 0.0106 0.0284 0.0454 stdev 0.1911 0.0051 0.0174 0.0302

0.0275 0.9808 0.9811 0.9678

Summary statistics of monthly excess returns and instruments. In the table represents excess returns, log dividend yields, log earnings yields, short rates. Excess returns and short rates are continuously compounded monthly returns. The equity returns are from MSCI and the short rates are EURO 1 month rates. The excess return for a country is equal to the equity return in local currency less the EURO 1 month rate for that country. The mean and standard deviation of and are obtained by multiplying the sample mean and standard deviation by 12 and respectively. denotes the sample autocorrelation. Dividend (earnings) yields are from MSCI which use the sum of dividends (earnings) over the past twelve months. The table reports continuously compounded growth in earnings rates which is the growth in earnings summed over the past year ( ) to the past year beginning one month earlier ( ) for the US. The log payout ratio for the US is the difference of and . The sample period is from Feb 1975 to Dec 1999 for the US, UK, France and Germany and from Jan 1978 to Dec 1999 for Japan. Earnings yields for Japan are negative during 1999, so we report levels, instead of logs, for dividend and earnings yields for Japan.

[Figure 92]

Table 2: Null Model VAR Estimation

Constant and Companion Form const Companion form Null Model

0.0002 0.9711 0.0000 0.0000 (0.0001) (0.0140)

0.0216 -0.2894 -0.0078 0.0079 (0.0012)

-0.0222 1.2894 0.0078 0.9921 (0.0012) (0.0900) (0.0105) (0.0010)

Alternative Present Value Model

0.0002 0.9711 0.0000 0.0000 (0.0001) (0.0140)

0.0125 -0.2452 0.2739 0.0096 (0.0037) (0.0597) (0.1669) (0.0036)

-0.0104 0.0584 0.0204 0.9867 (0.0024) (0.9690) (0.2237) (0.0044)

Conditional Volatilities and Correlations Volatility Conditional Correlations

0.0007 1.0000 (0.0000)

0.0647 0.1038 1.0000 (0.0137) (0.0318)

0.0351 -0.1758 -0.8496 1.0000 (0.0129) (0.4035) (0.1874)

We estimate the monthly VAR , of , where is the continuously-compounded risk-free rate, is monthly (unobserved) earnings growth and

is the monthly (unobserved) log payout ratio. We set , where subscripts denote matrix elements (row and column). Estimation of the Alternative VAR proceeds in two steps. First, we estimate the equation for on US EURO 1 month rates. Second, holding these parameters as ﬁxed, we estimate the remaining parameters in , , and using Simulated Method of Moments. We match the ﬁrst and second moments of MSCI data on log earnings growth and log payout ratio which use summed earnings and dividends over the past year in their construction. We also use the cross-moment of current (annual) growth and (annual) payout with lagged one-year growth and payout. The Alternative Model is exactly identiﬁed. To estimate the Null Model we hold ﬁxed the covariance matrix from the Alternative Model. Then using ﬁrst and cross-moments we estimate

and . The Null Model’s VAR is estimated subject to the restrictions:

The Null Model is over-identiﬁed. A test of the over-identify restriction yields a statistic of 0.4710, which has a p-value of 0.9252.

Table 3: Small Sample Coefﬁcients from the Null Model

horizon

- Panel A: Dividend Regression Coefﬁcient horizon

mean 0.0692 0.0547 0.0517 stdev 0.3216 0.2015 0.0879

- Panel B: Earnings Regression Coefﬁcient horizon

mean -0.0331 -0.0304 -0.0243 stdev 0.1735 0.1548 0.1169

- Panel C: Lamont Regression Coefﬁcients

mean 0.1877 -0.0913 0.1603 -0.0829 0.1175 -0.0604 stdev 0.3767 0.2207 0.2758 0.2108 0.1649 0.1607

Panel D: Trivariate Regression Coefﬁcients horizon

mean 0.2411 -0.1093 0.0003 0.1983 -0.0954 -0.0010 0.1266 -0.0624 -0.0004 stdev 0.3932 0.2386 0.1357 0.2828 0.2228 0.1199 0.1649 0.1613 0.0784

The table reports the mean and standard deviation of the small sample distribution of the slope coefﬁcients in the regression: where is the cumulated and annualized -period ahead return, is the log dividend yield alone in Panel A, the log earnings yield alone in Panel B, the log dividend yield and log earnings yield together in Panel C, and the log dividend yield, log earnings yield, and the short rate in Panel D. The small sample distribution is based on 5000 replications of a sample size of 299 observations using the Constant Expected Return Null Model in Table (2) as the DGP.

Table 4: Size Properties of T-Statistics from the Constant Expected Return Null Model

Dividend Regression Nominal size 0.100 0.050 0.100 0.050 0.100 0.050

- OLS 0.105 0.052 0.471 0.402 0.611 0.541 Robust Hansen-Hodrick 0.108 0.055 0.210 0.144 0.470 0.391 Hodrick 1B 0.108 0.055 0.106 0.052 0.144 0.076

Earnings Regression Nominal size 0.100 0.050 0.100 0.050 0.100 0.050

[Figure 93]

- OLS 0.106 0.052 0.601 0.539 0.786 0.747 Robust Hansen-Hodrick 0.111 0.055 0.190 0.124 0.475 0.403 Hodrick 0.111 0.055 0.096 0.044 0.079 0.036

[Figure 94]

#### Lamont Regression

Nominal size 0.100 0.050 0.100 0.050 0.100 0.050 Dividend coefﬁcients only OLS 0.133 0.069 0.583 0.514 0.786 0.722

[Figure 95]

- Robust Hansen-Hodrick 0.137 0.071 0.254 0.187 0.529 0.457

- Hodrick 0.137 0.071 0.145 0.081 0.139 0.077 Earnings coefﬁcients only OLS 0.136 0.075 0.661 0.600 0.835 0.800

Robust Hansen-Hodrick 0.138 0.078 0.223 0.152 0.497 0.426

- Hodrick 0.138 0.078 0.127 0.066 0.098 0.051 Extended Lamont Regression

Dividend coefﬁcients only Nominal size 0.100 0.050 0.100 0.050 0.100 0.050 Dividend coefﬁcients only OLS 0.157 0.086 0.613 0.549 0.788 0.744 Robust Hansen-Hodrick 0.162 0.089 0.297 0.223 0.561 0.486 Hodrick 0.162 0.089 0.170 0.099 0.145 0.079 Earnings coefﬁcients only OLS 0.146 0.084 0.668 0.610 0.826 0.801 Robust Hansen-Hodrick 0.149 0.086 0.249 0.175 0.524 0.448 Hodrick 0.149 0.086 0.131 0.075 0.091 0.047 Short Rate coefﬁcients only OLS 0.123 0.064 0.643 0.578 0.794 0.761 Robust Hansen-Hodrick 0.127 0.068 0.226 0.152 0.486 0.407 Hodrick 0.127 0.068 0.119 0.060 0.089 0.048

[Figure 96]

The table lists nominal versus empirical size properties of the OLS, Robust Hansen-Hodrick and Hodrick t-statistics. We simulate 5000 samples of length 299 from the Constant Expected Return Null Model in Table (2), calculate the t-statistics for each method and record the percentage of observations greater than the nominal critical values under the null hypothesis of no predictability.

Table 5: Predictability of US Excess Returns

Univariate Regressions Lamont Regression Trivariate Regression only only

[Figure 97]

Full Sample 1975:02 - 1999:12 1 -0.0820 -0.0415 -0.2994 0.2445 -0.3896 0.5747 -3.7341

(-1.0571) (-0.5301) (-1.6837)* (1.3720) (-2.1524)* (2.5620)* (-2.7539)** 12 -0.1063 -0.0673 -0.2581 0.1635 -0.2710 0.2433 -0.9604

(-1.1315) (-0.8086) (-1.3550) (1.0190) (-1.4465) (1.3738) (-0.8302) 60 -0.0942 -0.0859 0.2280 -0.2394 0.1815 -0.2616 0.6659

(-0.5249) (-0.9866) (0.2890) (0.5094) (0.2168) (-0.5890) (0.7111)

Restricted Sample I 1975:02 - 1994:12 1 0.0957 0.0552 0.2272 -0.0975 0.5494 0.0518 -4.5453

(0.6615) (0.5674) (0.5705) (-0.3725) (1.3249) (0.1939) (-2.9723)** 12 0.0480 0.0217 0.1859 -0.1009 0.2837 -0.0598 -1.3252

(0.3260) (0.2324) (0.4980) (-0.4547) (0.7318) (-0.2634) (-1.0870) 60 0.0415 0.0141 0.2574 -0.1917 0.1991 -0.2045 -0.6636

(0.2662) (0.0957) (0.7205) (-0.5266) (0.6007) (-0.5679) (1.2746)

Restricted Sample II 1975:02 - 1991:12 1 0.1050 0.0760 0.1417 -0.0306 0.5471 0.0315 -4.5079

(0.4763) (0.4094) (0.2553) (-0.0633) (0.9757) (0.0656) (-2.9744)** 12 0.0874 0.0700 0.0747 0.0111 0.1960 0.0281 -1.3268

(0.3904) (0.3559) (0.1629) (0.0256) (0.4201) (0.0654) (-1.0924) 60 0.0873 0.0320 0.4615 -0.3306 0.3669 -0.3210 0.5557

(0.3317) (0.1363) (1.0938) (-0.7625) (0.9128) (-0.7834) (0.5873)

We estimate regressions of the form where is the cumulated and annualized -period ahead return, with instruments . The ﬁrst two columns contain the coefﬁcients for univariate regressions ( , the log dividend yield, and

, the log earnings yield). Columns 3 and 4 contain the coefﬁcients for the Lamont regression ), and the last three columns give the coefﬁcients for the trivariate regression

, where is the annualized 1-month short rate. T-statistics are in parentheses and calculated using Hodrick standard errors. T-statistics signiﬁcant at 95% (99%) are denoted with * (**).

Table 6: Predictability Across Horizons in 5 Countries

US UK France Germany Japan Univariate Regressions

[Figure 98]

0.8556 0.5014 0.6207 0.5821 0.0818 0.5869 0.0404* 0.8732 0.8803 0.0572

Lamont Regression - and

only 0.6145 0.6129 0.5464 0.1394 0.9496 only 0.3723 0.8116 0.7030 0.1881 0.7433

Joint and 0.1495 0.1502 0.8271 0.2453 0.0101* Trivariate Regression - , ,

only 0.7016 0.5474 0.8857 0.3523 0.9691 only 0.0849 0.2583 0.6519 0.2966 0.7915

Joint and 0.0097** 0.0111* 0.7897 0.4082 0.0010** only 0.0399* 0.1063 0.3802 0.1279 0.9318 Joint , , 0.0105* 0.0312* 0.7260 0.0984 0.0018**

The table lists p-values of joint tests across horizons . P-values less than 5% (1%) are asterixed * (**). denotes the log dividend yield, the log earnings yield and the short rate. Japan’s (marked by ) regressions are performed in levels, not logs.

Table 7: Pooled-Country Estimations Excluding Japan

Lamont System and

-0.0234 0.0352 0.1084 (-0.2803) (0.3594) (1.2303)

0.0046 -0.0590 -0.0593 (0.0859) (-1.1053) (-1.4923) Test p-values

J-test 0.2605 0.5343 0.1667 0.9592 0.5167 0.2253

Trivariate System , ,

0.0719 0.0726 0.0860 (0.7884) (0.7119) (1.0057)

0.0236 -0.0521 -0.0613 (0.4626) (-1.0446) (-1.7079)

-1.7334 -0.6554 -0.3357

(-2.5247)* (-1.1852) (0.8094) p-values

J-test 0.1001 0.3960 0.1397 0.0851 0.4849 0.1451 0.4951 0.5653 0.1613

0.0116* 0.2359 0.4183

The predictability regression where is the cumulated and annualized -period ahead return with instruments , is estimated jointly across countries, constraining the coefﬁcients to be the same across countries (see Appendix F for details). Japan is excluded from estimation because of a shorter sample and negative earnings yields during 1999. The constants in the regressions are allowed to differ across countries (and are not reported in the table). We report the Lamont system where and a tri-variate system with

, where and denote the log dividend and earnings yields respectively, and is the annualized one-month short rate. T-statistics of the predictability coefﬁcients are in parentheses and are based on Hodrick (1992) standard errors. In the tests, the J-test is a test of the over-identifying restrictions and the other tests refer to joint test of coefﬁcients equalling zero. T-statistics signiﬁcant at levels greater than than 95% are asterixed *.

Table 8: Cross-Country Predictability of Equity Returns

US US US Local Local Local Local Market is UK

[Figure 99]

1 -0.4806 0.1215 -3.2367 0.5282 0.5427 -2.0319

(-1.1352) (0.2201) (-1.5434) (1.0346) (1.0204) (-1.1247) 12 -0.3486 0.2964 -0.4831 0.4699 -0.1061 -0.8179

(-1.1527) (0.8534) (-0.2761) (1.2299) (-0.4139) (-0.6138) 60 0.0467 -0.0024 0.6602 0.3559 -0.1419 -0.6771

(0.0532) (-0.0052) (0.4802) (1.1660) (-1.2958) (-0.4557) Local Market is FR

1 -0.6061 0.6967 -3.0557 0.0512 -0.0188 0.1898

(-1.8558)* (1.7115) (-1.1329) (0.2383) (-0.2786) (0.1090) 12 -0.3639 0.3448 -1.3904 0.0991 -0.0622 0.3813

(-1.1643) (1.2332) (-0.7624) (0.5041) (-1.0004) (0.4261) 60 0.0527 -0.1538 0.6449 0.1095 -0.0292 0.3064

(0.0330) (-0.2238) (0.3249) (0.4004) (-0.3712) (0.7332) Local Market is GER

1 -1.0831 0.8229 -4.1665 0.6142 0.0012 0.0589

(-2.6604)** (1.8206) (-1.7929) (1.4097) (0.0081) (0.0205) 12 -0.6014 0.4281 -1.4525 0.5002 -0.1343 -1.1546

(-1.5260) (1.3244) (-0.9198) (1.2788) (-1.0086) (-0.4912) 60 0.1639 -0.1531 0.1716 0.2981 -0.1729 0.8250

(0.1153) (-0.2313) (0.0982) (0.8964) (-1.7115) (0.5810) Local Market is JAP

1 -6.9948 3.6414 -1.9965 0.1794 0.0011 -0.4109

(-0.5427) (0.6959) (-0.9995) (1.0262) (0.0145) (-0.2348) 12 7.0783 -1.3938 -1.5191 0.1658 -0.0166 -0.4580

(0.5893) (-0.2835) (-0.8545) (0.8256) (-0.2091) (-0.3125) 60 16.8843 -5.0788 -0.1481 0.0568 0.0173 0.0583

(0.4863) (-0.6249) (-0.1294) (0.2003) (0.4359) (0.0589)

We regress local excess equity returns of horizon onto US instruments and local instruments. Hodrick standard errors are used to calculate t-statistics given in parantheses. T-statistics signiﬁcant at the 95% (99%) level are asterixed * (**). The regressions for Japan are run in levels for and

(not logs).

Table 9: Cross-Country Predictability of Equity Returns Tests

Base Local Base Pred Local Pred UK 0.1639 0.1761

[Figure 100]

US FR 0.3016 0.9773 GR 0.0498* 0.2441 JP 0.7870 0.5249 US 0.8656 0.0213*

[Figure 101]

UK FR 0.5197 0.9311 GR 0.6385 0.6695 JP 0.4137 0.4154 US 0.5299 0.0306*

[Figure 102]

FR UK 0.3826 0.1797 GR 0.9929 0.6612 JP 0.6355 0.1822 US 0.4925 0.0491*

[Figure 103]

GR UK 0.2993 0.1587 FR 0.4666 0.9912 JP 0.0250* 0.6342 US 0.5905 0.0013**

[Figure 104]

JP UK 0.4989 0.1619 FR 0.9183 0.2911 GR 0.9322 0.6202

[Figure 105]

We regress local excess equity returns on base country instruments and local instruments ( , and annualized short rates ). For example, the top entry regresses UK equity excess returns on US instruments and UK instruments; the second entry regresses French equity excess returns on US instruments and French instruments. We report p-value tests for the hypothesis of base country predictability (“Base Pred”) and local country predictability (“Local Pred”) at a one-month horizon. P-values less than 5% are asterixed *, those less than 1% are asterixed **. Regressions for Japan (indicated by ) are run in levels, not logs.

Table 10: US Predictability of Foreign Equity Returns

Coefﬁcients Predictability Tests

US US US , , , UK on US instruments

[Figure 106]

1 -0.2954 0.6406 -4.3467 0.1107 0.0354* 0.1867 (-1.2797) (1.8791) (-2.1040)* 12 -0.1080 0.2140 -1.1907 0.6400 0.4651 0.8233 (-0.5372) (0.8931) (-0.7305) 60 0.2872 -0.1720 0.2219 0.8947 0.8036 0.8584

(0.4010) (-0.4460) (0.2487) FR on US instruments

1 -0.5716 0.7090 -3.0522 0.0679 0.1789 0.1179 (-2.2632)* (2.1677)* (-1.3422) 12 -0.3033 0.3647 -1.4670 0.4244 0.4004 0.5711 (-1.1262) (1.2971) (-0.8410) 60 0.3506 -0.2421 0.3816 0.8133 0.7547 0.8258

(0.3277) (-0.4238) (0.3124) GR on US instruments

1 -0.6258 0.7185 -2.5147 0.0279* 0.0708 0.0308* (-2.4711)* (2.6343)** (-1.8071)* 12 -0.3903 0.4392 -1.1823 0.1366 0.2607 0.1989 (-1.4450) (1.9760)* (-1.1247) 60 0.3340 -0.3268 1.2753 0.1431 0.3402 0.0910

(0.2691) (-0.4968) (0.9537) JP on US instruments

1 -0.2984 0.5406 -2.5062 0.2503 0.1667 0.4201 (-1.0893) (1.5631) (-1.3828) 12 0.0469 0.2005 -1.8474 0.3647 0.2339 0.5681 (0.1673) (0.6744) (-1.1903) 60 0.9097 -0.4119 -0.1968 0.3525 0.8254 0.3183

(0.7357) (-0.5853) (-0.2207) Pooled Estimation (excluding JP) on US instruments

1 -0.4706 0.6607 -3.4119 0.0061** 0.0032** 0.0036** (-2.8419)** (3.1855)** (-2.9440)** 12 -0.2682 0.3153 -1.2001 0.1341 0.1683 0.1690 (-1.6076) (2.0033)* (-1.3776) 60 0.2883 -0.2506 0.6361 0.3242 0.4708 0.3839 (0.3771) (-0.6151) (0.7212)

We regress UK, FR, GR and JP excess equity returns for horizon on US instruments only (US , and annualized short rates ). The last panel presents the estimations of predictability coefﬁcients constraining the coefﬁcients to be the same across countries, excluding Japan. The constants in the regressions are allowed to differ across countries (and are not reported in the table). T-statistics of the predictability coefﬁcients are in parenthesis and are calculated using Hodrick (1992) standard errors. In the tests, we perform a joint test of coefﬁcients equalling zero. For the joint estimation the p-values for a J-test of over-identiﬁcation are 0.2876, 0.0940 and 0.6197 for

, 12 and 60 respectively. P-values less than 5% (1%) are asterixed * (**).

Table 11: Cross-Country Predictability of Exchange Rate Returns

US US US Local Local Local US-UK Exchange Rate Return

[Figure 107]

1 -0.1618 0.0846 -2.3076 -0.5544 0.0014 1.9074

(0.8279) (0.2819) (-2.2235)* (-2.3974)* (0.0061) (1.7577)* 12 -0.1189 0.5339 -2.1985 -0.2221 -0.3607 0.9876

(-0.6261) (1.9995)* (-2.5520)* (-1.0779) (-2.0673)* (1.2725) 60 -0.0202 0.0551 -0.2927 0.0408 -0.1638 0.0085

(-0.0463) (0.2400) (-0.3894) (0.2360) (-2.4828)* (0.0105) US-GR Exchange Rate Return

1 0.6462 -0.1047 0.0707 -0.8342 0.0790 -0.0619

(3.2389)** (-0.4852) (0.0514) (-3.8443)** (0.9796) (-0.0385) 12 0.5111 0.0105 -0.8178 -0.7206 0.1011 0.0671

(2.5128)* (0.0607) (-0.8983) (-3.5886)** (1.2660) (0.0505) 60 0.2615 -0.1337 0.4888 -0.2570 0.0459 -0.0697

(0.5061) (-0.5518) (0.6322) (-1.9243) (0.9329) (-0.1090) US-JP Exchange Rate Return

1 4.7153 -6.0483 0.0012 0.2085 -0.0666 3.7250

(0.5470) (-1.6499) (0.0007) (1.5573) (-1.2474) (-2.2651)* 12 -0.4377 -1.7852 -1.4859 -0.0136 0.0256 1.6005

(-0.0519) (-0.6045) (-1.1226) (-1.1096) (0.4801) (1.5244) 60 11.5440 -3.6162 0.2162 -0.1345 0.0227 0.1839

(0.4527) (-0.6076) (0.2755) (-0.7003) (0.9389) (0.2619)

Tests Joint Across Horizons , 12, 60 US Local Short Rates Yields All Variables

US-UK 0.1876 0.0615 0.2869 0.0465* 0.0000** US-GR 0.2982 0.1449 0.5286 0.0051** 0.0000** US-JP 0.0162 0.0002** 0.0049** 0.0047** 0.0000**

We regress exchange rate returns (expressed in dollars per foreign currency) onto US instruments and local (foreign country) instruments. We investigate horizons , 12 and 60. Hodrick standard errors are used to calculate t-statistics given in parentheses. T-statistics signiﬁcant at the 95% (99%) level are asterixed * (**). The regressions for Japan are run in levels for and (not logs). The bottom panel reports p-values of tests joint across horizons , 12, 60 for exchange rate predictability. The column labeled “US” tests joint predictability of US dividend yields

, earnings yields and US short rates . The column labeled “Local” tests joint predictability of foreign country , and . The column labeled “Short Rate” tests for joint US and foreign country predictability. The column labeled “Yields” tests for joint US and foreign country

and predictability. Finally, the column labeled “All Variables” tests joint predictability of all US and foreign country instruments. P-values less than 5% (1%) are asterixed * (**).

Risk Premium Annualized

0.12

|Model log risk premium Model simple risk premium Empirical log risk premium Empirical simple risk premium<br><br>|
|---|

0.1

0.08

RiskPremium

0.06

0.04

0.02

0

−0.02

−6 −5 −4 −3 −2 −1 0

Beta

Annualized simple risk premiums (dashed line) and log risk premiums (solid line). The simple risk premiums are calculated using Corollary 2.1 and the log risk premiums are produced by simulation. The simple (log) risk premium in the sample used for calibration is 0.0880 (0.0766). A price of risk vector with

of -4.655 matches both the empirical simple risk premium and the empirical log risk premium.

Figure 1: Risk Premium from the Null Present Value Model

Dividend Significance US T−statistics

Dividend Coefficients US

−0.08

−1

−2

−0.09

−3

|OLS Robust Hansen−Hodrick Hodrick|
|---|

−0.1

−4

Coefficient

−5

T−stat

−0.11

−6

−7

−0.12

−8

−0.13

−9

−10

−0.14

5 10 15 20 25 30 35 40 45 50 55 60

5 10 15 20 25 30 35 40 45 50 55 60

Horizon (months)

Horizon (months)

Earnings Significance US T−statistics

Earnings Coefficients US

−0.04

−1

−2

−0.05

−3

|OLS Robust Hansen−Hodrick Hodrick|
|---|

−0.06

−4

Coefficient

T−stat

−5

−0.07

−6

−0.08

−7

−8

−0.09

−9

5 10 15 20 25 30 35 40 45 50 55 60

5 10 15 20 25 30 35 40 45 50 55 60

Horizon (months)

Horizon (months)

Dividend Significance US T−statistics

Lamont Coefficients US

- 0

- 1

0.2

0.15

T−stat

−1

0.1

−2

0.05

Robust Hansen−Hodrick Hodrick

−3

5 10 15 20 25 30 35 40 45 50 55 60

Coefficient

0

Horizon (months)

|Dividend Earnings|
|---|

−0.05

Earnings Significance US T−statistics

−0.1

- 0

- 1

−0.15

T−stat

|Robust Hansen−Hodrick Hodrick<br><br>|
|---|

−0.2

−1

−0.25

−2

5 10 15 20 25 30 35 40 45 50 55 60

5 10 15 20 25 30 35 40 45 50 55 60

Horizon (months)

Horizon (months)

The left column shows coefﬁcients in the regression where

is the cumulated and annualized -period ahead return, with instruments (log dividend yields) in the top row, (log earnings yields) in the middle row and in the bottom row. The right column shows t-statistics from these regressions. Horizons are on the x-axis.

Figure 2: Coefﬁcients and Standard Errors from US Regressions

Dividend Coefficients UK

0.25

- −0.06

Coefficient

Dividend Coefficients US

0 10 20 30 40 50 60

- −1.2

−0.08

0.2

Coefficient

−0.1

0.15

−0.12

0.1

−0.14

0.05

−0.16

0 10 20 30 40 50 60

0 10 20 30 40 50 60

Dividend Significance UK T−statistics

Dividend Significance US T−statistics

1.6

−0.4

1.4

−0.6

1.2

HodrickT−stat

HodrickT−stat

- 0.8

- 1

−0.8

0.6

−1

0.4

0.2

0 10 20 30 40 50 60

Horizon (months)

Horizon (months)

Dividend Coefficients FR

Dividend Coefficients GR

0.08

0.1

0.06

0.05

0.04

Coefficient

Coefficient

0.02

0

0

−0.05

−0.02

−0.04

−0.1

0 10 20 30 40 50 60

0 10 20 30 40 50 60

Dividend Significance FR T−statistics

Dividend Significance GR T−statistics

- 0.8

- 1

0.6

0.4

0.6

0.2

HodrickT−stat

HodrickT−stat

0.4

0

0.2

−0.2

0

−0.4

−0.2

−0.6

−0.4

−0.8

0 10 20 30 40 50 60

0 10 20 30 40 50 60

Horizon (months)

Horizon (months)

Dividend Coefficients JP

- 10

- 11

- 12

- 13

- 14

- 15

- 16

- 17

Coefficient

0 10 20 30 40 50 60

Dividend Significance JP T−statistics

2.6

2.4

HodrickT−stat

2.2

- 1.8

- 2

1.6

0 10 20 30 40 50 60

Horizon (months)

Dividend coefﬁcients and t-statistics calculed using Hodrick standard errors for the regression

where is the cumulated and annualized -period ahead return, with instruments . Horizons are on the x-axis. For Japan, the dividend yield is in levels but for all other countries represents the log dividend yield.

Figure 3: Dividend Regressions in 5 Countries

Earnings Coefficients UK

0.2

- −0.03

Coefficient

Earnings Coefficients US

0 10 20 30 40 50 60

- −1.2

−0.04

0.15

−0.05

Coefficient

−0.06

0.1

−0.07

−0.08

0.05

−0.09

0

−0.1

0 10 20 30 40 50 60

0 10 20 30 40 50 60

Earnings Significance UK T−statistics

Earnings Significance US T−statistics

1.5

−0.4

−0.6

HodrickT−stat

HodrickT−stat

1

−0.8

0.5

−1

0

0 10 20 30 40 50 60

Horizon (months)

Horizon (months)

Earnings Coefficients FR

0

- −0.01

Coefficient

Earnings Coefficients GR

0 10 20 30 40 50 60

- −1.4

- −1.2

−0.02

- −0.1

−0.08

−0.06

−0.04

- −0.02

−0.03

Coefficient

−0.04

−0.05

−0.06

−0.07

−0.08

0 10 20 30 40 50 60

0 10 20 30 40 50 60

Earnings Significance FR T−statistics

Earnings Significance GR T−statistics

0

0

−0.2

−0.5

−0.4

HodrickT−stat

HodrickT−stat

−0.6

−1

−0.8

−1

−1.5

−2

0 10 20 30 40 50 60

Horizon (months)

Horizon (months)

Earnings Coefficients JP

- 0 10 20 30 40 50 60

- 1

- 2

- 3

- 4

- 5

- 6

- 7

Coefficient

Earnings Significance JP T−statistics

- 0.5

- 1

- 1.5

- 2

- 2.5

HodrickT−stat

0 10 20 30 40 50 60 Horizon (months)

Earnings coefﬁcients and t-statistics calculated using Hodrick standard errors for the regression

where is the cumulated and annualized -period ahead return, with instruments . Horizons are on the x-axis. For Japan, the earnings yield is in levels but for all other countries represents the log earnings yield.

Figure 4: Earnings Regressions in 5 Countries

Lamont Coefficients US

Lamont Coefficients UK

0.2

0.25

0.15

0.2

0.1

0.05

|Dividend Earnings|
|---|

0.15

Coefficient

Coefficient

0

|Dividend Earnings|
|---|

0.1

−0.05

−0.1

0.05

−0.15

0

−0.2

−0.25

−0.05

5 10 15 20 25 30 35 40 45 50 55 60

5 10 15 20 25 30 35 40 45 50 55 60

Lamont Coefficients FR

Lamont Coefficients GR

0.1

0.3

0.08

0.06

0.2

0.04

|Dividend Earnings|
|---|

0.02

0.1

Coefficient

Coefficient

0

- −0.1

−0.08

−0.06

−0.04

- −0.02

|Dividend Earnings|
|---|

0

−0.1

−0.2

5 10 15 20 25 30 35 40 45 50 55 60

5 10 15 20 25 30 35 40 45 50 55 60

Lamont Coefficients JP

|Dividend Earnings<br><br>|
|---|

20

15

Coefficient

10

5

0

5 10 15 20 25 30 35 40 45 50 55 60

Dividend and earnings coefﬁcients from the regression where

is the cumulated and annualized -period ahead return, with instruments . Horizons are on the x-axis. For Japan dividend and earnings yields in levels are used, all other countries use log dividend and earnings yields.

Figure 5: Lamont Regressions Coefﬁcients in 5 Countries

Short Rate Coefficient from Trivariate Regression UK

Short Rate Coefficient from Trivariate Regression US

0

- 0

- 1

−0.5

−1

Coefficient

Coefficient

−1

−1.5

−2

−2

−3

−2.5

−3

−4

0 10 20 30 40 50 60

0 10 20 30 40 50 60

Short Rate Significance in Trivariate Regression UK T−statistics

Short Rate Significance in Trivariate Regression US T−statistics

−0.4

- 0

- 1

−0.6

−0.8

HodrickT−stat

HodrickT−stat

−1

−1

−1.2

−1.4

−2

−1.6

−1.8

−3

0 10 20 30 40 50 60

0 10 20 30 40 50 60

Horizon (months)

Horizon (months)

Short Rate Coefficient from Trivariate Regression FR

Short Rate Coefficient from Trivariate Regression GR

- 0.5

- 1

- 0

- 1

- 2

0

Coefficient

Coefficient

−0.5

−1

−1

−2

−1.5

−2

−3

0 10 20 30 40 50 60

0 10 20 30 40 50 60

Short Rate Significance in Trivariate Regression FR T−statistics

Short Rate Significance in Trivariate Regression GR T−statistics

1

- 0

- 0.5

- 1

- 1.5

0.5

HodrickT−stat

HodrickT−stat

0

−0.5

−0.5

−1

−1

−1.5

−1.5

−2

0 10 20 30 40 50 60

0 10 20 30 40 50 60

Horizon (months)

Horizon (months)

Short Rate Coefficient from Trivariate Regression JP

0

−0.5

Coefficient

−1

−1.5

−2

0 10 20 30 40 50 60

Short Rate Significance in Trivariate Regression JP T−statistics

0

HodrickT−stat

−0.5

−1

−1.5

0 10 20 30 40 50 60

Horizon (months)

Short rate coefﬁcients and t-statistics constructed using Hodrick standard errors from the trivariate regression

where is the cumulated and annualized -period ahead return, with instruments . The short rate is annualized. We report only the coefﬁcient on . Horizons are on the x-axis. For Japan dividend yields and earnings yields are in levels, for the other countries these are log dividend and earning yields respectively.

Figure 6: Short Rate Coefﬁcients in Trivariate Regressions in 5 Countries

