# arXiv:1802.03042v1[q-fin.CP]8Feb2018

1

## DEEP HEDGING

HANS BUEHLER, LUKAS GONON, JOSEF TEICHMANN, AND BEN WOOD

Abstract. We present a framework for hedging a portfolio of derivatives in the presence of market frictions such as transaction costs, market impact, liquidity constraints or risk limits using modern deep reinforcement machine learning methods.

We discuss how standard reinforcement learning methods can be applied to non-linear reward structures, i.e. in our case convex risk measures. As a general contribution to the use of deep learning for stochastic processes, we also show in section 4 that the set of constrained trading strategies used by our algorithm is large enough to -approximate any optimal solution.

Our algorithm can be implemented eﬃciently even in high-dimensional situations using modern machine learning tools. Its structure does not depend on speciﬁc market dynamics, and generalizes across hedging instruments including the use of liquid derivatives. Its computational performance is largely invariant in the size of the portfolio as it depends mainly on the number of hedging instruments available.

We illustrate our approach by showing the eﬀect on hedging under transaction costs in a synthetic market driven by the Heston model, where we outperform the standard “complete market” solution.

Key words and phrases: reinforcement learning, approximate dynamic programming, machine learning, market frictions, transaction costs, hedging, risk management, portfolio optimization.

## MSC 2010 Classiﬁcation: 91G60, 65K99

1. Introduction

The problem of pricing and hedging portfolios of derivatives is crucial for pricing risk-management in the ﬁnancial securities industry. In idealized frictionless and “complete market” models, mathematical ﬁnance provides, with risk neutral pricing and hedging, a tractable solution to this problem. Most commonly, in such models only the primary asset such as the equity and few additional factors are modeled. Arguably, the most successful such model for equity models is Dupire’s Local Volatility [Dup94]. For risk management, we will then compute “greeks” with respect not only to spot, but also to calibration input parameters such as forward rates and implied volatilities - even if such quantities are not actually state variables in the underlying model. Essentially, the models are used as a form of low dimensional interpolation of the

1Opinions expressed in this paper are those of the authors, and do not necessarily reﬂect the view of JP Morgan.

Date: February 12, 2018.

1

hedging instruments. Under complete market assumptions, pricing and risk of a portfolio of derivatives is linear.

In real markets, though, trading in any instrument is subject to transaction costs, permanent market impact and liquidity constraints. Furthermore, any trading desk is typically also limited by its capacity for risk and stress, or more generally capital. This requires traders to overlay the trading strategy implied by the greeks computed from the complete-market model with their own adjustments. It also means that pricing and risk are not linear, but dependent on the overall book: a new trade which reduces the risk in a particular direction can be priced more favourably. This is called having an “axe”.

The prevalent use of the “complete market” models is due to a lack of eﬃcient alternatives; even with the impressive progress made in the last years for example around super-hedging, there are still few solutions which will scale well over a large portfolio of instruments, and which do not depend on the underlying market dynamics.

Our deep hedging approach addresses this deﬁciency. Essentially, we model the trading decisions in our hedging strategies as neural networks; their feature sets consist not only of prices of our hedging instruments, but may also contain additional information such as trading signals, news analytics, or past hedging decisions – quantitative information a human trader might use, in true machine learning fashion.

Such deep hedging strategies can be described and trained (optimized in classical language) in a very eﬃcient way, while the respective algorithms are entirely model-free and do not depend on the on the chosen market dynamics. That means we can include market frictions such as transaction costs, liquidity constraints, bid/ask spreads, market impact etc, all potentially dependent on the features of the scenario.

The modeling task now amounts to specifying a market scenario generator, a loss function, market frictions and trading instruments. This approach lends itself well to statistically driven market dynamics. That also means that we do not need to be able to compute greeks of individual derivatives with a classic derivative pricing model. In fact, we will need no such “equivalent martingale model”. Our approach is greek-free. Instead, we can focus our modeling eﬀort on realistic market dynamics and the actual out-of-sample performance of our hedging signal.

High level optimizers then ﬁnd reasonably good strategies to achieve good out-of-sample hedging performance under the stated objective. In our examples, we are using gradient descent “Adam” [KB15] mini-batch training for a semi-recurrent reinforcement learning problem.

To illustrate our approach, we will build on ideas from [IAR09] and [FL00] and optimize hedging of a portfolio of derivatives under convex risk measures. To be able to compare our results with classic complete market results, we chose in this article to drive the market with a Heston model. We re-iterate that our algorithm is not dependent on the choice of the model.

To illustrate our algorithm, we investigate the following questions:

- • Section 5.2: How does neural network hedging (for diﬀerent risk-preferences) compare to the benchmark in a Heston model without transaction costs?
- • Section 5.3: What is the eﬀect of proportional transaction costs on the exponential utility indiﬀerence price?
- • Section 5.4: Is the numerical method scalable to higher dimensions?

Our analysis is based on out-of-sample performance.

To calculate our hedging strategies numerically, we approximate them by deep neural networks. State-of-the-art machine learning optimization techniques (see [IGC16]) are then used to train these networks, yielding a closeto-optimal deep hedge. This is implemented in Python using TensorFlow. Under our Heston model, trading is allowed in both stock and a variance swap. Even experiments with proportional transaction costs show promising results and the approach is also feasible in a high-dimensional setting.

- 1.1. Related literature. There is a vast literature on hedging in market models with frictions. We only highlight a few to demonstrate the complex character of the problem. For example, [RS10] study a market in which trading a security has a (temporary) impact on its price. The price process is modelled by a one-dimensional Black-Scholes model. The optimal trading strategy can be obtained by solving a system of three coupled (non-linear) PDEs. In [PBV17] a more general tracking problem (covering the temporary price impact hedging problem) is carried out for a Bachelier model and a closed form solution (involving conditional expectations of a time integral over the optimal frictionless hedging strategy) is obtained for the strategy. [HMSC95] prove that in a Black-Scholes market with proportional transaction costs, the cheapest superhedging price for a European call option is the spot price of the underlying. Thus, the concept of super-replication is of little interest to practitioners in the one dimensional case. In higher dimensional cases it suﬀers from numerical intractability.

It is well known that deep feed forward networks satisfy universal approximation properties, see, e.g., [Hor91]. To understand better why they are so eﬃcient at approximating hedging strategies, we rely on the very recent and fascinating results of [HBP17], which can be stated as follows: they quantify the minimum network connectivity needed to allow approximation of all elements in pre-speciﬁed classes of functions to within a prescribed error, which establishes a universal link between the connectivity of the approximating network and the complexity of the function class that is approximated. An abstract framework for transferring optimal M-term approximation results with respect to a representation system to optimal M-edge approximation results for neural networks is established. These transfer results hold for dictionaries that are representable by neural networks and it is also shown in [HBP17] that a wide class of representation systems, coined aﬃne systems, and including

- as special cases wavelets, ridgelets, curvelets, shearlets, α-shearlets, and more generally, α-molecules, as well as tensor-products thereof, are re-presentable by neural networks. These results suggest an explanation for the “unreasonable eﬀectiveness” of neural networks: they eﬀectively combine the optimal

approximation properties of all aﬃne systems taken together. In our application of deep hedging strategies this means: understanding the relevant input factors for which the optimal hedging strategy can be written eﬃciently.

There are several related applications of reinforcement learning in ﬁnance which have similar challenges, of which we want to highlight two related streams: the ﬁrst is the application to classic portfolio optimization, i.e. without options and under the assumption that market prices are available for all hedging instruments. As in our setup, this problem requires the use of non-linear objective functions, c.f. for example [MW97] or [ZJL17]. The sec-

- ond promising application of reinforcement learning is in algorithmic trading, where several authors have shown promising results, e.g. [DZL09] and [Lu17] to give but two examples.

The novelty in this article is that we cover derivatives in the ﬁrst place, and in particular over-the-counter derivatives which do not have an observable market price. For example, [Hal17] covers hedging using Q-learning with only the stock price under Black&Scholes assumptions and without transaction cost.

This puts our article ﬁrmly in the realm of pricing and risk managing a contingent claims in incomplete markets with friction cost. A general introduction into quantitative ﬁnance with a focus on such markets is [FS16].

- 1.2. Outline. The rest of the article is structured as follows. In Sections 2 and
- 3 we provide the theoretical framework for pricing and hedging using convex risk measures in discrete-time markets with frictions. Section 4 outlines the parametrization of appropriate hedging strategies by neural nets and provides theoretical arguments why it works. In Section 5 several numerical experiments are performed demonstrating the surprising feasibility and accuracy of the method.

2. Setting: Discrete time-market with Frictions

Consider a discrete-time ﬁnancial market with ﬁnite time horizon T and trading dates 0 = t0 < t1 < ... < tn = T. Fix a ﬁnite1 probability space Ω = {ω1,...,ωN} and a probability measure P such that P[{ωi}] > 0 for all i. We deﬁne the set of all real-valued random variables over Ω as X := {X : Ω → R}.

We denote by Ik with values in Rr any new market information available at time tk, including market costs and mid-prices of liquid instruments – typically quoted in auxiliary terms such as implied volatilities –, news, balance sheet

information, any trading signals, risk limits etc. The process I = (Ik)k=0,...,n generates the ﬁltration F = (Fk)k=0,...,n, i.e. Fk represents all information available up to tk. Note that each Fk-measurable random variable can be written as a function of I0,...,Ik; this is therefore the richest available feature set for any decision taken at tk.

1The assumption that Ω is ﬁnite is only essential for the numerical solution of the optimal hedging problem (from Section 4.3 onwards). Alternatively, we could start with arbitrary Ω and discretize it for the numerical solution. If we imposed appropriate integrability conditions on all assets and contingent claims, then the results prior to section 4.3 would remain valid for general Ω.

The market contains d hedging instruments with mid-prices given by an Rd-valued F-adapted stochastic process S = (Sk)k=0,...,n. We do not require that there is an equivalent martingale measure under which S is a martingale. We stress that our hedging instruments are not simply primary assets such as equities, but also secondary assets such as liquid options on the former. Some of those hedging instruments are therefore not tradable before a future point in time (e.g. an option only listed in 3M with then time-to-maturity of 6M). Such liquidity restrictions are modeled alongside trading cost below.

