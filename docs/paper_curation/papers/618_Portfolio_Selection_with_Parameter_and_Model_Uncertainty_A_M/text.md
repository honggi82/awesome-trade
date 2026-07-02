# Portfolio Selection with Parameter and Model Uncertainty: A Multi-Prior Approach∗

Lorenzo Garlappi† Raman Uppal‡ Tan Wang§

April 2004

∗We gratefully acknowledge ﬁnancial support from INQUIRE UK; this article however represents the views of the authors and not of INQUIRE. We are very grateful to Lubosˇˇ P´stor for extensive comments. We thank Nicholas Barberis, Suleyman Basak, Ian Cooper, Victor DeMiguel, Francisco Gomes, Tim Johnson, Catalina Stefanescu, Yongjun Tang, Sheridan Titman, Roberto Wessels and participants at presentations given at Copenhagen Business School, Imperial College, Lancaster University, London Business School, University of Maryland, University of Texas at Austin, and the INQUIRE Fall 2003 conference for helpful suggestions.

†McCombs School of Business, The University of Texas at Austin, Austin TX, 78712; Email: lorenzo.garlappi@mccombs.utexas.edu.

‡London Business School and CEPR; IFA, 6 Sussex Place Regent’s Park, London, United Kingdom NW1 4SA; Email: ruppal@london.edu.

§University of British Columbia, 2053 Main Mall, Vancouver Canada V6T 1Z2, Canada; Email: tan.wang@commerce.ubc.ca.

# Portfolio Selection with Parameter and Model Uncertainty: A Multi-Prior Approach

### Abstract

In this paper, we extend the mean-variance portfolio model where expected returns are obtained using maximum likelihood estimation to explicitly account for uncertainty about the estimated expected returns. In contrast to the Bayesian approach to estimation error, where there is only a single prior and the investor is neutral to uncertainty, we allow for multiple priors and aversion to uncertainty. We characterize the set of priors as a conﬁdence interval around the estimated value of expected return and we model aversion to uncertainty via a minimization over the set of priors. The multi-prior model has several attractive features: One, just like the Bayesian model, the multi-prior model is ﬁrmly grounded in decision theory; Two, it is ﬂexible enough to allow for uncertainty about expected returns estimated jointly for all assets or diﬀerent levels of uncertainty about expected returns for diﬀerent subsets of the assets; Three, we show how in several special cases of the multi-prior model one can obtain closed-form expressions for the optimal portfolio, which can be interpreted as a shrinkage of the mean-variance portfolio towards either the risk-free asset or the minimum variance portfolio. We illustrate how to implement the multi-prior model using both international and domestic data. Our analysis suggests that allowing for parameter uncertainty reduces the ﬂuctuation of portfolio weights over time and, for the data set considered, improves the out-of sample performance.

Keywords: Portfolio choice, asset allocation, estimation error, uncertainty, ambiguity, robustness. JEL Classiﬁcation: G11, D81

# Contents

- 1 Introduction 1
- 2 Multi-prior approach to portfolio choice 5

- 2.1 The classical mean-variance portfolio model . . . . . . . . . . . . . . . . . . 6
- 2.2 Extension of the standard model to incorporate uncertainty aversion . . . . 7

- 2.2.1 Uncertainty about expected returns estimated asset-by-asset . . . . 8
- 2.2.2 Uncertainty about expected returns estimated jointly for all assets . 10
- 2.2.3 Uncertainty about expected returns estimated for subsets of assets . 11
- 2.2.4 Uncertainty about the return-generating model and expected returns 13

- 3 Comparison with other approaches to estimation error 15

- 3.1 A summary of the traditional Bayesian approach . . . . . . . . . . . . . . . 16
- 3.2 Comparison of the multi-prior approach with Bayesian approach . . . . . . 17
- 3.3 Analytic comparison of the portfolio weights from the various models . . . . 18

- 4 Empirical applications of the multi-prior approach 21

- 4.1 Uncertainty about expected returns: International data . . . . . . . . . . . 22
- 4.2 Uncertainty about expected returns and factor model: Domestic data . . . 26

- 5 Conclusion 28 A Appendix: Proofs of all propositions 30

# List of Tables

- 1 Parameters for the two-asset one-factor example . . . . . . . . . . . . . . . 35
- 2 Portfolio weights for the two-asset one-factor example . . . . . . . . . . . . 36
- 3 Summary statistics for international data . . . . . . . . . . . . . . . . . . . 37
- 4 Out-of-sample performance of various portfolios using international data . 38
- 5 Out-of-sample Sharpe Ratios for various portfolios using domestic data with

- ω = 0 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39

6 Out-of-sample Sharpe Ratios for various portfolios using domestic data with

- ω = 1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40

# List of Figures

- 1 Portfolio weights in the US index over time . . . . . . . . . . . . . . . . . . 41
- 2 Shrinkage factors φMP( ) and φBS over time . . . . . . . . . . . . . . . . . 42
- 3 Portfolio weights assuming expected returns estimated using MLE . . . . . 43
- 4 Portfolio weights assuming factor model (CAPM) for expected returns . . 45

# 1 Introduction

Expected returns, variances, and covariances are estimated with error. But classical meanvariance portfolio optimization ignores the estimation error, and consequently, the meanvariance portfolio formed using sample moments has extreme portfolio weights that ﬂuctuate substantially over time and the out-of-sample performance of such a portfolio is quite poor.1 The standard decision-theoretic approach2 adopted in the literature to deal with estimation error is to use Bayesian “shrinkage” estimators that incorporate a prior.3 But, the Bayesian approach assumes that the decision-maker has only a single prior or is neutral to uncertainty in the sense of Knight (1921).

Given the diﬃculty in estimating moments of asset returns, it is much more likely that investors have multiple priors rather than a single prior about moments of asset returns. Moreover, there is substantial evidence from economic experiments that agents are not neutral to the ambiguity arising from having multiple priors (Ellsberg (1961)), with the aversion to uncertainty being particularly strong in cases where people feel that their competence in assessing the relevant probabilities is low (Heath and Tversky (1991)) and when subjects are told that there may be other people who are more qualiﬁed to evaluate a particular risky position (Fox and Tversky (1995)). A recent literature, for instance, Anderson, Hansen, and Sargent (1999), Chen and Epstein (2002), and Uppal and Wang (2003), develops models of decision making that allow for multiple priors and where the decision maker is not neutral to uncertainty. Our objective in this paper is to examine the implications of these theoretical models for investment management.

- 1For a discussion of the problems entailed in implementing mean-variance optimal portfolios, see Hodges and Brealey (1978), Michaud (1989), Best and Grauer (1991), and Litterman (2003).
- 2Other approaches for dealing with estimation error are to impose arbitrary portfolio constraints prohibiting shortsales (Frost and Savarino (1988) and Chopra (1993)), which Jagannathan and Ma (2003) show can be interpreted as shrinking the extreme elements of the covariance matrix, and the use of resampling based on simulations advocated by Michaud (1998). Scherer (2002) describes the resampling approach in detail and discusses some of its limitations, while Harvey, Liechty, Liechty, and M¨uller (2003) discuss other limitations and provide an estimate of the loss incurred by an investor who chooses a portfolio based on this approach. Black and Litterman (1990, 1992) propose an approach that combines two sets of priors—one based on an equilibrium asset pricing model and the other based on the subjective views of the investor—which is not strictly Bayesian because a Bayesian approach combines a prior with the data.
- 3In the literature, the Bayesian adjustment has been implemented in diﬀerent ways. Barry (1974), and Bawa, Brown, and Klein (1979), use either a non-informative diﬀuse prior or a predictive distribution obtained by integrating over the unknown parameter. In a second implementation, Jobson and Korkie (1980), Jorion (1985, 1986), Frost and Savarino (1986), and Dumas and Jacquillat (1990), use empirical Bayes estimators, which shrinks estimated returns closer to a common value and moves the portfolio weights closer to the global minimum-variance portfolio. In a third implementation, P´stor (2000), and P´stor and Stambaugh (2000) use the equilibrium implications of an asset pricing model to establish a prior; thus, in the case where one uses the CAPM to establish the prior, the resulting weights move closer to those for a value-weighted portfolio.

Our main contribution is to show how the multi-prior model of decision making can be applied to the practical problem of portfolio selection when expected returns are estimated with error,4 and to compare explicitly the portfolio weights from this approach with those from the mean-variance and traditional Bayesian models. We demonstrate how to formulate the portfolio selection problem of an uncertainty-averse fund manager. This formulation relies on two changes to the standard mean-variance model: (i) We impose an additional constraint on the mean-variance portfolio optimization program that restricts the expected return for each asset to lie within a speciﬁed conﬁdence interval of its estimated value; and (ii) We permit the fund manager to minimize over the choice of expected returns and/or models subject to this constraint, in addition to the standard maximization over portfolio weights. The additional constraint recognizes the possibility of estimation error; that is, the point estimate of the expected return is not the only possible value of the expected return considered by the investor. The minimization over the estimated expected returns reﬂects the investor’s aversion to uncertainty; that is, in contrast to the standard mean-variance model or the Bayesian approach, in the model we consider the investor is not neutral toward uncertainty.5

To understand the intuition underlying the multi-prior model, observe that because of the constrained minimization over expected returns, when the conﬁdence interval is large for a particular risky asset (that is, the mean is estimated imprecisely), then the investor relies less on the estimated mean, and hence, reduces the weight invested in this asset. When this interval is small, the minimization is constrained more tightly, and hence, the portfolio weight is closer to the standard weight that one would get from a model that ignores estimation error. In the limit, when the conﬁdence interval is zero, the optimal weights are those from the classical mean-variance model.

Our formulation of the multi-prior model of portfolio selection has several attractive features. One, just like the Bayesian model, the multi-prior model is ﬁrmly grounded in decision theory—the max-min characterization of the objective function is consistent with

- 4We focus on the error in estimating expected returns of assets because as shown in Merton (1980) they are much harder to estimate than the variances and covariances. Moreover, Chopra and Ziemba (1993) estimate the cash-equivalent loss from the use of estimated rather than true parameters. They ﬁnd that errors in estimating expected returns are over ten times as costly as errors in estimating variances, and over twenty times as costly as errors in estimating covariances. For a discussion of the problems in estimating the covariance matrix in the context of portfolio optimization, see Best and Grauer (1992), Ledoit (1996), Chan, Karceski, and Lakonishok (1999), and Ledoit and Wolf (2003).
- 5See Section 2 and Bewley (1988) for a discussion of how conﬁdence intervals obtained from classical statistics are related to Knightian uncertainty and Bayesian models of decision making.

the multi-prior approach advocated by Gilboa and Schmeidler (1989) and developed in a static setting by Dow and Werlang (1992) and Kogan and Wang (2002), in dynamic discrete-time by Epstein and Wang (1994), and in continuous time by Chen and Epstein

- (2002). Two, in several economically interesting cases, we show that the multi-prior model can be simpliﬁed to a mean-variance model but where the expected return is adjusted to reﬂect the investor’s uncertainty about its estimate. The analytic expressions we obtain for the optimal portfolio weights allow us to provide insights about the eﬀects of parameter and model uncertainty in a multi-prior setting. For instance, in one special case where we obtain a closed-form solution, we show that the optimal portfolio weights can be interpreted as a weighted average of the classical mean-variance portfolio and the minimum-variance portfolio, with the weights depending on the precision with which expected returns are estimated and the investor’s aversion to uncertainty. This special case is of particular importance because it allows us to compare the multi-prior approach of this paper with the traditional Bayesian approach in the literature. The analytic solutions also indicate how the multi-prior model can be implemented as a simple maximization problem instead of a much more complicated saddle point problem.

Three, the multi-prior model is ﬂexible enough to allow for the case where the expected returns on all assets are estimated jointly and also where the expected returns on assets are estimated in subsets. The estimation may be undertaken using classical methods such as maximum likelihood or using a Bayesian approach. Moreover, the framework can incorporate both parameter and model uncertainty; that is, it can be implemented when one is estimating expected returns from their sample moments or when one is using a particular factor model for returns such as APT or the CAPM and there is uncertainty about this being the true model. Four, the multi-prior model does not introduce ad-hoc short-sale constraints on portfolio weights that rule out short positions even if these were optimal under the true parameter values. Instead, the constraints imposed in the multi-prior model arise because of the investor’s aversion to parameter and model uncertainty. At the same time, our formulation of the multi-prior model can accommodate real-world constraints on the size of trades or position limits.6 Finally, in contrast to the Bayesian approach where

