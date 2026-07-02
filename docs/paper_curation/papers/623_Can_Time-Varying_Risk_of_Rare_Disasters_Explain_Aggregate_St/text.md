NBER WORKING PAPER SERIES

CAN TIME-VARYING RISK OF RARE DISASTERS EXPLAIN AGGREGATE STOCK MARKET VOLATILITY?

Jessica Wachter Working Paper 14386 http://www.nber.org/papers/w14386

NATIONAL BUREAU OF ECONOMIC RESEARCH 1050 Massachusetts Avenue Cambridge, MA 02138 October 2008

For helpful comments, I thank Robert Barro, John Campbell, Mikhail Chernov, Gregory Du˙ee, Xavier Gabaix, Paul Glasserman, Francois Gourio, Dana Kiku, Bruce Lehmann, Christian Juillard, Monika Piazzesi, Nikolai Roussanov, Jerry Tsai, Pietro Veronesi and seminar participants at the 2008 NBER Summer Institute, the 2008 SED Meetings, the 2011 AFA Meetings, Brown University, the Federal Reserve Bank of New York, MIT, University of Maryland and the Wharton School. I am grateful for financial support from the Aronson+Johson+Ortiz fellowship through the Rodney L. White Center for Financial Research. Thomas Plank and Leonid Spesivtsev provided excellent research assistance. The views expressed herein are those of the author(s) and do not necessarily reflect the views of the National Bureau of Economic Research.

NBER working papers are circulated for discussion and comment purposes. They have not been peerreviewed or been subject to the review by the NBER Board of Directors that accompanies official NBER publications.

© 2008 by Jessica Wachter. All rights reserved. Short sections of text, not to exceed two paragraphs, may be quoted without explicit permission provided that full credit, including © notice, is given to the source.

Can Time-Varying Risk of Rare Disasters Explain Aggregate Stock Market Volatility? Jessica Wachter NBER Working Paper No. 14386 October 2008, Revised May 2011, Revised March 2012 JEL No. G12

### ABSTRACT

Why is the equity premium so high, and why are stocks so volatile? Why are stock returns in excess of government bill rates predictable? This paper proposes an answer to these questions based on a time-varying probability of a consumption disaster. In the model, aggregate consumption follows a normal distribution with low volatility most of the time, but with some probability of a consumption realization far out in the left tail. The possibility of this poor outcome substantially increases the equity premium, while time-variation in the probability of this outcome drives high stock market volatility and excess return predictability.

Jessica Wachter Department of Finance 2300 SH-DH The Wharton School University of Pennsylvania 3620 Locust Walk Philadelphia, PA 19104 and NBER jwachter@wharton.upenn.edu

# 1 Introduction

The magnitude of the expected excess return on stocks relative to bonds (the equity premium) constitutes one of the major puzzles in ﬁnancial economics. As Mehra and Prescott (1985) show, the ﬂuctuations observed in the consumption growth rate over U.S. history predict an equity premium that is far too small, assuming reasonable levels of risk aversion.1 One proposed explanation is that the return on equities is high to compensate investors for the risk of a rare disaster (Rietz (1988)). An open question has therefore been whether the risk is suﬃciently high, and the rare disaster suﬃciently severe, to quantitatively explain the equity premium. Recently, however, Barro (2006) shows that it is possible to explain the equity premium using such a model when the probability of a rare disaster is calibrated to international data on large economic declines.

While the models of Rietz (1988) and Barro (2006) advance our understanding of the equity premium, they fall short in other respects. Most importantly, these models predict that the volatility of stock market returns equals the volatility of dividends. Numerous studies have shown, however, that this is not the case. In fact, there is excess stock market volatility; the volatility of stock returns far exceeds that of dividends (e.g. Shiller (1981), LeRoy and Porter (1981), Keim and Stambaugh (1986), Campbell and Shiller (1988), Cochrane (1992), Hodrick (1992)). While the models of Barro and Rietz address the equity premium puzzle, they do not address this volatility puzzle.

In the original model of Barro (2006), agents have power utility and the endowment process is subject to large and relatively rare consumption declines (disasters). This paper proposes two modiﬁcations. First, rather than being constant, the probability of a disaster is stochastic and varies over time. Second, the representative agent, rather than having power utility preferences, has recursive preferences. I show that such a model can generate volatility of stock returns close to that in the data at reasonable values of the underlying parameters. Moreover, the model implies reasonable values for the mean and volatility of

1Campbell (2003) extends this analysis to multiple countries.

the government bills.

Both time-varying disaster probabilities and recursive preferences are necessary to ﬁt the model to the data. The role of time-varying disaster probabilities is clear, the role of recursive preferences perhaps less so. Recursive preferences, introduced by Kreps and Porteus (1978) and Epstein and Zin (1989) retain the appealing scale-invariance of power utility, but allow for separation between the willingness to take on risk and the willingness to substitute over time. Power utility requires that these are driven by the same parameter, leading to the counterfactual prediction that a high price-dividend ratios predicts a high excess return. Increasing the agent’s willingness to substitute over time reduces the eﬀect of the disaster probability on the riskfree rate. With recursive preferences, this can be accomplished without simultaneously reducing the agent’s risk aversion.

The model in this paper allows for time-varying disaster probabilities and recursive utility with unit elasticity of intertemporal substitution (EIS). The assumption that the EIS is equal to 1 allows the model to be solved in closed form up to an indeﬁnite integral. A time-varying disaster probability is modeled by allowing the intensity for jumps to follow a square-root process (Cox, Ingersoll, and Ross (1985)). The solution for the model reveals that allowing the probability of a disaster to vary not only implies a time-varying equity premium, it also increases the level of the equity premium. The dynamic nature of the model therefore leads the equity premium to be higher than what static considerations alone would predict.

This model can quantitatively match high equity volatility and the predictability of excess stock returns by the price-dividend ratio. Generating long-run predictability of excess stock returns without generating counterfactual long-run predictability in consumption or dividend growth is a central challenge for general equilibrium models of the stock market. This model meets the challenge: while stock returns are predictable, consumption and dividend growth are only predictable ex post if a disaster actually occurs. Because disasters occur rarely, the amount of consumption predictability is quite low, just as in the data. A second challenge for models of this type is to generate volatility in stock returns without counterfactual volatility in the government bill rate. This model meets this challenge as well. The model is capable

of matching the low volatility of the government bill rate because of two competing eﬀects. When the risk of a disaster is high, rates of return fall because of precautionary savings. However, the probability of government default (either outright or through inﬂation) rises. Investors therefore require greater compensation to hold government bills.

As I describe above, adding dynamics to the rare disaster framework allows for a number of new insights. Note however, that the dynamics in this paper are relatively simple. A single state variable (the probability of a rare disaster) drives all of the results in the model. This is parsimonious, but also unrealistic: it implies, for instance, that the price-dividend ratio and the riskfree rate are perfectly negatively correlated. It also implies a degree of co-movement among assets that would not hold in the data. In Section 2.4, I suggest ways in which this weakness might be overcome while still maintaining tractability.

Several recent papers also address the potential of rare disasters to explain the aggregate stock market. Gabaix (2008a) assumes power utility for the representative agent, while also assuming the economy is driven by a linearity-generating process (see Gabaix (2008b)) that combines time-variation in the probability of a rare disaster with time-variation in the degree to which dividends respond to a disaster. This set of assumptions allows him to derive closed-form solutions for equity prices as well as prices for other assets. In Gabaix’s numerical calibration, only the degree to which dividends respond to the disaster varies over time. Therefore the economic mechanism driving stock market volatility in Gabaix’s model is quite diﬀerent than the one considered here. Barro (2009) and Martin (2008) propose models with a constant disaster probability and recursive utility. In contrast, the model considered here focuses on the case of time-varying disaster probabilities. Longstaﬀ and Piazzesi (2004) propose a model in which consumption, and the ratio between consumption and the dividend are hit by contemporaneous downward jumps; the ratio between consumption and dividends then reverts back to a long-run mean. They assume a constant jump probability and power utility. In contemporaneous independent work, Gourio (2008b) speciﬁes a model in which the probability of a disaster varies between two discrete values. He solves this model numerically assuming recursive preferences. A related approach is taken by Veronesi (2004), who assumes

that the drift of dividends follows a Markov switching process, with a small probability of falling into a low state. While the physical probability of a low state is constant, the representative investor’s subjective probability is time-varying due to learning. Veronesi assumes exponential utility; this allows for the inclusion of learning but makes it diﬃcult to assess the magnitude of the excess volatility generated through this mechanism.

In this paper, the conditional distribution of consumption growth becomes highly nonnormal when a disaster is relatively likely. Thus the paper also relates to a literature that examines the eﬀects of non-normalities on risk premia. Harvey and Siddique (2000) and Dittmar (2002) examine the role of higher-order moments on the cross-section; unlike the present paper they take the market return as a given. Similarly to the present paper, Weitzman (2007) constructs an endowment economy with non-normal consumption growth. His model diﬀers from the present one in that he assumes independent and identically distributed consumption growth (with a Bayesian agent learning about the unknown variance), and he focuses on explaining the equity premium.

Finally, this paper draws on a literature that derives asset pricing results assuming endowment processes that include jumps, with a focus on option pricing (an early reference is Naik and Lee (1990)). Liu, Pan, and Wang (2005) consider an endowment process in which jumps occur with a constant intensity; their focus is on uncertainty aversion but they also consider recursive utility. My model departs from theirs in that the probability of a jump varies over time. Drechsler and Yaron (2011) show that a model with jumps in the volatility of the consumption growth process can explain the behavior of implied volatility and its relation to excess returns. Eraker and Shaliastovich (2008) also model jumps in the volatility of consumption growth; they focus on ﬁtting the implied volatility curve. Both papers assume of EIS greater than one and derive approximate analytical and numerical solutions. Santa-Clara and Yan (2006) consider time-varying jump intensities, but restrict attention to a model with power utility and implications for options. In contrast, the model considered here focuses on recursive utility and implications for the aggregate market.

# 2 Model

## 2.1 Assumptions

I assume an endowment economy with an inﬁnitely-lived representative agent. This set-up is standard, but I assume a novel process for the endowment. Aggregate consumption (the endowment) solves the following stochastic diﬀerential equation

dCt = µCt− dt + σCt− dBt + (eZ

t

− 1)Ct− dNt, (1)

where Bt is a standard Brownian motion and Nt is a Poisson process with time-varying intensity λt.2 This intensity follows the process

dλt = κ(λ¯ − λt)dt + σλ λt dBλ,t, (2)

where Bλ,t is also a standard Brownian motion, and Bt, Bλ,t and Nt are assumed to be independent. I assume Zt is a random variable whose time-invariant distribution ν is independent of Nt, Bt and Bλ,t. I use the notation Eν to denote expectations of functions of Zt taken with respect to the ν-distribution. The t subscript on Zt will be omitted when not essential for clarity.

Assumptions (1) and (2) deﬁne Ct as a mixed jump-diﬀusion process. The diﬀusion term µCt− dt + σCt− dBt represents the behavior of consumption in normal times, and implies that, when no disaster takes place, log consumption growth over an interval ∆t is normally distributed with mean (µ− 12σ2)∆t and variance σ2∆t. Disasters are captured by the Poisson process Nt, which allows for large instantaneous changes (“jumps”) in Ct. Roughly speaking, λt can be thought of as the disaster probability over the course of the next year.3 In what

- 2In what follows, all processes will be right continuous with left limits. Given a process xt, the notation xt− will denote lims↑t xs, while xt denotes lims↓t xs.
- 3More precisely, the probability of k jumps over the course of a short interval ∆t is approximately equal to e−λ

t∆t (λt∆t)k

k! , where t will be measured in units of years. In the calibrations that follow, the average value of λt will be 0.0355, implying a 0.0249 probability of a single jump over the course of a year, a 0.00044 probability of two jumps, and so forth.

follows, I will refer to λt either as the disaster intensity or the disaster probability depending on the context; these terms should be understood to have the same meaning. The instantaneous change in log consumption, should a disaster occur, is given by Zt. Because the focus of the paper is on disasters, Zt will be assumed to be negative throughout.

In the model, a disaster is therefore a large negative shock to consumption. The model is silent on the reason for such a decline in economic activity; examples include a fundamental change in government policy, a war, a ﬁnancial crisis and a natural disaster. Given this paper’s focus on time-variation in the likelihood of a disaster, it is probably most realistic to think of the disaster as caused by human beings (namely, the ﬁrst three examples given above, rather than a natural disaster). The recent ﬁnancial crisis in the United States illustrates such time-variation: Following the series of events in the fall of 2008, there was much discussion of a second Great Depression, brought on by a freeze in the ﬁnancial system. The conditional probability of a disaster seemed higher, say, than in 2006.

As Cox, Ingersoll, and Ross (1985) discuss, the solution to (2) has a stationary distribution provided that κ > 0 and λ¯ > 0. This stationary distribution is Gamma with shape parameter 2κλ/σ¯ λ2 and scale parameter σλ2/(2κ). If 2κλ¯ > σλ2, the Feller condition4 is satisﬁed, implying a ﬁnite density at zero. The top panel of Figure 1 shows the probability density function corresponding to the stationary distribution. The bottom panel shows the probability that λt exceeds x as a function of x (the y-axis uses a log scale). That is, the panel shows the diﬀerence between 1 and the cumulative distribution function for λt. As this ﬁgure shows, the stationary distribution of λt is highly skewed. The skewness arises from the square root term multiplying the Brownian shock in (2): This square root term implies that high realizations of λt make the process more volatile, and thus further high realizations more likely than they would be under a standard auto-regressive process. The model therefore implies that there are times when “rare” disasters can occur with high probability, but that these times are themselves unusual.

I assume the continuous-time analogue of the utility function deﬁned by Epstein and

4from Feller (1951)