Our portfolio of derivatives which represents our liabilities is an FT measurable random variable Z. In keeping with the classic literature we may refer to this as the contingent claim, but we stress that it is meant to represent a portfolio which is a mix of liquid and OTC derivatives. The maturity T is the maximum maturity of all instruments, at which point all payments are known. No classic derivative pricing model will be needed to valuate Z or compute Greeks at any point.

Simpliﬁcations. For notational simplicity, we assume that all intermediate payments are accrued using a (locally) risk-free overnight rate. This essentially means we may assume that rates are zero and that all payments occur

- at T. We also exclude for the purpose of this article instruments with true optionality such as American options. Finally, we also assume that all currency spot exchange happens at zero cost, and that we therefore may assume that all instruments settle in our reference currency.2

Trading Strategies. In order to hedge a liability Z at T, we may trade in S using an Rd-valued F-adapted stochastic process δ = (δk)k=0,...,n−1 with δk = (δk1,...,δkd). Here, δki denotes the agent’s holdings of the ith asset at time tk. We may also deﬁne δ−1 = δn := 0 for notational convenience.

We denote by Hu the unconstrained set of such trading strategies. However, each δk is subject to additional trading constraints. Such restrictions arise due to liquidity, asset availability or trading restrictions. They are also used to restrict trading in a particular option prior to its availability. In the example above of an option which is listed in 3M, the respective trading constraints would be {0} until the 3M point. To incorporate these eﬀects, we assume that δk is restricted to a set Hk which is given as the image of a continuous, Fk-measurable map Hk : Rd(k+1) → Rd, i.e. Hk := Hk(Rd(k+1)). We stipulate that Hk(0) = 0.

Moreover, for an unconstrained strategy δu ∈ Hu, we (successively) deﬁne

with (H◦δu)k := Hk((H◦δu)0,...,(H◦δu)k−1,δku) its constrained “projection” into Hk. We denote by H := (H ◦Hu) ⊂ Hu the corresponding non-empty set of restricted trading strategies.

- Example 2.1. Assume that S are a range of options and that Vki(Ski) computes the Black & Scholes Vega of each option using the various market parameters available at time tk. The overall Vega traded with δk is then Vk(δk − δk−1) := | di=1 Vki(Ski)(δki − δki−1)|. A liquidity limit of a maximum tradable

2See [BR06] for some background on multi-currency risk measures.

Vega of Vmax could then be implemented by the map: Hk(δ0,...,δk) := δk−1 + (δk − δk−1) Vmax max{Vk(δk − δk−1),Vmax}

.

Hedging. All trading is self-ﬁnanced, so we may also need to inject additional cash p0 into our portfolio. A negative cash injection implies we may extract cash. In a market without transaction costs the agent’s wealth at time T is thus given by −Z + p0 + (δ · S)T, where

n−1

(δ · S)T :=

δk · (Sk+1 − Sk).

k=0

However, we are interested in situations where trading cost cannot be neglected. We assume that any trading activity causes costs as follows: if the agent decides to buy a position n ∈ Rd in S at time tk, then this will incur cost ck(n). The total cost of trading a strategy δ up to maturity is therefore

n

ck(δk − δk−1)

CT(δ) :=

k=0

(recall δ−1 = δn := 0, the latter of which implies full liquidation in T). The agent’s terminal portfolio value at T is therefore

- (2.1) PLT(Z,p0,δ) := −Z + p0 + (δ · S)T − CT(δ).

Throughout, we assume that the non-negative adapted cost functions are

normalized to ck(0) = 0 and that they are upper semi-continuous.3 In our numerical examples we have assumed zero transaction costs at maturity.

Our setup includes the following eﬀects:

- • Proportional transaction cost: for for cik > 0 deﬁne ck(n) := di=1 cik Ski|ni|.
- • Fixed transaction costs: for cik > 0 and ε > 0 set ck(n) := di=1 cik1|ni|≥ε.
- • Complex cross-asset cost, such as cost of volatility when trading options across the surface: assume S1 is spot and that the rest of the

hedging instruments are options on the same asset. Denote by ∆ik Delta and by Vki Vega of each instrument, for example under a simple Black & Scholes model.

We may then deﬁne a simple cross-surface proportional cost model in Delta and Vega for ck > 0 and vk > 0 as

ck(n) := cikSk1 1 +

d

∆ikni + vki

i=2

d

Vkini

i=2

- Remark 2.2. Our general setup also allows modeling true market impact: in this case, the asset distribution is aﬀected by our trading decisions.

As an example for permanent market impact, assume for simplicity that I = S and that we have a statistical model of our market in the form of a conditional distribution P(Sk+1|Sk). For a proportional impact parameter ι > 0

3This property is needed in the proof of proposition 4.9.

we may now deﬁne the dynamics of S under exponentially decaying, proportional market impact as P Sk+1 Sk (1 + ι(δk − δk−1)) . The cost function is accordingly ck(n) := Skι|n|.

In a similar vein, dynamic market impact with decay such as described in [GS13] can be implemented.

The real challenge with modeling impact is the eﬀect of trading in one hedging instrument on other hedging instruments, for example when trading options.

3. Pricing and hedging using convex risk measures

In an idealized complete market with continuous-time trading, no transaction costs, and unconstrained hedging, for any liabilities Z there exists a unique replication strategy δ and a fair price p0 ∈ R such that −Z + p0 + (δ · S)T − CT(δ) = 0 holds P-a.s. This is not true in our current setting.

In an incomplete market with frictions, an agent has to specify an optimality criterion which deﬁnes an acceptable “minimal price” for any position. Such a minimal price is the going to be the minimal amount of cash we need to add to our position in order to implement the optimal hedge and such that the overall position becomes acceptable in light of the various costs and constraints.

We focus here on optimality under convex risk measures as studied e.g. in [Xu06] and [IAR09]. See also [KS07] and further references therein for a dynamic setting. Convex risk measures are discussed in great detail in [FS16].

- Deﬁnition 3.1. Assume that X,X1,X2 ∈ X represent asset positions (i.e., −X is a liability). We call ρ : X → R a convex risk measure if it is:

- (1) Monotone decreasing: if X1 ≥ X2 then ρ(X1) ≤ ρ(X2). A more favorable position requires less cash injection.
- (2) Convex: ρ(αX1 + (1 − α)X2) ≤ αρ(X1) + (1 − α)ρ(X2) for α ∈ [0,1]. Diversiﬁcation works.
- (3) Cash-Invariant: ρ(X + c) = ρ(X) − c for c ∈ R. Adding cash to a position reduces the need for more by as much. In particular, this means that ρ(X + ρ(X)) = 0, i.e. ρ(X) is the least amount c that needs to be added to the position X in order to make it acceptable in the sense that ρ(X + c) ≤ 0.

We call ρ normalized if ρ(0) = 0.

Let ρ: X → R be such a convex risk measure and for X ∈ X consider the optimization problem

ρ(X + (δ · S)T − CT(δ)) .

- (3.1) π(X) := inf

δ∈H

Proposition 3.2. π is monotone decreasing and cash-invariant.

If moreover CT(·) and H are convex, then the functional π is a convex risk measure.

Proof. For convexity, let α ∈ [0,1], set α := 1 − α and assume X1,X2 ∈ X. Then using the deﬁnition of π in the ﬁrst step, convexity of H in the second

step, convexity of CT(·) combined with monotonicity of ρ in the third step and convexity of ρ in the fourth step, we obtain

π(αX1 + α X2)

ρ αX1 + α X2 + (δ · S)T − CT(δ)

= inf

δ∈H

ρ α {X1 + (δ1 · S)T} + α {X2 + (δ2 · S)T} − CT(αδ1 + α δ2) ≤ inf

= inf

δ1,δ2∈H

ρ α {X1 + (δ1 · S)T − CT(δ1)} + α {X2 + (δ2 · S)T − CT(δ2)} ≤ inf

δ1,δ2∈H

αρ(X1 + (δ1 · S)T − CT(δ1)) + α ρ(X2 + (δ2 · S)T − CT(δ2))

δ1,δ2∈H

= απ(X1) + α π(X2) . Cash-invariance and monotonicity follow directly from the respective properties of ρ.

We deﬁne an optimal hedging strategy as a minimizer δ ∈ H of (3.1). Recalling the interpretation of ρ(−Z) as the minimal amount of capital that has to be added to the risky position −Z to make it acceptable for the risk measure ρ, this means that π(−Z) is simply the minimal amount that the agent needs to charge in order to make her terminal position acceptable, if she hedges optimally.

If we deﬁned this as the minimal price, then we would exclude the possibility that having no liabilities may actually have positive value. This might be the case in the presence of statistically positive expectation of returns under P for some of our hedging instruments. As mentioned before, our framework lends itself to the integration of signals and other trading information. We therefore deﬁne the indiﬀerence price p(Z) as the amount of cash that she needs to charge in order to be indiﬀerent between the position −Z and not doing so, i.e. as the solution p0 to π(−Z + p0) = π(0). By cash-invariance this is equivalent to taking p0 := p(Z), where

- (3.2) p(Z) := π(−Z) − π(0) .

It is easily seen that without trading restrictions and transaction costs, this price coincides with the price of a replicating portfolio (if it exists):

- Lemma 3.3. Suppose CT ≡ 0 and H = Hu. If Z is attainable, i.e. there exists δ∗ ∈ H and p0 ∈ R such that Z = p0 + (δ∗ · S)T, then p(Z) = p0. Proof. For any δ ∈ H, the assumptions and cash-invariance of ρ imply

ρ(−Z + (δ · S)T − CT(δ)) = p0 + ρ(([δ − δ∗] · S)T). Taking the inﬁmum over δ ∈ H on both sides and using H − δ∗ = H one obtains

ρ(([δ − δ∗] · S)T) = p0 + π(0).

π(−Z) = p0 + inf

δ∈H

- Remark 3.4. The methodology developed in this article can also be applied to approximate optimal hedging strategies in a setting where the price p0 is given exogenously: ﬁx a loss function : R → [0,∞). Suppose p0 > 0 is given, for

example being the result of trading derivatives in the market at competitive prices, without taking into account risk-management. The agent then wishes to minimize her loss at maturity, i.e. she deﬁnes an optimal hedging strategy

