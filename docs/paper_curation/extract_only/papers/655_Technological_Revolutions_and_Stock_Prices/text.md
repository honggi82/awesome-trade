NBER WORKING PAPER SERIES

TECHNOLOGICAL REVOLUTIONS AND STOCK PRICES Lubos Pastor Pietro Veronesi Working Paper 11876 http://www.nber.org/papers/w11876

NATIONAL BUREAU OF ECONOMIC RESEARCH 1050 Massachusetts Avenue Cambridge, MA 02138 December 2005 Revised February 2008

We thank Sreedhar Bharath, Markus Brunnermeier, Leonid Kogan, Lars Lochstoer, Lu Zhang, and

    especially Judy Chevalier and two anonymous referees for very helpful comments. We also thank Malcolm Baker, Robert Barro, Efraim Benmelech, Gene Fama, Bob Fogel, Boyan Jovanovic, John Heaton, Ali Lazrak, Robert Novy-Marx, Rob Stambaugh, Dmitriy Stolyarov, and the audiences at the 2008 AEA meeting, 2007 AFA meeting, 2006 EFA meeting, 2006 UBC Summer Conference, Fall 2005 NBER Asset Pricing meeting, CERGE-EI Prague, Dartmouth College, Ente Einaudi, Harvard University, Indiana University, London Business School, London School of Economics, New York University, Stockholm Institute for Financial Re- search, Stockholm School of Economics, University of Chicago, University of Pennsylvania, and University of Vienna. Shastri Sandy has provided valuable research assistance. The views expressed herein are those of the author(s) and do not necessarily reflect the views of the National Bureau of Economic Research.

© 2005 by Lubos Pastor and Pietro Veronesi. All rights reserved. Short sections of text, not to exceed two paragraphs, may be quoted without explicit permission provided that full credit, including © notice, is given to the source.

Technological Revolutions and Stock Prices Lubos Pastor and Pietro Veronesi NBER Working Paper No. 11876 December 2005, Revised February 2008 JEL No. G1

### ABSTRACT

We develop a general equilibrium model in which stock prices of innovative firms exhibit "bubbles" during technological revolutions. In the model, the average productivity of a new technology is uncertain and subject to learning. During technological revolutions, the nature of this uncertainty changes from idiosyncratic to systematic. The resulting "bubbles" in stock prices are observable ex post but unpredictable ex ante, and they are most pronounced for technologies characterized by high uncertainty and fast adoption. We find empirical support for the model’s predictions in 1830-1861 and 1992-2005 when the railroad and Internet technologies spread in the United States.

Lubos Pastor Graduate School of Business University of Chicago 5807 South Woodlawn Ave Chicago, IL 60637 and NBER lubos.pastor@chicagogsb.edu

Pietro Veronesi Graduate School of Business University of Chicago 5807 South Woodlawn Avenue Chicago, IL 60637 and NBER pietro.veronesi@gsb.uchicago.edu

“Technological revolutions and ﬁnancial bubbles seem to go hand in hand.” The Economist, Sep 21, 2000.

# 1. Introduction

Technological revolutions tend to be accompanied by bubble-like patterns in the stock prices of ﬁrms that employ the new technology. After an initial surge, stock prices of innovative ﬁrms usually fall in the presence of high volatility. Recent examples of such price patterns include the “Internet craze” of the late 1990s, the “biotech revolution” of the early 1980s, and the “tronics boom” of the early 1960s, as characterized by Malkiel (1999).1 Other examples include the 1920s and the turn of the 20th century; in both periods, technological innovation spread rapidly while the stock market boomed and then faltered (e.g., Shiller, 2000).2

The bubble-like stock price behavior during technological revolutions is frequently attributed to market irrationality (e.g., Shiller, 2000, Perez, 2002). We propose another possible explanation that does not involve irrationality. We argue that new technologies are characterized by high uncertainty about their future productivity, and that the time-varying nature of this uncertainty can also produce the observed stock price patterns.

We build a general equilibrium model of a ﬁnite-horizon representative-agent economy with two sectors: the “new economy” and the “old economy.” The old economy implements the existing technologies in large-scale production whose output determines the representative agent’s wealth. The new economy, which is created when a new technology is invented, implements the new technology in small-scale production that does not aﬀect the agent’s wealth. It is optimal for the new technology to be initially employed on a small scale because its future productivity is uncertain. By observing the new economy, the representative agent learns about the average productivity of the new technology before deciding whether to adopt the technology on a large scale. We show that this irreversible adoption takes place if the agent learns that the new technology is suﬃciently productive. We deﬁne a technological revolution as a period concluded by a large-scale adoption of a new technology.

We show that the nature of the risk associated with new technologies changes over time. Initially, this risk is mostly idiosyncratic due to the small scale of production and a low probability of a large-scale adoption. The risk remains idiosyncratic for those technologies

[Figure 1]

- 1According to Malkiel (1999), “What electronics was to the 1960s, biotechnology became to the 1980s... Valuation levels of biotechnology stocks reached levels previously unknown to investors... From the mid-1980s to the late 1980s, most biotechnology stocks lost three-quarters of their market value.”
- 2“Every previous technological revolution has created a speculative bubble... With each wave of technology, share prices soared and later fell... The inventions of the late 19th century drove p-e ratios to a peak in 1901, the year of the ﬁrst transatlantic radio transmission. By 1920 shares prices had dropped by 70% in real terms. The roaring twenties were also seen as a “new era”: share prices soared as electricity boosted eﬃciency and car ownership spread. After peaking in 1929, real share prices tumbled by 80% over the next three years.” (The Economist, September 21, 2000, Bubble.com)

that are never adopted on a large scale. For the technologies that are ultimately adopted, however, the risk must gradually change from idiosyncratic to systematic. As the probability of adoption increases, the new technology becomes more likely to aﬀect the old economy and with it the representative agent’s wealth, so systematic risk in the economy increases.

This time-varying nature of risk has interesting implications for stock prices. Initially, while uncertainty about the new technology is mostly idiosyncratic, the new economy stocks command high market values. As the adoption probability increases, the resulting increase in systematic risk pushes up the discount rates and thus depresses stock prices in both the new and old economies. The new economy stock prices fall deeper because their discount rates rise higher due to an increase in the new economy’s market beta.

Stock prices are aﬀected not only by discount rates but also by expected cash ﬂows. The technologies that are ultimately adopted must turn out to be suﬃciently productive before the adoption. This positive cash ﬂow news pushes stock prices up, countervailing the eﬀect of the higher discount rate. The cash ﬂow eﬀect prevails initially, pushing the new economy stock prices up, but the discount rate eﬀect prevails eventually, pushing the stock prices down. The resulting pattern in the new economy stock prices looks like a bubble but it obtains under rational expectations through a general equilibrium eﬀect.

The bubble-like pattern in stock prices arises in part due to an ex post selection bias. Researchers study technological revolutions with the ex post knowledge that the revolutions took place, but investors living through those periods did not know whether the new technologies would eventually be adopted on a large scale. The representative agent in our model never expects stock prices to fall; she always expects to earn positive stock returns commensurate to the stocks’ riskiness, and she subsequently earns those fair returns, on average. However, in those rare periods that are recognized as technological revolutions ex post, the agent’s realized returns tend to be initially positive due to good news about productivity and eventually negative due to bad news about systematic risk.

Uncertainty about new technologies aﬀects not only the level but also the volatility of stock prices. Due to this uncertainty, the new economy stocks are more volatile than the old economy stocks. After an initial decline, the new economy’s volatility rises sharply when the stochastic discount factor becomes more volatile as a result of a higher probability of a large-scale adoption. The same eﬀect also pushes up the new economy’s market beta and the old economy’s volatility, two diﬀerent aspects of systematic risk in the economy.

Our model makes many empirical predictions for technological revolutions: The “bubble”

in stock prices should be much stronger in the new economy than in the old economy; stock prices in both economies should reach the bottom at the end of the revolution; the new economy’s market beta should increase sharply before the end of the revolution; the new economy’s volatility should also rise sharply and it should exceed the old economy’s volatility; the old economy’s volatility should rise but less than the new economy’s volatility; the new economy’s beta and both volatilities should all peak at the end of the revolution; and the old economy’s productivity should begin rising at the end of the revolution.

All of these predictions are supported by empirical evidence from the recent Internet revolution. According to the model, this revolution ended (i.e., the probability of a large-scale adoption of the Internet technology reached one) in 2002. The “bubble” pattern was much stronger in the NASDAQ index (our proxy for the new economy) than in the NYSE/AMEX index (the old economy); both stock price indexes reached the bottom in 2002; NASDAQ’s beta doubled between 1997 and 2002; NYSE/AMEX’s return volatility also doubled and NASDAQ’s volatility tripled over the same period; NASDAQ’s volatility always exceeded NYSE/AMEX’s volatility; NASDAQ’s beta and both volatilities peaked in 2002; and the productivity growth of the U.S. economy accelerated sharply after 2002.

We also examine stock prices during the ﬁrst major technological revolution in the U.S. since the opening of the U.S. stock market – the introduction of steam-powered railroads. In the 1830s and 40s, there was substantial uncertainty about whether the railroad technology would be adopted on a large scale. We analyze stock prices before the Civil War, and ﬁnd that they fell before and during year 1857, with railroad stocks falling more than nonrailroad stocks. The railroad stock volatility and price-dividend ratios consistently exceeded their non-railroad counterparts. The volatility of all stocks rose in 1857. The railroad stock beta increased sharply in the 1850s, before falling right after 1857. In the context of our model, all of this evidence is consistent with a large-scale adoption of the railroad technology around 1857, soon after railroads began expanding west of the Mississippi River.

Much of the literature on technological innovation analyzes issues diﬀerent from those addressed here. Unlike Romer (1990), Aghion and Howitt (1992), and others, we take technological inventions to be exogenous. We do not examine the links between technological revolutions and human capital (e.g., Chari and Hopenhayn, 1991, Caselli, 1999, Manuelli, 2003). Diﬀerent but related models of learning are presented in Jovanovic (1982), Jovanovic and Nyarko (1996), and Atkeson and Kehoe (2007). We empirically examine the Internet and railroad revolutions, while other technological revolutions are examined by Jovanovic and Rousseau (2003, 2005), Mazzucato (2002), and others. Mokyr (1990) argues that tech-

nological progress is discontinuous, as assumed in our model, and that occasional seminal inventions (“macroinventions”) are the key sources of economic growth.

A small but growing literature explores the links between technological innovation and stock prices (e.g., Jovanovic and MacDonald, 1994, and Laitner and Stolyarov, 2003, 2004a,b). According to Greenwood and Jovanovic (1999) and Hobijn and Jovanovic (2001), innovation causes the stock market to drop because the incumbent ﬁrms are unable or unwilling to implement the new technology. Similar initial stock market drops are obtained in the models of Laitner and Stolyarov (2003) and Manuelli (2003). In our model, the stock market value of the old economy also drops after the new technology is invented, mostly because of the costs and risks associated with a large-scale adoption of the new technology, but our focus is on the subsequent bubble-like stock price pattern in the new economy.

The paper is organized as follows. Section 2 presents the model. Section 3 solves for stock prices and analyzes their dynamics. Section 4 investigates the model’s empirical predictions for stock prices during technological revolutions. Section 5 empirically examines the behavior of stock prices in 1830–1861 and 1992–2005 when the railroad technology and the Internet technologies, respectively, spread in the United States. Section 6 concludes.

# 2. The Economy

We consider an economy with a ﬁnite horizon [0,T]. A representative agent has preferences deﬁned by power utility over terminal wealth WT, with risk aversion γ > 1:

WT1−γ 1 − γ

. (1)

u(WT) =

[Figure 2]

At time t = 0, the agent is endowed with capital B0. Subsequently, capital is invested in a linear technology producing output (net of depreciation) at the rate of Yt = ρtBt. Since there is no intermediate consumption, all output is reinvested, and capital Bt follows

dBt = Ytdt = ρtBtdt. (2) Productivity ρt follows a mean-reverting process whose mean is determined by the available technology. There are two technologies: “old” and “new.” Initially, only the old technology is available, and the long-run mean of ρt is equal to ρ. At time t∗, the new technology becomes available. If the representative agent adopts the new technology at time t∗∗ ≥ t∗, the long-run mean of ρt changes from ρ to ρ + ψ. Thus, the dynamics of ρt are given by

[Figure 3]

[Figure 4]

[Figure 5]

dρt = φ(ρ − ρt)dt + σdZ0,t, 0 < t < t∗∗ (3) dρt = φ(ρ + ψ − ρt)dt + σdZ0,t, t∗∗ ≤ t < T, (4)

[Figure 6]

[Figure 7]

where φ is the speed of mean reversion, ρ is the mean productivity of the old technology, ψ is the “productivity gain” brought by the new technology, and σ2 is the variance of productivity shocks, represented by the Brownian increments dZ0,t. That is, the adoption of the new technology is equivalent to a shift in the economy’s average productivity.

[Figure 8]

The representative agent chooses whether and when to adopt the new technology to maximize utility in equation (1) under the market-clearing condition WT = BT. In equilibrium, the agent’s ﬁnal wealth must equal the amount of capital accumulated by time T.

Our key assumption is that the productivity gain ψ is unobservable. When the new technology appears at time t∗, ψ is drawn from a normal distribution with known variance:

ψ ∼ N 0, σt2∗ . (5)

All other parameters are known. The adoption of the new technology is irreversible and costly. Converting capital to the new technology incurs a proportional conversion cost κ ≥ 0.

The agent has three choices at time t∗ when the new technology becomes available:

- (i) Adopt the new technology
- (ii) Begin learning about the new technology (i.e., about ψ)
- (iii) Discard the new technology

We show below that the agent optimally chooses option (ii), so he begins learning at time t∗. The agent learns about ψ by “experimenting” with the new technology – i.e., by implementing it on a small scale. After time t∗, the economy consists of two sectors: the small-scale “new economy,” which employs the new technology, and the large-scale “old economy,” whose productivity ρt follows equation (3). The capital BtN used in the new economy is inﬁnitely smaller than Bt, so the agent’s wealth WT is aﬀected by the new technology only if this technology is adopted on a large scale (i.e., by the old economy). Denoting the new economy’s productivity by ρNt , the processes of BtN and ρNt for t > t∗ are given by

dBtN = ρNt BtNdt (6) dρNt = φ ρ + ψ − ρNt dt + σN,0dZ0,t + σN,1dZ1,t, (7)

[Figure 9]