Zin (1989) and Weil (1990), that generalizes power utility to allow for preferences over the timing of the resolution of uncertainty. The continuous-time version is formulated by Duﬃe and Epstein (1992); I make use of a limiting case of their model that sets the parameter associated with the intertemporal elasticity of substitution equal to one. Deﬁne the utility function Vt for the representative agent using the following recursion:

Vt = Et

∞

f(Cs,Vs)ds, (3)

t

where

1 1 − γ

f(C,V ) = β(1 − γ)V log C −

log((1 − γ)V ) . (4)

Note that Vt represents continuation utility, i.e. utility of the future consumption stream. The parameter β is the rate of time preference. I follow common practice in interpreting γ as relative risk aversion. As γ approaches one, (4) can be shown to be ordinally equivalent to logarithmic utility. I assume throughout that β > 0 and γ > 0. Most of the discussion will focus on the case of γ > 1.

## 2.2 The value function and the riskfree rate

Let W denote the wealth of the representative agent and J(W,λ) the value function. In equilibrium, it must be the case that J(Wt,λt) = Vt. Conjecture that the price-dividend ratio for the consumption claim is constant. Namely, let St denote the value of a claim to aggregate consumption, then

St Ct

= l. (5)

for some constant l.5 The process for consumption and the conjecture (5) imply that St satisﬁes

dSt = µSt− dt + σSt− dBt + (eZ

t

− 1)St− dNt. (6)

Let rt denote the instantaneous riskfree rate.

5Indeed, the fact that St/Ct is constant (and equal to 1/β) arises from the assumption of unit EIS, and is independent of the details of the model (see, e.g., Weil (1990)).

To solve for the value function, consider the Hamilton-Jacobi-Bellman equation for an investor who allocates wealth between St and the riskfree asset. Let αt be the fraction of wealth in the risky asset St, and (with some abuse of notation), let Ct be the agent’s consumption. Wealth follows the process

dWt = Wt−αt(µ − rt + l−1) + Wt−rt − Ct− dt + Wt−αtσ dBt + αt(eZ

t

− 1)Wt− dNt.

At the optimum, the instantaneous expected change in the value function, plus ﬂow utility must equal zero (Duﬃe and Epstein (1992)). That is, optimal consumption and portfolio choice must satisfy the equation:

sup

αt,Ct

JW Wtαt(µ − rt + l−1) + Wtrt − Ct + Jλκ(λ¯ − λt)+

- 1

- 2

- 1

- 2

JWWWt2αt2σ2 +

Jλλσλ2λt + λtEν J(Wt(1 + αt(eZ

− 1)),λt) − J(Wt,λt)

t

+f(Ct,J) = 0, (7) where Ji denotes the ﬁrst derivative of J with respect to variable i, for i equal to λ or W, and Jij the second derivative of J with respect to i and j. Note that the instantaneous return on wealth invested in the risky asset is determined by the dividend yield l−1 as well as by the change in price. Note also that the instantaneous expected change in the value function is given by the continuous drift plus the expected change due to jumps.

As Appendix A.1 shows, the form of the value function and the envelope condition fC = JW imply that that the wealth-consumption ratio l = β−1. Moreover, the value function takes the form

W1−γ 1 − γ

J(W,λ) =

I(λ). (8) The function I(λ) is given by

I(λ) = ea+bλ, (9) where

- a =

1 − γ β

µ −

- 1

- 2

γσ2 + (1 − γ)log β + b

κλ¯ β

, (10)

- b =

κ + β σλ2 −

2

Eν [e(1−γ)Z − 1] σλ2

κ + β σλ2

− 2

. (11)

It follows from (11) that, for γ > 1, b > 0.6 Therefore, by (8), an increase in disaster risk reduces utility for the representative agent. As Section 2.4 shows, the price of the dividend claim falls when the disaster probability rises. The agent requires compensation for this risk (because utility is recursive, marginal utility depends on the value function), and thus time-varying disaster risk increases the equity premium.

Appendix A.1 shows that the riskfree rate is given by

rt = β + µ − γσ2

standard model

+ λtEν e−γZ eZ − 1

disaster risk

. (12)

The term above the ﬁrst bracket in (12) is the same as in the standard model without disaster risk; β represents the reﬂects the role of discounting, µ intertemporal smoothing and γ precautionary savings. The term multiplying λt in (12) arises from the risk of a disaster. Because eZ < 1, the riskfree rate is decreasing in λ. An increase in the probability of a rare disaster increases the representative agent’s desire to save, and thus lowers the riskfree rate. The greater is risk aversion, the greater is this eﬀect.

## 2.3 Risk of default

Disasters often coincide with at least a partial default on government securities. This point is of empirical relevance if one tries to match the behavior of the riskfree asset to the rate of return on government securities in the data. I therefore allow for partial default on government debt, and consider the rate of return on this defaultable security. I assume that, in the event of disaster, there will be a default on government liabilities with probability q. I follow Barro (2006) in assuming that in the event of default, the percent loss is equal to the percent fall in consumption.

Speciﬁcally, let rtL denote the interest rate that investors would receive if default does not occur. As shown in Appendix A.5, the equilibrium relation between rtL and rt is

rtL = rt + λtqEν e−γZ

t

6Note that κ > 0 and β > 0 are standing assumptions.

1 − eZ . (13)

Let rb denote the instantaneous expected return on government debt. Then rtb = rtL + λtqEν eZ − 1 , so

rtb = rt + λtqEν (e−γZ

− 1) 1 − eZ . (14) The second term in (14) has the interpretation of a disaster risk premium: the percent change in marginal utility is multiplied by the percent loss on the asset. An analogous term will appear in the expression for the equity premium below. Figure 3 shows the face value of government debt, rtL, the instantaneous expected return on government debt rtb and the riskfree rate rt as a function of λt. Because of the required compensation for default, rtL lies above rt. The expected return lies between the two because the actual cash ﬂow that investors receive from the government bill will be below rtL if default occurs.

t

All three rates decrease in λt because, at these parameter values, a higher λt induces a greater desire to save. However, rtL and rtb are less sensitive to changes in λ than rt because of an opposing eﬀect: the greater is λt, the greater is the risk of default, and therefore the greater the return investors demand for holding the government bill. Because of a small cash ﬂow eﬀect, rtb decreases more than rtL, but still less than rt.

## 2.4 The dividend claim

This section describes prices and expected returns on the aggregate stock market. Let Dt denote the dividend. I model dividends as levered consumption, i.e. Dt = Ctφ as in Abel (1999) and Campbell (2003). Ito’s Lemma implies

dDt Dt−

= µD dt + φσ dBt + (eφZ

t

− 1)dNt, (15)

where µD = φµ + 21φ(φ − 1)σ2. For φ > 1, dividends fall by more than consumption in the event of a disaster. This is consistent with the U.S. experience (for which accurate data on dividends are available) as discussed in Longstaﬀ and Piazzesi (2004).

While dividends and consumption are driven by the same shocks, (15) does allow dividends and consumption to wander arbitrarily far from one another. This could be avoided by modeling the consumption-dividend ratio as a stationary but persistent process, as in,

e.g. Lettau and Ludvigson (2005), Longstaﬀ and Piazzesi (2004) and Menzly, Santos, and Veronesi (2004). In order to focus on the novel implications of time-varying disaster risk, I do not take this route here.

It is convenient to price the claim to aggregate dividends by ﬁrst calculating the stateprice density. Unlike the case of time-additive utility, the case of recursive utility implies that the state-price density depends on the value function. In particular, Duﬃe and Skiadas (1994) show that the state-price density πt is equal to

πt = exp

t

fV (Cs,Vs)ds fC(Ct,Vt), (16)

0

where fC and fV denote derivatives of f with respect to the ﬁrst and second argument respectively.

Let Ft = F(Dt,λt) denote the price of the claim to future dividends. Absence of arbitrage then implies that Ft is the integral of future dividend ﬂow, discounted using the state-price density:

∞

- πs

- πt

F(Dt,λt) = Et

Ds ds . (17) Deﬁne a function representing a single term in this integral:

t

H(Dt,λt,s − t) = Et

- πs

- πt

Ds .

Then

F(Dt,λt) =

∞

H(Dt,λt,τ)dτ.

0

The function H(Dt,λt,τ) has an interpretation: It is the price today of a claim to the dividend paid τ years in the future. Appendix A.3 shows that H takes a simple exponential form:

H(Dt,λt,τ) = exp{aφ(τ) + bφ(τ)λt}Dt

and that the functions aφ(τ) and bφ(τ) have solutions

- aφ(τ) = µD − µ − β + γσ2(1 − φ) −

κλ¯ σλ2

(ζφ + bσλ2 − κ) τ

−

2κλ¯ σλ2

log

(ζφ + bσλ2 − κ) e−ζ

φτ − 1 + 2ζφ 2ζφ

(18)

- bφ(τ) =

2Eν e(1−γ)Z − e(φ−γ)Z 1 − e−ζ

φτ

, (19)

(ζφ + bσλ2 − κ)(1 − e−ζφτ) − 2ζφ

where

ζφ = (bσλ2 − κ)2 + 2Eν [e(1−γ)Z − e(φ−γ)Z]σλ2. (20) Appendix A.3 discusses further properties of interest, such as existence, sign and convergence as τ approaches inﬁnity. In particular, for φ > 1, aφ(τ) and bφ(τ) are well-deﬁned for all values of τ. Moreover, bφ(τ) is negative. The sign of bφ(τ) is of particular importance for the model’s empirical implications. Negative bφ(τ) implies that when risk premia are high (namely when disaster risk is high), valuations are low. Thus the price-dividend ratio (which is F(D,λ,τ) divided by the aggregate dividend D) predicts realized excess returns with a negative sign.

The fact that higher risk premia go along with lower prices would seem like a natural implication of the model. After all, don’t higher risk premia imply higher discount rates, and don’t higher discount rates imply lower prices? The problem with this argument is that it ignores the eﬀect of disaster risk on the riskfree rate. As shown in Section 2.2, higher disaster risk implies a lower riskfree rate. As is true more generally for dynamic models of the price-dividend ratio (Campbell and Shiller (1988)), the net eﬀect depends on the interplay of three forces: the eﬀect of the disaster risk on risk premia, on the riskfree rate and on future cash ﬂows. A precise form of this statement is given in Section 2.6.

The result that bφ(τ) is negative implies that, indeed, the risk premium and cash ﬂow eﬀect dominate the riskfree rate eﬀect. Thus the price-dividend ratio will predict excess returns with the correct sign. Appendix A.3 shows that this is true in general for reasonable values of the parameters, namely for φ > 1. Section 2.7 contrasts this result with what holds in a dynamic model with power utility.

The results in this section also suggest the following testable implications: Stock market valuations should fall when the risk of a rare disaster rises. The risk of a rare disaster is unobservable, but, given a comprehensive data set, one can draw conclusions based on disasters that have actually occurred. This is important because it establishes independent evidence for the mechanism in the model.

Speciﬁcally, Barro and Ursua (2009) address the question: Given a large decline in the stock market, how much more likely is a decline in consumption than otherwise? Barro and Ursua augment the data set of Barro and Ursua (2008) with data on national stock markets. They look at cumulative multi-year returns on stocks that coincide with macroeconomic contractions. Their sample has 30 countries and 3037 annual observations; there are 232 stock-market crashes (deﬁned as cumulative returns of -25%) and 100 macroeconomic contractions (deﬁned as the average of the decline in consumption and in GDP). There is a 3.8% chance of moving from “normalcy” into a state with a contraction of 10% or more. This number falls to 1%, if one conditions on a lack of a stock market crash. If one considers major depressions (deﬁned as a decline in fundamentals of 25% or more), there is a 0.89% chance of moving from normalcy into a depression. Conditioning on no stock market crash reduces the probability to 0.07%.

Also closely related is recent work by Berkman, Jacobsen, and Lee (2010), who study the correlation between political crises and stock returns. Berkman et al. make use of the International Crisis Behavior (ICB) database, a detailed database of international political crises occurring during the period 1918–2006. Rather than dating the start of a crisis with a military action itself, the database identiﬁes a start of a crisis with with a change in the probability of a threat.7 A regression of the return on the world market on the number of such crises in a given month yields a coeﬃcient that is negative and statistically signiﬁcant. Results are particularly strong for the starting year of a crisis, for violent crises, and for crises rated as most severe. The authors also ﬁnd a statistically signiﬁcant eﬀect on valuations:

7See Berkman et al. for a discussion of the prior empirical literature on the relation between political instability and stock market returns.

the correlation between the number of crises and the earnings-price ratio on the S&P 500 is positive and statistically signiﬁcant, as is the correlation between the crisis severity index and the earnings-price ratio. Similar results hold for the dividend yield.

Comparing the results in this section and in Section 2.2 indicate that both the riskfree rate and the price-dividend ratio are driven by the disaster probability λt; this follows from the fact that there is a single state variable. This perfect correlation could be broken by assuming that consumption is subject to two types of disaster, each with its own time-varying intensity, and further assuming that one type has a stronger eﬀect on dividends (as modeled through high φ) than the other. The real interest rate and the price-dividend ratio would be correlated with both intensities, but to diﬀerent degrees, and thus would not be perfectly correlated with one another. The correlation between nominal rates and the price-dividend ratio could be further reduced by introducing a third type of consumption disaster. The three types could diﬀer across two dimensions: the impact on dividends and the impact on expected inﬂation. The expected inﬂation process would aﬀect the prices of nominal bonds but would not (directly) aﬀect stocks. I conjecture that the generalized model could be constructed to be as tractable as the present one.

## 2.5 The equity premium

The equity premium arises from the co-movement of the agent’s marginal utility with the price process for stocks. There are two sources of this co-movement: Co-movement during normal times (diﬀusion risk), and co-movement in times of disaster (jump risk). Ito’s Lemma implies that F satisﬁes the following:

dFt Ft−

