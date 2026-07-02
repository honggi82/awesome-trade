# Jumps in Financial Markets: A New Nonparametric Test and Jump Dynamics

Suzanne S. Lee Georgia Institute of Technology

Per A. Mykland Department of Statistics, University of Chicago

This article introduces a new nonparametric test to detect jump arrival times and realized jump sizes in asset prices up to the intra-day level. We demonstrate that the likelihood of misclassiﬁcation of jumps becomes negligible when we use high-frequency returns. Using our test, we examine jump dynamics and their distributions in the U.S. equity markets. The results show that individual stock jumps are associated with prescheduled earnings announcements and other company-speciﬁc news events. Additionally, S&P 500 Index jumps are associated with general market news announcements. This suggests different pricing models for individual equity options versus index options. (JEL G12, G22, G14)

Financial markets sometimes generate signiﬁcant discontinuities, so-called jumps, in ﬁnancial variables. A number of recent empirical and theoretical studies proved the existence of jumps and their substantial impact on ﬁnancial management, from portfolio and risk management to option and bond pricing and hedging (see Merton, 1976; Bakshi et al., 1997, 2000; Bates, 1996; Liu et al., 2003; Naik and Lee, 1990; Dufﬁe et al., 2000, and Johannes, 2004). Despite advances in asset pricing models and their inference techniques, the studies have found that jumps are empirically difﬁcult to identify, because only discrete data are available from continuous-time models, in which most of the aforementioned applications were studied. Our goal in this article is ﬁrst to propose a new jump detection technique to resolve such identiﬁcation problems. Further, we show that our technique provides a model-free tool for characterizing jump dynamics in individual equity and S&P 500 Index returns, which allows us to investigate different model structures for their option pricing.

We thank Federico Bandi, George Constantinides, Pietro Veronesi, Ruey Tsay, Matthew Spiegel (the executive editor), and two anonymous referees for helpful suggestions and comments. Financial support for this research from the National Science Foundation (DMS-02-04639, DMS-06-04758, and SES-06-31605), Oscar Mayer Dissertation Fellowships, and the Financial Mathematics Program at the University of Chicago is gratefully acknowledged. Lee also thanks for their comments the participants of the 2006 North American Econometric Society Summer Meeting, the 2006 Far Eastern Meeting of Econometric Society, the International Workshop on Applied Probability, the 6th All-Georgia Finance Conference, and the Department Seminar of Industrial and System Engineering at Georgia Tech. Comments are welcome. Address correspondence to Suzanne S. Lee, Georgia Institute of Technology, College of Management, Atlanta, GA 30332; telephone: 404-822-1552; fax: 404-894-6030; e-mail: suzanne.lee@mgt.gatech.edu.

C The Author 2007. Published by Oxford University Press on behalf of The Society for Financial Studies. All rights reserved. For Permissions, please email: journals.permissions@oxfordjournals.org. doi:10.1093/rfs/hhm056 Advance Access publication December 9, 2007

There are primarily two motivations for this study. First, while researchers recognize the presence of jumps in order to better explain the excess kurtosis and skewness of return distributions and implied volatility smiles, we also note the fact that jumps do not come to markets regularly, but their arrivals tend to depend on market information. For instance, Piazzesi, (2003) shows that incorporating jumps related to market information improves bond pricing models. Given the difﬁculty of pinning down jump parameters, even with both time-seriesand cross-sectional data in parametric settings, we question how one can simply search observable information relevant to jumps that appear to have such strong impact on pricing securities. To learn about the stochastic features ofirregular jumparrivals andtheir associated market information, itiscritical to ﬁrst develop a robust test to detect jumps. Once detected, one can examine what type of information is dynamically related to jumps to improve pricing models and better explain market phenomena. Our test is meant to be applicable to all kinds of ﬁnancial time series, including equity returns and volatility, interest rates, and exchange rates, so long as high-frequency observations are available. Becausejumpshavebiggerimpactsonderivativesecuritiesthanothersecurities (see Johannes, 2004, for discussion), our test would have greater implications in their ﬁnancial management. We take a nonparametric approach for the results to be robust with respect to model speciﬁcations as well as to nonstationarity of price processes—a common feature of ﬁnancial variables.

Another motivation for developing our test is the improvement of derivative hedging. The presence of jumps makes incomplete markets. The degree of market incompleteness depends on the size and intensity of jumps, which determines the magnitude of derivative hedging error (see Naik and Lee, 1990; and Bertsimas et al., 2001). As a by-product, our test yields both the direction and size of detected jumps, allowing the characterization of jump size distribution as well as stochastic jump intensity. These outcomes allow us to develop hedging strategies accordingly. Detecting arrival times is also important in order to rebalance hedging portfolios dynamically once a jump arrival is detected, as shown by Collin-Dufresne and Hugonnier (2001).

Our main methodological contribution is summarized as follows. We ﬁrst explain the intuition on how we develop the test and its mathematical deﬁnition. Then, we provide its asymptotic distribution and detection criterion for practical use. Second, we prove that it can precisely distinguish actual jumps using high-frequency data and show that spurious detection of jumps becomes negligible. Hence, we show that stochastic jump estimates based on our test are accurate. Third, we compare our test to the existing nonparametric jump tests by Barndorff-Nielsen and Shephard (2006) and Jiang and Oomen (2005). Ours outperforms these others in terms of size and power. Monte Carlo simulation conﬁrms the results as well.

After we discuss generally how our test can be applied in asset pricing models, we conduct an empirical study particularly for the U.S. equity markets. We collect from the Trade and Quote (TAQ) database high-frequency returns

of three individual stock and S&P 500 Index prices transacted on the New York Stock Exchange (NYSE) over the period of 1 September to 30 November 2005.Weﬁndthatjumpsdonotoccurregularly,sothatstochasticjumpintensity should be considered in equity markets. We observe more frequent jumps in the individual stock returns than in the index returns. Sizes of jumps in individual equities are greater than those in the index. We ﬁnd that detected jumps are related to news releases from Factiva, a real-time ﬁnancial news database. For the individual stocks, jumps are associated with company-speciﬁc news events like scheduled earnings announcements, as well as unscheduled news. For the index, jumps occur with general market news such as Federal Open Market Committee (FOMC) meetings and macroeconomic reports. It is noted that for individual equities, the majority of jumps occur with unscheduled news and their magnitudes are comparable to those that occur with earnings announcements. Therefore, we conclude that one should incorporate not only earnings announcements as in Dubinsky and Johannes, (2006), but also other company-speciﬁc news for individual equity option pricing. For the index options, general market announcements and events are to be taken into account. This evidence also provides support for the different model structures for individual equity and index options described in Bakshi et al., (2003).

The rest of the article is organized as follows. Section 1 sets up a theoretical framework to detect jumps and introduces the test. Section 2 discusses the precision of our test. Section 3 investigates the test’s ﬁnite sample performance. Section 4 empirically examines jump dynamics in equity returns and their association with news releases. Finally, we conclude in Section 5.

## 1. A Theoretical Model for the Test and Its Asymptotic Theory

We employ a one-dimensional asset return process with a ﬁxed complete probability space ( ,Ft,P), where {Ft : t ∈ [0, T]} is a right-continuous information ﬁltration for market participants, and P is a data-generating measure. Let the continuously compounded return be written as d log S(t) for t ≥ 0, where S(t) is the asset price at t under P. We are interested in ﬁnding jumps in the asset returns as follows. When there are no jumps in the market, S(t) is represented as

d log S(t) = µ(t)dt + σ(t)dW(t) (1)

where W(t) is an Ft-adapted standard Brownian motion. The drift µ(t) and spot volatility σ(t) are Ft-adapted processes, such that the underlying process is an Itˆo process that has continuous sample paths. When there are jumps, S(t) is given by

d log S(t) = µ(t)dt + σ(t)dW(t) + Y(t)dJ(t), (2)

where J(t) is a counting process independent of W(t). Y(t) is the jump size, which is a predictable process (see Protter, 2004, for deﬁnition). Its mean µy(t)

and standard deviation σy(t) are also Ft-predictable processes. We assume jump sizes Y(t) are independent of each other and identically distributed. They are also independent of other random components W(t) and J(t). J(t) may be a non-homogeneous Poisson-type jump process. Hence, for instance, scheduled (deterministic) events such as earnings announcements are allowed to affect jump intensity, in which case, the model can be the sum of a process with an intensity and a deterministic counting process.

Observation of S(t), equivalently log S(t), occurs only at discrete times 0 = t0 < t1 < ··· < tn = T. For simplicity, this article assumes that observation times are equally spaced: t = ti − ti−1. This simpliﬁed assumption can easily be generalized to non-equidistant cases by letting maxi(ti − ti−1) → 0. We also impose the following necessary assumption on price processes throughout this article:

Assumption 1. For any > 0,

- A1.1 sup i

sup

ti≤u≤ti+1

|µ(u) − µ(ti)| = Op t

- 1

- 2− , (3)

- A1.2 sup i

- 1

- 2− . (4)

sup

|σ(u) − σ(ti)| = Op t

ti≤u≤ti+1