where Z1,t is a Brownian motion uncorrelated with Z0,t. The agent learns about ψ by observing ρNt and ρt. The learning process is characterized by Lemma A1 in the Appendix. The posterior distribution of ψ conditional on Ft = ρNτ ,ρτ : t∗ ≤ τ ≤ t is normal,

ψ | Ft ∼ N ψt, σt2 ,

where the posterior mean ψt is a martingale (see equation (17)) and the posterior variance σt2 declines deterministically over time due to learning (see equation (18)). If the new technology

is adopted at time t∗∗, the agent continues to learn about ψ by observing ρNt and ρt, but the old economy’s productivity follows equation (4) rather than equation (3).

We deﬁne a technological revolution as the period [t∗,t∗∗] concluded by a large-scale adoption of the new technology. We treat the invention of the new technology as given, and study the conditions under which the invention leads to a technological revolution.

## 2.1. Optimal Adoption of the New Technology

The agent can adopt the new technology anytime between times t∗ and T (or never). We solve for the optimal adoption time t∗∗ numerically in Section 4.2. Until then, we focus on a simpler problem in which t∗∗ denotes an exogenously given time at which the agent decides whether or not to adopt the new technology. This simpler problem admits a closed-form solution for stock prices, which improves our understanding of the stock price dynamics. Our numerical results in Section 4.2. show that the dynamics obtained when t∗∗ is endogenously chosen are very similar to those obtained here with an exogenous t∗∗.

The sequence of events in the model is summarized in Figure 1. We assume that if a new technology is not adopted at time t∗∗, it continues to operate on a small scale until time T. Our history is full of examples of technologies that have not been adopted on a large scale but still survive on a small scale (e.g., direct-current electric motors, airships, etc.)

- Proposition 1: It is never optimal to adopt the new technology immediately at time t∗.

Adopting the new technology is risky – it may increase or decrease average productivity, depending on the sign of ψ. The prior for ψ in equation (5) is centered at zero, making the increases and decreases in productivity equally likely as of time t∗.3 Since the agent is risk averse, immediate adoption of the new technology is suboptimal. This intuition is formalized in the Appendix, which shows that the adoption of the new technology at time t∗ yields lower expected utility than no adoption. Proposition 1 holds for any κ, including κ = 0, as it is driven by the increase in risk resulting from the adoption of the new technology.

- Proposition 2: The new technology is adopted at time t∗∗ if and only if

log (1 − κ) A2 (τ∗∗)

ψt∗∗ ≥ ψ = −

+

[Figure 10]

[Figure 11]

- 1

[Figure 12]

- 2

(γ − 1) A2 (τ∗∗) σt2∗∗ , (8)

[Figure 13]

3If the prior is centered at ψt∗ = 0, Proposition 1 is modiﬁed so that it is not optimal to adopt the new technology at time t∗ unless ψt∗ is suﬃciently high. See Proposition 2 for an analogous relation.

where τ∗∗ = T − t∗∗ and A2 (τ) = τ − (1 − exp(−φτ))/φ > 0.

The new technology is adopted at time t∗∗ if the expected productivity gain, ψt∗∗, is positive and suﬃciently large. The threshold ψ is always positive, and it increases in the conversion cost κ, uncertainty σt∗∗, and risk aversion γ, which is intuitive. Note that the agent makes the adoption decision without knowing the true value of ψ. Regardless of the outcome of the adoption decision, learning about ψ continues after time t∗∗.

[Figure 14]

- Proposition 3: It is optimal to begin experimenting with the new technology at time t∗.

This proposition, proved in the Appendix, shows that the agent chooses to set up the new economy to begin learning about the new technology immediately after this technology becomes available at time t∗. The intuition is simple. Experimenting allows the agent to learn about the productivity gain ψ. If this learning leads the agent to believe at time t∗∗ that ψ is suﬃciently high, then it becomes optimal to adopt the new technology (Proposition

- 2). Otherwise, the status quo will prevail. Since experimenting is costless and there is no downside to it, it gives the agent a valuable option for free.4

Since option value generally increases with uncertainty, high uncertainty σt∗ makes a new technology desirable for experimentation. If it were costly to experiment with new technologies, or if the agent had to choose from a subset of technologies at time t∗, then the technologies with the highest σt∗ would be selected for experimentation, ceteris paribus. Uncertainty about productivity gains is thus a natural feature of innovative technologies.

- 3. Stock Prices

The stocks of the old and new economies pay liquidating dividends BT and BTN, respectively, at time T. There is also a riskless bond in zero net supply, whose yield we normalize to zero, for simplicity. Since the two shocks in the model are spanned by the two stocks, markets are complete. Standard arguments then imply that the state price density is uniquely given by

1 λ

Et WT−γ , (9) where λ is the Lagrange multiplier from the utility maximization problem of the representative agent. The market values (shadow prices) of the old and new economy stocks, denoted

πt =

[Figure 15]

[Figure 16]

4The problem we solve resembles the problem of making an irreversible marriage decision. It is generally suboptimal to marry a new acquaintance immediately because of substantial uncertainty regarding the quality of the personality match (cf. Proposition 1). Instead, it seems advisable to ﬁrst develop the relationship on a small scale, by dating without any commitment (cf. Proposition 3), and then to marry if we learn that the relationship is likely to work in the long run (cf. Proposition 2).

by Mt and MtN, respectively, are given by the standard pricing formulas

Mt = Et

πTBT πt

[Figure 17]

and MtN = Et

πTBTN πt

[Figure 18]

. (10)

To normalize the market values, we form “market-to-book” (M/B) ratios Mt/Bt and MtN/BtN. It seems reasonable to interpret capital as the book value of equity, and this interpretation

is exact for Bt and BtN in equations (2) and (6) if we also interpret output and productivity

- as earnings and proﬁtability, respectively (P´astor and Veronesi, 2003).

Let pt denote the probability at time t, t∗ ≤ t < t∗∗, that the new technology will be adopted at time t∗∗. Lemma A3 in the Appendix shows that pt = 1 − N ψ; ψt, σt2 − σt2∗∗ , where N (·;a,s2) denotes the c.d.f. of the normal distribution with mean a and variance s2.

[Figure 19]

- Proposition 4: For any t ∈ [t∗,t∗∗), the state price density is given by

πt = λ−1Bt−γ (1 − pt) Gnot + pt Gyest , (11)

where Gnot and Gyest are expectations of the marginal utility of wealth conditional on whether or not the new technology is adopted at time t∗∗. Both values are given in the Appendix.

- Corollary 1. For any t ∈ [t∗,t∗∗), the dynamics of πt are given by

dπt πt

[Figure 20]

= −γA1(τ)σd Z0,t − Sπ,t σt2

φ σN,1

[Figure 21]

d Z1,t, (12)

where τ = T − t, A1(τ) = (1 − e−φτ)/φ, Sπ,t is given in the Appendix, and so are the orthogonalized Brownian motions ( Z0,t, Z1,t), which capture the agent’s expectation errors.

This corollary illustrates the time-varying nature of risk during technological revolutions. When a new technology arrives at time t∗, the adoption probability pt∗ is generally small, which makes Sπ,t∗ small as well (pt = 0 implies Sπ,t = 0). The volatility of the stochastic discount factor in equation (12) then depends only slightly on σt2, making uncertainty about ψ mostly idiosyncratic. During a technological revolution, the adoption probability increases, which makes Sπ,t larger.5 As a result, the volatility of the stochastic discount factor becomes more closely tied to σt2, making uncertainty about ψ increasingly systematic.

- Proposition 5: For any t ∈ [t∗,t∗∗), the market-to-book ratios are given by

Mt Bt

[Figure 22]

=

(1 − pt)Gnot + ptGyest (1 − pt) Gnot + pt Gyest

[Figure 23]

and

MtN BtN

=

[Figure 24]

(1 − pt)Ktno + ptKtyes (1 − pt) Gnot + pt Gyest

, (13)

[Figure 25]

[Figure 26]

5In a technological revolution, pt rises from pt∗ ≈ 0 to pt∗∗ = 1, and Sπ,t rises from Sπ,t∗ ≈ 0 to Sπ,t∗∗ = γA2(τ∗∗) > 0. That is, as pt increases, Sπ,t increases from approximately zero to a positive number.

where Gnot , Gyest , Gnot , Gyest , Ktno, and Ktyes are given in the Appendix. In the special case pt = 0, the market-to-book ratio of the new economy simpliﬁes into

MtN BtN

0(τ)+A1(τ)ρNt +A2(τ)ψbt+12A2(τ)2σbt2, (14)

= eC

[Figure 27]

[Figure 28]

where A1(τ) is deﬁned in Corollary 1, A2(τ) in Proposition 2, and C0(τ) is in the Appendix. Note that MN/BN increases when uncertainty about ψ, σt2, increases. This relation, ﬁrst pointed out by P´astor and Veronesi (2003) in a simpler framework, is due to the idiosyncratic nature of uncertainty. When pt = 0, the state price density does not depend on uncertainty about ψ, but when pt > 0, it does. When pt is suﬃciently large, uncertainty is mostly systematic, and the associated risk reverses the positive relation between MN/BN and σt2.

The return processes for both stocks are given in Corollary A1 in the Appendix. Not surprisingly, the expected stock returns are given by the return covariances with dπt/πt, and the return volatilities of both stocks increase with uncertainty σt2.

## 3.1. The Dynamics of Prices during a Technological Revolution

In a technological revolution, the adoption probability pt rises from a small value at time t∗ to the value of one at time t∗∗. The eﬀect of pt on stock prices is analyzed next.

- Proposition 6: The new (old) economy’s M/B ratio is increasing in pt if and only if hnew > 0 (hold > 0), where hnew and hold are functions of ψt given in the Appendix.

For plausible parameter values, hnew > 0 when ψt is close to zero, but hnew < 0 when ψt approaches the threshold ψ. That is, the condition hnew > 0 holds shortly after time t∗, but it becomes violated as the adoption at time t∗∗ becomes more likely. Proposition 6 then implies that the new economy’s M/B is initially increasing but ultimately decreasing in pt during a technological revolution. The condition hold > 0 is never satisﬁed for the baseline parameter values, so the old economy’s M/B is always decreasing in pt.

[Figure 29]

While analyzing M/B as a function of pt seems informative, pt is driven primarily by ψt. Stock prices depend on ψt through two opposing eﬀects. On one hand, an increase in ψt is good news for prices because it increases expected cash ﬂows (Et [BT] and Et BTN ) in both economies. This cash ﬂow eﬀect is stronger for the new economy whose perceived productivity is immediately aﬀected; the old economy’s productivity is not aﬀected until time t∗∗, if at all. On the other hand, an increase in ψt is bad news for prices because the higher adoption probability makes the risk embedded in the new technology increasingly

systematic, thereby raising the discount rate. This discount rate eﬀect is also stronger for the new economy because πt covaries more with ρNt than with ρt (since both πt and ρNt correlate with revisions in ψt but ρt does not). Moreover, the discount rate eﬀect has a growing impact on the new economy’s M/B because the dependence of πt on revisions in ψt increases as pt increases. For the old economy, the discount rate eﬀect generally outweighs the cash ﬂow eﬀect from the very beginning, leading to a gradual decline in M/B during a revolution. For the new economy, the cash ﬂow eﬀect tends to dominate at ﬁrst, but the discount rate eﬀect dominates in the end, producing a “bubble”.

Although the dependence of MN/BN on ψt is complicated, its key features can be established locally at times t∗ and t∗∗. We show below that MN/BN is increasing (decreasing) in ψ around time t∗ (t∗∗), under certain assumptions.

(MtN/BtN) ∂ψbt > 0.

- Proposition 7: For any t ≥ t∗ there exists p¯ > 0 such that if pt < p¯ then ∂

[Figure 30]

In words, if the probability of adoption pt is suﬃciently small, then MN/BN is increasing in ψt. When pt is close to zero, so is its sensitivity to changes in ψt; thus an increase in ψt does not produce a large discount rate eﬀect.6 The cash ﬂow eﬀect is large, though, because MN/BN in equation (14) is strongly increasing in ψt. Proposition 7 follows.

When a new technology arrives at time t∗, its probability of eventual adoption is typically small because only a small fraction of new technologies are adopted by the whole economy. Proposition 7 then implies that, for most new technologies, the cash ﬂow eﬀect initially prevails over the discount rate eﬀect and MN/BN is increasing in ψt shortly after time t∗.

We also have some local results at time t∗∗. Below, we compare the M/B ratio of the new economy under two scenarios: ψt∗∗ = ψ ± ε, where ε > 0 is small. Corollary 2:

[Figure 31]

- (a) If ψt∗∗ = ψ + ε, then the new technology is adopted at time t∗∗, and MtN∗∗

[Figure 32]

[Figure 33]

BtN∗∗

= eC

[Figure 34]

0(τ∗∗)+A1(τ∗∗)ρNt∗∗+A2(τ∗∗)ψbt∗∗+21A2(τ∗∗)2(1−2γ)σbt2∗∗. (15)

[Figure 35]

- (b) If ψt∗∗ = ψ − ε, then the new technology is not adopted at time t∗∗, and

[Figure 36]

MtN∗∗ BtN∗∗

0(τ∗∗)+A1(τ∗∗)ρNt∗∗+A2(τ∗∗)ψbt∗∗+21A2(τ∗∗)2σbt2∗∗. (16)

[Figure 37]

= eC

[Figure 38]

[Figure 39]

[Figure 40]

6Analogously, if a stock option is deep out of the money, a small increase in the stock price does not change the option value by much since its delta is small and the option remains deep out of the money.

The new economy’s M/B is clearly lower when the technological revolution takes place. The reason is the uncertainty term σt2, whose coeﬃcient is negative in part (a) and positive in part (b). In part (a), σt2 is systematic (it aﬀects πt), whereas in part (b), it is idiosyncratic (it does not aﬀect πt). Since ψt (expected cash ﬂow) is essentially the same in both scenarios, the diﬀerence between M/B in parts (a) and (b) is due to the discount rate eﬀect. This knife-edge case shows that MN/BN is likely decreasing in ψt close to time t∗∗.

In summary, the cash ﬂow eﬀect usually dominates close to time t∗, leading to an initial positive relation between MN/BN and ψt, but the discount rate eﬀect usually dominates close to time t∗∗, leading to an eventual negative relation. During a technological revolution, ψt generally increases, leading to a bubble-like pattern in MN/BN.

## 3.2. Discussion

