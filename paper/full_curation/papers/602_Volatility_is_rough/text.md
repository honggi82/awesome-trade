# arXiv:1410.3394v1[q-fin.ST]13Oct2014

## Volatility is rough

Jim Gatheral Baruch College, City University of New York jim.gatheral@baruch.cuny.edu

Thibault Jaisson∗ CMAP, Ecole´ Polytechnique Paris thibault.jaisson@polytechnique.edu

Mathieu Rosenbaum LPMA, Universit´e Pierre et Marie Curie (Paris 6) mathieu.rosenbaum@upmc.fr

October 14, 2014

Abstract Estimating volatility from recent high frequency data, we revisit the question of the smoothness of the volatility process. Our main result is that log-volatility behaves essentially as a fractional Brownian motion with Hurst exponent H of order 0.1, at any reasonable time scale. This leads us to adopt the fractional stochastic volatility (FSV) model of Comte and Renault [16]. We call our model Rough FSV (RFSV) to underline that, in contrast to FSV, H < 1/2. We demonstrate that our RFSV model is remarkably consistent with ﬁnancial time series data; one application is that it enables us to obtain improved forecasts of realized volatility. Furthermore, we ﬁnd that although volatility is not long memory in the RFSV model, classical statistical procedures aiming at detecting volatility persistence tend to conclude the presence of long memory in data generated from it. This sheds light on why long memory of volatility has been widely accepted as a stylized fact. Finally, we provide a quantitative market microstructurebased foundation for our ﬁndings, relating the roughness of volatility to high frequency trading and order splitting.

Keywords: High frequency data, volatility smoothness, fractional Brownian motion, fractional Ornstein-Uhlenbeck, long memory, volatility persistence, volatility forecasting, option pricing, volatility surface, Hawkes processes, high frequency trading, order splitting.

∗Thibault Jaisson gratefully acknowledges ﬁnancial support from the chair “Risques Financiers” of the Risk Foundation and the chair “Marche´s en Mutation” of the French Banking Federation.

### 1 Introduction

#### 1.1 Volatility modeling

In the derivatives world, log-prices are often modeled as continuous semimartingales. For a given asset with log-price Yt, such a process takes the form

dYt = µtdt + σtdWt,

where µt is a drift term and Wt is a one-dimensional Brownian motion. The term σt denotes the volatility process and is the most important ingredient of the model. In the Black-Scholes framework, the volatility function is either constant or a deterministic function of time. In Dupire’s local volatility model, see [22], the local volatility σ(Yt,t) is a deterministic function of the underlying price and time, chosen to match observed European option prices exactly. Such a model is by deﬁnition time-inhomogeneous; its dynamics are highly unrealistic, typically generating future volatility surfaces (see Section

- 1.3 below) completely unlike those we observe. A corollary of this is that prices of exotic options under local volatility can be substantially oﬀ-market. On the other hand, in so-called stochastic volatility models, the volatility

σt is modeled as a continuous Brownian semi-martingale. Notable amongst such stochastic volatility models are the Hull and White model [32], the Heston model [31], and the SABR model [29]. Whilst stochastic volatility dynamics are more realistic than local volatility dynamics, generated option prices are not consistent with observed European option prices. We refer to [26] and [39] for more detailed reviews of the diﬀerent approaches to volatility modeling. More recent market practice is to use local-stochastic-volatility (LSV) models which both ﬁt the market exactly and generate reasonable dynamics.

#### 1.2 Fractional volatility

In terms of the smoothness of the volatility process, the preceding models offer two possibilities: very regular sample paths in the case of Black-Scholes, and volatility trajectories with regularity close to that of Brownian motion for the local and stochastic volatility models. Starting from the stylized fact that volatility is a long memory process, various authors have proposed models that allow for a wider range of regularity for the volatility. In a pioneering paper, Comte and Renault [16] proposed to model log-volatility using fractional Brownian motion (fBM for short), ensuring long memory by choosing the Hurst parameter H > 1/2. A large literature has subsequently developed around such fractional volatility models, for example [12, 15, 44].

The fBM (WtH)t∈R with Hurst parameter H ∈ (0,1), introduced in [36], is a centered self-similar Gaussian process with stationary increments satisfying for any t ∈ R, ∆ ≥ 0, q > 0:

E[|WtH+∆ − WtH|q] = Kq∆qH, (1.1)

with Kq the moment of order q of the absolute value of a standard Gaussian variable. For H = 1/2, we retrieve the classical Brownian motion. The sample paths of WH are H¨lder-continuous with exponent r, for any r < H1. Finally, when H > 1/2, the increments of the fBM are positively correlated and exhibit long memory in the sense that

+∞

Cov[W1H,WkH − WkH−1] = +∞.

k=0

Indeed, Cov[W1H,WkH − WkH−1] is of order k2H−2 as k → ∞. Note that in the case of the fBM, there is a one to one correspondence between regularity

and long memory through the Hurst parameter H.

As mentioned earlier, the long memory property of the volatility process has been widely accepted as a stylized fact since the seminal analyses of Ding, Granger and Engle [20], Andersen and Bollerslev [1] and Andersen et al. [3]. Initially, it appears that the term long memory referred to the slow decay of the autocorrelation function (of absolute returns for example), anything slower than exponential. Over time however, it seems that this term has acquired the more precise meaning that the autocorrelation function is not integrable, see [8], and even more precisely that it decays as a power-law with exponent less than 1. Much of the more recent literature, for example [7, 11, 13], assumes long memory in volatility in this more technical sense. Indeed, meaningful results can probably only be obtained under such a speciﬁcation, since it is not possible to estimate the asymptotic behavior of the covariance function without assuming a speciﬁc form. Nevertheless, analyses such as that of Andersen et al. [3] use data that predate the advent of high-frequency electronic trading, and the evidence for long memory has never been suﬃcient to satisfy remaining doubters such as Mikosch and Sta˘ric˘ in [38]. To quote Rama Cont in [17]:

... the econometric debate on the short range or long range nature of dependence in volatility still goes on (and may probably never be resolved)...

One of our contributions in this paper is (we believe) to ﬁnally resolve this question, showing that the autocorrelation function of volatility does not behave as a power law, at least at usual time scales of observation. This implies

1Actually H corresponds to the regularity of the process in a more accurate way: in terms of Besov smoothness spaces, see Section 2.1.

that when stated in term of the asymptotic behavior of the autocorrelation function, the long memory question can simply not be answered. Nevertheless, we are able to provide explicit expressions enabling us to analyze thoroughly the dependence structure of the volatility process.

#### 1.3 The shape of the implied volatility surface

[Figure 1]

Figure 1.1: The S&P volatility surface as of June 20, 2013.

- As is well-known, the implied volatility σBS(k,τ) of an option (with logmoneyness k and time to expiration τ) is the value of the volatility parameter in the Black-Scholes formula required to match the market price of that option. Plotting implied volatility as a function of strike price and time to expiry generates the volatility surface, explored in detail in, for example, [26]. A typical such volatility surface generated from a “stochastic volatility inspired” (SVI) [27] ﬁt to closing SPX option prices as of June 20, 20132 is shown in Figure 1.1. It is a stylized fact that, at least in equity markets, although the level and orientation of the volatility surface do change over time, the general overall shape of the volatility surface does not change, at least to a ﬁrst approximation. This suggests that it is desirable to model

2Closing prices of SPX options for all available strikes and expirations as of June 20, 2013 were sourced from OptionMetrics (www.optionmetrics.com) via Wharton Research Data Services (WRDS).

volatility as a time-homogenous process, i.e. a process whose parameters are independent of price and time.

However, conventional time-homogenous models of volatility such as the Hull and White, Heston, and SABR models do not ﬁt the volatility surface. In particular, as shown in Figure 1.2, the observed term structure of at-themoney (k = 0) volatility skew

∂ ∂k

ψ(τ) :=

σBS(k,τ)

k=0

is well-approximated by a power-law function of time to expiry τ. In contrast, conventional stochastic volatility models generate a term structure of at-the-money (ATM) skew that is constant for small τ and behaves as a sum of decaying exponentials for larger τ.

[Figure 2]

- Figure 1.2: The black dots are non-parametric estimates of the S&P ATM volatility skews as of June 20, 2013; the red curve is the power-law ﬁt ψ(τ) = Aτ−0.4.