Following Pollard (2002), we use Op notation throughout this article to mean that, for random vectors {Xn} and non-negative random variable {dn}, Xn = Op(dn), if for each δ > 0, there exists a ﬁnite constant Mδ such that P(|Xn| > Mδdn) < δ eventually. One can interpret Assumption 1 as the drift and diffusion coefﬁcients not changing dramatically over a short time interval. Furthermore, Assumption 1 allows drift and diffusion to depend on the process itself. This is reasonable in view of Lemma 2 in Mykland and Zhang (2006). It is satisﬁed for most Itˆo processes. The stochastic volatility model in Heston (1993) and its extendedversionsstudiedinBakshietal.,(2005)areexamples.Thisassumption also satisﬁes the stochastic volatility plus ﬁnite activity jump semi-martingale class in Barndorff-Nielsen and Shephard, (2004).

- 1.1 Intuition for and deﬁnition of the nonparametric jump test In this subsection, we address the basic intuition behind our new detection technique and mathematically deﬁne the jump detection statistic L. Our discussion here refers to a single test at time ti. We do not make assumptions about whether there were or were not jumps before or after ti. Generalization to a global test to determine whether a diffusion model (1) is rejected is straightforward by multiple tests (single tests over available times). A global test would be interesting in itself and achieving one is also part of our goal. However, as mentioned in the introduction, the main purpose of this article is to detect jumps over time in order to advance our knowledge of the stochastic mechanism of jump arrival dynamics. Multiple tests on time series allow us to extract such information.

The intuition that gives rise to our test is as follows. Imagine that asset prices evolve continuously over time. Suppose that a jump occurs in a market at some time, say ti. We would expect the realized asset return at that time to be much greater than usual continuous innovations. What if the spot volatility at that time is also high? Even if there is no jump, if the volatility is high and if we can only observe prices in discrete times, the realized return we observe may be as high as the return that is actually due to a jump. To distinguish those two cases, it is natural to standardize the return by a measure that explains the local variation only from the continuous part of the process. We refer to this measure as instantaneous volatility in this article and denote it as σ(ti). This idea is incorporated into our test. In essence, we compare a realized return at any given time to a consistently estimated instantaneous volatility using corresponding local movements of returns. More speciﬁcally, the ratio of realized return to estimated volatility creates the test statistic for jumps.

How do we estimate instantaneous volatility? A commonly used nonparametric estimator for variance in the literature is the realized power (quadratic) variation, deﬁned as the sum of squared returns

n

(log S(ti) − log S(ti−1))2. (5)

plimn→∞

i=2

Using high-frequency returns within some period just before our testing time may yield a variance estimate over that period. However, this well-known variance estimator is inconsistent in the presence of jumps in a return process. Alternatively, a slightly modiﬁed version called the realized bipower variation, deﬁned as the sum of products of consecutive absolute returns

n

|log S(ti) − log S(ti−1)||log S(ti−1) − log S(ti−2)|, (6)

plimn→∞

i=3

has been suggested and shown to be a consistent estimator for the integrated volatility, even when there are jumps in return processes (see Barndorff-Nielsen and Shephard, 2004; and A¨ıt-Sahalia, 2004). Despite the intuition that jumps in a process may impact its volatility estimation, it remains consistent no matter how large or small jumps are mixed with the diffusive part of pricing models. Incorporating this estimator makes the detection procedure independent of the presence of jumps over time, especially those jumps used for volatility estimation.

Our test is based on this interesting insight. Even if a highly volatile market environment makes the detection of jumps more difﬁcult, infrequent Poisson jumps will be detected by our procedure fairly accurately, as long as we use high-frequency observations.

Here, we describe the formulation of the statistic and provide its mathematical deﬁnition. Suppose we have a ﬁxed time horizon T, and n is the number

[Figure 1]

Figure 1 Intuition of jump detection test

This graph illustrates how our jump detection test distinguishes the jump arrivals. The example uses S&P 500 Index returns and a window size K is 10. The jump detection statistic L is formulated by taking the ratio of the last return in a window to the instantaneous volatility, estimated by bipower variation using the returns in the same window. By shifting the window over time, one can determine stochastic jump dynamics.

of observations in [0, T]. The distance between two successive observations is

t = Tn . Consider a local movement of the process within a window size K. With realized returns in the window consisting of the previous K − 1 observations just before a testing time ti, the instantaneous volatility is estimated based on the realized bipower variation, which was discussed earlier. We then take the ratio of this estimated volatility to the next realized return in order to determine whether there was a jump arrived at ti and how large that jump size was. For example, if t = 5 minutes, ti = 10-05 a.m., and K = 10, then we test for a jump by examining the relative magnitude of a realized return from 10:00 a.m. to 10:05 a.m. compared to instantaneous volatility estimated using 5-minute returns from 9:10 a.m. to 10:00 a.m. Figure 1 illustrates the construction of the test. Mathematical notation of the test statistics is as follows:

Definition 1. The statistic L(i), which tests at time ti whether there was a jump from ti−1 to ti, is deﬁned as

log S(ti)/S(ti−1) σ(ti)

, (7)

L(i) ≡

### where

i−1

1 K − 2

σ(ti)2 ≡

|log S(tj)/S(tj−1)||log S(tj−1)/S(tj−2)|. (8)

j=i−K+2

Notice that the realized bipower variation is used for the instantaneous volatility estimation in the denominator of the statistic, which makes our technique robust

to the presence of jumps in previous time periods. We choose the window size K in such a way that the effect of jumps on the volatility estimation disappears.

We state our results ignoring the drift. For our analysis using high-frequency data, the drift (of order dt) is mathematically negligible compared to the diffusion (of order √dt) and the jump component (of order 1). In fact, the drift estimates have higher standard errors, so that they cause the precision of variance estimates to decrease if included in variance estimation. Though we study a simpliﬁed version of the model without the drift term, i.e., µ = 0, we also prove theoretically in Appendix A.1 that the main result continues to hold with the nonzero drift term. A modiﬁed statistic Lµ(i) for the nonzero drift case is formally deﬁned, and a corresponding theorem is presented therein as well.

- 1.2 Under the absence of jumps at testing time ti This subsection explains the asymptotic behavior of our jump detection statistics, L(i), when there is no jump at time ti. We suppose our realized return from time ti−1 to ti is from the diffusion part of the model (1) or (2). The asymptotic distribution of L is provided in Theorem 1. Theorem 1. Let L(i) be as in Deﬁnition 1 and the window size K = Op( tα),

- where −1 < α < −0.5. Suppose the process follows (1) or (2) and Assumption 1 is satisﬁed. Let A¯ n be the set of i ∈ {1,2,...,n} so that there is no jump in (ti−1,ti]. Then, as t → 0,

3

2−δ+α− ), (9)