- Corollary 2 shows that the adoption reduces the new economy’s M/B, holding ψt constant. Intuitively, the adoption does not bring any beneﬁt to the new economy, which already uses the new technology. On the contrary, it increases systematic risk and thus reduces the new economy’s market value. The model features only one shareholder, the representative agent, who employs inﬁnitely more capital in the old economy than in the new economy. This agent wants the adoption to take place because the utility gain from making the old economy more productive outweighs the negligible loss of market value in the new economy.

Analogous to Corollary 2, we can show that the old economy’s market value also decreases

- at time t∗∗ if the adoption takes place when ψt∗∗ is close to ψ. Interestingly, the representative agent chooses to adopt the new technology even if doing so reduces the market value of her stocks. There is a diﬀerence between maximizing utility and maximizing market value. The adoption occurs only if it increases the agent’s expected utility. This adoption changes the economic environment by installing (what the agent perceives to be) a more productive technology and by increasing expected stock returns. In this new environment, stock prices are lower (due to higher discount rates) but expected utility is higher (due to higher expected wealth). Expected utility and stock prices need not move in the same direction because stock prices are related to the agent’s marginal utility rather than to the level of utility.

[Figure 41]

We solve the social planner’s problem in which a utility-maximizing representative agent owns all output by holding the stocks of the old and new economies. When a new technology is invented, it becomes property of the social planner. The social planner ﬁnds it optimal to set up a small-scale new economy to learn about the new technology before deciding whether

to adopt this technology in the large-scale old economy. Upon adoption, there is no transfer from the old economy to the new economy because the new economy does not own the new technology (the social planner does). As an example of a new economy ﬁrm, Amazon was an early user of the Internet but it did not own the Internet technology.

As an alternative to the social planner’s problem, we analyze a competitive economy in which ﬁrms independently decide whether to adopt the new technology while maximizing their own market values. We present this alternative decentralized model in the Appendix, and ﬁnd that it produces the same stock price dynamics as the social planner’s problem. The alternative model features “network externalities,” in that the average productivity of a technology increases as the fraction of ﬁrms using this technology increases. Each ﬁrm makes its own adoption decision independently, taking the decisions of all other ﬁrms as given. Adopting the same technology as other ﬁrms has two opposing eﬀects. On one hand, it hurts the ﬁrm, because the technology adopted by all other ﬁrms carries more systematic risk. On the other hand, it beneﬁts the ﬁrm through network externality gains. We show that it is possible to choose the magnitude of the network externality gains such that the solution is identical to that in the social planner’s problem. Speciﬁcally, the Nash equilibrium at time t∗∗ is such that all ﬁrms adopt the new technology if ψt∗∗ ≥ ψ, but none of them do if ψt∗∗ < ψ, analogous to our Proposition 2. As a result, all pricing formulas are the same as in the social planner’s problem, and the same “bubbles” in stock prices obtain.

[Figure 42]

[Figure 43]

The alternative model highlights the lack of coordination among ﬁrms in a competitive economy. Although each ﬁrm maximizes its own market value, the aggregate eﬀect of the ﬁrms’ adoptions is to reduce market values. The reason is that ﬁrms adopting the new technology do not fully internalize the resulting increases in the volatility of the stochastic discount factor. Each adopting ﬁrm imposes a negative externality on the market values of other ﬁrms by increasing systematic risk in the economy. We see that the stock price patterns obtained in our simple model with a utility-maximizing social planner hold also in a more complicated model featuring value-maximizing competitive ﬁrms.

Other ways of decentralizing the model could also lead to similar stock price dynamics. For example, suppose that ﬁrms facing diﬀerent conversion costs observe signals about ψ. As ψt rises during a technological revolution, the proportion of ﬁrms that adopt the new technology also rises. This proportion might play the same role as the adoption probability in our model: As the proportion rises from about zero to one, the volatility of the stochastic discount factor also rises, making the uncertainty about ψ increasingly systematic.

In our simple model, all output represents ﬁrm proﬁts, so productivity and proﬁtability

coincide. In reality, technological advances lead to permanent increases in productivity but only temporary increases in proﬁtability. In the long run, new technology tends to beneﬁt workers and consumers, not producers. Therefore, we also analyze a richer model in which labor income drives a wedge between productivity and proﬁtability.7 In this model, productivity gains from new technology last until time T, but proﬁtability gains last only until time t∗∗∗ < T, after which all productivity gains go to labor. Proﬁtability aﬀects the cash ﬂow to stocks, whereas productivity aﬀects the discount rates. Systematic risk depends on uncertainty about productivity because the agent’s total wealth depends on productivity. As a result, our basic mechanism is unaﬀected by the shorter proﬁtability horizon. Indeed, we ﬁnd that this richer model produces stock price dynamics very similar to those reported here. For the same parameter values, the bubble pattern is somewhat less pronounced, but more dramatic patterns can be easily obtained after plausible parameter changes.

# 4. Empirical Implications

The purpose of this section is to analyze the model-implied paths of the key variables during technological revolutions. We simulate 50,000 samples of shocks in our economy and compute the paths of quantities such as the M/B ratios and volatilities in each simulated sample. We split the 50,000 samples into two groups, depending on whether or not the new technology is adopted at time t∗∗, and plot the average paths of prices and volatilities across all samples within each group. Our objective is to understand how these paths diﬀer depending on whether or not the new technology leads to a technological revolution.

Table 1 shows the parameters used in our simulations. For the productivity processes, we choose parameter values close to those estimated by P´astor and Veronesi (2006) for the dynamics of proﬁtability. The relation between productivity and proﬁtability in our model is explained in Section 3.2. The parameter values for the conversion cost, time horizon, risk aversion, and prior beliefs about ψ are varied later in our sensitivity analysis.

Figure 2 plots the average paths of ψt, pt, and σπ ≡ Std(dπt/πt). Panel A shows that the average drift in ψt during technological revolutions is positive, due to conditioning on the ex post event that ψt∗∗ ≥ ψ (without such conditioning, ψt is a martingale; see equation (17)).8 Analogously, conditional on ψt∗∗ < ψ, ψt in Panel B (no revolution) drifts downward. The drift is less pronounced in Panel B than in Panel A because ψt∗ = 0 and ψ > 0. The

[Figure 44]

[Figure 45]

[Figure 46]

[Figure 47]

7This model is presented in the Technical Appendix, which is downloadable from the authors’ websites. 8Brown, Goetzmann and Ross (1995) provide a mathematical proof of a related statement in their analysis

of stock returns conditional on the stock’s survival through the end of the sample.

average probability of adoption, pt, drifts up in Panel C (revolution) and down in Panel D (no revolution), as expected. The volatility of the stochastic discount factor, σπ, is almost ﬂat while pt is low, but it increases as pt increases (Panel E).

Figure 3 plots the average paths of M/B and volatility for the new economy (solid line) and the old economy (dashed line). The panels on the left are based on the samples in which pt∗∗ = 1 (revolution); the panels on the right condition on pt∗∗ = 0 (no revolution).9 The dotted vertical lines mark the time when the new technology arrives, t∗ = 1, and the time at which the agent decides whether to adopt the technology, t∗∗ = 9.

Panel A of Figure 3 plots the average paths of M/B across all technological revolutions. The new economy’s M/B rises and then falls, as predicted in Section 3.1. Since we are conditioning on the adoption of the new technology at time t∗∗, ψt must go up between t∗ and t∗∗ (Figure 2). This increase in ψt has two countervailing eﬀects on prices. First, it increases expected future cash ﬂow from the new technology, pushing M/B up. Second, it increases the adoption probability, which makes the risks embedded in the new technology ever more systematic (aﬀecting WT), which then increases the discount rate applied to future cash ﬂow, pushing M/B down. For the old economy, the discount rate eﬀect outweighs the cash ﬂow eﬀect from the outset, leading to a slow decline in M/B. For the new economy, the cash ﬂow eﬀect is stronger at ﬁrst, but the discount rate eﬀect prevails in the end, producing a “bubble.” Since the path plotted in Panel A is an average across all revolutions, it shows that apparent bubbles in high-tech stock prices are not merely possible in a rational world; they should in fact be expected during technological revolutions.

Diﬀerent technological revolutions produce diﬀerent paths of M/B, depending on the path of realized productivity. These individual paths look mostly like bubbles that peak at diﬀerent times, and they are less smooth than the average path plotted in Panel A of Figure 3. On this average path, the peak-to-bottom drop in the new economy’s M/B lasts

- 5 years, but for some revolutions, the price drop is much more abrupt. For example, for 10% of all revolutions, the peak-to-bottom drop lasts less than 2.56 years, and for 5% of all revolutions, it lasts less than 1.68 years. The magnitude of the price drop also exhibits substantial dispersion across revolutions. On the average path, M/B falls by 2.9 from the peak to the bottom, but for 5% of all revolutions, it falls by more than 7.8.

Panel B of Figure 3 plots the average paths of M/B across all samples in which pt∗∗ = 0

[Figure 48]

9The fraction of the simulated samples in which pt∗∗ = 1 is approximately equal to the ex ante probability of adoption implied by our parameter choices, pt∗ ≈ 2%, as expected. In principle, any product innovation could potentially lead to a technological revolution, but very few do, both in reality and in our model.

(no revolution). In these samples, ψt declines slightly between t∗ and t∗∗, nudging the M/Bs down as well. The decline is larger in the new economy, for two reasons. One, the new economy’s M/B is more sensitive to ψt, as discussed earlier. Two, uncertainty about ψ gradually declines due to learning, which reduces M/B for the new economy but not for the old economy (see equation (14)). Thanks in part to this uncertainty, the level of M/B is higher in the new economy than in the old economy, in both Panels A and B. Higher productivity is another reason why the new economy’s M/B is higher in Panel A, even after time t∗∗. Although the adoption makes the long-run means of productivity equal in both economies, the productivity at time t∗∗ is higher in the new economy (ρNt∗∗ is likely to be high to make ψt∗∗ > ψ), lifting the M/B of the new economy above that of the old economy.

[Figure 49]

Panel C of Figure 3 plots the average paths of stock return volatility across all technological revolutions. Volatility is higher in the new economy than in the old economy, partly due to higher volatility of the fundamentals, but mostly due to uncertainty about ψ. To understand the U-shape in the new economy’s volatility, recall that shocks to ψt aﬀect stock prices via the discount rate and cash ﬂow eﬀects, which work in opposite directions. Around time t∗ (t∗∗), the cash ﬂow (discount rate) eﬀect dominates, so the two eﬀects do not oﬀset each other much and the volatility is high. The volatility is lowest when the two eﬀects cancel each other, which happens at some point between times t∗ and t∗∗; hence the U-shape. For the old economy, the discount rate eﬀect dominates from the outset, so the old economy’s volatility slowly increases as the rising adoption probability makes the stochastic discount factor more volatile. The spike in volatility at time t∗∗ is caused by those simulated paths for which ψt∗∗ is close to ψ because then pt swings a lot shortly before time t∗∗, making returns highly volatile (Corollary 2). We show later that the volatility spike disappears (but all other eﬀects remain) when t∗∗ is chosen optimally instead of being ﬁxed exogenously. Panel D plots the average return volatility across all no-revolution samples. In these samples, the discount rate eﬀect is weak and volatility is roughly constant over time.

[Figure 50]

Panels A and B of Figure 4 plot the market beta of the new economy, β, deﬁned as the slope from the regression of the new economy stock returns on the old economy stock returns. In Panel A, where we condition on pt∗∗ = 1 (revolution), β exhibits an asymmetric U-shape pattern, for the following reason. Positive shocks to ψt always reduce the market value of the old economy stocks, but they increase the value of the new economy stocks initially while the cash ﬂow eﬀect prevails over the discount rate eﬀect, leading to an initial decrease in β. Only after the discount rate eﬀect overcomes the cash ﬂow eﬀect, shocks to ψt begin aﬀecting the market values of both economies in the same direction, leading to an increase in β. Since the eﬀect of ψt on the old economy stocks increases with the adoption

probability, the rise in β is more dramatic than the initial fall. After a mild decline in the ﬁrst half of the revolution, β doubles in the second half, from 0.75 to 1.5. The average beta in the no-revolution samples, plotted in Panel B, is almost ﬂat over time.

As explained above, two aspects of systematic risk increase during technological revolutions: the old economy’s volatility and the new economy’s beta. The increase in the old economy’s volatility raises the discount rates for both economies, old and new, holding β constant. The increase in β gives an additional boost to the discount rate of the new economy, which is why stock prices fall by more in the new economy than in the old economy.

The remaining panels of Figure 4 plot the average realized returns (solid line) and expected returns (dashed line).10 In technological revolutions, realized stock returns are ﬁrst positive and then negative for both economies, due to an ex post selection bias. Ex post, we know that a technological revolution took place at time t∗∗, but ex ante, we only have a probability assessment of this event. Before time t∗∗, stock prices are not expected to rise and fall; expected returns are given simply by the covariances with the stochastic discount factor. However, conditioning on a technological revolution means that the adoption probability pt must be revised upward between times t∗ and t∗∗, causing a bubble-like pattern in prices through the cash ﬂow and discount rate eﬀects discussed earlier. The bias of realized returns relative to expected returns is due solely to ex post conditioning on pt∗∗ = 1; when this conditioning is removed, the bias disappears. (Across all 50,000 simulations, average realized returns are equal to average expected returns.) The rise and fall in stock prices during technological revolutions are observable ex post but not predictable ex ante.

The unexpected arrival of the new technology causes the old economy’s market value to drop immediately at time t∗ (Panel E of Figure 4). This drop is driven by two forces. The possibility of eventual adoption means that conversion costs might be paid at time t∗∗, and it also increases systematic risk and so drives up the discount rate.

## 4.1. Sensitivity Analysis

This section examines the sensitivity of the price dynamics to our parameter choices. Figure 5 is the counterpart of Panel A of Figure 3 (revolution), with various parameter changes.

In Panel A of Figure 5, risk aversion γ = 3, as opposed to γ = 4 in Figure 3. Lower risk aversion increases M/B in both economies, as expected, but the pattern of M/B is otherwise the same as that in Figure 3. A hump-shaped pattern in MN/BN obtains for any γ > 1.

[Figure 51]

10All returns are annualized by multiplying each interval-dt return by 1/dt.

In Panel B of Figure 5, the conversion cost is κ = 0, as opposed to κ = 0.1 in Figure 3. The main eﬀect of the lower κ is to decrease MN/BN. The lower conversion cost makes it more likely that the new technology will be adopted, which increases discount rates and thus depresses prices. For the old economy, there is also a counterbalancing eﬀect, as the lower conversion cost increases the old economy’s post-conversion capital Bt∗∗