= µF,t dt + σF,t[dBt dBλ,t] + (eφZ − 1)dNt, (21) for processes µF,t and σF,t. It is helpful to deﬁne notation for the price dividend ratio. Let

∞

exp{aφ(τ) + bφ(τ)λ} dτ. (22) Then

G(λ) =

0

σF,t = φσ (G (λt)/G(λt))σλ λt . (23)

Ito’s Lemma also implies

dπt πt−

= µπ,t dt + σπ,t[dBt dBλ,t] + (e−γZ

t

− 1)dNt, (24)

where

σπ,t = −γσ bσλ λt (25) as shown in Appendix A.2. Finally, deﬁne

Dt Ft

rte = µF,t +

+ λtEν eφZ − 1 . (26)

Then rte can be understood to be the instantaneous return on equities.8 The instantaneous equity premium is therefore rte − rt.

Appendix A.4 shows that the equity premium can be written as

rte − rt = −σπ,tσ F,t + λtEν (e−γZ − 1)(1 − eφZ) (27) The ﬁrst term represents the portion of the equity premium that is compensation for diﬀusion risk (which includes time-varying λt). The second term is the compensation for jump risk. While the diﬀusion term represents the co-movement between the state-price density and prices during normal times, the jump risk term shows the co-movement between the stateprice density and prices during disasters. That is,

πt − πt− πt− for a time t such that a jump takes place. Substituting (23) into (27) implies

Ft − Ft− Ft−

Eν (e−γZ − 1)(1 − eφZ) = −Eν

rte − rt = φγσ2

standard model

G G

bσλ2 + λtEν (e−γZ − 1)(1 − eφZ)

− λt

static disaster risk time-varying disaster risk

##### (28)

8The ﬁrst term in (26)) is the percentage drift in prices, the second term is the instantaneous dividend yield, and the third term is the expected decline in prices in the event of a disaster. The ﬁrst plus the third term constitutes the expected percentage change in prices.

The ﬁrst and third terms are analogous to expressions in Barro (2006): the ﬁrst term is the equity premium in the standard model with normally distributed consumption growth, while the third term arises from the (static) risk of a disaster. The second term is new to the dynamic model. This is the risk premium due to time variation in disaster risk. Because bφ is negative, G is also negative. Moreover, b is positive, so this term represents a positive contribution to the equity premium. Because both the second and the third terms are positive, an increase in the risk of rare disaster increases the equity premium.9

The instantaneous equity premium relative to the government bill rate is equal to (28) minus the default premium rtb − rt (given in (14)):

G G

rte − rtb = φγσ2 − λt

bσλ2 + λtEν e−γZ − 1 (1 − q) 1 − eφZ + q eZ − eφZ . (30)

The last term in (30) takes the usual form for the disaster risk premium: the percent change in marginal utility is multiplied by the percent loss. Here, with probability q, the expected loss on equity relative to bonds is reduced because both assets perform poorly. This instantaneous equity premium is shown in Figure 4 (solid line). The diﬀerence between the dashed line and the solid line represents the component of the equity premium that is new to the dynamic model, and shows that this term is large. The dotted line represents the equity premium in the standard diﬀusion model without disaster risk and is negligible compared with the disaster risk component. Figure 4 shows that the equity premium is increasing with the disaster risk probability.

Equation (30) and Figure 4 show that the return required for holding equity increases with the probability of a disaster. How does it depend on a more traditional measure of risk, namely the equity volatility? When there is no disaster, instantaneous volatility can be

9Also of interest is the equity premium conditional on no disasters, which is equal to (28) less the component due to jumps in the realized return (see Equation 26). This conditional equity premium is given by

G G

bσλ2 + λtEν e−γZ(1 − eφZ) . (29)

rte − rt − λtEν[eφZ − 1] = φγσ2 − λt

##### computed directly from (23):

σF,tσ F,t

- 1

- 2

= φ2σ2 +

G (λt) G(λt)

2

σλ2λt

- 1

- 2

.

Figure 5 shows that volatility is an increasing and concave function of the disaster probability. When the probability of a disaster is close to zero, the variance in the disaster probability is also very small. Thus the volatility is close to that of the dividend claim in non-disaster periods (φσ). As the risk of a rare disaster increases, so does the volatility of the disaster process. The increase in risk rises (approximately) with the square root of λ. Because the equity price falls when the disaster probability increases, the model is consistent with the “leverage eﬀect” found by Black (1976), Schwert (1989) and Nelson (1991).

The above equations show that an increase in the equity premium is accompanied by an increase in volatility. The net eﬀect of a change in λ on the Sharpe ratio (the equity premium divided by the volatility) is shown in Figure 6. Bad times, interpreted in this model as times with high probability of disaster, are times when the investors demand a higher risk-return tradeoﬀ than usual. Harvey (1989) and subsequent papers report empirical evidence that the Sharpe ratio indeed varies countercyclically. Like the model of Campbell and Cochrane (1999), this model is consistent with this evidence.

The time-varying disaster risk model generates a countercyclical Sharpe ratio through two mechanisms. First, the value function varies with λt: when disaster risk is high, investors require a greater return on all assets with prices negatively correlated with λ. The component of the equity premium associated with time-varying λt thus rises linearly with λ while the volatility rises only with the square root. Second, the component of the equity premium corresponding to disaster risk itself (the last term in (30)) has no counterpart in volatility. This term compensates equity investors for negative events that are not captured by the standard deviation of returns.

## 2.6 Zero-coupon equity

In order to understand the dynamics of the price-dividend ratio, it is helpful to think of the aggregate as being composed of components that pay a dividend at a speciﬁc point in time, namely, zero-coupon equity.

Recall that

H(Dt,λt,T − t) = exp{aφ(τ) + bφ(τ)λt}Dt is the time-t price of the claim that pays the aggregate dividend at time t+τ. Appendix A.3 shows that the risk premium on the zero-coupon claim with maturity τ is equal to

rte,(τ) − rt = φγσ2 − λtσλ2bφ(τ)b + λtEν (e−γZ − 1)(1 − eφZ) . (31) Like the equity premium, the risk premium on zero-coupon equity is positive and increasing in λt.

Zero-coupon equity can help answer the question of why the price-dividend ratio on the aggregate market is decreasing in λt. Because bφ(0) = 0, the question can be restated as: why is b φ(τ) negative for small values of τ?10 The diﬀerential equation for bφ(τ) is given by (A.27). Evaluating at zero yields:

b φ(0) = Eν e(φ−γ)Z − e(1−γ)Z

= −Eν e−γZ(eZ − 1)

− Eν (e−γZ − 1)(1 − eφZ)

equity premium

riskfree rate

+ Eν eφZ − 1

(32).

expected future dividends

Equation (32) shows that the change in bφ(τ) can be written in terms of risk premium, riskfree rate and cash ﬂow eﬀects. The ﬁrst term multiplies λt in the equation for the riskfree rate (12). The second term multiplies λt in the equation for the risk premium (31) in the limit as τ approaches zero. The third term represents the eﬀect of change in λt on expected future dividends: eφZ − 1 is the percent change in dividends in the event of a disaster. The

10This restatement relies on the fact that bφ(τ) is monotonically decreasing. It is, because as τ increases, e−ζ

φτ falls and 1 − e−ζ

φτ rises. The numerator of (19) therefore rises. In the denominator, the term (ζφ + bσλ2 − κ) 1 − e−ζ

φτ rises, and so the denominator falls in absolute value.

terms corresponding to the riskfree rate and the risk premium enter with negative signs, because higher discount rates reduce the price. Expected future dividend growth enters with a positive sign because higher expected cash ﬂows raise the price. Indeed, the term corresponding to the equity premium and to expected future dividends together exceed that of the riskfree rate when φ > 1.

As explained in the paragraph above, understanding b φ(τ) for low values of τ is suﬃcient for understanding why the price-dividend ratio is a decreasing function of λt. However, it is also instructive to decompose b φ(τ) for general values of τ. At longer maturities, it is possible for λt to change before the claim matures. Thus there are additional terms that account for the eﬀect of future changes in λt:

− −bσλ2bφ(τ) + Eν (e−γZ − 1)(1 − eφZ)

b φ(τ) = −Eν e−γZ(eZ − 1)

equity premium

riskfree rate

- 1

- 2

##### + Eν eφZ − 1

σλ2bφ(τ)2

− κbφ(τ)

+

mean-reversion

expected future dividends

Jensen’s inequality

The ﬁrst three terms in this more general decomposition are analogous to those in the simpler (32). The ﬁnal two terms account for the eﬀect of future changes in λt. The ﬁrst of these is a Jensen’s inequality term; all else equal, more volatility in the state variable increases the price-dividend ratio. The second of these represents the fact that, if λt is high in the present, λt is likely to decrease in the future on account of mean reversion.

While the focus of this paper is on the aggregate market, it is also of interest to compare the model’s implications for zero-coupon equity to the behavior of these claims in the data.11 Binsbergen, Brandt, and Koijen (2011) use option price data to calculate prices and risk premia on zero-coupon equity. Their methods are able to establish prices for dividend claims that have variable maturities of less than two years. They ﬁnd that these claims have expected excess returns that are statistically diﬀerent from zero. In other words, the equity premium arises at least in part from the short-term portion of the dividend stream.

11A related issue is the behavior of zero-coupon bonds. Bonds are described in detail in Appendix B.

Binsbergen et al. argue that this evidence is contrary to the implications of some leading asset pricing models such as Bansal and Yaron (2004) and Campbell and Cochrane (1999). In these models, the claim to dividends in the very near future has a premium close to zero; the equity premium arises from dividends paid in the far future.

In contrast, the present model implies a substantial equity premium for the short-term claim, and thus is consistent with the empirical evidence. Figure 7 shows risk premia (31)

- as a function of maturity. While the equity premium is increasing in maturity (that is, the “term structure of equities” is upward-sloping), the intercept of the graph is not at zero but rather at 5.5%. The reason is that a major source of the equity premium is disaster risk itself. Equities of all maturities have equal exposure to this risk, and thus even equities with short maturities have substantial risk premia, as the data imply.12

## 2.7 Comparison with power utility

To understand the role played by the recursive utility assumption, it is instructive to consider the properties of a model with time-varying disaster risk and time-additive utility.13 Consider a model with identical dynamics of consumption and dividends, but where utility is given by

∞

Cs1−γ 1 − γ

e−βs

ds. Appendix C shows that the riskfree rate under this model is equal to rt = β + γµ −

Vt = Et

t

- 1

- 2

γ(γ + 1)σ2 − λtEν e−γZ − 1 (33) the equity premium is given by

rte − rt = φγσ2 + λtEν e−γZ − 1 (1 − eφZ) (34)

- 12van Binsbergen et al. also show that, in their sample, short-maturity equity has a higher risk premium than the aggregate equity claim. While the model predicts that short-maturity equity has a lower risk premium, the data ﬁnding is not statistically signiﬁcant, and the predictions of the model appear to be well within the standard errors that van Binsbergen et al. calculate.
- 13Gourio (2008b) also shows analytically that the power utility model cannot replicate the predictability evidence.

and the value of the aggregate market takes the form

F(Dt,λt) = Dt

∞

exp{ap,φ(τ) + bp,φ(τ)λt} dτ.

0

The functions ap,φ(τ) and bp,φ(τ) satisfy ordinary diﬀerential equations given in Appendix C. The solutions are:

ap,φ(τ) = µD − µ − β + γσ2

2κλ¯ σλ2

−

κλ¯ σλ2

- 1

- 2

(γ + 1) − φ −

(ζp,φ − κ) τ

(ζp,φ − κ) e−ζ

p,φτ − 1 + 2ζp,φ 2ζp,φ

log

(35)

bp,φ(τ) =

2Eν e(φ−γ)Z − 1 e−ζ

p,φτ − 1 (ζp,φ − κ)(1 − e−ζp,φτ) − 2ζp,φ

, (36)

where

ζp,φ = κ2 − 2Eν [e(φ−γ)Z − 1]σλ2. (37) It is useful to contrast (36) with its counterpart in the recursive utility model. Under recursive utility, bφ(τ) is negative for φ > 1, implying that the price-dividend ratio is decreasing in λt. For power utility, bφ(τ) is negative only if φ > γ; otherwise it is positive.14 Under the reasonable assumption that φ is less than γ, the power utility model makes the counterfactual prediction that price-dividend ratios predict excess returns with a positive sign.15

What accounts for the diﬀerence between the power utility model and the recursive utility model? The answer lies in the behavior of the riskfree rate. Comparing (33) with (12) reveals that the riskfree rate under power utility falls more in response to an increase in disaster risk

14For φ > γ, the numerator of (36) is positive, and ζp,φ > κ, so 2ζp,φ > ζp,φ − κ > (ζp,φ − κ)(1 − e−ζ

p,φτ) and the denominator is negative. For φ < γ, it is necessary to also assume that κ2 > 2Eν e(φ−γ)Z − 1 σλ2. The numerator is negative because Eν e(φ−γ)Z − 1 > 0. The denominator is also negative because κ > ζp,φ.

15Gabaix (2008a) solves a model with disaster risk and power utility assuming linearity generating processes for consumption and dividends. While the theoretical model that Gabaix proposes allows for a time-varying probability of rare disasters, the disaster probability is assumed to be constant in the calibration and dynamics are generated by changing the degree to which dividends respond to a consumption disaster. As this discussion shows, incorporating time-varying probabilities into Gabaix’s calibrated model would likely reduce the model’s ability to match the data.

than under recursive utility with EIS equal to 1. In the power utility model, the riskfree rate eﬀect exceeds the combination of the equity premium and cash ﬂow eﬀect, and, as a result, the price-dividend ratio increases with disaster risk.16

# 3 Calibration and Simulation

## 3.1 Calibration

#### 3.1.1 Distribution of consumption declines