6In addition to the features described above, the multi-prior approach is consistent with any utility function, not just utility deﬁned over mean and variance—our focus on the mean-variance objective function is only because of our desire to compare our results to those in this literature.

the investor is neutral to uncertainty, the multi-prior model captures the investor’s aversion to uncertainty about both estimated parameters and the return-generating model.

Our paper is closely related to several papers in the literature. Goldfarb and Iyengar

- (2003), Halld´rsson and T¨ut¨unc¨u (2000), and T¨ut¨unc¨u and Koenig (2003) develop algorithms for solving max-min saddle-point problems numerically and apply the algorithms to portfolio choice problem, while Wang (2003) shows how to obtain the optimal portfolio numerically in a Bayesian setting in the presence of uncertainty. Our paper diﬀers from Goldfarb and Iyengar (2003), Halld´rsson and T¨ut¨unc¨u (2000), and T¨ut¨unc¨u and Koenig

(2003) in serval respects. First, we incorporate not only parameter uncertainty, but also model uncertainty. Second, we introduce joint constraints on expected returns instead of only individual constraints as in Goldfarb and Iyengar (2003), Halld´rsson and T¨ut¨unc¨u (2000), and T¨ut¨unc¨u and Koenig (2003). Finally, as mentioned above, for several special cases we obtain not just numerical solutions but also closed-form expressions for the optimal portfolio weights, which enables us to provide an economic interpretation of the eﬀect of aversion to uncertainty.

In order to understand the diﬀerence between the properties of the portfolio weights from the multi-prior approach and the mean-variance and Bayesian models, we apply the multi-prior model to two portfolio selection problems. In the ﬁrst application, we consider the problem of a fund manager allocating wealth across eight international equity indices and who is uncertain about the expected returns on these equity indices. In the second application, we consider the problem of a fund manager who is uncertain about the expected returns on two investable portfolios, HML and SMB, and also about the market-model generating returns on these portfolios. For both applications, we characterize the properties of the portfolio weights under the multi-prior approach and compare them to the standard mean-variance portfolio that ignores estimation error and the Bayesian portfolio that allows for estimation error but has a single prior or is uncertainty neutral. Even though the utility function under which each of these portfolios is selected is not the same, we report the out-of-sample performance of these portfolios so that prospective users of the model can evaluate the various models.

For the international data set, we ﬁnd that the portfolio weights using the multi-prior model are less unbalanced and vary much less over time compared to the mean-variance

portfolio weights. More importantly, the out-of-sample returns generated by the multiprior portfolio model have a substantially higher mean and lower volatility compared to the standard mean-variance portfolio strategy. The portfolio that incorporate aversion to uncertainty also outperforms the Bayes-diﬀuse-prior and the empirical Bayes-Stein portfolios. The explanation for this is that the uncertainty averse portfolio and the Bayesian portfolios consist of a weighted average of the mean-variance and minimum-variance portfolios, the uncertainty averse portfolio puts a higher weight on the minimum-variance portfolio, and in this data set the expected returns are so noisy that it is optimal to ignore estimates of expected returns all together. The second application considers the case where returns are assumed to be driven by a single-factor (CAPM) model, and the fund manager faces both parameter and model uncertainty when deciding how to allocate wealth to the FamaFrench HML and SMB portfolios and the market portfolio. In this case, we ﬁnd that the portfolio has a substantial proportion of wealth in the riskfree asset—typically more than the Bayesian model would suggest. Moreover, when the multi-prior portfolio allows for a small degree of uncertainty its out-of-sample Sharpe Ratio is greater than that of the mean-variance portfolio and the Bayesian portfolios.

The rest of the paper is organized as follows. In Section 2, we show how one can formulation the problem of portfolio selection for a fund manager who is averse to parameter and model uncertainty and illustrate this formulation through a simple example with only two risky assets. In Section 3, we discuss the relation of the multi-prior model to the traditional Bayesian approach for dealing with estimation error and we compare analytically the portfolio weights under the two approaches. Then, in Section 4, we illustrate the out-ofsample properties of the multi-prior model by considering two empirical portfolio selection settings: in the ﬁrst, the investor has to allocate wealth across eight international equitymarket indices, and in the second the investor has to allocate wealth to the market portfolio and two Fama-French portfolios, HML and SMB. Our conclusions are presented in Section 5. Proofs for propositions are collected in the Appendix.

# 2 Multi-prior approach to portfolio choice

This section is divided into two parts. In the ﬁrst, Section 2.1, we summarize the standard mean-variance model of portfolio choice where estimation error is ignored. In the second

part, Section 2.2, we show how this model can be extended to incorporate aversion to uncertainty about the estimated parameters and the return-generating model.

## 2.1 The classical mean-variance portfolio model

According to the classical mean-variance model (Markowitz (1952, 1959), Sharpe (1970)), the optimal portfolio of N risky assets, w, is given by the solution of the following optimization problem,

γ 2

maxw w µ −

w Σw, (1) where µ is the N-vector of the true expected excess returns, Σ is the N × N covariance matrix, 1N is a N-vector of ones and the scalar γ is the risk aversion parameter. The solution to this problem is

1 γ

Σ−1µ, (2)

w =

In the absence of a risk-free asset, the problem faced by the investor has the same form as (1) with the diﬀerence that µ represents the vector of true expected return and the portfolio weights has to sum to one. The solution in this case is

1 γ

Σ−1 µ − µ0 1N , (3)

w =

where µ0 is the expected return on the zero-beta portfolio associated with the optimal portfolio w and is given by

B − γ A

, (4)

µ0 =

where A = 1 NΣ−11N and B = µ Σ−11N.

A fundamental assumption of the standard mean-variance portfolio selection model in (1) is that the investor knows the true expected returns. In practice, however, the investor has to estimate expected returns. Denoting the estimate of expected returns by µˆ, the actual problem that the investor solves is

maxw w µ ˆ −

γ 2

w Σw. (5)

subject to w 1N = 1. The problem in (5) coincides with (1) only if expected returns are estimated with inﬁnite precision, that is, µˆ = µ. In reality, however, expected returns are

notoriously diﬃcult to estimate. As a result, portfolio weights obtained from solving (5) tend to consist of extreme positions that swing dramatically over time. Moreover, these optimal portfolios often perform poorly out of sample even compared to portfolios selected according to some simple ad hoc rules, such as holding the value-weighted or equally-weighted market portfolio.

## 2.2 Extension of the standard model to incorporate uncertainty aversion

To explicitly take into account that asset expected returns are estimated imprecisely, we introduce two new components into the standard mean-variance portfolio selection problem in (1). One, we impose an additional constraint on the mean-variance optimization program that restricts the expected return for each asset to lie within a speciﬁed conﬁdence interval of its estimated value. This constraint implies that the investor recognizes explicitly the possibility of estimation error; that is, the point estimate of the expected return is not the only possible value considered by the investor. Two, we introduce an additional optimization—the investor is allowed to minimize over the choice of expected returns and/or models subject to the additional constraint. This minimization over expected returns, µ, reﬂects the investor’s aversion to uncertainty (Gilboa and Schmeidler (1989)).

With the two changes to the standard mean-variance model described above, the multiprior model takes the following form in general:

subject to

maxw minµ w µ −

γ 2

w Σw, (6)

f(µ,µ,ˆ Σ) ≤  , (7) w 1N = 1, (8)

where f(·) is a vector-valued function, and is a vector of constants that reﬂects both the investor’s uncertainty and his aversion to uncertainty. The role of will be explained further below. As before, equation (8) constrains the weights to sum to unity in the absence of a riskfree asset; when a riskfree asset is available, this constraint can be dropped.

In the rest of this section we illustrate several possible speciﬁcations of the constraint given in (7) and their implications for portfolio selection.

### 2.2.1 Uncertainty about expected returns estimated asset-by-asset

We start by considering the case where f(µ,µ,ˆ Σ) has N components,

(µj − µˆj)2 σj2/Tj

fj(µ,µ,ˆ Σ) =

, j = 1,...,N, (9)

where Tj is the number of observations in the sample for asset j. In this case, the constraint in (7) becomes

(ˆµj − µj)2 σj2/Tj ≤ j, j = 1,...,N. (10)

The constraints (10) have an immediate interpretation as conﬁdence intervals. For instance, it is well known that if returns are assumed to be normally distributed then σµˆj−µj

√

Tj follows a normal distribution.7 Thus, the j in constraints (10) determines a conﬁdence interval. When all the N constraints in (10) are taken together, (10) is closely related to the probabilistic statement

j/

P(µ1 ∈ I1,...,µN ∈ IN) = 1 − p, (11)

where Ij, j = 1, ..., N, are intervals in the real line. Here p is a signiﬁcance level. For instance, if the returns are independent of each other and if pj is the signiﬁcance level associated with j, then the probability that all the N true expected returns fall into the N intervals, respectively, is 1 − p = (1 − p1)(1 − p2)···(1 − pN).8

While conﬁdence intervals or signiﬁcance levels are often associated with hypothesis testing in statistics, Bewley (1988) shows that they can be interpreted as a measure of the level of uncertainty associated with the parameters estimated. An intuitive way to see it is to envision an econometrician who estimates the expected returns for an investor. He can report to the investor his best estimates of the expected returns. He can at the same time report the uncertainty of his estimates by stating, say, the conﬁdence level of µj ∈ Ij for all j = 1, ..., j = N, is 95%.

- 7If σj is unknown then it follows a t-distribution with Tj − 1 degrees of freedom.
- 8When the asset returns are not independent, the calculation of the conﬁdence level of the event involves multiple integrals. In general, it is diﬃcult to obtain a closed-form expression for the conﬁdence level. The fact that the data for diﬀerent assets may be of diﬀerent lengths does not present a serious problem for the multivariate normal distribution setting as shown by Stambaugh (1997).

When viewed in isolation, (10) can have the simple interpretation as measure of uncertainty just described. When it is combined with the maxmin problem (6), i.e., when it is used in an investor’s portfolio selection problem, however, it also captures the investor’s aversion to uncertainty. For example, suppose that the standard practice of econometricians is to report 95% conﬁdence interval. If the investor has high uncertainty aversion, he could use an that corresponds to a 99% conﬁdence interval. In other words, by picking the appropriate j the investor can indicate the level of uncertainty he has about the estimate of the expected return of asset j as well as his level of uncertainty aversion.

To gain some intuition regarding the eﬀect of uncertainty about the estimated mean on the optimal portfolio weight, one can simplify the max-min portfolio problem, subject to the constraint in (10), as follows.

- Proposition 1 The max-min problem (6) subject to (8) and (10) is equivalent to the following maximization problem

maxw w (ˆµ − µadj) −

γ 2

w Σw , (12)

subject to (8), where µadj is the N-vector of adjustments to be made to the estimated expected return:

√

√

σ1 √

σN √

µadj ≡ sign(w1)

1,...,sign(wN)

N . (13)

T

T

The proposition above shows that the multi-prior model, which is expressed in terms of a max-min optimization, can be interpreted as the mean-variance optimization problem in

- (5), but where the mean has been adjusted to reﬂect the uncertainty about its estimated value. The term sign(wj) in (13) ensures that the adjustment leads to a shrinkage of the portfolio weights; that is, if a particular portfolio weight is positive (long position) then the expected return on this asset is reduced, while if it is negative (short position) the expected return on the asset is increased. In Section 2.2.3, we characterize the optimal solution for this problem.

### 2.2.2 Uncertainty about expected returns estimated jointly for all assets

Instead of stating the conﬁdence intervals for the expected returns of the assets individually as described in the previous section, one could do this jointly for all assets. Suppose that expected returns are estimated by their sample mean µˆ. If returns are drawn from a normal distribution, then the quantity

T(T − N) (T − 1)N

(ˆµ − µ) Σ−1(ˆµ − µ) (14)

has an χ2 distribution with N degrees of freedom.9 Let f = T(T(T−−1)NN)(ˆµ − µ) Σ−1(ˆµ − µ) and be a chosen quantile for the F-distribution. Then the constraint (7) can be expressed as

T(T − N) (T − 1)N

(ˆµ − µ) Σ−1(ˆµ − µ) ≤  . (15)

In other words, this constraint corresponds to the probabilistic statement

P

T(T − N) (T − 1)N

(ˆµ − µ) Σ−1(ˆµ − µ) ≤ = 1 − p,

for some appropriate level p.