|L(i) − L(i)| = Op( t

sup

i∈A¯ n

where δ satisﬁes 0 < δ < 32 + α and

Ui c

L(i) =

. (10)

Here Ui = √1 t (Wt

), a standard normal variable and a constant c = E|Ui| =

i − Wt

i−1

√2/√π ≈ 0.7979. A related procedure in which the instantaneous mean is estimated is considered in Theorem 1.1 in Appendix A.1.

## Proof of Theorem 1. See Appendix A.2.

- Theorem 1 states that our detection statistic L(i) follows approximately the same distribution as L(i). And, we ﬁnd that L(i) follows a normal distribution

with mean 0 and variance c1

because Ui is a standard normal random variable. When the absence of jumps in the whole price process is absolutely known a priori, the usage of realized quadratic variation for estimating instantaneous volatility would yield the same asymptotic distribution. As discussed when explaining our intuition, however, we do not require the absence of jumps in earlier or later time periods. Therefore, using quadratic variation does not

2

sufﬁce in this case. As can be noted, L(i) is asymptotically independent and normally distributed over time; hence, one can easily ﬁnd a joint asymptotic null distribution of the test statistics for various periods.

- 1.3 Under the presence of jumps at testing time ti We show in this subsection how the jump test reacts to the arrival of jumps and discuss the choice of window size. Suppose the realized return from time ti−1 to ti is now from jump diffusion of Equation (2). Theorem 2 speciﬁcally shows that as the sampling interval t goes to 0, the test statistic becomes so large that we can detect the jump arrival at time ti.

- Theorem 2. Let L(i) be as in Deﬁnition 1 and the window size K = Op( tα),

- where −1 < α < −0.5. Suppose the process follows (2) and the Assumption 1 is satisﬁed. Suppose there is a jump at any time τ ∈ (ti−1,ti]. Then,

Y(τ) cσ

Ui c +

L(i) ≈

, (11)

√ t

where Y(τ) is actual jump size at actual jump time τ. Therefore, L(i) → ∞, as

t → 0. If there is no jump at any time τ ∈ (ti−1,ti], L(i) has the asymptotic behavior described in Theorem 1.

## Proof of Theorem 2. See Appendix A.3.

The beneﬁt of the bipower variation as an instantaneous volatility estimator in the denominator of the test statistic is that the presence of jumps at earlier times does not affect the consistency of estimation. Therefore, our test is robust to earlier jumps in detecting current jumps. This does not imply that we make no use of earlier jumps. One can learn about an earlier jump arrival by doing the same single test at that earlier time. Several single tests over time become a multiple test, which can provide us more information on jump dynamics.

In order to retain the beneﬁt of bipower variation, the window size K must be large enough so that the effect of jumps on estimating instantaneous volatility disappears, but it must obviously be smaller than the number of observations n. The condition K = Op( tα) with −1 < α < −0.5 satisﬁes this requirement. Therefore,thechoiceofsamplingfrequency t willdeterminethewindowsize. In general, for nobs number of observations per day, t = 252×1nobs. The integers between √252 × nobs and 252 × nobs are candidates for K. If daily data are used in the analysis, t = 2521 , and K = tα, integers between 15.87 and 252 are within the required range. The unreported simulation study ﬁnds that if K is within the range, increasing K only elevates the computational burden without marginal contribution. We suggest the smallest integer K that satisﬁes the necessary condition as an optimal choice for K. Our speciﬁc recommendation of optimal window sizes for one-week, one-day, one-hour, 30-minute, 15-minute, and 5-minute data are 7, 16, 78, 110, 156, and 270, respectively.

## 1.4 Selection of rejection region

In this subsection, we address the rejection region for our proposed test. In effect, we demonstrate that the suggested rejection region allows us to distinguish jumps more precisely at higher frequencies of observation in Section 3.

As described in Theorems 1 and 2, our test statistics present completely differentlimitingbehaviordependingontheexistenceofjumpsatthetestingtimes. If there is no jump at the testing time, our test statistic follows approximately a normal distribution. If there is a jump, however, the test statistic becomes very large. To determine a reasonable rejection region, we raise a question of how large our test statistic can be when there is no jump. Hence, we ﬁrst study the asymptotic distribution of maximums of our test statistics under the absence of jumps at any time in (ti−1,ti]. Such a distribution then guides us to choose the relevant threshold for the test to distinguish the presence of jumps at a testing time. Lemma 1 states the limiting distribution of the maximums as follows:

Lemma 1. If the conditions for L(i), K, c, and A¯ n are as in Theorem 1, then

- as t → 0,

maxi∈A¯n |L(i)| − Cn

Sn → ξ, (12) where ξ has a cumulative distribution function P(ξ ≤ x) = exp(−e−x),

(2logn)1/2

logπ + log(logn) 2c(2logn)1/2

1 c(2logn)1/2

, (13)

Cn =

and Sn =

c −

where n is the number of observations. Proof of Lemma 1. See Appendix A.4.

In short, the main idea in selecting a rejection region is that if our observed test statistics are not even within the usual region of maximums, it is unlikely that the realized return is from the continuous part of the jump diffusion model. To apply this result for selecting a rejection region, for instance, we can set a signiﬁcance level of 1%. Then, the threshold for |L(i)|−C

Sn is β∗, such that P(ξ ≤ β∗) = exp(−e−β∗) = 0.99. Equivalently, β∗ = −log(−log(0.99))

n

= 4.6001. Therefore, if |L(i)|−C

Sn > 4.6001, then we reject the hypothesis of no jump at ti.

n

## 2. Misclassiﬁcations

In this section, after deﬁning four different types of misclassiﬁcation that can occur in our study, we demonstrate that the probability of such a misclassiﬁcation becomes negligible at higher frequencies of observation. For a single

testing time, say ti, there can be two kinds of misclassiﬁcation. The ﬁrst is when there is a jump in interval (ti−1,ti], but the test fails to reveal its existence. We call this a failure to detect actual jump (FT Di) at ti. The second kind of misclassiﬁcation is when there is no jump in (ti−1,ti], but the test wrongly concludes there is one. We call this a spurious detection of jump (SDi)

- at ti. It is usually the case that we do this test several times with time-series data. Global extension of these concepts is straightforward. If there are some jumps over the whole time horizon, [0, T], but the test fails to detect any one of them, we call it a global failure to detect actual jump (GFTD). If there are some returns that are not due to jumps, but the procedure wrongly declares any one of them as due to a jump, we call it a global spurious detection of jump (GSD). We will use the following mathematical notations to explain the above situations. We let An be jump times among n observations and Bn be times at which the test declares the presence of a jump. We use Ji (J is for jumps) to denote the event that there is a jump in (ti−1,ti]. Note that Ji = {i ∈ An}. Di (D is for declaring jumps) denotes the event that our test declares a jump in (ti−1,ti]. In this case, Di = {i ∈ Bn}. Then, the following statements hold:

failure to detect actual jump at ti (local property) (FT Di) = Ji DiC,

spurious detection of jump at ti (local property) (SDi) = JiC Di,

n

Ji DiC ,

failure to detect actual jumps (global property) (GFT D) =

i=1

n

JiC Di .

spurious detection of jumps (global property) (GSD) =

i=1

With these new notations, we now generalize the example at the end of Section 1, using a ﬁxed signiﬁcance level to any signiﬁcance level αn that approaches 0. Alternatively, βn approaches ∞. In Theorem 3 and Corollary 1, we explicitly show that both the conditional and unconditional probabilities of global failure to detect actual jumps (GFTD) approach 0. They state specifically the convergence rates to show how fast these probabilities converge to 0.

- Theorem 3. Let βn be the (1 − αn)th percentile of the limiting distribution of ξ in Lemma 1, where αn is the signiﬁcance level of the test. Let N be the number of jumps in [0, T]. Then, the probability of global failure to detect actual jumps (GFTD) is

P(GFTD|N) =

2 √2π

### ynN + o(ynN), (14)

where yn = (βnSn + Cn)cσ √n logn, √ t. Therefore, as long as βn → ∞ slower than

P(GFTD|N) −→ 0 (15) as t → 0.

## Proof of Theorem 3. See Appendix A.5.

If jumps arrive randomly, as in a Poisson process with constant intensity λ, one can expect the probability to be as in Corollary 1.

Corollary 1. If J(t) is a Poisson process with jump intensity λ, and the observation time horizon is from 0 to T, then

E[P(GFT D)] =

2 √2π

ynλT + o(ynλT). (16)

Theorem 4 also shows that the conditional probability of global spurious detection of jumps (GSD) approaches 0 quickly. The corresponding convergence rate is provided as the signiﬁcance level αn approaches 0 or, equivalently, the rejection threshold βn approaches ∞.

- Theorem 4. Let βn be as in Theorem 3. Again, let N be the number of jumps in [0, T]. Then, as t → 0, the probability of spurious detection of jumps (GSD) is

P(GSD|N) = exp(−βn) + o(exp(−βn)). (17) Therefore, as βn → ∞,

P(GSD|N) −→ 0, (18) as t → 0.

Proof of Theorem 4. See Appendix A.6.

The immediate consequence of our ﬁndings in Theorems 3 and 4 is that we can classify actual and spurious jumps precisely so that we obtain an accurate stochastic jump intensity estimator based on our nonparametric test. If both probabilities in Theorems 3 and 4 become negligible, then the likelihood of global misclassiﬁcation by either GFTD or GSD is also negligible, as stated in

- Theorem 5.

Theorem5. If (T)istheestimatorofthenumberofjumpsin[0, T]usingour test(whichisformallyacumulativejumpintensityestimator),and actual(T) = N is the number of actually realized jumps in [0, T], then the probability of global misclassiﬁcation is

P(  = actual|N) = P(GFTD or GSD|N)

2 √2π

ynN + exp(−βn) + o(exp(−βn)). (19)

=

√2√nTlogNn). Moreover, the overall optimal convergence rate is σ