(1 − κ). The two eﬀects approximately cancel out, so the old economy’s M/B is almost unaﬀected by the change in κ. Most important, the price patterns look just like those in Figure 3.

= Bt∗∗

−

+

- In Panel C, prior uncertainty about ψ is σt∗ = 8%, compared to σt∗ = 4% in Figure 3. The higher uncertainty increases MN/BN, especially close to time t∗ when pt is small (equation (14)). However, as pt increases during a revolution, uncertainty becomes increasingly systematic, pushing MN/BN down, and this discount rate eﬀect is stronger when systematic uncertainty is higher. Therefore, in technological revolutions characterized by high uncertainty, the new economy ﬁrms tend to start out with high valuations that exhibit a large decline. High uncertainty ampliﬁes the bubble-like pattern in stock prices.
- In Panel D of Figure 5, the time until the adoption decision is shortened to t∗∗ − t∗ = 6, compared to t∗∗ − t∗ = 8 in Figure 3. Faster adoption increases MN/BN. To understand this eﬀect, we note two facts. First, faster adoption implies higher uncertainty about ψ at time t∗∗ because there is less time to learn (equation (18)). Second, faster adoption implies a higher adoption threshold ψ because t∗∗ is lower and σt∗∗ is higher (equation (8)). Since ψt has less time to reach a higher threshold, the adoption probability pt∗ is lower, which implies that systematic risk is initially lower and MN/BN starts higher than in Figure 3. MN/BN then rises higher and falls deeper than in Figure 3, conditional on pt∗∗ = 1, because both the cash ﬂow eﬀect and the discount rate eﬀect are stronger when adoption is faster. The cash ﬂow eﬀect is stronger because in order for ψt to reach a higher threshold in shorter time, the increase in ψt must be sharper. The discount rate eﬀect is stronger because uncertainty at time t∗∗ is higher, and conditional on pt∗∗ = 1, this uncertainty is systematic. Since both eﬀects are stronger, the rise and fall in MN/BN are more striking than in Figure 3. Faster adoption of the new technology magniﬁes the bubble-like pattern in stock prices.

[Figure 52]

## 4.2. Optimal Adoption Time

In this section, we relax the assumption that t∗∗ is exogenously given. Without this assumption, no closed-form solutions are available, but we can solve the problem numerically. The agent is choosing the optimal time t∗∗, t∗ ≤ t∗∗ ≤ T to adopt the new technology (no adoption is a possibility). This is essentially a problem of solving for the best time to exercise an

American real option. The details of our solution are in the Appendix.

Figure 6 plots the average paths of M/B and volatility when t∗∗ is chosen optimally. Depending on the path of productivity, the adoption can occur anytime between t∗ and T, but averaging across very diﬀerent t∗∗’s would not be meaningful. For comparison with Figure

- 3 in which t∗∗ = 9 years, the left panels of Figure 6 report averages across those simulations in which the optimal t∗∗ is between years 8 and 10. Our main results are unaﬀected by endogenizing t∗∗. During revolutions, the new economy’s M/B exhibits a rise and fall similar to that in Figure 3, albeit slightly weaker (a stronger “bubble” pattern is obtained for γ = 3,

- as we show in an earlier draft). The path of volatility in Panel C is also similar, except that the volatility spike observed in Figure 3 disappears, as explained earlier.

5. Empirical Evidence

In this section, we empirically examine the behavior of stock prices during two technological revolutions, one recent and one distant. For both revolutions, we consider the key quantities in our model, such as the new economy’s market beta and the level and volatility of stock prices, and compare their empirical dynamics with their model-implied dynamics.

5.1. The Internet Revolution

The Internet’s predecessor, Arpanet, was created in 1969 with funding from the U.S. Department of Defense. Arpanet ceased to exist in 1990, roughly when the team of Tim Berners-Lee

- at CERN released the World Wide Web. The ﬁrst Web site, info.cern.ch, appeared in 1991. The ﬁrst graphics-based web browser, Mosaic, was launched in 1993 by Marc Andreessen at the National Center for Supercomputing Applications. In 1994, Andreessen co-founded Netscape Communications, which went public in August 1995 in the ﬁrst Internet IPO. The ﬁrst big pioneer of e-commerce was the online bookseller Amazon.com, which was launched by Jeﬀ Bezos in 1995 and went public in May 1997. The Internet gradually became mainstream. The number of web servers grew from about 23,000 in mid-1995 to about 30 million in mid-2001 and 65 million in mid-2005 (see www.zakon.org/robert/internet/timeline/). A prominent example of the Internet’s integration into traditional business models was the creation of the ﬁrst “clicks-and-mortar” company through the merger of AOL and Time Warner.11 Today, the Internet technology is an indelible part of the economic landscape.

[Figure 53]

11AOL announced its plan to acquire Time Warner (for some $182bn in stock) in January 2000, and the FTC approved the deal in January 2001. “The merger, the largest deal in history, combines the nation’s top internet service provider with the world’s top media conglomerate. The deal also validates the Internet’s

To provide a benchmark for our empirical analysis, we plot the model-implied dynamics of some key variables in Figure 7. These are the expected dynamics during a revolution, in that we average the model-implied paths across many simulations in which the new technology is adopted at time t∗∗. We keep all parameters from the baseline case (Table 1) except that we shorten the duration of the revolution from eight to six years because the Internet revolution was relatively fast. Panel A of Figure 7 shows that the new economy’s market beta decreases slightly (from 0.9 to 0.7) in the ﬁrst half of the revolution, but then it increases sharply in the second half, reaching 1.65 at time t∗∗ before falling to one. This increase in beta is even steeper than in the baseline case (Panel A of Figure 4). Panel B shows that the increase in stock return volatility is also steeper than in the baseline case (Panel C of Figure 3), with the old economy’s volatility doubling to 38% and the new economy’s volatility rising to over 65%. Panel C plots the market values of both economies. There is a clear “bubble” in the new economy, whose market value quintuples and then falls by half. The old economy’s market value also rises and falls, but this pattern is much weaker than in the new economy. Panel D shows that the old economy’s productivity begins rising immediately after the adoption of the new technology, when it begins mean-reverting toward a higher mean.

Figure 8 is an empirical counterpart of Figure 7 for the period 1992–2005. For simplicity, we assume that the technology-loaded NASDAQ index represents the new economy and the NYSE/AMEX index is the old economy. We obtain daily index returns from CRSP.

- Panel A of Figure 8 plots the market beta of the NASDAQ index, along with its two-

standard-error conﬁdence bands. The beta is computed daily as the slope coeﬃcient from the regression of the NASDAQ returns on the NYSE/AMEX returns over the most recent 500 trading days (i.e., about two years). After a slight decrease from about 1.2, NASDAQ’s beta doubles from 1.0 to 2.0 between 1997 and mid-2002, and this increase is highly statistically signiﬁcant. This empirical pattern is strikingly similar to the model-implied pattern in Panel A of Figure 7, in which the beta also decreases by about 0.2 before rising 2.3-fold by the end of the revolution. According to the model, the time when the beta peaks is the time of the large-scale adoption; hence the evidence on NASDAQ’s beta is consistent with the probability of the Internet’s large-scale adoption reaching one by mid-2002.

- Panel B of Figure 8 plots the standard deviations of returns on the NASDAQ and

NYSE/AMEX indices, computed daily over the most recent 500 trading days. NASDAQ’s volatility falls from 17% in 1992 to 11% in 1995, before rising to 47% at the beginning of

[Figure 54]

role as a leader in the new world economy, while redeﬁning what the next generation of digital-based leaders will look like.” (CNN Money, Jan 10, 2000).

2002. NYSE/AMEX’s volatility falls from 13% in 1992 to 8% in 1995, before rising to 21% by the end of 2002. These patterns are similar to the model-implied patterns in Panel B of Figure 7 in several ways: (i) the new economy’s volatility always exceeds the old economy’s volatility; (ii) both volatilities generally rise over time, with a bit of a U-shape pattern; (iii) the new economy’s volatility rises much faster; and (iv) both volatilities peak at about the same time. In the model, both volatilities peak at the time of the adoption; the volatility evidence is thus consistent with the Internet revolution ending sometime in 2002.

- Panel C of Figure 8 plots the index levels for NASDAQ and NYSE/AMEX, namely, the value of $1 invested in these indices in January 1992, with dividend reinvestment. The NASDAQ index quadruples between 1996 and March 2000, but then it falls back to the 1996 level by October 2002, after which it rises again. In contrast, NYSE/AMEX exhibits a much smaller rise and fall over the same period. This pattern is similar to the model-implied pattern in Panel C of Figure 7, in which the new economy’s market value also exhibits a “bubble” but the old economy’s rise and fall are much less pronounced.12 According to the model, the time when both indices stop falling is the time of the large-scale adoption; hence this evidence is consistent with the Internet’s adoption by October 2002.
- Panel D of Figure 8 plots a three-year moving average of multifactor productivity growth in the private business sector of the U.S. economy. (This is the most commonly used multifactor productivity measure, according to the Bureau of Labor Statistics, which is the source of the data.) In year t, we plot the average annual productivity growth in years t − 2, t − 1, and t. Multifactor productivity growth averaged about 1% per year in the 1990s, but it increased sharply after year 2002: from 1% per year in 2002 to 1.5% in 2003 and 2.5% in 2004 and 2005. A similar pattern is observed for labor productivity.13 The observed productivity pattern is similar to the model-implied pattern in Panel D of Figure 7, except that

[Figure 55]

- 12P´stor and Veronesi (2006) show that NASDAQ’s M/B dropped by 5.3 (from 8.5 to 3.2) from the peak to the bottom in 2.7 years. Both the duration and the magnitude of this drop in M/B correspond closely to their counterparts in our model. The corresponding model-implied average pattern in M/B is plotted in Panel D of Figure 5 (in which the revolution lasts 6 years, as it does in Figure 7). This average M/B falls by 4.5 from the peak to the bottom, also in 2.7 years, matching the observed values remarkably closely.
- 13In his Remarks Before Leadership South Carolina on August 31, 2006, Ben Bernanke argued that “One of the most important economic developments in the United States in the past decade or so has been a sustained increase in the growth rate of labor productivity... From the early 1970s until about 1995, productivity growth in the U.S. nonfarm business sector averaged about 1.5% per year... Between 1995 and 2000, however, the rate of productivity growth picked up signiﬁcantly, to about 2.5% per year... Talk of the “new economy” faded with the sharp declines in the stock valuations of high-tech ﬁrms at the turn of the millennium. Yet, remarkably, productivity accelerated further in the early part of this decade. From the end of 2000 to the end of 2003, productivity rose at a 3.5% annual rate and it is estimated to have increased at an average annual rate of 2.25% since the end of 2003. These advances were achieved despite adverse developments that included the 2001 recession, the terrorist attacks of September 11, [etc.].”

that ﬁgure plots the level of productivity as opposed to its growth rate.14 In the model, the economy’s productivity begins rising at the time of the adoption; hence the productivity evidence is consistent with a large-scale adoption of the Internet by 2002.

Overall, we ﬁnd Figure 8 remarkably similar to Figure 7. The patterns of NASDAQ’s beta and NYSE/AMEX’s volatility show that both sectors experienced large increases in systematic risk in 1997–2002, supporting the key prediction of the model. To summarize, the empirical evidence seems consistent with the joint hypothesis that our model holds and that the Internet technology was adopted on a large scale by 2002.

## 5.2. American Railroads Before the Civil War

Our paper is motivated by the technological revolutions, listed in the introduction, that were accompanied by apparent bubbles in stock prices. In this section, we conduct an “out-ofsample” analysis of a revolution whose stock prices do not seem to have been analyzed before. We analyze the ﬁrst major technological revolution that took place in the U.S. since the New York Stock Exchange was organized in 1792 – the introduction of steam-powered railroads (RRs). In the early days of the RR, there was substantial uncertainty about whether the RR technology would be ultimately adopted on a large scale. After examining the historical milestones of American RRs in Section 5.2.1., we argue that the probability of a large-scale adoption rose gradually, and that it approached one in the late 1850s after the RR expansion west of the Mississippi River. We then empirically examine the behavior of the RR stock prices in 1830–1861 in Section 5.2.2. In the context of our model, our evidence is consistent with a large-scale adoption of the RR technology around year 1857.

- 5.2.1. Brief History

The steam engine, an 18th-century invention, was ﬁrst used for rail-based transportation in the early 19th century in Britain. The United States followed shortly afterwards. The ﬁrst RR act in the U.S. was passed in 1815 when the New Jersey legislature awarded a charter to Colonel John Stevens to build a RR between the Delaware and Raritan rivers.15 In 1825, Stevens operated the ﬁrst locomotive in America – his 16-foot “Steam Waggon” ran around a circular rail track in Hoboken at 12 miles per hour. The construction of the ﬁrst RR, the Baltimore & Ohio, began in July 1828. The Baltimore & Ohio initially used

[Figure 56]

14Our comparison seems reasonable because in the model, average productivity can grow only via technological revolutions, whereas in reality, there are also many non-revolutionary improvements in productivity. Therefore, in the data, it is the growth rate of productivity that sets a technological revolution apart. 15The discussion in this section draws especially on Stover (1961), Fogel (1964), and Klein (1994).

horses to draw its cars, but it replaced them in 1830 by a steam locomotive, Peter Cooper’s “Tom Thumb.” In 1830, both passenger and freight service commenced on the Baltimore & Ohio. RRs spread quickly. On Christmas Day in 1830, the “Best Friend of Charleston,” the ﬁrst locomotive built for sale in the U.S., made the ﬁrst scheduled steam-RR train run in America. Between 1830 and 1840, the RR mileage in the U.S. grew from 23 to 2,808 miles. In 1840, only four of the 26 states had not completed their ﬁrst mile of track.

The new RR technology competed with the existing modes of transportation such as wagons, stagecoaches, steamboats, and canals. Those were not without problems – wagons were slow and expensive, stagecoaches were uncomfortable, steamboats were dangerous and limited in scope, and canals froze over in winter. However, it was far from obvious in the 1830s and 1840s that the RRs would later come to dominate the transportation industry. For example, waterways were much less expensive than RRs, and wagons were not restricted to rails. While the RR mileage caught up with the canal mileage in the early 1840s, waterways still carried the great bulk of the nation’s freight in the late 1840s. Writes Fogel (1964): “Far from being viewed as essential to economic development, the ﬁrst RRs were widely regarded as having only limited commercial application. Extreme skeptics argued that RRs were too crude to insure regular service, that the sparks thrown oﬀ by belching engines would set ﬁre to buildings and ﬁelds, and that speeds of 20 to 30 miles per hour could be “fatal to wagons, road and loading, as well as to human life.” More sober critics questioned the ability of RRs to provide low cost transportation, especially for heavy freight. [Some] placed “a RR between a good turnpike and a canal” in transportation eﬃciency.”