In Section 3.3 of [25], as an example of the application of his martingale expansion, Fukasawa shows that a stochastic volatility model where the volatility is driven by fractional Brownian motion with Hurst exponent H generates an ATM volatility skew of the form ψ(τ) ∼ τH−1/2, at least for small τ. This is interesting in and of itself in that it provides a counterexample to the widespread belief that the explosion of the volatility smile as τ → 0 (as clearly seen in Figures 1.1 and 1.2) implies the presence of jumps [10]. The main point here is that for a model of the sort analyzed by Fukasawa to generate a volatility surface with a reasonable shape, we would need

to have a value of H close to zero. As we will see in Section 2, our empirical estimates of H from time series data are in fact very small.

The volatility model that we will specify in Section 3.1, driven by fBM with H < 1/2, therefore has the potential to be not only consistent with the empirically observed properties of the volatility time series but also consistent with the shape of the volatility surface. In this paper, we focus on the modeling of the volatility time series. A more detailed analysis of the consistency of our model with option prices is left for a future article.

#### 1.4 Main results and organization of the paper

In Section 2, we report our estimates of the smoothness of the log-volatility for selected assets. This smoothness parameter lies systematically between 0.08 and 0.2 (in the sense of H¨lder regularity for example). Furthermore, we ﬁnd that increments of the log-volatility are approximately normally distributed and that their moments enjoy a remarkable monofractal scaling property. This leads us to model the log of volatility using a fBM with Hurst parameter H < 1/2 in Section 3. Speciﬁcally we adopt the fractional stochastic volatility (FSV) model of Comte and Renault [16]. We call our model Rough FSV (RSFV) to underline that, in contrast to FSV, we take H < 1/2. We also show in the same section that the RFSV model is remarkably consistent with volatility time series data. The issue of volatility persistence is considered through the lens of the RFSV model in Section

- 4. Our main ﬁnding is that although the RFSV model does not have any long memory property, classical statistical procedures aiming at detecting volatility persistence tend to conclude the presence of long memory in data generated from it. This sheds new light on the supposed long memory in the volatility of ﬁnancial data. In Section 5, we apply our model to forecasting volatility. In particular, we show that RFSV volatility forecasts outperform conventional AR and HAR volatility forecasts. Finally, in Section 6, we present a market microstructure explanation for the regularities we observe in the volatility process at the macroscopic scale. We show that the empirical behavior of volatility may be explained in terms of order splitting and the high degree of endogeneity of the market ascribed to algorithmic trading. Some proofs are relegated to the appendix.

### 2 Smoothness of the volatility: empirical results

In this section we report estimates of the smoothness of the volatility process for four assets: The DAX and Bund futures contracts, for which we estimate integrated variance directly from high frequency data using an estimator based on the model with uncertainty zones, [42, 43], and the S&P and

NASDAQ indices, for which we use precomputed realized variance estimates from the Oxford-Man Institute of Quantitative Finance Realized Library3.

#### 2.1 Estimating the smoothness of the volatility process

Let us ﬁrst pretend that we have access to discrete observations of the volatility process, on a time grid with mesh ∆ on [0,T]: σ0, σ∆,...,σk∆,..., k ∈ {0, T/∆ }. Set N = T/∆ , then for q ≥ 0, we deﬁne

N

1 N

|log(σk∆) − log(σ(k−1)∆)|q.

m(q,∆) =

k=1

In the spirit of [46], our main assumption is that for some sq > 0 and bq > 0, as ∆ tends to zero,

Nqsqm(q,∆) → bq. (2.1) Under additional technical conditions, Equation (2.1) essentially says that the volatility process belongs to the Besov smoothness space Bq,sq∞ and does not belong to Bq,s q∞, for s q > sq, see [45]. Hence sq can really be viewed

- as the regularity of the volatility when measured in lq norm. In particular, functions in Bq,s ∞ for every q > 0 enjoy the H¨lder property with parameter h for any h < s. For example, if log(σt) is a fBM with Hurst parameter H, then for any q ≥ 0, Equation (2.1) holds in probability with sq = H and it can be shown that the sample paths of the process indeed belong to

Bq,H∞ almost surely. Assuming the increments of the log-volatility process are stationary and that a law of large number can be applied, m(q,∆) can also be seen as the empirical counterpart of

E[|log(σ∆) − log(σ0)|q].

Of course, the volatility process is not directly observable, and an exact computation of m(q,∆) is not possible in practice. We must therefore proxy spot volatility values by appropriate estimated values. Since the minimal ∆ will be equal to one day in the sequel, we proxy the (true) spot volatility daily at a ﬁxed given time of the day (11 am for example). Two daily spot volatility proxies will be considered:

• For our ultra high frequency intraday data (DAX future contracts and Bund future contracts4, 1248 days from 13/05/2010 to 01/08/20145),

- 3http://realized.oxford-man.ox.ac.uk/data/download. The Oxford-Man Institute’s Realized Library contains a selection of daily non-parametric estimates of volatility of ﬁnancial assets, including realized variance (rv) and realized kernel (rk) estimates. A selection of such estimators is described and their performances compared in, for example, [28] .
- 4For every day, we only consider the future contract corresponding to the most liquid maturity.
- 5Data kindly provided by QuantHouse EUROPE/ASIA, http://www.quanthouse.com.

we use the estimator of the integrated variance from 10 am to 11 am London time obtained from the model with uncertainty zones, see [42, 43]. After renormalization, the resulting estimates of integrated variance over very short time intervals can be considered as good proxies for the unobservable spot variance. In particular, the one hour long window on which they are computed is small compared to the extra day time scales that will be of interest here.

• For the S&P and NASDAQ indices6, we proxy daily spot variances by daily realized variance estimates from the Oxford-Man Institute of Quantitative Finance Realized Library (3,540 trading days from January 3, 2000 to March 31, 2014). Since these estimates of integrated variance are for the whole trading day, we expect estimates of the smoothness of the volatility process to be biased upwards, integration being a regularizing operation. We compute the extent of this bias by simulation in Section 3.4.

In the following, we retain the notation m(q,∆) with the understanding that we are only proxying the (true) spot volatility as explained above. We now proceed to estimate the smoothness parameter sq for each q by computing the m(q,∆) for diﬀerent values of ∆ and regressing log m(q,∆) against log ∆. Note that for a given ∆, several m(q,∆) can be computed depending on the starting point. Our ﬁnal measure of m(q,∆) is the average of these values.

#### 2.2 DAX and Bund futures contracts

DAX and Bund futures are amongst the most liquid assets in the world and moreover, the model with uncertainty zones used to estimate volatility is known to apply well to them, see [19]. So we can be conﬁdent in the reliability of our volatility proxy. Nevertheless, as an extra check, we will conﬁrm the quality of our volatility proxy by Monte Carlo simulation in Section 3.4.

Plots of log m(q,∆) vs log ∆ for diﬀerent values of q, are displayed for the DAX in Figure 2.1, and for the Bund in Figure 2.2.

6And also the CAC40, Nikkei and FTSE indices in some speciﬁc parts of the paper.

[Figure 3]

- Figure 2.1: log m(q,∆) as a function of log ∆, DAX.

[Figure 4]

- Figure 2.2: log m(q,∆) as a function of log ∆, Bund.

For both DAX and Bund, for a given q, the points essentially lie on a straight line. Under stationarity assumptions, this implies that the log-volatility increments enjoy the following scaling property in expectation:

E[|log(σ∆) − log(σ0)|q] = Kq∆ζq,

where ζq > 0 is the slope of the line associated to q. Moreover, the smoothness parameter sq does not seem to depend on q. Indeed, plotting ζq against

q, we obtain that ζq ∼ H q with H equal to 0.125 for the DAX and to 0.082 for the Bund, see Figure 2.3.

[Figure 5]

[Figure 6]

- Figure 2.3: ζq (blue) and 0.125×q (green), DAX (left); ζq (blue) and 0.082×q (green), Bund (right).

We remark that the graphs for ζq are actually very slightly concave. However, we observe the same small concavity eﬀect when we replace the logvolatility by simulations of a fBM with the same number of points. We conclude that this eﬀect relates to ﬁnite sample size and is thus not signiﬁcant.

#### 2.3 S&P and NASDAQ indices

We report in Figure 2.4 and Figure 2.5 similar results for the S&P and NASDAQ indices. The variance proxies used here are the precomputed 5minute realized variance estimates for the whole trading day made publicly available by the Oxford-Man Institute of Quantitative Finance.

[Figure 7]

Figure 2.4: log m(q,∆) as a function of log ∆, S&P.

[Figure 8]

Figure 2.5: log m(q,∆) as a function of log(∆), NASDAQ.

We observe the same scaling property for the S&P and NASDAQ indices as we observed for DAX and Bund futures and again, the sq do not depend on q. However, the estimated smoothnesses are slightly higher here: H = 0.142 for the S&P and H = 0.139 for the NASDAQ, see Figure 2.6.