- as a minimizer to

E[ (−Z + p0 + (δ · S)T − CT(δ))].

- (3.3) inf

δ∈H

This problem, i.e. optimal hedging under a capital constraint, is closely related to taking for ρ a shortfall risk measure, see e.g. [FL00].

Arbitrage. We mentioned in the introduction that we do not require per se that the market is free of arbitrage. To recap, we call δ[X] ∈ H an arbitrage opportunity given X is an opportunity to make money without risk of a loss, i.e. 0 ≤ X + (δ[X]S)T − CT(δ[X]) =: (∗) while P[(∗) > 0] > 0.

In case such an opportunity exists, we obviously have ρ(X) < 0. Depending on the cost function and our constraints H, we may be able to invest an unlimited amount into this strategy. In this case, we get π(X) = −∞. If this applies to X = 0, we call such a market irrelevant. This is justiﬁed by the following observation:

Corollary 3.5. Assume that π(0) > −∞. Then π(X) > −∞ for all X. Proof. Since Ω is ﬁnite we have supX < ∞ and therefore, using monotonicity, π(X) ≥ π(supX) ≥ π(0) − supX > −∞.

We note, however, that irrelevance is not necessarily a consequence of outright arbitrage; such statistical arbitrage may also occur in markets without arbitrage. Consider to this end the convex risk measure ρ(X) := −E[X], and assume that the market without interest rates is driven by a standard Black & Scholes model with positive drift µ between two time points t0 and t1, i.e.

S0 := 1 and S1 := exp µt1 + σZ√t1

for Z normal and a volatility σ > 0. Assume the proportional cost of trading S in t0 is 0.5eµt1. In this case ρ(δ0S1 −C0(δ)) = −0.5δ0eµt1 for any δ0 ∈ R which implies π(0) = −∞. Hence, the market is irrelevant, too, even if it does not exhibit classic arbitrage. We also note that this is expected in practise: as an example, consider a strategy which writes options on an underlying. In most market scenarios such a strategy will on average make money, even if it is subject to potentially drastic short-term losses.

In closing we note that even if the market dynamics exhibit classic arbitrage, and even in the absence of cost or liquidity constraints, we may not be able to exploit it. Let us assume that for every arbitrage opportunity δ[0] there is a non-zero probability of not making money, i.e. P[(δ[0]S)T + CT(δ[0]) = 0] > 0. Under the extreme risk measure ρ(X) := −inf X this market remains relevant with π(0) = 0.

- 3.1. Exponential Utility Indiﬀerence Pricing. The following lemma shows that the present framework includes exponential utility indiﬀerence pricing as studied for example in [HN89], [MHADZ93],[WW97] and [KMK15]. Recall that for the exponential utility function U(x) := −exp(−λx),x ∈ R with

risk-aversion parameter λ > 0 the indiﬀerence price q(Z) ∈ R of Z is deﬁned by

E[U(q(Z) − Z + (δ · S)T + CT(δ))] = sup δ∈H

E[U((δ · S)T + CT(δ))].

sup

δ∈H

In other words, if the seller charges a cash amount of q(Z), sells Z and trades in the market, she obtains the same expected utility as by not not selling Z

- at all.

- Lemma 3.6. Deﬁne q(Z) as above. Choose ρ as the entropic risk measure

(3.4) ρ(X) =

1 λ

log E[exp(−λX)], and deﬁne p(Z) by (3.2). Then q(Z) = p(Z). Proof. Using the special form of U, one may write the indiﬀerence price as

q(Z) =

1 λ

log

supδ∈H E[U(−Z + (δ · S)T + CT(δ))] supδ∈H E[U((δ · S)T + CT(δ))] and so the claim follows from (3.2) and (3.4).

3.2. Optimized certainty equivalents. Assume that : R → R is a loss function, i.e. continuous, non-decreasing and convex. We may deﬁne a convex risk measure ρ by setting

(3.5) ρ(X) := inf

w∈R

{w + E[ (−X − w)]}, X ∈ X.

- Lemma 3.7. (3.5) deﬁnes a convex risk measure. Proof. Let X,Y ∈ X be assets.

- (i) Monotonicity: suppose X ≤ Y . Since is non-decreasing, for any w ∈ R one has E[ (−X − w)] ≥ E[ (−Y − w)] and thus ρ(X) ≥ ρ(Y ).
- (ii) Cash invariance: for any m ∈ R, (3.5) gives

ρ(X + m) = inf

w∈R

{(w + m) − m + E[ (−X − (w + m))]} = −m + ρ(X).

- (iii) Convexity: let λ ∈ [0,1]. Then convexity of implies

ρ(λX+(1 − λ)Y )

{w + E[ (−λX − (1 − λ)Y − w)]}

= inf

w∈R

{λw1 + (1 − λ)w2 + E[ (λ(−X − w1) + (1 − λ)(−Y − w2))]} ≤ inf

= inf

w1,w2∈R

{λ(w1 + E[ (−X − w1)]) + (1 − λ)(w2 + E[ (−Y − w2)])}

inf

w1∈R

w2∈R

= λρ(X) + (1 − λ)ρ(Y ).

Taking (x) := −u(−x) (x ∈ R) for a utility function u: R → R, (3.5) coincides with the optimized certainty equivalent as deﬁned (and studied in a lot more detail than here) in [BTT07].

- Example 3.8. Fix λ > 0 and set (x) := exp(λx) − 1+log(λ λ), x ∈ R. Then the optimization problem in (3.5) can be solved explicitly and the minimizer

- w∗ satisﬁes eλw∗ = λE[exp(−λX)]. Inserting this into (3.5), one obtains the entropic risk measure deﬁned in (3.4) above.

Example 3.9. Let α ∈ (0,1) and set (x) := 1−1α max(x,0). The associated risk measure (3.5) is called average value at risk at level 1 − α (see [FS16,

- Deﬁnition 4.48, Proposition 4.51] with λ := 1−α) or also conditional value at risk or expected shortfall.

- Proposition 3.10. Suppose S is a P-martingale, ρ is deﬁned as in (3.5) and π, p as in (3.1), (3.2). Then

- (i) π(0) = ρ(0),
- (ii) p(Z) ≥ E[Z] for any Z ∈ X.

Proof. Since 0 ∈ H and CT(0) = 0, one has π(0) ≤ ρ(0) for any choice of risk measure ρ in (3.1). Under the present assumptions the converse inequality is also true: Since S is a martingale, it holds that

n−1

- (3.6) E[(δ · S)T] =

E[δjE[Sj+1 − Sj|Fj]] = 0 for any δ ∈ H.

j=0

By ﬁrst applying Jensen’s inequality (recall that is convex) and then using

- (3.6), that CT(δ) ≥ 0 for any δ ∈ H and that is non-decreasing, one obtains
- (3.7)

{w + E[ (Z − (δ · S)T + CT(δ) − w)]} ≥ inf

π(−Z) = inf

inf

w∈R

δ∈H

{w + (E[Z − (δ · S)T + CT(δ) − w])} ≥ inf

inf

w∈R

δ∈H

{w + (E[Z] − w)} = ρ(−E[Z]) = E[Z] + ρ(0).

w∈R

Inserting Z = 0 yields the converse inequality π(0) ≥ ρ(0) and thus (i). Combining (i), (3.2) and (3.7) then directly gives (ii).

4. Approximating hedging strategies by deep neural networks

The key idea that we pursue in this article is to approximate hedging strategies by neural networks. Before describing this approach in more detail we recall the deﬁnition and approximation properties of neural networks and prove some basic results on hedging strategies built from them. While these results show that the approach is theoretically well-founded, they are only one reason why we have used neural networks (and not some other parametric family of functions) to approximate hedging strategies. The other reason is that optimal hedging strategies built from neural networks can numerically be calculated very eﬃciently. This is explained ﬁrst for the case of OCE risk measures and for entropic risk. Finally, an extension to general risk measures is presented.

- 4.1. Universal approximation by neural networks. Let us ﬁrst recall the deﬁnition of a (feed forward) neural network:

Deﬁnition 4.1. Let L,N0,N1,...,NL ∈ N, σ: R → R and for any = 1,...,L, let W : RN −1 → RN an aﬃne function. A function F : RN0 → RNL deﬁned as

F(x) = WL ◦ FL−1 ◦ ··· ◦ F1 with F = σ ◦ W for = 1,...,L − 1 is called a (feed forward) neural network. Here the activation function σ is applied componentwise. L denotes the number of layers, N1,...,NL−1 denote the dimensions of the hidden layers and N0, NL of the input and output layers,

respectively. For any = 1,...,L the aﬃne function W is given as W (x) = A x + b for some A ∈ RN ×N −1 and b ∈ RN . For any i = 1,...N ,j = 1,...,N −1 the number A ij is interpreted as the weight of the edge connecting the node i of layer − 1 to node j of layer . The number of non-zero weights of a network is the sum of the number of non-zero entries of the matrices A ,

= 1,...,L and vectors b , = 1,...,L.

Denote by NNσ∞,d0,d1 the set of neural networks mapping from Rd0 → Rd1 and with activation function σ. The next result ([Hor91, Theorems 1 and 2]) illustrates that neural networks approximate multivariate functions arbitrarily well.

Theorem 4.2 (Universal approximation, [Hor91]). Suppose σ is bounded and non-constant. The following statements hold:

- • For any ﬁnite measure µ on (Rd0,B(Rd0)) and 1 ≤ p < ∞, the set NNσ∞,d0,1 is dense in Lp(Rd0,µ).
- • If in addition σ ∈ C(R), then NNσ∞,d0,1 is dense in C(Rd0) for the topology of uniform convergence on compact sets.

Since each component of an Rd1-valued neural network is an R-valued neural

network, this result easily generalizes to NNσ∞,d0,d1 with d1 > 1, see also [Hor91]. A variety of other results with diﬀerent assumptions on σ or emphasis

on approximation rates are available, see e.g. [HBP17] for further references. In what follows, we ﬁx an activation function σ and omit it in the no-

tation, i.e. we write NN∞,d0,d1 := NNσ∞,d0,d1. Furthermore, we denote by {NNM,d0,d1}M∈N a sequence of subsets of NN∞,d0,d1 with the following properties:

- • NNM,d0,d1 ⊂ NNM+1,d0,d1 for all M ∈ N,
- • M∈N NNM,d0,d1 = NN∞,d0,d1,
- • for any M ∈ N, one has NNM,d0,d1 = {Fθ : θ ∈ ΘM,d0,d1} with ΘM,d0,d1 ⊂ Rq for some q ∈ N (depending on M).

- Remark 4.3. We have two classes of examples in mind: the ﬁrst one is to take

for NNM,d0,d1 the set of all neural networks in NN∞,d0,d1 with an arbitrary number of layers and nodes, but at most M non-zero weights. The second

- one is to take for NNM,d0,d1 the set of all neural networks in NN∞,d0,d1 with a ﬁxed architecture, i.e. a ﬁxed number of layers L(M) and ﬁxed input and output dimensions for each layer. These are speciﬁed by d0, d1 and some

non-decreasing sequences {L(M)}M∈N and {N1(M)}M∈N, ..., {NL(M(M))−1}M∈N. In both cases the set NNM,d0,d1 is parametrized by matrices A and vectors b .

- 4.2. Optimal hedging using deep neural networks. Motivated by the universal approximation results stated above, we now consider neural network hedging strategies. Let our activation function therefore be bounded and nonconstant.

In order to apply our theorem 4.2, we represent the optimization over constrained trading strategies δ ∈ H as an optimization over δ ∈ Hu with a following modiﬁed objective.

- Lemma 4.4. We may write the constrained problem 3.1 as the modiﬁed unconstrained problem as

- (3.1’) π(X) = inf

δ∈Hu

ρ(X + (H ◦ δ · S)T − CT(H ◦ δ)) . Proof. Note that H◦δ = δ for all δ ∈ H, and H◦δu ∈ H for all δu ∈ Hu.

Recall that the information available in our market at tk is described by the observed maximal feature set I0,...,Ik. Our trading strategies should therefore depend on this information and on our previous position in our tradable assets. This gives rise to the following semi-recurrent deep neural network structure for our unconstrained trading strategies:

HM = {(δk)k=0,...,n−1 ∈ Hu : δk = Fk(I0,...,Ik,δk−1),Fk ∈ NNM,r(k+1)+d,d}

- (4.1)

= {(δkθ)k=0,...,n−1 ∈ Hu : δkθ = Fθk(I0,...,Ik,δk−1),θk ∈ ΘM,r(k+1)+d,d} We now replace the set Hu in (3.1’) by HM ⊂ Hu. We aim at calculating

πM(X) := inf

- (4.2) ρ(X + (H ◦ δ · S)T − CT(H ◦ δ))

δ∈HM

ρ(X + (H ◦ δθ · S)T − CT(H ◦ δθ)),

= inf

θ∈ΘM

where ΘM = nk=0−1 ΘM,r(k+1)+d,d. Thus, the inﬁnite-dimensional problem of ﬁnding an optimal hedging strategy is reduced to the ﬁnite-dimensional con-

straint problem of ﬁnding optimal parameters for our neural network.

- Remark 4.5. Our setup becomes truly “recurrent” if we enforce θk = θ0 for all k and add “k” as a parameter into the network. Below proof applies with few modiﬁcations.
- Remark 4.6. If S is an (F,P)-Markov process and Z = g(ST) for g: Rd → R and with simplistic market frictions we may know that the optimal strategy in (3.1) is of the simpler form δk = fk(Ik,δk−1) for some fk : Rr+d → Rd.
- Remark 4.7. We would similarly transform (3.3) into a modiﬁed unconstrained problem, optimized over HM.
- Remark 4.8. For practical implementations, handling trading constraints with 4.2

is not particularly eﬃcient since the gradient of ΘM of our objective outside H vanishes. In the case where H ◦ δ = δ for δ ∈ H, this can be addressed by variants of

ρ(X + (H ◦ δ · S)T − CT(δ) − γ δ − H ◦ δ 1) . for Lagrange multipliers γ 0.

π(X) ≡ inf

δ∈Hu

The next proposition shows that thanks to the universal approximation theorem, strategies in H are approximated arbitrarily well by strategies in HM. Consequently, the neural network price πM(−Z) − πM(0) converges to the exact price p(Z).

- Proposition 4.9. Deﬁne HM as in (4.1) and πM as in (4.2). Then for any X ∈ X,

πM(X) = π(X) .

lim

M→∞

Proof. We ﬁrst note that the argument δk−1 in 4.2 is redundant, since iteratively δk−1 is itself a function of I0,...,Ik−1. We may therefore write for the purpose of this proof

- (4.1’) HM = {(δkθ)k=0,...,n−1 ∈ Hu : δkθ = Fk(I0,...,Ik),Fk ∈ NNM,r(k+1),d} .

Since HM ⊂ HM+1 ⊂ Hu for all M ∈ N it follows that πM(X) ≥ πM+1(X) ≥ π(X). Thus it suﬃces to show that for any ε > 0 there exists M ∈ N such that πM(X) ≤ π(X) + ε.

By deﬁnition, there exists δ ∈ Hu such that (4.3) ρ(X + (H ◦ δ · S)T − CT(H ◦ δ)) ≤ π(X) +

ε 2

.

Since δk is Fk-measurable, there exists fk : Rr(k+1) → Rd measurable such that δk = fk(I0,...,Ik) for each k = 0,...,n−1. Since Ω is ﬁnite, δk is bounded and so fki ∈ L1(Rr(k+1),µ) for any i = 1,...d, where µ is the law of (I0,...,Ik) under P. Thus one may use theorem 4.2 to ﬁnd Fk,ni ∈ NN∞,r(k+1),1 such that Fk,ni (I0,...,Ik) converges to fki(I0,...,Ik) in L1(P) as n → ∞.

By passing now to a suitable subsequence, convergence holds P-a.s. simul-

taneously for all i,k. Writing δkn := Fk,n(I0,...,Ik) and using P[{ω}] > 0 for all ω ∈ Ω, this implies

(4.4) lim

n→∞

δkn(ω) = δk(ω) for all ω ∈ Ω.

Continuity of Hk(·)(ω) for a ﬁxed ω implies moreover that also limn→∞ Hk(ω)◦ δkn(ω) = Hk(ω) ◦ δk(ω).

Since Ω is ﬁnite, ρ can be viewed as a convex function ρ: RN → R. In particular, ρ is continuous. Using continuity of ρ in the ﬁrst step and upper semi-continuity of ck(·)(ω) for each ω ∈ Ω combined with monotonicity of ρ in the second step, one obtains

liminf

n→∞

ρ(X + (H ◦ δn · S)T − CT(H ◦ δn)) ≤ ρ(X + (H ◦ δ · S)T − limsup

n→∞

CT(H ◦ δn))

≤ ρ(X + (H ◦ δ · S)T − CT(H ◦ δ)). Combining this with (4.3), there exists n ∈ N (large enough) such that (4.5) ρ(X + (H ◦ δn · S)T − CT(H ◦ δn)) ≤ π(X) + ε. Since δn ∈ HM for all M large enough, one obtains πM(X) ≤ π(X) + ε by

- (4.2) and (4.5), as desired.

- 4.3. Numerical solution for OCE-risk measures. While Theorem 4.2 and Proposition 4.9 give a theoretical justiﬁcation for using hedging strategies built from neural networks, we now turn to computational considerations: how

can we calculate a (close-to) optimal parameter θ ∈ ΘM for (4.2)?

To explain the key ideas we focus on the case when ρ is an OCE risk measure (see (3.5)) and no trading constraints are present, the case of general risk measures is treated below.

Inserting the deﬁnition of ρ, see (3.5), into (4.2), the optimization problem can be rewritten as

w + E[ (Z − (δθ¯ · S)T + CT(δθ¯) − w)] = inf

πM(−Z) = inf

inf

J(θ),

w∈R

θ¯∈ΘM

θ∈Θ

where Θ = R × ΘM and for θ = (w,θ¯) ∈ Θ,

- (4.6) J(θ) := w + E[ (Z − (δθ¯ · S)T + CT(δθ¯) − w)].

Generally, to ﬁnd a local minimum of a diﬀerentiable function J, one may use a gradient descent algorithm: Starting with an initial guess θ(0), one iteratively deﬁnes

- (4.7) θ(j+1) = θ(j) − ηj∇Jj(θ(j)),

for some (small) ηj > 0, j ∈ N and with Jj = J. Under suitable assumptions on J and the sequence {ηj}j∈N, θ(j) converges to a local minimum of J as j → ∞. Of course, the success and feasibility of this algorithm crucially depends on two points: Firstly, can one avoid ﬁnding a local minimum instead of a global one? Secondly, can ∇J be calculated eﬃciently?

One of the key insights of deep learning is that for cost functions J built based on neural networks both of these problems can be dealt with simultaneously by using a variant of stochastic gradient descent and the (error) backpropagation algorithm. What this means in our context is that in each step j the expectation in (4.6) (which is in fact a weighted sum over all elements of the ﬁnite, but potentially very large sample space Ω) is replaced by an expectation over a randomly (uniformly) chosen subset of Ω of size Nbatch N, so that Jj used in the update (4.7) is now given as

Nbatch

Jj(θ) = w+

m=1

N Nbatch

(Z(ωm(j))−(δθ¯·S)T(ωm(j))+CT(δθ¯)(ωm(j))−w)

P[{ωm(j)}]

for some ω1(j),...,ωN(j)

∈ Ω. This is the simplest form of the (minibatch) stochastic gradient algorithm. Not only does it make the gradient computation

batch

- a lot more eﬃcient (or possible at all, if N is large), but it also avoids getting stuck in local minima: even if θ(j) arrives at a local minimum at some j, it moves on afterwards (due to the randomness in the gradient). In order

to calculate the gradient of Jj for each of the terms in the sum, one may now rely on the compositional structure of neural networks. If , c and σ are suﬃciently diﬀerentiable and the derivatives are available in closed form, then one may use the chain rule to calculate the gradient of Fθ¯k with respect to θ analytically and the same holds for the gradient of Jj. Furthermore, these analytical expressions can be evaluated very eﬃciently using the so called backpropagation algorithm (see subsequent section).