Nearly all RRs organized as corporations funded by private investors. More than half of the more than $300 million invested in American RRs in 1850 was represented by capital stock, the remainder being in bonds. The freight business was economically more important than passenger traﬃc, which typically produced around 30% of the total revenue.

While most early RRs were built with local capital to provide local transportation, RR building became more ambitious in the 1850s. This decade “was one of the most dynamic periods in the history of American RRs” (Stover, 1961). RR mileage expanded from 9,021 in 1850 to 30,626 in 1860, and total investment in the industry increased from about $300m to about $1,150m over the same period. This growth was spurred by land grants to RRs by the federal government. The ﬁrst land-granting act was passed by the Congress in 1850, aiding the Illinois Central and the Mobile & Ohio RRs. The RR growth in the 1850s was also stimulated by the discovery of gold in California and the lure of the trans-Paciﬁc trade. In the 1850s, New York, Philadelphia, and Baltimore all achieved their rail connections with

the west. In 1853, an all-rail route opened from the East to Chicago, and Chicago quickly became the rail capital of the nation. The RR technology also advanced in the 1850s – telegraph was ﬁrst used to dispatch trains, T-rails became the general rule, and so did the standard track gauge, at least in the North.16 “Instead of merely serving as connectors between navigable bodies of water as originally conceived, RRs were replacing them as the preferred way of transport” (Klein, 1994).

The dramatic RR growth in the 1850s is also evident in Figure 9, which plots the total rail consumption in the U.S., measured by the number of track-miles of rails laid each year (Fogel, 1964). Rail consumption grew fast in the 1830s, but especially fast during the decade leading up to 1856. After 1856, rail consumption slowed down and even declined in 1861 when the Civil War began, but it accelerated again after the war.

The diﬀusion of the RR technology made a leap in 1856 when two milestone RRs were completed: the Illinois Central, the longest RR in the world (705 miles), and the Sacramento Valley, the ﬁrst RR in California. Also in 1856, the ﬁrst RR bridge across the Mississippi was built near Davenport, Iowa, heralding future westward expansion into the region then known as the “Great American Desert.” This westward expansion was the deﬁning feature of the RR growth in the decades to come. The RRs shaped the economy of the West, creating new national markets and fostering unprecedented economic specialization across the nation.

By the late 1850s, it seemed clear that the RR had become a dominant form of transportation. According to Stover (1961), “By 1860 the canal packets and river steamers had lost much of their passenger traﬃc” to the RR. In 1860, every state save Minnesota and Oregon had RR mileage, and 29 of the 33 states had more than 100 miles of line. Klein (1994) argues that “By 1860... [the RR] had emerged not only as the preferred form of transportation but also as the chief weapon of commercial rivalry.” This evidence suggests that a large-scale adoption of the RR technology took place by the end of the 1850s.

- 5.2.2. Railroad Stock Prices

To examine the behavior of RR stock prices in the early days of the RR (1830–1861), we use the data compiled by Goetzmann, Ibbotson, and Peng (2001). These data contain monthly individual stock prices for NYSE stocks from 1815 to 1925, as well as annual dividends for a

[Figure 57]

16The Northern RRs were using 11 diﬀerent track gauges in the 1850s, but the standard gauge, 4’8.5”, became by far the most common by 1860, according to Stover (1961). The South was still mostly on the 5’ gauge. Benmelech (2007) exploits the diversity of track gauges in 19th century American railroads to examine the eﬀect of asset liquidation value on capital structure.

subset of stocks from 1825 to 1870. The data are provided at http://icf.som.yale.edu/nyse/.

To focus on common stocks, we exclude stocks classiﬁed as “preferred” or “scrip” in the database. (Scrips are certiﬁcates convertible into shares when fully paid-in.) If such classiﬁcation is not provided, we examine the stock name and exclude stocks whose name contains an indication of non-common status such as “pref,” “pr.,” “pf,” or “scrip.” Among the 671 stocks in the database, we identify and exclude 85 preferred stocks and 29 scrips.

We identify 284 RR stocks (42.32% of the whole sample) by examining the stock names. The ﬁrst RRs that appear in our price index (discussed below) in 1831 are Camden & Amboy, Canajoharie & Catskill, Harlem, and Ithaca & Oswego. All RRs that have at least one valid monthly common stock return between 1830 and 1861 are listed in Table 2.

We clean the monthly price ﬁle to remove apparent data errors. To proceed in a systematic fashion, we exclude all prices that imply implausibly large return reversals. Speciﬁcally, we exclude prices that more than tripled compared to the most recent available price and then fell to less than a third at the nearest future observation, as well as prices that experienced the same reversals in reverse order (ﬁrst down, then up). We eliminate 34 such prices in our 1830–1861 sample. We also examine all price sequences in which the price increased or decreased at least tenfold without reversal, and eliminate six suspicious price entries between 1830 and 1861. We retain the price entries that imply returns below -90% at the very end of a stock’s price series because these could be stocks heading for bankruptcy. Altogether, we delete 40 of the 15,276 price entries between 1830 and 1861, or 0.26% of the sample.

Before the price coverage in the database improves in 1848, uninterrupted price sequences for RR stocks are rare. In no month before 1848 are there more than ﬁve RR stocks with valid monthly returns, and there are months with zero RR returns. An important part of the problem are gaps in the price series, in which one or several missing values are sandwiched between two valid prices for a given stock. To alleviate the data shortage, we ﬁll in such gaps by linear interpolation, but only for gaps that are no more than three months long. This procedure substantially increases the price coverage early in the sample. For example, without interpolating, the RR year-end price-dividend ratio discussed below would have only three valid observations prior to 1847; with interpolation, the number of valid observations increases to eight. Without interpolating, our results would be noisier, with more missing values, but they would lead to the same basic conclusions.

We compute monthly RR (non-RR) index returns as price-weighted averages of monthly

capital gains across all RR (non-RR) stocks.17 We use capital gains rather than total returns because the dividend data available to us are annual, not monthly, and because these data are spotty, especially early in the sample (Goetzmann et al. (2001) suggest that their dividend sample is incomplete). The resulting return series can be viewed as approximations to the actual returns earned by investors.

Panel A of Figure 10 plots the beta of the RR index, with a two-standard-error conﬁdence band. The beta in month t is the slope coeﬃcient from the regression of the most recent 36 monthly RR returns (in months t−35 through t) on the non-RR returns. Not surprisingly, the beta estimates computed from only 36 observations have wide conﬁdence bands. Nonetheless, it appears that the largest increase in beta took place in the 1850s: The beta estimate rose from about 0.2 in 1850 to about 1.8 in 1856, before falling to about 1.0 right after 1857. This empirical pattern is quite similar to the model-implied pattern in Panel A of Figure 4 if we assume that the RR technology was adopted on a large scale in 1857.

- Panel B plots the volatility of returns in the RR and non-RR industries, computed

annually as the standard deviation of monthly industry returns within the year. Two facts seem noteworthy. First, the RR volatility exceeds the non-RR volatility in every year except 1841, consistent with the presence of uncertainty about the RR technology. The volatility diﬀerence is also due in part to the fact that the RR portfolio is less diversiﬁed than the nonRR portfolio, but it persists also after the number of RRs with valid monthly stock returns increases sharply (from 6 in December 1847 to 15 in January 1848, to 25 in July 1850). The second interesting fact in Panel B is that return volatility increases sharply in 1857, to 33.5% per year for RRs and to 23.1% for non-RRs. Comparison with Panel C of Figure 3 shows that both facts are consistent with a large-scale adoption of the RR technology in 1857.

- Panel C plots the stock price index levels for the RR and non-RR industries, obtained

by cumulating monthly returns in each industry. The general downward trend in the price indexes is partly due to the absence of dividends and partly due to the absence of inﬂation in the economy. The biggest price declines occur in the mid-1850s. For example, between June 1853 and October 1857, the RR price index falls by 58.3%, whereas the non-RR index falls by 33.9%. Both the sharp price decline for RRs and the milder decline for non-RRs are consistent with the RR technology being adopted on a large scale around 1857. Recall that our model predicts that the new economy (RR) stock prices fall by more than the old economy (non-RR) stock prices shortly before the adoption of the new technology.

[Figure 58]

17Goetzmann et al. (2001) argue that price-weighting best approximates the return on a buy-and-hold portfolio, given the absence of information about market capitalization and book value in their database.

Various events played a role in the stock price decline in 1857. Investor conﬁdence was shaken by embezzlement at the Ohio Life Insurance and Trust Company in August, as well as by the government’s loss of a large amount of gold at sea in September. Other commonly cited negative inﬂuences include falling grain prices, British withdrawals of capital from U.S. banks, and manufacturing surpluses. The stock market bottomed in October 1857 amidst a number of bank failures. However, the stock price decline cannot be fully attributed to the banking panic. According to Mishkin (1991), “Rather than starting with the banking panic in October 1857, the disturbance to the ﬁnancial markets seems to arise several months earlier with the rise in interest rates, the stock market decline... and the widening of the interest rate spread.” Mishkin’s last observation is particularly interesting. He shows that the spread between the yields of low- and high-quality corporate bonds was unusually high in 1857–1859, higher than at any future time before the 1930s. These high yield spreads indicate that the risk premia in the late 1850s were high, consistent with our story. Mishkin also opines that the decline in stock prices in the late 1850s “might be linked to the general rise in interest rates which lowers the present discounted value of future income streams.” This is precisely our story - stock prices fall shortly before the adoption of the new technology because discount rates increase due to an increase in systematic risk.

In Panel D of Figure 10, we do not plot productivity as we did in Figure 8 because, to our knowledge, productivity in this period has been computed only at a ten-year frequency from census data. We note, however, that the evidence points to a large increase in productivity after the late 1850s. For example, Cochrane (1979) argues that productivity advanced sharply just before the Civil War, and Craig and Weiss (1993) conclude that “the 1860s saw the greatest increase in output per farm worker of any decade in the 19th century.” This evidence on productivity further strengthens the case for a large-scale adoption of the RR technology in the late 1850s in the context of our model (cf. Panel D of Figure 7).

Panel D plots the aggregate price-to-dividend ratio (P/D) for the RR and non-RR industries. Each year, we compute P/D as the sum of year-end prices divided by the sum of dividends paid in that year, summing across all RR (or non-RR) stocks with valid price and dividend data. Note three main results. First, the P/D of RRs almost invariably exceeds the P/D of non-RRs before the mid-1850s. Second, the RR P/D falls from 24.9 in 1846 to 15.8 in 1852, to 6.5 in 1857. Third, the non-RR P/D falls as well, but less dramatically: from 14.0 to 12.8 to 9.1 over the same period. While interpreting the noisy data requires caution, all three results in Panel D are consistent with the joint hypothesis that our model is true and that the new RR technology was widely adopted around 1857.

## 5.3. Other Evidence

Three recent papers explicitly test some predictions of our model. Bharath and Viswanathan (2006) empirically analyze the model’s risk implications at the ﬁrm level. They examine 252 brick-and-mortar ﬁrms that launched commercial websites (i.e., adopted the Internet technology as a way of doing business) in 1995–2004. The authors ﬁnd that adopting the new technology is associated with an increase in ﬁrm risk, with diﬀerences between the early and late adopters: Firms that adopted the Internet before March 2000 (while stock prices were rising) experienced signiﬁcant increases in idiosyncratic risk, whereas ﬁrms that adopted after March 2000 had signiﬁcant increases in systematic risk. The authors conclude that their evidence provides strong support for our model.

Mazzucato and Tancioni (2006) analyze stock prices and patent-related measures of innovation in a sample of ﬁrms in the pharmaceutical and biotechnology industries between 1975 and 1999. They ﬁnd that the ﬁrms’ price-earnings ratios are positively related to innovation as well as to idiosyncratic risk, and argue that this evidence supports our model.

Hoberg and Phillips (2006) empirically examine the real and ﬁnancial outcomes following industry booms in 1972–2004. They test the risk predictions of our model at the industry level. They ﬁnd that market betas increase and idiosyncratic risk declines after booms, consistent with our model. The authors ﬁnd strong support for our model in competitive industries but not in concentrated industries. It would be useful to extend our simple model to analyze the eﬀect of product market competition theoretically.

In earlier work, Mazzucato (2002) studies the early phases of the life-cycles of the automobile and PC industries in the U.S. She ﬁnds that in both industries, stock prices were the most volatile when technological change was the most radical. She also ﬁnds idiosyncratic risk to be higher in the early stage of industry evolution, consistent with our model.

# 6. Conclusions

We develop a general equilibrium model that produces stock price “bubbles” during technological revolutions. The model features Bayesian learning about the average productivity of the new technology. Stock prices of innovative ﬁrms initially rise due to good news about this productivity, but they ultimately fall as the risk of the technology changes from idiosyncratic to systematic. The rise and fall in stock prices are observable only in hindsight – this pattern is unexpected by investors in real time but we observe it ex post when we focus on

technologies that eventually led to technological revolutions. The “bubbles” should be most pronounced in revolutions characterized by high uncertainty and fast adoption.

The model makes many empirical predictions. We ﬁnd support for these predictions in the evidence from 1830–1861 and 1992–2005 when the railroad and Internet technologies spread in the United States. In the context of our model, the empirical evidence is consistent with large-scale adoptions of railroads by the late 1850s and the Internet by 2002.

We focus on stock prices but our model also has implications for productivity. The new technology does not bring productivity gains immediately upon arrival because the agent ﬁnds it optimal to learn about a new technology before adopting it. Since the agent chooses the adoption time optimally depending on what she learns, the time it takes for the productivity gains to begin emerging is endogenous in the model. The implication that productivity gains arrive with a lag seems reasonable; for example, although electric power ﬁrst appeared around 1880, it was not until the 1920s that the productivity of the U.S. economy increased as a result of a large-scale adoption of electricity (David, 1991).