[Figure 9]

[Figure 10]

- Figure 2.6: ζq (blue) and 0.142×q (green), S&P (left); ζq (blue) and 0.139×q (green), NASDAQ (right).

Once again, we do expect these smoothness estimates to be biased high because we are using whole-day realized variance estimates, as explained earlier in Section 2. Finally, we remark that as for DAX and Bund futures, the graphs for ζq are slightly concave.

#### 2.4 Other indices

Repeating the analysis of Section 2.3 for each index in the Oxford-Man dataset, we ﬁnd the m(q,∆) present a universal scaling behavior. For each index and for q = 0.5, 1, 1.5, 2, 3, by doing a linear regression of log(m(q,∆)) on log(∆) for ∆ = 1,...,30, we obtain estimates of ζq that we summarize in Table B.1 in the appendix.

#### 2.5 Distribution of the increments of the log-volatility

Having established that all our underlying assets exhibit essentially the same scaling behavior7, we focus in the rest of the paper only on the S&P index, unless speciﬁed otherwise. That the distribution of increments of logvolatility is close to Gaussian is a well-established stylized fact reported for example in the papers [2] and [3] of Andersen et al. Looking now at the histograms of the increments of the log-volatility in Figure 2.7 with the ﬁtted normal density superimposed in red, we see that, for any ∆, the empirical distributions of log-volatility increments are veriﬁed as being close to

7We have also veriﬁed that this scaling relationship holds for Crude Oil and Gold futures with similar smoothness estimates ζq.

Gaussian. More impressive still is that rescaling the 1-day ﬁt of the normal density by ∆H generates (blue dashed) curves that are very close to the red ﬁts of the normal density, consistent with the observed scaling.

[Figure 11]

[Figure 12]

(a) ∆ = 1 day (b) ∆ = 5 days

[Figure 13]

[Figure 14]

(c) ∆ = 25 days (d) ∆ = 125 days

- Figure 2.7: Histograms for various lags ∆ of the (overlapping) increments

log σt+∆ − log σt of the S&P log-volatility; normal ﬁts in red; normal ﬁt for ∆ = 1 day rescaled by ∆H in blue.

The slight deviations from the Normal distribution observed in Figure 2.7 are again consistent with the computation of the empirical distribution of the increments of a fractional Brownian motion on a similar number of points.

#### 2.6 Does H vary over time?

In order to check whether our estimations of H depends on the time interval, we split the Oxford-Man realized variance dataset into two halves and reestimate H for each half separately. The results are presented in Table B.2 in the appendix. We note that although the estimated H all lie between 0.06 and 0.20, they seem to be higher in the second period which includes

the ﬁnancial crisis.

### 3 A simple model compatible with the empirical smoothness of the volatility

In this section, we specify the Rough FSV model and demonstrate that it reproduces the empirical facts presented in Section 2.

#### 3.1 Speciﬁcation of the RFSV model

In the previous section, we showed that, empirically, the increments of the log-volatility of various assets enjoy a scaling property with constant smoothness parameter and that their distribution is close to Gaussian. This naturally suggests the simple model:

log σt+∆ − log σt = ν WtH+∆ − WtH , (3.1)

where WH is a fractional Brownian motion with Hurst parameter equal to the measured smoothness of the volatility and ν is a positive constant. We may of course write (3.1) under the form

σt = σ exp ν WtH , (3.2) where σ is another positive constant.

However this model is not stationary, stationarity being desirable both for mathematical tractability and also to ensure reasonableness of the model

- at very large times. This leads us to impose stationarity by modeling the log-volatility as a fractional Ornstein-Uhlenbeck process (fOU process for short) with a very long reversion time scale.

A stationary fOU process (Xt) is deﬁned as the stationary solution of the stochastic diﬀerential equation

dXt = ν dWtH − α (Xt − m)dt,

where m ∈ R and ν and α are positive parameters, see [12]. As for usual Ornstein-Uhlenbeck processes, there is an explicit form for the solution which is given by

t

e−α(t−s)dWtH + m. (3.3)

Xt = ν

−∞

Here the stochastic integral with respect to fBM is simply a pathwise RiemannStieltjes integral, see again [12].

We thus arrive at the ﬁnal speciﬁcation of our Rough Fractional Stochastic Volatility (RFSV) model for the volatility on the time interval of interest [0,T]:

σt = exp{Xt}, t ∈ [0,T], (3.4)

where (Xt) satisﬁes Equation (3.3) for some ν > 0, α > 0, m ∈ R and H < 1/2 the measured smoothness of the volatility. Such a model is indeed stationary. However, if α 1/T, the log-volatility behaves locally (at time scales smaller than T) as a fBM. This observation is formalized in Proposition 3.1 below.

Proposition 3.1. Let WH be a fBM and Xα deﬁned by (3.3) for a given α > 0. As α tends to zero,

|Xtα − X0α − νWtH| → 0.

E sup

t∈[0,T]

- The proof is given in Appendix A.1.

Proposition 3.1 implies that in the RFSV model, if α 1/T, and we conﬁne ourselves to the interval [0,T] of interest, we can proceed as if the the log-volatility process were a fBM. Indeed, simply setting α = 0 in (3.3) gives (at least formally) Xt − Xs = ν(WtH − WsH) and we immediately recover our simple non-stationary fBM model (3.1).

The following corollary implies that the (exact) scaling property of the fBM is approximately reproduced by the fOU process when α is small.

- Corollary 3.1. Let q > 0, t > 0, ∆ > 0. As α tends to zero, we have

E[|Xtα+∆ − Xtα|q] → νq Kq ∆qH.

- The proof is given in Appendix A.2.

##### RFSV versus FSV

We recognize our RFSV model (3.4) as a particular case of the classical FSV model of Comte and Renault [16]. The key diﬀerence is that here we take H < 1/2 and α 1/T, whereas to accommodate the assumption of long memory, Comte and Renault have to choose H > 1/2. The analysis of Fukasawa referred to earlier in Section 1.3 implies in particular that if H > 1/2, the volatility skew function ψ(τ) is increasing in time to expiration τ (at least for small τ), which is obviously completely inconsistent with the approximately 1/√τ skew term structure that is observed. To generate a decreasing term structure of volatility skew for longer expirations, Comte and Renault are then forced to choose α 1/T. Consequently, for very short expirations (τ 1/α), models of the Comte and Renault type with

H > 1/2 still generate a term structure of volatility skew that is inconsistent with the observed one, as explained for example in Section 4 of [15].

In contrast, the choice H < 1/2 enables us to reproduce both the observed smoothness of the volatility process and generate a term structure of volatility skew in agreement with the observed one. The choice H < 1/2 is also consistent with what is improperly called mean reversion by practitioners, which is the fact that if volatility is unusually high, it tends to decline and if it is unusually low, it tends to increase. Finally, taking α very small implies that the dynamics of our process is close to that of a fBM, see Proposition

- 3.1. This last point is particularly important. Indeed, recall that at the time scales we are interested in, the important feature we have in mind is really this fBM like-behavior of the log-volatility.

We could no doubt have considered other stationary models satisfying Proposition 3.1 and Corollary 3.1, where log-volatility behaves as a fBM at reasonable time scales; the choice of the fOU process is probably the simplest way to accommodate this local behavior together with the stationarity property.

#### 3.2 RFSV model autocovariance functions

From Proposition 3.1 and Corollary 3.1, we easily deduce the following corollary, where o(1) tends to zero as α tends to zero.

- Corollary 3.2. Let q > 0, t > 0, ∆ > 0. As α tends to zero,

Cov[Xtα,Xtα+∆] = Var[Xtα] −

- 1

- 2

ν2 ∆2H + o(1).

Consequently, in the RFSV model, for ﬁxed t, the covariance between Xt and Xt+∆ is linear with respect to ∆2H. This result is very well satisﬁed empirically. For example, in Figure 3.1, we see that for the S&P, the empirical autocovariance function of the log-volatility is indeed linear with respect to ∆2H. Note in passing that at the time scales we consider, the term Var[Xtα] is higher than 21ν2 ∆2H in the expression for Cov[Xtα,Xtα+∆].

[Figure 15]

- Figure 3.1: Autocovariance of the log-volatility as a function of ∆2H for H = 0.14, S&P.

Thanks to [12], we even have an exact formula for the autocovariance function of the log-volatility in the RFSV model:

Cov[log σt,log σt+∆] =

H (2H − 1)ν2 2α2H

e−α∆ Γ(2H − 1)

∞

α ∆

e−u