It can be minimized at β∗n = −log( σ

√2√nTlogNn.

- Proof of Theorem 5. See Appendix A.7.

- 3. Monte Carlo Simulation

In this subsection, we examine the effectiveness of our test using a Monte Carlo simulation. Our asymptotic argument in previous sections requires that the sampling interval t converges to 0. This ideal requirement cannot be perfectly met in real applications. This subsection investigates the ﬁnite sample performance of the test. The main result from this simulation proves that as we increase the frequency of observation the precision of our test increases. For series generation, we used the Euler-Maruyama stochastic differential equation (SDE) discretization scheme (Kloeden and Platen, 1992), an explicit order 0.5 strong and order 1.0 weak scheme. We discard the burn-in period—the ﬁrst part of the whole series—to avoid the starting value effect. Throughout, we use the notation t = 252×1nobs, with nobs as the number of observations per day.

- 3.1 Constant volatility We ﬁrst consider the simplest model in the class, with a ﬁxed volatility. Table 1 presents the probability of spurious detection of jump (SDi). We simulate two

Table 1 Probability of spurious detection P(SDi) freq σ = 0.3 (SE) σ = 0.6 (SE) SV (SE)

24-hour 1.3305e-03 (7.4050e-05) 1.3305e-03 (7.6239e-05) 3.9110e-03 (1.3319e-04) 12-hour 5.7380e-04 (3.4901e-05) 5.3222e-04 (3.3570e-05) 2.3306e-03 (7.7336e-05) 6-hour 2.0696e-04 (1.4460e-05) 2.1209e-04 (1.4790e-05) 1.3289e-03 (4.3670e-05) 2-hour 5.2879e-05 (4.3701e-06) 5.5911e-05 (4.2684e-06) 4.8131e-04 (1.6731e-05) 1-hour 2.1775e-05 (1.9032e-06) 2.5126e-05 (2.0353e-06) 2.7688e-04 (1.0062e-05) 30-minute 8.8436e-06 (8.3749e-07) 8.6768e-06 (8.3965e-07) 1.4467e-04 (7.2952e-06) 15-minute 3.4947e-06 (3.7430e-07) 4.1876e-06 (4.2736e-07) 8.9449e-05 (4.2818e-06)

The encompassing model is d log S(t) = µ(t)dt + σ(t)dW(t). Constant volatility sets σ(t) = σ at 30% and 60%. Stochastic volatility (SV) assumes the Afﬁne model of Heston (1993), speciﬁed as dσ2(t) =

θ0 + θ1σ2(t) dt + ωσ(t)dB(t), where B(t) denotes a Brownian motion. The table shows means and standard errors (in parentheses) of probability of spurious detection P(SDi) at time ti. The signiﬁcance level α is 5%. freq denotes the frequency of observations.

Table 2 Probability of detecting actual jump [1 − P(FT Di)] Jump Size 3σ 2σ 1σ 0.5σ 0.25σ 0.1σ

Constant volatility σ at 30%

freq = 24-hour 0.9920 0.9880 0.9810 0.9270 0.4690 0.0260

(0.0028) (0.0034) (0.0043) (0.0082) (0.0158) (0.0050) freq = 6-hour 0.9860 0.9780 0.9820 0.9700 0.9050 0.1520

(0.0037) (0.0046) (0.0042) (0.0054) (0.0093) (0.0114) freq = 1-hour 0.9950 0.9860 0.9890 0.9890 0.9770 0.8880

(0.0022) (0.0037) (0.0033) (0.0033) (0.0047) (0.0100) freq = 15-minute 0.9980 0.9970 0.9960 0.9920 0.9970 0.9820

(0.0014) (0.0017) (0.0020) (0.0028) (0.0017) (0.0042) Jump Size 3 σ(t) 2 σ(t) 1 σ(t) 0.5 σ(t) 0.25 σ(t) 0.1 σ(t)

Stochastic volatility (SV)

freq = 24-hour 0.9470 0.9330 0.8540 0.5720 0.2500 0.0320

(0.0071) (0.0079) (0.0112) (0.0157) (0.0137) (0.0056) freq = 6-hour 0.9770 0.9690 0.9410 0.8480 0.5320 0.1400

(0.0047) (0.0055) (0.0075) (0.0114) (0.0158) (0.0110) freq = 1-hour 0.9870 0.9860 0.9830 0.9610 0.8770 0.5260

(0.0036) (0.0037) (0.0041) (0.0061) (0.0104) (0.0158) freq = 15-minute 0.9970 0.9990 0.9980 0.9920 0.9610 0.8100

(0.0017) (0.0010) (0.0014) (0.0028) (0.0061) (0.0130)

The encompassing model is d log S(t) = µ(t)dt + σ(t)dW(t) + Y(t)dJ(t). Constant volatility sets σ(t) = σ at 30%. Stochastic volatility (SV) assumes the Afﬁne model of Heston (1993), speciﬁed as dσ2(t) = θ0 + θ1σ2(t) dt + ωσ(t)dB(t), where B(t) denotes a Brownian motion. The table contains means and standard errors (in parentheses) of probability of detecting actual jumps [1 − P(FT Di)] at time ti. The signiﬁcance level α is 5%. The jump sizes are set in comparison with volatility level: 3σ means jump sizes are set at three times of volatility level. For stochastic volatility, the jump size depends on the mean of volatility σ(t) = E[σ(t)]. f req denotes the frequency of observations.

constant volatility diffusion processes with ﬁxed spot volatilities at realistic annualized values of 30% and 60%, respectively. One thousand series of returns over one year are simulated at several different frequencies from daily to 15-minute returns. The signiﬁcance level for this study is 5%. Table 1 shows thatincreasingthefrequencyofobservationsreducestheprobabilityofspurious detection of jump (SDi).

Table 2 shows the probability of success in detecting an actual jump, that is,

- 1 minus the probability of failure to detect actual jump (FTDi). One thousand simulated tests at different frequencies, from daily to 15-minute, are performed. Arrivals of jumps with six different magnitudes are assumed at 300–10% of the given volatility level of 30%. We choose different jump sizes to present that it is harder to detect smaller-sized jumps at low frequency. However, we show that as we increase the frequency, we obtain very high detection power (above 98%), even for very small-sized jumps. For instance, we observe from Table 2 that when the magnitudes of relevant jumps are equal to 10% of volatility, econometricians are less likely to distinguish between price changes that result from diffusion and those from the actual jump in a low-frequency environment, such as with daily observations. This study shows that only 2% of jumps can be detected using daily returns. In contrast, at observation frequencies of every

30 minutes or higher, we can distinguish the difference more than 95% of the time.

- 3.2 Stochastic volatility We examine how the test performs differently for stochastic volatility. We ﬁrst consider a one-factor Afﬁne model and compare with the constant volatility case, studied in Subsection 3.1. The model is as in Heston (1993), which is speciﬁed as the square root processes (used by Cox, Ingersoll, and Ross, 1985)

dσ2(t) = θ0 + θ1σ2(t) dt + ωσ(t)dB(t), (20)

where B(t) denotes a Brownian motion. For the simulation, we used the parameter estimates from equity markets found in the empirical study by Bakshi et al., (2005), Table 2, to mimic the real equity markets. We assume no correlation between the Brownian motion in volatility and the random terms in the return process, which leaves us with no leverage effect in this simulation. The jump size and the Poisson jump counting process are set to be the same

- as in the case of constant volatility. We include the result when the volatility is stochastic in Tables 1 and 2 in order to allow direct comparison with the constant volatility case. It conﬁrms our intuition that if the volatility changes over time, it would be more difﬁcult to disentangle jumps. At every frequency, the corresponding spurious detection probability for stochastic volatility is greater than that for ﬁxed volatility. We ﬁnd the similar result from the comparison in Table 2: the probability of successful detection of a jump at some given time decreases under stochastic volatility. For another robustness check, we also study the case where the stochastic volatility is driven by a general model that accommodates stochastic elasticity of variance and a nonlinear drift (e.g., A¨ıt-Sahalia, 1996; A¨ıt-Sahalia, 2004; and Bakshi et al., 2005) as

dσ2(t) = θ0 + θ1σ2(t) + θ2σ4(t) + θ3σ−2 dt

+ ω0 + ω1σ2(t) + ω2σ2ω

3dB(t). (21)

Again, using the estimates for all the nested models in Bakshi et al., (2005), we obtain results similar to those under the Afﬁne models presented earlier. The only impact of nonlinearity of drift is in the rate of convergence. In other words,

- at higher frequencies, such as 15-minute or higher, we ﬁnd that the success rates of detecting actual jumps become similar to those for the Afﬁne case, though at lower frequencies, such as daily, we have lower success rates. We also calculate the sample skewness and kurtosis that surrogate tail asymmetry and tail size and ﬁnd that both decrease (in absolute terms for skewness) to normal cases as we increasefrequency.Hence,ourasymptoticresultisnotaffected,althoughsmallsampledistributionsofourtestwillbeaffectedatlowerfrequenciessuchthatthe precision of our test at lower frequency decreases, as shown in the simulation results of Tables 1 and 2. To capture the effect of skewness and kurtosis at

Table 3 Global misclassiﬁcation

Jump size 3σ 2σ 1σ 0.5σ 0.25σ

Probability of global misclassiﬁcation freq = 24-hour 0.2140 0.2120 0.1640 0.3540 0.9860

(0.0184) (0.0183) (0.0166) (0.0214) (0.0053) freq = 12-hour 0.1252 0.1312 0.1531 0.1173 0.7714

(0.0148) (0.0151) (0.0161) (0.0144) (0.0188) freq = 6-hour 0.0477 0.0407 0.0407 0.0506 0.0755

(0.0095) (0.0088) (0.0088) (0.0098) (0.0118) freq = 2-hour 0.0036 0.0046 0.0023 0.0063 0.0050

(0.0027) (0.0030) (0.0021) (0.0035) (0.0031) freq = 1-hour 0.0012 0.0012 0.0005 0.0007 0.0008

(0.0015) (0.0015) (0.0010) (0.0011) (0.0013) freq = 30-minute 0.0001 0.0001 0.0006 0.0004 0.0002

(0.0003) (0.0004) (0.0011) (0.0009) (0.0006) freq = 15-minute 0.0001 0.0001 0.0001 0.0002 0.0000

(0.0001) (0.0002) (0.0005) (0.0006) (0.0001)

The table contains means and standard errors (in parentheses) of probability of global misclassiﬁcation of jumps, discussed in Theorem 5. P (T)  = actual(T) is by either global spurious detection of jumps (GSD) or global failure to detect actual jumps (GFT D), where (T) is the number of jumps in [0, T] using our test, and actual(T) is the number of actually realized jumps. The model under consideration is a jump diffusion process with Afﬁne stochastic volatility and jumps of various sizes. The signiﬁcance level α is 5%. f req denotes the frequency of observations.

lower frequencies, one may apply the Edgeworth expansion method. For an application of Edgeworth expansion in the context of realized volatility, see Zhang,Mykland,andA¨ıt-Sahalia(2005a).ForgeneraldiscussionofEdgeworth expansionfordependentdata,seeGoetzeandHipp(1983)andMykland(1993). In summary, the results show that stochastic volatility reduces the precision of jump detection. However, this study does conﬁrm that if we increase the frequency of observation, we obtain improved power of jump detection.

- 3.3 Global misclassiﬁcation In this subsection, we examine the global likelihood of misclassiﬁcation by either global spurious detection of jumps (GSD) or global failure to detect actual jumps (GFTD), as studied in Theorem 5. This tells us how accurately we can locate actual jump arrival times. We simulate 500 different series of one-year observations at different frequencies from daily to 15-minute returns. We consider ﬁve different jump sizes from 300% to 25% of volatility level. As discussed in Theorem 5, we ﬁnd that the likelihood of misclassiﬁcation becomes negligible at higher frequencies. Table 3 presents the probability that the number of jumps counted by our test is not equal to the actual number of jumps; this shows that global misclassiﬁcation of jumps is negligible.
- 3.4 Comparison with other jump tests Comparable tests to ours are those introduced by Barndorff-Nielsen and Shephard (2006; hereafter BNS) and Jiang and Oomen (2005; hereafter JO), both of which are also nonparametric approaches, making test results robust to

model speciﬁcation. This subsection discusses the differences between these tests (BNS and JO) and ours (LM). Furthermore, we argue, by simulation, that our test outperforms these two tests. Our study measures the performance of tests by the probability of global success in detecting actual jumps and global spurious detection of jumps in one day, which can be alternatively taken as power and size for each test.

The main differences between the two others and ours are as follows. BNS takes the difference (or ratio) between the realized quadratic variation and bipower variation during a time interval to indicate the presence of jumps in that interval. JO’s swap variance test solves the problem with a similar approach to BNS’s. The only difference between BNS and JO is that instead of using bipower variation, JO uses cumulative delta-hedged gain or loss of a variance swap replicating strategy. They both provide asymptotic null distributions for their jump test statistics. One of the features of their tests, as described in BNS, is that they cannot distinguish two jumps a day with low variance and one jump with high variance in terms of detection rates. The reason for this problem is that these tests depend on integrated quantities. JO’s swap variance test shares this feature because it also employs integrated quantities. For instance, suppose there are two jumps in a day and an analyst chooses one day as the interval for their test. Even if the presence of jumps in that day can be recognized, the other two tests cannot determine how many jumps occurred, whether the jump(s) was (were) negative or positive, at what time of day the jump(s) occurred, and how large each jump was. These issues can, however, be resolved by our test.

Furthermore, our test also outperforms the BNS and OJ tests. We compare the performance of the three tests in terms of probability of global success in detecting actual jumps within a given interval and probability of global spurious detection of jumps in that interval. Our test does not use the conventional terms of size and power, but introduces the misclassiﬁcation of jumps in Section

- 2, because the detection criterion for our test is based on the distribution of maximums of null distribution, which is different from the usual hypothesis tests, and we do not select one model over another when we do a single test for jump detection. In essence, the probability of global success in detecting actual jumps is the power of the test, and the probability of global spurious detection of jumps is the size of the test.

We now report simulation results comparing the power and size of our new test to BNS’s linear test and OJ’s difference test. For the probability of global success to detect actual jumps (power), the simulation introduces one jump within one day to a diffusion process with a constant volatility. We consider 3000 simulated series of a process in one day, with each jump arriving randomly as a Poisson process. The number of jumps was set to be one per day. If there is a given number of jumps for some given time (one day in this study), then the Poisson jump arrival time is uniformly distributed (see Ross, 1995). Hence, we randomly select the arrival times from a uniform distribution. σ is set at 30%, as in the previous simulation. The standard deviation of jump size distribution is

Table 4 Comparison with other jump tests

Probability of global success to detect actual jumps [1 − P(GFTD)] 100% Our test (LM) Linear test (BNS) Difference test (OJ)

f req 1 − P(GFTD) (SE) 1 − P(GFTD) (SE) 1 − P(GFTD) (SE)

2-hour 0.8260 (0.0120) 0.8110 (0.0124) 0.7690 (0.0133)

- 1-hour 0.8720 (0.0106) 0.8460 (0.0114) 0.8210 (0.0121) 30-minute 0.9190 (0.0086) 0.8990 (0.0095) 0.8820 (0.0102) 15-minute 0.9410 (0.0075) 0.9260 (0.0083) 0.9200 (0.0086) 50% Our test (LM) Linear test (BNS) Difference test (OJ)

f req 1 − P(GFTD) (SE) 1 − P(GFTD) (SE) 1 − P(GFTD) (SE)

- 2-hour 0.7480 (0.0137) 0.7110 (0.0143) 0.6470 (0.0151)

- 1-hour 0.8410 (0.0116) 0.8030 (0.0126) 0.7550 (0.0136) 30-minute 0.9070 (0.0092) 0.8590 (0.0110) 0.8390 (0.0116) 15-minute 0.9140 (0.0089) 0.8840 (0.0101) 0.8630 (0.0109) 25% Our test (LM) Linear test (BNS) Difference test (OJ)

f req 1 − P(GFTD) (SE) 1 − P(GFTD) (SE) 1 − P(GFTD) (SE)

- 2-hour 0.6140 (0.0154) 0.5330 (0.0158) 0.4400 (0.0157)

- 1-hour 0.7520 (0.0137) 0.6380 (0.0152) 0.5540 (0.0157) 30-minute 0.8060 (0.0125) 0.7220 (0.0142) 0.6560 (0.0150) 15-minute 0.8690 (0.0107) 0.7960 (0.0127) 0.7470 (0.0138)

Probability of global spurious detection of jumps [P(GSD)] Our test (LM) Linear test (BNS) Difference test (OJ)

f req P(GSD) (SE) P(GSD) (SE) P(GSD) (SE)

- 2-hour 0.0000 (0.0000) 0.2426 (0.0061) 0.0484 (0.0030) 1-hour 0.0000 (0.0000) 0.1686 (0.0053) 0.0076 (0.0012) 30-minute 0.0000 (0.0000) 0.1190 (0.0046) 0.0010 (0.0004) 15-minute 0.0000 (0.0000) 0.0840 (0.0039) 0.0000 (0.0000)

The table shows the probability of global success in detecting actual jumps [1 − P(GFT D)] (equivalent to power) and the probability of global spurious detection of jumps P(GSD) (equivalent to size) within one day by our test (LM), linear test of Barndorff-Nielsen and Shephard (2006) (BNS), and difference test of Jiang and Oomen (2005) (JO). The null model is a diffusion process with constant volatility at 30% and the alternative of a jump diffusion process containing one jump per day with constant volatility at 30%. The time interval for integration of linear test (BNS) and difference test (OJ) is one day. f req denotes the frequency of observations. The jump sizes are 100%, 50%, and 25% of the volatility level.

chosen at 100%, 50%, 25%, and 10% of σ. Our test (LM) outperforms BNS and JO at all jump sizes. For the probability of global spurious detection of jumps (size), we apply the same analysis without introducing jumps in the one-day interval. Table 4 shows the superior performance of our test. In conclusion, our test performs better than BNS and JO for all jump sizes, numbers of jumps, and frequencies.

## 4. Implications of Identifying Jump Dynamics

Precise identiﬁcation of jump arrival dynamics, including timing and jump size distribution, using our new test creates important implications for, among others, ﬁnancial derivative security pricing. Because the test is applicable to all kinds of ﬁnancial variables, such as stock returns and volatility, interest rates, and exchange rates, as long as high-frequency observations are available, we ﬁrst discuss general implications for pricing equity options, index options, currency options, interest rate derivatives, volatility derivatives, and bond pricing.

Then we apply our test to real individual equity and S&P 500 Index returns and focus our discussion speciﬁcally on equity option markets based on our empirical ﬁndings.

- 4.1 Application to general option and bond pricing models Much of the option and bond pricing literature estimates jumps by various parametric inference methods such as the Calibration method, (Implied State) Generalized Method of Moments (GMM), (Simulated) Maximum Likelihood Estimation (MLE), Efﬁcient Method of Moment (EMM), or Bayesian approach (see Bakshi et al., 1997; Bates, 2000; Pan 2002; Schaumburg 2001; Chernov et al., 2003; Eraker, Johannes, and Polson, 2003; A¨ıt-Sahalia, 2004; Piazzesi, 2003; and A¨ıt-Sahalia and Jacod, 2005). As is well known, parametric approaches run the risk of incorrect speciﬁcation for functionals in their chosen models. This is not the case with our nonparametric test. Many of the above-mentioned studies realize that jump parameters are difﬁcult to pin down even with both time-series and cross-sectional data. Biased estimates can lead to increased security pricing errors. They also conclude that the models can be improved by introducing the stochastic jump intensity that captures the timevarying nature of the ﬁnancial markets. Some studies allow jump arrival rates to depend on variables such as latent volatility, latent jump size, or market information in an Afﬁne or non-Afﬁne fashion (see Chernov et al., 2003; Piazzesi, 2003; and Dubinsky and Johannes, 2006, for instance). Though incorporating state variables is intuitively attractive, these existing (computationally intensive) parametric procedures become quite complicated to implement due to the discontinuity introduced by jumps and the increased number of parameters. Moreover, they often end up ﬁnding counterintuitively insigniﬁcant outcomes.

If our test is applied initially to determine the jump intensity and jump size distribution, and to search for observable variables that are signiﬁcantly associated with jump arrivals, the inference for the whole model can become much simpler. This beneﬁt is discussed in Tauchen and Zhou (2005), who applied Barndorff-Nielsen and Shephard (2006) to empirically prove that jump volatilities explain credit spread and credit default swap (CDS) spread better than other risk factors in the markets. Given the market information determined by the jump test, which can predict or explain jump arrivals, such as earnings announcements and other company-speciﬁc news releases for equities discussed in Subsection 4.2, equity option pricing models can be improved with reduced uncertainty involved with jumps.

## 4.2 Empirical analysis for U.S. equity option markets

In this subsection, we apply our new test on three major U.S. individual equity and S&P 500 Index returns to determine their jump dynamics, which may suggest different option pricing models as well as provide supporting evidence for ﬂatter implied volatility smiles of individual equity options compared to index options (see Bakshi et al., 2003).

We use ultra-high-frequency data from transactions on the NYSE that are collected from the TAQ database. We calculate stock returns by taking differences of log transaction prices and multiplying all returns by 100 to present them as percentages. The time span is three months, from 1 September to 30 November 2005, which represent the most recent data available, and which have never been investigated in the literature. We choose three equities (WalMart (WMT), IBM (IBM), and General Electric (GE)) and the S&P 500 Index to compare their different jump dynamics. Because the simulation study in Section 3 shows that a 15-minute frequency is high enough for our test to achieve a sufﬁcient power to detect actual jumps, we choose 15-minute returns to generate the empirical evidence, and we present the results in Table 5. With this choice of frequency, results are not greatly affected by the presence of market microstructure noise. Therefore, the evidence presented here is robust to the effect of the noise. The signiﬁcance level for all analyses is 5%. The outcomes of the tests are: each jump arrival date and time, jump size, and mean and variance of the detected jump size distribution. We do not assume that there is no more than one jump per day, but we do assume that when a jump occurs, the jump size dominates the return. After detecting the realized jumps, we search for real-time ﬁnancial news and information releases around jump arrival times using the Factiva database in order to examine their association with jump arrivals. Sources used in the Factiva search include the Wall Street Journal, the Financial Times, and the Dow Jones and Reuters newswires.

Overall results indicate that jumps do not occur regularly, so that existing option pricing models with constant jump intensity are not appropriate. Detailed results for individual equities are explained as follows. First, we ﬁnd that most jumps in equity prices under consideration arrive around the time of a market’s opening. Except in one or two cases, jumps were always associated with news events. During the three months, there was one scheduled corporate news event for each company—the third-quarter earnings announcement. On the earnings announcement date (EAD), there was always a jump in the corresponding series. This evidence coincides with the individual equity option pricing model in Dubinsky and Johannes, (2006), who incorporate deterministic jump events conditional on scheduled EADs. However, as in Table 5, in addition to scheduled announcements, we ﬁnd that a majority of stock price jumps are associated with other unscheduled company-speciﬁc news events. The implication of this ﬁnding is that scheduled earnings announcements as a deterministic jump predictor in earlier studies are not sufﬁcient to model stochastic jump arrivals in individual equity prices. Other company-speciﬁc news releases, in addition to EADs, should be incorporated in accordance with the evidence in Table 5. Similarly, jumps in the S&P 500 Index are associated with market-wide news such as FOMC meetings and macroeconomic reports. This empirical ﬁnding is consistent with the notion that signiﬁcant ﬁnancial market jumps are related to responses to macroeconomic news announcements (see Andersen et al., 2003).

12Sep269:30a.m.1.29LawSuitNSep139:45a.m.0.76AnnounceN−

34Oct069:31a.m.1.12SalesUpYSep199:30a.m.0.74DealNewsN−

56NSep219:30a.m.0.96OptionMarketNOct109:30a.m.1.53NewLaunch−

78Oct149:30a.m.0.93LawSuitNSep279:45a.m.1.03GoodNewsN

910Oct1910:45a.m.0.84InvestmentNOct079:45a.m.1.04GoodNewsN

1112Oct319:30a.m.1.33SalesUpNOct109:30a.m.0.98NewProductN

1314Nov159:48a.m.1.25EADNOct119:30a.m.1.24ExpansionN−

1516NOct189:30a.m.1.99EADYNov189:30a.m.1.11Announce

- 17Oct199:30a.m.1.29RivalEADY−
- 18Nov189:30a.m.1.30AnnouncementN

DateTimeSize(%)NewsSDateTimeSize(%)NewsS

DateTimeSize(%)NewsSDateTimeSize(%)NewsS

WMTWMTIBMIBM08625088170383011801====µσµσ....yyyy

WalMart(WMT)IBM(IBM)

GeneralElectric(GE)S&P500

DynamicsofjumparrivalinindividualequitiesandtheS&P500index

Table5

Theabovetablecontainsresultsofourjumptest:detectedjumpdates,jumptimes,andobservedjumpsizeswithassociatednewseventsofthreeU.S.individualequitiesandtheS&P

watchline,16.Earningsfallonitems,17.EMC(itskeyrival)earningsnetup94%,18.Globalmovementmanagementinitiative,19.Financialconglomeratebackeditsearningsforecast

Sdenoteswhetherthenewswasscheduled(Y)ornot(N).FOMCdenotestheFederalOpenMarketCommitteemeetingdateandEADdenotestheearningsannouncementdatesof

standarddeviationofrealizedjumpsizesofacompanyduringoneyearfrom1July2005to30June2006.The-valuesofallthedetectedjumpsreportedherearelessthan5%.ticp

unexpectedly,20.Raiseitstargetforthefederalfundrateby25basispoints,21.Defensecontracts,22.Economicreportshowingareboundindurablegoodsordersandconsumer

12.Newvirtualizationtechnologiesfromsoftwaretosystems,13.Smallestproﬁtgaininmorethan4years,14.Speechsolutionoffering,15.PartnershipwithFossiltoproducefashion

tictic500Index.TheyarebasedontransactionpricesfromtheNewYorkStockExchange(NYSE)during3monthsfrom1Septemberto30November2005.andarethemeanandµσyy

Relatednewsreportedareasfollows.1.ApotentialTommyHilﬁgersuitor,2.GlobalpartnershippactwithNuHorizonsElectronicsCorp,3.Salesmeetitsexpectation,4.Negative

correspondingcompanies.Thespeciﬁcnews-retrievalsourcesusedintheFactivasearchincludethe,the,andtheDowJonesandReutersnewswires.WallStreetJournalFinancialTimes

newsofSiebeldealwithOracle,itsrivalindatabasesoftware,5.Metro7,anewclothingbrandlaunch,6.Unusualoptionactivity,7.Uncollectedsalestaxes,8.Deliveryofmostsecure

versionofLinuxavailable,9.$25millioninvestmenttoestablishaprivate-equityfund,10.“Healthy"hardwaresalesbookingof$12billionormore,11.Salesupaboveitspriorforecast,

conﬁdenceimprovement,23.SyndicatewithMorganStanley,24.Solidgrowthinequipmentandservices,25.Earningsrise15%,26.Finalphaseofinsuranceportfoliotransformation.

1920Sep159:45a.m.0.70GoodNewsNSep203:00p.m.0.45FOMCY−

2122Sep219:30a.m.0.95BadNewsNNov299:30a.m.0.96GoodNewsY−

GEGES&PS&P100171132402816260====µσµσ....yyyy

- 23Oct069:31a.m.2.03AnnounceN
- 24Oct079:30a.m.0.92GoodNewsN
- 25YOct149:30a.m.1.11EAD
- 26Nov189:30a.m.2.20AnnounceN

Second,wecomparetheresultsforindividualequitiesandtheS&P500Index in Table 5. It shows that the frequency of jump occurrences in the index is much less than in the three individual equities. Another difference between jumps in individual equities and in the S&P 500 Index is the jump size distribution. The mean of jumps in the index (0.2036) is smaller than those in the three stocks (0.3014, 0.3487, and 0.4278). The variance of jumps in the index (0.5521) is also smaller than that in the stocks (1.2689, 0.9745, and 1.2050). We used oneyear observations from 1 July 2005 to 30 June 2006 to obtain a reliable mean and variance, avoiding problems with small samples. In summary, individual stocks have more frequent jumps of greater size than the S&P 500 Index. According to deﬁnition of the index, the index should in theory jump when the individual component stock jumps. We refer, however, to detected jumps as those of empirically and economically signiﬁcant magnitudes. The presence of jumps in both series implies that both individual stocks and the index have fattailed return distributions in physical measures. More frequent and larger-sized jumps in individual stock returns are likely to make the tails fatter.

Finally, this empirical outcome supports the explanation of Bakshi et al., (2003) for the implied volatility smiles of equity options. They economically prove that the negative risk-neutral skewness is feasible as long as the physical return distributions are fat-tailed and investors are risk averse. The evidence of different structure of fat-tailed return distributions supports their economic reasoning for the implied volatility curve, coupled with different levels of risk aversion of investors participating in the two different option markets.

## 5. Concluding Remarks

Realizing the difﬁculty in estimating jump parameters and the importance of incorporating market information into option pricing models, we introduce a new jump test to characterize the dynamic jump mechanism. Monte Carlo simulation proves that our test can precisely disentangle jump arrivals using high-frequency observations, allowing us to investigate the stochastic nature of jump dynamics and to search for observable information relevant to jump arrivals in any kind of ﬁnancial time series. We perform an empirical study using our test and provide evidence of strong association between jumps and news events in the U.S. equity markets. Individual stock jumps occur with earnings announcements and other company-speciﬁc news releases, whereas the S&P 500 Index jumps with more overall market news such as FOMC meetings. These results suggest the need to consider company-speciﬁc news releases for individual equity option pricing and market-wide news releases for the index option pricing. We also ﬁnd more frequent jumps with greater mean and variance in individual equities than the index returns, which supports the economic explanation by Bakshi et al., (2003) on negative risk-neutral skewness.

Though our test is designed to detect Poisson-type rare jumps in jump diffusion frameworks, it is still applicable to discrete observations from suitably modiﬁed pure jump models such as inﬁnite-activity L´evy processes as in Carr and Wu (2004) and Wu (2006). Distinguishing very small magnitude jumps from such models is beyond the scope of the current article and is one possible direction forfutureresearch. Another extension of thetestistotake intoaccount the presence of market microstructure noise in ultra-high-frequency data when testing as in Andersen et al. (2006), which we are currently developing. Finally, since the test is designed to use high-frequency observations, its application on market microstructure problems would also be interesting.

Appendix A A.1 The Nonzero Drift

The main conclusion of Theorem 1 is not altered for the case where we estimate the nonzero drift. A modiﬁed version of Deﬁnition 1 for this case is as follows:

Deﬁnition 1.1. The statistic Lµ(i), which tests at time ti whether there was a jump from ti−1 to ti, is deﬁned as

log S(ti)/S(ti−1) − mi σ(ti)

Lµ(ti) ≡

, (A1)

where

σ(ti) is as in Equation (8) and mi =

i−1

1 K − 1

(log S(tj)/S(tj−1)).

j=i−K+1

This demeans the return at time ti using the average return in the window. The result similar to Theorem 1 holds for the case of nonzero drift in Theorem 1.1.

Theorem 1.1. Let Lµ(i) be as in Deﬁnition 1.1 and the window size K = Op( tα), where −1 < α < −0.5. Suppose the process follows (1) or (2) and Assumption 1 is satisﬁed. Let A¯ n be the set of i ∈ {1,2,...,n} so that there is no jump in (ti−1,ti]. Then, as t → 0,

3

2−δ+α− ), (A2)