The distribution of the percentage decline, 1 − eZ is taken directly from the data . That is, 1 − eZ is assumed to have a multinomial distribution, with outcomes given by actual consumption declines in the data. I use the distribution of consumption declines found by Barro and Ursua (2008). Barro and Ursua update the original cross-country dataset of Maddison (2003) used by Barro (2006). The Maddison data consists of declines in GDP; Barro and Ursua correct errors and ﬁll in gaps in Maddison’s GDP data, as well as construct an analogous dataset of consumption declines. I calibrate to the consumption data because it is a more appropriate match to consumption in the model than is GDP. However, results obtained from GDP data are very similar. The frequency of large consumption declines implies an average disaster probability, λ¯ of 3.55%.17

The distribution of consumption declines in Panel A comes from data on 22 countries from 1870 to 2006. One possible concern about the data is the relevance of this group for the United States. For this reason, Barro and Ursua (2008) also consider the disaster distribution

16As in the recursive utility model, examining b p,φ(0) allows a precise statement of these trade-oﬀs. For power utility:

b p,φ(0) = Eν e(φ−γ)Z − 1

= −Eν e−γZ − 1 riskfree rate

− Eν (e−γZ − 1)(1 − eφZ) equity premium

+ Eν eφZ − 1 expected future dividends

,

which is greater than zero when γ > φ. 17I follow Barro and Ursua in using a 10% cut-oﬀ to identify large consumption declines.

for a subset consisting of developed economies. For convenience, I follow Barro and Ursua and refer to these as “OECD countries.”18 The distribution of consumption declines in these countries is given in Panel B. There are fewer of these crises; the implied average disaster probability is 2.86%. However, eliminating the non-OECD crises in eﬀect eliminates many comparatively minor crises (generally occurring after World War II). The overall distribution is shifted toward the more serious crises. In what follows, I use the distribution in Panel A for the base calibration, while the implications of the distribution in Panel B are explored in Section 3.4.

#### 3.1.2 Other parameters

- Table 1 describes model parameters other than the disaster distribution described above. Results are compared with quarterly U.S. data beginning in 1947 and ending in the ﬁrst quarter of 2010. Equities are constructed using the CRSP value-weighted index, while the riskfree rate moments are constructed from real returns on the three-month Treasury Bill). Postwar data are chosen as the comparison point in order to provide a clean comparison to moments of the model that are calculated conditional on no disasters having occurred. Two types of moments are simulated from the model. The ﬁrst type (referred to as “population” in the tables) are calculated based on all years in the simulation. The second type (referred to as “conditional” in the tables) are calculated after ﬁrst eliminating years in which one or more disasters took place.19

In the model, time is measured in units of years and parameter values should be interpreted accordingly. The drift rate µ is calibrated so that in normal periods, the expected

- 18The overlap with the actual founding members of what is now known as the OECD is not exact. The seventeen countries are Australia, Belgium, Canada, Denmark, Finland, France, Germany, Italy, Japan, Netherlands, Norway, Portugal, Spain, Sweden, Switzerland, U.K and U.S. The remaining ﬁve countries are Argentina, Brazil, Chile, Peru and Taiwan.
- 19For calculations done over consecutive years, relevant periods are omitted. For example, for evaluating predictability over 10-year horizons, 10 year periods of the simulation with a disaster are omitted.

growth rate of log consumption is 2.5% per annum.20 The standard deviation of log consumption σ is 2% per annum. These parameters are chosen as in Barro (2006) to match postwar data in G7 countries. The probability of default given disaster, q, is set equal to 0.4, calculated by Barro based on data for 35 countries over the period 1900–2000.

Barro and Ursua (2008) consider values of risk aversion equal to 3 and 3.5; because the dynamic nature of the present model leads to a higher risk premium, I use risk aversion equal to 3. Given these parameter choices, a rate of time preference (β) equal to 1.2% per annum matches the average real return on the three-month Treasury Bill in postwar U.S. data.

Leverage, φ, is set equal to 2.6; this is a conservative value by the standards of the prior literature. For example, the model of Bansal and Yaron (2004) uses leverage parameters of

- 3 and 5. The ratio of dividend to consumption volatility in postwar U.S. data is 4.9. In the present model, φ has implications for the response of dividends to a disaster, relative to consumption. For example, if consumption falls by 40%, dividends fall by 1 − 0.62.6 = 74%. Is this reasonable? For many countries and events in the Barro and Ursua data set, accurate dividend and earnings information is diﬃcult to come by. However, data on corporate earnings are available for the Great Depression, as described by Longstaﬀ and Piazzesi (2004), who argue that earnings may be a better proxy for economic dividends due to artiﬁcial dividend smoothing. Longstaﬀ and Piazzesi report that in the ﬁrst year of the Great Depression, when consumption fell by 10%, corporate earnings fell by more than 103%. In their calibration, they adopt a more conservative assumption: for a 10% decline in consumption, earnings fall by 90%. This is consistent with a leverage parameter of 22. However, the Longstaﬀ and Piazzesi calibration assumes that the consumption-dividend ratio is stationary; thus not all of the dividend decline is permanent. One approach to this issue would be to model a stationary consumption-dividend ratio. As argued above, this would complicate the model signiﬁcantly, so instead I adopt a relatively conservative value for leverage along with the simpler assumption that the dividend decline, like the consumption decline, is permanent.

20The value µ = 2.52% reﬂects an adjustment for Jensen’s inequality.

Other novel parameters are (implicitly) the elasticity of intertemporal substitution, the mean reversion of the disaster intensity, κ, and the volatility parameter for the disaster intensity, σλ. The EIS is set equal to 1 for tractability. A number of studies have concluded that reasonable values for this parameter lie in a range close to one, or slightly lower than 1 (e.g. Vissing-Jørgensen (2002)). Mean reversion κ is chosen to match the annual autocorrelation of the price-dividend ratio in postwar U.S. data. Because λt is the single state variable, the autocorrelation of price-dividend ratio implied by the model is determined almost entirely by the autocorrelation of λt. Setting κ equal to 0.080 generates an autocorrelation for the price-dividend ratio equal to 0.92, its value in the data. The volatility parameter σλ is chosen to be 0.067; as will be discussed below, this generates a reasonable level of volatility in stock returns. The quantity σλ itself is hard to interpret economically; for this reason the table also reports σλE λ1/2 , which is a measure of the annual volatility of λt. This measure indicates that λt varies (approximately) by 1.14 percentage points a year. That is, when λt is one standard deviation above its mean, its value is 4.49%.

## 3.2 Simulation Results

- Table 2 describes moments from a simulation of the model as well as moments from postwar U.S. data. The model is discretized using an Euler approximation (see Glasserman (2004, Chapter 3)) and simulated at a monthly frequency for 50,000 years; simulating the model

- at higher frequencies produces negligible diﬀerences in the results.21 First I simulate the series λt and ∆log Ct. Given the simulated series λt, the price-dividend ratio is given by

(22) and the yield on government debt, rtL, is given by (13). Equity returns are computed using the series for the price-dividend ratio and for consumption growth, while bond returns are computed using (A.41). The resulting series for monthly returns and growth rates in fundamentals are then compounded to an annual frequency.

The model can be rejected if it oﬀers unrealistic implications for the mean and volatility

21The discrete-time approximation requires setting λt to equal zero in the square root when it is negative. However, this occurs in less than 1% of the simulated draws.

of the aggregate market, Treasury bills and consumption and dividend growth as well as for predictability of stock returns and consumption growth.22 These particular measures have been the focus of much of the recent asset pricing literature. As I argue below, the model’s implications are in fact realistic. Table 2 shows that the model generates a realistic equity premium. In population, the equity premium is 7.6%, while, conditional on no disasters, the equity premium is 8.9%. In the historical data it is 7.1%. The expected return on the government bill is 1% in population, 1.36% conditional on no disasters, and 1.34% in the data. The model predicts equity volatility of 19.9% per annum in population and 17.7% conditional on no disasters. The observed volatility is 17.7%. The Sharpe ratio is 0.39 in population, 0.49 conditional on no disasters and 0.40 in the data.

The model is able to generate reasonable volatility for the stock market without generating excessive volatility for the government bill or for consumption and dividends. Note that the parameter values were not explicitly chosen to target a low interest rate volatility. The volatility of the government bill is 3.8% in population, much of which is due to realized disasters; it is 2.0% conditional on no disasters. This compares with a volatility of 2.7% in the data. Given that interest rate volatility in the data arises largely from unexpected inﬂation that is not captured by the model, the data volatility should be viewed as an upper bound on reasonable model volatility.

The volatilities for consumption and dividends predicted by the model for periods of no disasters are also below their data counterparts. Conditional on no disasters, consumption volatility is 2.0%, compared with 1.3% in the data. Dividend volatility is 5.2%, compared with 6.6% in the data. Including rare disasters in the data simulated from the model has a large eﬀect on dividend volatility. When the disasters are included, dividend volatility is

- 16.5%. The diﬀerence between the eﬀect of including rare disasters on returns as compared with the eﬀect on fundamentals is striking. Unlike dividends, returns exhibit a relatively small diﬀerence in volatility when calculated with and without rare disasters: 19.9% versus

22While the calibration approach that I adopt has the advantages of transparency and comparability to the results of other models, it has the disadvantage that it does not oﬀer a formal test of quantitative success.

- 17.7%. This is because a large amount of the volatility in returns arises from variation in the equity premium. Risk premia are equally variable regardless of whether disasters actually occur in the simulated data or not.

I next discuss the model’s implications for excess return and consumption predictability. These moments are not explicit targets of the calibration, but follow naturally given the model’s properties, as described in Section 2.4. Table 3 reports the results of regressing longhorizon excess returns (the log return on equity minus the log return on the government bill) on the price-dividend ratio in simulated data. I calculate this regression for returns measured over horizons ranging from 1 to 10 years. Table 3 reports results for the entire simulated data set (“population moments”) for periods in the simulation in which no disasters occur (“conditional moments”) and for the historical sample.

Panel A of Table 3 shows population moments from simulated data. The coeﬃcients on the price-dividend ratio are negative: a high price-dividend ratio corresponds to low disaster risk and therefore predicts low future expected returns on stocks relative to bonds. The R2 is 4% at a horizon of 1 year, rising to 26% at a horizon of 10 years. Panel B reports conditional moments. The conditional R2s are larger: 13% at a horizon of 1 year, rising to 63% at a horizon of 10 years. The unconditional R2 values are much lower because, when a disaster occurs, nearly all of the unexpected return is due to the shock to cash ﬂows.

The data moments are higher than the population values, but, more relevantly, lower than the conditional values. As demonstrated in a number of studies (e.g. Campbell and Shiller (1988), Cochrane (1992), Fama and French (1989), Keim and Stambaugh (1986)) and replicated in this sample, high price-dividend ratios predict low excess returns. While returns exhibit predictability over a wide range of sample periods, the high persistence of the price-dividend ratio leads sample statistics to be unstable (see, for example, Lettau and Wachter (2007) for calculations of long-horizon predictability using this data set but for diﬀering sample periods), and unusually low when calculated over recent years. For this reason, the R2 statistics in the data should be viewed as an approximate benchmark.

Another potential source of variation in returns is variation in expected future consump-

tion growth. According to the model, a low price-dividend ratio indicates not only that the equity premium is likely to be high in the future, but also that consumption growth is likely to be low because of the increased probability of a disaster. However, a number of studies (e.g. Campbell (2003), Cochrane (1994), Hall (1988), Lettau and Ludvigson (2001)) have found that consumption growth exhibits little predictability at long horizons, a ﬁnding replicated in Panel B of Table 4. It is therefore of interest to quantify the amount of consumption growth predictability implied by the model.

Table 4 reports the results of running long-horizon regressions of consumption growth on the price-dividend ratio in data simulated from the model and in historical data. Panel A shows the population moments implied by the model. The model does imply some predictability in consumption growth, but the eﬀect is very small. The R2 values never rise above 6%, even at long horizons. This predictability arises entirely from the realization of a rare disaster. When these rare disasters are conditioned out, there is zero predictability because consumption follows a random walk (in simulated data, the coeﬃcient values are less than .001 and the R2 values are less than .0001). Thus the model accounts for both the predictability in long-horizon returns and the absence of predictability in consumption growth.

Of possible concern is the dependence of these results on the assumed probability of default, equal to 0.4. Barro (2006) calculates this value based on the number of times a disaster results in default, divided by the total number of disasters. However, one might expect that the default is more likely to occur during the worst disasters. The value 0.4 does not take this correlation into account.23 To evaluate the sensitivity of the results to

23One could extend the model to allow for such a correlation, without aﬀecting tractability. Consider the current speciﬁcation of the price process for government liabilities, described in detail in Appendix A.5:

where

dLt Lt

= rtL dt + eZ

L,t

− 1 dNt,

 

ZL,t =



Zt with probability q 0 otherwise.

this assumption, I consider a higher probability of default, namely q = 0.6 (keeping all other parameters the same). This change has the eﬀect of raising the expected rate of return on government debt to 2.1% (conditional on no disasters), as compared with a value of 1.3% when 0.4 is used. The bond volatility falls from 2% to 1.4%. Because the government bill rate is higher, the equity premium relative to the government bill is lower: 8.10% rather than 8.85%. The Sharpe ratio is lower as well: 0.45 rather than 0.49. The predictability of excess stock returns is slightly lower under this calibration: R2 values range from 11% to 56%. Other results do not change. Thus, except for the average government bill rate, this change improves the ﬁt of the model to the data. While the implied average government bill rate of 2% is slightly higher than the sample average, it is not unreasonable given the diﬃculties of measuring the mean for a highly persistent process (alternatively one could further lower this rate by lowering β; this has very little eﬀect on the other results).