eu u2−2H du + eα∆

+ e−α∆

u2−2H du(3.5) , and

0

α ∆

H (2H − 1)ν2 α2H

Γ(2H − 1), where Γ denotes the Gamma function.

Var[log σt] =

Having computed the autocovariance function of the log-volatility, we now turn our attention to the volatility itself. We have

E[σt+∆σt] = E[eXtα+Xtα+∆],

with Xα deﬁned by Equation (3.3). Since Xα is a Gaussian process, we deduce that

E[σt+∆σt] = eE[Xtα]+E[Xtα+∆]+Var[Xtα]/2+Var[Xtα+∆]/2+Cov[Xtα,Xtα+∆].

Applying Corollary 3.2, we obtain that when α is small, E[σt+∆σt] is approximately equal to

2H

e2E[Xtα]+2Var[Xtα]e−ν2∆

2 . (3.6)

It follows that in the RFSV model, log(E[σt+∆σt]) is also linear in ∆2H. This property is again very well satisﬁed on data, as shown by Figure 3.2, where we plot the logarithm of the empirical counterpart of E[σt+∆σt] against ∆2H, for the S&P with H = 0.14.

[Figure 16]

- Figure 3.2: Empirical counterpart of log(E[σt+∆σt]) as a function of ∆2H, S&P.

We note that putting ∆2H on the x-axis of Figure 3.2 is really crucial in order to retrieve linearity. In particular, a corollary of (3.6) is that the autocovariance function of the volatility does not decay as a power law as widely believed; see Figure 3.3 where we show that a log-log plot of the autocovariance function does not yield a straight line.

[Figure 17]

- Figure 3.3: Empirical counterpart of log(Cov[σt+∆,σt]) as a function of log(∆), S&P.

#### 3.3 RFSV versus FSV again

To further demonstrate the incompatibility of the classical long memory FSV model with volatility data, consider the quantity m(2,∆). Recall that in the data (see Section 2) we observe the linear relationship log m(2,∆) ≈ ζ2 log ∆ + k for some constant k. Also, in both FSV and RFSV, we can consider

m(2,∆) = E (log σt+∆ − log σt)2

= 2 (Var[log σt] − Cov[log σt,log σt+∆]). Therefore, using Equation (3.5), we have a closed form formula for m(2,∆).

In Figure 3.4, we plot m(2,∆) with the parameters H = 0.53, corresponding to the FSV model parameter estimate of Chronopoulou and Viens in [14], and α = 0.5 to ensure some visible decay of the volatility skew. The slope of m(2,∆) in the FSV model for small lags is driven by the value of H; the lag at which m(2,∆) begins to ﬂatten and stationarity kicks in corresponds to a time scale of order 1/α. It is clear from the picture that to ﬁt the data, we must have α 1/T and the value of H must be set by the initial slope of the regression line, which as reported earlier in Section 2 is ζ2 = 2×0.14.

[Figure 18]

- Figure 3.4: Long memory models such as the FSV model of Comte and Renault are not compatible with S&P volatility data. Black points are empirical estimates of m(2,∆); the blue line is the FSV model with α = 0.5 and H = 0.53; the orange line is the RFSV model with α = 0 and H = 0.14.

#### 3.4 Simulation-based analysis of the RFSV model

Our goal in this section is to show that in terms of smoothness measures, one obtains on simulated data from the RFSV model the same behaviors as those observed on empirical data. In particular, we would like to be able to quantify the positive bias associated with estimating H from whole-day realized variance data as in Section 2.3 relative to using data from a one-hour window as in Section 2.2.

We simulate the RFSV model for 2,000 days (chosen to be between the lengths of our two datasets). In order to account for the overnight eﬀect, we simulate the volatility σt8 and eﬃcient price Pt9 over the whole day. The parameters: H = 0.14, ν = 0.3, m = X0 = −5 and α = 5 × 10−4, are chosen to be consistent with our empirical estimates from Section 2. To model microstructure eﬀects such as the discreteness of the price grid, we consider that the observed price process is generated from Pt using the uncertainty zones model of [42] with tick value 5 × 10−4 and parameter η = 0.25.

Exactly as in Section 2, for each of the 2,000 days, we consider two volatility

8To simulate the fBM, we use a spectral method with 40,000,000 points (20,000 points

per day). We then simulate X taking X(n+1)δ − Xnδ = ν(W(Hn+1)δ − WnδH) + αδ(m − Xnδ) (with δ = 1/20000).

√

9P(n+1)δ − Pnδ = Pnδσnδ

δ Un where the Un are iid standard Gaussian variables.

proxies obtained from the observed price and based on:

- • The integrated variance estimator using the model with uncertainty zones over one hour windows, from 10 am to 11 am.
- • The 5 minutes realized variance estimator, over eight hours windows (the trading day).

We now repeat our analysis of Section 2, generating graphs analogous to Figures 2.1, 2.2, 2.4 and 2.5 obtained on empirical data. Figure 3.5 compares smoothness measures obtained using the uncertainty zones estimator on onehour windows with those obtained using the realized variance estimator on 8-hour windows.

[Figure 19]

- Figure 3.5: log(m(q,∆)) as a function of log(∆), simulated data, with realized variance and uncertainty zones estimators.

When the uncertainty zones estimator is applied on a one-hour window (1/24 of a simulated day) as in Section 2.2, we estimate H = 0.16, which is close to the true value H = 0.14 used in the simulation. The results obtained with the realized variance estimator over daily eight-hour windows (1/3 of a simulated day) do exhibit the same scaling properties that we see in the empirical data with a smoothness parameter that does not depend on q. However, the estimated H is biased slightly higher at around 0.18. As discussed in Section 2.1, this extra positive bias is no surprise and is due to the regularizing eﬀect of the integral operator over the longer window. We note also that the estimated values of ν (“volatility of volatility” in some sense) obtained from the intercepts of the regressions, are lower with the longer time windows, again as expected. A detailed computation of the bias in the

estimated H associated with the choice of window length in an analogous but more tractable model is presented in Appendix C.

We end this section by presenting in Figure 3.6 a sample path of the modelgenerated volatility (spot volatility direct from the simulation rather than estimated from the simulated price series) together with a graph of S&P volatility over 3,500 days.

[Figure 20]

Figure 3.6: Volatility of the S&P (above) and of the model (below).

A ﬁrst reaction to Figure 3.6 is that the simulated and actual graphs look very alike. In particular, in both of them, persistent periods of high volatility alternate with low volatility periods. On closer inspection of the empirical volatility series, we observe that the sample path of the volatility on a restricted time window seems to exhibit the same kind of qualitative properties as those of the global sample path (for example periods of high and low activity). This fractal-type behavior of the volatility has been investigated both empirically and theoretically in, for example, [5, 9, 37].

- At the visual level, we observe that this fractal-type behavior is also reproduced in our model, as we now explain. Denote by Lx,H the law of the geometric fractional Brownian motion with Hurst exponent H and volatility x on [0,1], that is (exWtH)t∈[0,1]. Then, when α is very small, the rescaled volatility process on [0,∆]: (σt∆/σ0)t∈[0,1], has approximately the law Lν∆H,H. Now remark that for H small, the function uH increases very slowly. Thus, over a large range of observation scales ∆, the rescaled volatility processes on [0,∆] have approximately the same law. For example, between an observation scale of one day and ﬁve years (1250 open days), the coeﬃcient x characterizing the law of the volatility process is “only” multiplied by 12500.14 = 2.7. It follows that in the RFSV model, the volatility process over one day resembles the volatility process over a decade.

### 4 Spurious long memory of volatility?

We revisit in this section the issue of long memory of volatility through the lens of our model. As mentioned earlier in the introduction, the long memory of volatility is widely accepted as a stylized fact. Speciﬁcally, this means that the autocovariance function Cov[log(σt),log(σt+∆)] (or sometimes Cov[σt,σt+∆]) goes slowly to zero as ∆ → ∞ and often even more precisely, that it behaves as ∆−γ, with γ < 1 as ∆ → ∞.

In previous sections, we showed that both in the data and in our model,

Cov[log(σt),log(σt+∆)] ≈ A − B∆2H and

Cov[σt,σt+∆] ≈ C e−B∆2H − D,

for some constants A, B, C and D. Thus, neither in the model nor in the data does the autocovariance function decay as a power law. And neither the data nor the model exhibits long memory10, see again Figure 3.3.

We now revisit some standard statistical procedures aimed at identifying long memory that have been used in the ﬁnancial econometrics literature. In the sequel, we apply these both to the data and to sample paths of the RFSV model. Such procedures are of course designed to identify long memory under rather strict modeling assumptions; spurious results may obviously then be obtained if the model underlying the estimation procedure

