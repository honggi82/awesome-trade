

Journal of Econometrics 116 (2003) 225–257

www.elsevier.com/locate/econbase

# Alternative models for stock price dynamics

Mikhail Chernova, A. Ronald Gallantb, Eric Ghyselsb;∗, George Tauchenc

aColumbia Business School, Division of Finance and Economics, 413 Uris Hall, 3022 Broadway, New York, NY 10027, USA bDepartment of Economics, University of North Carolina at Chapel Hill CB 3305, Chapel Hill, NC 27599-3305, USA cDepartment of Economics, 305 Social Science, Box 90097, Duke University, Durham, NC 27708-0097, USA

Abstract

This paper evaluates the role of various volatility speci cations, such as multiple stochastic volatility (SV) factors and jump components, in appropriate modeling of equity return distributions. We use estimation technology that facilitates nonnested model comparisons and use a long data set which provides rich information about the conditional and unconditional distribution of returns. We consider two broad families of models: (1) the multifactor loglinear family, and (2) the a ne-jump family. Both classes of models have attracted much attention in the derivatives and econometrics literatures. There are various tradeo s in considering such diverse speci cations. If pure di usion SV models are chosen over jump di usions, it has important implications for hedging strategies. If logarithmic models are chosen over a ne ones, it may seriously complicate option pricing. Comparing many di erent speci cations of pure di usion multifactor models and jump di usion models, we  nd that (1) log linear models have to be extended to two factors with feedback in the mean reverting factor, (2) a ne models have to have a jump in returns, stochastic volatility or probably both. Models (1) and (2) are observationally equivalent on the data set in hand. In either (1) or (2) the key is that the volatility can move violently. As we obtain models with comparable empirical  t, one must make a choice based on arguments other than statistical goodness-of- t criteria. The considerations include facility to price options, to hedge and parsimony. The a ne speci cation with jumps in volatility might therefore be preferred because of the closed-form derivatives prices.

c 2003 Elsevier B.V. All rights reserved.

JEL classi cation: G13; C14; C52; C53

Keywords: E cient method of moments; Poisson jump processes; Stochastic volatility models

∗ Corresponding author.

E-mail address: eghysels@unc.edu (E. Ghysels).

0304-4076/03/$-see front matter c 2003 Elsevier B.V. All rights reserved. doi:10.1016/S0304-4076(03)00108-8

- 0. Introduction

Stochastic volatility (SV) models are speci cally designed to capture salient properties of volatility such as randomness and persistence. However, one of the most important recent  ndings is that these models are not able to characterize all aspects of asset returns distribution.1 Indeed, given a reasonable  t to the conditional dynamics of volatility, SV models cannot match the high conditional kurtosis of returns (tail thickness) documented in the literature for many classes of  nancial assets, of which equities are the most prominent example.

This paper evaluates the role of various factors, such as additional volatility factors and jumps, in appropriate modeling of equity returns. To do so we estimate a variety of extensions of SV models using the same estimation technology with a common data set.

We are particularly interested in the role of SV factors and their functional form because this issue has not been considered in the prior work as much as the role of jump components has. Moreover, the evidence from option markets shows that adding a jump component to returns is not su cient to fully capture the dynamics of  nancial series. Bakshi et al. (1997) and Bates (2000)  nd that the volatility of volatility coe cient, which is estimated from the underlying asset time series is much lower than the one estimated from the options cross-section. In addition, Pan (2002) using simultaneously equity returns and options prices  nds evidence suggesting that the volatility of volatility is stochastic. This observation is con rmed by Jones (2003) who  nds, based on the implied volatility series, that volatility of volatility is higher during the more volatile periods in the stock market.

This evidence suggests that an appropriate extension might involve two SV factors, thus breaking the link between tail thickness and volatility persistence. Depending on model speci cation—a ne or logarithmic—a second SV factor may act as either a factor dedicated to exclusive modeling of tail behavior (the  rst factor is then often referred to as a long memory component), or as a stochastic volatility of volatility factor. In the latter speci cation, the volatility would be capable of making rapid moves, which is prohibited by a single SV speci cation. EJP propose to model the same feature by introducing a jump component to the SV factor.

There are various tradeo s in considering these di erent speci cations. If pure diffusion models are chosen over jump di usions, it has important implications for hedging strategies. If logarithmic models are chosen over a ne ones, it may seriously complicate option pricing. Finally, if we obtain models with comparable empirical  t, we would still have to make a choice based on arguments other than statistical goodness-of- t criteria. Such arguments could be facility to price options, to hedge, or simply parsimony. Our approach allows us to address all these issues.

1 Formal statistical diagnostics and rejections of SV models are reported in Andersen et al. (2002) (ABL hereafter), Chernov and Ghysels (2000), Eraker et al. (2003) (EJP hereafter), Jones (2003), and Pan (2002).

We estimate a total of ten di erent models, broadly classi ed as either a ne or logarithmic. The benchmark for each class is a single SV model, i.e. the Heston (1993) model for a ne class, and the Scott (1987) model for the logarithmic class. In the a ne class the model is extended by considering two SV factors, a jump to returns (ABL), and a simultaneous jump to both returns and volatility (EJP). In the logarithmic class the extensions are achieved by adding a second SV factor, and by considering models with feedback (Gallant et al., 1999).

We consider a long data set, providing rich information about the conditional and unconditional distribution of returns under the objective probability measure. The common data set consists of returns on the Dow Jones industrial average (DJIA) index from January 1953 to July 1999, covering in addition to the market crash of October 1987, the more recent crashes of October 1997 and August 1998, as well as historical events such as the Cuban Missile Crisis in October 1962, or Arab Oil Embargo in October 1973. The long data set also o ers more variety in the dynamics of volatility, which allows the determination of a more robust model. These are the longest series considered for such a study: corresponding to the combination of ABL, and EJP, who study 1953–1996 and 1980–1999, respectively. Although these authors use the S& P 500 index, our results should be qualitatively comparable because historically DJIA closely tracks the S& P 500 index.

Since the risk-neutral measure used in derivatives valuation has to coincide with the objective one up to sets of measure zero, the models of equities will retain the same factor structure under both probability measures. Therefore, despite the fact that we are not using options data in the present paper, we motivate our work by empirical results from both underlying and options literature. By the same token, our results will have implications for both.

The common estimation method is the e cient method of moments (EMM) of Gallant and Tauchen (1996). The advantages of using EMM, critical for comparison of several models, are that it o ers: (1) formal statistical tests of a model  t, (2) formal diagnostics of model inadequacies and most importantly (3) nonnested speci cations can be compared in a meaningful way since EMM forces all models to confront the same set of moment conditions.

The paper is organized as follows. In a  rst section, we describe the models that we consider in the study. The next section covers the estimation methods, brie y summarizing EMM procedure and the SNP model selection. Section three reports the empirical results. A  nal section concludes the paper.

- 1. Models speci cations

In this section we describe the various classes of models we consider in our study, starting with single index volatility di usion models in a  rst subsection. Special cases include a ne models, constant elasticity of variance (CEV) and logarithmic models. In the second subsection, we discuss jump-di usion models. In the third and  nal subsection we introduce a uni ed notation for the di erent models.

- 1.1. Single index volatility di usion models

The starting point is the multifactor pure di usion SV model. We consider models with at most four factors, namely,

dPt=Pt = ( 10 + 12U2t)dt + ( 10 + 13U3t + 14U4t)

×( 11 dW1t + 13 dW3t + 14 dW4t); (1)

dU2t = ( 20 + 22U2t)dt + 20 dW2t; (2)

dUit = ( i0 + iiUit)dt + ( i0 + iiUit)

dWit; i = 3;4: (3)

i

In the above, Pt represents the  nancial price series evolving in continuous time (we reserve the notation U1t for the logarithm of the price).

We allow for a  exible drift speci cation via a stochastic factor U2t, which evolves according to an Ornstein–Uhlenbeck process. This speci cation can accommodate the mild serial correlation appearing in the returns series, which may be explained by the nonsynchronous trading and unexpected stochastic dividend e ects. An alternative strategy to incorporate these e ects would be to pre lter the data as was done in ABL or Gallant and Tauchen (1993).

We model the di usion coe cient (:) as a function of the linear combination of the two stochastic volatility factors U3t and U4t, which are described by the usual mean reverting processes. The mean reversion parameters ii or respective volatility half-lives log 2= ii measure persistence of these processes.

The use of a functional transformation of linear combination of factors is reminiscent of index models used in various areas of econometrics.2 We can, therefore, refer to the volatility models as single index volatility (SIV) models. Di erent speci cations of the index function will yield various classes of SV models, including a ne and logarithmic two volatility factor models.

Finally, we parameterize 11 = 1 − 13 2 − 14 2 so that 13 and 14 are correlation coe cients. Note that, when we have multiple stochastic volatility factors, the correlation coe cients loose the interpretation of the leverage e ect, i.e. the instantaneous correlation between returns and changes in variance. In this case, as can be easily shown, the leverage e ect is equal to

corr(dU1t; 13 dU3t + 14 dU4t)

( 30 + 33U3t) 3 + 14 14( 40 + 44U4t) 4

= 13 13

dt: (4)