sup

|Lµ(i) − Lµ(i)| = Op( t

i∈A¯ n

where

Ui − U¯i−1 c

Lµ(i) =

.

Here, U¯i−1 = K1−1

i−1 j=i−K+1 Uj and the rest of notations are the same as in

Theorem 1. Proof of Theorem 1.1. See Appendix A.2.

The error rate is the same as in the zero drift case, because the error due to the drift term is dominated by the error due to the diffusion part. Lµ(i) asymptotically follows a normal distribution with its mean 0 and variance

c2(K−1) → c12 , since K → ∞. Our choice of window size K makes the effect of jumps on mˆ i vanish because of the property of the Poisson process for rare jumps: there can be no more than a single jump in an inﬁnitesimal time interval. Because there can be only a ﬁnite number, say F, of jumps in the window, the statistic for the nonzero drift case becomes

K

Ui − U¯i−1 c −

F × Y(τ) cσ × (K − 1)√ t

Lµ(i) ≈

i−K,ti−1]. (A3)

Iτ∈(t

The second term will disappear because of the condition K√ t → ∞. This provesthatjumpsinthewindowhaveasymptoticallynegligibleeffectontesting jumps with our choice of K.

A.2 Proof of Theorems 1 and 1.1 in Appendix A.1 For ti−K < t < ti,

t

t

log S(t) − log S(ti−K) =

µ(u)du +

σ(u)dW(u). (A4)

ti−K

ti−K

Given the imposition of Assumption 1, we have (from A1.1)

and

ti

3

2− ) (A5)