10In fact the notion of empirical long memory does not make much sense outside the power law case. Indeed the empirical values of covariances at very large time scales are never measurable and thus one cannot conclude if the series of covariances converges in general. All that we say here is that the autocovariance of the (log-)volatility does not behave as a power law.

is misspeciﬁed .

With the same model parameters as in Section 3.4, we simulate our model over 3,500 days, which corresponds to the size of our dataset. Consider ﬁrst the procedure in [3], where the authors test for long memory in the volatility by studying the scaling behavior of the quantity

V (t) = Var

t

0

σs2ds

with respect to t. In the model they consider, if V (t) behaves asymptotically as t2−γ with γ < 1, then the autocorrelation function of the log-volatility should behave as t−γ. Figure 4.1 presents the graph of the logarithm of the empirical counterpart of V (t) against the logarithm of t, on the S&P data and within our simulation framework.

[Figure 21]

- Figure 4.1: Empirical counterpart of log(V (t)) as a function of log(t) on S&P (above) and simulation (below).

We note from Figure 4.1 that both our simulated model and market data lead to very similar graphs, close to straight lines with slope 1.86. Accordingly, in the setting of [3], we would deduce power law behavior of the autocorrelation function with exponent 0.14 and therefore long memory. Thus, if the data are generated by a model like the RFSV model, one can easily be wrongly convinced that the volatility time series exhibits long memory.

In [4], the authors deduce long memory in the volatility by showing that the process εt obtained by fractional diﬀerentiation of the log-volatility εt = (1 − L)dlog(σt), with d = 0.4 (which is considered as a reasonable value) and L the lag operator, behaves as a white noise. To check for this, they simply compute the autocorrelation function of εt. We give in Figure 4.2 the autocorrelation functions of the logarithm of σt and εt, again both on the data and on the simulated path.

[Figure 22]

- Figure 4.2: Autocorrelation functions of log(σt) (in blue) and εt (in green) and the Bartlett standard error bands (in red), for S&P data (above) and for simulated data (below).

Once again, the data and the simulation generate very similar plots. We conclude that this procedure for estimating long memory is just as fragile

- as the ﬁrst, and it is easy to wrongly deduce volatility long memory when applying it.

In conclusion, it seems that classical estimation procedures identify spurious long memory of volatility in the RFSV model. Moreover, these procedures estimate the same long memory parameter from data generated from a suitably calibrated RFSV model as they estimate from empirical data. Once again, our conclusion is that although the (log-)volatility may exhibit some form of persistence, it does not present any long memory in the classical power law sense.

### 5 Forecasting using the RFSV model

In this section, we present an application of our model: forecasting the log-volatility and the variance.

#### 5.1 Forecasting log-volatility

The key formula on which our prediction method is based is the following one:

t

WsH (t − s + ∆)(t − s)H+1/2

cos(Hπ) π

E[WtH+∆|Ft] =

∆H+1/2

ds,

−∞

where WH is a fBM with H < 1/2 and Ft the ﬁltration it generates, see Theorem 4.2 of [41]. By construction, over any reasonable time scale of interest, as formalized in Corollary 3.1, we may approximate the fOU volatility process in the RFSV model as log σt2 ≈ 2ν WtH + C for some constants ν and C. Our prediction formula for log-variance then follows:11

t

log σs2 (t − s + ∆)(t − s)H+1/2

cos(Hπ) π

E log σt2+∆|Ft =

∆H+1/2

ds. (5.1)

−∞

This formula, or rather its approximation through a Riemann sum (we assume in this section that the volatilities are perfectly observed, although they are in fact estimated), is used to forecast the log-volatility 1, 5 and 20 days ahead (∆ = 1, 5, 20).

We now compare the predictive power of formula (5.1) with that of AR and HAR forecasts, in the spirit of [18]12. Recall that for a given integer p > 0, the AR(p) and HAR predictors take the following form (where the index i runs over the series of daily volatility estimates):

- • AR(p):

log(σt2+∆) = K0∆ +

p

i=0

Ci∆ log(σt2−i).

- • HAR :

1 5

log(σt2+∆) = K0∆+C0∆ log(σt2)+C5∆

5

1 20

log(σt2−i)+C20∆

i=0

20

log(σt2−i).

i=0

11The constants 2ν and C cancel when deriving the expression. 12 Note that we do not consider GARCH models here since we have access to high frequency volatility estimates and not only to daily returns. Indeed, it is shown in [4] that forecasts based on the time series of realized variance outperform GARCH forecasts based on daily returns.

We estimate AR coeﬃcients using the R stats library13 on a rolling time window of 500 days. In the HAR case, we use standard linear regression to estimate the coeﬃcients as explained in [18]. In the sequel, we consider p = 5 and p = 10 in the AR formula. Indeed, these parameters essentially give the best results for the horizons at which we wish to forecast the volatility (1,

- 5 and 20 days). For each day, we forecast volatility for ﬁve diﬀerent indices14.

We then assess the quality of the various forecasts by computing the ratio P between the mean squared error of our predictor and the (approximate) variance of the log-variance:

2

N−∆ k=500 log(σk2+∆) − log(σk2+∆)

P =

,

N−∆ k=500 log(σk2+∆) − E[log(σt2+∆)] 2

where E[log(σt2+∆)] denotes the empirical mean of the log-variance over the whole time period.

| |AR(5)|AR(10)<br><br>|HAR(3)<br><br>|RFSV|
|---|---|---|---|---|
|SPX2.rv ∆ = 1<br><br>|0.317|0.318<br><br>|0.314<br><br>|0.313|
|SPX2.rv ∆ = 5<br><br>|0.459|0.449|0.437<br><br>|0.426|
|SPX2.rv ∆ = 20|0.764<br><br>|0.694<br><br>|0.656|0.606|
|FTSE2.rv ∆ = 1<br><br>|0.230<br><br>|0.229|0.225|0.223|
|FTSE2.rv ∆ = 5<br><br>|0.357|0.344<br><br>|0.337<br><br>|0.320|
|FTSE2.rv ∆ = 20|0.651|0.571<br><br>|0.541|0.472|
|N2252.rv ∆ = 1<br><br>|0.357|0.358|0.351<br><br>|0.345|
|N2252.rv ∆ = 5|0.553<br><br>|0.533<br><br>|0.513|0.504|
|N2252.rv ∆ = 20<br><br>|0.875<br><br>|0.795|0.746|0.714|
|GDAXI2.rv ∆ = 1<br><br>|0.237<br><br>|0.238|0.234|0.231|
|GDAXI2.rv ∆ = 5|0.372<br><br>|0.362<br><br>|0.350|0.339|
|GDAXI2.rv ∆ = 20|0.661|0.590<br><br>|0.550|0.498|
|FCHI2.rv ∆ = 1|0.244|0.244<br><br>|0.241|0.238|
|FCHI2.rv ∆ = 5<br><br>|0.378|0.373<br><br>|0.366<br><br>|0.350|
|FCHI2.rv ∆ = 20|0.669<br><br>|0.613<br><br>|0.598|0.522|

Table 5.1: Ratio P for the AR, HAR and RFSV predictors.

We note from Table 5.1 that the RFSV forecast consistently outperforms the AR and HAR forecasts, especially at longer horizons. Moreover, our forecasting method is more parsimonious since it only requires the parameter

13More precisely, we use the default Yule-Walker method. 14In addition to S&P and NASDAQ, we also investigate CAC40, FTSE and Nikkei, over the same time period as S&P and NASDAQ. For simplicity, the parameter H used in our predictor is computed only once for each asset, using the whole time period. This yields similar results to using a moving time window adapted in time.

H to forecast the log-variance. Compare this with the AR and HAR methods, for which coeﬃcients depend on the forecast time horizon and must be recomputed if this horizon changes.

Remark that our predictor can be linked to that of [21], where the issue of the prediction of the log-volatility in the multifractal random walk model of [5] is tackled. In this model,

√

t

log(σs2) (t − s + ∆)√t − s

1 π

E[log(σt2+∆)|Ft] =

∆

ds,

−∞

which is the limit of our predictor when H tends to zero.

Note also that our prediction formula may be rewritten as

cos(Hπ) π

E[log(σt2+∆)|Ft] =

log(σt2−∆u) (u + 1)uH+1/2

+∞

du.

0

For a given small ε > 0, let r be the smallest real number such that

+∞

1 (u + 1)uH+1/2

du ≤ ε.

r

Then we have, with an error of order ε,

cos(Hπ) π