2 13( 30 + 33U3t)2 3 + 14 2 ( 40 + 44U4t)2 4

As a result, the leverage e ect is state dependent in these models.

2 For cross-sectional applications see for instance Powell et al. (1989) and Stoker (1993), for time-series applications in term structure models see Ghysels and Ng (1998) and in portfolio allocation see A  t-Sahalia and Brandt (2001).

The classical models of Heston (1993) and Scott (1987) are obtained when U2t and U4t are switched-o . These models proved to be a substantial improvement over the Black and Scholes (1973) speci cation because of their formulation of volatility as a random persistent process. However, this persistence turned out to be the weakness of the model as well: extreme movements in returns occur more frequently in the observed data than would be implied by the Heston or Scott model calibrated to the data (see, for instance, ABL). These observations prompt us to explore generalizing the Heston and Scott models to better accommodate the data. In particular, we introduce a second stochastic volatility factor. The presence of two volatility factor breaks the aforementioned linkage between tail thickness and volatility persistence.

We have to note that the list of the models considered is by no means exhaustive. For example, Meddahi (2001) proposes to model the di usion coe cient as a  nite order expansion based on the eigenfunctions of the expectations of the state variables. In our notation his model can be represented as

2(U3t;U4t) =

ai;jE3;i(U3t)E4;j(U4t); (5)

06i;j6p

where p is the order of expansion. The advantage of such a speci cation is that it nests all the models we consider here and o ers more  exibility in modeling the di usion term. However, as is often the case with nonparametric speci cations, the intuition behind the speci cation is lost because of the higher-order expansions. The goal of this paper is to compare intuitive and commonly used speci cations, therefore we leave nonparametric  exible form alternatives for future research. In the next subsections we consider (1) a ne, (2) CEV and (3) logarithmic models, all particular cases of index volatility models.

- 1.1.1. A ne models A ne di usion models are characterized by linearity of the drift and variance func-

tions. Dai and Singleton (2000) discuss the most general speci cation of such models including the identi cation and admissibility conditions. We consider a very simple representative of this class by specializing the SIV speci cation in (1)–(3) to

(u) = √u; (6)

i = 0:5; i = 3;4: (7)

The volatility factors enter additively into the di usion component speci cation, as in Engle and Lee (1999). Hence, they could be interpreted as short and long memory components. The long memory (persistent) component should be responsible for the main part of the returns distribution, while the short memory component will accommodate the extreme observations.

- 1.1.2. CEV models The SIV model specializes to the CEV class when the volatility function of the a ne

models (6), is modi ed to allow i in the range from 0.5 to 1. As extreme cases, the class contains the a ne models, when i = 0:5, and the GARCH di usion models

(Nelson, 1990), when i = 1. We do not provide a detailed discussion of the CEV models in this paper because our  t was very close to a ne models, and, therefore, did not provide many new insights. Jones (2003) has success with these models, when allowing for volatility induced stationarity ( i ¿1) and confronting it with the joint options and the underlying index data set.

- 1.1.3. Logarithmic models In logarithmic models, the variance is an exponential function of the factors. We

consider the following specializations of SIV (1)–(3): (u) = exp(u): (8)

We study two di erent  avors of the logarithmic models, depending on the value of the coe cients i.

When i =0, i =3;4 the volatility factors are described by Ornstein–Uhlenbeck processes. In this case, the drift and variance of the volatility factors are linear functions. Hence, this is a multifactor generalization of the Scott (1987), also known as log-linear, speci cation.3 When i = 1, i = 3;4 we have volatility feedback, a feature which will turn out to be empirically relevant. The key property of interest is that it permits the volatilities of the volatility factors, via the terms 33U3t and/or 44U4t, to be high when the volatility factors themselves are high. These terms are found to be important in Gallant et al. (1999).4

The logarithmic models with feedback violate the standard regularity conditions. Therefore, the stochastic integrals and solutions of the SDEs associated with these models are not de ned. To remedy this problem one can splice the exponential volatility function in (8) with, essentially, the linear growth condition at the level of volatility so high that it is unlikely to be observed in the U.S. equity index returns. Fig. 6 compares the exponential function in (8) and the actual speci cation that we use. All the details are relegated to Appendix A.

The model with feedback also has a di erent volatility domain. As opposed to the a ne and log-linear models, where (u) ranges between zero and in nity, this model has a lower bound equal to exp( 10 − 13 30= 33 − 14 40= 44).5 While there is no a priori consideration against this on pure modeling ground—after all volatility never reaches zero in practice—the fact that volatility boundary depends on the parameters may lead to nonstandard asymptotic behavior of estimators. Method of moment estimators are less prone to boundary problems than are maximum likelihood estimators.6

3 We are not the  rst to suggest two-factor log-linear SV models, see for instance Alizadeh et al. (2002), Chacko and Viceira (1999), Gallant et al. (1999) and the two-factor GARCH model of Engle and Lee

(1999).

- 4 We use the terminology “feedback” to refer to a feature of the latent factors. One might argue that it

is di cult to label and compare models through latent factor features. However, if we de ne feedback on the basis of the time variation of the variance of the instantaneous variance of returns, we would  nd that almost all SV models exhibit feedback. Our terminology is therefore based on distinct features of the latent volatility factors.

- 5 When i = 1, the volatility factors are equal to GARCH di usion model shifted by i0= ii. Since the

domain of GARCH di usion is [0; ∞), the domain of our volatility factors is [ − i0= ii; ∞).

- 6 For further discussion of ML estimation with boundary parameters, see e.g. van der Vaart (2000).

Nonetheless, we strongly suspect that the densities are smooth enough at the boundary so that the parameter estimates follow the usual √N-asymptotics; however, we have been unable to prove this. An alternative strategy to address the boundary issue is to subtract the lower bound from the volatility speci cation in (8) as this would ensure that the lower bound is equal to zero. However, our estimation results showed that this speci cation is dominated by the one we consider here in terms of overall  t.

It is perhaps not so surprising that the feedback model has good empirical properties. Intuitively, the second factor not only takes care of the tail behavior, as the jump process does, it also features dynamics that seem appealing for modeling extreme market conditions. Indeed, the process can accommodate (mild) persistence in volatility during high volatility days, and when 44 = 0 (assuming the second factor determines tail behavior), the volatility of volatility increases as well. These properties cannot be accomplished by a simple Poisson jump process, which can accommodate tail behavior but not the dynamics of extreme events. It should also be noted that a nice feature of the logarithmic speci cation is the multiplicative e ect of U3t and U4t on the volatility of returns. Neither a ne models nor jump processes feature separate factors which scale multiplicatively the Brownian motion W1t. Also, the ability of the exponential function to generate very high volatility values adds additional capability to model market stress. All these properties of logarithmic models facilitate mimicking the short-lived erratic behavior through the second volatility factor.

- 1.2. A ne jump di usion models

As will be seen from empirical results, the log-linear models dominate the pure a ne di usion models and are not rejected by statistical tests. We would like to give a ne models a fair chance and consider extensions of the Heston SV model via jump components.

As a benchmark, we will consider a constant intensity jump di usion model. Namely the SV model is augmented by the jump to returns, U1t = log Pt, speci ed as

dq1;t = J1;t dNt; (9) where

Nt ∼ Poi( J); (10) J1;t ∼ N( J; J2); (11)

which is added to the a ne version of (1) when U4t ≡ 0. ABL constrain J to be equal to zero. We estimate both constrained and unconstrained speci cations.

EJP consider a jump to the volatility factor U3t as well, namely,

dq3;t = J3;t dNt; (12) where

J3;t ∼ exp( ) (13) This speci cation means that jumps to returns and volatility are driven by the same Poisson process Nt, i.e. jumps occur at the same time. Such a speci cation allows the

introduction of correlation between jump sizes: the jump to return speci cation (11) should be replaced by

J1;t ∼ N( J + JJ3;t; J2) (14)

EJP  nd this model to be the most successful a ne speci cation in terms of the residual properties and the shape of implied volatilities smile.

- 1.3. Normalizations and model abbreviations

Some normalizations are needed to achieve identi cation of the various speci cations described in the previous subsection. In the SIV speci cation (1)–(2) the long-run mean of the drift is simultaneously controlled by 10 and 20, while the volatility of the drift volatility is controlled by 12 and 20. Therefore, we impose

20 = 0; 20 = 1: (15) By analogy, for the general a ne model in (3), (6) and (7) we impose the restrictions:

10 = 0; 30 = 0; 33 = 1; 40 = 0; 44 = 1: (16) Finally, for the logarithmic speci cation (3) and (8) we set

30 = 0; 40 = 0; 30 = 1; 40 = 1: (17)

Note, that 10 is not equal to zero here, because it controls the long-run mean of the total volatility.

It proves convenient to have acronyms for the various models: AFF1V means the simplest AFFine One Volatility factor model appearing in

(1)–(3), (6), and (7). This model with constant drift corresponds to the Heston (1993) model.

AFF2V stands for the AFFine Two Volatility factor model, i.e. the most general model appearing in (1)–(3), (6), and (7). This model augments the previous one with an additional continuous path factor.