While this certainly answers the second question posed above (eﬃciency), the ﬁrst one (local minima) is only partially resolved, as there is no general result guaranteeing convergence to the global minimum in a reasonable amount

- of time. However, it is common belief that for suﬃciently large neural networks, it is possible to arrive at a suﬃciently low value of the cost function in a reasonable amount of time, see [IGC16, Chapter 8].

Finally, note that for the experiments in Section 5 below we have used Adam, a more reﬁned version of the stochastic gradient algorithm, as introduced in [KB15] and also discussed in [IGC16, Chapter 8.5.3].

- Remark 4.10. In the experiments in Section 5 below, the functions , c and σ are continuous, but have only piecewise continuous derivatives. Nevertheless, similar techniques can be applied.
- Remark 4.11. Numerically, trading constraints can be handled by introducing Lagrange-multipliers or by imposing inﬁnite trading cost outside the allowed trading range. Certain types of constraints can also be dealt with by the choice of activation function: for example, no short-selling constraints can be enforced by choosing a non-negative activation function σ. A systematic numerical treatment will be left for future research.

- 4.4. Certainty Equivalent of Exponential Utility. The entropic risk measure (3.4) is a special case of an OCE risk measure, as explained in example 3.8. However, when applying the methodology explained in Section 4.3, there is no need to minimize over w: we may directly insert (3.4) into (4.2) to write

πM(−Z) =

1 λ

log inf

θ∈ΘM

J(θ),

where (4.8) J(θ) := E[ exp(−λ[−Z + (δθ · S)T − CT(δθ)]) ]. A close-to-optimal θ ∈ ΘM can then be found numerically as above.

- 4.5. Extension to general risk measures. As explained in Section 4.3, for OCE risk measures the optimal hedging problem (4.2) is amenable to deep learning optimization techniques (i.e. variants of stochastic gradient descent) via (4.6). The key ingredient for this is that the objective J satisﬁes

- (ML1) the gradient of J decomposes into a sum over the samples, i.e. ∇θJ(θ) = N m=1 ∇θJ(θ,ωm) and
- (ML2) ∇θJ(θ,ωm) can be calculated eﬃciently for each m, i.e. using backpropagation.

The goal of the present section is to show that for a general class of convex risk measures (including all coherent ones) one can approximate (3.1) by a minimax problem over neural networks and that the objective functional of this approximate problem also has these two key properties, making it amenable to deep learning optimization techniques.

Denote by P the set of probability measures on (Ω,F). The following result serves as a starting point:

- Theorem 4.12 (Robust representation of convex risk measures). Suppose ρ: X → R is a convex risk measure. Then ρ can be written as

(EQ[−X] − α(Q)), X ∈ X,

- (4.9) ρ(X) = max

Q∈P

where α(Q) := supX∈X (EQ[−X] − ρ(X)).

Proof. Since for Ω ﬁnite the set of probability measures P coincides with the set of ﬁnitely additive, normalized set functions (appearing in [FS16, Theorem 4.16]), the present statement follows directly from the cited theorem and [FS16, Remark 4.17].

The function α: P → R is called the (minimal) penalty function of the risk measure ρ.

Since Ω is ﬁnite, P can be identiﬁed with the standard N −1 simplex in RN and so (4.9) is an optimization over RN. However, N is very large in our context and so the representation (4.9) is of little use for numerical calculations. The next result shows that ρ(X) can be approximated by an optimization problem over a lower-dimensional space. To state it, let us deﬁne the set L ⊂ X of log-likelihoods by

L := {f ∈ X : E[exp(f)] = 1},

deﬁne α¯: L → R by α¯(f) = α(exp(f)dP) for any f ∈ L and write Peq for the set of probability measures on (Ω,F), which are equivalent to P. Furthermore,

one may view I¯ = (I0,...,In) as a map Ω → Rr(n+1).

## Theorem 4.13. Suppose

- (i) α(Q) < ∞ for some Q ∈ Peq,
- (ii) α¯ is continuous,
- (iii) F = FT.

Then for any X ∈ X, ρ(X) = limM→∞ ρM(X), where

- (4.10) ρM(X) := sup θ∈ΘM,r(n+1),1

E[exp(Fθ◦I¯)]=1

E[−X exp(Fθ ◦ I¯)] − α¯(Fθ ◦ I¯) .

Proof. We proceed in two steps. In a ﬁrst step we show that for any X ∈ X one may write

- (4.11) ρ(X) = sup f¯∈M

E[exp(f¯◦I¯)]=1

E[−X exp(f¯◦ I¯)] − α¯(f¯◦ I¯) ,

where M denotes the set of measurable functions mapping from Rr(n+1) → R. In the second step we rely on (4.11) to prove the statement.

Step 1: Since P[{ωi}] > 0 for all i, X coincides with L∞(Ω,F,P) and ρ is law-invariant. Thus by (i) and [FS16, Theorem 4.43] one may write

- (4.12) ρ(X) = sup Q∈Peq

(EQ[−X] − α(Q)), X ∈ X. Note that Peq may be written in terms of L as

- (4.13) Peq = {exp(f)dP : f ∈ L}. Furthermore, using (iii) one obtains
- (4.14) X = {f¯◦ I¯ : f¯∈ M}. Combining (4.12), (4.13) and the deﬁnition of α¯ one obtains

(E[−X exp(f)] − α¯(f)), which can be rewritten as (4.11) by using (4.14).

ρ(X) = sup

f∈L

Step 2: Note that one may also write (4.10) as

- (4.15) ρM(X) = sup

f∈NNM,r(n+1),1 E[exp(f◦I¯)]=1

E[−X exp(f ◦ I¯)] − α¯(f ◦ I¯) .

Combining (4.15) with (4.11) and using NNM,r(n+1),1 ⊂ NNM+1,r(n+1),1 ⊂ M, one obtains that ρM(X) ≤ ρM+1(X) ≤ ρ(X) for all M ∈ N. Thus it suﬃces to show that for any ε > 0 there exists M ∈ N such that ρM(X) ≥ ρ(X) − ε.

By (4.11), for any ε > 0 one ﬁnds f¯∈ M such that

- (4.16) E[exp(f¯◦ I¯)] = 1,
- (4.17) ρ(X) − 2ε ≤ E[−X exp(f¯◦ I¯)] − α¯(f¯◦ I¯).

Precisely as in the proof of Proposition 4.9, one may use Theorem 4.2 to ﬁnd f(n) ∈ NN∞,r(n+1),1 such that P-a.s., f(n) ◦ I¯ converges to f¯◦ I¯ as n → ∞. Combining this with (4.16), one obtains that for all n large enough, cn := log(E[exp(f(n) ◦ I¯)]) is well-deﬁned and that f¯(n) ◦ I¯ also converges P-a.s. to f¯◦ I¯, as n → ∞, where f¯(n) := f(n) − cn. Using this, (4.17) and assumption (ii), for some (in fact all) n ∈ N large enough one obtains

- (4.18) ρ(X) − ε ≤ E[−X exp(f¯(n) ◦ I¯)] − α¯(f¯(n) ◦ I¯).

From NN∞,r(n+1),1−cn = NN∞,r(n+1),1 and from the choice of NNM,r(n+1),1, one has f¯(n) ∈ NNM,r(n+1),1 for M large enough. By combining this with

- (4.18) and the choice of cn one obtains ρ(X) − ε ≤ ρM(X),

as desired.

Combining (4.2) and (4.10), one thus approximates (3.1) for X = −Z by solving

- (4.19) inf θ0∈ΘM

sup

J(θ),

θ1∈ΘM,r(n+1),1

where θ = (θ0,θ1), J(θ) := E −PL(Z,0,δθ0)exp(Fθ1 ◦ I¯) − α¯(Fθ1 ◦ I¯) − λ0(E[exp(Fθ1 ◦ I¯)] − 1) and λ0 is a Lagrange multiplier.

We conclude this section by arguing that the objective J in (4.19) indeed satisﬁes (ML1) and (ML2). This is standard (c.f. Section 4.3) for all terms in the sum except for α¯(Fθ1 ◦ I¯) and so we only consider this term.

Recall that Ω is ﬁnite and consists of N elements, thus X = {X : Ω → R} can be identiﬁed with RN. As for standard backpropagation the compositional structure can be used for eﬃcient computation:

Proposition 4.14. Suppose α¯ can be extended to α¯: X → R continuously diﬀerentiable, σ is continuously diﬀerentiable and NNM,r(n+1),1 is the set of neural networks with a ﬁxed architecture (see Remark 4.3). Then J(θ1) := α¯(Fθ1 ◦I¯), θ1 ∈ ΘM,r(n+1),1 is continuously diﬀerentiable and satisﬁes (ML1).

Proof. Note that F = Fθ1 is parametrized by the matrices A and vectors

- b , = 1,...,L, and that one may consider all partial derivatives separately.

### α¯(F ◦ I¯) and ∂b

Given α¯: X → R and ∇α¯: X → X, one thus aims at calculating ∂A

i,j

α¯(F ◦ I¯) for = 1,...,L,i = 1,...,N ,j = 1,...,N −1. This can be done by the chain rule: For θ ∈ {A i,j,b i}, one has

i

N

∂θα¯(F ◦ I¯) =

∇α¯(F ◦ I¯)(ωm)∂θF(I¯(ωm))

m=1

and in particular (ML1) holds. Furthermore, in the notation of the proof, for any m = 1,...N the deriva-

tive ∂θF(I¯(ωm)) can be calculated using standard backpropagation algorithm (preceded by a forward iteration) and so (ML2) holds as well. For the reader’s

convenience we state it here: One sets x0 = I¯(ωm), iteratively calculates

- x := F (x −1) for = 1,...,L−1 and xL := WL(xL−1). Then (this is the backward pass) one sets JL := AL and calculates iteratively J = J +1dF (x −1) for = L − 1,...,1, where

dF (x −1) = diag(σ (W x −1))A . From this one may use again the chain rule to obtain for any = 1,...L,i = 1,...,N ,j = 1,...,N −1 the derivatives of F with respect to the parameters

- as

### F(I¯(ωm)) = Ji +1σ ((W x −1)i)xj −1 ∂b

∂A

i,j

F(I¯(ωm)) = Ji +1σ ((W x −1)i).