Our model has no implications for investment because the agent invests only a negligible amount in the new technology for learning purposes. As a result, the model fails to predict the large amount of investment that often accompanies technological revolutions. For example, it seems clear ex post that the 1990s witnessed signiﬁcant overinvestment in the Internet infrastructure.18 Billions of dollars worth of optical ﬁbers laid in the 1990s remain unused to this day as the market appears to have overestimated the extent to which the Internet would revolutionize the delivery of bandwidth-intensive content. It is possible that market irrationality, which is absent from our model, contributes to the overinvestment and stock price “bubbles” observed during technological revolutions. Future research can test our model against alternatives that involve behavioral biases. Some predictions of our model, such as those involving market beta, are unlikely to follow from behavioral models, in which there is typically no role for systematic risk. Since we ﬁnd empirically that systematic risk increased sharply during two prominent revolutions, it seems unlikely that behavioral biases can fully explain the observed stock price patterns. Such biases could certainly be a part of the story, though, and quantifying their relative importance would be interesting.

[Figure 59]

18Johnson (2007) and DeMarzo, Kaniel, and Kremer (2007) develop models that can generate overinvestment in new technologies. These models have a diﬀerent focus and they rely on diﬀerent mechanisms – learning about the curvature of the production function and relative wealth concerns, respectively.

Table 1 Parameters used in Simulations.

[Figure 60]

ρ ψt∗ σt∗

[Figure 61]

0.1217 0 0.04 φ σ σN,0 σN,1

[Figure 62]

0.3551 0.07 0.07 0.07

[Figure 63]

κ t∗∗ − t∗ T γ 0.1 8 30 4

[Figure 64]

[Figure 65]

Table 2 Railroads Appearing in our Price Index.

This table lists all railroads in our sample that have at least one valid monthly common stock return between 1830 and 1861. The railroads are sorted by the year of appearance of their ﬁrst valid monthly return.

[Figure 66]

Year Railroad

[Figure 67]

- 1831 Camden & Amboy; Canajoharie & Catskill; Harlem; Ithaca & Oswego
- 1832 Boston & Providence
- 1833 Boston & Worcester; Brooklyn & Jamaica 1835 Hudson & Berkshire; Long Island 1839 Auburn & Syracuse 1841 Auburn & Rochester 1844 Housatonic

- 1847 Hudson River; Macon & West
- 1848 Hartford & New Haven; New York & Erie
- 1849 Erie
- 1850 Albany & Schenectady; Baltimore & Ohio; Michigan Central; New York & Harlem
- 1851 Chemung
- 1852 Michigan & Southern
- 1853 Cincinnati, Hamilton & Dayton; Cleveland, Columbus & Cincinnati; Cleveland & Pittsburg; Cleveland & Toledo; Galena & Chicago; Illinois Central; Little Miami
- 1854 Chicago & Rock Island
- 1855 Michigan Southern & Northern Indiana
- 1856 Eighth Avenue; Lacrosse & Milwaukee; Macon & Western
- 1857 Chicago, Burlington & Quincy; Delaware, Lackawanna & Western; Indianapolis & Cincinnati
- 1858 Brooklyn City; Buﬀalo & State Line; Cleveland, Painesville & Ashtabula

[Figure 68]

New technology adopted by old economy Mean productivity increases by ψ Technological revolution

New technology arrives New economy formed Learning begins

T

Agent decides whether to adopt the new technology

Agent consumes WT = BT

|0|
|---|

|t*| |t**|
|---|---|---|
| | | |

Old technology Old economy

Agent learns about ψ

T

No adoption Mean productivity unchanged No technological revolution

- Figure 1. The Sequence of Events. In this chart, t∗∗, the time when the agent decides whether to adopt the new technology, is taken as given. We initially take t∗∗ as given for the purpose of obtaining closed-form solutions for prices, but later we solve for the optimal time t∗∗ to adopt the new technology.

(A) Revolution:ψ t

6

4

(%)ψ t

2

0

0 2 4 6 8 10

(C) Revolution: pt

- 0.5
- 1

| | | |
|---|---|---|

pt

0

0 2 4 6 8 10

(E) Revolution:σπ

120

(%) σπ

100

80

0 2 4 6 8 10

Years

(B) No Revolution:ψ t

6

4

(%)ψ t

2

0

0 2 4 6 8 10

(D) No Revolution: pt

- 0.5
- 1

| | | |
|---|---|---|

pt

0

0 2 4 6 8 10

(F) No Revolution:σπ

| | | |
|---|---|---|
| | | |

120

(%) σπ

100

80

0 2 4 6 8 10

Years

- Figure 2. Average ψt, pt, σπ,t in Simulations. The left panels plot the perceived productivity gain ψt (Panel A), the adoption probability pt (Panel C), and the volatility of the stochastic discount factor σπ,t (Panel E), averaged across all simulations in which the new technology was adopted at time t∗∗ (pt∗∗ = 1). The right panels (B, D, and F) plot the same quantities but the average is taken across all simulations in

which the new technology was not adopted at time t∗∗ (pt∗∗ = 0). In each panel, the ﬁrst vertical line denotes t∗ = 1, the time when the new technology becomes available, and the second vertical line denotes t∗∗ = 9, the time at which the agent decides whether to adopt the technology on a large scale. All parameters are given in Table 1.

(A) Revolution: Market to Book Ratio

(B) No Revolution: Market to Book Ratio

- 0
- 1
- 2
- 3
- 4
- 5

- 0
- 1
- 2
- 3
- 4
- 5

| ||New<br><br>Old|
|---|
| |
|---|---|---|

| | | |
|---|---|---|

M/B

M/B

0 2 4 6 8 10

0 2 4 6 8 10

Years

Years

(C) Revolution: Stock Return Volatility

(D) No Revolution: Stock Return Volatility

60

60

| | | |
|---|---|---|
| | | |

| | | |
|---|---|---|
| | | |

50

50

Volatility(%)

Volatility(%)

40

40

30

30

20

20

10

10

0 2 4 6 8 10

0 2 4 6 8 10

Years

Years

- Figure 3. Average M/B and Volatility in Simulations. Panel A plots the path of the market-to-book ratio of the new economy (solid line) and old economy (dashed line) averaged across all simulations in which

the new technology was adopted at time t∗∗ (pt∗∗ = 1). Panel B is an equivalent of Panel A, except that the averages are computed across all simulations in which the new technology was not adopted at time t∗∗ (pt∗∗ = 0). Panels C and D are equivalents of Panels A and B, respectively, with M/B replaced by the volatility of stock returns. In each panel, the ﬁrst vertical line denotes t∗ = 1, the time when the new technology becomes available, and the second vertical line denotes t∗∗ = 9, the time at which the agent decides whether to adopt the technology on a large scale. All parameters are given in Table 1.

(A) Revolution: New Economy Beta

(B) No Revolution: New Economy Beta

1.4

1.4

1.2

1.2

- 0.8

- 1

- 0.8

- 1

0 2 4 6 8 10

0 2 4 6 8 10

Years

Years

(D) No Revolution: New Economy Return

(C) Revolution: New Economy Return

60

50

40

Return(%)

Return(%)

20

0

0

Expected

−20

−40

Realized

−60

−50

0 2 4 6 8 10

0 2 4 6 8 10

Years

Years

(F) No Revolution: Old Economy Return

(E) Revolution: Old Economy Return

60

50

40

Return(%)

Return(%)

20

0

0

−20

Expected

−40

−50

Realized

−60

0 2 4 6 8 10

0 2 4 6 8 10

Years

Years

- Figure 4. Beta and Average Stock Return in Simulations. The left panels plot the beta of the new economy (Panel A), the realized stock return (solid line) and the expected stock return (dashed line) for the new economy (Panel C) and the old economy (Panel E), averaged across all simulations in which the

new technology was adopted at time t∗∗ (pt∗∗ = 1). The right panels (B, D and F) plot the same quantities but the average is taken across all simulations in which the new technology was not adopted at time t∗∗

(pt∗∗ = 0). In each panel, the ﬁrst vertical line denotes t∗ = 1, the time when the new technology becomes available, and the second vertical line denotes t∗∗ = 9, the time at which the agent decides whether to adopt the technology on a large scale. All parameters are given in Table 1.

(A) Lower Risk Aversion

10

| | | |
|---|---|---|

8

6

M/B

4

2

0

0 2 4 6 8 10

Years

(C) Higher Uncertainty

8

6

M/B

4

2

0

0 2 4 6 8 10

Years

(B) Zero Conversion Cost

- 0
- 1
- 2
- 3
- 4

| | | |
|---|---|---|

M/B

0 2 4 6 8 10

Years

(D) Faster Adoption

8

| | | |
|---|---|---|

6

M/B

4

2

0

0 2 4 6 8

Years

- Figure 5. Average M/B in Simulated Revolutions: Sensitivity Analysis. All four panels plot the paths of the market-to-book ratio of the new economy (solid line) and old economy (dashed line) averaged

across all simulations in which the new technology was adopted at time t∗∗ (pt∗∗ = 1). All parameters are given in Table 1, except for one change that varies across the panels. In Panel A, the risk aversion γ = 3 instead of the benchmark case γ = 4. In Panel B, the conversion cost κ = 0 instead of the benchmark case κ = 0.1. In Panel C, the uncertainty σt∗ = 0.08 instead of the benchmark case σt∗ = 0.04. In Panel D, the time until the adoption t∗∗ − t∗ = 6 instead of the benchmark case t∗∗ − t∗ = 8 years. In each panel, the ﬁrst vertical line denotes t∗, the time when the new technology becomes available, and the second vertical line denotes t∗∗, the time at which the agent decides whether to adopt the technology on a large scale.

(A) Revolution: Market to Book Ratio

(B) No Revolution: Market to Book Ratio

|New<br><br>Old|
|---|

M/B

M/B

- 0 2 4 6 8 10

- 1

- 1.5

- 2

2.5

3

- 3.5

- 4

- 0 2 4 6 8 10

- 1

- 1.5

- 2

2.5

3

- 3.5

- 4

Years

Years

(C) Revolution: Stock Return Volatility

(D) No Revolution: Stock Return Volatility

40

40

| |
|---|
| |

35

35

Volatility(%)

Volatility(%)

30

30

25

25

20

20

15

15

0 2 4 6 8 10

0 2 4 6 8 10

Years

Years

- Figure 6. Average M/B and Volatility in Simulations with Optimal Adoption Time. Panel A plots the path of the market-to-book ratio of the new economy (solid line) and old economy (dashed line) averaged across all simulations in which the new technology was adopted at an optimally chosen time t∗∗ between years 8 and 10. Panel B is an equivalent of Panel A, except that the averages are computed across all simulations in which the new technology was never adopted. Panels C and D are equivalents of Panels A and B, respectively, with M/B replaced by the volatility of stock returns. All parameters are in Table 1.

(A) New Economy Beta

(B) Stock Return Volatility New

70

| | |
|---|---|
| | |

1.6

60

Old

1.4

Volatility(%)

50

1.2

40

- 0.8
- 1

30

20

0.6

0 2 4 6

0 2 4 6

Years

Years

(C) Market Value

(D) Old Economy Productivity

20

- 10
- 11
- 12
- 13
- 14
- 15

| | |
|---|---|

| | |
|---|---|

15

percent

10

5

0

0 2 4 6

0 2 4 6 8

Years

Years