µ(u)du − µ(ti−1) t = Op( t

ti−1

ti

3

2+α− ) uniformly in all i. (A6)

µ(u)du − µ(ti−K)K t = Op( t

ti−K

This implies

t

3

2+α− ). (A7)

{µ(u) − µ(ti−K)}du = Op( t

sup

i,t≤ti

ti−K

Similarly to Lemma 1 in Mykland and Zhang (2006), under the condition A1.2, we can apply Burkholder’s Inequality (Protter, 2004) to get

sup

i,t≤ti

t

3

2−δ+α− ), (A8)

{σ(u) − σ(ti−K)}dW(u) = Op( t

ti−K

where δ can be any number in 0 < δ < 32 + α. This result is also uniform in i for K = Op( tα) as speciﬁed. Therefore, over the window, for t ∈ [ti−K,ti], d log S(t) can be approximated by d log Si(t), such that

d log Si(t) = µ(ti−K)dt + σ(ti−K)dW(t), (A9) because

|(log S(t) − log S(ti−K)) − (log Si(t) − log Si(ti−K))|

t

t

(µ(u) − µ(ti−K))du +

(σ(u) − σ(ti−K))dW(u)

=

ti−K

ti−K

3

2−δ+α− ). (A10)

= Op( t

For all i, j and tj ∈ [ti−K,ti], the numerator is

log S(tj) − log S(tj−1) − mi

i−1

1 K − 1

= log Si(tj) − log Si(tj−1) −

log Si(tl) − log Si(tl−1)

l=i−K+1

3

2−δ+α− )