i

5. Numerical experiments and results

After having introduced the optimal hedging problem (3.1) in Section 3 and described in Section 4 how one may numerically approximate the solution by (4.2) using neural networks, we now turn to numerical experiments to illustrate the feasibility of the approach. We start by explaining in Section 5.1 the modeling choices in detail. The remainder of this section will then be devoted to examining the following three questions:

- • Section 5.2: How does neural network hedging (for diﬀerent risk-preferences) compare to the benchmark in a Heston model without transaction costs?
- • Section 5.3: What is the eﬀect of proportional transaction costs on the exponential utility indiﬀerence price?
- • Section 5.4: Is the numerical method scalable to higher dimensions?

- 5.1. Setting and Implementation. For the results presented here we have chosen a time horizon of 30 trading days with daily rebalancing. Thus, T = 30/365, n = 30 and the trading dates are ti = i/365, i = 0,...,n. As ex-

plained in Section 4 and Remark 4.6, the number of units δti ∈ Rd that the agent decides to hold in each of the instruments at ti is parametrized by a semi-recurrent neural network: we set δkθ = Fθk(Ik,δkθ−1) where Fθk is a feed forward neural network with two hidden layers and Ik = Φ(S0,...,Sk) for

some Φ: R(k+1)d → Rd speciﬁed below. More precisely, in the notation of Definition 4.1, Fθk is a neural network with L = 3, N0 = 2d, N1 = N2 = d + 15, N3 = d and the activation function is always chosen as σ(x) = max(x,0). The weight matrices and biases are the parameters to be optimized in (4.2). Note that these are diﬀerent for each k.

Having made these choices, the algorithm outlined in Section 4 can now be used for approximate hedging in any market situation: given sample trajectories of the hedging instruments S(ωm), samples of the payoﬀ Z(ωm) and associated weights P[{ωm}] for m = 1,...,N (on a ﬁnite probability space Ω = {ω1,...,ωN}), for any choice of transaction cost structure c and any risk measure ρ one may now use the algorithm outlined in Section 4 to calculate close-to optimal hedging strategies and approximate minimal prices. Of course, for a path-dependent derivative with payoﬀ Z = G(S0,...,ST) with G: (Rd)n+1 → R one obtains samples of the payoﬀ by simply evaluating G on the sample trajectories of S.

Diﬀerent risk measures ρ, transaction cost functions c and payoﬀs Z will be used in the examples and so these are described separately in each of the subsequent sections. To illustrate the feasibility of the algorithm and have a benchmark at hand for comparison (at least in the absence of transaction costs), we have chosen to generate the sample paths of S from a standard stochastic volatility model under a risk-neutral measure P. Thus in most of the examples below, the process S follows (a discretization of) a Heston model, see the beginning of Section 5.2 below. But we stress again that, as explained above, the algorithm is model independent in the sense that no information about the Heston model is used except for the (weighted) samples of the price and variance process.

The algorithm has been implemented in Python, using Tensorﬂow to build and train the neural networks. To allow for a larger learning rate, the technique of batch normalization (see [IS15] and [IGC16, Chapter 8.7.1]) is used in each layer of each network right before applying the activation function. The network parameters are initialized randomly (drawn from uniform and normal distribution). For network training the Adam algorithm (see [KB15], [IGC16, Chapter 8.5.3]) with a learning rate of 0.005 and a batch size of 256 has been used. Finally, the model hedge for the benchmark in Section 5.2 has been calculated using Quantlib.

Remark 5.1. For the numerical experiments in this article the optimality criteria in (4.6) and (4.8) are speciﬁed under a risk-neutral measure. Thus, an optimal hedging strategy is based on market anticipations of future prices. Alternatively, one could use a statistical measure. The algorithm presented here can be applied also in this case.

- 5.2. Benchmark: No transaction costs. As a ﬁrst example, we consider hedging without transaction costs in a Heston model. In this example the risk measure ρ is chosen as the average value at risk (also called conditional value

- at risk or expected shortfall), deﬁned for any random variable X by

1 1 − α

- (5.1) ρ(X) :=

1−α

VaRγ(X)dγ

0

for some α ∈ [0,1), where VaRγ(X) := inf{m ∈ R : P(X < −m) ≤ γ}. An alternative representation of ρ of type (3.5) is discussed in Example 3.9. We refer to [FS16, Section 4.4] for further details. Note that diﬀerent levels of α correspond to diﬀerent levels of risk-aversion, ranging from risk-neutral for α close to 0 to very risk-averse for α close to 1. The limiting cases are ρ(X) = −E[X] for α = 0 and limα↑1 ρ(X) = −essinf(X), see [FS16, p.234 and

- Remark 4.50].

A brief reminder on the Heston model. Recall that a Heston model is speciﬁed by the stochastic diﬀerential equations

- (5.2)

dSt1 = VtSt1dBt, for t > 0 and S01 = s0 dVt = α(b − Vt)dt + σ VtdWt, for t > 0 and V0 = v0,

where B and W are one-dimensional Brownian motions (under a probability measure Q) with correlation ρ ∈ [−1,1] and α, b, σ, v0 and s0 are positive constants. Below we have chosen α = 1, b = 0.04, ρ = −0.7, σ = 2, v0 = 0.04 and s0 = 100, reﬂecting a typical situation in an equity market.

Here S1 is the price of a liquidly tradeable asset and V is the (stochastic) variance process of S1, modeled by a Cox-Ingersoll-Ross (CIR) process. V itself is not tradable directly, but only through options on variance. In our framework this is modeled by an idealized variance swap with maturity T, i.e. we set FtH := σ((Ss1,Vs) : s ∈ [0,t]) and

- (5.3) St2 := EQ

T

0

Vs ds FtH , t ∈ [0,T],

and consider (S1,S2) as the prices of liquidly tradeable assets. A standard calculation4 shows that (5.3) is given as

- (5.4) St2 =

t

0

Vs ds + L(t,Vt) where

L(t,v) =

v − b α

(1 − e−α(T−t)) + b(T − t).

Consider now a European option with payoﬀ g(ST1) at T for some g: R → R. Its price (under Q) at t ∈ [0,T] is given as Ht := EQ[g(ST1)|FtH]. By the Markov property of (S1,V ), one may write the option price at t as Ht = u(t,St1,Vt) for some u: [0,T] × [0,∞)2 → R. Assuming that u is suﬃciently smooth, one may apply Itˆ’s formula to H and use (5.4) to obtain

- (5.5) g(ST1) = q +

T

0

δt1 dSt1 +

T

0

δt2 dSt2 where q = EQ[g(ST1)] and

- (5.6) δt1 := ∂su(t,St1,Vt) and δt2 :=

∂vu(t,St1,Vt) ∂vL(t,Vt)

.

4For example, one may use that (log(S1), V ) is an aﬃne process to see that the conditional expectation in (5.3) can be taken only with respect to σ(Vt, s ∈ [0, t]). This conditional expectation can then be calculated by using the SDE for V or by directly inserting the expression from e.g. [Duf01, Section 3].

Thus, if continuous-time trading was possible, (5.5) shows that the option payoﬀ can be replicated perfectly by trading in (S1,S2) according to the strategy

- (5.6).

- Remark 5.2. The strategy (5.6) depends on Vt. Although not observable di-

rectly, an estimate can be obtained by estimating 0 t Vs ds and solving (5.4) for Vt.

Setting: Discretized Heston model. In addition to the setting explained in detail in Section 5.1, here we set d = 2, consider no transaction costs (i.e. CT ≡ 0) and generate sample trajectories of the price process of the hedging instruments from a discretely sampled Heston model. Thus, S = (S0,...,Sn) and for any k = 0,...,n, Sk = (Sk1,Sk2) is given by (5.2) and (5.4) under Q. The sample paths of S are generated by (exact) sampling from the transition density of the CIR process (see [Gla04, Section 3.4]) and then using the (simpliﬁed) Brodie-Kaya scheme (see [LBAK10] and [BK06]).5 Generating independent samples of S according to this scheme can now be viewed as sampling from a uniform distribution on a (huge) ﬁnite probability space Ω.6 Thus, in the notation of Section 5.1 one has P[{ωm}] = 1/N for all m = 1,...,N with each S(ωm) corresponding to a sample of the Heston model generated as explained above.

If continuous-time trading was possible, any European option could be replicated perfectly by following the strategy (5.6). However, in the present setup the hedging portfolio can only be adjusted at discrete time-points. Nevertheless one may choose δkH := (δk1,δk2) for k = 0...n−1 with δ1,δ2 deﬁned by (5.6) and charge the risk-neutral price q. This will be referred to as the model-delta hedging strategy (or simply model hedge) and serves as a benchmark.

Finally, in order to compare the neural network strategies to this benchmark, the network input is chosen as Ik = (log(Sk1),Vk). One could also replace Vk by Sk2 instead. The network structure at time-step tk is illustrated in Figure 1.

Results. We now compare the model hedge δH to the deep hedging strategies δθ corresponding to diﬀerent risk-preferences, captured by diﬀerent levels of α in the average value at risk (5.1).

As a ﬁrst example, consider a European call option, i.e. Z = (ST1 − K)+ with K = s0. Following the methodology outlined in Section 5.1, we calculate a (close-to) optimal parameter θ for (4.2) with X = −Z and denote by

δθ and pθ0 the (close-to) optimal hedging strategy and value of (4.2), respectively. By deﬁnition of the indiﬀerence price (3.2), the approximation property

Proposition 4.9, Proposition 3.10 and ρ(0) = 0, pθ0 is an approximation to the indiﬀerence price p(Z). As an out-of-sample test, one can then simulate another set of sample trajectories (here 106) and evaluate the terminal hedging errors q−Z +(δH ·S)T (model hedge) and pθ0 −Z +(δθ ·S)T (CVar) on each of them. In fact, since the risk-adjusted price pθ0 is higher than the risk-neutral

- 5This corresponds to replacing V in the SDE for S1 in (5.2) by a piecewise constant

process and the integral in (5.4) by a sum.

- 6To be more precise, one replaces the normal distributions appearing in the simulation

scheme for S by (arbitrarily ﬁne) discrete distributions.

Input layer at ti

Output layer at ti

Hidden layer I at ti