Other models succeed in matching the mean and volatility of stock returns. Two such models are those of Bansal and Yaron (2004) and of Campbell and Cochrane (1999). Despite the fact that all three models can capture these ﬁrst two unconditional moments of returns, they generate diﬀerent implications for other observable quantities. The principle mechanism in the Bansal-Yaron model is a persistent, time-varying mean of consumption growth. Their model therefore implies that consumption growth should be predictable at long horizons. However, it is diﬃcult to see evidence for this in the data (Table 4). Because this model implies a smaller degree of predictability, and only then in samples in which a disaster occurs, it is more in line with the data in this respect. The Campbell-Cochrane model is driven by shocks to consumption growth, and as such implies a perfect correlation between consumption and stock returns. However, the correlation in the data is very low, and, while time-aggregation in consumption over longer horizons mitigates this concern, it does not

Replace the latter equation by

 

Zt if Zt < k

ZL,t =



0 otherwise for some threshold value k. In the absence of more complete data on defaults, and to maintain the simplicity of the present model, I do not pursue this route here.

eliminate it. The present model implies zero correlation in samples without a disaster.

This model also imposes diﬀerent, and arguably more reasonable, requirements on the utility function of the representative agent. In the main calibration, risk aversion is assumed to equal 3. In contrast, in the model of Bansal and Yaron (2004), it is assumed to equal 10, while the model of Campbell and Cochrane (1999) assumes a time-varying risk aversion, which equals 35 when the state variable is at its long-run mean. Bansal and Yaron also require a higher elasticity of intertemporal substitution (1.5 rather than 1); independent evidence discussed above supports the lower value. While a full comparison of these three models is outside the scope of this study, it appears that the present model may oﬀer advantages relative to leading alternative explanations for the high equity premium and the volatility puzzle.

## 3.3 Implied disaster probabilities

This section describes the disaster probabilities implied by the historical time series of stock prices. Equation 22 shows that, in the model, the price-dividend ratio as a strictly decreasing function of the disaster probability. In principle, given observations on the price-dividend ratio, one could invert this function to ﬁnd the values of λt implicit in the historical data. I follow a slightly modiﬁed approach: rather than using the price-dividend ratio itself, I use price divided by smoothed earnings, as in Shiller (1989, Chap. 26). Dividend payouts appear to have shifted downwards in the latter part of the sample (Fama and French (2001)). Because the process assumed for dividends does not allow for this shift, requiring the model to match the price-dividend ratio in the data could yield misleading results.24 For this exercise it is particularly useful to have a longer time series. I therefore use data on the S&P 500, which can be found on Robert Shiller’s website. These data begin in 1880 and are updated to the present. Because the levels of the price-earnings ratio and the price-dividend

24The predictability of returns and consumption is very similar regardless of which measure is used; thus the choice of the price-dividend versus the price-earnings ratio has little impact on the results in Tables 3 and 4.

ratio are diﬀerent, I adjust the level of the series in the data so it is comparable to that in the model. That is, I subtract the sample mean from the historical time series of the log priceearnings ratio. Then I add the population mean of the log price-dividend ratio computed from the simulation of the model. I invert the resulting time series to ﬁnd the implied values of λt using (22). A few observations (namely, those corresponding to the highest observed price-earnings ratios) imply negative values of λt. In these instances, I set λt to zero.

Figure 8 shows the resulting time series for λt. The peak in the series occurs in 1920, with a disaster probability of 14%. This year corresponds not only to a recession, but also to an inﬂuenza epidemic. In fact, one of the two U.S. disasters as deﬁned by Barro and Ursua (2008) occurs at this time. A second peak in the series occurs in 1932 during the Great Depression, which is the second disaster in U.S. data. The disaster probability was relatively high in the 1950s, declining in the 1960s, and rising again in the 1970s. The highest postwar values of the probability occur in the 1980s, corresponding to a period of heightened fears of a third World War. In contrast, the disaster probability was very low in the 1990s and early part of this century (rising very slightly with the bursting of the “tech bubble”). The ﬁnancial crisis of late 2008 and early 2009 coincides with a rapid increase in the probability of a disaster, from 0 to 5%. In 2010, the probability falls to less than 2%

## 3.4 Alternative calibrations

Table 5 shows the results of two alternative calibrations of the model. Panel A shows the results of calibrating the disaster distribution to disasters in OECD countries only, as described in Section 3.1. This calibration, by focusing on mainly developed economies, alleviates the concern that the disaster distribution is not applicable to the U.S. Under this calibration, there are fewer disasters, implying a lower mean of λ¯, namely 2.86%. I keep all other parameters the same.25 The equity premium conditional on no disasters is 7.83% per annum, lower than in the base calibration, but still higher than in the data. The average

25Rather than keeping σλ the same, namely 6.4%, it might seem natural to hold σλE λ1/2 ﬁxed, and raise σλ accordingly. However, it is not possible to do this and keep the value function well-deﬁned.

government bill rate is 1.86% per annum, higher than before, but not far from the data mean of 1.34% per annum. Other quantities, such as return volatility, the Sharpe ratio, volatility of consumption and dividends and predictability (not shown), the results are also quite similar. This change makes little diﬀerence because, while disasters are less frequent under the OECD calibration, they are also more severe (see Figure 2).

A second concern is that the results in this paper assume that the disasters are permanent, rather than allowing for faster growth following a disaster (see Gourio (2008a)). It would be of interest to consider a model allowing for time-variation in the mean of consumption and dividends along with time-variation in the probability of disaster. Such a change would signiﬁcantly complicate the model, so for the present paper I consider a simpler modiﬁcation. I consider the OECD above as a starting point, and reduce the percent declines in consumption by half. This is the fraction of the decline that is, on average, permanent as estimated by Nakamura, Steinsson, Barro, and Ursua (2011). That is, I assume that half of the observed decline is noise, in the sense that it is immediately reversed.26 The results are given in Panel B. Under these more conservative assumptions, the model can still capture most of the equity premium and volatility with slightly higher risk aversion, namely with γ = 6.

Finally, the results also assume disasters are instantaneous, rather than occurring over multiple periods (see Constantinides (2008)). Nakamura, Steinsson, Barro, and Ursua (2011) estimate and numerically solve a model of multiperiod disasters with recoveries. While they assume a constant disaster probability, their results provide insight into how multiperiod disasters would eﬀect the calibration in the current paper. Indeed, Nakamura et al. show that a model with multiperiod disasters can match the equity premium with risk aversion that is moderately higher than that required by a model with single-period disasters. The mechanism, which is also operative in the present model, is that the agent with recursive utility

26This is a conservative calibration, not only in that it assumes the reversal is instantaneous. Any variation in the amount of the decline that is reversed, along with uncertainty about the average reversal would increase the risk of disasters to the agent.

considers future consumption growth to be a source of risk along with current consumption growth.27

# 4 Conclusion

This paper has shown that a continuous-time endowment model in which there is timevarying risk of a rare disaster can explain many features of the aggregate stock market. Besides explaining the equity premium without assuming a high value of risk aversion, it can also explain the high level of stock market volatility. The volatility of the government bill rate remains low because of a tradeoﬀ between an increased desire to save due to an increase in the disaster probability and a simultaneous increase in the risk of default. The model therefore oﬀers a novel explanation of volatility in the aggregate stock market that is consistent with other macroeconomic data. Moreover, the model accounts for economically signiﬁcant excess return predictability found in the data, as well as the lack of long-run consumption growth predictability. Finally, the model can be solved in closed form, allowing for straightforward computation and for potential extensions. While this paper has focused on the aggregate stock market, the model could be extended to price additional asset classes, such as long-term government bonds, options and exchange rates.

27Both multiperiod disasters and recoveries could in principle be introduced in the present framework without aﬀecting tractability. Allowing, for example, jumps in the drift rate of consumption growth would imply disasters unfolding over multiple periods. Mean reversion in the drift rate would also imply faster recoveries following disasters.

# Appendix

## A Solution to the recursive utility model

#### A.1 Value function

The value function J(W,λ) satisﬁes

sup

αt,Ct

JW Wtαt(µ − rt + l−1) + Wtrt − Ct + Jλκ(λ¯ − λt)+

- 1

- 2

JWWWt2αt2σ2 +

1 2

Jλλσλ2λt + λtEν J(Wt(1 + αt(eZ

t

− 1)),λt) − J(Wt,λt)

+ f(Ct,J) = 0. (A.1)

In equilibrium, α = 1 and C = l−1W. Substituting these policy functions into (A.1) implies

JWWtµ + Jλκ(λ¯ − λt) +

- 1

- 2

- 1

- 2

JWWWt2σ2 +

Jλλσλ2λt + λtEν J(WteZ

,λt) − J(Wt,λt) + f(Ct,J) = 0. (A.2)

t

Conjecture that the solution to this equation takes the form

J(W,λ) =

W1−γ 1 − γ

I(λ). (A.3)

It is helpful to solve for the consumption-wealth ratio prior to solving for I(λ); because ψ is equal to 1, the expression for the consumption-wealth ratio is very simple. By deﬁnition

Note that

f(C,V ) = β(1 − γ)V log C −

1 1 − γ

log((1 − γ)V ) . (A.4)

V C

fC(C,V ) = β(1 − γ)

. (A.5)

The envelope condition fC = JW, together with (A.5) and the conjecture (A.3) implies

W1−γ 1 − γ

β(1 − γ)

I(λ)

Solving for l yields l = β−1.

1 l−1W

= W−γI(λ)

Given the consumption-wealth ratio, it follows that

f(C(W),J(W,λ)) = βW1−γI(λ) log(βW) −

log I(λ) 1 − γ

= βW1−γI(λ) log β −

Substituting (A.3) and (A.6) into (A.2) implies

1 1 − γ

log(W1−γI(λ))

. (A.6)

I(λt)µ + I (λt)(1 − γ)−1κ(λ¯ − λt) −

1 2

γI(λt)σ2 +

1 2

(1 − γ)−1I (λt)σλ2λt

+ (1 − γ)−1I(λt)λtEν e(1−γ)Z − 1

log I(λt) 1 − γ

+ βI(λt) log β −

Conjecture that a function of the form

= 0. (A.7)

I(λ) = ea+bλ (A.8)

solves (A.7). Substituting (A.8) into (A.7) implies

- 1

- 2

- 1

- 2

µ + b(1 − γ)−1κ(λ¯ − λt) −

b2σλ2λt(1 − γ)−1 + (1 − γ)−1λtEν e(1−γ)Z − 1 + β log β − (1 − γ)−1(a + bλt) = 0. Collecting terms in λt results in the following quadratic equation for b: σλ2b2 − (κ + β)b + Eν e(1−γ)Z − 1 = 0,

γσ2 +

- 1

- 2

implying

κ + β σλ2 ±

b =

2

Eν [e(1−γ)Z − 1] σλ2

κ + β σλ2

− 2

. (A.9)

Collecting constant terms results in the following characterization of a in terms of b:

1 − γ β

a =

µ −

κλ¯ β

- 1

- 2

γσ2 + (1 − γ)log β + b

. (A.10)

For the value function to exist, the term inside the square root in (A.9) must be non-negative. This places a joint restriction on the severity of disasters, the agent’s risk aversion and rate

of time preference, and the volatility and permanence of shocks to λt. Note also that κ > 0 and β > 0 are standing assumptions that are required for the existence of λt and of the value function respectively.

While the presence of two roots in (A.9) suggests multiple possible solutions, a simple thought experiment reveals that only one of these roots displays reasonable economic properties. Consider the case of Z identically equal to zero; namely the Poisson process Nt has positive realizations, but that these have no economic consequence. There are no disasters in this case and the value function should reduce to its counterpart under the standard diﬀusion model. However, the choice of the positive root in (A.9) implies that the representative agent’s utility is reduced by an increased likelihood of these inconsequential Poisson realizations. The choice of the negative root does not suﬀer from this defect.28

Taking the derivative of (A.1) with respect to portfolio choice α, evaluating at α = 1 and setting to zero implies

µ − rt + l−1 = γσ2 − λtEν e−γZ(eZ − 1) . (A.11) Because l−1 = β, it follows that the equation for the riskfree rate is given by

rt = β + µ − γσ2 + λtEν e−γZ eZ − 1 .

#### A.2 State-price density

Calculation of prices and rates of return in the economy is simpliﬁed considerably by making use of the state-price density, which determines the equilibrium compensation investors require for bearing various risks in the economy. As discussed in Section 2.4, the state-price density is given by

t

πt = exp

fV (Cs,Vs)ds fC(Ct,Vt), (A.12)

0

28Two other considerations (perhaps not coincidentally) point toward choosing the negative root. First, Tauchen (2005) suggests choosing the root such that the solution approaches a well-deﬁned limit as σλ approaches zero (this holds for the negative root but not the positive root). Second, for the present calibration, the choice of the negative root is more conservative in that it implies a smaller equity premium and lower equity volatility than the choice of a positive root.

Because the exponential term in (A.12) is (locally) deterministic, covariances of the stateprice density with fundamentals, and thus risk premia, are determined by the second term, fC(C,V ). In equilibrium, Vt = J(β−1Ct,λt). Therefore,

Vt Ct

= βγCt−γI(λt). (A.13) Ito’s Lemma and (A.13) imply29

fC(Ct,Vt) = β(1 − γ)

dπt πt−

= µπ,t dt + σπ,t[dBt dBλ,t] + (e−γZ

− 1)dNt, (A.14) where

t

σπ,t = −γσ bσλ λt . (A.15) It follows from no-arbitrage that

µπ,t = −rt − λtEν e−γZ − 1 (A.16)

= −µ − β + γσ2 − λt Eν e−γZ(eZ − 1) + Eν e−γZ − 1 , (A.17) where (A.17) follows from (12).

In the event of a disaster, marginal utility (as represented by the state-price density) jumps upward, as can be seen by the term multiplying the Poisson process in (A.14). This implies that investors require compensation for bearing disaster risk, not surprisingly. The ﬁrst element of (A.15) implies that the standard diﬀusion risk in consumption is priced; more interestingly, changes in λt are also priced as reﬂected by the second element of (A.15).

#### A.3 Pricing equity claims