+ Op( t

i−1

1 K − 1

3

2−δ+α− )

= σ(ti−K)W t −

σ(ti−K)W t + Op( t

l=i−K+1

= σ(ti−K)√ t(Uj − U¯i−1) + Op( t

3

2−δ+α− ), (A11)

) ∼ iid Normal(0,1)andU¯i−1 = K1−1

i−1 j=i−K+1

where Uj = √1 t (Wt

j −Wt

j−1

Uj.

For the denominator, we use the instantaneous volatility estimator based on the realized bipower variation (see Barndorff-Nielsen and Shephard, 2004). According to Proposition 2 in Barndorff-Nielsen and Shephard, (2004), the impact of the drift term is negligible; hence, it does not affect the asymptotic limit behavior. Then, we prove the following approximation of the scaled volatility estimator:

plim t→0c2σˆ2(t) = plim t→0

### 1 (K − 2) t j |log S(tj)/S(tj−1)||log S(tj−1)/S(tj−2)|

= c2σ2(t). (A12)

It is due to

i−1

1 (K − 2) t

|log S(tj)/S(tj−1)||log S(tj−1)/S(tj−2)|

j=i−K+3

i−1

1 (K − 2) t

3

log Si(tj)/Si(tj−1) + Op( t

2−δ+α− )

=

j=i−K+3

3

× log Si(tj−1)/Si(tj−2) + Op( t

2−δ+α− )

i−1

1 (K − 2) t

|log Si(tj)/Si(tj−1)||log Si(tj−1)/Si(tj−2)|

=

j=i−K+3

3

2−δ+α− )

+ Op( t

i−1

√ tUj||

√ tUj−1| + Op( t

1 K − 2

3

σ2(ti−K)|

2−δ+α− )

=

j=i−K+3

3

= σ2(ti−K)c2 + Op( t

2−δ+α− ), (A13) where Ui’s are iid Normal(0,1) and c = E(|Ui|) ≈ 0.7979. Then,

(Ui − U¯i−1)

3

2−δ+α− ). (A14) This proves Theorems 1 and 1.1.

L(i) =

c + Op(

Alternatively, for the nonzero drift case, we can use Girsanov’s theorem to suppose µ(t) = 0, as in Zhang et al. (2005b).

- A.3 Proof of Theorem 2 When there is a possibility of rare Poisson jumps in the window, the scaled bipower variation c2σˆ2(t) can be decomposed into two parts: one with jump terms and other without jump terms, as follows:

c2σˆ2(t)

1 (K − 2) t termswithjumps

= terms without jumps +

σ(tj)| Wt

j||Jump|

Op(√ t)

1 (K − 2) t

= terms without jumps +

### σ(tj)|Jump|

termswithjumps

Op(√ t). (A15)

1 (K − 2) t

= terms without jumps +

The order of the second term is due to the property of Poisson jump processes that allows a ﬁnite number of jumps over the window. Since σ(tj)|Jump| = Op(1), termswithjumps σ(tj)|Jump| = Op(1). For the effect of jump terms to

become negligible, the second term must be op(1) as t goes to 0. The window size K that satisﬁes K√ t → ∞ and K t → 0 as t goes to 0 will work. If we assume the window size to be K = tα, then the necessary condition for α is −1 < α < −0.5. Accordingly,

lim t→0σˆ2|alternative = lim t→0σˆ2|null = σ2(t). (A16) Then, putting the approximation for return above in the statistic yields

### √ tUi + Y(τ)Iτ∈(t

σt

i−1,ti)