AFF1V-J0 represents the simplest AFFine One Volatility factor model with Jumps to returns appearing in (1)–(3), (6), and (7) in combination with the Poisson process as speci ed in (9)–(11) and mean jump size, J, constrained to be equal to 0. This is the ABL model.

AFF1V-J is the AFFine One Volatility factor model with Jumps to returns appearing in (1)–(3), (6), and (7) in combination with the Poisson process as speci ed in

(9)–(11).

AFF1V-JJ is AFFine One Volatility factor model appearing in (1)–(3), (6), and (7) with the Poisson process speci ed in (10) driving both Jumps to volatility in (12) and (13) and Jumps to returns in (9) and (14). This is the model introduced in Du e et al. (2000) and estimated by EJP.

LL1V means the simplest Log Linear One Volatility factor model with no volatility feedback. This model with constant drift corresponds to the Scott (1987) model.

LL1VF means the One Volatility factor version of (1)–(3), (8), and i = 1, i = 3;4 with Feedback where 14 = 0 making the second volatility factor irrelevant.

Modelde nitionsandminimizedchi-squaredcriterion

Table1

J J J J 10 12 22 30 33 40 44 10 13 14 30 33 40 44 13 14 2(ˆ )dfp-value

- AFF1V******1*20.19690.0167
- AFF2V*********11**13.66850.0179

AFF1V-J0******1*5.60*18.70470.0092

AFF1V-J******1*1.70**11.21360.0820

AFF1V-JJ******1*1.70****8.57740.0726

LL1V******1*30.06290.4e-04

- LL2VI********11***4.15350.5276

LL2VF********1*1***3.17140.5296

- LL1VF******1**22.75280.0037
- LL2V********11**15.03760.0200

Notes:Inthispaperweconsiderthefollowingmodelspeci cations:

=(+U) dt 10 122tPt

dPt