E[log(σt2+∆)|Ft] ≈

log(σt2−∆u) (u + 1)uH+1/2

r

du.

0

Consequently, the volatility process needs to be considered (roughly) down to time t − ∆r if one wants to forecast up to time ∆ in the future. The relevant regression window is thus linear in the forecasting horizon. For example, for r = 1, ε = 0.35 which is not so unreasonable. In this case, as is well-known to practitioners, to predict volatility one week ahead, one should essentially look at the volatility over the last week. If trying to predict the volatility one month ahead, one should look at the volatility over the last month.

#### 5.2 Variance prediction

Recall that log σt2 ≈ 2ν WtH + C for some constant C. In [41], it is shown that WtH+∆ is conditionally Gaussian with conditional variance

Var[WtH+∆|Ft] = c∆2H with

Γ(3/2 − H) Γ(H + 1/2)Γ(2 − 2H)

c =

.

Thus, we obtain the following natural form for the RFSV predictor of the variance:

σt2+∆ = exp log σt2+∆ + 2cν2∆2H

where log(σt2+∆) is the estimator from Section 5.1 and ν2 is estimated as the exponential of the intercept in the linear regression of log(m(2,∆)) on

log(∆).

As in the previous paragraph, we compare in Table 5.2 the performance of the RFSV forecast with those of AR and HAR forecasts (constructed on variance rather than log-variance this time).

| |AR(5)<br><br>|AR(10)|HAR(3)<br><br>|RFSV|
|---|---|---|---|---|
|SPX2.rv ∆ = 1<br><br>|0.520|0.566<br><br>|0.489|0.475|
|SPX2.rv ∆ = 5|0.750<br><br>|0.745|0.723|0.672|
|SPX2.rv ∆ = 20|1.070<br><br>|1.010|1.036|0.903|
|FTSE2.rv ∆ = 1|0.612<br><br>|0.621|0.582<br><br>|0.567|
|FTSE2.rv ∆ = 5|0.797<br><br>|0.770|0.756<br><br>|0.707|
|FTSE2.rv ∆ = 20|1.046<br><br>|0.984|0.935<br><br>|0.874|
|N2252.rv ∆ = 1|0.554<br><br>|0.579<br><br>|0.504|0.505|
|N2252.rv ∆ = 5|0.857|0.807<br><br>|0.761|0.729|
|N2252.rv ∆ = 20|1.097<br><br>|1.046|1.011|0.964|
|GDAXI2.rv ∆ = 1|0.439<br><br>|0.448|0.399<br><br>|0.386|
|GDAXI2.rv ∆ = 5<br><br>|0.675|0.650<br><br>|0.616|0.566|
|GDAXI2.rv ∆ = 20<br><br>|0.931<br><br>|0.850|0.816|0.746|
|FCHI2.rv ∆ = 1<br><br>|0.533<br><br>|0.542|0.470|0.465|
|FCHI2.rv ∆ = 5|0.705<br><br>|0.707<br><br>|0.691|0.631|
|FCHI2.rv ∆ = 20|0.982<br><br>|0.952|0.912<br><br>|0.828|

Table 5.2: Ratio P for the AR, HAR and RFSV predictors.

We ﬁnd again that the RFSV forecast typically outperforms HAR and AR, although it is worth noting that the HAR forecast is already visibly superior to the AR forecast.

### 6 The microstructural foundations of the irregularity of the volatility

We gather in this section some ideas which may help to understand why the observed volatility appears so irregular. The starting point is the analysis of the order ﬂow through Hawkes processes. These processes are extensions of Poisson processes where the intensity at a given time depends on the

location of the past jumps. More precisely, let us consider a time period starting at 0 and denote by Nt the number of transactions between 0 and t. Assuming the point process Nt follows a Hawkes process means its intensity

- at time t, λt, takes the form:

φ(t − Ji),

λt = µ +

0<Ji<t

where the Ji are the past jump times, µ is a positive constant and φ is a non negative deterministic function called kernel.

When trying to calibrate such models on high frequency data, two main phenomena almost systematically occur:

- • The L1 norm of φ is close to one, see [23, 24, 30, 35].
- • The function φ has a power law tail, see [6, 30].

The ﬁrst of these two facts means the degree of endogeneity of the market is very high, that is one given order endogenously generates many other orders, see [23, 24, 30]. This recent feature of ﬁnancial markets is obviously related to electronic high frequency trading, where market participants automatically react to other participants orders through their algorithms. The second observation tells us that generally, a given order inﬂuences other orders over a long time period. This is likely due to the splitting of large orders. Indeed, many orders are actually part of a metaorder whose full execution can take a large amount of time.

We believe these two phenomena together lead to a superposition eﬀect inducing this irregular volatility. Indeed, it is explained in [33, 34] that the macroscopic scaling limit of Hawkes processes with power law tail and kernel with L1 norm close to one can be seen as an integrated fractional process, with Hurst parameter H smaller than 1/2. This signiﬁes that at large sampling scales, the dynamics of the cumulated order ﬂow is well approximated by an integrated fractional process, with H < 1/2. Then, it is clearly established that there is a linear relation between cumulated order ﬂow and integrated variance. Thus we retrieve here that because of this superposition eﬀect, the volatility should behave as a fractional process with H < 1/2.

### 7 Conclusion

Using daily realized variance estimates as proxies for daily spot (squared) volatilities, we uncovered two startlingly simple regularities in the resulting

time series. First we found that the distributions of increments of logvolatility are approximately Gaussian, consistent with many prior studies. Secondly, we established the monofractal scaling relationship

E[|log(σ∆) − log(σ0)|q] = Kq νq ∆qH, (7.1)

where H can be seen as a measure of smoothness characteristic of the underlying volatility process; typically, 0.06 < H < 0.2. The simple scaling relationship (7.1) naturally suggests that log-volatility may be modeled using fractional Brownian motion.

The resulting Rough Fractional Stochastic Volatility (RFSV) model turns out to be formally almost identical to the FSV model of Comte and Renault [16], with one major diﬀerence: In the FSV model, H > 1/2 to ensure long memory whereas in the RFSV model H < 1/2, typically, H ≈ 0.1. Moreover, in the FSV model, the mean reversion coeﬃcient α has to be large compared to 1/T to ensure a decaying volatility skew; in the RFSV model, the volatility skew decays naturally just like the observed volatility skew, α 1/T and indeed for time scales of practical interest, we may proceed

- as if α were exactly zero.

We further showed that applying standard statistical estimators to volatility time series simulated with the RFSV model would lead us to erroneously deduce the presence of long memory, with parameters similar to those found in prior studies. Despite that volatility in the RFSV model (or in the data) is not long memory, we can therefore explain why long memory of volatility is widely accepted as a stylized fact.

As an application of the RFSV model, we showed how to forecast volatility

- at various times cales, at least as well as Fulvio Corsi’s impressive HAR estimator, but with only one parameter – H!

Finally, we explained how the RFSV model could emerge as the scaling limit of a Hawkes process description of order ﬂow.

In future work, we will explore the implications of the RFSV model (written under the physical measure P), for option pricing (under the pricing measure Q). In particular, following Mandelbrot and Van Ness, the fBM that appears in the deﬁnition (3.4) of the RFSV model may be represented as a fractional integral of a standard Brownian motion as follows [36]:

t

0

dWs (t − s)γ

1 (t − s)γ −

1 (−s)γ

WtH =

+

dWs, (7.2)

−∞

0

with γ = 21 − H. The observed anticorrelation between price moves and volatility moves may then be modeled naturally by anticorrelating the Brow-

nian motion W that drives the volatility process with the Brownian motion driving the price process. As already shown by Fukasawa [25], such a model with a small H reproduces the observed decay of at-the-money volatility skew with respect to time to expiry, asymptotically for short times. We will show that an appropriate extension of Fukasawa’s model, consistent with the RFSV model, ﬁts the entire implied volatility surface remarkably well, not just for short expirations. Moreover, despite that it would seem from (7.2) that knowledge of the entire path {Ws : s < t} of the Brownian motion would be required, it turns out that the statistics of this path necessary for option pricing are traded and thus easily observed.

### A Proofs

- A.1 Proof of Proposition 3.1 Starting from Equation (3.3) and applying integration by parts, we get

Xtα = νWtH −

t

−∞

ναe−α(t−s)WsHds + m.

Therefore,

(Xtα−X0α)−νWtH = −

t

0

ναe−α(t−s)WsHds−

0

−∞

να(e−α(t−s)−eαs)WsHds.

Consequently,

sup

t∈[0,T]

|(Xtα − X0α) − νWtH| ≤ ναTWˆTH +