L(i) ≈

i−K

cσ(ti−K)√ t =

Y(τ) cσ

Ui c +

i−1,ti). (A17)

Iτ∈(t

√ t

- A.4 Proof of Lemma 1 Proof of Lemma 1 follows from Aldous (1989) and the proof in Galambos

(1978).

- A.5 Proof of Theorem 3 Let N be the number of jumps from time t = 0 to t = T. We claim there is a jump if |L(i)| > βnSn + Cn. Fix a set of jump times as An = {i : there is a jump in (ti−1,ti]}. Then,

P(We correctly classify all N jumps|N)

= P(For all i ∈ An,|L(i)| > βnSn + Cn) ≈

i∈An

P(|L(i)| > βnSn + Cn) ≈

i∈An

P(|Y(ti)| > (βnSn + Cn)cσ

√ t)

=

i∈An

1 − F|Y|(yn) ∼ 1 −

2 √2π

yn + o(yn2)

N

= 1 −

2 √2π

ynN + o(yn2N). (A18)

- A.6 Proof of Theorem 4 Let ACn = {1,...,n} − An be a set of non-jump times. Then,

P(We incorrectly reject any non-jumps|N)

### = P(for some i ∈ ACn ,|L(i)| > βnSn + Cn|N)

= P max

### |L(i)| > βnSn + Cn|N ≈ P max

i∈ACn

| L(i)| > βnSn + Cn =1− Fξ(βn)= exp(−βn)+o(exp(−βn)). (A19)

i∈ACn

By L’Hopital’s rule, we obtain the last step because

1 − Fξ(βn) exp(−βn) = 1. (A20)

limβ

n→∞

- A.7 Proof of Theorem 5 Prob(GMJ or GMNJ) = Prob(GMJ) + Prob(GMNJ) and the results follow

from Theorems 3 and 4. Minimum probability can be achieved at β∗n, which can be obtained by taking the ﬁrst derivative of probability with respect to βn and setting it equal to 0, as

∂P ∂βn =

### Snσc√ tN − exp(−βn) = 0. (A21)

2 √2π

References A¨ıt-Sahalia, Y. 1996. Testing Continuous-Time Models of the Spot Interest Rate. Review of Financial Studies 9:385–426.

A¨ıt-Sahalia, Y. 2004. Disentangling Diffusion from Jumps. Journal of Financial Economics 74:487–528. A¨ıt-Sahalia, Y., and J. Jacod. 2005. Fisher’s Information for Discretely Sampled Levy Processes. Working Paper, Department of Economics, Princeton University. Aldous, D. 1989. Probability Approximations via the Poisson Clumping Heuristic. New York: Springer-Verlag. Andersen, T., T. Bollerslev, F. Diebold, and C. Vega. 2003. Micro Effects Macro Announcements: Real-Time Price Discovery in Foreign Exchange. American Economic Review 93:38–62.

Andersen, T., T. Bollerslev, and D. Dobrev. 2006. No-Arbitrage Semi-Martingale Restrictions for ContinuousTime Volatility Models Subject to Leverage Effects, Jumps, and i.i.d. Noise: Theory and Testable Distributional Implications. Journal of Econometrics, 138:125–80.

Bakshi, G., C. Cao, and Z. Chen. 1997. Empirical Performance of Alternative Option Pricing Models. Journal of Finance 52:2003–49.

Bakshi, G., C. Cao, and Z. Chen. 2000. Pricing and Hedging Long-Term Options. Journal of Econometrics 94:277–318.

Bakshi, G., N. Kapadia, and D. Madan. 2003. Stock Return Characteristics, Skew Laws, and the Differential Pricing of Individual Equity Options. Review of Financial Studies 16:101–43.

Bakshi, G., N. Yu, and H. Ou-Yang. 2005. Estimation of Continuous-Time Models with an Application to Equity Volatility. Journal of Financial Economics, 82:227–49.

Barndorff-Nielsen, O. E., and N. Shephard. 2004. Power and Bipower Variation with Stochastic Volatility and Jumps. Journal of Financial Econometrics 2:1–48.

Barndorff-Nielsen, O. E., and N. Shephard. 2006. Econometrics of Testing for Jumps in Financial Economics Using Bipower Variation. Journal of Financial Econometrics 4:1–30.

Bates, D. S. 1996. Jumps and Stochastic Volatility: Exchange Rate Processes Implicit in Deutsch Mark Options. Reivew of Financial Studies 9:69–107.

Bates, D. S. 2000. Post-’87 Crash Fears in the S&P 500 Futures Option Market. Journal of Econometrics 94:181–238.

Bertsimas, D., L. Kogan, and A. Lo. 2001. Hedging Derivative Securities and Incomplete Markets: An EpsilonArbitrage Approach. Operations Research 49:372–97.

Carr, P., and L. Wu. 2004. Time-Changed L´evy Processes and Option Pricing. Journal of Financial Economics 71:113–41.

Chernov, M., A. R. Gallant, E. Ghysels, and G. Tauchen. 2003. Alternative Models for Stock Price Dynamics. Journal of Econometrics 116:225–57.

Collin-Dufresne, P., and J. Hugonnier. 2001. Event Risk, Contingent Claims and the Temporal Resolution of Uncertainty. Working Paper, Tepper School of Business, Carnegie Mellon University.

Cox, J. T., J. E. Ingersoll, and S. A. Ross. 1985. A Theory of the Term Structure of Interest Rates. Econometrica 53:385–407.

Dubinsky, A., and M. Johannes. 2006. Earnings Announcements and Option Prices. Working Paper, Graduate School of Business, Columbia University.

Dufﬁe, D., J. Pan, and K. Singleton. 2000. Transform Analysis and Asset Pricing for Afﬁne Jump Diffusions. Econometrica 68:1343–76.

Eraker, B., M. Johannes, and N. Polson. 2003. The Impact of Jumps in Volatility and Returns. Journal of Finance 53:1269–300.

Galambos, J. 1978. The Asymptotic Theory of Extreme Order Statistics. New York: John Wiley & Sons. Goetze, F., and C. Hipp. 1983. Asymptotic Expansions for Sums of Weakly Dependent Random Vectors. Z. Wahrsch. Verw. Gebiete 64:211–39.

Heston, S. 1993. A Closed-Form Solution for Options with Stochastic Volatility with Applications to Bonds and Currency Options. Review of Financial Studies 6:327–43.

Jiang, G. J., and R. Oomen. 2005. A New Test for Jumps in Asset Prices. Working Paper, Eller College of Management, University of Arizona.

Johannes, M. 2004. The Statistical and Economic Role of Jumps in Interest Rates. Journal of Finance 59:227– 60.

Kloeden, P. E., and E. Platen. 1992. Numerical Solution of Stochastic Differential Equations. New York: SpringerVerlag.

Liu, J., F. Longstaff, and J. Pan. 2003. Dynamic Asset Allocation with Event Risk. Journal of Finance 58:231– 59.

Merton, R. C. 1976. Option Pricing When Underlying Stock Returns Are Discontinuous. Journal of Financial Economics 3:125–44.

Mykland, P. 1993. Asymptotic Expansions for Martingales. Annals of Probability 21:800–18. Mykland, P. A., and L. Zhang. 2006. ANOVA for Diffusions and Ito processes. Ann. Statist., 34:1931–63. Naik, V., and M. Lee. 1990. General Equilibrium Pricing of Options on the Market Portfolio with Discontinuous Returns. Review of Financial Studies 3:493–521. Pan, J. 2002. The Jump-Risk Premia Implicit in Options: Evidence from an Integrated Time-Series Study. Journal of Financial Economics 63:3–50. Piazzesi, M. 2003. Bond Yields and the Federal Reserve. Journal of Political Economy 113:311–44. Pollard, D. 2002. A User’s Guide of Measure Theoretic Probability. Cambridge: Cambridge University Press. Protter, P. 2004. Stochastic Integration and Differential Equations: A New Approach. New York: Springer. Ross, S. M. 1995. Stochastic Processes. New York: John Wiley & Sons. Schaumburg, E. 2001. Maximum Likelihood Estimation of Jump Processes with Applications to Finance. Ph.D. Thesis, Department of Economics, Princeton University.

Tauchen, G., and H. Zhou. 2005. Identifying Realized Jumps on Financial Markets. Working Paper, Department of Economics, Duke University.

Wu, L. 2006. Dampened Power Law: Reconciling the Tail Behavior of Financial Asset Returns. Journal of Business 79:1445–74.

- Zhang, L., P. A. Mykland, and Y. A¨ıt-Sahalia. 2005a. Edgeworth Expansions for Realized Volatility and Related Estimators. Working Paper, University of Illinois at Chicago.
- Zhang, L., P. A. Mykland, and Y. A¨ıt-Sahalia. 2005b. A Tale of Two Time Scales: Determining Integrated Volatility with Noisy High-Frequency Data. Journal of American Statistical Association 472:1394– 411.