Let Ft = F(Dt,λt) denote the price of the claim to the aggregate dividend. It follows from the absence of arbitrage that

F(Dt,λt) = Et

∞

- πs

- πt

Ds ds . (A.18)

t

29To compute the term in (24) multiplying the Poisson shock, note that

πt − πt− πt−

=

fC(Ct,Vt) − fC(Ct−,Vt−) fC(Ct−,Vt−)

=

where the second equality follows from (A.13).

Ct−γ − Ct−γ

−

Ct−γ

−

##### As discussed in Section 2.4, F is an integral of expressions of the form Et π

πtDs . It is convenient to calculate these expectations ﬁrst, and then calculate F as the integral of these expectations (since one-dimensional integrals are typically very simple to compute numerically).

s

Let Ht = H(Dt,λt,s − t) denote the price of the asset that pays the aggregate dividend at time T, namely,

- πs

- πt

H(Dt,λt,s − t) = Et

Ds . No-arbitrage implies that H(Ds,λs,0) = Ds and that

πtH(Dt,λt,s − t) = Et [πsH(Ds,λs,0)].

That is, πtHt follows a martingale. Conjecture that

H(Dt,λt,τ) = Dt exp{aφ(τ) + bφ(τ)λt}. (A.19)

Ito’s Lemma then implies

dHt Ht−

= µH,t dt + σH,t[dBt dBλ,t] + (eφZ

t

− 1)dNt, (A.20)

for processes µH,t and σH,t deﬁned below. Applying Ito’s Lemma to πtHt implies that the product can be written as

πtHt = π0H0 +

t

πsHs µH,s + µπ,s + σπ,sσ H,s ds +

0

t

πsHs (σH,s + σπ,s)[dBs dBλ,s]

0

+

0<si≤t

i − πs−

##### Hs−

Hs

πs

i

i

i

, (A.21)

where si = inf {s : Ns = i} (namely, the time that the ith jump occurs).

I use (A.21) to derive a diﬀerential equation for H. The ﬁrst step is to compute the expectation of the jump term 0<s

i − πs−

. Note that πt is the product of a pure diﬀusion process and Ct−γ, while Ht is the product of a pure diﬀusion process and Dt = Ctφ. The pure diﬀusion processes are not aﬀected by the jump. Therefore,

i≤t πs

Hs

##### Hs−

i

i

i

Eν

πtHt − πt−H− πt−Ht−

1 Ct−−γDt−

t −γ Dt−eφZ

Eν Ct−eZ

=

t

##### − Ct−−γDt− = Eν e(φ−γ)Z − 1 .

Adding and subtracting the “jump compensation term” from (A.21) yields:

πtHt = π0H0 +

t

πsHs µH,s + µπ,s + σπ,sσ H,s + λsEν e(φ−γ)Z − 1 ds

0

t

πsFs (σH,s + σπ,s)[dBs dBλ,s]

+

0

t

πsHsλsEν e(φ−γ)Z − 1 ds , (A.22)

−

i − πs−

πs

##### Hs−

+

Hs

i

i

i

0

0<si≤t

Under mild regularity conditions analogous to those given in Duﬃe, Pan, and Singleton (2000, Proposition 1), the second and the third terms on the right hand side of (A.22) are martingales. Therefore the ﬁrst term on the right hand side of (A.22) must also be a martingale, and it follows that the integrand of this term must equal zero:

µH,t + µπ,t + σH,tσ π,t + λtEν e(φ−γ)Z − 1 = 0. (A.23)

Lastly, it follows from Ito’s Lemma that µH and σH are given by

1 H

∂H ∂τ

- 1

- 2

HDµD + Hλκ(λ¯ − λt) −

Hλλσλ2λt

µH,t =

+

- 1

- 2

= µD + bφ(τ)κ(λ¯ − λt) − (a φ(τ) + b φ(τ)λt) +

bφ(τ)2σλ2λt, (A.24)

and

1 H

σH,t =

HDµD[σD 0] + Hλ[0 σλ λt]

= φσ bφ(τ)σλ λt , (A.25)

where HD and Hλ denote partial derivatives of H with respect to D and λ respectively, and where Hλλ denotes the second derivative with respect to λ. Substituting these equations, along with (25) and (A.17) into (A.23) implies

- 1

- 2

µD + bφ(τ)κ(λ¯ − λt) − a φ(τ) − b φ(τ)λt +

b2φ(τ)σλ2λt − µ − β + γσ2 − λtEν e−γZ(eZ − 1) − λtEν e−γZ − 1 − γσ2φ + bφ(τ)bσλ2λt + λtEν e(φ−γ)Z − 1 = 0.

Collecting constant terms results in the following ordinary diﬀerential equation for aφ

a φ(τ) = µD − µ − β + γσ2 − γσ2φ + κλb¯ φ(τ) (A.26) while collecting terms multiplying λ results in the following ordinary diﬀerential equation for bφ.

- 1

- 2

σλ2bφ(τ)2 + (bσλ2 − κ)bφ(τ) + Eν e(φ−γ)Z − e(1−γ)Z . (A.27) The boundary conditions are aφ(0) = bφ(0) = 0. The solutions are

b φ(τ) =

- aφ(τ) = µD − µ − β + γσ2(1 − φ) −

κλ¯ σλ2

(ζφ + bσλ2 − κ) τ

−

2κλ¯ σλ2

log

(ζφ + bσλ2 − κ) e−ζ

φτ − 1 + 2ζφ 2ζφ

(A.28)

- bφ(τ) =

2Eν e(1−γ)Z − e(φ−γ)Z 1 − e−ζ

φτ

, (A.29)

(ζφ + bσλ2 − κ)(1 − e−ζφτ) − 2ζφ

where

ζφ = (bσλ2 − κ)2 + 2Eν [e(1−γ)Z − e(φ−γ)Z]σλ2. (A.30) Assume conditions suﬃcient for the existence of λt and Vt (see Sections 2.1 and 2.2). Then the conditions Z < 0, σλ > 0 and φ > 1 are suﬃcient for the existence of aφ(τ) and bφ(τ) at all values of τ.30 First, because Z is negative, Eν e(1−γ)Z − e(φ−γ)Z > 0, and thus the term inside the square root of (A.30) is guaranteed to be positive. Moreover, ζφ > |bσλ2 − κ| ≥ bσλ2 − κ, implying that the denominator (ζφ + bσλ2 − κ) 1 − e−ζ

φτ − 2ζφ is strictly negative for all τ. This argument also establishes that bφ(τ) < 0 for all τ.

The last discussion shows that bφ(τ) exists and is negative for all τ. I now show that bφ(τ) converges as τ goes to inﬁnity. It follows from (A.29) that

2Eν e(φ−γ)Z − e(1−γ)Z ζφ + κ − bσλ2

lim

bφ(τ) =

τ→∞

1 σλ2

ζφ − κ + bσλ2 ,

= −

30These functions also exist for the limiting cases of φ = 1, σλ = 0, and Z = 0. If φ = 1, G(λ) equals the wealth-consumption ratio: bφ(τ) = 0 and aφ(τ) = −βτ. If σλ = 0, G(λ) can be shown to converge to its analogue in a model with constant disaster risk. If Z = 0, the expressions converge to the standard model with only normal shocks to consumption.

where the second line follows from the fact that ζφ2−(κ−bσλ)2 = −2Eν e(φ−γ)Z − e(1−γ)Z σλ2. The constant term aφ(τ) does not approach a ﬁnite limit itself, but its asymptotic slope is given by

κλ¯ σλ2

aφ(τ) τ

= µD − µ − β + γσ2(1 − φ) −

ζφ + bσλ2 − κ .

lim

τ→∞

Finally, let re,(τ) denote the instantaneous expected return on zero-coupon equity with maturity τ. Because zero-coupon equity pays only a terminal dividend at maturity, its instantaneous expected return is simply the drift plus the expected percent change in price in the event of a disaster:

rte,(τ) ≡ µH,t + λtEν eφZ − 1 . Therefore, it follows from (A.16) and (A.23) that the risk premium is given by