Hidden layer II at ti

##### log(st

)

i

δt(s)

##### Input layer at ti+1

vt

i

i

δt(s)

Input layer at ti+1

i

δt(s)

##### Output layer at ti−1

i−1

δt(v)

Output layer at ti−1

i−1

Figure 1. Recurrent network structure

price q = 1.69 (as shown in Proposition 3.10(ii)), for (CVar) we have evaluated q − Z + (δθ · S)T, i.e. the hedging error from using the optimal strategy associated to ρ, but only charging the risk-neutral price q. This is shown in a histogram in Figure 2 for α = 0.5, yielding a risk-adjusted price pθ0 = 1.94. As one can see, the hedging performance of δH and δθ is very similar. In particular

- • for this choice of risk-preferences (ρ as in (5.1) with α = 0.5) the optimal strategy in (3.1) is close to the model hedge δH,
- • the neural network strategy δθ is able to approximate well the optimal strategy in (3.1).

This is also illustrated by Figure 3, where the strategies δtθ and δtH at a ﬁxed time-point t are plotted conditional on (St1,Vt) = (s,v) on a grid of values for (s,v). To make this last comparison fully sensible instead of the recurrent network structure δkθ = Fθk(Ik,δkθ−1) here a simpler structure δkθ = Fθk(Ik) is used. The hedging performance for this simpler structure is, however, very similar, see Figure 4. Of course, this is also expected from (5.6).7

A more extreme case is shown in Figure 6, where instead of the model hedge the 99%-CVar criterion is used, i.e. α = 0.99. This results in a signiﬁcantly higher risk-adjusted price pθ0 = 3.49. If both the 50% and 99%-CVar optimal strategies are used, but only the risk-neutral price is charged (see Figure 7) one can clearly see the risk preferences: the 50%-CVar strategy is more centered at 0 and also has a smaller mean hedging error, but the 99%-expected shortfall

7For non-zero transaction costs this is not true anymore, i.e. the recurrent network structure is needed. For example, Figure 5 is generated for precisely the same parameters as Figure 4, except that α = 0.99 and proportional transaction costs are incurred, i.e. (5.7) with ε = 0.01.

35000

0.5-CVar

Model hedge

30000

25000

20000

15000

10000

5000

0

3 2 1 0 1 2 3

- Figure 2. Comparison of model hedge and deep hedge associated to 50%-expected shortfall criterion.

96

98

100

102 0.04

0.06

0.08

0.10

0.12

0.14

0.2

0.4

0.6

0.8

Network Delta

96

98

100

102 0.04

0.06

0.08

0.10

0.12

0.14

0.1

0.2

0.3

0.4

0.5

0.6

0.7

0.8

Model Delta

96

98

100

102 0.04

0.06

0.08

0.10

0.12

0.14

0.10

0.08

0.06

0.04

0.02

0.00

0.02

0.04

Difference

- Figure 3. δtH,(1) and neural network approximation as a function of (st,vt) for t = 15 days

strategy yields smaller extreme losses (c.f. also the realized 99%-CVar loss value realized on the test sample, shown in the table below Figure 7).

To further illustrate the implications of risk-preferences on hedging, as a last example we consider selling a call-spread, i.e. Z = [(ST1 − K1)+ − (ST1 − K2)+]/(K2 − K1) for K1 < K2. Here we have chosen K1 = s0, K2 = 101. Proceeding as above, we compare the model hedge to the more risk-averse hedging strategies associated to α = 0.95 and α = 0.99. The strategies (on a grid of values for spot and variance) are shown in Figures 8 and 9. The model hedge would again correspond to α = 0.5. As one can see for higher levels of risk-aversion, the strategy ﬂattens. From a practical perspective, this precisely corresponds to a barrier shift, i.e. a more risk-averse hedge for a call spread

30000

recurrent

simpler

25000

20000

15000

10000

5000

0

3 2 1 0 1 2 3

### Figure 4. Comparison of recurrent and simpler network structure (no transaction costs).

16000

recurrent

simpler

14000

12000

10000

8000

6000

4000

2000

0

1 0 1 2 3 4 5 6

| |Mean Loss|Price|Realized CVar|
|---|---|---|---|
|recurrent|0.0018|5.5137|-0.0022|
|simpler|0.0022|6.7446|-0.0|

### Figure 5. Network architecture matters: Comparison of recurrent and simpler network structure (with transaction costs and 99%-CVar criterion).

30000 0.99-CVar

0.5-CVar

25000

20000

15000

10000

5000

0

3 2 1 0 1 2 3

- Figure 6. Comparison of 99%-CVar and 50%-CVar optimiality criterion.

| |Mean Loss|Realized 0.5-CVar|Realized 0.99-CVar|
|---|---|---|---|
|0.99-CVar|0.2635|0.527|1.8034|
|0.5-CVar|0.1514|0.2531|2.3631|

3 2 1 0 1 2

0

5000

10000

15000

20000

25000

0.99-CVar

0.5-CVar

- Figure 7. Comparison of 99%-CVar and 50%-CVar optimiality criterion, normalized to risk-neutral price.

with strikes K1 and K2 actually aims at hedging a spread with strikes K˜1 and K2 for K˜1 < K1.

- 5.3. Price asymptotics under proportional transaction costs. In Section 5.2 we have seen that in a market without transaction costs, deep hedging is able to recover the model hedge and can be used to calculate risk-adjusted optimal hedging strategies.

Spread Delta

Model Delta

0.18

0.25

0.16

0.20

0.14

0.12

0.15

0.10

0.10

0.08

0.06

0.05

0.04

0.14

0.14

0.12

0.12

0.10

0.10

0.08

0.08

96

96

98

98

0.06

0.06

100

100

102 0.04

102 0.04

Difference

0.04

0.02

0.00

0.02

0.04

0.06

0.08

0.14

0.12

0.10

0.08

96

98

0.06

100

102 0.04

- Figure 8. Call spread δtH,(1) and neural network approximation as a function of (st,vt) for t = 15 days

96

98

100

102 0.04

0.06

0.08

0.10

0.12

0.14

0.02

0.04

0.06

0.08

0.10

0.12

0.14

Spread Delta

96

98

100

102 0.04

0.06

0.08

0.10

0.12

0.14

0.05

0.10

0.15

0.20

0.25

Model Delta

96

98

100

102 0.04

0.06

0.08

0.10

0.12

0.14

0.125

0.100

0.075

0.050

0.025

0.000

0.025

0.050

Difference

- Figure 9. Call spread δtH,(1) and neural network approximation as a function of (st,vt) for t = 15 days

The goal of this section is to illustrate the power of the methodology by numerically calculating the indiﬀerence price (3.2) in a multi-asset market with transaction costs.

So far, this has been regarded a highly challenging problem, see e.g. the introduction of [KMK15]. For example, calculating the exponential utility indifference price for a call option in a Black-Scholes model involves solving a multidimensional nonlinear free boundary problem, see e.g. [HN89], [MHADZ93]. Motivated by this [WW97] have studied asymptotically optimal strategies and price asymptotics for small proportional transaction costs, i.e. for

- (5.7) ck(n) =

d

i=1

ε|ni|Ski and as ε ↓ 0. One of the results in the asymptotic analysis is that

- (5.8) pε − p0 = O(ε2/3), as ε ↓ 0,

- where pε = pε(Z) is the utility indiﬀerence price of Z associated to transaction costs of size ε. In fact (5.8) is true in more general one-dimensional models, see [KMK15], and the rate 2/3 also emerges in a variety of related problems with proportional transaction costs, see e.g. [Rog04], [JMKS17] and the references therein.

Here we numerically verify (5.8) using the deep hedging algorithm, ﬁrst for a Black-Scholes model (for which (5.8) is known to hold) and then for a Heston model (with d = 2 hedging instruments). For this latter case (or any other model with d > 1) there have been neither numerical nor theoretical results on (5.8) previously in the literature.

Black-Scholes model. Consider ﬁrst d = 1 and St = s0 exp(−tσ2/2 + σWt), where σ > 0 and W is a one-dimensional Brownian motion. We choose σ = 0.2, s0 = 100 and use the explicit form of S to generate sample trajectories. Setting Ik = log(Sk) and proceeding precisely as in the Heston case (see Sections 5.1 and 5.2), we may use the deep hedging algorithm to calculate the exponential utility indiﬀerence price pε for diﬀerent values of ε. Recall that we choose proportional transaction costs (5.7) and ρ is the entropic risk measure (3.4) (see Lemma 3.6). For the numerical example we take λ = 1 and Z = (ST −K)+ with K = s0 and we calculate pεi for εi = 2−i+5, i = 1,...,5.

- Figure 10 shows the pairs (log(εi),log(pεi −p0)) (in red) and the closest (in

squared distance) straight line with slope 2/3 (in blue). Thus, in this range of ε the relation log(pε − p0) = 2/3log(ε) + C for some C ∈ R indeed holds true and hence also (5.8).

Note that trading is only possible at discrete time-points and so the indiﬀerence price and the risk-neutral price do not coincide. Since (5.8) is a result for continuous-time trading (where q = p0), we have compared to the risk-neutral price q here (thus neglecting the discrete-time friction in pε for ε > 0).

Heston model. We now consider a Heston model with two hedging instruments, i.e. d = 2 and the setting is precisely as in Section 5.2, except that here ρ is chosen as (3.4) and proportional transaction costs (5.7) are incurred. Choosing λ = 1, Z = (ST1 −K)+ and εi as in the Black-Scholes case above, one can again calculate the exponential utility indiﬀerence prices and show the diﬀerence to p0 in a log-log plot (see above) in a graph. These are shown as red dots in

- Figure 11. Here the blue line in Figure 11 is the regression line, i.e. the least squares ﬁt of the red dots. The rate is very close to 2/3 and so it appears that the relation (5.8) also holds in this case.

- 5.4. High-dimensional example. As a last example consider a model built from 5 separate Heston models, i.e. d = 10 and (Sh,Sh+1) is the price process of spot and variance swap in a Heston model (speciﬁed by (5.2) and (5.4)) for h = 1,...,5. To have a benchmark at hand the 5 models are assumed independent and each of them has parameters as speciﬁed in Section 5.2. This choice is of course no restriction for the algorithm and is only made for convenience. The payoﬀ is a sum of call options on each of the underlyings, i.e.