The following proposition shows how the max-min problem (6) subject to (8) and (15) can be simpliﬁed into a maximization problem which is easier to solve, and how one can obtain an intuitive characterization of the optimal portfolio weights.

- Proposition 2 The max-min problem (6) subject to (8) and (15) is equivalent to the following maximization problem

maxw w µ ˆ −

γ 2

w Σw −

√

εw Σw, (16)

subject to w 1N = 1, where ε ≡ T (T(T−−1)NN) . Moreover, the expression for the optimal portfolio weights can be written as:

√ε γσP∗

  1

 

 µˆ −

 , (17)

B − γ 1 +

1 γ

w∗ =

Σ−1

1N

√ε γσP∗

A

1 +

9It follows an F distribution with N and T −N degrees of freedom (Johnson and Wichern, 1992, p. 188) if Σ is not known.

where A = 1 N Σ−1 1N, B = µˆ Σ−1 1N, and σP∗ is the variance of the optimal portfolio that can be obtained from solving the polynomial equation (A11) in Appendix A.

We can now use the expression in (17) for the optimal weights to interpret the eﬀect of parameter uncertainty. Note that as ε → 0, that is either → 0 or T → ∞, the optimal weight w∗ converges to the mean-variance portfolio10

w∗ =

=

1 γ

B − γ A

Σ−1 µ ˆ −

1N

1 γ

Σ−1 µ ˆ − µ01N , (18)

where B−γ

A = µ0 is the expected return on the zero-beta portfolio associated with w∗ deﬁned in equation (3). Thus, in the absence of parameter uncertainty the optimal portfolio reduces to the mean-variance weights. On the other hand, as ε → ∞ the optimal portfolio converges to

1 A

w∗ =

Σ−11N, (19)

which is the minimum-variance portfolio. These results suggest that parameter uncertainty shifts the optimal portfolio away from the mean-variance weights toward the minimumvariance weights.

### 2.2.3 Uncertainty about expected returns estimated for subsets of assets

In Section 2.2.1 we described the case where there was uncertainty about expected returns that were estimated individually asset-by-asset, and in Section 2.2.2 we described the case where the expected returns were estimated jointly for all assets. Stambaugh (1997) provides motivation for why one may wish to do this – for example, the lengths of available histories may diﬀer across the assets being considered. In this section, we present a generalization that allows the estimation to be done separately for diﬀerent subclasses of assets, and we show that this generalization uniﬁes the two speciﬁcations described above.

10In taking these limits, it is important to realize that σP∗ also depends on the weights. In order to obtain the correct limits, it is useful to look at equation (A11), which characterizes σP∗ .

Let Jm = {i1,...,iNm}, m = 1, ..., M, be M subsets of {1,...,N}, each representing a subset of assets. Let f be a M-valued function with

Tm(Tm − Nm) (Tm − 1)Nm

(ˆµJm − µJm) Σ−1

fm(µ,µ,ˆ Σ) =

Jm(ˆµJm − µJm). (20)

Then (15) becomes

Tm(Tm − Nm) (Tm − 1)Nm

(ˆµJm − µJm) Σ−1

Jm(ˆµJm − µJm) ≤ m, m = 1,...,M. (21)

Just as in the earlier speciﬁcations, these constraints corresponds to the probabilistic statement

P (X1 ∈ I1,...,XM ∈ IM) = 1 − p,

where Xm, m = 1, ..., M, are sample statistics deﬁned by the left hand side of the inequalities in (21).

The case where Jm, m = 1, ..., M, do not overlap with each other and investors have access to a risk-free asset is of particular interest since we can obtain an analytic characterization of the portfolio weights, as the following proposition shows.

- Proposition 3 Consider the case of M non-overlapping subsets of assets and assume f in (7) is an M-valued function expressing the uncertainty aversion of the investor in each subset of assets. Then, if the investor has access to a risk-free asset, the optimal portfolio is given by the solution to the following system of equations:

 1 −

√εm g(w−m) Σ−1 m g(w−m)

wm = max

,0

  1

Σ−1

m g(w−m) (22)

γ

for m = 1,...,M, where εm ≡ T(Tm−1)Nm

m(Tm−Nm), w−m represents the weights in the assets not in subclass m, Σm is the variance-covariance matrix of the asset in subclass m, and

g(w−m) = µˆm − γΣm,−mw−m, m = 1,...M (23)

with Σm,−m the matrix of covariances between assets in class m and assets outside class m.

If the number of subclasses M is equal to the number of assets N, the model reduces to the one discussed in Section 2.2.1. Similarly, if there is only one subclass of assets, (M = 1)

the model reduces to the one studied in Section 2.2.2. The following two corollaries formalize this relation and characterize the optimal portfolios.

- Corollary 1 If the number of subclasses M is equal to the number of assets N and there is a risk-free asset, the optimal portfolio in problem (6) is given by solving the following system of simultaneous equations

wi = max[|g(w−i)| −

√εi,0]

1 γσi

sign[g(w−i)], i = 1,2,...,N (24)

where εi = i

T , w−i are the N − 1 portfolio weights on the assets other than i,

g(w−i) = µˆi − Σi,−iw−i and Σi,−i is the i-th row of the variance-covariance matrix with the i-th element removed.

- Corollary 2 If there is only one subclass of assets, that is M = 1, then in the presence of a risk-free asset, the optimal portfolio is given by

√ε µˆ Σ−1µˆ

w = max 1 −

,0

1 γ

Σ−1µ,ˆ where ε ≡

(T − 1)N T(T − N)

. (25)

### 2.2.4 Uncertainty about the return-generating model and expected returns

In this section, we explain how the general model developed in Section 2.2.3 where there are M subsets of assets can be used to analyze situations where investors rely on a factor model to generate estimates of expected return and are averse to both the estimated expected returns on the factor portfolios and the model used to generate the expected returns on investable assets.

To illustrate this situation, consider the case of a market with N risky asset in which an asset pricing model with K factors is given. Denote with rat the N × 1 vector of excess returns of the non-benchmark assets over the risk-free rate in period t. Similarly, denote by rft the excess return over the benchmark assets. The mean and variance of the assets and factors are:

Σaa Σaf Σfa Σff

µa µf

µ =

, Σ =

. (26)

We can always summarize the mean and variance of the assets by the parameters of the following regression model

rat = α + βrft + ut, cov(ut,u t ) = Ω, (27)

where α is a N ×1 vector, β is a N ×K matrix of factor loadings, and ut is a N ×1 vectors of residuals with covariance Ω. Hence, the mean and variance of the returns can always be expressed as follows

µ =

α + βµf µf

, Σ =

βΣffβ + Ω βΣff Σffβ Σff

. (28)

An investor who is averse to uncertainty about both the expected returns on the factors and the model generating the returns on the assets will solve the following problem. Deﬁning w ≡ (wa,wf) to be the (N + K) × 1 vector of portfolio weights, the investor’s problem is:

γ 2

maxw µmin

w Σw, (29)

a,µf w µ −

subject to

(ˆµa − µa) Σ−1

aa (ˆµa − µa) ≤ a, (30) (ˆµf − µf) Σ−1

ff (ˆµf − µf) ≤ f. (31) Equations (30) and (31) capture parameter uncertainty over the estimate of the expected returns. If investors use the asset pricing model to determine the estimate of µˆa, then µˆa = βµf and equation (30) can be interpreted as a multi-prior characterization of model uncertainty. Setting a = 0 corresponds to imposing that the investor believes dogmatically in the model.11

From Proposition 3 the solution to this problem is given by the following system of equations

 1 −

  1

√

a

Σ−1

wa = max

,0

aa g(wf), (32)

γ

g(wf) Σ−1

aa g(wf)

 1 −

  1

√

f

Σ−1

wf = max

,0

ff h(wa), (33)

γ

h(wa) Σ−1

ff h(wa)

11To be precise, the interpretation of equation (30) as a characterization of model uncertainty is true only if f = 0. To see this, note that when µˆa = βµf, µˆa − µa = β(ˆµf − µf) − α. Therefore, unless µf = µˆf the diﬀerence µˆa − νa does not represent Jensen’s α.

where

- g(wf) = µˆa − γΣafwf, (34)
- h(wa) = µˆf − γΣfawa. (35)

To understand the structure of the solution to this problem we consider the case where there are two assets and one factor. The parameters for these assets are summarized in Table 1 and the optimal portfolio weights are reported in Table 2.12 Each panel corresponds to a diﬀerent level of uncertainty f about the factor. Within each panel of the table, each row represent a diﬀerent level of uncertainty a about the asset. A clear pattern emerges from the portfolio weights reported in the table. First, when f = 0 then for all values of

a > 0 the investor is more uncertain about the assets than about the factor, and hence will hold 100% of his wealth in the factor portfolio. Second, given a certain level of uncertainty about the factor (i.e. keeping ﬁxed f > 0), as uncertainty in the asset estimate increases the holdings of the risky non-benchmark assets decrease and the holding of the factor portfolio increases. Third, given a certain level of uncertainty about the assets (i.e., keeping ﬁxed

a), as f increases, the holdings of risky non-benchmark assets increase and the holding of the factor decreases. These results are intuitive and suggest that the more uncertain is the estimate of the expected return of an asset the less an investor is willing to invest in that asset. Obviously, the uncertainty in the assets and the factors are interrelated and it is ultimately the relative level of uncertainty between the two classes of asset that determines the ﬁnal portfolio.

# 3 Comparison with other approaches to estimation error

In this section, we relate the multi-prior framework for portfolio choice in the presence of parameter and model uncertainty to other approaches considered in the literature, and in particular, to portfolios that use the traditional Bayesian approach. We compare the portfolio weights from the multi-prior model to the following: (i) the standard mean-variance portfolio that ignores estimation error, (ii) the minimum-variance portfolio, (iii) the portfolio based on Bayes-diﬀuse-prior estimates as in Bawa, Brown, and Klein (1979), and (iv) the

12The parameters are chosen to match the results we would obtain by estimating a regression of the monthly returns on the Fama-French portfolios HML and SMB on the Market from July 1926 to December

2002. More details on this data set are provided in section 4.2.

portfolio based on the empirical Bayes-Stein estimator, as described in Jorion (1985, 1986). In this section, the comparison is done in terms of the theoretical foundations of the models and their implications for portfolio weights, while in Section 4 this comparison is undertaken empirically using two diﬀerent data sets and the comparison set includes also the weights obtained by using the data-and-model approach of P´stor (2000).

## 3.1 A summary of the traditional Bayesian approach

It is useful to begin with a brief summary of the traditional Bayesian approach. Let U(R) be the utility function, where R is the return from the investment, and g(R|θ) the conditional density (likelihood) of asset returns given parameter θ. In the setting of this paper, θ is the vector of the expected returns of the risky assets. More generally, it can include the covariances of the asset returns. If the parameter θ is known, then the conditional expected utility of the investor is

E[U(R)|θ] = U(R)g(R|θ)dR. (36)

In practice, however, the parameter θ is often unknown and needs to be estimated from data, i.e., there is parameter uncertainty. In the presence of such parameter uncertainty, Savage’s expected utility approach is to introduce a conditional prior (posterior) p(θ|X), where X = (r1,...,rT) is the vector of past returns, such that the expected utility is given by

E[U(R)|X] = E [E[U(R)|θ]|X] = U(R)g(R|θ)p(θ|X)dRdθ. (37)

Let π(θ) is the unconditional prior about the unknown parameter. Then the posterior density given X is

T t=1 g(rt|θ)π(θ) T t=1 g(rt|θ)π(θ)dθ

p(θ|X) =

, (38)

and the predictive density, given X, is

T t=1 g(rt|θ)π(θ) T t=1 g(rt|θ)π(θ)dθ

g(R|X) = g(R|θ)p(θ|X)dθ = g(R|θ)

dθ. (39)

Using the predictive density, the expected utility of the investor is given by

E[U(R)|X] = U(R) g(R|θ,X)p(θ|X)dθ dR = U(R)g(R|X)dR. (40)

Thus the key to the Bayesian approach is the incorporation of prior information and the information from data in the calculation of the posterior and predictive distributions. The eﬀect of information on the investor’s decision comes through its eﬀect on the predictive distribution.

The foundation for the Bayesian approach was provided by Savage (1954). Early applications of this approach can be found in Klein and Bawa (1976), Jorion (1985, 1986). More recent applications include P´stor (2000) and P´stor and Stambaugh (2000) who, in addition to parameter uncertainty, consider also model uncertainty.