- Figure 7. The Internet Revolution: Theory. This ﬁgure plots the model-implied dynamics of selected quantities in a revolution characterized by fast adoption of the new technology (such as the internet revolution). All quantities are averages computed across all simulations that led to a revolution (i.e., adoption at time t∗∗ = 6. Panel A reports the market beta of the new economy. Panel B plots the market volatility of the new economy (solid) and old economy (dashed). Panel C plots the market values of the new economy (solid) and old economy (dashed). Panel D plots the productivity of the old economy.

(B) Stock Return Volatility

(A) Beta of NASDAQ

50

2.2

|NASDAQ<br><br>NYSE/AMEX|
|---|

- 1.8

- 2

40

Stddeviation(%peryear)

30

1.6

20

1.4

1.2

10

1

0

1993 1995 1997 1999 2001 2003 2005

1993 1995 1997 1999 2001 2003 2005

Year−end

Year−end

(C) Stock Price Index Level

(D) Productivity Growth

10

||NASDAQ<br><br>NYSE/AMEX|
|---|
|
|---|

Valueof$1investedinJan1992

8

%peryear

6

4

2

0

- 0

- 0.5

- 1

1.5

2

- 2.5

1993

1995 1997 1999 2001 2003 2005

1993 1995 1997 1999 2001 2003 2005 Year−end

Year−end

- Figure 8. The Internet Revolution: Data. Panel A plots the market beta of the NASDAQ index, with a two-standard-error conﬁdence band. The beta in day t is the slope coeﬃcient from the regression of daily NASDAQ returns on NYSE/AMEX returns over the 500 trading days (i.e., about two years) immediately preceding day t (i.e., days t − 499 through t). Panel B plots the standard deviations of returns on the NASDAQ and NYSE/AMEX indices, also computed from daily data over the 500 trading days immediately preceding day t. Panel C plots the value of $1 invested in January 1992 in the NASDAQ and NYSE/AMEX indices, with dividend reinvestment. Panel D plots a three-year moving average of multifactor productivity growth in the private business sector (in year t, we plot the average annual productivity growth in years t − 2, t − 1, and t). The vertical dotted line marks October 2002.

Rail Consumption in the U.S.

4500

4000

3500

3000

2500

Track−miles

2000

1500

1000

500

0

1830 1835 1840 1845 1850 1855 1860

Year

- Figure 9. Total Rail Consumption in the United States. The ﬁgure plots the number of track-miles of rails laid each year in the U.S., as estimated by Fogel (1964, p.174). A track-mile of rails is deﬁned as one half of the length of the rails in a mile of single track. The total includes rails used in the construction of new track as well as in the replacement of worn-out rails.

(A) Railroad Beta

(B) Stock Return Volatility

35

||Beta<br><br>Confidence bands|
|---|
|
|---|

||Railroads<br><br>Non−railroads|
|---|
|
|---|

- 0

0.5

1

- 1.5
- 2

30

Stddeviation(%peryear)

25

20

15

10

5

0

1830 1835 1840 1845 1850 1855 1860 Year

1830 1835 1840 1845 1850 1855 1860

Year

(C) Stock Price Index Level

(D) Aggregate P/D Ratio

1.6

40

||Railroads<br><br>Non−railroads|
|---|
|
|---|

||Railroads<br><br>Non−railroads<br><br>|
|---|
|
|---|

Valueof$1investedinJan1831

35

1.4

30

1.2

25

P/D

- 0.8
- 1

20

15

0.6

10

0.4

5

1830 1835 1840 1845 1850 1855 1860

1830 1835 1840 1845 1850 1855 1860

Year

Year

Figure 10. The Railroad Revolution: Data. Panel A plots the beta of the railroad index, with a two-standard-error conﬁdence band. The beta in month t is the slope coeﬃcient from the regression of the most recent 36 monthly railroad returns (in months t − 35 through t) on non-railroad returns. The monthly railroad (non-railroad) index returns are computed as price-weighted averages of monthly capital gains across all railroad (non-railroad) stocks. Panel B plots the standard deviation of returns in the railroad and non-railroad industries. Each year, this standard deviation is computed across all monthly price-weighted average industry returns in the given year. Panel C plots the stock price index level, obtained by cumulating monthly capital gains to $1 invested in January 1831 in the railroad and non-railroad indices. Panel D plots the aggregate price-to-dividend ratio for the railroad and non-railroad industries. Each year, this ratio is computed as the sum of year-end prices divided by the sum of dividends paid in that year, summing across all railroad (non-railroad) stocks with valid price and dividend data. The vertical dotted line marks 1857.

## Appendix.

The Appendix contains technical material omitted from the text. The proofs of all results are available in the Technical Appendix, which is downloadable from the authors’ websites. Lemma A1: Suppose the prior distribution of ψ at time t∗ is normal, ψ ∼ N(0, σt2∗). Then the posterior distribution of ψ at time t, t∗ < t < t∗∗, conditional on Ft = ρNτ ,ρτ : t∗ ≤ τ ≤ t is also normal, ψ|Ft ∼ N( ψt, σt2), where the posterior mean ψt follows the process d ψt = σt2

φ σN,1

d Z1,t, (17)

[Figure 69]

and the posterior variance σt2 is given by

1 ( σt∗)−2 + σ φ

σt2 =

. (18)

[Figure 70]

2

(t − t∗)

[Figure 71]

N,1

Moreover, the productivity processes can be rewritten as

dρt = φ(ρ − ρt) dt + σd Z0,t (19) dρNt = φ ρ + ψt − ρNt dt + σN,0d Z0,t + σN,1d Z1,t, (20)

[Figure 72]

[Figure 73]

where the Brownian motions ( Z0,t, Z1,t), which capture the agent’s expectation errors, follow

- dZ˜0,t
- dZ˜1,t

=

σ 0 σN,0 σN,1

−1 dρt dρNt

− Et

dρt dρNt

. (21)

Lemma A1 follows from Theorem 10.3 in Liptser and Shiryayev (1977).

- Re Proposition 1: Deﬁne the value function at time t as

V Bt,ρt, ψt, σt,t;T = Et

WT1−γ 1 − γ

[Figure 74]

, (22)

where ρt follows the process in equation (4). Lemma A2 in the Technical Appendix shows:

BT1−γ 1 − γ

Bt1−γ 1 − γ

0(τ)+(1−γ)A1(τ)ρt+(1−γ)A2(τ)ψbt+12(1−γ)2A2(τ)2σbt2,

V Bt,ρt, ψt, σt2,t;T = Et

eA

=

[Figure 75]

[Figure 76]

[Figure 77]

(23) where τ = T − t, A1(τ) and A2(τ) are given in the text, and

A0 (τ) = (1 − γ) ρ(τ − A1 (τ)) +

[Figure 78]

(1 − γ)2 φ2

σ2 2

[Figure 79]

[Figure 80]

1 − e−2φτ 2φ

1 − e−φτ φ

− 2

τ +

[Figure 81]

[Figure 82]

.

Since γ > 1, V (.) is negative, decreasing in σt2, and increasing in Bt. As a result, V Bt∗ (1 − κ),ρt∗,0, σt2∗,t∗;T < V (Bt∗,ρt∗,0,0,t∗;T). (24)

- Proposition 1 follows immediately from equation (24). The left-hand side is the expected utility conditional on adopting the technology at time t∗, and the right-hand side is the expected utility conditional on not adopting the technology at time t∗ or any time afterwards.19 The expected utility from no adoption at time t∗ exceeds the right-hand side (and hence also the left-hand side) because it includes the value of the option to adopt after time t∗.

- Re Proposition 2: Using (23), equation (8) follows from the optimality condition

V Bt∗∗ (1 − κ) ,ρt∗∗, ψt∗∗, σt2∗∗,t∗∗;T ≥ V (Bt∗∗,ρt∗∗,0,0,t∗∗;T). (25)

Lemma A3: The distribution of ψt∗∗ conditional on ψt is normal:

ψt∗∗|ψb

t

∼ N ψt, σt2 − σt2∗∗ .

In addition, pt ≡ Prob ψt∗∗ > ψ| ψt = 1 − N ψ; ψt, σt2 − σt2∗∗ , where N (x;a,s2) ≡

[Figure 83]

[Figure 84]

x

−∞(2πs2)−1/2 exp(y − a)2/(2s2)dy is the c.d.f. of a normal distribution, N(a,s2).

- Re Proposition 3: Deﬁne the value function at time t, t∗ ≤ t < t∗∗, as

V Bt,ρt, ψt, σt2,t;T = Et max

Et∗∗

{yes, no}

WT1−γ 1 − γ

[Figure 85]

, (26)

where the maximization involves choosing whether or not to adopt the new technology at time t∗∗, following Proposition 2.20 Lemma A4 in the Technical Appendix shows:

Bt1−γ 1 − γ

{(1 − pt)Gnot + ptGyest } , (27) where

V Bt,ρt, ψt, σt2,t;T =

[Figure 86]

0(τ)+(1−γ)A1(τ)ρt (28) Gyest = Gnot (1 − κ)1−γ Rte(1−γ)A

Gnot = eA

2(τ∗∗)ψbt+12(1−γ)2A2(τ∗∗)2σbt2 (29)

[Figure 87]

Rt =

1 − N ψ; ψt + (1 − γ)A2 (τ∗∗)( σt2 − σt2∗∗), σt2 − σt2∗∗ 1 − N ψ; ψt, σt2 − σt2∗∗

< 1. (30)

[Figure 88]

[Figure 89]

[Figure 90]

Using (23) and (27), we prove Proposition 3 in the Technical Appendix by showing that expected utility is higher when experimentation takes place:

V Bt∗,ρt∗,0, σt2∗,t∗;T > V (Bt∗,ρt∗,0,0,t∗;T). (31)

[Figure 91]

- 19On the right hand side, V is evaluated at ψt∗ = σt2∗ = 0. If the agent decides not to adopt the new technology, ρt follows the process in equation (3), which is equivalent to equation (4) when ψ = 0.
- 20Note the diﬀerence between the value functions V in equation (26) and V in equation (23). Whereas V includes the value of the option to adopt the new technology at the future time t∗∗, V does not include such option value because it applies to settings in which the adoption decision has already been made.

- Re Proposition 4: The functions Gnot and Gyest are given by

Gnot = Et

BT Bt

[Figure 92]

−γ

| ψt∗∗ < ψ = eA

[Figure 93]

[Figure 94]

0(τ)−γA1(τ)ρt (32)

Gyest = E

BT Bt

[Figure 95]

−γ

| ψt∗∗ ≥ ψ = Gnot (1 − κ)−γ Rte−γA

[Figure 96]

2(τ∗∗)ψbt+12γ2A2(τ∗∗)2σbt2, (33)

[Figure 97]

where

Rt =

1 − N ψ; ψt − γA2 (τ∗∗) ( σt2 − σt2∗∗) , σt2 − σt2∗∗ 1 − N ψ; ψt, σt2 − σt2∗∗

[Figure 98]

[Figure 99]

[Figure 100]

< 1 (34)

[Figure 101]

A0 (τ) = −γρ(τ − A1 (τ)) +

[Figure 102]

σ2 2

[Figure 103]

γ2 φ2

[Figure 104]

τ +

1 − e−2φτ 2φ

[Figure 105]

− 2

1 − e−φτ φ

[Figure 106]

. (35)

- Re Corollary 1: Let pt = 1 − N ψ; ψt − γA2 (τ∗∗) ( σt2 − σt2∗∗) , σt2 − σt2∗∗ . Then

[Figure 107]

Sπ,t =

γA2 (τ∗∗) − pe1

[Figure 108]

t

∂pet

[Figure 109]

∂ψbt Gyest + ∂p

t

[Figure 110]

∂ψbt Gnot (1 − pt) Gnot + pt Gyest

[Figure 111]

. (36)

- Re Proposition 5: The functions Gnot , Gyest , Gnot and Gyest are presented above. The functions Ktno, and Ktyes are given by

Ktno ≡ Et

Ktyes ≡ Et

BT Bt

[Figure 112]

BT Bt

[Figure 113]

−γ BTN BtN

| ψt∗∗ < ψ = KtRNL,t

[Figure 114]

[Figure 115]

−γ BTN BtN

| ψt∗∗ ≥ ψ = (1 − κ)−γ KtNRNH,t,

[Figure 116]

[Figure 117]

where

0(τ)−γA1(τ)ρt+A1(τ)ρNt +A2(τ)ψbt+12 A22(τ)σbt2

Kt = eC

[Figure 118]

2(τ∗∗)ψbt+21γA2(τ∗∗)(γA2(τ∗∗)−2A2(τ))σbt2

KtN = Kte−γA

[Figure 119]

RNL,t =

N ψ; ψt + σyLψb, σt2 − σt2∗∗ N ψ; ψt, σt2 − σt2∗∗

[Figure 120]

[Figure 121]

[Figure 122]

with σyLψb = A2 (τ) σt2 − A2 (τ∗∗) σt2∗∗

RNH,t =

1 − N ψ; ψt + σyHψb, σt2 − σt2∗∗ 1 − N ψ; ψt, σt2 − σt2∗∗

[Figure 123]

[Figure 124]

[Figure 125]

with σyψH = σyψL − γA2 (τ∗∗) σt2 − σt2∗∗

C0 (τ) = (1 − γ)ρ (τ − A1 (τ))

[Figure 126]

1 − e−2φτ 2φ

- 1

[Figure 127]

- 2φ2

τ +

+

[Figure 128]

1 − e−φτ φ

− 2

[Figure 129]

γ2σ2 − 2γσN,0σ + σN,2 0 + σN,2 1 .

Corollary A1: For any t ∈ [t∗,t∗∗), the stock return processes are given by

dMt Mt

= µM,tdt + σM,t0 d Zt0 + σM,t1 d Zt1 and

[Figure 130]

dMtN MtN

= µNM,tdt + σM,tN,0d Zt0 + σM,tN,1d Zt1,

[Figure 131]

where expected returns are equal to the return covariances with dπt/πt,

µM,t = −σM,t0 σπ,t0 − σM,t1 σπ,t1 ; µNM,t = −σM,tN,0σπ,t0 − σM,tN,1σπ,t1 , (37) and the components of the return volatilities are

φ σN,1

σM,t0 = A1 (τ)σ; σM,t1 = (SM,t + Sπ,t) σt2

[Figure 132]

φ σN,1

σM,tN,0 = A1 (τ)σN,0; σM,tN,1 = A1 (τ)σN,1 + SM,tN + Sπ,t σt2

(38)

, (39)

[Figure 133]

with SM,t and SM,tN given by

∂pt

∂ψbt Gyest (1 − pt)Gnot + ptGyest

−∂p

[Figure 134]

∂ψbtGnot + (1 − γ)A2 (τ∗∗) + p1

t

[Figure 135]

[Figure 136]

[Figure 137]

[Figure 138]

t

SM,t =

(40)

[Figure 139]

∂pNL,t

∂pNH,t

∂ψb Ktyes (1 − pt)Ktno + ptKtyes

∂ψb Ktno + (A2 (τ) − γA2 (τ∗∗)) + pN1

A2 (τ) + pN1

[Figure 140]

[Figure 141]

[Figure 142]

[Figure 143]

SM,tN =

L,t

H,t

(41)

[Figure 144]

pt = 1 − N ψ; ψt + (1 − γ) A2 (τ∗∗) σt2 − σt2∗∗ , σt2 − σt2∗∗ (42) pNL,t = N ψ; ψt + σyLψb, σt2 − σt2∗∗ (43) pNH,t = 1 − N ψ; ψt + σyHψb, σt2 − σt2∗∗ . (44)

[Figure 145]

[Figure 146]

[Figure 147]

[Figure 148]

- Re Proposition 6:. The functions hold and hnew are given by

- 1

[Figure 149]

- 2

(1 − 2γ) A2 (τ∗∗)2 σt2 (45)

hold = − κ + A2 (τ∗∗) ψt +

 

  (46)

1 − N ψ; ψt − γA2 (τ∗∗)( σt2 − σt2∗∗), σt2 − σt2∗∗ 1 − N ψ; ψt + (1 − γ)A2 (τ∗∗)( σt2 − σt2∗∗), σt2 − σt2∗∗

−log

[Figure 150]

[Figure 151]

[Figure 152]

 

  (47)

N ψ; ψt + σyLψb, σt2 − σt2∗∗ N ψ; ψt, σt2 − σt2∗∗

hnew = −γA2 (τ∗∗)A2 (τ) σt2 − log

[Figure 153]

[Figure 154]

[Figure 155]

 . (48)

 

1 − N ψ; ψt − γA2 (τ∗∗)( σt2 − σt2∗∗) , σt2 − σt2∗∗ 1 − N ψ; ψt − γA2 (τ∗∗) ( σt2 − σt2∗∗) + σyψL , σt2 − σt2∗∗

−log

[Figure 156]

[Figure 157]

[Figure 158]

[Figure 159]

[Figure 160]

- Re Corollary 2: In the corollary, C0(τ∗∗) = C0(τ∗∗) − A0(τ∗∗).

Re Optimal Adoption Time: The value function is

V Bt,ρt, ψt, σt2,t;T = Et max

Et∗∗

t∗∗

WT1−γ 1 − γ

[Figure 161]

= Bt1−γe(1−γ)A

1(T−t)ρtV2 ψt,t;T , (49)

where V2 ψt,t;T satisﬁes the partial diﬀerential equation

∂V2 ∂t

+ (1 − γ)A1(T − t)φρ +

0 =

[Figure 162]

[Figure 163]

- 1

[Figure 164]

- 2

(1 − γ)2 A1(T − t)2σ2 V2 +

∂2V2 ∂ ψ2

- 1

[Figure 165]

- 2

[Figure 166]

φ σN,1

σt2

[Figure 167]

2

,

with the boundary conditions V2 ψT,T = 1−1γ if t∗∗ > T and

[Figure 168]

V2 ψt,t;T ≥

(1 − κ)1−γ 1 − γ

[Figure 169]

0(τ)+(1−γ)A2(τ)ψbt+21(1−γ)2A2(τ)2σbt2,

eA

[Figure 170]

with an equality at t = t∗∗. We solve the PDE by using the ﬁnite diﬀerence method. Alternative Decentralized Model.

Below, we develop a model of a competitive economy in which ﬁrms independently decide whether to adopt the new technology while maximizing their own market values. We show that, in equilibrium, this decentralized economy produces the same adoption rules and same stock price dynamics (including “bubbles”) as the social planner’s problem in Section 2.

Consider a ﬁnite-horizon economy with a continuum of identical ﬁrms and investors. All investors maximize utility as in Section 2. Before time t∗, all ﬁrms employ the same “old technology.” The productivity ρi,t of any ﬁrm i that uses the old technology follows

dρi,t = φ g sOt − ρi,t dt + σdZ0,t, (50)

where sOt ∈ [0,1] is the fraction of ﬁrms using the old technology at time t, and g (s) > 0. The function g(s) captures “network externalities”: the average productivity of a technology increases as the fraction of ﬁrms using this technology increases. Denote g (1) = ρ and g(0) = ρ0. We refer to ρ − ρ0 > 0 as the network externality gain. Since sOt = 1 for t ≤ t∗, the productivity of all ﬁrms before time t∗ is identical to equation (3) in Section 2.

[Figure 171]

[Figure 172]

[Figure 173]

[Figure 174]

At time t∗ a new unique ﬁrm N appears, equipped with a new technology. The productivity process of ﬁrm N is given by

dρN,t = φ(ρ + ψ − ρN,t)dt + σN,0dZ0,t + σN,1dZ1,t, (51)

[Figure 175]

where ψ is an unobservable productivity gain from using the new technology, as in Section 2. The prior distribution for ψ at time t∗ is given in equation (5). After time t∗, all ﬁrms learn about ψ by observing ρN,t and ρi,t for all i.

Firms using the old technology can adopt the new technology either immediately at time t∗, or at a given later time t∗∗, or never. When they adopt, they incur a proportional

conversion cost κ. If the fraction sNt = 1 − sOt of all ﬁrms use the new technology at time t, the productivity of each ﬁrm i that uses the new technology is given by

dρi,t = φ g sNt + ψ − ρi,t dt + σdZ0,t. (52)

If all ﬁrms adopt the new technology (sNt = 1), then the process (52) is identical to equation (4). Aggregate productivity (obtained by aggregating across identical ﬁrms i) therefore follows the same process (4) as it does in the social planner’s problem. If no ﬁrm adopts the new technology (sNt = 0), then the aggregate economy uses the old technology. Aggregate productivity is then given by the process (50) with sOt = 1, which is identical to equation (3). Once again, aggregate productivity follows the same process as in the planner’s problem. We show below in Proposition D2 that, in equilibrium at time t∗∗, either sNt∗∗ = 1 or sNt∗∗ = 0. Therefore, the pricing kernel for t ≥ t∗∗ is the same as in the planner’s problem, and it depends on whether sNt∗∗ = 1 or sNt∗∗ = 0.

The market value of each ﬁrm at time t∗∗ depends not only on whether the ﬁrm adopts the new technology, but also on the adoption decisions of all other ﬁrms, because those decisions aﬀect the pricing kernel. We denote the market value of ﬁrm i at time t∗∗ as Ms

N=1,yes i,t∗∗ , Ms

N=0,yes i,t∗∗ , or Ms

N=1,no i,t∗∗ , Ms

N=0,no

i,t∗∗ , where “yes” or “no” indicates whether ﬁrm i adopts or not, and “sN = 0” or “sN = 1” indicates whether other ﬁrms adopt or not. Closed-form expressions for these four values are given in the Technical Appendix. Taking the choice of other ﬁrms as given (sN = 1 or sN = 0), each ﬁrm adopts the new technology if doing so maximizes its market value. That is, ﬁrm i adopts if and only if

N=1,yes i,t∗∗ > Ms

N=1,no

Ms

i,t∗∗ if everybody else adopts (53) Ms

N=0,yes i,t∗∗ > Ms

N=0,no i,t∗∗ if nobody else adopts (54)

The following proposition characterizes the value-maximizing adoption decision of any individual ﬁrm, conditional on the decisions of all other ﬁrms at time t∗∗.

Proposition D1: (a) If sNt∗∗ = 1 (i.e., all ﬁrms adopt the new technology at time t∗∗), then ﬁrm i adopts the new technology at time t∗∗ if and only if

log (1 − κ) A2 (τ∗∗)

N=1 = −

ψt∗∗ ≥ ψs

+

[Figure 176]

[Figure 177]

- 1

[Figure 178]

- 2

(2γ − 1) A2 (τ∗∗) σt2∗∗ − (ρ − ρ0) (55)

[Figure 179]

[Figure 180]

(b) If sNt∗∗ = 0 (i.e., no ﬁrm adopts the new technology at time t∗∗), then ﬁrm i adopts the new technology at time t∗∗ if and only if

log (1 − κ) A2 (τ∗∗)

N=0 = −

ψt∗∗ ≥ ψs

−

[Figure 181]

[Figure 182]

- 1

[Figure 183]

- 2

A2 (τ∗∗) σt2∗∗ + (ρ − ρ0) (56)

[Figure 184]

[Figure 185]

N=0. Both thresholds consist of three terms. The ﬁrst term, which reﬂects the conversion cost κ, is the same in both cases. The second term, which reﬂects uncertainty σt∗∗, is positive in (55) but negative in (56). This diﬀerence is due to systematic risk. In case (a), all ﬁrms adopt the new technology, so the equilibrium stochastic discount

N=1 = ψs

In general, ψs

[Figure 186]

[Figure 187]

factor is heavily aﬀected by the risk of the new technology. Hence, the new technology carries higher systematic risk than the old technology. If a ﬁrm adopts the new technology, its beta increases, pushing its discount rate up and market value down. This undesirable feature of the new technology increases the adoption threshold. In case (b), the new technology carries less systematic risk, so the σt∗∗ term reduces the adoption threshold.

The third term reﬂects the network externality gain, ρ − ρ0 > 0. In case (a), all other ﬁrms have already adopted the new technology, so its average productivity is higher and, as a result, the adoption threshold is lower. In case (b), the new technology is less productive because no other ﬁrm has adopted it, so the adoption threshold is higher.

[Figure 188]

[Figure 189]

Intuitively, adopting the same technology as other ﬁrms has two eﬀects. On one hand, it hurts the ﬁrm, because the technology adopted by all other ﬁrms carries more systematic risk. On the other hand, it beneﬁts the ﬁrm through network externality gains.

We are interested in setting up a competitive environment that supports the social planner’s solution. This can be done by a judicious choice of the magnitude of the network externality gains, ρ − ρ0. When we choose ρ0 as

[Figure 190]

[Figure 191]

[Figure 192]

- 1

[Figure 193]

- 2

γA2 (τ∗∗) σt2∗∗, (57) the thresholds in Proposition D1 become equal to each other:

ρ0 = ρ −

[Figure 194]

[Figure 195]

log (1 − κ) A2 (τ∗∗)

N=1 = ψs

N=0 = ψ = −

ψs

+

[Figure 196]

[Figure 197]

[Figure 198]

[Figure 199]

- 1

[Figure 200]

- 2

(γ − 1)A2 (τ∗∗) σt2∗∗.

Moreover, both thresholds are now equal to the threshold ψ in equation (8). In other words, the adoption thresholds in the competitive problem and the social planner’s problem are identical. Still operating under condition (57), we obtain the following proposition.

[Figure 201]

Proposition D2: If ψt∗∗ ≥ ψ, then sNt∗∗ = 1 is a Nash equilibrium. If ψt∗∗ < ψ, then sNt∗∗ = 0 is a Nash equilibrium.

[Figure 202]

[Figure 203]

Proposition D2 shows that, in equilibrium, either all ﬁrms adopt the new technology at time t∗∗ or none of them do.21 Moreover, the adoption decision is analogous to that in

- Proposition 2, with an identical threshold. As a result, the equilibrium stochastic discount factor is the same, and all pricing formulas are identical to those in the planner’s problem.

Note that when all ﬁrms choose to adopt the new technology at time t∗∗, they increase the equilibrium discount rates and thus decrease their market values. Although each ﬁrm maximizes its own market value, the aggregate eﬀect of the ﬁrms’ adoptions is to depress market values at time t∗∗. The reason is that ﬁrms that adopt the new technology do not fully internalize the resulting increases in systematic risk. To summarize, this decentralized model with value-maximizing competitive ﬁrms produces the same stock price dynamics as our simpler model with a utility-maximizing social planner.

[Figure 204]

21We can also prove a related result for time t∗: sNt∗ = 1 is not a Nash equilibrium but sNt∗ = 0 is, under plausible parametric conditions (see Technical Appendix). That is, in equilibrium, no ﬁrm adopts the new technology at time t∗, analogous to our Proposition 1 in the social planner’s problem.

REFERENCES Aghion, Philippe, and Peter Howitt, 1992, A model of growth through creative destruction,

Econometrica 60, 323–351.

Atkeson, Andrew, and Patrick J. Kehoe, 2007, Modeling the Transition to a New Economy: Lessons from Two Technological Revolutions, American Economic Review 97, 64–88.

Benmelech, Efraim, 2007, Asset salability and debt maturity: Evidence from 19th century American railroads, Review of Financial Studies, forthcoming .

Bharath, Sreedhar T., and Siva Viswanathan, 2006, Is the Internet bubble consistent with rationality?, Working paper, University of Michigan.

Brown, Stephen J., William N. Goetzmann, and Stephen A. Ross, 1995, Survival, Journal of Finance 50, 853–873.

Caselli, Francesco, 1999, Technological revolutions, American Economic Review 89, 78–102. Chari, V.V., and Hugo Hopenhayn, 1991, Vintage human capital, growth, and the diﬀusion

of new technology, Journal of Political Economy 99, 1142–1165. Cochrane, W., 1979, The Development of American Agriculture, Minneapolis. Craig, Lee A., and Thomas Weiss, 1993, Agricultural Productivity Growth During the

Decade of the Civil War, Journal of Economic History 53, 527548.

David, Paul A., 1991, Computer and dynamo: The modern productivity paradox in a nottoo-distant mirror, In Technology and Productivity: The Challenge for Economic Policy (OECD, Paris), 315–347.

DeMarzo, Peter, Ron Kaniel, and Ilan Kremer, 2007, Technological Innovation and Real Investment Booms and Busts, Journal of Financial Economics 85, 735–754.

Fogel, Robert W., 1964, Railroads and American Economic Growth: Essays in Econometric History, Johns Hopkins Press, Baltimore, MD.

Goetzmann, William N., Roger G. Ibbotson, and Liang Peng, 2001, A new historical database for the NYSE 1815 to 1925, Journal of Financial Markets 4, 1–32.

Greenwood, Jeremy, and Boyan Jovanovic, 1999, The information-technology revolution and the stock market, American Economic Review Papers and Proceedings 89, 116–122.

Hoberg, Gerard, and Gordon Phillips, 2006, Real and ﬁnancial industry booms and busts, Working paper, University of Maryland.

Hobijn, Bart, and Boyan Jovanovic, 2001, The Information-technology revolution and the stock market: Evidence, American Economic Review 91, 1203–1220.

Johnson, Timothy C., 2007, Optimal learning and new technology bubbles, Journal of Monetary Economics 54, 2486–2511.

Jovanovic, Boyan, 1982, Selection and the evolution of industry, Econometrica 50, 649–670. Jovanovic, Boyan, and Glenn M. MacDonald, 1994, The life cycle of a competitive industry,

Journal of Political Economy 102, 322–347.

Jovanovic, Boyan, and Yaw Nyarko, 1996, Learning by doing and the choice of technology, Econometrica 64, 1299-1310.

Jovanovic, Boyan, and Peter L. Rousseau, 2003, Two technological revolutions, Journal of European Economic Association 1, 419–428.

Jovanovic, Boyan, and Peter L. Rousseau, 2005, General purpose technologies, NBER Working paper #11093.

Klein, Maury, 1994, Unﬁnished Business: The Railroad in American Life, University Press of New England.

- Laitner, John, and Dmitriy Stolyarov, 2003, Technological change and the stock market, American Economic Review 93, 1240–1267.
- Laitner, John, and Dmitriy Stolyarov, 2004a, Aggregate returns to scale and embodied technical change: Theory and measurement using stock market data, Journal of Monetary Economics 51, 191–233.

- Laitner, John, and Dmitriy Stolyarov, 2004b, The role of owned ideas in stock market run-

ups, Working paper, University of Michigan. Malkiel, Burton G., 1999, A Random Walk Down Wall Street, W. W. Norton & Co., NY. Manuelli, Rodolfo E., 2003, Technological change, the labor market and the stock market,

Working paper, University of Wisconsin-Madison. Mazzucato, Mariana, 2002, The PC industry: New economy or early life-cycle?, Review of Economic Dynamics 5, 318–345. Mazzucato, Mariana, and Massimiliano Tancioni, 2006, Stock price volatility and patent citation dynamics, Working paper, Open University.

Mishkin, Frederic S., 1991, Asymmetric information and ﬁnancial crises: A historical perspective, In Financial Markets and Financial Crises, edited by R. Glenn Hubbard, University of Chicago Press, Chicago, 69–108.

Mokyr, Joel, 1990, The Level of Riches: Technological Creativity and Economic Progress, Oxford University Press, New York.

P´astor, Lubosˇ,ˇ and Pietro Veronesi, 2003, “Stock valuation and learning about proﬁtability,” Journal of Finance 58, 1749–1789.

P´astor, Lubosˇ,ˇ and Pietro Veronesi, 2006, “Was there a Nasdaq bubble in the late 1990s?” Journal of Financial Economics 81, 61–100.

Perez, Carlota, 2002, Technological Revolutions and Financial Capital: The Dynamics of Bubbles and Golden Ages, Edward Elgar, Cheltenham, UK.

Romer, Paul, 1990, Endogenous technological change, Journal of Political Economy 98, S71–

S102. Shiller, Robert, 2000, Irrational Exuberance, Princeton University Press, Princeton, NJ. Stover, John F., 1961, American Railroads, University of Chicago Press.