Z = 5h=1 Zh with Zh = (ST2h−1 − K)+ and K = s0 = 100. In a market with continuous-time trading and no transaction costs, Z can be replicated perfectly

by trading according to strategy (5.6) in each of the models. In particular, this

Rate of convergence is 0.67

0.50

0.25

0.00

log()pp0

0.25

0.50

0.75

1.00

1.25

7.0 6.5 6.0 5.5 5.0 4.5

log( )

### Figure 10. Black-Scholes model price asymptotics.

Rate of convergence is 0.71

| | | | | | | | |
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

0.50

0.25

0.00

log()pp0

0.25

0.50

0.75

1.00

1.25

1.50

7.0 6.5 6.0 5.5 5.0 4.5

log( )

Figure 11. Heston model price asymptotics

strategy is decoupled, i.e. the optimal holdings in (Sh,Sh+1) only depend on (S(h),S(h+1)). While in the present setup trading is only possible at discrete time steps and so the strategy optimizing (3.1), where X = −Z, leads to a nondeterministic terminal hedging error (2.1), by independence one still expects that the optimal strategy is decoupled as above, at least for certain classes of risk measures. To see this most prominently, here we consider variance

optimal hedging: the objective is chosen as (3.3) for (x) = x2 and p0 = 5q,

- where q = E[Z1]. Let δ ∈ H and write δ(2h−1:2h) := (δ2h−1,δ2h) for h = 1,...,5 (and anal-

ogously for S). If δ is decoupled, i.e. such that δ(2h−1:2h) is independent of S(2j−1:2j) for j = h, then by independence and since S is a martingale one has

5

Var −Zi + (δ(2h−1:2h) · S(2h−1:2h))T .

- (5.9) E (−Z + p0 + (δ · S)T)2 =

h=1

By building δ from the (discrete-time) variance optimal strategies for each of the 5 models, one sees from (5.9) that the minimal value of (3.3) over all δ ∈ H is at most 5 times the minimal value of (3.3) associated to a single Heston model. This consideration serves as a guideline for assessing the approximation quality of the neural network strategy.

To assess the scalability of the algorithm, we now calculate the close-tooptimal neural network hedging strategy associated to (3.3) in both instances (i.e. for nH = 5 models and for a single one, nH = 1) and compare the results. Unless speciﬁed otherwise, the parameters are as in Section 5.1. Since for nH = 5 we are actually solving 5 problems at once, we allow for a network with more hidden nodes by taking N1 = N2 = 12nH. We then train both networks for a ﬁxed number of time-steps (here 2 × 105) and measure the performance in terms of both training time and realized loss (evaluated on a test set of nH × 105 sample paths): the training times on a standard Lenovo X1 Carbon laptop are 5.75 and 2.1 hours for nH = 5 and nH = 1, respectively and the realized losses are 1.13 and 0.20. In view of the considerations above, this indicates that the approximation quality is roughly the same for both instances (and close-to-optimal).

While far from a systematic study, this last example nevertheless demon-

strates the potential of the algorithm for high-dimensional hedging problems. 6. Disclaimer

Opinions and estimates constitute our judgement as of the date of this Material, are for informational purposes only and are subject to change without notice. This Material is not the product of J.P. Morgans Research Department and therefore, has not been prepared in accordance with legal requirements to promote the independence of research, including but not limited to, the prohibition on the dealing ahead of the dissemination of investment research. This Material is not intended as research, a recommendation, advice, oﬀer or solicitation for the purchase or sale of any ﬁnancial product or service, or to be used in any way for evaluating the merits of participating in any transaction. It is not a research report and is not intended as such. Past performance is not indicative of future results. Please consult your own advisors regarding legal, tax, accounting or any other aspects including suitability implications for your particular circumstances. J.P. Morgan disclaims any responsibility or liability whatsoever for the quality, accuracy or completeness of the information herein, and for any reliance on, or use of this material in any way. Important disclosures at: www.jpmorgan.com/disclosures

### References

[BK06] M. Broadie and O.¨ Kaya, Exact simulation of stochastic volatility and other aﬃne jump diﬀusion processes, Operations Research 54 (2006), no. 2, 217– 231.

[BR06] C. Burgert and L. Ru¨schendorf, Consistent risk measures for portfolio vectors, Insurance: Mathematics and Economics (2006), 289–297.

[BTT07] A. Ben-Tal and M. Teboulle, An old-new concept of convex risk measures: the optimized certainty equivalent, Mathematical Finance 17 (2007), no. 3, 449– 476.

[Duf01] D. Dufresne, The integrated square-root process, Centre for Actuarial Studies,

University of Melbourne, 2001, Research Paper no. 90. [Dup94] B. Dupire, Pricing with a smile, Risk 7 (1994), 18–20. [DZL09] X. Du, J. Zhai, and K. Lv, Algorithm trading using q-learning and recurrent

reinforcement learning, arxiv (2009), https://arxiv.org/pdf/1707.07338.pdf. [FL00] H. Fo¨llmer and P. Leukert, Eﬃcient hedging: Cost versus shortfall risk, Finance and Stochastics 4 (2000), 117–146. [FS16] H. Fo¨llmer and A. Schied, Stochastic ﬁnance: An introduction in discrete time, De Gruyter, 2016. [Gla04] P. Glasserman, Monte carlo methods in ﬁnancial engineering, Applications of mathematics : stochastic modelling and applied probability, Springer, 2004. [GS13] J. Gatheral and A. Schied, Dynamical models of market impact and algorithms for order execution, Handbook on Systemic Risk (2013), 579–599. [Hal17] I. Halperin, Qlbs: Q-learner in the black-scholes (-merton) worlds, arxiv (2017), https://arxiv.org/abs/1712.04609.

[HBP17] G. Kutyniok, H. Bo¨lcskei, P. Grohs and P. Petersen, Optimal approximation with sparsely connected deep neural networks, Preprint arXiv:1705.01714

(2017).

[HMSC95] S. E. Shreve, H. M. Soner and J. Cvitani´c, There is no nontrivial hedging portfolio for option pricing with transaction costs, The Annals of Applied Probability 5 (1995), no. 2, 327–355.

[HN89] S. Hodges and A. Neuberger, Optimal replication of contingent claims under transaction costs, The Review of Futures Markets 8 (1989), no. 2, 222–239. [Hor91] K. Hornik, Approximation capabilities of multilayer feedforward networks, Neural Networks 4 (1991), no. 2, 251–257.

[IAR09] M. Jonsson, A. Ilhan˙ and R. Sircar, Optimal static-dynamic hedges for exotic options under convex risk measures, Stochastic Processes and their Applications 119 (2009), no. 10, 3608 – 3632.

[IGC16] Y. Bengio, I. Goodfellow and A. Courville, Deep learning, MIT Press, 2016, http://www.deeplearningbook.org.

[IS15] S. Ioﬀe and C. Szegedy, Batch normalization: Accelerating deep network training by reducing internal covariate shift, Proceedings of the 32nd International Conference on Machine Learning, 2015, pp. 448–456.

[JMKS17] M. Reppen, J. Muhle-Karbe and H. M. Soner, A primer on portfolio choice with small transaction costs, Annual Review of Financial Economics 9 (2017), no. 1, 301–331.

[KB15] D. P. Kingma and J. Ba, Adam: a method for stochastic optimization, Proceedings of the International Conference on Learning Representations (ICLR)

(2015). [KMK15] J. Kallsen and J. Muhle-Karbe, Option pricing and hedging with small transaction costs, Mathematical Finance 25 (2015), no. 4, 702–723. [KS07] S. Klo¨ppel and M. Schweizer, Dynamic indiﬀerence valuation via convex risk measures, Mathematical Finance 17 (2007), no. 4, 599–627. [LBAK10] P. Ja¨ckel, L. B. G. Andersen and C. Kahl, Simulation of square-root processes, Encyclopedia of Quantitative Finance, John Wiley & Sons, Ltd, 2010. [Lu17] D. Lu, Agent inspired trading using recurrent reinforcement learning and lstm neural networks, arxiv (2017), https://arxiv.org/pdf/1707.07338.pdf.

[MHADZ93] V. G. Panas, M. H. A. Davis and T. Zariphopoulou, European option pricing with transaction costs, SIAM Journal on Control and Optimization 31 (1993), no. 2, 470–493.

[MW97] J. Moody and L. Wu, Optimization of trading systems and portfolios, Proceedings of the IEEE/IAFE 1997 Computational Intelligence for Financial Engineering (CIFEr) (1997), 300–307.

[PBV17] H. M. Soner, P. Bank and M. Voß, Hedging with temporary price impact, Mathematics and Financial Economics 11 (2017), no. 2, 215–239.

[Rog04] L. C. G. Rogers, Why is the eﬀect of proportional transaction costs O(δ2/3), Mathematics of Finance (G. Yin and Q. Zhang, eds.), American Mathematical Society, Providence, RI, 2004, pp. 303–308.

[RS10] L. C. G. Rogers and S. Singh, The cost of illiquidity and its eﬀects on hedging, Mathematical Finance 20 (2010), no. 4, 597–615.

[WW97] A. E. Whalley and P. Wilmott, An asymptotic analysis of an optimal hedging model for option pricing with transaction costs, Mathematical Finance 7 (1997), no. 3, 307–324.

[Xu06] M. Xu, Risk measure pricing and hedging in incomplete markets, Annals of Finance 2 (2006), no. 1, 51–71.

[ZJL17] D. Xu, Z. Jiang and J. Liang, A deep reinforcement learning framework for the ﬁnancial portfolio management problem, arxiv (2017), https://arxiv.org/abs/1706.10059.

Hans Buhler,¨ J.P. Morgan, London E-mail address: hans.buehler@jpmorgan.com

Lukas Gonon, Eidgenossische¨ Technische Hochschule Zurich,¨ Switzerland E-mail address: lukas.gonon@math.ethz.ch

Josef Teichmann, Eidgenossische¨ Technische Hochschule Zurich,¨ Switzerland E-mail address: josef.teichmann@math.ethz.ch

Ben Wood, J.P. Morgan, London E-mail address: ben.wood@jpmorgan.com