rte,(τ) − rt = −σπ,tσ H,t − λt Eν e(φ−γ)Z − 1 − (Eν e−γZ − 1 − Eν eφZ − 1 .

It follows that

rte,(τ) − rt = φγσ2 − λtbφ(τ)bσλ2 + λtEν e−γZ − 1 (1 − eφZ) . (A.31)

#### A.4 Equity Premium

To derive an expression for the premium on the aggregate market, I ﬁrst return to the expression for the price of the dividend claim given in Appendix A.3:

F(Dt,λt) = Et

∞

- πs

- πt

Ds ds . (A.32)

t

I use this expression to derive a “local” no-arbitrage condition analogous to (A.23). Multiplying each side of (A.32) by πt implies

πtFt = Et

∞

πuDu du. (A.33)

t

The same equation must hold at any time s > t:

πsFs = Es

∞

πuDu du. (A.34)

s

Combining (A.33) and (A.34) implies

πtFt = Et πsFs +

- s
- t

πuDu du . (A.35)

Adding 0 t πuDu du to both sides of (A.35) implies

πtFt +

t

πuDu du = Et πsFs +

0

s

πuDu du . (A.36)

0

Therefore πtFt + 0 t πuDu du is a martingale. Further, as in Appendix A.3

πtFt +

t

πsDs ds =

0

+

t

Ds Fs

+ σπ,sσ F,s + λsEν e(φ−γ)Z − 1 ds

πsFs µF,s + µπ,s +

0

t

+

πsFs (σF,s + σπ,s)[dBs dBλ,s]

0

t

πsFsλsEν e(φ−γ)Z − 1 ds , (A.37)

−

i − πs−

πs

Fs

##### Fs−

i

i

i

0

0<si≤t

where si = inf {s : Ns = i}. The second and the third terms on the right hand side of (A.37) are martingales. Therefore the ﬁrst term in (A.37) must also be a martingale, and it follows that the integrand of this term must equal zero:

Dt Ft

µF,t + µπ,t +

+ σπ,tσ F,t + λtEν e(φ−γ)Z − 1 = 0. (A.38)

Substituting (A.16) into (A.38) and re-arranging implies

Dt Ft − rt = −σπ,tσ F,t − λt Eν e(φ−γ)Z − 1 − Eν e−γZ − 1 . (A.39) The left hand side of (A.39) is the instantaneous equity premium conditional on no disasters occurring. The instantaneous equity premium in population is given by this quantity, plus the expected percentage change if a disaster occurs. That is, if rte is deﬁned as

µF,t +

Dt Ft

rte ≡ µF,t +

+ λtEν[eφZ − 1],

then, from (A.39), it follows that the equity premium in population equals

rte − rt = −σπ,tσ F,t − λt Eν e(φ−γ)Z − 1 − Eν e−γZ − 1 − Eν[eφZ − 1]

= −σπ,tσ F,t + λtEν (e−γZ − 1)(1 − eφZ) . (A.40)

#### A.5 Default

Consider government debt with an instantaneous maturity. Namely, let Lt be the price process resulting from rolling over instantaneous government debt. Then Lt follows the process

dLt Lt

= rtL dt + eZ

− 1 dNt, (A.41) where rtL is the “face value” of government debt (i.e. the amount investors receive if there is no default), ZL,t is a random variable whose distribution will be described shortly and Nt is the same Poisson process that drives the consumption process. Assume that, in event of a disaster, there will be a default on government liabilities with probability q. I follow Barro (2006) and assume that in the event of default, the percent loss is equal to the percent fall in consumption. Therefore,

L,t

 

Zt with probability q 0 otherwise

ZL,t =

(A.42)



By no-arbitrage, the process Lt must satisfy

rtL + µπ.t + λtEν e−γZeZ

− 1 = 0. (A.43) Equation (A.43) is the analogue of the equity pricing equation (A.38) (note that the “dividend” on government liabilities is zero). It follows from the deﬁnition of ZL that

L

Eν e−γZeZ

L

− 1 = qEν e(1−γ)Z − 1 + (1 − q)Eν e−γZ − 1 . (A.44)

The expression for µπ,t is given by (A.17). Substituting into (A.43) and solving for rtL yields

rtL = rt + λtEν e−γZ

t

− 1 − λt (1 − q)Eν e−γZ

t

− 1 + qEν e(1−γ)Z

t

− 1 ,

which reduces to (13), the expression in the text.

## B Prices and returns on long-term bonds

The price at time t of a real, default-free zero-coupon bond maturing at time s > t is given by Et[πs/πt]. The steps in Appendix A.3 can be followed to conclude that this price is given

by

Et

πs πt

= exp{a0(τ) + b0(τ)λt},

where a0(τ) and b0(τ) satisfy the diﬀerential equations:

- a 0(τ) = −µ − β + γσ2 + κλb¯ 0(τ) (B.1)
- b 0(τ) =

- 1

- 2

σλ2b0(τ)2 + (bσλ2 − κ)b0(τ) + Eν e(−γ)Z − e(1−γ)Z . (B.2)

and boundary conditions a0(τ) = b0(τ) = 0. These correspond to the diﬀerential equations in Appendix A.3, with φ = 0 and µD = 0.

The fact that long-term bond prices move with the disaster probability, combined with the fact that changes in the disaster probability are priced in the model, implies that expected returns on long-term bonds diﬀer from the riskfree rate. Speciﬁcally, let rt(τ) denote the instantaneous expected return on a default-free zero coupon bond with maturity τ. The same reasoning used to derive (A.31) shows

rt(τ) − rt = −λtb0(τ)bσλ2. (B.3) Risk premia on default-free bonds arise only from the correlation with the time-varying probability of a disaster (namely, there is no covariance with shocks to consumption, during a disaster or otherwise). Intuitively, this risk premium should be negative, because bond prices rise when interest rates fall, which occurs when disaster risk is high (keeping in mind that the investor requires a premium to hold assets with prices positively correlated with disaster risk). Indeed, as I show below, b0(τ) is positive for relevant parameter values. Because b is positive (as shown in Section 2.2) risk premia on bonds are negative and the real default-free term structure will be downward sloping.

I now give the solutions to (B.1) and (B.2). Unlike for equities, there are two cases.31

31The diﬀerence arises from the fact that the analogue to Eν e−γZ − e(1−γ)Z in the case of equities is Eν e(φ−γ)Z − e(1−γ)Z , which is negative rather than positive.

- Case 1: (bσλ2 − κ)2 − 2Eν e−γZ − e(1−γ)Z σλ2 > 0 In this case, the solution resembles that of equities. Namely, the solution is given by (18–20), with µD = φ = 0:

b0(τ) =

2Eν e−γZ − e(1−γ)Z e−ζ

0τ − 1 (ζ0 + bσλ2 − κ)(1 − e−ζ0τ) − 2ζ0

(B.4)

ζ0 = (bσλ2 − κ)2 − 2Eν [e−γZ − e(1−γ)Z]σλ2, (B.5) and

a0(τ) = −µ − β + γσ2 −

κλ¯ σλ2

(ζ0 + bσλ2 − κ) τ

−

2κλ¯ σλ2

log

(ζ0 + bσλ2 − κ) e−ζ

0τ − 1 + 2ζ0 2ζ0

. (B.6)

These functions exist for all τ provided that bσλ2 < κ. If, however, bσλ2 > κ, then there is some ﬁnite τ at which bond prices go to inﬁnity.32

If bσλ2 > κ, then b0(τ) is positive for all τ. This follows from the fact that the numerator is negative because Eν e−γZ − e(1−γ)Z > 0. Moreover, ζ0 < |bσλ2 − κ| = κ − bσλ2, so ζ0 +bσλ2 −κ < 0, implying that the denominator is also negative. If bσλ2 < κ, then by similar reasoning, b0(τ) is positive for τ less than the maturity at which bond prices become inﬁnite. Therefore, an increase in the risk of a disaster raises prices of long-term default-free bonds, not surprisingly, since an increase in the risk of a disaster decreases the riskfree rate.

- Case 2: (bσλ2 − κ)2 − 2Eν e−γZ − e(1−γ)Z σλ2 < 0 This case applies for the calibrations given in this paper. Here, the solution takes the form

1 σλ2

η tan

b0(τ) =

1 2

ητ + arctan

bσλ2 − κ η −

bσλ2 − κ σλ2

, (B.7)

32Consider the case of bσλ2 −κ < 0. Then ζ0 < κ−bσλ2. It follows that the denominator in (B.4) is negative for all τ, and that b0(τ) exists for all τ > 0. Now consider bσλ2 −κ > 0. Then ζ0 < bσλ2 −κ. For τ suﬃciently small, the second term in the denominator 2ζ0 exceeds the ﬁrst term (ζ0 + bσλ2 − κ) 1 − e−ζ

0τ , and so the

denominator is negative. As τ approaches inﬁnity, however, the denominator approaches bσλ2 − κ − ζ0 > 0. Because the denominator is a continuous function, there must exist a τ for which it equals zero.

where

η = 2Eν [e−γZ − e(1−γ)Z]σλ2 − (bσλ2 − κ)2. and where arctan(·) denotes the inverse tangent function.33 It follows that

a0(τ) =

 

 . (B.8)

2 λ−κ

cos 2 1ητ + arctan bσ

κλ¯ σλ2

2κλ¯ σλ2

η

(bσλ2 − κ) τ −

−µ − β + γσ2 −

log

2 λ−κ

cos arctan bσ

η

2 λ−κ

The functions a0(τ) and b0(τ) approach inﬁnity as 21ητ + arctan bσ

η approaches π/2 (where π denotes the geometric constant). Real bond prices therefore become unbounded at a ﬁnite maturity. For the baseline calibration, this occurs at a maturity of 33 years. While this conclusion may seem extreme, it is useful to remember that even a very small probability of default would change this result.

Figure B.1 shows zero-coupon bond yields for λ at zero, at its mean, and at the 90th percentile, for parameter values given in Table 1. The ﬁgure shows that the yield curve shifts down as the disaster probability shifts up. As mentioned above, the yield curves are downward sloping because of the negative risk premia on bonds. The slope increases in magnitude with an increase in the disaster probability. While Treasury yield curves are upward sloping on average in the data, there are several diﬀerences between these yield curves and the ones in the paper. First, Treasury bonds are subject to inﬂation risk. Because inﬂation might be expected to rise in the event of a disaster, or perhaps with even an increased probability of disaster, introducing inﬂation could very well lead to positive risk premia on nominal bonds. Because inﬂation is a persistent process, long-term bonds carry greater exposure to this risk than short-term bonds. This could lead to an upward slope of the term structure. Second, all government bonds are subject to some risk of default, either through inﬂation or outright. Because default could be expected to eﬀect all debt outstanding when it occurs, long-term bonds would again be exposed to more risk. To summarize, because

33While this solution appears very diﬀerent from that in (B.7), they can both be expressed in terms of the hyperbolic tangent.

the main economic force causing very low yields is the protection that bonds oﬀer in very bad states (when short-term interest rates are low), introducing inﬂation or default in these states would signiﬁcantly change these results.

## C Solution to the power utility model

Consider time-separable utility with

∞

Cs1−γ 1 − γ

e−βs

Vt = Et

ds.

t

The state-price density for this model takes the familiar form

πt = e−βtCt−γ. (C.1) Ito’s Lemma implies that the state-price density follows the process

dπt πt−

= µπ,t dt + σπ,t[dBt dBλ,t] + (e−γZ − 1)dNt, where

- 1

- 2

γ(γ + 1)σ2. (C.2) and

µπ,t = −β − γµ +

σπ,t = [−γσ 0]. (C.3) Risk of changes in the disaster probability are not priced in the power utility model.

The absence of arbitrage implies

µπ,t = −rt − λtEν e−γZ − 1 , (C.4) It follows from (C.2) that the riskfree rate under power utility is given by

rt = β + γµ −

1 2

γ(γ + 1)σ2 − λtEν e−γZ − 1 .

As in the recursive utility model, let F(Dt,λt) denote the price of the dividend claim and H(Dt,λt,τ) the price of zero-coupon equity with maturity τ. Equations (A.18) and (A.23) are still satisﬁed, except of course the process for πt is diﬀerent. The solution takes the form

H(Dt,λt,τ) = Dt exp{ap,φ(τ) + bp,φ(τ)λ},

where ap,φ(τ) and bp,φ(τ) satisfy ordinary diﬀerential equations

a p,φ(τ) = µD − γµ − β +

1 2

γ(γ + 1)σ2 − γσ2φ + κλb¯ p,φ(τ)

and

b p,φ(τ) =

1 2

σλ2bp,φ(τ)2 − κbp,φ(τ) + Eν e(φ−γ)Z − 1 .

with boundary conditions ap,φ(0) = bp,φ(0) = 0. These ordinary diﬀerential equations take the same form as those in the recursive utility case and therefore have analogous solutions given in the main text.

The equity premium for power utility can be computed in the same way as for recursive utility (see Appendix A.4). The equity premium is given by

rte − rt = −σπ,tσ F,t + λtEν (e−γZ − 1)(1 − eφZ) . Thus the equity premium takes the same general form as under recursive utility. However, σπ,t is diﬀerent. Ito’s Lemma implies

σF,t = φσ (G (λt)/G(λt))σλ λt .

Therefore, from (C.3), it follows that

rte − rt = φγσ2 + λtEν (e−γZ − 1)(1 − eφZ) .

# References

Abel, Andrew, 1999, Risk premia and term premia in general equilibrium, Journal of Monetary Economics 43, 3–33.

Bansal, Ravi, and Amir Yaron, 2004, Risks for the long-run: A potential resolution of asset pricing puzzles, Journal of Finance 59, 1481–1509.

Barro, Robert J., 2006, Rare disasters and asset markets in the twentieth century, The Quarterly Journal of Economics pp. 823–866.

Barro, Robert J., 2009, Rare disasters, asset prices, and welfare costs, forthcoming, American Economic Review.

- Barro, Robert J., and Jose F. Ursua, 2008, Macroeconomic crises since 1870, Brookings Papers on Economic Activity no. 1, 255–350.
- Barro, Robert J., and Jose F. Ursua, 2009, Stock-market crashes and depressions, NBER Working Paper No. 14760.

Berkman, Henk, Ben Jacobsen, and John Lee, 2010, Time-varying rare disaster risk and stock returns, forthcoming, Journal of Financial Economics.

Binsbergen, Jules H. van, Michael W. Brandt, and Ralph S. Koijen, 2011, On the Timing and Pricing of Dividends, Forthcoming, American Economic Review.

Black, Fischer, 1976, Studies of stock price volatility changes, in Proceedings of the Business and Economic Satistics Section, American Statistical Association (American Statistical Association, Washington ).

Campbell, John Y., 2003, Consumption-based asset pricing, in G. Constantinides, M. Harris, and R. Stulz, eds.: Handbook of the Economics of Finance, vol. 1b (Elsevier Science, NorthHolland ).

Campbell, John Y., and John H. Cochrane, 1999, By force of habit: A consumption-based explanation of aggregate stock market behavior, Journal of Political Economy 107, 205– 251.

Campbell, John Y., and Robert J. Shiller, 1988, The dividend-price ratio and expectations of future dividends and discount factors, Review of Financial Studies 1, 195–228.

Cochrane, John H., 1992, Explaining the variance of price-dividend ratios, Review of Financial Studies 5, 243–280.

Cochrane, John H., 1994, Permanent and transitory components of GDP and stock prices, Quarterly Journal of Economics 109, 241–265.

Constantinides, George M., 2008, Discussion of ‘Macroeconomic crises since 1870’, Brookings Papers on Economic Activity no. 1, 336–350.

Cox, John C., Jonathan C. Ingersoll, and Stephen A. Ross, 1985, A theory of the term structure of interest rates, Econometrica 53, 385–408.

Dittmar, Robert F., 2002, Nonlinear Pricing Kernels, Kurtosis Preference, and Evidence from the Cross Section of Equity Returns, The Journal of Finance 57, pp. 369–403.

Drechsler, Itamar, and Amir Yaron, 2011, What’s vol got to do with it, Review of Financial Studies 24, 1–45.

Duﬃe, Darrell, and Larry G Epstein, 1992, Asset pricing with stochastic diﬀerential utility, Review of Financial Studies 5, 411–436.

Duﬃe, Darrell, Jun Pan, and Kenneth Singleton, 2000, Transform analysis and asset pricing for aﬃne jump-diﬀusions, Econometrica 68, 1343–1376.

Duﬃe, Darrell, and Costis Skiadas, 1994, Continuous-time asset pricing: A utility gradient approach, Journal of Mathematical Economics 23, 107–132.

Epstein, Larry, and Stan Zin, 1989, Substitution, risk aversion and the temporal behavior of consumption and asset returns: A theoretical framework, Econometrica 57, 937–969.

Eraker, Bjorn, and Ivan Shaliastovich, 2008, An Equilibrium Guide to Designing Aﬃne Pricing Models, Mathematical Finance 18, 519–543.

Fama, Eugene F., and Kenneth R. French, 1989, Business conditions and expected returns on stocks and bonds, Journal of Financial Economics 25, 23–49.

Fama, Eugene F., and Kenneth R. French, 2001, Disappearing dividends: changing ﬁrm characteristics or lower propensity to pay?, Journal of Financial Economics 60, 3 – 43.

Feller, William, 1951, Two Singular Diﬀusion Problems, The Annals of Mathematics 54, 173–182.

- Gabaix, Xavier, 2008a, An exactly solved framework for ten puzzles in macro-ﬁnance, NBER Working Paper No. 13724.
- Gabaix, Xavier, 2008b, Linearity-generating processes: A modelling tool yielding closed forms for asset prices, Working paper, New York University.

Glasserman, Paul, 2004, Monte Carlo Methods in Financial Engineering. (Springer Science

+ Business Media New York, New York).

- Gourio, Fran¸cois, 2008a, Disasters and Recoveries, The American Economic Review Papers and Proceedings 98, pp. 68–73.
- Gourio, Fran¸cois, 2008b, Time-series predictability in the disaster model, Finance Research Letters 5, 191 – 203.

Hall, Robert E., 1988, Intertemporal substitution in consumption, Journal of Political Economy 96, 221–273.

Harvey, Campbell, 1989, Time-varying conditional covariances in tests of asset pricing models, Journal of Financial Economics 24, 289–317.

Harvey, Campbell R., and Akhtar Siddique, 2000, Conditional skewness in asset pricing tests, The Journal of Finance 55, pp. 1263–1295.

Hodrick, Robert J., 1992, Dividend yields and expected stock returns: Alternative procedures for inference and measurement, Review of Financial Studies 5, 357–386.

Keim, Donald B., and Robert F. Stambaugh, 1986, Predicting returns in the stock and bond markets, Journal of Financial Economics 17, 357–390.

Kreps, D., and E. Porteus, 1978, Temporal resolution of uncertainty and dynamic choice theory, Econometrica 46, 185–200.

LeRoy, Stephen F., and Richard D. Porter, 1981, The present-value relation: Tests based on implied variance bounds, Econometrica 49, 555–574.

Lettau, Martin, and Sydney C. Ludvigson, 2001, Consumption, aggregate wealth and expected stock returns, Journal of Finance 56, 815–849.

Lettau, Martin, and Sydney C. Ludvigson, 2005, Expected returns and expected dividend growth, Journal of Financial Economics 76, 583–626.

Lettau, Martin, and Jessica A. Wachter, 2007, Why is long-horizon equity less risky? A duration-based explanation of the value premium, Journal of Finance 62, 55–92.

Liu, Jun, Jun Pan, and Tan Wang, 2005, An equilibrium model of rare-event premia and its implication for option smirks, Review of Financial Studies 18, 131–164.

Longstaﬀ, Francis A., and Monika Piazzesi, 2004, Corporate earnings and the equity premium, Journal of Financial Economics 74, 401–421.

Maddison, Angus, 2003, The World Economy: Historical Statistics. (OECD Paris).

Martin, Ian, 2008, Consumption-based asset pricing with higher cumulants, Working paper, Stanford University.

Mehra, Rajnish, and Edward Prescott, 1985, The equity premium puzzle, Journal of Monetary Economics 15, 145–161.

Menzly, Lior, Tano Santos, and Pietro Veronesi, 2004, Understanding predictability, Journal of Political Economy 112, 1–47.

Naik, Vasanttilak, and Moon Lee, 1990, General equilibrium pricing of options on the market portfolio with discontinuous returns, Review of Financial Studies 3, 493–521.

Nakamura, Emi, Jon Steinsson, Robert Barro, and Jose Ursua, 2011, Crises and recoveries in an empirical model of consumption disasters, Working paper, Columbia University and Harvard University.

Nelson, Daniel B., 1991, Conditional heteroskedasticity in asset returns: A new approach, Econometrica 59, 347–370.

Rietz, Thomas A., 1988, The equity risk premium: A solution, Journal of Monetary Economics 22, 117–131.

Santa-Clara, Pedro, and Shu Yan, 2006, Crashes, volatility, and the equity premium: Lessons from S&P 500 options, Working paper, UCLA and University of Arizona.

Schwert, William G., 1989, Why does stock market volatility change over time?, Journal of Finance 44, 1115–1153.

Shiller, Robert J., 1981, Do stock prices move too much to be justiﬁed by subsequent changes in dividends?, American Economic Review 71, 421–436.

Shiller, Robert J., 1989, Market Volatility. (MIT Press Cambridge, MA).

Tauchen, George, 2005, Stochastic volatility in general equilibrium, Working paper, Duke University.

Veronesi, Pietro, 2004, The Peso problem hypothesis and stock market returns, Journal of Economic Dynamics and Control pp. 707–725.

Vissing-Jørgensen, Annette, 2002, Limited Asset Market Participation and the Elasticity of Intertemporal Substitution, Journal of Political Economy 110, 825–853.

Weil, Philippe, 1990, Nonexpected utility in macroeconomics, Quarterly Journal of Economics 105, 29–42.

Weitzman, Martin L., 2007, Subjective Expectations and Asset-Return Puzzles, The American Economic Review 97, pp. 1102–1130.

Table 1: Parameters for the time-varying disaster risk model

Relative risk aversion γ 3.0 Rate of time preference β 0.012 Average growth in consumption (normal times) µ 0.0252 Volatility of consumption growth (normal times) σ 0.020 Leverage φ 2.6 Average probability of a rare disaster λ¯ 0.0355 Mean reversion κ 0.080 Volatility parameter σλ 0.067 σλE λ1/2 0.0114 Probability of default given disaster q 0.40

Notes: The table shows parameter values for the time-varying disaster risk model. The process for the disaster intensity is given by

dλt = κ(λ¯ − λt)dt + σλ λt dBλ,t.

The consumption (endowment) process is given by

dCt = µCt dt + σCt dBt + (eZ

t

− 1)Ct− dNt,

where Nt is a Poisson process with intensity λt, and Zt is calibrated to the distribution of large declines in GDP in the data. The dividend Dt equals Ctφ. The representative agent has recursive utility deﬁned by Vt = Et t ∞ f(Cs,Vs)ds, with normalized aggregator

f(C,V ) = β(1 − γ)V log C −

Parameter values are in annual terms.

1 1 − γ

log((1 − γ)V ) .

Table 2: Population moments from simulated data and sample moments from the historical time series

Model U.S. Data Population Conditional

E[Rb] 0.99 1.36 1.34 σ(Rb) 3.79 2.00 2.66 E[Re − Rb] 7.61 8.85 7.06 σ(Re) 19.89 17.66 17.72

Sharpe Ratio 0.39 0.49 0.40 σ(∆c) 6.36 1.99 1.34 σ(∆d) 16.53 5.16 6.59

Notes: The model is simulated at a monthly frequency and simulated data are aggregated to an annual frequency. Data moments are calculated using overlapping annual observations constructed from quarterly U.S. data, from 1947 through the ﬁrst quarter of 2010. With the exception of the Sharpe ratio, moments are in percentage terms. The second column reports population moments from simulated data. The third column reports moments from simulated data that are calculated over years in which a disaster did not occur. The last column reports annual sample moments. Rb denotes the gross return on the government bond, Re the gross equity return, ∆c growth in log consumption and ∆d growth in log dividends.

Table 3: Long-horizon regressions: Excess returns

Horizon in years 1 2 4 6 8 10

- Panel A: Model – Population moments

β1 -0.11 -0.22 -0.40 -0.56 -0.69 -0.82 R2 0.04 0.08 0.15 0.20 0.23 0.26

- Panel B: Model – Conditional moments

β1 -0.16 -0.30 -0.56 -0.77 -0.95 -1.10 R2 0.13 0.24 0.41 0.52 0.59 0.63 Panel B: U.S. Data

β1 -0.13 -0.23 -0.33 -0.48 -0.64 -0.86 t-stat -2.62 -2.87 -3.64 -4.80 -5.82 -5.67 R2 0.09 0.17 0.23 0.30 0.38 0.43

Notes: Excess returns are regressed on the lagged price-dividend ratio in data simulated from the model and in quarterly data from 1947 to 2010.1. Speciﬁcally, the table reports coeﬃcients β1, R2 statistics and, for the sample, Newey-West t-statistics for regressions

- h
- i=1

log(Rte+i) − log(Rtb+i) = β0 + β1(pt − dt) + t,

where Rte+i and Rtb+i are, respectively, the return on the aggregate market and the return on the government bill between t + i − 1 and t + i and pt − dt is the log price-dividend ratio on the aggregated market. The time-varying disaster risk model is simulated at a monthly frequency and simulated data are aggregated to an annual frequency. Panel A reports population moments from simulated data. Panel B reports moments from simulated data that are calculated over years in which a disaster does not take place (for a horizon of 2, for example, all 2-year periods in which a disaster takes place are eliminated). Panel C reports sample moments.

Table 4: Long-horizon regressions: Consumption growth

Horizon in years 1 2 4 6 8 10

Panel A: Model – Population moments

β1 0.02 0.04 0.07 0.10 0.12 0.13 R2 0.01 0.02 0.04 0.05 0.06 0.06

Panel B: U.S. Data β1 -0.001 -0.006 -0.009 -0.011 -0.016 -0.014 t-stat -0.22 -0.85 -1.02 -1.15 -1.09 -0.79 R2 0.0006 0.0137 0.0164 0.0180 0.0268 0.0162

Notes: Growth in aggregate consumption is regressed on the lagged price-dividend ratio in data simulated from the model and in quarterly data from 1947 to 2010.1. Speciﬁcally, the table reports coeﬃcients β1, R2 statistics and, for the sample, Newey-West t-statistics for regressions

- h
- i=1

∆ct+i = β0 + β1(pt − dt) + t,

where ∆ct+i is log growth in aggregate consumption between periods t + i − 1 and t + i and pt − dt is the log price-dividend ratio on the aggregated market. The time-varying disaster risk model is simulated at a monthly frequency and simulated data are aggregated to an annual frequency. Panel A reports population moments from simulated data. Panel B reports sample moments. The conditional moments, namely the slope coeﬃcient and the R2 calculated over periods in the simulation without disasters, are equal to zero.

Table 5: Results from alternative calibrations

Model U.S. Data Population Conditional

- Panel A: Calibration with OECD disasters

- E[Rb] 1.56 1.86 1.34 σ(Rb) 3.38 1.75 2.66 E[Re − Rb] 6.82 7.83 7.06 σ(Re) 20.13 18.33 17.72 Sharpe Ratio 0.35 0.42 0.40 σ(∆c) 5.86 1.99 1.34 σ(∆d) 15.24 5.16 6.59

Panel B: Calibration with disasters of moderate severity and γ = 6

- E[Rb] 2.74 2.89 1.34 σ(Rb) 1.58 0.61 2.66 E[Re − Rb] 5.48 6.06 7.06 σ(Re) 16.44 15.69 17.72 Sharpe Ratio 0.34 0.38 0.40 σ(∆c) 3.08 1.99 1.34 σ(∆d) 8.02 5.16 6.59

Notes: Panel A describes data simulated from the model when the distribution of disasters are calibrated to those from OECD countries only. The average disaster probability λ¯ = 2.86% per annum; all other parameters (including σλ) is unchanged. Panel B describes data simulated from the model when the distribution of disasters is as in Panel A, except that realizations are cut in half. Risk aversion γ is set equal to 6, and λ¯ = 2.86%. All other parameter values are unchanged.

##### Figure 1: Distribution of the disaster probability, λt

20

15

density

10

5

0

0 0.05 0.1 0.15 0.2 0.25

disaster probability

100

10−1

λP(>x)

10−2

10−3

10−4

0 0.05 0.1 0.15 0.2 0.25

x

##### Notes: The top panel shows the probability density function for λt, the time-varying intensity (per year) of a disaster. The solid vertical line is located at the unconditional mean of the process. The bottom panel shows the probability that λ exceeds a value x, for x ranging from 0 to 0.25. The y-axis on the bottom panel uses a log (base–10) scale. Parameter values are given in Table 1.

Figure 2: Distribution of consumption declines in the event of a disaster

Panel A: All countries

20

18

16

14

Frequency

12

10

8

6

4

2

0

10 20 30 40 50 60 70

##### Panel B: OECD countries

10

8

Frequency

6

4

2

0

10 20 30 40 50 60

Percent decline in consumption

##### Notes: Histograms show the distribution of large consumption declines (in percentages). Panel A shows data for 22 countries, 17 of which are OECD countries and 5 of which are not; Panel B shows data for the subsample of OECD countries. Data are from Barro and Ursua (2008). Panel A is the distribution of 1−eZ in the baseline calibration, while Panel B is the distribution of 1 − eZ in the calibration discussed in Section 3.4.

##### Figure 3: Government bill return in the time-varying disaster risk model

0.04

0.02

0

expectedreturn

−0.02

−0.04

−0.06

|government bill expected return<br><br>government bill yield<br><br>riskfree rate<br><br>|
|---|

−0.08

0 0.02 0.04 0.06 0.08 0.1

disaster probability

##### Notes: This ﬁgure shows rb, the instantaneous expected return on a government bill; rL, the instantaneous expected return on the bill conditional on no default and r, the rate of return on a default-free security as functions of the disaster intensity λ. All returns are in annual terms.

Figure 4: Decomposition of the equity premium in the time-varying disaster risk model

0.2

|standard model<br><br>static disaster risk<br><br>time−varying disaster risk<br><br>|
|---|

0.18

0.16

0.14

riskpremium

0.12

0.1

0.08

0.06

0.04

0.02

0

0 0.02 0.04 0.06 0.08 0.1

disaster probability

Notes: The solid line shows the instantaneous equity premium (the expected excess return on equity less the expected return on the government note), the dashed line shows the equity premium in a static model with disaster risk and the dotted line shows the what the equity premium would be if disaster risk were zero.

##### Figure 5: Equity volatility in the time-varying disaster risk model

0.24

0.22

0.2

0.18

0.16

volatility

0.14

0.12

0.1

0.08

0.06

0.04

0 0.02 0.04 0.06 0.08 0.1

disaster probability

##### Notes: The ﬁgure shows instantaneous equity return volatility as a function of the disaster probability λt. All quantities are in annual terms.

##### Figure 6: Sharpe ratio in the time-varying disaster risk model

0.8

0.7

0.6

0.5

Sharperatio

0.4

0.3

0.2

0.1

0

0 0.02 0.04 0.06 0.08 0.1

disaster probability

##### Notes: This ﬁgure shows the instantaneous equity premium over the government bill divided by the instantaneous equity return volatility (the Sharpe ratio) as a function of disaster probability λt. All quantities are in annual terms.

Figure 7: Risk premia on zero-coupon equity

0.1

|standard model<br><br>time−varying disaster risk<br><br>|
|---|

0.09

0.08

0.07

Riskpremia

0.06

0.05

0.04

0.03

0.02

0.01

0

0 5 10 15 20 25 30 35 40

Maturity (years)

Notes: This ﬁgure shows average risk premia on zero-coupon equity claims as a function of maturity. Zero-coupon equity is a claim to the aggregate dividend at a single point in time (referred to as the maturity). Risk premia are deﬁned as expected excess returns less the riskfree rate. The dotted line shows what risk premia would be if the disaster risk were zero. The solid line shows risk premia in the model. Risk premia are expressed in annual terms.

##### Figure 8: Implied disaster probabilities

0.14

0.12

0.1

Disasterprobability

0.08

0.06

0.04

0.02

0

1890 1910 1930 1950 1970 1990 2010

##### Notes: This ﬁgure shows the disaster probability λt implied by historical values of the ratio of the price divided to the previous ten years of earnings for the S&P 500 index. This ratio is de-meaned and set equal to the price-dividend ratio in the model (also de-meaned). The disaster probability is found by inverting the equation for the price-dividend ratio; when the resulting value of λt is negative, it is set to zero. The solid line marks the average value the disaster probability.

##### Figure B.1: Yields on zero-coupon bonds

0.05

0

- −0.4

−0.35

−0.3

−0.25

−0.2

−0.15

−0.1

- −0.05

Yield

|zero probability<br><br>average probability<br><br>90th percentile probability<br><br>|
|---|

−0.45

0 5 10 15 20 25 30

Maturity (years)

Notes: This ﬁgure shows continuously-compounded yields to maturity on default-free zerocoupon bonds as a function of maturity. Yields are shown for three values of the disaster probability: zero, average, and the 90th percentile critical value. Yields are in annual terms.