J 2 2+U+U)(+ (1dW+dW+dW)+(e1) dN;1;t−−−t 10 133t 144t1t 133t 144t1314

dU=Udt+dW;2t 222t2t

=(+U) dt+(+U)dW+JdN;i=3;4;dU itit iiit iiitit i0 i03;t

√ (u)=u;  =0:5forAFF;i

=0forLLor=1forLLF; (u)=exp(u);  i i

denotesafreeparameter;1denotesaparameterpinnedatunity;blankdenotesaparametersettozero.Thereportedresultsarebasedonasimulationof∗

lengthN=75 000simulatedat1= =6048stepsperyear,or,equivalently24stepsperdaywith252tradingdaysperyear.

2N(+J;  ):J∼ J J1;t3;tJ

NPoi();∼t J

exp( );J∼3;t

- LL2V is the model (1)–(3), (8), and i = 0, i = 3;4 meaning Log Linear, Two

Volatility Factors without volatility feedback.

- LL2VI is the model meaning Log Linear, Two Volatility Factors—the Intermediate

case—one without volatility feedback and the other one with the feedback, i.e. 3 = 0 and 4 = 1.

LL2VF is the most general model, where the acronym means Log Linear, Two Volatility Factors, which feature Feedback via 33 = 0 and 44 = 0 from the Gallant, Hsu, and Tauchen (1999) exploredvolatility factors to their own volatilities. This is the Gallant et al. (1999) model.

The various models are summarized in Table 1. In what follows, denotes the parameters of the underlying SDE that is to be estimated. For example, for the largest logarithmic speci cation LL2VF the parameter vector is

= ( 10; 12; 22; 33; 44; 10; 13; 14; 33; 44; 13; 14): (18)

- 2. E cient method of moments

Let {yt}∞t=−∞, yt ∈RM, be a discrete stationary time series. In this paper, {yt} is 100 × [log(Pt) − log(Pt−1)], where Pt is the daily DJIA. When, as here, {yt} comes from a discretely sampled SDE system, then the SDE speci cation implicitly determines the density p(yt−L;:::;yt| ) of a contiguous stretch of length L + 1 from {yt}, where ∈Rp is a vector of unknown parameters of the generic di usion process (1). The fundamental problem that blocks straightforward application of standard statistical methods is that an analytic expression for p(yt−L;:::;y0| ) is not available. (see for instance, A  t-Sahalia, 2002; Elerian et al., 2001, Durham and Gallant, 2000 for further discussion). However, by using simulation, an expectation of the form

E (g) = ··· g(y−L;:::;y0)p(y−L;:::;y0| )dy−L ··· dy0

can be computed for given  : That is, for given , one can generate a simulation {yˆt}Nt=1 from the system and put

N

1 N

E (g) =

g(yˆt−L;:::;yˆt)

t=1

with N large enough that Monte-Carlo error is negligible.

Gallant and Tauchen (1996) propose a minimum chi-squared estimator for in this situation, which they termed the e cient method of moments (EMM) estimator. Being minimum chi-squared, the optimized chi-square criterion can be used to test system adequacy. The moment equations that enter the minimum chi-squared criterion of the EMM estimator are obtained from the score vector (9=9 )log f(yt|xt−1; ) of an auxiliary model f(yt|xt−1; ) where xt−1 is a lagged state vector. The auxiliary model is termed the score generator. Gallant and Long (1997) show that if the score

generator is the SNP density fK(y|x; K) described below, then the e ciency of the EMM estimator can be made as close to that of maximum likelihood as desired by

taking K large enough. The  rst step in computing the EMM estimator ˆ n is to use the score generator

f(yt|xt−1; ) ∈ (19)

to summarize the data {y˜t;x˜t−1}nt=1 by computing the quasimaximum likelihood estimate

1 n

˜ n = argmax

∈

n

log[f(y˜t|x˜t−1; )]

t=1

and the corresponding estimate of the information matrix

n

1 n

I˜n =

t=1

9 9

log f(y˜t|x˜t−1; ˜ n)

9 9

log f(y˜t|x˜t−1; ˜ n) : (20)

Estimator (20) presumes the score generator (19) provides an adequate statistical approximation to the transition density of the data, so that {(9=9 )log f(y˜t|x˜t−1; ˜ n)} is essentially serially uncorrelated. If (19) is not adequate, then one of the more complicated expressions for I˜n set forth in Gallant and Tauchen (1996) must be used, although the EMM estimator is still consistent and asymptotically normal. De ne

m( ; ) = E

9 9

log[f(y0|x−1; )] ;

which is computed by averaging over a long simulation

N

9 9

1 N

: =

log[f(yˆt|xˆt−1; )]: (21)

m( ; )

t=1

The EMM estimator is

m ( ; ˜ n)(I˜n)−1m( ; ˜ n): (22)

ˆ n = argmin

∈Rp

The estimator is consistent and asymptotically normally distributed with asymptotic distribution given in Gallant and Tauchen (1996). Under the null hypothesis that p(y−L;:::;y0| ) is the correct model, n times the minimized value of the objective function is asymptotically chi-squared on p − p degrees of freedom where p and p are, respectively, the lengths of parameter vectors and .

The EMM estimation involves simulating continuous path di usions which has been covered extensively in the literature. We rely on a standard Euler discretization scheme. The simulations involve a sampling frequency with twenty four steps per trading day. The trading day was set equal to 2521 , therefore the models parameters have annual scaling.

We use a nonstandard approach to simulate the a ne di usions from (1)–(3), (6), and (7).7 Instead of a naive discretization of U3t and U4t, we  rst derive the dynamics of log U3t and log U4t using the Itˆo’s lemma. Then we apply the Euler scheme to these processes. As is well known, square-root processes require constraints on the coe cients for the processes to stay positive (e.g. Feller, 1971). Given our normalizations in (16), these constraints translate into i0 ¿0:5 for i = 3;4. If we directly simulate the a ne processes these constraints impose numerical burdens, as it becomes hard to take numerical derivatives and even simulate for the borderline cases. When we simulate the log-versions of U3t and U4t, we are not concerned with the positivity of the processes, so we can let the parameters i0 change freely. This manipulation improves the stability of the procedure tremendously. Therefore, although a ne di usions satisfy the standard regularity conditions, we might expect, on this basis, that simulating the log provides some increase in numerical accuracy. This approach is related to the Doss transformation which improves the speed of convergence of simulation-based estimates (Detemple et al., 2002).

We took the following approach with respect to jump component simulation. We opted a pro ling approach, where the EMM objective function is optimized with respect to the parameters appearing in (18) and the jump size parameters. Since we focus on a standard Merton type jump process the size distribution is Gaussian and involves two parameters. The jump frequency is drawn from a Poisson process, with its intensity parameter  xed and moved over a grid to appraise the overall  t of the model. The jump process was implemented by drawing durations between jumps from a exponential distribution. When the durations fell inside the discretization interval, the size of the jump was attributed time proportionally to the hourly observations bracketing the jump event. In practice, this scheme is equivalent to the one in Platen and Rebolledo (1985) and hence achieves the same convergence.

The best choice of a moment function to implement simulated method of moments is the score of a auxiliary model that closely approximates the system dynamics where the parameter vector of the auxiliary model is evaluated at its quasi maximum likelihood estimate. The SNP density of Gallant and Tauchen (1989,1992,2003), which is derived as a location-scale transform of an innovation density represented

- as a Hermite expansion leads to a useful, general purpose auxiliary model. We give a brief description. Here, yt represents the observed process and, for now, xt−1 = (yt−L;:::;yt−1). We frequently drop the time subscripts and write y and x generically.

If one expands √p(x;y | 0) in a Hermite series, that is, expands the square root of the stationary density of system (1) in a Hermite series, and derives the approximation to the transition density p(y |x; 0) of the system that corresponds to the truncated expansion, then one obtains an approximating transition density fK(yt |xt−1) that has the form of a location-scale transform

y = Rxz + x (23)

7 We are greatful to Michael Johannes for suggesting this.

of an innovation zt, where Rx is an upper triangular matrix (see Gallant et al., 1997).8 The density function of the innovation zt, is

[P(z;x)]2 (z) [P(u;x)]2 (u)du

; (24)

hK(z|x) =

where P(z;x) is a polynomial in (z;x) of degree K and (z) denotes the multivariate normal density function with dimension M, mean vector zero, and variance–covariance matrix the identity.

It proves convenient to express the polynomial P(z;x) in a rectangular expansion

##  

aijxi

Kx

Kz

zj; (25)

P(z;x) =

|j|=0

|i|=0

where K = (Kz;Kx), i and j are multiindexes, and | · | denotes the degree of an index. Because [P(z;x)]2= [P(u;x)]2 (u)du is a homogeneous function of the coe cients of the polynomial P(z;x), P(z;x) can only be determined to within a scalar multiple. To achieve a unique representation, the constant term a00 of the polynomial P(z;x) is put to one. With this normalization, hK(z|x) has the interpretation of a series expansion whose leading term is the normal density (z) and whose higher-order terms induce departures from normality.

The advantage of a rectangular expansion is that it gives the polynomial P(z;x) the interpretation of a polynomial in z of degree Kz whose coe cients are polynomials of degree Kx in x. This is useful in applications because putting Kx = 0 implies that the innovation density hK(zt|xt−1) does not depend on xt−1 and is therefore homogeneous. That is, if Kx=0 none of the moments of the innovation density hK(z|xt−1) will depend on the past. Conversely, if Kx ¿0, then the shape of the innovation distribution does depend on the history xt−1=(yt−L;:::;yt−1) of the process {yt}∞t=−∞. In the empirical application we will compare parameter estimates obtained from both homogeneous and heterogeneous scores for certain models.

The location function takes the form of an autoregression x = b0 + Lk=1u Bkyt−k. Consequently, the density determined by the location-scale transform y = Rz + x together with the innovation density hK(z|x) is a Gaussian vector autoregression if Kz = Kx = 0. It is a semi-parametric autoregression along the lines of Engle and Gonzales-Rivera (1991) if Kz ¿0 and Kx = 0, and is a fully nonparametric nonlinear process if Kz ¿0 and Kx ¿0: The two choices of Rx that have given good results in applications are an ARCH-like moving average speci cation and a GARCH-like ARMA speci cation which are discussed in Gallant and Tauchen (1997). In summary, Lu, Lg, and Lr determine the location-scale transformation y=Rxzt+ x and hence determine the nature of the leading term of the expansion. The number of lags in the location function

x is Lu and the number of lags in the scale function Rx is Lu+Lr. The number of lags

8 Although R does not depend on x in this derivation, it proves advantageous in applications to allow the scale matrix Rx to depend on x because it reduces the degree Kx required to achieve an adequate approximation to the transition density p(y|x;  0).

that go into the x part of the polynomial P(z;x) is Lp. The parameters Kz, Kx determine the degree of P(z;x) and hence the nature of the innovation process {zt}.

- 3. Empirical  ndings

In a  rst subsection we cover the estimation of the auxiliary model. The second subsection reports and discusses the estimates. A  nal subsection discusses reprojection of the factors and their properties.

- 3.1. Data and auxiliary model

The raw data for analysis consist of 11717 daily observations January 2, 1953, to July 16, 1999, on the (geometric) percent movement

yt = 100 ∗ [log(Pt) − log(Pt−1)] (26)

of the DJIA, Pt. As noted earlier, we use the raw series and do not perform any transformation on the raw data which are plotted in Fig. 1. The  rst step is to project the data {yt} onto an auxiliary model, which is the SNP model described above. We reserve the  rst 47 data points for forming lags leaving 11670 observations, net. The tuning parameters Lu, Lg, Lr, Lp, Kz, and Kx are selected by moving upward along an expansion path using the BIC criterion:

BIC = sn( ˜ ) + (1=2)(pK=n)log(n); where the objective function sn( ) is given by

n

1 n

sn( ) = −

log [fK(y˜t|x˜t−1; )]

t=1

to guide the search. Models with small values of BIC are preferred.

The expansion path has a tree structure. Rather than examining the full tree, the strategy is to expand  rst in Lu with Lg=Lr =Lp=Kz =Kx =0 until BIC turns upward. For ARCH-type speci cations, we expand Lr with Lg = Lp = Kz = Kx = 0, then expand Kz with Kx = 0, and lastly Lp and Kx. It is useful to expand in Kz, Lp and Kx at a few intermediate values of Lr because it sometimes happens that the smallest value of BIC lies elsewhere within the tree. For GARCH-type speci cations, the strategy is similar: we put Lg = Lr = 1, then expand Kz, Lp and Kx as above. We then check Lg = Lr = 2. These two are the only GARCH-type speci cations considered, which is consistent with standard practice among GARCH practitioners. There is the di culty that increases in Kx add a plethora of parameters. We control this by restricting the coe cients aij of the Hermite expansion (25) to be zero when |j|¿2 and |i|¿1, which was motivated by inspecting t-statistics on Hermite coe cients of larger models without such restrictions. The net e ect of the restrictions is that the Hermite coe cients of (25) are state dependent, i.e. dependent upon x, only up through quadratic terms; the Hermite coe cients of zj are constant for cubics and higher.

| |
|---|

25

20

15

10

5

0

- -25
- -20
- -15
- -10
- -5

1950 1955 1960 1965 1970 1975 1980 1985 1990 1995 2000

Fig. 1. DJIA 1953–1999.

The  nal SNP model selected via this procedure has Lu = 1;Lr = 1;Lg = 1;Lp = 1;Kz = 8;Kx = 1: (27)

This SNP model, preferred under BIC, can be characterized as a GARCH(1,1) with a nonparametric error density represented as an eighth-degree Hermite expansion where the Hermite coe cients up through quadratic terms are state dependent. The model is akin to the semiparametric GARCH of Engle and Gonzales-Rivera (1991), except their nonparametric error density is represented as a state-independent kernel density. Unlike SNP, the kernel representation of the semiparametric GARCH precludes state dependence of the error density, which is found to be empirically important for this data set.

We generate starting values for the optimization by  rst estimating the models based on a homogeneous score where the state dependence of the Hermite polynomial is not incorporated, namely the tuning parameters are set to

Lu = 1;Lr = 1;Lg = 1;Lp = 1;Kz = 8;Kx = 0: (28)

We use the EMM package capability to process a sequence of input parameter  les with many randomly perturbed starting values from each input  le and, therefore, bad starting values leading to local optima are not a concern. This strategy

yielded satisfactory  ts sometime substantially improving results of previous work.

- 3.2. Estimation results

Table 1 shows the various model speci cations along with the minimized value of the EMM objective function appearing in (22), scaled to follow an asymptotic chi-squared on p −p degrees of freedom. Tables 3 and 4 report parameter estimates of the a ne and logarithmic models, respectively. The parameters correspond to returns expressed in decimal form on a yearly basis. The models diagnostics via t-ratios of individual SNP score elements are provided in Table 5. We start the discussion with the benchmark case of single factor SV models, and then analyze various extensions.

- 3.2.1. Benchmark case: single factor SV models It is not surprising that all three single factor SV speci cations, AFF1V, LL1V,

and LL1VF, are rejected. The t-ratios indicate that because of the misspeci cation the models can match only some aspects of the returns distribution exempli ed by components of the SNP score. All of these models seem to capture the tails of the distribution foregoing matching more intuitively appealing GARCH components. The AFF1V model is the most dramatic example: its speed of mean reversion, 33 is about 28 times larger than that of logarithmic models, which indicates highly erratic behavior capable of generating extreme tails, but missing the main bulk of the returns distribution.

In fact, the estimated 33 is about 40 times larger than the speed coe cient in a ne models estimated by ABL and EJP. In order to understand this puzzling result better, we evaluate the AFF1V estimation results based on the homogeneous score 11118000 appearing in (28). This score mitigates the in uence of the tails, and, therefore, a misspeci ed model should be able to match the GARCH components of the score better.

Table 2 reports the parameter estimates of AFF1V based on the homogeneous score 11118000. The most interesting feature of Table 2 is that it o ers two sets of parameters for one model. The parameter estimates di er particularly with respect to 33 measuring the speed of mean reversion in the volatility process. The intuitive  t yields estimates with slow mean reversion, i.e. 33 equals −3:39, or half-life of 2.5 months, which conforms to the usual empirical  ndings. However, the intuitive  t turns out to be a local minimum of the EMM objective function equal to 31.815, as there is a better  t, which we refer to as the best with a lower 2 of 17.886 and, unlike previous  ndings, with very fast mean reversion, which corresponds to volatility half-life of 1.3 days.9 Panel B of Table 2 shows the EMM t-ratio diagnostics. We learn that the intuitive  t violates the moment conditions associated with Hermite polynomial coe cients

9 The better  t was discovered with the help of the heterogenous score, but theoretically it can be found via meticulous grid search of the starting values, so the heterogeneous score is not required for this.

Table 2 Parameter estimates, standard errors and t-ratio diagnostics for the AFF1V model, homogeneous score case

Intuitive Best Est SE Est SE

- Panel A. Parameter estimates and standard errors 10 0.1096 0.0652 0.0989 0.0203

- 12 0.8992 1.5165 5.7842 2.3474 22 −1.1644 3.5986 −44.5889 30.8810 30 0.8445 0.1460 1.1864 0.0136 33 −3.3857 0.7865 −132.2989 36.0200
- 13 0.0604 0.0115 1.1245 0.0783

13 −0.2786 0.1459 −0.1574 0.0948 2 6 = 31:815 6 2 = 17:886

Intuitive Best

- Panel B. t-ratio diagnostics

- AR b0 −1.806 2.725
- AR b1 1.771 1.159

- GARCH 0 2.102 2.335
- GARCH 1a 0.849 3.352 GARCH 1g 1.671 3.111

- Hermite a01 −1.753 2.531
- Hermite a02 2.748 2.767
- Hermite a03 −2.305 2.733
- Hermite a04 2.527 2.786
- Hermite a05 −2.560 0.973
- Hermite a06 2.028 2.903
- Hermite a07 −2.662 0.023
- Hermite a08 1.762 2.670

Notes: Entries to the table show the parameter estimates along with conventional Wald-type standard errors determined by numerical di erentiation for one-factor a ne models:

dPt Pt = ( 10 + 12U2t) dt + 13U3t( 1 − 13 2 dW1t + 13 dW3t);

- dU2t = 22U2t dt + dW2t;
- dU3t = ( 30 + 33U3t) dt + U3t dW3t:

 tting the tail behavior, whereas the best  t fails at mimicking the GARCH volatility persistence moment conditions.

This evidence indicates that there is a dilemma in accommodating at the same time volatility persistence and tail behavior via a single SV factor.10 The AFF1V model combined with the homogenous score can put emphasis either on the persistence in the

10 Meddahi (2001) gives an excellent theoretical discussion of this issue in the framework of the discrete-time LL1V model.

Parameterestimatesandstandarderrorsfora nemodels

Table3

Notes:EntriestothetableshowtheparameterestimatesalongwithconventionalWald-typestandarderrorsdeterminedbynumericaldi erentiationforthe

0.87672.0354− J

0.03010.00230.00890.0026−− J

137.87420.166333.087617.43215.75211.07122.78980.54403.64070.8597−−−−− 33

0.01810.0420

27.02523.20742.14281.40143.00351.700610.959313.287011.62337.1798−−−−− 22

0.19910.00390.40580.05340.48300.01440.47620.09870.51990.0904−−−−− 13

0.02130.00020.00780.00100.01730.0010 J

0.10080.01840.09850.02020.10700.01980.086250.02360.08430.0226 10

4.43090.12334.21161.56941.55750.47243.21901.88393.18801.0081 12

1.22410.00091.15980.28940.97560.17031.01970.11520.74940.0826 30

1.04770.06050.29750.12580.07290.01250.04270.01010.07420.0124 13

EstSEEstSEEstSEEstSEEstSE

AFF1V-J0AFF1V-JAFF1V-JJAFF1VAFF2V

5.601.701.70 J

J 2 2(+U+U1dW+dW+dW)+(e1) dN;1;t−−−t 133t 144t1t 133t 144t1314

1.06550.0602 40

0.00500.0344 14

0.90310.0221 14

92.825013.6036− 44

√dU=(+U) dt+UdW+JdN;i=3;4;tit iiititit i03;t

2exp( );JJN(+J;  ):∼∼ J J3;t1;t3;tJ

=Udt+dW;dU2t 222t2t

=(+U) dt; 10 122tPt

NPoi();∼t J

a nemodels:

Notes:EntriestothetableshowtheparameterestimatesalongwithconventionalWald-typestandarderrorsdeterminedbynumericaldi erentiationfor

0.60870.85401.05310.34251.12191.00431.17012.51377.01955.9997−−−−− 22

6.37780.93154.30160.36010.00410.02910.05120.04100.12030.1227−−−−− 33

2.28820.03202.25850.02532.06591.02942.19690.04142.21430.0486−−−−− 10

0.64820.02160.63650.01070.33820.32850.29660.02400.34030.1077−−−−− 13

0.35380.07930.29150.04080.28040.0564−−− 14

74.761010.799452.66733.110751.30828.2119−−− 44

- 0.53420.11680.04080.3672 33
- 1.92280.22602.21690.3655 44

3.54770.51622.76880.25972.74420.3130 14

0.08310.02000.08410.01950.07800.03370.05890.02250.06740.0279 10

0.67870.05130.88700.13970.98330.48201.16700.78722.19270.7281 12

1.37080.10591.20510.04100.03670.02610.08630.04000.13480.0695 13

EstSEEstSEEstSEEstSEEstSE

LL1VLL1VFLL2VLL2VILL2VF

Parameterestimatesandstandarderrorsforlogarithmicmodels

logarithmicmodels:

Table4

2 2=(+U) dt+exp(+U+U)(1dW+dW+dW);−− 10 122t 10 133t 144t1t 133t 144t1314Pt

=Udt+dW;dU2t 222t2t

dU=Udt+(1+U)dW;i=3;4; iit iiit iiitit

=0forLLor=1forLLF: i i

Table 5 t-ratio diagnostics

LL1V LL1VF LL2V LL2VI LL2VF AFF1V AFF2V AFF1V-J0 AFF1V-J AFF1V-JJ

- AR b0 −1.509 −0.081 1.706 0.410 −0.110 1.428 0.912 −3.120 0.566 1.553
- AR b1 1.593 0.521 0.941 0.011 −0.409 0.397 1.122 0.266 −0.137 0.456

- GARCH 0 3.828 3.519 2.364 1.842 1.675 3.580 0.858 2.996 −0.699 −1.884
- GARCH 1a 2.804 2.641 3.167 1.521 1.761 3.992 1.844 2.079 −0.448 −2.335 GARCH 1g 3.664 3.164 2.765 1.708 1.688 3.973 1.483 2.905 −0.553 −2.133

- Hermite a10 0.033 0.665 −0.748 −0.273 −0.177 −0.497 −1.853 −0.919 −1.379 −0.614

- Hermite a01 0.694 0.094 2.117 0.407 0.051 1.085 2.240 −0.837 2.509 0.992

Hermite a11 1.938 0.531 0.740 −0.473 −0.825 −0.604 0.955 1.623 −0.504 −0.047

- Hermite a02 3.899 3.660 3.719 0.789 −0.034 2.325 2.471 2.106 0.556 1.827

Hermite a12 −1.189 −0.743 −1.477 −0.841 −0.469 −0.920 −2.653 −1.738 −1.213 −0.591

- Hermite a03 −0.080 −0.233 2.134 0.136 0.040 0.827 1.064 −0.981 2.432 0.562
- Hermite a04 4.313 4.192 4.012 1.106 0.115 1.633 2.758 1.942 0.430 1.173
- Hermite a05 −1.243 −0.790 0.252 −0.451 −0.076 0.582 −0.826 −1.119 1.580 −0.115
- Hermite a06 3.502 3.557 1.587 1.344 0.392 1.597 2.464 1.539 0.075 0.253
- Hermite a07 −1.841 −1.075 −1.095 −0.912 −0.276 0.253 −1.706 −1.103 0.806 −0.343
- Hermite a08 2.528 2.710 1.271 1.079 0.358 1.833 2.168 1.290 −0.420 −0.754

volatility or the tail behavior whereas the heterogeneous score restricts the one factor model to emphasizing the tail behavior only.

- 3.2.2. Di usion extensions: multiple SV models The second SV factor in AFF2V leads to a tremendous improvement in capturing

the returns dynamics. The t-ratios indicate that the model does a good job with the tails and signi cantly improves the  t for the GARCH components of the score. It is clear that for this speci cation one SV factor, U3, is working on the main part of the distribution (notice that its persistence is much higher than that of the AFF1V model) and another factor, U4, is matching the tails. The relative success of this model is evident in the dramatic decrease of the objective function value from 20.196 for AFF1V to 13.668. However, the speed of mean reversion of the persistent factor U3 is still very high, which indicates potential misspeci cation of the model. Moreover, the loss of degrees of freedom associated with the increase in the number of parameters is not compensated by the decrease in the objective function value. The p-values for the two a ne models are roughly the same and therefore AFF2V is rejected as well.

Note that while single factor models are known to have negative correlation between innovations in volatility and returns, this may not be the case for the two-factor model. The models have been parameterized so that the coe cients 13 and 14 come out as correlations. We  nd in Table 3 a correlation in AFF1V equal to −0:19, the correlations of returns with U3 and U4 are equal to −0:41 and 0.90, respectively. The leverage e ect formula (4) will allow us to understand how these correlations a ect overall relationship between returns and volatility.

Specializing the general formula (4) to the case of AFF2V we obtain

√U3t + 14 14√U4t

corr(dU1t; 13 dU3t + 14 dU4t) = 13 13

dt: (29)

2 13U3t + 14 2 U4t

Since correlation coe cients take opposite signs, the leverage could become positive in certain states. To asses the likelihood of this happening, we  rst compute the “average” case. Ideally, we would have to compute the unconditional leverage e ect. However, we cannot do this analytically. Therefore, we compute something that is very close to the unconditional leverage e ect. Namely, we evaluate the conditional leverage e ect

- at the unconditional, or long-run, means of the states, which are equal to i0= ii. After substituting values of the parameters and the long-run means into (29) we  nd the value of leverage e ect equal to −0:3971.

In order to investigate a possibility of the positive value of the leverage e ect, we consider a very unlikely scenario: factor U3 is equal to 1=10th of its long-run mean and factor U4 is equal to 10 times of its long-run mean. This scenario puts a lot of weight on the contribution of the positive correlation coe cient 14 to the overall leverage e ect. In this case, the leverage is equal to −0:3175. So, as the factor U4 increases, the leverage e ect moves into the positive direction, but very slowly. As a result, positive leverage is theoretically feasible, but is highly unlikely.

The second factor in logarithmic models leads to improvements as well. However, since it enters the model multiplicatively, U4 will work as stochastic volatility of volatility rather than the factor dedicated to the tails of distribution. The LL2V is the least successful speci cation. Despite its p-value of 2% being higher than those of all pure di usive a ne models and all single factor logarithmic models, it is still quite low for the model to be retained as an adequate model. In particular, when one examines the t-ratio diagnostics, they show only marginal improvements over single factor models. Moreover, some of the key model parameters related to the more persistent factor U3 ( 33, 13, and 13) are insigni cant.

The LL2VF speci cation, which adds feedback to the LL2V speci cation, dominates all di usion models based on t-ratios, p-values, and objective function values. The estimated parameters clearly indicate extreme persistence, i.e. near unit root discretely sampled, of U3 and extreme mean reversion, i.e. near white noise discretely sampled, of U4.

Evaluating LL2VF more carefully, one observes that 33, the coe cient controlling the feedback component of U3 is not signi cantly di erent from zero. The factor’s persistence parameter, 33, is not signi cant either. Our last logarithmic speci cation LL2VI explores the possibility of modeling the persistent factor U3 without feedback. We  nd that, despite an increase in the objective function, additional degree of freedom leads to p-value very close to that of LL2VF. Moreover, all nice t-ratio diagnostics remain intact and 33 becomes signi cant. These results suggest that the introduction of feedback to both SV factors is unnecessary, and LL2VI becomes our preferred logarithmic model.

Interestingly, the point estimates of the leverage e ect coe cients 13 and 14 are −0:30 and −0:29, respectively. Hence, they are both negative and signi cant. The value

of 14 is quite a dramatic reversal as compared to AFF2V. This is additional evidence that a ne and logarithmic speci cations work in fundamentally di erent ways.

Indeed, specializing the general formula (4) to the case of LL2VI we obtain corr(dU1t; 13 dU3t + 14 dU4t) = 13 13

+ 14 14(1 + 44U4t)

dt: (30)

2 13 + 14 2 (1 + 44U4t)2

As we noted earlier in Section 1.1.3, the factor U4 is a GARCH-di usion shifted by 1= 44. Therefore, the expression 1+ 44U4 will always be nonnegative. Since both correlation coe cients are below zero, the leverage e ect will be negative in any state. For comparison with the a ne model, we compute the conditional leverage e ect evaluated at the long-run mean of U4. It is equal to −0:3006. So, on average, logarithmic models produce a slightly smaller leverage e ect.

- 3.2.3. Jump extensions Our  ndings indicate that logarithmic di usion models overwhelmingly dominate

the a ne di usion models mainly because of the multiplicative speci cation of the volatility. However, we would like to investigate the role of jumps in a ne models since they were shown to be important by several authors. This analysis will lead to a fair comparison between a ne and logarithmic models.

The  rst speci cation, AFF1V-J0, o ers a somewhat modest improvement in the EMM objective function value as compared to AFF1V. Moreover, because of the loss of one degree of freedom the p-value is slightly worse. Turning to the t-ratios we see a mild improvement in the GARCH components of the score. However, looking at the parameter estimates, it becomes clear that the di usion part of the model becomes much more reasonable. In particular, the persistence of U3 increases 24-fold. This is not surprising: incorporating jumps provides additional  exibility in  tting the tails of the returns distribution, relieving the volatility factor from this burden. Therefore, the volatility process coe cients are much more closely aligned with the intuitive  t in Table 2.

ABL, who study the speci cation of type (1)  nd that jump occur about six times per year and on average jump up and down by the same magnitude. Clearly, jump component is  tting the tail behavior. A priori, it seems that a second SV factor can perform the same task. Our results con rm this intuition: AFF2V does even a better job than AFF1V-J0.

The jumps in AFF1V-J0 are symmetric (because J was set to zero) and occur 5.6 times per year.11 Casual observation of the return series in Fig. 1 indicates that this is not the case: there seem to be more negative than positive jumps, and the negative moves tend to more severe. Moreover, the extreme events seem to occur less frequently than six times a year. One way to formally test this is to estimate J as a free parameter. AFF1V-J shows a very di erent picture: the frequency of jumps drops to 1.7 per year and the jump size has a signi cant negative mean, which is consistent with

11 Because of our pro ling approach to the estimation of J (see Section 2), we cannot compute standard errors. However, for all of our jump models the objective function dramatically increased outside of the interval ˆ J ± 0:1. Hence, this could be considered as an informal con dence interval.

negative skewness of returns. The volatility component becomes even more persistent. The improvement occurs not only in realism of the parameters estimates, but in statistic inference as well: t-ratios substantially improve and the model cannot be rejected at 5% con dence level, but is rejected at 10%. Moreover, the properties of the jump-di usion model become intuitive: volatility is more persistent, jumps are seldom: a little bit less than two per year.

The AFF1V-JJ model has an appealing feature that during market stress, when returns jump down, spot volatility jumps up.12 In combination these two components can produce a market move of a large size. As a result of a jump, volatility deviates from its long-run mean and then mean reversion pulls it back via di usive movements. Such dynamics are very similar to the one generated by multiplicative volatility factors in LL2VI. Despite the intuitive appeal of AFF1V-JJ, we cannot distinguish it from a more parsimonious AFF1V-J based on the EMM diagnostics. Dramatic decrease in the objective function is not compensated by the degrees-of-freedom loss. As a result, asymptotic p-values are almost identical. The t-ratio diagnostics do not clarify the picture either: while the GARCH part of the auxiliary model seems to be  t worse by AFF1V-JJ, we have recently uncovered evidence that the t-ratios might not be reliably estimated when the degrees of freedom are small. Hence, based on the parsimony considerations, we select AFF1V-J as our preferred a ne model.

- 3.3. Additional diagnostics via reprojection

Our results up to this point indicate that, intuitively, a pure di usion model with multiplicative volatility factors, one of which is almost explosive, can generate dynamics similar to that of single volatility model with explicit jump component. The empirical success of the logarithmic speci cation can intuitively be explained by the fact that the second factor not only accommodates the tails of the (conditional) return distribution, but also accommodates the volatility dynamics during extreme market conditions, since the speci cation of the second factor is mean reverting with local persistence and state-dependent volatility of volatility. The potential explosiveness of the persistent volatility factor contributes to realistic modeling of the extreme behavior. This  nding has potentially very important implications because, if the di usion model turns out to be better than the jump di usion previously advocated in the literature, this will have very important simplifying implications for hedging as well as complicating implications for option pricing.

For this reason, we further investigate the best models from each class in order to better understand the di erences and commonalities between the two models. We turn therefore our attention to the time-series properties of the volatility factors. Since the factors are latent we use the reprojection method of Gallant and Tauchen (1998). Figs. 2–5 report time-series plots of the Dow Jones returns and volatility factors

12 This behavior is modeled by negative correlation J. It is very hard to estimate this parameter with high precision because it measures the correlation of two seldom and unobservable events, therefore the large standard error reported in the table should not be surprising.

Dow Jones Industrial Average, Daily Returns, 1953-1999

| |
|---|

10

0

- -30
- -20
- -10

1955 1960 1965 1970 1975 1980 1985 1990 1995 2000

| |
|---|

- -4
- -3
- -2
- -1

- 0
- 1

AFF1V Model, Filtered Log Volatility Factor

| |
|---|

1955 1960 1965 1970 1975 1980 1985 1990 1995 2000

- -4
- -3
- -2
- -1

1955 1960 1965 1970 1975 1980 1985 1990 1995 2000 AFF1V-J Model, Filtered Log Volatility Factor

- 0
- 1

Fig. 2. Reprojection of volatility factors from AFF1V and AFF1V-J models—1953–1999.

reprojected from the single volatility (benchmark) models in a ne and logarithmic class as well as from the most successful models in each class.

The  rst two plots pertain to AFF1V and AFF1V-J covering sample 1953–1999 (Fig. 2) and a single year, namely 1998 (Fig. 3). Likewise, Figs. 4 and 5 cover LL1VF and LL2VI for the same samples, i.e. 1953–1999 and 1998. Note that we report the estimates of the logarithm of the a ne volatility factors to make them comparable to the volatility factors from the logarithmic models. It is worth noting that when one looks at Figs. 3 and 4 it appears that the model without jumps (AFF1V) creates a more volatile reprojected factor than the model with jumps (AFF1V-J). This is as expected

| |
|---|

- -10
- -5

0

5

Dow Jones Industrial Average, Daily Returns, 1998

| |
|---|

1998 1998.1 1998.2 1998.3 1998.4 1998.5 1998.6 1998.7 1998.8 1998.9 1999

- -3
- -2
- -1

0

AFF1V Model, Filtered Log Volatility Factor

| |
|---|

1998 1998.1 1998.2 1998.3 1998.4 1998.5 1998.6 1998.7 1998.8 1998.9 1999

- -3
- -2
- -1

1998 1998.1 1998.2 1998.3 1998.4 1998.5 1998.6 1998.7 1998.8 1998.9 1999

AFF1V-J Model, Filtered Log Volatility Factor

0

Fig. 3. Reprojection of volatility factors from AFF1V and AFF1V models—1998.

given that the parameter estimates of the model will jumps yielded a more persistent U3 process. Note that in logarithmic models the volatility level is controlled through one parameter 10, while in a ne models it is controlled through i0= ii. Since we can not allocate 10 between the two volatility factors in LL2VF, we report factors scaled by the respective weights, i0, without regard to the level on all plots. As a result, one can compare the shape and relative size of the volatility, but not the level.

The one-factor models yield reprojected volatilities which look quite di erent. The AFF1V appears to be more erratic, which is consistent with a much lower persistence

Dow Jones Industrial Average, Daily Returns, 1953-1999

| |
|---|

10

0

- -30
- -20
- -10

1955 1960 1965 1970 1975 1980 1985 1990 1995 2000

LL1VF Model, Filtered Volatility Factor

| |
|---|

- 0
- 1
- 2
- 3

-1

1955 1960 1965 1970 1975 1980 1985 1990 1995 2000

LL2VI Model, First Filtered Volatility Factor

| |
|---|

- 0
- 1
- 2
- 3

-1

1955 1960 1965 1970 1975 1980 1985 1990 1995 2000

LL2VI Model, Second Filtered Volatility Factor

| |
|---|

- 0
- 1
- 2
- 3

-1

1955 1960 1965 1970 1975 1980 1985 1990 1995 2000

Fig. 4. Reprojection of volatility factors from LL1VF and LL2VI models—1953–1999.

measured by 33. Nonetheless, the overall pattern and the volatility range seems to be close for both models. These plots partially con rm the  ndings of ABL, who compare the empirical  t of logarithmic and a ne volatility models.

| |
|---|

- -10
- -5

0

5

Dow Jones Industrial Average, Daily Returns, 1998

| |
|---|

1998 1998.1 1998.2 1998.3 1998.4 1998.5 1998.6 1998.7 1998.8 1998.9 1999

- -0.5

- 0

- 0.5
- 1

- 1.5

LL1VF Model, Filtered Volatility Factor

| |
|---|

1998 1998.1 1998.2 1998.3 1998.4 1998.5 1998.6 1998.7 1998.8 1998.9 1999

- -0.5

1998 1998.1 1998.2 1998.3 1998.4 1998.5 1998.6 1998.7 1998.8 1998.9 1999

LL2VI Model, First Filtered Volatility Factor

- 0

- 0.5
- 1

- 1.5

LL2VI Model, Second Filtered Volatility Factor

- 0

- 0.5
- 1

- 1.5

| |
|---|

-0.5

1998 1998.1 1998.2 1998.3 1998.4 1998.5 1998.6 1998.7 1998.8 1998.9 1999

Fig. 5. Reprojection of volatility factors from LL1VF and LL2VI models—1998.

The volatility factors in the preferred speci cations resemble each other much better. The persistence, range and level (after taking into an account the value of 10 ≈ −2:2) of the  rst volatility factor, U3t, of the LL2VI model is very close to the

only volatility factor of AFF1V-J. We plotted a single year from the sample, namely 1998, to highlight that the  rst factor in LL2VI picks up persistence, as does the volatility factor in AFF1V-J, (see Figs. 3 and 5), and in fact resembles very much the single factor model reprojected volatilities. The second factor of LL2VI looks very di erent. This is apparent from both the entire sample plot in Fig. 4 as well as the 1998 reprojected volatilities. The second volatility factor U4t clearly behaves like white noise allowing to generate observations in the tails similarly to the jump component of AFF1V-J.13

The local behavior of LL2VI is very di erent from AFF1V-J model, even from a theoretical point of view. For the jump-di usion model extreme events are represented by the i.i.d. jump process, while the second volatility factor in the LL2VI model has a half-life of three and a half-days, meaning that extreme events taper o  over several days. This is consistent with Das and Sundaram (1999) who  nd downward sloping and hump-shaped term structures of higher moments for jump di usions and pure di usions, respectively. The model diagnostics that we have used do not pick up the subtle features of the data generating processes. The statistical tools appear unable to discriminate between such features pertaining to events rarely occuring over the entire sample (despite its length).

- 4. Conclusion

In this paper, we examine various generalizations of SV models via the EMM estimation procedure applied to a sample of post-war Dow Jones daily return series.

We explored and compared the following two-factor speci cations (1) a continuous path a ne di usion factor process augmented with a jump component to better  t the tail behavior, (2) a two-factor logarithmic SV speci cation with possible feedback, the latter causing volatility of volatility to increase, and (3) the two factor a ne SV model.

We  nd that none of the one-factor stochastic volatility speci cations  t the data, which con rms previous  ndings. We note that the asymptotic p-value for the a ne model is much higher than for logarithmic speci cation.

The two-factor a ne model improves dramatically upon the single volatility model in terms of the EMM objective function value. However, the associated loss of degrees of freedom does not compensate enough: p-values of one and two factor a ne models are roughly the same. The same conclusion applies to a ne model with jumps to returns which have zero mean. However, the model cannot be rejected at 10% con dence level when the constraint on the mean of the jump size is relaxed. Moreover, this simple modi cation dramatically changes the behavior of both volatility, which becomes more persistent, and jumps, which become less frequent. The jumps to volatility further reduce the objective function value.

13 We notice that the reprojected path of U4t features the local exuberance around the summer of 1998 when LTCM and the Russian  nancial crisis shook  nancial markets.

Based on the p-values we  nd that the logarithmic two-factor model speci cation without feedback is rejected at the 5% signi cance level, though it dominates all rejected a ne models. The most important new  nding is that two factor logarithmic speci cation involving at least one volatility factor with feedback  t the data with the p-values of over 50%. Thus, we  nd that logarithmic factor model with feedback, which has rapidly moving stochastic volatility of volatility, is at par with the a ne jump model.

All two-factor speci cations feature one factor which accounts for the persistence in volatility and the second determines the tail behavior. The empirical success of the logarithmic speci cation can intuitively be explained by the fact that the second factor not only accommodates the tails of the (conditional) return distribution, but also accommodates the volatility dynamics during extreme market conditions, since the speci cation of the second factor is mean-reverting with local persistence and state-dependent volatility of volatility. The near explosiveness of the short memory volatility factor contributes to realistic modeling of the extreme behavior.

Casual observations of the data reveal that abrupt changes in the volatility are an essential ingredient of a successful model. Jumps in returns and volatility simultaneously appear to be the ideal model. Yet, the improvement in statistical  t is not strong enough to justify this conclusion. The statistical tools combined with the data do not allow us to  ne-tune the diagnostic any further to declare an overall winner. Additional data, e.g. options data, would help in discriminating the remaining competing models.

An alternative approach is, rather than trying to establish the “ideal” model, to realize that there will always be uncertainty regarding model misspeci cation and to be robust with respect to it in the spirit of Anderson et al. (2002). However, our model uncertainty does not directly fall into their framework because the model perturbations are not absolutely continuous with respect to each other. Hence, more theoretical work is required before this approach can be implemented in practice.

Acknowledgements

We would like to thank Torben Andersen, the Editor, two anonymous referees and Nour Meddahi, the third referee, for comments that substantially improved the paper. We are also grateful to Luca Benzoni, Paul Glasserman, Michael Johannes, David Robinson, the conference and seminar participants at the CAP Mathematical Finance Workshop, Columbia University, the Conference on Risk Neutral and Objective Probability Distributions, Fuqua School of Business, Duke University, CIREQ-CIRANOMITACS Conference on Univariate and Multivariate Models for Asset Pricing, University of Montreal, NBER Summer Institute 2002, NBER/NSF Time Series Conference 2002, CIRANO and Vanderbilt University for their comments. All remaining errors are our own. This paper subsumes part of the material presented in the working paper titled “A New Class of Stochastic Volatility Models with Jumps: Theory and Estimation.”

Appendix A. Regularity conditions for logarithmic models

The use of logarithmic volatility models raises several issues regarding regularity conditions which ensure existence of moments, strong solutions to stochastic di erence equations (SDEs), and convergence of discretization schemes. In particular, the stochastic integrals associated with the SDEs of the logarithmic SV models with feedback are not de ned in the usual sense (the integrand has to be in L2, e.g. Kloeden and Platen, 1995, pp. 81–82).14 The exponential transformation of the volatility factors results in explosive behavior. The explosiveness of the logarithmic SV process has been recognized for a while in the term structure literature. For instance, Brace et al. (1997) replace the continuously compounded rate by the e ective annual rate. This removes the exponentiation of a lognormal variable, which in its turn removes fatness in the tail, so that the moments exist.

We have to ensure that solutions to the speci ed logarithmic SV processes exist and are unique.15 The processes we consider do satisfy the local Lipshitz conditions, but violate the usual growth conditions in Itˆo’s theorem (Kloeden and Platen, 1995, p. 128). To resolve this problem we splice the exponential volatility function in (8) with appropriate growth conditions at the point, which corresponds to the volatility level unlikely to occur in the U.S. markets, i.e. 150% annualized.16

Formally, instead of the volatility speci cation (8), we estimated

exp(u) if u6u0 = log(1:5)

 

(u) =

(A.1)

√euu00 u0 − u02 + u2 otherwise



where at least one of the i in (3) is equal to one. Now it is clear that we can  nd a constant K, such that

2(u)6K2(1 + u2): (A.2)

The particular functional form of in (A.1) is selected to ensure a smooth splicing, i.e. the two functions and their  rst derivatives coincide at u0.

This modi cation is adequate to ensure the existence of stochastic integrals, SDE solutions, convergence of discretization schemes, and EMM applicability. From the practical perspective, we are e ectively considering the exponential form of the volatility function. Fig. 6 compares both speci cations.

- 14 We are greatful to Nour Meddahi for pointing this out to us.
- 15 It should be noted that we are discussing su cient conditions. See Chen et al. (2001) for further

discussion.

- 16 For comparison, on October 19, 1987 implied 1 month volatility on S& P 100, which is approximately

equal to integrated volatility over the whole month, was equal to 150%.

- 0

- 1

- 2

- 3

- 4

- 5

- 6

- 7

- 8

- 9

- 10

-5 -4 -3 -2 -1 0 1 2

Fig. 6. The functional form of the di usion coe cient in logarithmic models: spline vs. pure exponential form.

References

A  t-Sahalia, Y., 2002. Maximum likelihood estimation of discretely sampled di usions: a closed-form approximation approach. Econometrica 70, 223–262.

A  t-Sahalia, Y., Brandt, M., 2001. Variable selection for portfolio choice. Journal of Finance 56, 1297–1351. Alizadeh, S., Brandt, M.W., Diebold, F.X., 2002. Range-based estimation of stochastic volatility models.

Journal of Finance 57, 1047–1091. Andersen, T., Benzoni, L., Lund, J., 2002. An empirical investigation of continuous-time equity return models. Journal of Finance 57, 1239–1284. Anderson, E., Hansen, L.P., Sargent, T., 2002. A quartet of semi-groups for model speci cation, detection, robustness, and the price of risk. Working Paper, University of North Carolina. Bakshi, G., Cao, C., Chen, Z., 1997. Empirical performance of alternative option pricing models. Journal of Finance 52, 2003–2049. Bates, D., 2000. Post-’87 crash fears in the S& P 500 futures option market. Journal of Econometrics 94, 181–238. Black, F., Scholes, M., 1973. The pricing of options and corporate liabilities. Journal of Political Economy 81, 637–654. Brace, A., Gatarek, D., Musiela, M., 1997. The market model of interest rate dynamics. Mathematical Finance 7, 127–155. Chacko, G., Viceira, L., 1999. Spectral GMM estimation of continuous-time processes. Discussion Paper, Harvard Business School.

Chen, X., Hansen, L.P., Carrasco, M., 2001. Nonlinearity and temporal dependence. Discussion Paper, University of Chicago.

Chernov, M., Ghysels, E., 2000. A study towards a uni ed approach to the joint estimation of objective and risk neutral measures for the purpose of options valuation. Journal of Financial Economics 56, 407–458. Dai, Q., Singleton, K., 2000. Speci cation analysis of a ne term structure models. Journal of Finance 55,

1943–1978. Das, S., Sundaram, R., 1999. Of smiles and smirks: a term-structure perspective. Journal of Financial and Quantitative Analysis 34, 211–240. Detemple, J., Garcia, R., Rindisbacher, M., 2002. Asymptotic properties of Monte Carlo estimators of di usion processes. Working Paper, CIRANO. Du e, D., Pan, J., Singleton, K., 2000. Transform analysis and option pricing for a ne jump-di usions. Econometrica 68, 1343–1377. Durham, G., Gallant, A.R., 2000. Numerical techniques for maximum likelihood estimation of continuous-time di usion processes. Working Paper, University of North Carolina. Elerian, O., Chib, S., Shephard, N., 2001. Likelihood inference for discretely observed non-linear di usions. Econometrica 69, 959–993. Engle, R.F., Gonzales-Rivera, G., 1991. Semi-parametric ARCH models. Journal of Business and Economic Statistics 9, 345–359.

Engle, R.F., Lee, G., 1999. A long-run and short-run component model of stock return volatility. In: Engle, R.F., White, H. (Eds.) Cointegration, Causality and Forecasting—A Festschrift in Honour of Clive W.J. Granger, Oxford University Press, Oxford.

Eraker, B., Johannes, M., Polson, N., 2003. The impact of jumps in equity index volatility and returns.

Journal of Finance, forthcoming. Feller, W., 1971. An Introduction to Probability Theory and its Applications, Vol. II. Wiley, New York. Gallant, A.R., Hsieh, D., Tauchen, G., 1997. Estimation of stochastic volatility models with diagnostics.

Journal of Econometrics 81, 159–192. Gallant, A.R., Hsu, C.-T., Tauchen, G., 1999. Using daily range data to calibrate volatility di usions and extract the forward integrated variance. Review of Economics and Statistics, forthcoming. Gallant, A.R., Long, J.R., 1997. Estimating stochastic di erential equations e ciently by minimum chi-square. Biometrika 84, 125–141. Gallant, A.R., Tauchen, G., 1989. Seminonparametric estimation of conditionally constrained heterogeneous processes: asset pricing applications. Econometrica 57, 1091–1120.

Gallant, A., Tauchen, G., 1992. A nonparametric approach to nonlinear time series analysis: estimation and simulation, in: Parzen, E., Brillinger, D., Rosenblatt, M., Taqqu, M., Geweke, J., Caines, P. (eds.), New Dimensions in Time Series Analysis. Springer-Verlag, New York.

Gallant, A.R., Tauchen, G., 1993. SNP: a program for nonparametric time series analysis, version 8.3, User’s Guide. Discussion Paper, University of North Carolina at Chapel Hill.

- Gallant, A.R., Tauchen, G., 1996. Which moments to match? Econometric Theory 12, 657–681.
- Gallant, A.R., Tauchen, G., 1997. EMM: a program for e cient method of moments estimation, Version 1.4, User’s guide. Discussion Paper, University of North Carolina at Chapel Hill.
- Gallant, A.R., Tauchen, G., 1998. Reprojecting partially observed systems with application to interest rate di usions. Journal of American Statistical Association 93, 10–24.

Gallant, A.R., Tauchen, G., 2003. SNP: a program for nonparametric time series analysis, a user’s guide. Manuscript, University of North Carolina. (Available along with code via http://www.econ.duke.edu/∼get./snp.html).

Ghysels, E., Ng, S., 1998. A semiparametric factor model of interest rates and tests of the a ne term structure. Review of Economics and Statistics 80, 535–548. Heston, S.L., 1993. A closed-form solution for options with stochastic volatility with applications to bond

and currency options. Review of Financial Studies 6, 327–343. Jones, C., 2003. The dynamics of stochastic volatility. Journal of Econometrics, this issue. Kloeden, P.E., Platen, E., 1995. Numerical Solution of Stochastic Di erential Equations. Springer, Berlin. Meddahi, N., 2001. An eigenfunction approach for volatility modeling. Working Paper, University of

Montreal. Nelson, D., 1990. ARCH models as di usion approximations. Journal of Econometrics 45, 7–38.

Pan, J., 2002. The jump-risk premia implicit in options: evidence from an integrated time-series study. Journal of Financial Economics 63, 3–50. Platen, E., Rebolledo, R., 1985. Weak convergence of semimartingales and discretisation methods. Stochastic Processes and their Applications 20, 41–58. Powell, J., Stock, J., Stoker, T., 1989. Semiparametric estimation of index models. Econometrica 57, 1403–1430. Scott, L., 1987. Option pricing when the variance changes randomly: theory, estimation and an application.

Journal of Financial and Quantitative Analysis 22, 419–438. Stoker, T., 1993. Lectures on Semiparametric Econometrics. CORE Lecture Series. van der Vaart, A., 2000. Asymptotic Statistics. Cambridge University Press, Cambridge, MA.