## 3.2 Comparison of the multi-prior approach with Bayesian approach

The decision-theoretic foundation of the multi-prior approach is laid by Gilboa and Schmeidler (1989). Equally well-founded axiomatically, the most important diﬀerence between the Bayesian approach and the multi-prior approach is that in the Bayesian approach the investor is implicitly assumed to be neutral to parameter and/or model uncertainty, while in the multi-prior approach, the investor is averse to that uncertainty.

That in the Bayesian approach the investor is uncertainty neutral is best seen through equation (40). The middle expression in the equation suggests that parameter and/or model uncertainty enters the investor’s utility through the posterior p(θ|X), which can aﬀect the investor’s utility only through its eﬀect on the predictive density g(R|X). In other words, as far as the investor’s utility maximization decision is concerned, it does not matter whether the overall uncertainty comes from the conditional distribution g(R|θ) of the asset return or from the uncertainty about the parameter/model p(θ|X), as long as the predictive distribution g(R|X) is the same. In other words, if the investor were in a situation where there is no parameter/model uncertainty, say, because the past data X could be used to identify the true parameter perfectly, and the distribution of asset returns is characterized by g(R|X), then the investor would feel no diﬀerent. In particular, there is no meaningful separation of risk aversion and uncertainty aversion. In this sense, we say that the investor is uncertainty neutral.

In the multi-prior framework, the risk (the conditional distribution g(R|θ) of the asset returns is treated diﬀerently from the uncertainty about the parameter/model of the data generating process. For example, in the portfolio choice problem described by equations

- (6)-(8), the risk of the asset returns is captured by Σ which appears in equation (6). The uncertainty about the unknown mean return vector, µ, is however captured by the constraint
- (7). The two are further separated by the minimization over µ subject to the constraint

(7). As a result, the investor is no longer uncertainty neutral in this approach.

## 3.3 Analytic comparison of the portfolio weights from the various models

In this section, we compare analytically the portfolio weights from the multi-prior model to those obtained when using traditional Bayesian methods to deal with estimation error.13 We start by describing the portfolio obtained when using the empirical Bayes-Stein estimator. The Bayes-diﬀuse prior portfolio is then obtained as a special case of this portfolio, while the mean-variance portfolio and the minimum-variance portfolio are discussed as limit cases of the traditional Bayesian models and also the multi-prior model.

The problem facing a Bayesian investor is to estimate the N-dimensional vector of means µ from the i.i.d. population yt ∼ N(µ,Σ), t = 1,...,T. The key result in Jorion (1986) can be summarized as follows. Assume the following three conditions: (i) Investors have an informative prior on µ of the form

- 1

- 2

p(µ|µ,ν¯ µ) ∝ exp −

(µ − µ¯1N) (νµ Σ−1)(µ − µ¯1N) , (41)

with µ¯ being the grand mean and νµ giving an indication of prior precision (or tightness of the prior); (ii) Investors have diﬀuse prior on the grand mean µ¯; (iii) The density p(νµ|µ,µ,¯ Σ) is a Gamma function. Then, the predictive density for the returns p(r|y,Σ,νµ), conditional on Σ and the precision νµ is a multivariate normal with predictive Bayes-Stein mean, µBS, equal to

µBS = (1 − φBS)ˆµ + φBS µMIN 1N, (42)

13The Bayes-Stein approach to minimizing the impact of estimation risk on optimal portfolio choice involves “shrinking” the sample mean towards a common value or, as it is usually called, a grand mean. Stein (1955) and Berger (1974) developed the idea of shrinking the sample mean towards a common value and showed that these kind of estimators achieve uniformly lower risk than MLE estimator (where here risk is deﬁned as the expected loss, over repeated samples, incurred by using an estimator instead of the true parameter). The results from Stein and Berger can be interpreted in a Bayesian sense where the decisionmaker assumes a prior distribution for the common value and for the precision of the estimation procedure. This is what deﬁnes a Bayes-Stein estimator. An Empirical Bayes estimator is a Bayes estimator where the grand mean and the precision are inferred from the data.

where µˆ is the sample mean, µMIN is the minimum-variance portfolio,

φBS =

νµ T + νµ

and covariance matrix

N + 2 (N + 2) + T(ˆµ − µMIN 1N) Σ−1(ˆµ − µMIN 1N)

=

, (43)

1 T + νµ

V [r] = Σ 1 +

1N1 N 1 NΣ−11N

νµ T(T + 1 + νµ)

+

. (44)

Note that the case of zero precision (νµ = 0) corresponds to the Bayes-diﬀuse-prior case considered in Bawa, Brown, and Klein (1979) in which the sample mean is the predictive mean but the covariance matrix is inﬂated by the factor (1+1/T). Finally, observe that for νµ → ∞ the predictive mean is the common mean represented by the mean of the minimum variance portfolio.

We are now ready to determine the optimal portfolio weights using the Bayes-Stein estimators. Let us assume that we know the variance-covariance matrix and that only the expected returns are unknown. In the case where a risk free asset is not available, we know that the classical mean-variance portfolio is given by (3). Substituting the empirical BayesStein (BS) estimator µBS in (3), one can show that the optimal weights can be written as follows:

wBS = φBS wMIN + (1 − φBS)wMV , (45) where the minimum-variance portfolio weights, which ignore expected returns altogether, is

1 A

Σ−11N, (46)

wMIN =

and the mean-variance portfolio weights formed using the maximum-likelihood estimates of the expected return are

1 γ

Σ−1 (ˆµ − µˆ0 1N). (47)

wMV =

We now compare the mixture portfolio (45) obtained from a Bayes-Stein estimator with the optimal portfolio derived from the multi-prior (MP) approach that incorporates aversion to parameter uncertainty and is given in equation (17). After some manipulation, the optimal portfolio for an investor who is averse to parameter uncertainty can be written

as

wMP = φMP wMIN + (1 − φMP)wMV , (48) where

(T−1)N T(T−N)

√ε γσ∗

φMP( ) =

=

, (49)

P + √ε

P + T (T(T−−1)NN)

γσ∗

and wMIN and wMV are deﬁned in (46) and (47), respectively.

Comparing the weights in equation (45) that are obtained using a Bayes-Stein estimator to the weights in equation (48) obtained from the multi-prior model, we notice that both methods shrink the mean-variance portfolio toward the minimum-variance portfolio, which is the portfolio that essentially ignores all information about expected returns. However, the magnitude of the shrinkage is diﬀerent, that is, φBS = φMP( ). In the next section, where we implement these diﬀerent portfolio strategies using real-world data, we will ﬁnd that the shrinkage factor from the multi-prior approach is much greater than that for the empirical Bayes-Stein portfolio; that is, for reasonable values of , φMP( ) > φBS.

So far, we have considered the following two cases: one, where the investor uses classical maximum-likelihood estimators to estimate expected returns and then accounts for model uncertainty in obtaining the weights in equation (48), and two, where the investor uses Bayesian methods for estimating expected returns but ignores the possibility that these estimates are uncertain, which leads to the portfolio weights in (45). But, one could just as well have a third case where the estimation is done using Bayesian methods and the investor allows for parameter uncertainty.14 In this case, the optimal portfolio weights are given by the following expression.

wMPBS = φMP wMIN + (1 − φMP)wBS, (50)

where the minimum-variance-portfolio, wMIN, and the Bayesian portfolio, wBS, are deﬁned in (46) and (45), respectively. Observe that the expression in (50) is similar to that in (48) but where wBS replaces wMV ; that is, the eﬀect of uncertainty is to shrink the portfolio that is now obtained using Bayesian estimation methods, wBS, toward wMIN. Notice that in the limiting case where the investor is neutral toward uncertainty, setting = 0 in (50),

14In this comparison, the Bayesian approach is interpreted narrowly as an estimation technique rather than a decision-theoretic approach.

which leads to φMP = 0, implies that the optimal portfolio reduces to wBS. This is the sense in which the portfolio obtained using Bayesian estimation methods is nested in the multi-prior approach.

One can also view the expression in (50) as being similar to that in (45), but where the shrinkage factor consists not just of an adjustment because one is using Bayesian estimation but also because the investor is averse to uncertainty. To see this, substitute in (50) the expression for wBS in (45), to get

wMPBS = φBSMP wMIN + 1 − φBSMP wML, (51)

where the shrinkage factor is now given by

φBSMP = φMP + φBS − φMP φBS. (52)

This expression again shows that if the investor is uncertainty neutral ( = 0), then φMP = 0 and the optimal portfolio is the Bayesian portfolio wBS. If, on the other hand, there is zero precision about the prior mean (νµ = 0), then φBS = 0 and the optimal portfolio is wMP. And, only in the case where the investor is both uncertainty neutral and has zero precision about the prior mean is it optimal to hold the standard mean-variance portfolio, wMV , which is obtained using maximum-likelihood estimates of the mean.

Of course, from equation (52) it is clear that φBSMP > φBS and φBSMP > φMP, so the investor who is using Bayesian estimation methods and is averse to uncertainty will shrink his portfolio much more toward the minimum-variance portfolio, wMIN, than either the investor who uses Bayesian estimation methods but is uncertainty averse, or the investor who is uncertainty averse but has a diﬀuse prior so that he is using maximum-likelihood estimates.

# 4 Empirical applications of the multi-prior approach

In this section, we show how to apply the multi-prior approach to portfolio selection. Our goal in this section is (i) to demonstrate how the multi prior approach can be implemented in practice and (ii) to compare the portfolio recommendations from this approach to other procedures commonly used, with a particular emphasis on the Bayesian approach with model uncertainty introduced in P´stor (2000).

We consider two versions of the model. First, in Section 4.1 we illustrate the model described in Section 2.2.2, where the expected returns on all assets are estimated jointly and there is no riskfree asset. Then, in Section 4.2, we illustrate the model described in Section 2.2.3 where there is both uncertainty about expected asset returns and the factor model generating these returns and a riskfree asset is available. For the ﬁrst application, we use returns on eight international equity indices. For the second application, we consider returns on a factor portfolio, which is the excess return on the US market portfolio (deﬁned as the value-weighted return on all NYSE, AMEX and NASDAQ stocks, minus the onemonth Treasury bill rate) and the Fama-French portfolios, HML and SMB. Details of these two applications are given below.

## 4.1 Uncertainty about expected returns: International data

For our ﬁrst empirical illustration we consider allocating wealth over eight international equity indices whose returns are computed based on the month-end US-dollar value of the equity index for the period January 1970 to July 2001. The equity indices are for Canada, Japan, France, Germany, Italy, Switzerland, United Kingdom, United States. Data are from MSCI (Morgan Stanley Capital International). The data set is similar to the one used by De Santis and Gerard (1997) but spans for a longer time period than theirs. Summary statistics for the indexes of the eight countries as well as for the MSCI world index are provided in Table 3.

We assume that there is no risk-free asset and that the investor estimates the expected returns jointly over portfolio by expressing uncertainty over the whole set of assets, as described in Section 2.2.2. Using this model, we compute the mean-variance portfolios that account for diﬀerent degrees of uncertainty in the statistical estimate ( ) about the expected returns. We also compute (i) the standard mean-variance portfolio that ignores estimation error, (ii) the minimum-variance portfolio, and (iv) the portfolio based on BayesStein estimators, as described in Jorion (1985, 1986). From the result in Section 2.2.2 we know that the resulting portfolio is a combination of the minimum variance portfolio and the mean-variance portfolio.

To assess the performance of the diﬀerent portfolio models, we determine the weights from each model based on a window of 60 months and then calculate the return from holding

this portfolio in the 61st month. We repeat this for the entire data set and compute the average out-of sample means, volatilities and Sharpe ratios of each strategy. For each of the portfolio models, we consider two cases: one, where short-selling is allowed, and the other where short-selling is not allowed.

In our analysis, we set T = 60 because the estimation is done using a rolling-window of 60 months and we set N = 8 because there are eight country-indexes. Under the assumption that the returns are normally distributed, if µˆ is taken to be the sample average of the returns, the quantity T(T(T−−1)NN) (ˆµ − µ) Σ−1(ˆµ − µ) is distributed as an F8,52. For reference purpose, we recall that the 95-percentile of an F8,52 corresponds to = 2.122, while the 99-percentile corresponds to = 2.874.15

The results of our analysis are reported in Panel A of Table 4. Compared to the meanvariance strategy in which historical mean returns µˆ are taken to be the estimator of expected returns µ, the portfolios constructed using the model that allows for parameter uncertainty exhibit uniformly higher means and lower volatility.

Notice from Panel A that the case of = 0 corresponds to the mean-variance portfolio while the case of → ∞ corresponds to the minimum-variance portfolio, as discussed in the previous section. Both the Bayes-diﬀuse-prior and the empirical Bayes-Stein portfolios show lower mean and higher variance than any of the portfolios that account for uncertainty aversion. To understand the reason for this, observe that for the case of the Bayes-diﬀuse prior portfolios parameter uncertainty is dealt with by inﬂating the variance-covariance matrix by the factor 1+ T1 (see Bawa, Brown, and Klein (1979)) while still using the historical mean as a predictor of expected returns. For large enough T (60 in our case), this correction to the variance-covariance matrix has only a mild eﬀect on performance. The under-performance of the empirical Bayes-Stein portfolio is due to the fact that this estimation model still puts too much weight on the estimated expected returns, and consequently, does not shrink the portfolio weights suﬃciently toward the minimum-variance portfolio relative to the portfolio that incorporates model uncertainty. The weighting factor assigned by the empirical BayesStein model to the minimum-variance portfolio over the out of sample period averages to

15Alternatively, selecting = 2 implies a 93.53%-conﬁdence interval, while = 3 corresponds to 99.24%conﬁdence interval.

0.6582, while this factor for the model that accounts for parameter uncertainty is 0.8741 when = 1 and, as shown in the previous section, this factor is increasing with . 16

Recall from equations (45) and (48) that the optimal portfolio of the investor can also be interpreted as one that is a weighted-average of the standard mean-variance portfolio and the minimum-variance portfolio, with the mean-variance portfolio shrinking toward the minimum-variance portfolio as uncertainty increases. In Figure 2 we present the weights assigned by the investor to the minimum-variance portfolio when he is uncertain about expected returns, φMP( = 1), and a second case where the level of uncertainty is higher, φMP( = 5). We also provide the shrinkage factor for the empirical Bayes-Stein approach, φBS. From the ﬁgure, we see that as increases the shrinkage toward the minimum-variance portfolio increases; moreover, the shrinkage factor ﬂuctuates much less for higher levels of uncertainty.

To analyze the eﬀect of uncertainty aversion on the individual weights in the risky portfolio, we report in Panel A of Figure 1 the percentage weight allocated to the US index from January 1975 to July 2001.17 The dashed line refers to the percentage of wealth allocated to the US index implied by the mean-variance portfolio implemented using historical estimates. The other two lines refer to portfolios obtained by incorporating aversion to parameter uncertainty. Two levels of aversion to uncertainty are considered. The dash-dotted line ( = 1) are the portfolio weights obtained for a degree of uncertainty expressed roughly by the 55% conﬁdence interval for an F8,52 centered around the sample mean, while the solid line ( = 3) are portfolio weights obtained assuming uncertainty about expected returns is given by the 99% conﬁdence interval. We ﬁnd that portfolio weights from the optimization incorporating parameter uncertainty has less extreme positions and the portfolio weights vary much less over time compared to the weights for the classical mean-variance portfolio.

- A higher means a higher conﬁdence interval and, consequently, more aversion to uncertainty in the estimates. As a consequence, the higher is , the less extreme are the portfolio weights.

In the results described above, investors were permitted to hold short positions. We now repeat the analysis but impose a further condition on the multi-prior model that short-sales

- 16For reference purposes, the number in parenthesis appearing in the table refer to the percentageconﬁdence interval implied by diﬀerent value of and computed from a F8,52 distribution.
- 17Estimates of the turnover in the composition of the standard mean-variance optimal portfolio as a function of the estimation error are given in Chopra (1993).

are not allowed. Formally, the problem we now solve is the same as the one in Section 2.2.2, but with the additional constraint that short sales are not allowed: w ≥ 0N.

The results of this analysis are reported in Panel B of Table 4. As in Panel A, this panel compares the out-of-sample mean return, volatility and Sharpe ratio obtained from the multi-prior model with alternative portfolio strategies. We ﬁnd that the portfolio strategies that incorporate parameter uncertainty achieve a higher mean and lower volatility than the mean-variance portfolio and the Bayes-diﬀuse-prior portfolio. The relatively poor performance of the empirical Bayes-Stein portfolio is again due to the relatively low weight this approach assigns to the minimum-variance portfolio, as discussed above.18

It is well known (Frost and Savarino (1988)) and Jagannathan and Ma (2003)) that imposing a short-selling constraint improves the performance of the mean-variance portfolio. This result can be conﬁrmed by comparing Panel B of Table 4 with Panel A. Both the meanvariance portfolio and the Bayesian portfolios show a higher Sharpe ratio in the case in which short selling is not allowed. It is also interesting to note that the out-of sample performance of the portfolio constructed by incorporating parameter uncertainty is less sensitive to the introduction of a short sale constraint. For these portfolios, the diﬀerence in Sharpe ratios between Panels A and B is much less dramatic than for the case of the mean-variance portfolio or for the Bayesian portfolios. This is because the eﬀect of parameter uncertainty, as we saw previously for the case in which short-sales were allowed, is to reduce extreme positions, producing the same eﬀect on the portfolio as a constraint on short selling. This intuition is conﬁrmed by noting, for example, that for greater than 3 (99-percentile of an F8,52) the Sharpe ratios for the parameter uncertainty portfolios in Panel A of Table 4 are larger than the Sharpe ratio for the constrained mean-variance portfolio in Panel B. Though the eﬀect of incorporating parameter uncertainty is similar to the eﬀect of constraining short sales, there is one important diﬀerence: the “constraints” imposed by incorporating parameter uncertainty are endogenous rather than exogenous, and consequently, if it is optimal to have short positions in some assets these are not ruled out a priori.