0

−∞

να(eαs − e−α(T−s))WˆsHds,

where WˆtH = sups∈[0,t] |WsH|. Using the maximum inequality of [40], we get

E sup

t∈[0,T]

|(Xtα − X0α) − νWtH| ≤ c ναTTH +

0

−∞

να(Tαeαs)|s|Hds ,

with c some constant. The term on the right hand side is easily seen to go to zero as α tends to zero.

- A.2 Proof of Corollary 3.1 We ﬁrst recall Equation (2.2) in [12] which writes:

Cov[Xtα+∆,Xtα] = K

ei∆x |x|1−2H α2 + x2

dx,

R

with K = ν2Γ(2H + 1)sin(πH)/(2π)15. Now remark that

E[(Xtα+∆ − Xtα)2] = 2Var[Xtα] − 2Cov[Xtα+∆,Xtα]. Therefore,

E[(Xtα+∆ − Xtα)2] = 2K

(1 − ei∆x)|x|1−2H α2 + x2

dx.

R

This implies that for ﬁxed ∆, E[|Xtα+∆ − Xtα|2] is uniformly bounded by

(1 − ei∆x)|x|1−2H x2

dx.

2K

R

Moreover, Xtα+∆ − Xtα is a Gaussian random variable and thus for every q, its (q + 1)th moment is uniformly bounded (in α) so that the family

|Xtα+∆ − Xtα|q is uniformly integrable. Therefore, since by Proposition 3.1, |Xtα+∆ − Xtα|q → νq|WtH+∆ − WtH|q, in law, we get the convergence of the sequence of expectations.

15This covariance is real because it is the Fourier transform of an even function.

### B Estimations of H

#### B.1 On diﬀerent indices

|Index|ζ0.5/0.5|ζ1<br><br>|ζ1.5/1.5|ζ2/2<br><br>|ζ3/3|
|---|---|---|---|---|---|
|SPX2.rv|0.128|0.126<br><br>|0.125|0.124|0.124|
|FTSE2.rv|0.132<br><br>|0.132|0.132|0.131<br><br>|0.127|
|N2252.rv<br><br>|0.131|0.131<br><br>|0.132<br><br>|0.132|0.133|
|GDAXI2.rv|0.141<br><br>|0.139|0.138<br><br>|0.136<br><br>|0.132|
|RUT2.rv|0.117<br><br>|0.115<br><br>|0.113<br><br>|0.111<br><br>|0.108|
|AORD2.rv<br><br>|0.072<br><br>|0.073|0.074<br><br>|0.075|0.077|
|DJI2.rv<br><br>|0.117|0.116<br><br>|0.115<br><br>|0.114|0.113|
|IXIC2.rv|0.131<br><br>|0.133<br><br>|0.134|0.135<br><br>|0.137|
|FCHI2.rv<br><br>|0.143<br><br>|0.143|0.142|0.141<br><br>|0.138|
|HSI2.rv|0.079|0.079<br><br>|0.079<br><br>|0.080|0.082|
|KS11.rv<br><br>|0.133|0.133<br><br>|0.134<br><br>|0.134|0.132|
|AEX.rv|0.145<br><br>|0.147<br><br>|0.149|0.149<br><br>|0.149|
|SSMI.rv|0.149<br><br>|0.153<br><br>|0.156|0.158<br><br>|0.158|
|IBEX2.rv<br><br>|0.138|0.138<br><br>|0.137<br><br>|0.136|0.133|
|NSEI.rv<br><br>|0.119|0.117|0.114<br><br>|0.111<br><br>|0.102|
|MXX.rv<br><br>|0.077|0.077<br><br>|0.076<br><br>|0.075|0.071|
|BVSP.rv<br><br>|0.118<br><br>|0.118|0.119|0.120<br><br>|0.120|
|GSPTSE.rv<br><br>|0.106|0.104|0.103|0.102<br><br>|0.101|
|STOXX50E.rv<br><br>|0.139|0.135|0.130<br><br>|0.123<br><br>|0.101|
|FTSTI.rv|0.111<br><br>|0.112<br><br>|0.113|0.113|0.112|
|FTSEMIB.rv|0.130|0.132<br><br>|0.133|0.134<br><br>|0.134|

Table B.1: Estimates of ζq for all indices in the Oxford-Man dataset.

#### B.2 On diﬀerent time intervals16

|Index|H (ﬁrst half)|H (second half)|
|---|---|---|
|SPX2.rk|0.115<br><br>|0.158|
|FTSE2.rk|0.140<br><br>|0.156|
|N2252.rk|0.083<br><br>|0.134|
|GDAXI2.rk<br><br>|0.154|0.168|
|RUT2.rk|0.098<br><br>|0.149|
|AORD2.rk|0.059<br><br>|0.114|
|DJI2.rk<br><br>|0.123|0.151|
|IXIC2.rk<br><br>|0.094<br><br>|0.156|
|FCHI2.rk|0.140<br><br>|0.146|
|HSI2.rk|0.072<br><br>|0.129|
|KS11.rk<br><br>|0.109|0.147|
|AEX.rk<br><br>|0.168|0.151|
|SSMI.rk|0.206<br><br>|0.183|
|IBEX2.rk<br><br>|0.122|0.149|
|NSEI.rk<br><br>|0.112|0.124|
|MXX.rk<br><br>|0.068|0.118|
|BVSP.rk<br><br>|0.074|0.134|
|GSPTSE.rk<br><br>|0.075|0.147|
|STOXX50E.rk<br><br>|0.138|0.132|
|FTSTI.rk|0.080<br><br>|0.171|
|FTSEMIB.rk<br><br>|0.133|0.140|

Table B.2: Estimates of H over two diﬀerent time intervals for all indices in the Oxford-Man dataset

- C The eﬀect of smoothing Although we are really interested in the model

log σt+∆ − log σt = ν WtH+∆ − WtH , consider the more tractable (fractional Stein and Stein or fSS) model: vt+∆ − vt = α WtH+∆ − WtH ,

where vt = σ2. We cannot observe vt but suppose we can proxy it by the average

δ

1 δ

vˆtδ =

vu du.

0

16Note that we used realized kernel rather than realized variance estimates to generate

- Table B.2. Results obtained using diﬀerent variance estimators are almost indistinguishable.

We would, for example, like to estimate m(2,∆) = E (vt+∆ − vt)2 . However, we need to proxy spot variance with integrated variance so instead we have the estimate

mδ(2,∆) = E (ˆvtδ+∆ − vˆtδ)2

δ

1 δ2

E

(vu+∆ − vu)du

=

0

2

=

=

α2 δ2

δ

δ

0

δ

0

0

δ

E (WuH+∆ − WuH)(WsH+∆ − WsH) duds

0

|u − s + ∆|2H − |u − s|2H duds, (C.1)

where the last step uses that:

- 1

- 2

E WuH WsH =

u2H + s2H − |u − s|2H , and the symmetry of the integral.

We assume that the length δ of the smoothing window is less than one day so ∆ > δ. Then easy computations give

and

=

δ

δ

|u − s + ∆|2H duds

0

0

1 2H + 1

1 2H + 2

(∆ + δ)2H+2 − 2∆2H+2 + (∆ − δ)2H+2

δ

0

δ

|u − s|2H duds =

0

1 2H + 2

2 2H + 1

δ2H+2.

Substituting back into (C.1) gives

1 2H + 1

1 2H + 2

1 θ2

mδ(2,∆) = α2 ∆2H

=: α2 ∆2H f(θ). where θ = δ/∆.

(1 + θ)2H+2 − 2 − 2θ2H+2 + (1 − θ)2H+2

- Figure C.1 shows the eﬀect of smoothing on the estimated variance in the fSS model. Keeping δ ﬁxed, as ∆ increases, f(θ) = f(δ/∆) increases towards one. Thus, in a linear regression of log mδ(2,∆) against log ∆, we will obtain a higher eﬀective H (from the higher slope) and a lower eﬀective (“volatility of volatility”) α, exactly as we observed in the RSFV model simulations in Section 3.4.

[Figure 23]

Figure C.1: f(θ) vs θ = δ/∆ with H = 0.14.

##### Numerical example

In the simulation of the RSFV model in Section 3.4, we have H = 0.14, δ1 = 1/24 for the UZ estimate and δ2 = 1/3 for the RV estimate. We now reproduce a fSS analogue of the RFSV simulation plots of m(2,∆) in Figure 3.5. Speciﬁcally, for each ∆ ∈ {1,2,...,100}, with α = 0.3 and δ = δ1 or δ = δ2, we compute the mδ(2,∆) and regress log mδ(2,∆) against log ∆. The regressions are shown in Figure C.2 and results tabulated in Table C.1.

In Figure C.2 and Table C.1, we observe similar qualitative and quantitative biases from our fSS model simulation as we observe in our simulation of the RSFV model with equivalent parameters in Section 3.4.

Estimate Est. α Est. H Exact (δ = 0) 0.300 0.140 UZ (δ = 1/24) 0.263 0.161 RV (δ = 1/3) 0.230 0.184

- Table C.1: Estimated model parameters from the regressions shown in Figure C.2.

[Figure 24]

- Figure C.2: Analogue of Figure 3.5 in the fSS model: The blue solid line is the true m(2,∆); the red long-dashed line is the UZ estimate mδ1(2,∆); the orange short-dashed line is the RV estimate mδ2(2,∆).

### References

- [1] T. G. Andersen and T. Bollerslev. Intraday periodicity and volatility persistence in ﬁnancial markets. Journal of Empirical Finance, 4(2):115–158, 1997.
- [2] T. G. Andersen, T. Bollerslev, F. X. Diebold, and H. Ebens. The distribution of realized stock return volatility. Journal of Financial Economics, 61(1):43–76, 2001.
- [3] T. G. Andersen, T. Bollerslev, F. X. Diebold, and P. Labys. The distribution of realized exchange rate volatility. Journal of the American Statistical Association, 96(453):42–55, 2001.
- [4] T. G. Andersen, T. Bollerslev, F. X. Diebold, and P. Labys. Modeling and forecasting realized volatility. Econometrica, 71(2):579–625, 2003.
- [5] E. Bacry and J. F. Muzy. Log-inﬁnitely divisible multifractal processes. Communications in Mathematical Physics, 236(3):449–475, 2003.

- [6] E. Bacry and J.-F. Muzy. Hawkes model for price and trades highfrequency dynamics. Quantitative Finance, 14(7):1147–1166, 2014.
- [7] S. R. Bentes and M. M. Cruz. Is stock market volatility persistent? A fractionally integrated approach. 2011.
- [8] J. Beran. Statistics for long-memory processes, volume 61. CRC Press, 1994.
- [9] J.-P. Bouchaud and M. Potters. Theory of ﬁnancial risk and derivative pricing: From statistical physics to risk management. Cambridge University Press, 2003.
- [10] P. Carr and L. Wu. What type of process underlies options? A simple robust test. Journal of Finance, 58(6):2581–2610, 2003.
- [11] Z. Chen, R. T. Daigler, and A. M. Parhizgari. Persistence of volatility in futures markets. Journal of Futures Markets, 26(6):571–594, 2006.
- [12] P. Cheridito, H. Kawaguchi, and M. Maejima. Fractional OrnsteinUhlenbeck processes. Electron. J. Probab, 8(3):14, 2003.
- [13] A. Chronopoulou. Parameter estimation and calibration for longmemory stochastic volatility models. In F. G. Viens, M. C. Mariani, and I. Florescu, editors, Handbook of Modeling High-Frequency Data in Finance, pages 219–231. John Wiley & Sons, 2011.
- [14] A. Chronopoulou and F. G. Viens. Estimation and pricing under longmemory stochastic volatility. Annals of Finance, 8(2-3):379–403, 2012.
- [15] F. Comte, L. Coutin, and E. Renault. Aﬃne fractional stochastic volatility models. Annals of Finance, 8(2-3):337–378, 2012.
- [16] F. Comte and E. Renault. Long memory in continuous-time stochastic volatility models. Mathematical Finance, 8(4):291–323, 1998.
- [17] R. Cont. Volatility clustering in ﬁnancial markets: Empirical facts and agent-based models. In G. Teyssi`ere and A. P. Kirman, editors, Long Memory in Economics, pages 289–309. Springer Berlin Heidelberg, 2007.
- [18] F. Corsi. A simple approximate long-memory model of realized volatility. Journal of Financial Econometrics, 7(2):174–196, 2009.
- [19] K. Dayri and M. Rosenbaum. Large tick assets: Implicit spread and optimal tick size. Working paper, 2013.
- [20] Z. Ding, C. W. Granger, and R. F. Engle. A long memory property of stock market returns and a new model. Journal of Empirical Finance, 1(1):83–106, 1993.

- [21] J. Duchon, R. Robert, and V. Vargas. Forecasting volatility with the multifractal random walk model. Mathematical Finance, 22(1):83–108, 2012.
- [22] B. Dupire. Pricing with a smile. Risk Magazine, 7(1):18–20, 1994.
- [23] V. Filimonov and D. Sornette. Quantifying reﬂexivity in ﬁnancial markets: Toward a prediction of ﬂash crashes. Physical Review E, 85(5):056108, 2012.
- [24] V. Filimonov and D. Sornette. Apparent criticality and calibration issues in the Hawkes self-excited point process model: Application to high-frequency ﬁnancial data. arXiv preprint arXiv:1308.6756, 2013.
- [25] M. Fukasawa. Asymptotic analysis for stochastic volatility: Martingale expansion. Finance and Stochastics, 15(4):635–654, 2011.
- [26] J. Gatheral. The volatility surface: A practitioner’s guide, volume 357. John Wiley & Sons, 2006.
- [27] J. Gatheral and A. Jacquier. Arbitrage-free SVI volatility surfaces. Quantitative Finance, 14(1):59–71, 2014.
- [28] J. Gatheral and R. C. Oomen. Zero-intelligence realized variance estimation. Finance and Stochastics, 14(2):249–283, 2010.
- [29] P. S. Hagan, D. Kumar, A. S. Lesniewski, and D. E. Woodward. Managing smile risk. Wilmott Magazine, pages 84–108, 2002.
- [30] S. J. Hardiman, N. Bercot, and J.-P. Bouchaud. Critical reﬂexivity in ﬁnancial markets: A Hawkes process analysis. arXiv preprint arXiv:1302.1405, 2013.
- [31] S. L. Heston. A closed-form solution for options with stochastic volatility with applications to bond and currency options. Review of Financial Studies, 6(2):327–343, 1993.
- [32] J. Hull and A. White. One-factor interest-rate models and the valuation of interest-rate derivative securities. Journal of Financial and Quantitative Analysis, 28(02):235–254, 1993.
- [33] T. Jaisson and M. Rosenbaum. Limit theorems for nearly unstable Hawkes processes. The Annals of Applied Probability, to appear, 2013.
- [34] T. Jaisson and M. Rosenbaum. Fractional diﬀusions as scaling limits of nearly unstable heavy-tailed Hawkes processes. Working paper, 2014.
- [35] M. Lallouache and D. Challet. Statistically signiﬁcant ﬁts of Hawkes processes to ﬁnancial data. Available at SSRN 2450101, 2014.

- [36] B. B. Mandelbrot and J. W. Van Ness. Fractional Brownian motions, fractional noises and applications. SIAM review, 10(4):422–437, 1968.
- [37] R. N. Mantegna and H. E. Stanley. Introduction to econophysics: Correlations and complexity in ﬁnance. Cambridge University Press, 2000.
- [38] T. Mikosch and C. St˘ric˘a. Is it really long memory we see in ﬁnancial returns. In P. Embrechts, editor, Extremes and integrated risk management, pages 149–168. Risk Books, 2000.
- [39] M. Musiela and M. Rutkowski. Martingale methods in ﬁnancial modelling, volume 36. Springer, 2006.
- [40] A. Novikov and E. Valkeila. On some maximal inequalities for fractional Brownian motions. Statistics & Probability Letters, 44(1):47–54, 1999.
- [41] C. J. Nuzman and V. H. Poor. Linear estimation of self-similar processes via Lamperti’s transformation. Journal of Applied Probability, 37(2):429–452, 2000.
- [42] C. Y. Robert and M. Rosenbaum. A new approach for the dynamics of ultra-high-frequency data: The model with uncertainty zones. Journal of Financial Econometrics, 9(2):344–366, 2011.
- [43] C. Y. Robert and M. Rosenbaum. Volatility and covariation estimation when microstructure noise and trading times are endogenous. Mathematical Finance, 22(1):133–164, 2012.
- [44] M. Rosenbaum. Estimation of the volatility persistence in a discretely observed diﬀusion model. Stochastic Processes and their Applications, 118(8):1434–1462, 2008.
- [45] M. Rosenbaum. First order p-variations and Besov spaces. Statistics & Probability Letters, 79(1):55–62, 2009.
- [46] M. Rosenbaum. A new microstructure noise index. Quantitative Finance, 11(6):883–899, 2011.