18Note however that in Panels A and B of Table 4 the portfolio with the highest mean and lowest volatility is the minimum-variance portfolio (or, equivalently, the portfolio for a very high level uncertainty ( = ∞). The reason for this is that in the particular data that we are using, returns are so noisy that expected returns are estimated very imprecisely, and hence, one is best oﬀ ignoring them all together. However, simulations reveal that when data is less noisy, then it will no longer be optimal to hold only the minimum-variance portfolio.

We report also the portfolio weights over time when short sales are prohibited, just as we did for the case without shortsale constraints. In Panel B of Figure 1, we report the percentage weight allocated to the US index from January 1975 to July 2001. As in Panel A of Figure 1, the dashed refers to the mean-variance portfolio obtained using historical estimates while the other two lines refers to weights obtained from portfolios that allow for parameter uncertainty with = 1 (dash-dotted line, low uncertainty) and

= 3 (solid line, higher uncertainty). Note how the introduction of parameter uncertainty reduces the “bang-bang” nature displayed by the mean-variance portfolio weight, and thus, incorporating parameter uncertainty reduces turnover.

## 4.2 Uncertainty about expected returns and factor model: Domestic data

In this section we implement the model discussed in Section 2.2.4 in which assets are assumed to follow a factor structure and investors are uncertain about the validity of the returngenerating model. The assets we consider for this exercise are the Fama-French portfolio, HML and SMB. The former is a zero-cost portfolio that is long in high book-to-market stocks and short in low book-to-market stocks. The latter is a zero-cost portfolio that is long in small stocks and short in big stocks. We use a series of monthly returns on HML and SMB starting in July 1926 until December 2002. As a factor we use the excess return on the market, deﬁned as the value-weighted return on all NYSE, AMEX and NASDAQ stocks (from CRSP) minus the one-month Treasury bill rate (from Ibbotson Associates).19 In this application we allow for the existence of a risk-free asset.

In each month, the investor uses the most recent 120 months of data to estimate the moments of the asset and to form portfolios.20 These estimates and the resulting portfolios are then revised a month later when the most recent data point is added to the estimation period and the most distant data point is dropped. We consider two possible scenarios: in the ﬁrst, the investor takes as a reference for the estimate µˆa of the expected return on the asset the MLE estimate (i.e. the sample average) but allows for uncertainty around this estimate as indicated by the parameter a. In the second case, the investor forms his expectation about µˆa by relying on the CAPM and therefore, in each month estimates

19The data are taken from Kenneth French’s website. 20We use a 120-month window to compare the portfolios from the multi-prior model with the portfolios

obtained by Pa´stor (2000).

µˆa = βaµˆf where βa is the 2 × 1 vector of betas. In this case too, the investor allows for uncertainty about the estimate from the model, captured by the parameter a. In both cases, the reference estimate for the expected return on the factor µˆf is represented by the MLE estimate. However, the investor allows for uncertainty about this estimate too, as reﬂected by the uncertainty aversion parameter f. When a = 0 and f = 0, the investor’s portfolio will be the mean-variance portfolio if the reference estimator for µˆa is the MLE estimator, while it will be the market portfolio, if the reference estimator for µˆa is obtained through the CAPM. This case would correspond to an investor who believes dogmatically in the CAPM.

Figure 3 reports the evolution of the portfolio in SMB, HML, Market and the riskfree asset for an investor who estimates expected returns using the maximum-likelihood estimator and historical returns. In each plot, we report the portfolio holdings for diﬀerent levels of uncertainty over the estimate of the expected return of the assets ( a) and over the estimate of the expected return of the factors ( f). For comparison purposes the solid line in each ﬁgure represents the portfolio which will be chosen by using a MLE estimator.21

The ﬁgures conﬁrms the properties of the multi-prior portfolios described in section 2.2.4. As the uncertainty about the estimate of the expected return in an asset increases, the optimal holdings in that asset decrease. This can be seen in each ﬁgure by comparing the portfolio holdings for diﬀerent values of a. For the assets (HML and SMB—in Panels A and

- B) it is always the case that higher levels of a lead to lower portfolio holdings. Similarly for the factor (MKT—in Panel C), higher level of f lead to lower holding of the market. In interpreting the portfolio holdings reported in Figure 3 it is important to bear in mind that

it is the relative uncertainty a vs. f that ultimately determine the optimal portfolio in a multi-prior setting. This explain why, for example, when investors are uncertain about the market ( f = 2) they decide to hold more of the asset (as in Panels A and B) or, equivalently, why higher uncertainty over the assets ( a) induces more holdings of the market (as in Panel

- C).

Figure 4 repeats the above analysis by assuming that expected returns of assets are generated by a single-factor (CAPM) model. In this case note that the portfolio is almost always entirely invested in the market (as it should be). The only case in which this does

21This portfolio corresponds to a portfolio chosen by a Bayesian with inﬁnite conﬁdence in the data.

not happen is when investors are uncertain about the factor ( f = 2) and inﬁnitely conﬁdent about the estimate of the individual assets ( a = 0), as is shown in Figure 4.

For completeness, we report the Sharpe Ratios of various portfolio strategies when the fund manager can invest in the market (factor) portfolio and the HML and SMB portfolios. In addition to the mean-variance portfolio, the minimum-variance portfolio (of only risky assets), and the Bayes-Stein Bayesian portfolio, we give the Sharpe ratio for the single-prior “model-and-data” approach in P´stor (2000) and the portfolio weights from the multi-prior model. The Bayesian prior is represented by the value ω, where ω = 0 implies no conﬁdence in the model, while ω = 1 implies 100% conﬁdence in the model.22 The multi-prior model assumes that an investor uses a prior belief ω in determining the “reference” estimator for µa but allows for multiple priors as represented by a > 0 and f > 0.

In Table 5 we consider the case in which ω = 0 and in Table 6 we consider the case in which ω = 1. From the two tables we observe that the multi-prior portfolio with small values of a > 0 and f > 0 has a Sharpe Ratio that is greater than that of the meanvariance portfolio and the Bayesian portfolios. However, for larger values of a and f, the performance of the portfolio from the multi-prior model declines. The minimum-variance portfolio has quite a high Sharpe Ratio and for only a few values of a and f for the case in which ω = 0 does the multi-prior model outperform the minimum-variance portfolio, while the mean-variance and Bayesian models never outperform it.

# 5 Conclusion

Traditional mean-variance portfolio optimization assumes that the parameters that the expected returns used as inputs to the model and obtained using maximum likelihood estimation are known with perfect precision. In practice, however, it is extremely diﬃcult to estimate expected returns precisely. And, portfolios that ignore estimation error have very poor properties: the portfolio weights have extreme values and ﬂuctuate dramatically over time. The Bayesian approach that is traditionally used to deal with estimation error assumes that investors have only a single prior and that they are neutral to uncertainty.

22P´stor (2000) considers also other values of ω; we have not reported the Sharpe Ratios for these values of ω because for those values Pastor’s model is not strictly nested in our model. The results for these other values of ω are available on request.

In this paper, we have shown how one can extend the classical mean-variance portfolio optimization model to allow for the possibility of multiple priors and to incorporate aversion to uncertainty about the estimated expected returns and the underlying return-generating model. The multi-prior approach relies on imposing constraints on the mean-variance portfolio optimization program, which restrict each parameter to lie within a speciﬁed conﬁdence interval of its estimated value. This constraint recognizes the possibility of estimation error. And, in addition to the standard maximization of the mean-variance objective function over the choice of weights, one also minimizes over the choice of parameter values subject to this constraint. This minimization reﬂects the desire of the investor to guard against estimation error by making choices that are conservative.

We show analytically that the max-min problem faced by an investor who is concerned about parameter uncertainty can be reduced to a maximization-only problem, but where the estimated expected returns are adjusted in order to reﬂect the parameter uncertainty. The adjustment depends on the precision with which these parameters are estimated, the length of the data series, and on the investor’s aversion to uncertainty. For the case without a riskless asset, we show that the optimal portfolio can be characterized as a weighted average of the standard mean-variance portfolio, which is the portfolio where the investor ignores the possibility of error in estimating expected returns, and the minimum-variance portfolio, which is the portfolio formed by completely ignoring expected returns. We also explain the sense in which the portfolio formed using Bayesian estimation methods is nested in the multi-prior model.

We illustrate the multi-prior approach using both domestic and international sets. First, we consider a portfolio allocated across equity indexes for eight countries and then consider a portfolio allocated to the US market portfolio and the Fama-French portfolios, HML and SMB, when there is uncertainty both about the factor model generating returns and also about expected returns. We ﬁnd that the portfolio weights using the multi-prior model are less unbalanced and ﬂuctuate much less over time compared to the standard mean-variance portfolio weights and also the portfolios from the Bayesian models. We ﬁnd that allowing for a small amount of uncertainty about factor and asset returns in the multi-prior model leads to an out-of-sample Sharpe Ratio that is greater than that of the mean-variance and Bayesian portfolios.

# A Appendix: Proofs of all propositions

## Proof of Proposition 1

The solution to the inner minimization problem is easily found to be

√ √ j

µj = µˆj − sign(wj)σ

, j = 1,...,N.

T

which, when substituted back into the original problem, gives

 

 

N

σj √

γ 2

√

w µ ˆ −

w Σw

, (A1)

maxw

sign(wj)wj

j −





T

j

subject to w 1N = 1.23 Collecting the ﬁrst two terms in the curly brackets gives the result in the proposition.

## Proof of Proposition 2

Let us focus ﬁrst on the inner minimization

minµ w µ −

γ 2

w Σw, (A2)

subject to

(ˆµ − µ) Σ−1(ˆµ − µ) ≤ ε. (A3) The Lagrangian is

L(µ,λ) = w µ −

γ 2

w Σw − λ ε − (ˆµ − µ) Σ−1(ˆµ − µ) . (A4)

It is well-known that µ∗ is a solution of the constrained problem (A2)-(A3) if and only if there exist a scalar λ∗ ≥ 0 such that (µ∗,λ∗) is a solution of the following unconstrained problem

minµ max

L(µ,λ). (A5)

λ

From the ﬁrst order conditions with respect to µ in (A4) we obtain

- 1

- 2λ

µ∗ = µˆ −

Σw. (A6)

23Note that the objective function is not diﬀerentiable at wj = 0, j = 1, . . . , N.

Substituting this in the Lagrangian (A4), we get

L(µ∗,λ) = w µ ˆ −

1 4λ

γ 2

+

w Σw − λε. (A7)

Hence, the original max-min problem in (6) subject to (8) and (15) is equivalent to the following maximization problem

max

w µ ˆ −

w,λ

1 4λ

γ 2

+

w Σw − λε, (A8)

subject to w 1N = 1. Solving for λ we obtain λ = 21 w ε Σw > 0 from which, upon substitution in (A8) we obtain (16).

The maximization in (16) can be rewritten as follows

maxw w µ ˆ −

2√ε γ

γ 2

w Σw 1 +

√

w Σw

,

√ε γ

subject to w 1N = 1. Letting Ω(w) ≡ 1 + 2

w Σw , we can write the above maximization as

√

γ 2

maxw w µ ˆ −

w Ω(w)w,

subject to w 1N = 1. The Lagrangian is

L(w,λ) = w µ ˆ −

γ 2

w Ω(w)w + λ(1 − w 1N).

The ﬁrst order conditions with respect to w gives

µˆ −

√

√ε + γ

w Σw √

w Σw

Σw − λ1N = 0.

Let σP ≡

√

w Σw. From the last equation

w =

σP √ε + γσP

Σ−1(ˆµ − λ1N). (A9)

Using w 1N = 1 we can write

1 = w 1N =

σP √ε + γσP

(ˆµ − λ1 N)Σ−11N

=

σP √ε + γσP

(B − λA),

where A = 1 N Σ−1 1N and B = µˆ Σ−1 1N. From the last equality, we obtain

1 A

λ =

√ε + γσP σP

B −

.

Substituting this in the expression for the weights in (A9) we arrive at

1 A

σP √ε + γσP

Σ−1 µ ˆ −

w =

√ε + γσP σP

B −

1N . (A10)

- We obtain, after some manipulation, that the variance of the optimal portfolio w∗ subject

to w 1N = 1 is given by the (unique) positive real solution σP∗ of the following polynomial equation

Aγ2 σP4 + 2Aγ√εσP3 + (Aε − AC + B2 − γ2)σP2 − 2γ√εσP − ε = 0, (A11)

where A = 1 NΣ−11N, B = µˆ Σ−11N and C = µˆ Σ−1µˆ. Note that, since Σ is deﬁnite positive, the above polynomial equation always has at least one positive real root. Let σP∗ be the unique positive real root of this equation.24 Then, the optimal portfolio w∗ is given by

√ε + γσP∗ σ∗

1 A

σP∗ √ε + γσ∗

w∗ =

Σ−1 µ ˆ −

1N , (A12)

B −

P

P

which simpliﬁes to (17).

## Proof of Proposition 3

Without loss of generality we consider the case of M = 2 non-overlapping subsets. The two subsets are labeled a containing Ma assets, and f containing Mf assets, with Ma+Mf = N. Since there are only two subclasses if we label by a subclass m, subclass −m will be labeled by f and vice-versa. The investor faces the following problem

maxw µmin

a,µf w µ −

γ 2

w Σw, (A13)

24It is possible to show that the fourth degree polynomial in (A11) has at least two real roots, one of which is positive. This occurs since the polynomial is equal to −ε in x = 0 and tends to +∞ for x → ±∞. Moreover, the ﬁrst derivative of (A11) is negative in x = 0 and has at least a negative local maximum, implying that the positive real root of (A11) is unique.

subject to

(ˆµa − µa) Σ−1

aa (ˆµa − µa) ≤ a (A14) (ˆµf − µf) Σ−1

ff (ˆµf − µf) ≤ f (A15)

The Lagrangian of the inner minimization is

L(µa,µf,λf,λα) = w a µa + w f µf −

γ 2

w Σw (A16)

− λα α − (ˆµa − µa) Σ−1

aa (ˆµa − µa) (A17) − λf f − (ˆµf − µf) Σ−1

ff (ˆµf − µf) .

Solving for µa and µf in the inner minimization yields

µ∗a = µˆa −

- 1

- 2λα

Σaawa, µ∗f = µˆf −

- 1

- 2λf

Σff (A18)

λα =

w a Σaawa √

- 1

- 2

, λf =

α

w f Σffwf √

- 1

- 2

, (A19)

f

where λf ≥ 0 and λα ≥ are the Lagrange multipliers for the constraints (A15) and (A14).

Substituting these back in the Lagrangian we can rewrite the original maxmin problem as follows

γ 2

w a Σˆaa(wa, α)wa − w a Σafwf − w f Σfawa − w f Σˆff(wf, f)wf ,

wmax

a,wf w a µˆa + w f µˆf −

(A20) where

Σˆaa(wa, α) = 1 +

Σˆff(wf, f) = 1 +

√ √waΣaa a wa

2 γ

√

2 γ

f wfΣffwf

(A21)

. (A22)

Let us deﬁne

σa ≡ waΣaawa (A23) σf ≡ wfΣffwf. (A24)

Since Σaa and Σff are positive deﬁnite, σa > 0 unless wa = 0Ma×1, and similarly, σf > 0 unless wf = 0Mf×1. Now the ﬁrst-order conditions with respect to wa and wf yield

√

α + γσa σa

Σaawa = µˆa − γΣafwf, (A25) √

f + γσf σf

Σffwf = µˆf − γΣfawa. (A26)

Given wf, we can solve for σa in (A25) and get

σa =

1 γ

√

max g(wf) Σ−1

aa g(wf) −

α,0 , (A27)

- where g(wf) = µˆa−γΣafwf. Substituting this back into (A25) we obtain (22) when m = a. Similarly, given wa, we can solve for σf in (A26) and get

σf =

1 γ

max h(wf) Σ−1

ff h(wf) −

√

α,0 (A28)

- where h(wa) = µˆf −γΣfawa. Substituting this back into (A26) we obtain (22) when m = f. Note ﬁnally that it is always possible to ﬁnd a set in which the mapping Υ : Ma ×

Mf → Ma × Mf deﬁned by (22) admits a solution. To see this, let Wa ⊂ Ma and

- Wf ⊂ Mf be non-empty, closed, bounded and convex subsets containing the origin. Deﬁne the set

1 γ

1 γ

Σ−1

Σ−1

Γ =

aa g(Wa) ×

ff h(Wf) ⊂ Ma × Mf. (A29)

Since Υ is continuous and the “max” in (22) are bounded between zero and one, Υ(Γ) ⊆ Γ. By the Brower Fixed Point Theorem, Υ has a ﬁxed point in Γ.

## Proof of Corollary 1

Immediate consequence of Proposition 3 for M = N.

## Proof of Corollary 2

From Proposition 3, note that when M = 1, g(wm) = g(w) = µˆ. The result then follows from equation (22).

### Table 1: Parameters for the two-asset one-factor example

This tables reports the parameters used to solve for the optimal portfolio of an uncertainty averse investor who bases his expected return for the N asset using an asset pricing model with K factors. Here, αi denotes the mispricing of each asset, βij are the factor loadings, ωi are the percent volatilities of the residuals (assuming that the matrix Ω is diagonal), µFj and σjF are the expected returns and volatilities of the factor.

Parameter Value N 2 K 1

- α1 0.0000
- α2 0.0000

- β1 0.1900
- β2 0.1300

- ω1 3.3764
- ω2 3.6194 µF1 0.6230 σ1F 5.5227

### Table 2: Portfolio weights for the two-asset one-factor example

This table reports for diﬀerent values of a and f (which gives the level of uncertainty about the factor), the optimal percentage of wealth to be invested in the two assets, w1 and w2, and in the weight in the factor, wf according to the multi-prior model. The parameters used to generate asset returns are described in Table 1.

w1(%) w2(%) wf(%)

- Panel A: f = 0.0

- a = 0.00000 0.00 0.00 100.00 a = 0.00005 0.00 0.00 100.00 a = 0.00010 0.00 0.00 100.00 a = 0.00015 0.00 0.00 100.00 a = 0.00020 0.00 0.00 100.00

Panel B: f = 0.01

- a = 0.00000 1.86 1.11 97.03 a = 0.00005 0.15 0.09 99.76 a = 0.00010 0.00 0.00 100.00 a = 0.00015 0.00 0.00 100.00 a = 0.00020 0.00 0.00 100.00

Panel C: f = 0.02

- a = 0.00000 2.65 1.58 95.78

- a = 0.00005 0.94 0.56 98.50 a = 0.00010 0.21 0.13 99.66 a = 0.00015 0.00 0.00 100.00 a = 0.00020 0.00 0.00 100.00

Panel D: f = 0.03 a = 0.00000 3.25 1.94 94.81

- a = 0.00005 1.56 0.93 97.52

- a = 0.00010 0.83 0.49 98.67 a = 0.00015 0.26 0.16 99.58 a = 0.00020 0.00 0.00 100.00

Panel E: f = 0.04

a = 0.00000 3.77 2.24 93.99 a = 0.00005 2.08 1.24 96.68

- a = 0.00010 1.36 0.81 97.84 a = 0.00015 0.79 0.47 98.74 a = 0.00020 0.31 0.18 99.51

### Table 3: Summary statistics for international data

This table gives the summary statistics for the monthly returns on eight country indices and the unconditional correlations of excess returns. The month-end dollar-denominated returns on the equity indices of eight countries are from MSCI (Morgan Stanley Capital International). Excess return are obtained by subtracting the month-end return on the United States 30 day T-bill as reported by the CRSP data-ﬁles. The sample period is 31 January 1970 to 31 July 2001 (379 observations).

Panel A: Summary statistics

World Canada Japan France Germany Italy Switzerland U.K. U.S. Mean 0.90 0.89 1.13 1.10 1.01 0.76 1.09 1.11 0.95 Std.Dev. 4.16 5.62 6.61 6.61 5.91 7.55 5.50 6.83 4.46 Skewness -0.40 -0.42 0.24 0.01 -0.12 0.32 -0.03 1.34 -0.30 Kurtosis 1.44 1.93 0.53 1.40 0.91 0.72 1.34 11.30 2.00

Panel B: Unconditional correlations of excess returns World Canada Japan France Germany Italy Switzerland U.K. U.S.

WR 1 0.726 0.685 0.641 0.587 0.444 0.674 0.683 0.846 CA 1 0.312 0.458 0.355 0.306 0.453 0.508 0.721 JP 1 0.398 0.365 0.351 0.424 0.369 0.306 FR 1 0.627 0.461 0.611 0.550 0.459 GE 1 0.412 0.673 0.439 0.397 IT 1 0.376 0.339 0.253 SW 1 0.565 0.502 UK 1 0.515 US 1

### Table 4: Out-of-sample performance of various portfolios using international data

This table reports the out-of-sample Mean, Standard Deviation and Mean-to-Standard Deviation ratio for the returns on diﬀerent portfolio strategies. Means and Standard Deviations are expressed as percentage per month. The portfolio weights for each strategy are determined based using the international data based on a data-window of 60 months and these portfolio weights are then used to calculate the returns in the 61st month. The resulting out-of-sample period spans January 1975 to July 2001 (319 observations). Data are described in Table 3. In parenthesis we report the percentage size of the conﬁdence interval for a F8,52 implied by the values of .

Strategy Mean Std.Dev. Mean

Std.Dev.

Panel A: Short sales allowed

Mean-Variance -0.517 42.085 -0.012 Minimum-Variance 1.090 4.116 0.265 Bayesian approach

Diﬀuse Prior -0.491 41.394 -0.012 Empirical Bayes-Stein -0.162 17.508 -0.009

Multi-prior approach

- = 0 (0.00%) -0.517 42.085 -0.012
- = 1 (55.26%) 0.555 7.687 0.072

= 3 (99.23%) 0.965 4.513 0.214 = 5 (99.98%) 1.010 4.267 0.237 = 10 (99.99%) 1.040 4.135 0.251 → ∞ (100%) 1.090 4.116 0.265

Panel B: Short sales not allowed

Mean-Variance 1.031 5.708 0.181 Minimum-Variance 1.100 4.007 0.274 Bayesian approach

Diﬀuse Prior 1.031 5.708 0.181 Empirical Bayes-Stein 1.081 5.071 0.213

Multi-prior approach

- = 0 (0.00%) 1.030 5.708 0.181
- = 1 (55.26%) 1.085 4.330 0.251

= 3 (99.23%) 1.086 4.087 0.266 = 5 (99.98%) 1.089 4.044 0.269 = 10 (99.99%) 1.092 4.013 0.272 → ∞ (100%) 1.100 4.007 0.274

ω = 0.00, implying that the investor has zero conﬁdence in the return-generating model. The portfolio weights for each strategy are determined using the domestic data based on a data-window of 120 months and these portfolio weights are then used to calculate the returns in the 121st month. The data range from July 1926 to December 2002, with the ﬁrst portfolio formed in August 1936. The slight diﬀerence between the Sharpe Ratio for the mean-variance portfolio, 0.111, and the 0.109 for the multi-prior model when

a = f = 0 is because of the degrees-of-freedom adjustment, as explained in Wang (2003). In parenthesis we report the percentage size of the conﬁdence interval for a F2,118 implied by the values of a and the percentage size of the conﬁdence interval for a t119 implied by the values of f.

Strategy Sharpe Ratio Mean-Variance 0.111 Minimum-Variance 0.162 Bayesian approach

Bayes-Stein 0.116 Pastor-Stambaugh

with ω = 0.00 0.109 Multi-prior approach f with ω = 0.00 0.00 0.50 1.00 1.50 2.00 2.50 3.00

% (0.0) (38.20) (68.07) (86.37) (95.22) (98.62) (99.67) a %

- 0.000 (0.00) 0.109 0.105 0.069 0.014 0.086 0.082 0.071

- 0.500 (39.21) 0.130 0.053 0.082 0.044 0.075 -0.027 -0.009
- 1.000 (62.90) 0.157 0.168 0.109 0.041 0.051 0.036 0.090

1.500 (77.26) 0.069 0.181 0.170 0.159 0.132 0.074 0.009 2.000 (86.01) 0.072 0.171 0.161 0.157 0.150 0.138 0.113

- 2.500 (91.36) 0.104 0.147 0.146 0.153 0.156 0.143 0.118
- 3.000 (94.64) 0.091 0.143 0.146 0.149 0.154 0.144 0.108

3.500 (96.66) 0.064 0.144 0.148 0.152 0.159 0.154 0.125 4.000 (97.91) 0.070 0.141 0.143 0.139 0.151 0.145 0.114

- 4.500 (98.69) 0.097 0.137 0.138 0.140 0.151 0.150 0.118

ω = 1, implying that the investor has perfect conﬁdence in the return-generating model. The portfolio weights for each strategy are determined using the domestic data based on a data-window of 120 months and these portfolio weights are then used to calculate the returns in the 121st month. The data range from July 1926 to December 2002, with the ﬁrst portfolio formed in August 1936.In parenthesis we report the percentage size of the conﬁdence interval for a F2,118 implied by the values of a and the percentage size of the conﬁdence interval for a t119 implied by the values of f.

Strategy Sharpe Ratio Mean-Variance 0.111 Minimum-Variance 0.162 Bayesian approach

Bayes-Stein 0.116 Pastor-Stambaugh

with ω = 1.00 0.102 Multi-prior approach f with ω = 1.00 0.00 0.50 1.00 1.50 2.00 2.50 3.00

% (0.0) (38.20) (68.07) (86.37) (95.22) (98.62) (99.67) a %

- 0.000 (0.00) 0.102 -0.047 -0.017 -0.016 -0.037 -0.023 -0.026

- 0.500 (39.21) 0.102 0.140 0.151 0.142 0.144 0.139 -0.018
- 1.000 (62.90) 0.102 0.140 0.151 0.142 0.145 0.144 0.116

1.500 (77.26) 0.102 0.140 0.151 0.142 0.145 0.144 0.116 2.000 (86.01) 0.102 0.140 0.151 0.142 0.145 0.144 0.116

- 2.500 (91.36) 0.102 0.140 0.151 0.142 0.145 0.144 0.116
- 3.000 (94.64) 0.102 0.140 0.151 0.142 0.145 0.144 0.116

3.500 (96.66) 0.102 0.140 0.151 0.142 0.145 0.144 0.116 4.000 (97.91) 0.102 0.140 0.151 0.142 0.145 0.144 0.116

- 4.500 (98.69) 0.102 0.140 0.151 0.142 0.145 0.144 0.116

### Figure 1: Portfolio weights in the US index over time

This ﬁgure reports the portfolio weights in the US index from January 1975 to July 2001. Panel A shows the case where short-selling is allowed and Panel B gives the case where short-selling is not allowed. The dashed line (MV) refers to the mean-variance portfolio. The dash-dotted line ( = 1) are the portfolios obtained with a degree of uncertainty expressed roughly by the 55% conﬁdence interval for an F8,52 centered around the sample mean, while the solid line ( = 3) are portfolio obtained assuming uncertainty about expected returns is given by a 99% conﬁdence interval.

#### Panel A: Shortselling allowed

2500

|MV<br><br>ε= 1 ε= 3<br><br>|
|---|

2000

1500

1000

500

0

−500

−1000

Jan 75 Mar 79 May 83 Jul 87 Sep 91 Nov 95 Jan 99

#### Panel B: Shortselling not allowed

120

|MV<br><br>ε= 1 ε= 3<br><br>|
|---|

100

80

60

40

20

0

−20

Jan 75 Mar 79 May 83 Jul 87 Sep 91 Nov 95 Jan 99

### Figure 2: Shrinkage factors φMP( ) and φBS over time

The optimal portfolio of the investor can be interpreted as the weighted-average of the standard meanvariance portfolio and the minimum-variance portfolio. The ﬁgure reports the weight put on the minimumvariance portfolio for diﬀerent levels of uncertainty. The plot φMP(1) gives the weight on the minimumvariance portfolio when = 1, and the plot φMP(5) gives the weight on the minimum-variance portfolio when = 5. The solid line, φBS gives the weight on the minimum-variance portfolio if one were using the empirical Bayes-Stein estimator of expected returns. These weights are determined based on a data-window of 60 months and the resulting portfolio generates returns over the 61st month. The out-of sample period spans from January 1975 to July 2001 (319 observations). The data are described in Table 3.

1

0.9

0.8

0.7

0.6

0.5

0.4

|φBS φPU(1) φPU(5)<br><br>|
|---|

0.3

Jan 75 Mar 79 May 83 Jul 87 Sep 91 Nov 95 Jan 99

### Figure 3: Portfolio weights assuming expected returns estimated using MLE

The ﬁgure has four panels (two on this page and two on the next) which report the weight over time in SMB, HML, MKT and the riskfree asset. Expected returns are estimated using the maximum-likelihood estimator using a rolling window estimation period of 120 months. The data range from July 1926 to December 2002. The ﬁrst portfolio is formed in August 1936. The plots on the left hand side refer to the case of no uncertainty in the market ( f = 0), while the plots on the right hand side assume a level of uncertainty in the market equal to f = 2. In each ﬁgure we consider three diﬀerent level of uncertainty about the asset estimate:

a = 0 (dash-dotted), a = 0.5 (dotted), a = 4.5 (dashed). The solid black line represents the portfolio chosen by a single-prior Bayesian who places inﬁnite conﬁdence in the data (ω = 0).

Panel A: Portfolio weights in SMB f = 0.00 f = 2.00

- −0.1

−0.05

0

0.05

0.1

0.15

|εa=0 εa=0.5 εa=4.5 Bayes, ω=0<br><br>|
|---|

Jul36 Nov44 Mar53 Jun61 Oct69 Feb78 May86 Sep94 Dec02

−0.2

−0.15

−0.1

−0.05

0

0.05

0.1

0.15

|εa=0 εa=0.5 εa=4.5 Bayes, ω=0<br><br>|
|---|

Panel B: Portfolio weights in HML f = 0.00 f = 2.00

Jul36 Nov44 Mar53 Jun61 Oct69 Feb78 May86 Sep94 Dec02

−0.04

- −0.02

−0.15

−0.2

Jul36 Nov44 Mar53 Jun61 Oct69 Feb78 May86 Sep94 Dec02

0.16

0.16

0.14

0.14

0.12

0.12

0.1

0.1

0.08

0.08

0.06

0.06

0.04

0.04

0.02

0.02

0

0

|εa=0 εa=0.5 εa=4.5 Bayes, ω=0<br><br>|
|---|

|εa=0 εa=0.5 εa=4.5 Bayes, ω=0<br><br>|
|---|

−0.02

−0.04

Jul36 Nov44 Mar53 Jun61 Oct69 Feb78 May86 Sep94 Dec02

##### Panel C: Portfolio weights in MKT f = 0.00 f = 2.00

0.16

0.16

0.14

0.14

0.12

0.12

0.1

0.1

0.08

0.08

0.06

0.06

0.04

0.04

0.02

0.02

0

0

|εa=0 εa=0.5 εa=4.5 Bayes, ω=0<br><br>|
|---|

|εa=0 εa=0.5 εa=4.5 Bayes, ω=0<br><br>|
|---|

−0.02

−0.02

−0.04

−0.04

Jul36 Nov44 Mar53 Jun61 Oct69 Feb78 May86 Sep94 Dec02

Jul36 Nov44 Mar53 Jun61 Oct69 Feb78 May86 Sep94 Dec02

##### Panel D: Portfolio weights in the riskfree asset f = 0.00 f = 2.00

1.05

1.1

1.05

1

1

0.95

0.95

0.9

0.9

0.85

0.85

| | |
|---|---|
|εa=0 εa=0.5 εa=4.5 Bayes, ω=0<br><br>| |

0.8

0.8

|εa=0 εa=0.5 εa=4.5 Bayes, ω=0<br><br>|
|---|

0.75

0.75

0.7

0.7

Jul36 Nov44 Mar53 Jun61 Oct69 Feb78 May86 Sep94 Dec02

Jul36 Nov44 Mar53 Jun61 Oct69 Feb78 May86 Sep94 Dec02

### Figure 4: Portfolio weights assuming factor model (CAPM) for expected returns

The ﬁgure has four panels (two on this page and two on the next) which report the weight over time in SMB, HML, MKT and the riskfree asset. Expected returns are estimated assuming that there is a factor structure (CAPM) and using a rolling window estimation period of 120 months. The data range from July 1926 to December 2002. The ﬁrst portfolio is formed in August 1936. The plots on the left hand side refer to the case of no uncertainty in the market ( f = 0), while the plots on the right hand side assume a level of uncertainty in the factor equal to f = 2. In each ﬁgure we consider three diﬀerent level of uncertainty about the asset estimate: a = 0 (dash-dotted), a = 0.5 (dotted), a = 4.5 (dashed). The solid black line represents the portfolio chosen by a single-prior Bayesian who places inﬁnite conﬁdence in the model (ω = 1).

Panel A: Portfolio weights in SMB f = 0.00 f = 2.00

- −0.2

0

0.2

0.4

0.6

- 0.8

- 1

|εa=0 εa=0.5 εa=4.5 Bayes, ω=1<br><br>|
|---|

Jul36 Nov44 Mar53 Jun61 Oct69 Feb78 May86 Sep94 Dec02

−0.04

−0.03

−0.02

−0.01

0

0.01

0.02

0.03

0.04

|εa=0 εa=0.5 εa=4.5 Bayes, ω=1<br><br>|
|---|

Panel B: Portfolio weights in HML f = 0.00 f = 2.00

Jul36 Nov44 Mar53 Jun61 Oct69 Feb78 May86 Sep94 Dec02

- −1

−0.4

−0.6

−0.8

−1

Jul36 Nov44 Mar53 Jun61 Oct69 Feb78 May86 Sep94 Dec02

- 0.8

- 1

0.03

0.02

0.6

0.01

0.4

0.2

0

0

−0.01

−0.2

−0.4

−0.02

−0.6

|εa=0 εa=0.5 εa=4.5 Bayes, ω=1<br><br>|
|---|

|εa=0 εa=0.5 εa=4.5 Bayes, ω=1<br><br>|
|---|

−0.03

−0.8

−0.04

Jul36 Nov44 Mar53 Jun61 Oct69 Feb78 May86 Sep94 Dec02

##### Panel C: Portfolio weights in MKT f = 0.00 f = 2.00

0.14

0.14

0.12

0.12

0.1

0.1

0.08

0.08

0.06

0.06

0.04

0.04

0.02

0.02

|εa=0 εa=0.5 εa=4.5 Bayes, ω=1<br><br>|
|---|

εa=0 εa=0.5 εa=4.5 Bayes, ω=1

0

0

−0.02

−0.02

Jul36 Nov44 Mar53 Jun61 Oct69 Feb78 May86 Sep94 Dec02

Jul36 Nov44 Mar53 Jun61 Oct69 Feb78 May86 Sep94 Dec02

##### Panel D: Portfolio weights in the riskfree asset f = 0.00 f = 2.00

1.05

1

- 0.9

0.95

- 1

0.95

0.9

|εa=0 εa=0.5 εa=4.5 Bayes, ω=1<br><br>|
|---|

|εa=0 εa=0.5 εa=4.5 Bayes, ω=1<br><br>|
|---|

0.85

Jul36 Nov44 Mar53 Jun61 Oct69 Feb78 May86 Sep94 Dec02

Jul36 Nov44 Mar53 Jun61 Oct69 Feb78 May86 Sep94 Dec02

# References

Anderson, E., L. Hansen, and T. Sargent, 1999, “Robustness detection and the price of risk,” Working paper, University of Chicago.

Barry, C. B., 1974, “Portfolio Analysis under Uncertain Means, Variances, and Covariances,” Journal of Finance, 29, 515–22.

Bawa, V. S., S. Brown, and R. Klein, 1979, Estimation Risk and Optimal Portfolio Choice, North Holland, Amsterdam.

Berger, J., 1974, “Minimax Estimator of a Multivariate Normal Mean Under Polynomial Loss,” Journal of Multivariate Analysis, 8, 173–180.

- Best, M. J., and R. R. Grauer, 1991, “On the Sensitivity of Mean-Variance-Eﬃcient Portfolios to Changes in Asset Means: Some Analytical and Computational Results,” Review of Financial Studies, 4, 315–42.
- Best, M. J., and R. R. Grauer, 1992, “Positively Weighted Minimum-Variance Portfolios and the Structure of Asset Expected Returns,” Journal of Financial and Quantitative Analysis, 27, 513–37.

Bewley, T., 1988, “Knightian Decision Theory and Econometric Inference,” Working Paper, Yale University.

Black, F., and R. Litterman, 1990, “Asset Allocation: Combining Investor Views with Market Equilibrium,” Discussion paper, Goldman, Sachs & Co.

Black, F., and R. Litterman, 1992, “Global Portfolio Optimization,” Financial Analysts Journal, 48, 28–43.

Chan, L. K. C., J. Karceski, and J. Lakonishok, 1999, “On Portfolio Optimization: Forecasting Covariances and Choosing the Risk Model,” Review of Financial Studies, 12, 937–74.

Chen, Z., and L. Epstein, 2002, “Ambiguity, Risk, and Asset Returns in Continuous Time,”

Econometrica, 70, 1403–43. Chopra, V. K., 1993, “Improving Optimization,” Journal of Investing, 8, 51–59. Chopra, V. K., and W. T. Ziemba, 1993, “The Eﬀect of Errors in Means, Variances, and

Covariances on Optimal Portfolio Choice,” Journal of Portfolio Management, 19, 6–11. De Santis, G., and B. Gerard, 1997, “International Asset Pricing and Portfolio Diversiﬁca-

tion with Time-Varying Risk,” Journal of Finance, 52, 1881–1912. Dow, J., and S. R. d. C. Werlang, 1992, “Uncertainty Aversion, Risk Aversion, and the Optimal Choice of Portfolio,” Econometrica, 60, 197–204. Dumas, B., and B. Jacquillat, 1990, “Performance of Currency Portfolios Chosen by a Bayesian Technique: 1967-1985,” Journal of Banking and Finance, 14, 539–58. Ellsberg, D., 1961, “Risk, Ambiguity and the Savage Axioms,” Quarterly Journal of Economics, 75, 643–669.

Epstein, L. G., and T. Wang, 1994, “Intertemporal Asset Pricing Under Knightian Uncertainty,” Econometrica, 62, 283–322.

Fox, C., and A. Tversky, 1995, “Ambiguity Aversion and Comparative Ignorance,” Quarterly Journal of Economics, 110, 585–603.

Frost, P., and J. Savarino, 1988, “For Better Performance Constrain Portfolio Weights,” Journal of Portfolio Management, 15, 29–34.

Frost, P. A., and J. E. Savarino, 1986, “An Empirical Bayes Approach to Eﬃcient Portfolio Selection,” Journal of Financial and Quantitative Analysis, 21, 293–305.

Gilboa, I., and D. Schmeidler, 1989, “Maxmin Expected Utility Theory with Non-Unique Prior,” Journal of Mathematical Economics, 18, 141–153.

Goldfarb, D., and G. Iyengar, 2003, “Robust Portfolio Selection Problems,” Mathematica of Operations Research, 28, 1–38.

Halld´rsson, B., and R. T¨ut¨unc¨u, 2000, “An Interior-Point Method for a Class of Saddle Point Problems,” Working Paper, Carnegie Mellon University.

Harvey, C. R., J. Liechty, M. Liechty, and P. M¨uller, 2003, “Portfolio Selection with Higher Moments,” Working Paper, Duke University.

Heath, C., and A. Tversky, 1991, “Preferences and Beliefs: Ambiguity and Competence in Choice under Uncertainty,” Journal of Risk and Uncertainty, 4, 5–28.

Hodges, S. D., and R. A. Brealey, 1978, “Portfolio Selection in a Dynamic and Uncertin World,” in James H. Lorie, and R. A. Brealey (ed.), Modern Developments in Investment Management, Dryden Press, Hinsdale, Illionois, 2nd edn.

Jagannathan, R., and T. Ma, 2003, “Risk Reduction in Large Portfolios: Why Imposing the Wrong Constraints Helps,” Journal of Finance, 58, 1651–1684.

Jobson, J. D., and R. Korkie, 1980, “Estimation for Markowitz Eﬃcient Portfolios,” Journal of the American Statistical Association, 75, 544–554.

Johnson, R., and D. W. Wichern, 1992, Applied Multivariate Statistical Analysis, Prentice Hall.

- Jorion, P., 1985, “International Portfolio Diversiﬁcation with Estimation Risk,” Journal of Business, 58, 259–278.
- Jorion, P., 1986, “Bayes-Stein Estimation for Portfolio Analysis,” Journal of Financial and Quantitative Analysis, 21, 279–92.

Klein, R. W., and V. S. Bawa, 1976, “The Eﬀect of Estimation Risk on Optimal Portfolio

Choice,” Journal of Financial Economics, 3, 215–31. Knight, F., 1921, Risk, Uncertainty and Proﬁt, Houghton Miﬄin, Boston. Kogan, L., and T. Wang, 2002, “A Simple Theory of Asset Pricing under Model Uncer-

tainty,” Working Paper, University of British Columbia. Ledoit, O., 1996, “A Well-Conditioned Estimator for Large-Dimensional Covariance Matrices,” Working Paper, Anderson School, UCLA.

Ledoit, O., and M. Wolf, 2003, “Honey, I Shrunk the Sample Covariance Matrix,” Working

Paper, Department of Economics and Business, Universitat Pompeu Fabra. Litterman, R., 2003, Modern Investment Management: An Equilibrium Approach, Wiley. Markowitz, H. M., 1952, “Mean-Variance Analysis in Portfolio Choice and Capital Mar-

kets,” Journal of Finance, 7, 77–91. Markowitz, H. M., 1959, Portfolio Selection, Wiley, New York. Merton, R., 1980, “On estimating the expected return on the market: An exploratory

investigation,” Journal of Financial Economics, 8, 323–361. Michaud, R. O., 1989, “The Markowitz Optimization Enigma: Is Optimized Optimal,” Financial Analysts Journal, 45, 31–42.

Michaud, R. O., 1998, Eﬃcient Asset Management, Harvard Business School Press, Boston. P´stor, L.,ˇ 2000, “Portfolio Selection and Asset Pricing Models,” Journal of Finance, 55,

179–223. P´stor, L.,ˇ and R. F. Stambaugh, 2000, “Comparing Asset Pricing Models: An Investment Perspective,” Journal of Financial Economics, 56, 335–81. Scherer, B., 2002, “Portfolio Resampling: Review and Critique,” Financial Analysts Jour-

nal, 58, 98–109. Sharpe, W. F., 1970, Portfolio Theory and Capital Markets, McGraw-Hill, New York. Stambaugh, R. F., 1997, “Analyzing Investments whose Histories Diﬀer in Length,” Journal

of Financial Economics, 45, 285–331.

Stein, C., 1955, “Inadmissibility of the Usual Estimator for the Mean of a Multivariate Normal Distribution,” in 3rd Berkely Symposium on Probability and Statistics, , vol. 1, pp. 197–206, Berkeley. University of California Press.

Tu¨t¨unc¨u, R., and M. Koenig, 2003, “Robust Asset Allocation,” Working Paper, Carnegie Mellon University.

Uppal, R., and T. Wang, 2003, “Model Misspeciﬁcation and Underdiversiﬁcation,” Journal of Finance, 58, 2465–2486.

Wang, Z., 2003, “A Shrinkage Approach to Model Uncertainty and Asset Allocation,” Working Paper, Columbia University.

