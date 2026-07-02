arXiv:0809.0822v1[q-fin.TR]4Sep2008

# How markets slowly digest changes in supply and demand

## Jean-Philippe Bouchaud∗, J. Doyne Farmer†, , Fabrizio Lillo‡,†

∗ Science & Finance, Capital Fund Management, 6 Bvd Haussmann, 75009 Paris, France †Santa Fe Institute, 1399 Hyde Park Rd., Santa Fe NM 87505, USA

LUISS Guido Carli, Viale Pola 12, 00198 Roma, Italy ‡Dipartimento di Fisica e Tecnologie Relative, Viale delle Scienze I-90128, Palermo, Italy

ACADEMIC PRESS

##### Abstract

In this article we revisit the classic problem of tatonnement in price formation from a microstructure point of view, reviewing a recent body of theoretical and empirical work explaining how ﬂuctuations in supply and demand are slowly incorporated into prices. Because revealed market liquidity is extremely low, large orders to buy or sell can only be traded incrementally, over periods of time as long as months. As a result order ﬂow is a highly persistent long-memory process. Maintaining compatibility with market eﬃciency has profound consequences on price formation, on the dynamics of liquidity, and on the nature of impact. We review a body of theory that makes detailed quantitative predictions about the volume and time dependence of market impact, the bid-ask spread, order book dynamics, and volatility. Comparisons to data yield some encouraging successes. This framework suggests a novel interpretation of ﬁnancial information, in which agents are at best only weakly informed and all have a similar and extremely noisy impact on prices. Most of the processed information appears to come from supply and demand itself, rather than from external news. The ideas reviewed here are relevant to market microstructure regulation, agent-based models, cost-optimal execution strategies, and understanding market ecologies.

CONTENTS

- 1 Introduction 5

- 1.1 Overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
- 1.2 Organization of the paper . . . . . . . . . . . . . . . . . . . . . . 6
- 1.3 Motivation and scope . . . . . . . . . . . . . . . . . . . . . . . . . 6
- 1.4 Approach to model building . . . . . . . . . . . . . . . . . . . . . 9

- 2 Market structure 10
- 3 Information, liquidity & eﬃciency 11

- 3.1 Information and fundamental values . . . . . . . . . . . . . . . . . 12
- 3.2 Market eﬃciency . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
- 3.3 Trading and information . . . . . . . . . . . . . . . . . . . . . . . 14
- 3.4 Diﬀerent explanations for market impact . . . . . . . . . . . . . . 15
- 3.5 Noise trader models and informed vs. uninformed trading . . . . . 16
- 3.6 A critique of the noise trader explanation of market impact . . . . 17
- 3.7 The liquidity paradox – price are not in equilibrium . . . . . . . . 18
- 3.8 Time scales and market ecology . . . . . . . . . . . . . . . . . . . 20
- 3.9 The volatility puzzle . . . . . . . . . . . . . . . . . . . . . . . . . 22
- 3.10 The Kyle model . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23

- 4 Large ﬂuctuations and long-memory of order ﬂow 24

- 4.1 Empirical evidence for long-memory of order ﬂow . . . . . . . . . 24
- 4.2 On the origin of long-memory of order ﬂow . . . . . . . . . . . . . 26
- 4.3 Theory for long-memory in order ﬂow based on strategic order splitting . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
- 4.4 Evidence based on exchange membership codes . . . . . . . . . . 29
- 4.5 Evidence for heavy tails in volume . . . . . . . . . . . . . . . . . . 31

- 5 Summary of empirical results for diverse types of market impact 31

- 5.1 Impact of individual transactions . . . . . . . . . . . . . . . . . . 33
- 5.2 Impact of aggregate transactions . . . . . . . . . . . . . . . . . . 34
- 5.3 Hidden order impact . . . . . . . . . . . . . . . . . . . . . . . . . 36
- 5.4 Upstairs market impact . . . . . . . . . . . . . . . . . . . . . . . . 37

- 6 Theory of market impact 37

- 6.1 Why is individual transaction impact concave? . . . . . . . . . . . 38
- 6.2 A ﬁxed permanent impact model . . . . . . . . . . . . . . . . . . 40
- 6.3 The MRR model . . . . . . . . . . . . . . . . . . . . . . . . . . . 41
- 6.4 A transient impact framework . . . . . . . . . . . . . . . . . . . . 42

- 6.4.1 Transient impact and mean reversion . . . . . . . . . . . . 43
- 6.4.2 Mathematical theory of long term resilience . . . . . . . . 43

- 6.5 History dependent, permanent impact . . . . . . . . . . . . . . . 45

- 6.5.1 Predictable order ﬂow and statistical eﬃciency . . . . . . . 45
- 6.5.2 Equivalence with the transient impact model . . . . . . . . 47
- 6.5.3 More general information models . . . . . . . . . . . . . . 47
- 6.5.4 Mechanisms for Asymmetric Liquidity . . . . . . . . . . . 48

- 6.6 Empirical results . . . . . . . . . . . . . . . . . . . . . . . . . . . 51
- 6.7 Impact of a large hidden order . . . . . . . . . . . . . . . . . . . 54
- 6.8 Aggregated impact . . . . . . . . . . . . . . . . . . . . . . . . . . 56

- 6.8.1 Independent identically distributed order ﬂow . . . . . . . 57
- 6.8.2 Transient impact model . . . . . . . . . . . . . . . . . . . 58

- 7 The determinants of the Bid-Ask spread 59

- 7.1 The basic economics of spread and impact . . . . . . . . . . . . . 59

- 7.1.1 The average gain of market makers . . . . . . . . . . . . . 59
- 7.1.2 How informed are the trades? . . . . . . . . . . . . . . . . 60

- 7.2 Models for the bid-ask spread . . . . . . . . . . . . . . . . . . . . 62

- 7.2.1 The Glosten-Milgrom model . . . . . . . . . . . . . . . . . 62
- 7.2.2 The MRR model with a bid-ask spread . . . . . . . . . . . 64

- 7.3 Limit vs. market orders: the microstructure phase diagram . . . . 66

- 7.3.1 Market order strategies . . . . . . . . . . . . . . . . . . . . 66
- 7.3.2 An inﬁnitesimal market making strategy . . . . . . . . . . 67
- 7.3.3 Comparison with empirical data . . . . . . . . . . . . . . . 69

- 7.4 Spread dynamics after a temporary liquidity crisis . . . . . . . . . 71

- 8 Liquidity and volatility 72

- 8.1 Liquidity and large price changes . . . . . . . . . . . . . . . . . . 72
- 8.2 Volume vs. liquidity ﬂuctuations as proximate causes of volatility 75
- 8.3 Spread vs. volatility . . . . . . . . . . . . . . . . . . . . . . . . . 77
- 8.4 Market cap eﬀects . . . . . . . . . . . . . . . . . . . . . . . . . . . 80

- 9 Order book dynamics 81

- 9.1 Heavy tails in order placement and the shape of the order book . 82
- 9.2 Volume at best prices: the Glosten-Sandas model . . . . . . . . . 83
- 9.3 Statistical models of order ﬂow and order books . . . . . . . . . . 85

- 9.3.1 Zero intelligence models . . . . . . . . . . . . . . . . . . . 85
- 9.3.2 Statistical model of order book . . . . . . . . . . . . . . . 87
- 9.3.3 A simple empirical agent based model for liquidity ﬂuctuations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 89

- 10 Impact and optimized execution strategies 91
- 11 Toward an empirical characterization of a market ecology 93

- 11.1 Identifying hidden orders . . . . . . . . . . . . . . . . . . . . . . . 94
- 11.2 Specialization of strategies . . . . . . . . . . . . . . . . . . . . . . 95

### 12 Conclusions 96

- 12.1 Deﬁnition of mechanical impact for order books . . . . . . . . . . 99
- 12.2 Empirical results . . . . . . . . . . . . . . . . . . . . . . . . . . . 100 Bibliography104

1 INTRODUCTION

- 1.1 Overview

In this article we discuss the slow process by which markets “digest” ﬂuctuations in supply and demand, reviewing a body of work that suggests a new approach to the classic problem of tatonnement, the dynamic process through which markets seek to reach equilibrium. The foundation of this approach is based on several empirical observations about ﬁnancial markets, the most important of which is long-memory in the ﬂuctuations of supply and demand. This is exhibited in the placement of trading orders, and corresponds to long term, slowly decaying positive correlations in the initiation of buying vs. selling. It is observed in all the stock markets studied so far at very high levels of statistical signiﬁcance. It appears that the primary cause of this is the incremental execution of large hidden trading orders. The fact that the long-memory of order ﬂow must coexist with market eﬃciency (at least in a statistical sense) has a profound inﬂuence on price formation, causing dynamic adjustments of liquidity that are strongly asymmetric between buyers and sellers.

This has important consequences for market impact. (By market impact we mean the average response of prices to trades; liquidity refers to the scale of the market impact)1. We discuss theoretical work predicting the average market impact as a function of both volume and time. The asymmetric liquidity adjustments needed to maintain compatibility between the long-memory of order ﬂow and market eﬃciency can equivalently be interpreted in terms of the temporal response of market impact, leading to a slow decay of market impact with time.

This work also has important consequences about the interpretation and eﬀect of information in ﬁnancial markets. In particular, the explanation for market impact that we develop here from the standard view in the ﬁnance literature, which holds that the shape of the impact function is determined by diﬀerences in the information content of trades. The body of work reviewed here instead assumes that the impact of trades depends only on their predictability, e.g. that highly predictable trades have little impact, as originally postulated by Hasbrouck [1988]. We argue that this is a much simpler explanation, that produces stronger

- 1 Market impact is closely related to the demand elasticity of price, and is typically measured

- as the return associated with a transaction as a function of volume. Liquidity (as we will use it here) measures the size of the price response to a trade of a ﬁxed size, and is inversely proportional to the scale of the impact. If trading a given quantity produces only a small price change, the market is liquid, and if it produces a large price change it is illiquid.

predictions, is more plausible from a theoretical point of view, and is more in line with what is observed in the data.

The implications of this work range upward from microstructure, i.e. at the level of individual price changes, to patterns of price formation on timescales that can be measured in months. At the microstructure level this work makes several predictions, such as the relationship between market impact, the bid-ask spread, and volatility. It also make predictions about the impact of large trades executed over long times, as well as the eﬀect such trades may have in causing clustered volatility.

### 1.2 Organization of the paper

In the remainder of the introduction we discuss the motivation and scope of the work described here, and discuss our approach to creating a theory for market microstructure, which is somewhat unusual within economics. In Section 2 we discuss the institutional aspects of the markets that form the basis of our empirical studies and deﬁne some of the terms that will be used throughout the paper. In Section 3 we lay out some of the main conceptual issues, discussing the concept of information in ﬁnance and its relationship to market eﬃciency, and the important role that liquidity (or more accurately, the lack of liquidity) plays in forming markets. We critique so-called “noise trader” models and present an alternative point of view. In Section 4 we present the empirical evidence for long-memory in order ﬂow, develop a theory for its explanation based on strategic order splitting, and present evidence that this theory is correct. In Section 5 we describe the diﬀerent types of impact and review the empirical evidence. In Section 6 we develop a theory for market impact for each of the diﬀerent types of impact. In Section 7 we discuss the problem of explaining the behavior of the bid-ask spread, and compare theory and empirical observations. Section 8 discusses the close relationship between liquidity and volatility. In Section 9 we discuss models for the order book, which can be regarded as models for liquidity. Section 10 discusses the problem of trading in an optimal manner in order to minimize execution costs. Section 11 describes recent attempts to characterize trading ecologies of market behavior at short time scales, and Section 12 presents our conclusions.

### 1.3 Motivation and scope

Markets are places where buyers meet sellers and the price of exchanged goods are ﬁxed. As originally observed by Adam Smith, during the course of this apparently simple process remarkable things happen. The information of diverse buyers and sellers, which may be too complex and textured for any of them to fully articulate, is somehow incorporated into a single number, the price. One of the powerful achievements of economics has been the formulation of simple and elegant equilibrium models that attempt to explain the end results of this

process without going into the details of the mechanisms through which prices are actually set.

There has always been a nagging worry, however, that there are many situations in which broad-brush equilibrium models that do not delve suﬃciently deeply into the process of trading and the strategic nature of its dynamics, may not be good enough to tell us what we need to know; to do better we will ultimately have to roll up our sleeves and properly understand how prices change from a more microscopic point of view. Walras himself worried about the process of tatonnement, the way in which prices settle into equilibrium. While there are many proofs for the existence of equilibria, it is quite another matter to determine whether or not a particular equilibrium is stable under perturbations, i.e. whether prices that are initially out of equilibrium will be attracted to an equilibrium. This necessarily requires a more detailed model of how prices are actually formed. There is a long history of work in economics seeking to create models of this type (see e.g. Fisher [1983]), but many would argue that this line of work was ultimately not very productive, and in any case it has had little inﬂuence on modern mainstream economics.

A renewed interest in dynamical models that incorporate market microstructure is driven by many factors. In ﬁnance, one important factor is growing evidence suggesting that there are many situations where equilibrium models, at least in their current state, do not explain the data very well. Under the standard model prices should change only when there is news, but there is growing evidence that news is only one of several determinants of prices, and that prices can stray far from fundamental values (Campbell and Shiller [1989], Roll [1984], Cutler et al. [1989], Joulin et al. [2008])2. Doubts are further fueled by a host of studies in behavioral economics demonstrating the strong boundaries of rationality. Taken together this body of work calls into question the view that prices always remain in equilibrium and respond instantly and correctly to new information.

The work reviewed here argues that trading is inherently an incremental process, and that because of this, prices often respond slowly to new information. The reviewed body of theory springs from the recent empirical discovery that changes in supply and demand constitute a long-memory process , i.e. that its autocorrelation function is a slowly decaying power law (Bouchaud et al. [2004], Lillo and Farmer [2004]). This means that supply and demand ﬂow in and out of the market only very gradually, with a persistence that is observed on timescales of weeks or even months. We argue that this is primarily caused by the practice of order splitting, in which large institutional funds split their trading orders into many small pieces. Because of the heavy tails in trading size, there are long periods where buying pressure dominates, and long periods where selling pressure dominates. The market only slowly and with some diﬃculty “digests” these

2 See Engle and Rangel [2005] for a dissenting view.

swings in supply and demand. In order to keep prices eﬃcient, in the sense that they are unpredictable and there are not easy proﬁt making opportunities, it has to make signiﬁcant adjustments in liquidity. Understanding how this happens leads to a deeper understanding of many properties of market microstructure, such as volatility, the bid-ask spread, and the market impact of individual incremental trades. It also leads to an understanding of important economic issues that go beyond market microstructure, such as how large institutional orders impact the price, and in particular how this depends on both the quantity traded and on time. It implies that the liquidity of markets is a dynamic process with a strong historical dependence.

The work reviewed here by no means denies that information plays a role in forming prices, but it suggests that for many purposes this role is secondary. In the last half of the twentieth century ﬁnance has increasingly emphasized information and de-emphasized supply and demand. The work we review here brings forward the role of ﬂuctuations in supply and demand, which may or may not be exogenous. As we view it, it is useful to begin the story with a quantitative description of the properties of ﬂuctuations in supply and demand. Where such ﬂuctuations come from doesn’t really matter; they could be driven by rational responses to information or they could simply be driven by a demand for liquidity. In either case, they imply that there are situations when order arrival can be very predictable. Orders contain a variable amount information about the hidden background of supply and demand. This aﬀects how much prices move, and therefore modulates the way in which information is incorporated into prices. This notion of information is internal to the market. In contrast to the prevailing view in market microstructure theory, there is no need to distinguish between “informed” and “uninformed” trading to explain important properties of markets, such as the shape of market impact functions or the bid-ask spread3.

We believe the work here should have repercussions on a wide gamut of questions:

- • At a very fundamental level – how do we understand why prices move, how information is reﬂected in prices and what ﬁxes the value of the volatility?;
- • At the level of price statistics – what are the mechanisms leading to price jumps and volatility clustering?;
- • At the level of market organisation – what are the optimal trading rules to insure immediate liquidity and orderly ﬂow to investors?;
- • At the level of agent-based models – what are the microstructural ingredients necessary to build a realistic agent-based model of price changes?
- • At the level of trading strategies and execution costs – what are the consequence of empirical microstructure regularities on transaction costs and implementa-

3 Since modern continuous double auction markets are typically anonymous, it is hard to see how the identity of traders could play an important role in the size of the price response to trades. See the discussion in Section 3.

tion shortfall?

We do not wish to imply that these questions will be answered here, only that the word described here bears on all of them. We will return to discuss the implications in the conclusions.

### 1.4 Approach to model building

Because this work reﬂects an approach to model building that many economists will ﬁnd unfamiliar, we ﬁrst make a few remarks to help the reader understand the philosophy behind this approach. Put succinctly, our view is that the enormous quantities of data that are now available fundamentally change the approach one should take to building economic theories about ﬁnancial markets.

In recent years the computer has made it possible to automate markets, has enabled an explosion in the amount of recorded data, and makes it possible to analyze unprecedented quantities of information. Financial instruments are now typically standardized, stable entities that are traded day after day by many thousands of market participants. Modern electronic markets oﬀer an open and transparent environment that allows traders across the world to get real time access to prices, and most importantly for science, makes it possible to save detailed records of human decision making. The past decades have seen an explosion in the volume of stored data. For example, the total volume of data related to US large caps on, say Oct 2, 2007, was 57 million lines, approximately a gigabyte of stored data. The complete record of world ﬁnancial activity is more than a terabyte per day. Each market has slightly diﬀerent rules of operation, making it possible to compare market structures and how they aﬀect price formation, and most important of all, to look for patterns of behavior that are common across all market structures. The system of world ﬁnancial markets can be viewed as a huge social science experiment in which proﬁt-seekers spend large quantities of their own money to collect enormous quantities of data for the pleasure of scientists.

With so much data it becomes possible to change the style in which economics is done. When one has only a small amount of noisy data statistical testing must be done with great care and it is diﬃcult to test and reject competing models unless the diﬀerences in their predictions are very large. Data snooping is a constant worry. In contrast, with billions of data points if an eﬀect is not strong enough to leap out of the noise it is unlikely to be of any economic importance. Even more important is the eﬀect this has on the development and testing of theories. With a small data set inference requires strong priors. This fosters an approach in which one begins with pure theory and tests the resulting models only after they are fully formulated; there is less opportunity to let the data speak for itself. Without great quantities of data it is diﬃcult to test a theory in a fully quantitative manner, and so predictions of theories are typically qualitative.

The work reviewed in this article takes advantage of the size of ﬁnancial data

MARKET STRUCTURE 10

sets by strongly coupling the processes of model formation and data analysis. This begins with a search for empirical regularities, i.e. behaviors that under certain circumstances follow consistent quantitative laws. Even though such eﬀects do not have the consistency of the laws of physics, one can nonetheless be somewhat more ambitious than simply trying to establish a set of “stylized facts”. An attempt is made to describe regularities in terms that are suﬃciently quantitative so that theories have a clear target, and can thus sensibly make strongly falsiﬁable predictions. A key goal of such theories is of course to understand the necessary and suﬃcient conditioned for regularities.

The approach for building theory described here is phenomenological. That is, it does not attempt to derive everything from a set of ﬁrst principles, but rather simply tries to connect diverse phenomena to each other in order to simplify our description of the world. Many economists will be uncomfortable with this approach because it often lacks “economic content”, i.e. the theories that are developed do not invoke utility maximization. In this sense this body of work lies somewhere between pure econometrics and what is usually called a theory in micro-economics. Even though the models infer properties of agent behavior, and connect them to market properties such as prices, there is no attempt to derive the results from theories that maximize preferences, contenting ourselves with weaker assumptions, such as market eﬃciency. Given all the empirical problems surrounding the concept of utility, we view this as a strength rather than a weakness.

The work described here is still in an early stage, and is very much in ﬂux; many of these results are quite new and indeed our own view is still changing as new results appear.

### 2 MARKET STRUCTURE

All of the work described here is based on results from studying stocks from the London, Paris, New York (NYSE and NASDAQ) and Spanish stock markets. These markets diﬀer in their details, but they all do at least half of their trading (and in some cases all their trading) through a continuous double auction. “Auction” indicates that participants may place quotes (also called orders) stating the quantities and prices at which they are willing to trade; “continuous” indicates that they can update, cancel or place new quotes at any time, and “double” indicates that the market is symmetric between buyers and sellers4.

There are some important diﬀerences in the way these markets are organized. The NYSE is unusual in that each stock has a designated specialist who maintains and clears the limit order book. The specialist can see the identity of all the quotes and can selectively show them to others. The specialist can also trade for his own account but has regulatory obligations to “maintain an orderly market”.

4 There are some small exceptions to symmetry between buying and selling, such as the uptick rule in the NYSE, but these are relatively small eﬀects.

The London Stock Exchange in contrast, has no specialists. It is completely transparent in the sense that all orders are visible to everyone, but completely anonymous in the sense that there is no information about the identity of the participants, and such information is not disclosed even to the counterparties of transactions. The Spanish Stock Market is unusual in that membership codes for quotes are publicly displayed. Thus these exchanges are generically similar but have their own peculiar characteristics.

Markets also diﬀer in the details of the types of orders that can be placed. For example, the types of orders in the London Stock Exchange are called “limit orders”,“market orders with limiting price”, “ﬁll-or-kill”, and “execute & eliminate”. In order to treat these diﬀerent types simply and in a uniﬁed manner we simply classify them based on whether an order results in an immediate transaction, in which case we call it an eﬀective market order, or whether it leaves a limit order sitting in the book, in which case we call it an eﬀective limit order. Marketable limit orders (also called crossing limit orders) are limit orders that cross the opposing best price, and so result in at least a partial transaction. The portion of the order that results in an immediate transaction is counted as an eﬀective market order, while the non-transacted part (if any) is counted as an effective limit order; thus in this case a single action by the participant gets counted

- as two separate orders. Note that we typically drop the term “eﬀective”, so that e.g. “market order” means “eﬀective market order”. Similarly a limit order can be removed from the book for many reasons, e.g. because the agent changes her mind, because a time speciﬁed when the order was placed has been reached, or because of the institutionally-mandated 30 day limit on order duration. We will lump all of these together, and simply refer to them as “cancellations”.

In addition to continuous double auctions the London Stock Exchange has what is called the oﬀ-book market and the New York Stock Exchange has what is called the upstairs market. These are both bilateral exchanges, in which members of the exchange can interact in person or via telephone to arrange transactions. Such transactions are then reported publicly at a later time. With exceptions noted in the text all the results obtained are from the continuous markets.

### 3 INFORMATION, LIQUIDITY & EFFICIENCY

The aim of this section is to motivate the empirical study of microstructure in a broader economic context, that of the information content of prices and the mechanisms that can lead to market eﬃciency. We discuss several fundamental questions concerning how markets operate. The discussion here sets the stage for the detailed quantitative investigations that we report in the following sections. Since one of our main subjects here is market impact, we review and critique the standard model for market impact, which is based on informed vs. uninformed trading.

### 3.1 Information and fundamental values

It is often argued that there is a fundamental value for stocks, correctly known to

- at least some informed traders, who buy underpriced stocks and sell overpriced stocks. By doing so they make a proﬁt and, through the very impact of their trades, drive back the price toward its fundamental value. This mechanism is the cornerstone of the theory of eﬃcient markets, and is often used to justify why prices are unpredictable. In such a framework, the fundamental value of a stock can only change with unanticipated news. The scenario is then the following: A piece of news becomes available, market participants work out how this changes the price of the stock, and trade accordingly. After a (supposedly fast) phase of ‘tatonnement’, the price converges to its new equilibrium value, and the process repeats itself. To explain deviations from this picture one can add a suitable fraction of uninformed trades to add some high frequency noise.

Is this picture fundamentally correct to explain why prices move and to account for the observed value of the volatility? Judging from the literature, it looks as if a majority of academics still believe that this story is at least a good starting point (but see, for example Lyons [2001]). Recent empirical microstructure studies open the way to testing in detail the basic tenets and the overall plausibility of the standard equilibrium picture. We hope to convince the reader that the story is in fact signiﬁcantly diﬀerent. That is, we argue that an alternative way of looking at events provides superior explanatory power based on a simpler set of hypotheses. Before discussing at length the microstructural evidence for a change of paradigm, we would like at this stage to make several general comments that will be relevant below; ﬁrst on the very notion of fundamental value and information, and second on various orders of magnitude and time scales involved in the problem.

Is the fundamental value of a stock or a currency a valid concept, in the sense that it can be computed, at least as a matter of principle, with arbitrary accuracy with all information known at time t? The number of factors inﬂuencing the fundamental value of a company or of a currency is so large that there should be, at the very least, an irreducible intrinsic error. All predictive tools used by traders, either based on economic ratios, earning forecasts, etc., are based on statistical models detecting trends or mean-reversion, are obviously noisy and sometimes even biased. For example, ﬁnancial experts are known to be on the whole rather bad at forecasting the next earning of a company (see e.g. Guedj and Bouchaud [2005]). News are often ambiguous and not easy to interpret. But if we accept the idea of an intrinsically noisy fundamental value with some band of width ∆ within which the price can almost freely wander, the immediate question is: how large is the uncertainty ∆? Is it very small, say 10−3 in relative terms, or quite a bit larger, say 100%, as suggested by Black [1986]? If Black is right (which we tend to believe) and the uncertainty in the fundamental value is large, then the information contained in a trade is noisy, and the amount of information contained in any given trade is necessarily small. Analysis of price impact makes

it clear that the standard deviation of impacts is very large compared to their mean, suggesting that this is indeed the case.

### 3.2 Market eﬃciency

Market eﬃciency is one of the central ideas in ﬁnance and appears in many guises. A standard deﬁnition of market eﬃciency (in the informational sense) is that the current price should be the best predictor of future prices, i.e. that prices should be a martingale. Another closely related notion is arbitrage eﬃciency, which in its weakest form states that it should not be possible to make a proﬁt without taking risks; in a stronger form it says that two strategies with the same risk should make the same proﬁts, at least once their usefulness for inclusion in a portfolio is taken into account. Steve Ross, among others, has advocated that market eﬃciency (rather than equilibrium) should be the core postulate for ﬁnancial theory (Ross [2004]).

We agree with this point of view, at least in so far as it does not imply believing in allocative eﬃciency, i.e. that prices correctly reﬂect the underying value of the assets. Strictly speaking a market is allocatively eﬃcient if it is Pareto optimal, in the sense that there is no alternative allocation of prices and holdings that makes someone better oﬀ without making someone worse oﬀ. This is related to whether or not prices are set at their “proper” values. It is entirely possible to imagine a market in which prices are unpredictable and yet in which there is no sense in which prices are set correctly. That is, once we depart from neoclassical equilibrium a market might be informationally eﬃcient yet allocatively ineﬃcient.

A closely related point is that there are two very diﬀerent possible explanations for market eﬃciency. (1) The standard view in economics is that perfect eﬃciency reﬂects perfect information processing. Traders process each new bit of information as it arrives and prices immediately go to their new equilibrium values. This is, however, by no mean the only explanation for why prices can be a martingale. An obvious alternative is the standard one that explains randomness in many other ﬁelds, such as ﬂuid turbulence: (2) Markets are too complicated to be predictable. Under this explanation prices move randomly because investor behavior is complicated, based on many hidden factors, so to an external observer it is “as if” individual investors are just ﬂipping coins. The correct explanation is likely to be a mixture of both eﬀects. On one hand markets are inherently complicated, but on the other hand, whatever predictability is left over is substantially removed by arbitrageurs. Under this synthetic view, which we take here, one can simply associate an impact with trades, treat all investors as more or less the same, and adjust the expected impact as needed to preserve eﬃciency based on factors that derive from the predictability of trades.

Finally we want to emphasize that while we believe that market eﬃciency is a very useful concept and provides an excellent starting point for developing theories, it is inherently contradictory, and is at best an approximation. Markets can

only be informationally eﬃcient at ﬁrst order but must necessarily be ineﬃcient

- at second order. This was originally pointed out by Milton Friedman, who noted that without informed traders to push prices in the right direction, there is no reason that markets should ever be eﬃcient. If markets were truly eﬃcient then informed traders should make the same proﬁts as anyone else, and there would be no motivation for them to remain in the market. Thus markets cannot be fully eﬃcient.

Even if for many purposes it can be a good approximation to assume that they markets are eﬃcient, there are other situations where deviations from eﬃciency can be quite important. Understanding how markets evolve from ineﬃcient to eﬃcient states, predicting the necessary level of deviations from eﬃciency that must persist in steady state, and understanding their role in how markets function remains an area of investigation that is still largely not understood. This is relevant for our discussions on incorporating information into prices because when we speak about information we must have traders to process that information and trade based on it. It is precisely the market impact of these traders that moves prices. Thus while on one hand market impact is a friction, it can also be viewed

- as the factor that maintains eﬃciency, and so it is essential to properly understand it.

### 3.3 Trading and information

Informational eﬃciency means that information must be properly incorporated into prices. Under assumptions of rationality, when all traders have the same information, prices should move more or less automatically, with very little trading (Milgrom and Stokey [1982], Sebenius and Geanakoplos [1983]). But of course that’s not true – people don’t have the same information, and even if they did, real people are likely to take diﬀerent views about what the information means. The empirical fact that there is so much trading supports this (Shiller [1981]). Grossman and Stiglitz [1980] developed an equilibrium model in which traders have diﬀerent information, that shows that in this situation trading and price movements are informative (see also Grossman [1989]). If I know that you are rational, and I know that you have diﬀerent information than I have, when I see you trade and the price rises I can infer the importance of your information and thus I should change my own valuation.

Intuitively the problem with this view is that even small deviations from rationality and perfect information can lead to incorrect prices and instabilities in the price process. Suppose, for example, that you and I both overestimate how much information the other has. Then when I see you trade I change my valuation too much. When I see you buy, I also buy, but I buy more than I should. To make this slightly more quantitative, let the initial price be p0 and suppose that after agent A observes new fundamental information the price rises by f, which might or might not be the correct fundamental level. After agent A trades the

new price becomes p1 = p0 + f. Agent B sees the price rise by f, and assuming that agent A has more information than he really does, he buys and causes the price to rise to p2 = p0 + af. Then B sees the price rise more than f, so he buys, driving it to p3 = p0 + a2f, and so on. This process is clearly unstable if a > 1. The agents either need to know the value of a exactly or they need to be able to adapt a based on information that is not contained in the price. It is diﬃcult to understand how they can do this since by deﬁnition if they are not rational, not only do they not have full information, they do not know how much information they have, and they thus cannot know a priori the proper value of a. Under deviations from rationality, deviations from fundamentals are inevitable. For a beautiful model where copy-cats lead to such instabilities, see P. Curty and M. Marsili [2006].

In its extreme version, this is just the kind of scenario that occurs during a bubble (see Bouchaud and Cont [1998] for an explicit model of this). Any reasonable investor who lived through the millennium technology bubble experienced this problem. Even though high prices seemed diﬃcult to rationalize based on values, prices kept going up. This led many sanguine investors to lose conﬁdence in their own valuations, and to hang on to their shares much longer than they thought was reasonable. If they didn’t do this they experienced losses as measured relative to their peers. Under this view, bubbles stem from the problem of not knowing how much information price movements really contain, and the feedback eﬀects that occur when most people think they contain more information than they really do. This point of view diﬀers from that in the standard literature on rational bubbles. As we argue below, while not entirely diﬀerent, there are important contrasts between this view and the standard rational expectations/noise

- trader models.

- 3.4 Diﬀerent explanations for market impact Why is there market impact? We will distinguish three possibilities:

- 1. Trades convey a signal about private information. This idea, discussed in the previous section, was developed by Grossman and Stiglitz [1980]. The arrival of new private information causes trades, which cause other agents to update their valuations, which changes prices. In this case it is fair to say that trades cause price changes, since even if there happens to be no information, unless this is common knowledge the observation of a trade is still interpreted as information, which causes the price to change.
- 2. Agents successfully forecast short term price movements and trade accordingly. This can result in measurable market impact even if these agents have absolutely no eﬀect on prices at all. If an agent correctly forecasts price movements and trades based on this forecast, when this agent buys there will be a tendency for the price to subsequently rise. In this case causality runs backward, i.e. because the price is about to rise, agents are more likely

- to trade in anticipation of it, but a trade based on no information will have no eﬀect.
- 3. Random ﬂuctuations in supply and demand. Even in the standard market clearing framework, if a given agent increases her demand while other agents keep theirs constant, when the market clears that agent buys and the price rises. Fluctuations in supply and demand can be completely random, unrelated to information, and the net eﬀect regarding market impact is the same. In this sense impact is a completely mechanical – or better, statistical, phenomenon. As we will see in Appendix 1, the meaning of this can be subtle and may depend on the market framework.

All three of these result in identical short term market impact, i.e. a positive correlation of trading volume and price movement, but are conceptually very diﬀerent. If some traders really have an information on the “true” price at some time in the future (say the end of the day, after the market closes), then the observation of an excess of buy trades allows the market to guess that the price will move up and to change the quotes accordingly (see Section 7.2.1 on the Glosten-Milgrom model). In this sense, information is progressively included into prices, as a function of the observed order ﬂow. In this picture, as emphasized in Hasbrouck [2007], “orders do not impact prices. It is more accurate to say that orders forecast prices.” But if the mechanical interpretation is correct, correlation between price changes and order ﬂow is a tautology. If prices move only because of trades, “information revelation” may merely be a self-fulﬁlling prophecy which would occur even if the fraction of informed traders is zero. The only possible diﬀerences between these picutres come about in the temporal behavior of impact, which we will discuss in Section 6.

### 3.5 Noise trader models and informed vs. uninformed trading

In behavioral ﬁnance the problem of irrational investors is typically coped with by introducing “noise trader” models, in which some agents (the noise traders) are stupid while others are completely rational (Kyle [1985], Delong et al. [1990], Shleifer [2000]). Noise trading could be driven by the need for liquidity (here meaning the need to raise capital for other reasons), it could be driven by the desire to reduce risk, or it could be “irrational behavior”, such as trend following. The assumption is made that such investors lack the skill or information processing ability to collect and/or make full use of information. The rational investors, in contrast, are assumed to correspond to skilled professionals. Their trading is perfect, in the sense that they know everything. Examples of what they must know includes the strategies of all the noise traders, and the fraction of capital traded by noise traders as opposed to rational investors. In such models prices can deviate from fundamental values due to the action of the noise traders and the desire of the rational agents to exploit them as much as possible, but the rational agents always keep them from deviating too much. In such

models the rational traders make “informed” trades while the noise traders make “uninformed” trades.

There are several conceptual problems with noise trader models that are clear a priori. No one can seriously dispute that traders must have diﬀerent levels of skill, but is the noise trader approach the right way to model this? While it might be ﬁne to model a continuum of skill levels as “low” and “high”, the idea of identifying the “high” level with perfect rationality postulates a level of skill

- at the top end that is diﬃcult to imagine. The panoply of strategies used by real traders is large, and ﬁnancial professionals (and even private investors) are suﬃciently secretive about what they do, that it is diﬃcult to imagine that even the most skilled traders could fully understand everyone else’s behavior.

Another problematic issue is the operational problem of measuring information. For example, under the theory that urgency is a proxy for informativeness, empirical work on the subject has often deﬁned an informed trade as one that is executed by a market order, and deﬁned an uninformed trade as one that is represented by a limit order. This goes against the fact that many of the most successful hedge funds make extensive use of limit orders5. The only alternative is to use data that contains information about the identity of the agents making the trades. Such data does indeed conﬁrm that professionals perform better than amateurs (Barber et al. [2004]), but as mentioned above, there is no demonstration that this means they are rational, and other than stating that professionals make larger proﬁts, it is impossible to determine whether or not professionals are good enough to be considered rational. (On this point, see also Odean [1999]).

### 3.6 A critique of the noise trader explanation of market impact

One of the most important questions to ask about any theory is what it explains that is not explained by a simpler alternative. Noise trader models have been proposed to explain why market impact is a concave function of trading volume. The empirical evidence for this will be discussed in detail in Sections 5 and 6; in any case, it is a well established empirical fact that the market impact as a function of trade size has a decreasing derivative. This can be alternatively stated as saying that the price impact per share decreases with the total size of the trade. The standard explanation for this is that it is due to a mixture of informed and uninformed trading. If more informed traders use small trade sizes and less informed traders use large trade sizes, then small trades will cause larger price movement per share than large trades.

There are several problems with this theory:

5 We are basing this on personal conversations with market practitioners and so can only place a lower bound: We know many people working in many sophisticated trading operations and all of them at least partially use limit orders. We suspect the correct statement is that “most”, or even “nearly all” successful hedge funds use limit orders for at least a substantial part of their trading.

- • A concave market impact function is observed in all markets that have been studied, including many such as the London and Paris markets where the identity of orders is kept completely anonymous. This rules out any explanation that depends on trades made by some agents communicating more information about prices than others, and leaves only the possibility that some traders are able to anticipate short term price movements better than others – see the discussion in Section 3.4.
- • The model is unparsimonious in the sense that it requires the speciﬁcation of a function that states the information that traders have as a function of the size of the trades that they use.
- • The model is diﬃcult to test because it requires ﬁnding a way to specify the information that diﬀerent groups of traders have a priori. One proposal is to do this based of the average proﬁts of diﬀerent groups of traders. This suﬀers from the problem that the time horizon for market impact is typically very diﬀerent than the time horizon on which traders attempt to make proﬁts. A fund manager who intends to a buy a stock and hold it for three years may make the trade to take up that position in a single day. While this manager might have great skill in predicting stock price movements on a three year time horizon she may have no skill at all on a daily horizon. Thus in a large fraction of cases, even under large variations in trader skill, impact may have little correlation with proﬁts.
- • If it is indeed advantageous to use small trades then since this is a trivial strategy, one would think that everyone would quickly adopt it and the eﬀect would disappear. In fact in the last ﬁve years or so there has been a huge increase in algorithmic trading, in which brokers automatically execute large trades for clients by cutting them up into small pieces. One would therefore think that in modern times the concavity should have diminished or even been eliminated entirely. There is little evidence for this - the impact continues to be highly concave.

Thus we have argued above that the theory is implausible, but even more important, that it makes weak and untestable predictions. The prediction of concavity requires a set of assumptions that are complicated to specify and impossible to measure. The predictions are purely qualitative, and it is not obvious how they might be extended to other properties of impact, such as its temporal behavior.

### 3.7 The liquidity paradox – price are not in equilibrium

We will argue here that liquidity is an important intermediary that modulates the eﬀect of information. We are deﬁning liquidity in terms of the size of the price response to a trade of a given size. High liquidity implies a small price response. Since trades carry information, then if the size of trades in response to a given level of information remains constant, as the liquidity varies the price response

to information varies with it.

Under the assumption that trading is an intermediate step in the response of prices to information, one can conceptually decompose it into two terms.

∆p = T (I)/λ, (3.1)

where λ is the liquidity and T (I) is the response of trades to information I. Variations in the liquidity do not tell the full story about the response of prices to information – to do that one would also need to understand T (I). Nonetheless,

- as we argue here, the eﬀects of varying liquidity are substantial, and they have the huge advantage of being easily measurable6. In contrast, since information is diﬃcult to measure, T (I) is diﬃcult to measure. Furthermore, the above equation should be interpreted rather loosely: as we shall see below, impact is in fact neither linear nor permanent.

A very important empirical fact that is crucial to understand how markets operate is that even “highly liquid” markets are in fact not that liquid. Take for example a US large cap stock. Trading is extremely frequent: a few thousand trades per day, adding up to a daily volume of roughly 0.1 – 1% of total market capitalization. Trading is even more frantic on futures and Forex markets. However, the volume of buy or sell limit orders typically available in the order book

- at a given instant of time is quite small: only the order of 1% of the traded daily volume, i.e. 10−4 – 10−5 of the market cap for stocks. Of course, this number has an intraday pattern and ﬂuctuates in time, and it can reach much smaller values in liquidity crises.

The fact that the outstanding liquidity is so small has an immediate consequence: trades must be fragmented. The theoretical motivations for this were originally discussed by Kyle [1985]. It is not uncommon that investment funds want to buy large fractions of a company, often exceeding several percent. One possibility is to arrange upstairs block trades but this lacks transparency and can be costly. If trading occurs through the continuous double auction market, the numbers above suggest that to buy 1% of a company requires at least the order of 100 – 1000 individual trades. This is under the unrealistic assumption that each individual trade completely empties the order book – more realistically each trade consumes only a fraction of the order book, and the number of trades is even larger. But since a thousand trades corresponds to roughly the whole daily liquidity, it is clear that these trades have to be diluted over several days, since otherwise the market would be completely destabilized. Thus an informed trader cannot use her information immediately, and has to trade into the market little by little.

But why is liquidity, as measured by the number of standing limit orders, so low? Both for similar and for opposite reasons. Too large a buy limit order from

6 Of course liquidity may also depend on information, and indeed in Section 6 we will develop this connection.

an “informed” trader would give her away and raise the price of the sellers. Too large a limit order from a liquidity provider would put her at risk of being ‘pickedoﬀ’ by an informed trader. There is a kind of hide and seek liquidity game taking place in organized markets, where buyers and sellers face a paradoxical situation: Both want to have their trading done as quickly as possible, but both try not to show their hands and reveal their intentions. As a result, markets operate in a regime of vanishing revealed liquidity, but large latent liquidity; this leads to a series of empirical regularities that we will present below.

From a conceptual point of view, however, the most important conclusion of this qualitative discussion is that prices are typically not in equilibrium, in the traditional Marshall sense. That is, the true price is very diﬀerent than it would be if it were set so that supply and demand were equal as measured by the honest intent of the participants, as opposed to what they actually expose. As emphasized above, the volume of individual trades is much smaller than the total demand or supply at the origin of the trades. This means that there is no reason to believe that instantaneous prices are equilibrium, eﬃcient prices that reﬂect all known information. Much of the information is necessarily latent, withheld due to the small liquidity of the market, and only slowly revealing itself (see Lyons [2001] for similar ideas). At best, the notion of equilibrium prices can only make sense over a long time scale; high frequency prices are necessarily soiled by a signiﬁcant amount of noise.

### 3.8 Time scales and market ecology

Consider again the case of a typical US large cap stock, say Apple, which (as of Nov. 2007) had a daily turnover of around 8B$. There are on average 6 transactions per second, and on the order of 100 events per second aﬀecting the order book. These are extremely small time scales compared to the typical time for public news events, in which a hot stock like Apple might be mentioned by name every few hours during a period of fast information arrival. Perhaps surprisingly, the number of large jumps in price is much higher. For example, if we deﬁne a jump as a one minute return exceeding three standard deviations, there are the order of ten such jumps per day, reﬂecting the very heavy tailed distribution of high frequency returns (Joulin et al. [2008]). More often than not such jumps occur in the absence of any identiﬁed news. It is obviously a particularly important question to understand the origin and the mechanisms leading to these jumps. The diﬀerence between the frequency of news and the frequency of jumps already suggests that something else must be at work, such as ﬂuctuations in liquidity, that may have little or nothing to do with external news entering the market.

What is the typical time scale of the round trip trades of investors? This depends very much on the style of trading – traditional long-only funds have investment horizons on the scale of years, while more aggressive long-short stat-

arbs have time scales of weeks or days, sometimes even shorter. Some empirical results support the existence of a broad spectrum of investment horizons (see Section 4.3 and 11.1). The optimal frequency of a trading strategy is a trade-oﬀ between the expected proﬁt and the friction and transaction costs. Since the fraction of costs grows with the trading volume large investment funds cannot trade too quickly. This, again, is directly related to the small prevailing liquidity. So it is reasonable to think that information based trading decisions have intrinsic frequencies ranging from a few days to years. As we have already emphasized, for large investors a single decision may generate many more trades: A decision to buy or sell may persist for days to months, generating a series of small trades. Again, the important message is that low frequency, large volume investment decisions imply high frequency, small volume trades, and that high frequency prices cannot be equilibrium prices.

There is however a potentially viable high-frequency strategy called marketmaking that consists in providing instantaneous liquidity to buyers and sellers and trying to eke out a proﬁt from the bid-ask spread. As originally shown by Glosten and Milgrom [1985], the diﬃculty is to avoid losses due to adverse price moves. Since market makers are oﬀering either to buy or to sell, they are giving a free option to others who might have better information. The proﬁtability of market-making strategies depends both on the spread, which is beneﬁcial, and on the long-term impact of trades, which is detrimental. This intuition will be made more precise and discussed in detail in section 7. On some exchanges marketmaking is institutionalized, with certain obligations and advantages bestowed to those who take the burden of providing liquidity. Markets have become, however, more and more electronic, with an open orderbook allowing each investor to behave either as a liquidity provider by posting limit orders, or as a liquidity taker by issuing market orders. Depending on market conditions (for example, the instantaneous value of the spread), investors can choose either type of order. There is both empirical and anecdotal evidence that some players implement high frequency, market-making like strategies. This contribution to order ﬂow is often described as “uninformed”. Although this ﬂow diﬀers from longer horizon trades, which are supposed to be economically informed, these market-making strategies routinely use sophisticated short-term prediction tools and exploit any proﬁtable high-frequency signals. The above simpliﬁed separation of market participants into two broad classes, speculators/liquidity hunters that trade at medium to low frequencies and market-makers/liquidity providers at high frequencies is both realistic and useful to understand the ecology of ﬁnancial markets (Handa and Schwartz [1996], Farmer [2002], Wyart et al. [2006], Lillo et al. [2008b]). The competition between these two categories of traders allows one to make sense of a number of empirical facts, we believe much more usefully than noise trader models. In Section 11 we present some recent empirical results on the characterization of a market ecology.

### 3.9 The volatility puzzle

Given that markets are ecological systems where participants have a broad distribution of time horizons from seconds to years, it is perhaps not surprising to see long-memory eﬀects in ﬁnancial markets, e.g. in trading volume, volatility and order ﬂow. What is a priori surprising, however, is that despite the fact that high frequency prices cannot possibly be in equilibrium because of lack of liquidity, and despite the fact that it should take time for the market to interpret a piece of news and agree on a new price, the average volatility is remarkably constant on a wide range of diﬀerent timescales. As measured by autocorrelation, prices are remarkably eﬃcient down to the fastest timescales. We have argued that news arrival happens on much longer timescales. Given that this is true, how can prices remain so eﬃcient, at least with respect to linear models, even on very fast time scales?

One possible explanation for this is might be that public information as evidenced on news feeds is only a small part of the available information. Instead, suppose there are many sources of private information, which agents are continually processing. As they make their decisions they trade. Given that heavily traded stocks average many trades per second, this would suggest that a truly staggering amount of information is being processed. We ﬁnd this explanation implausible.

The alternative is to that there is an information processing cascade from fundamental information on slow time scales to technical information on fast time scales. As we have argued above, fundamental information enters at a relatively slow rate, and then is processed and incorporated into prices. Under this view high frequency strategies play an important role. Such strategies do not process external information directly, but rather serve the role of digesting that information and keeping the price stream unpredictable. Such strategies are not processing fundamental information, but rather are acting as technical trading strategies, processing information contained in the time history of prices, trading volume and other information that is completely internal to the market. The ability to substitute information in a time history for state information is well supported in dynamical systems theory (Packard et al. [1980], Takens [1981], Casdagli et al. [1991]). Thus we argue that in the ecology of ﬁnancial markets, high frequency strategies are fed by lower frequency strategies through an information cascade from longer to shorter timescales, and from fundamental to technical information, ﬁnally resulting in white noise on all scales.

This also suggests that microstructural eﬀects may inﬂuence the value of the volatility, as suggested by Lyons [2001], e.g. “microstructure implications may be long-lived” and “are relevant to macroeconomics”. We will comment on the relation between microstructure and volatility in Section 8. This relation is also relevant for the regulator, who might attempt to alter the microstructural organisation of markets in order to reduce the volatility.

### 3.10 The Kyle model

A classic model noise trader model for market impact, which is a natural a point of comparison is due to Kyle [1985]. This model assumes that there are three types of traders: Noise traders who make random trades, market makers who set prices in order to guarantee eﬃciency, and an insider who has access to superior information. Under the most general version of the model the noise traders and insider trade continuously from a starting time until a ﬁnal liquidation time, at which point everyone is paid the liquidation price for their holdings. The insider has superior information about the ﬁnal liquidation price p∞, and an inﬁnite bank, which she uses to maximize proﬁts at the expense of the noise traders.

The optimal amount that the investor should trade is easily found to be proportional to the diﬀerence p∞−pt. With the assumption of a linear and permanent impact, in Kyle’s notation the price evolution is given by:

pt+1 − pt = λ[Φt + ξt] + ηt; Φt = β[p∞ − pt] (3.2)

where Φt is the signed demand of the investor, λ, β are coeﬃcients, and ξt is the noise trader demand coming from all other market participants, and ηt a noise term accounting for possible changes of prices not induced by trading (news, etc.). The above equation can easily be solved, and leads to an exponential relaxation of the initial price towards p∞ plus a bounded noise term.

The impact in this model can be regarded as essentially mechanical. There is an apparently permanent change in price which is linearly proportional to the total amount that the noise traders and insider trade. We say “apparently permanent” because, since there is a ﬁnal liquidation time, what happens past this point is undeﬁned. Note that in this model the price will move toward p∞ regardless of whether it is the correct price; all that is necessary is that insider believe it is the correct price. A random assignment of beliefs about p∞ will result in a corresponding random set of impacts. Thus, referring to our discussion of the diﬀerent explanations for market impact in Section 3.4, while the Kyle model is built in the spirit of explanation (1), that trades convey a signal about private information, it is equally consistent with (3), random ﬂuctuations in supply and demand.

The assumption of a ﬁnal liquidation price can naively lead to erroneous conclusions. For example, this model suggests that one can easily manipulate the price. However, in the absence of a liquidation price where a transaction with a counterparty can be realized without impact, things are not so trivial: as soon

- as the investor wants to close his position, he will again mechanically revert the price back to its initial value and take losses. (To see this note that in a single round trip the investor will buy at a high price and sell at the original price). The above impact model, Eq. (3.2), although very often used in agent based models of price ﬂuctuations (two of us have also developed similar ideas, i.e. Bouchaud and Cont [1998], Farmer [2002])), is far too naive to represent the way real markets

operate, at least at the tick by tick level.

Thus we see that while the Kyle model provides a good starting point for understanding why there should be market impact, and why it is useful to trade into a position incrementally, it falls short of making realistic predictions about impact. We feel that the key elements that need to be extended are: (1) Removing the ﬁnal liquidation price, (2) eliminating the inﬁnite bank of the insider and replacing it with the more realistic assumption of a ﬁnite, predetermined trading size, and (3) eliminating the distinction between the insider and the noise trader. The aim of the following sections is to explain in detail how to construct a model generalizing Eq. (3.2), using an approach based on robust facts observed in empirical data and consistency arguments. We will ﬁnd that impact is in general non-linear and transient – or equivalently, as explained in section 6.5, history dependent. It is only after a properly deﬁned “coarse graining” procedure that such an impact model can possibly make sense.

### 4 LARGE FLUCTUATIONS AND LONG-MEMORY OF ORDER FLOW

From a mechanical point of view price formation process is the outcome of (i) the ﬂow of orders arriving in the market and (ii) the response of prices to individual orders. Since price dynamics are reasonably well described by a Brownian motion one might naively assume that this would be true for order ﬂow as well. In fact this is far from the truth. As we will explain in detail in this section, order ﬂow is a highly autocorrelated long-memory process. As a consequence, to maintain market eﬃciency the price response to orders must strongly depend on the past history of order ﬂow. This has profound conseqences for the way in which markets incorporate information.

### 4.1 Empirical evidence for long-memory of order ﬂow

We discuss here the statistical properties of order ﬂow by considering the time series of signs of orders. Speciﬁcally, consider the symbolic time series obtained in event time by replacing buy orders with +1 and sell orders with −1, irrespective of the volume of the order. We reduce these series to ±1 rather than analyzing the signed series of order sizes directly in order to avoid problems created by the large ﬂuctuations in order size7. This reduction can be done for market orders, limit orders, or cancellations, all of which show very similar behavior8. We denote with

- 7 Fluctuations in order size are heavy tailed and have long-memory themselves, so statistical

averages based on them converge only slowly. The essential behavior is captured by the series of signs.

- 8 Long memory is also observed if the signs of all orders, including both limit and market

orders, are taken together. In contrast, if one assigns a cancellation of a buy order a negative sign, corresponding to the fact that the only nonzero price movements it can produce are downward, then the combined sequence of signs for market orders, limit orders, and cancellations does not show long-memory.

[Figure 1]

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

[Figure 13]

[Figure 14]

[Figure 15]

[Figure 16]

[Figure 17]

[Figure 18]

- Figure 1. Autocorrelation function of the time series of signs of orders that result in immediate trades (eﬀective market orders) for the stock Vodafone traded on the London Stock Exchange in the period May 2000 - December 2002, a total of 5.8 × 105 events.

i the sign of the ith market order. Figure 1 shows the sample autocorrelation function of the market order sign time series for Vodafone (VOD) in the period 1999-2002 in double logarithmic scale. The ﬁgure shows that the autocorrelation function for market order signs decays very slowly. The autocorrelation function is still above the statistical noise level even after 104 transactions, which for this stock corresponds to roughly 10 days. This result indicates that if one observes a buy market order now, based on this information alone there is some nonvanishing predictability of the market order signs two weeks from now.

We also note that the autocorrelation function shown in Fig. 1 is roughly linear in a double logarithmic scale over more than 4 decades9. This suggests that a power-law relation Cτ ∼ τ−γ might be a reasonable description for the sample autocorrelation function10.

Stochastic processes for which the autocorrelation function decays asymptotically as a power-law with an exponent smaller than one are called long-memory processes Beran [1994]. A precise deﬁnition of long-memory processes can be given in terms of the autocovariance function Γτ. We deﬁne a process as longmemory if in the limit τ → ∞

Γ(τ) ∼ τ−γL(τ), (4.1)

- 9 The noisy behavior for large τ comes from the fact that for large lags the statistical errors

are remaining roughly constant while the signal decreases, so the relative size of the ﬂuctuations becomes larger.

- 10 f(y) ∼ g(y) means that there exists a constant K = 0 such that limy→∞ f(y)/g(y) = K.

where 0 < γ < 1 and L(τ) is a slowly varying function11 at inﬁnity. The degree of long-memory is given by the exponent γ; the smaller γ, the longer the memory. The integral of the autocovariance (or autocorrelation) function of a long memory process diverges. Long-memory can also be discussed in terms of the Hurst exponent H, which is simply related to γ. For a long-memory process H = 1−γ/2 or γ = 2 − 2H. Short-memory processes have H = 1/2, and the autocorrelation function decays faster than 1/τ. A positively correlated long-memory process is characterized by a Hurst exponent in the interval (0.5,1). The use of the Hurst exponent is motivated by the relationship to diﬀusion properties of the integrated process. For normal diﬀusion, where by deﬁnition the increments do not display long-memory, the standard deviation asymptotically increases as t1/2, whereas for diﬀusion processes with long-memory increments, the standard deviation asymptotically increases as tHL(t), with 1/2 < H < 1, and L(t) a slowvarying function. In econometrics of ﬁnancial time series many variables have the long-memory property. For example, it is widely accepted that the volatility of prices (Ding et al. [1993]) and stock market trading volume (Lobato and Velasco [2000]) are long memory processes. Models of long-memory processes include fractional Brownian noise (Mandelbrot and van Ness [1968]) and the ARFIMA process introduced by Granger and Joyeux [1980] and Hosking [1981].

As Figure 1 suggests, and as discovered by Bouchaud et al. [2004] and Lillo and Farmer [2004], order ﬂow is also described by a long-memory process. The long-memory of order ﬂow is very robust, and is consistently observed for every stock that has so far been examined. Lillo and Farmer tested for long-memory in a panel of 20 highly capitalized stocks traded at the London Stock Exchange using Lo’s modiﬁed R/S test (Lo [1991]), which is known to be a strict test for long memory. They found that even on short samples, in most cases the hypothesis of long-memory could not be rejected. The value of H observed in the London Stock Exchange was generally about H ≈ 0.7, which corresponds to γ = 0.6. Bouchaud et al. (2004) measured a larger interval of γ values in the Paris Stock Exchange, ranging from 0.2 to 0.7. Long-memory has also measured long-memory for an assortment of stocks in the NYSE (these results are mentioned in Lillo and Farmer [2004], but have not been published in detail).

### 4.2 On the origin of long-memory of order ﬂow

What causes long-memory in order ﬂow? The presence of persistent time correlations in the order ﬂow suggests two possible classes of explanations: The ﬁrst type of explanation is that this is a property of the order ﬂow of each investor, independent of the behavior of other investors, as proposed by Lillo et al. [2005].

11L(x) is a slowly varying function (see Embrechts et al., 1997) if limx→∞ L(tx)/L(x) = 1 ∀t. In the deﬁnition above, and for the purposes of this paper, we are considering only positively correlated long-memory processes. Negatively correlated long-memory processes also exist, but the long-memory processes we will consider in the rest of the paper are all positively correlated.

The second type of explanation is that investors herd in their trading though an imitation process that involves an interaction between them, as proposed by LeBaron and Yamamoto [2007]. It is of course possible that both eﬀects operate

- at once, but in any case one would like to know their relative magnitude. We believe that the evidence gathered so far strongly favors the ﬁrst explana-

tion. More explicitly, we believe the dominant cause is the strategic behavior of large investors who split their orders into many small pieces and execute them incrementally. The evidence from this comes from two sources. One is the agreement of the properties of the order ﬂow with theory, and the other is additional evidence based on data that gives information about the identity of participants. We summarize both of these here.

### 4.3 Theory for long-memory in order ﬂow based on strategic order splitting

Lillo et al. [2005] have hypothesized that the cause of the long-memory of order ﬂow is a delay in market clearing. To make this clearer, imagine that a large investor decides to buy ten million shares of a company. It is unrealistic for her to simply state her demand to the world and let the market do its job. There are unlikely to be suﬃcient sellers present, and even if there were, revealing the intention to buy a large quantity of shares will very likely push the price up substantially. Instead the large investor keeps her intentions as secret as possible and trades incrementally over an extended period of time, possibly through intermediaries. As already discussed, the strategic reasons for doing this were made clear by Kyle [1985], who investigated a model in which an insider with information about a ﬁnal liquidation price tries to maximize proﬁts. In simple terms, the motivation is that by splitting the hidden order into small pieces the investor is able to execute much of the hidden order at prices that do not reﬂect the full price movement that it will eventually cause.

Our perspective diﬀers from Kyle’s in that we assume that the size of the order, which we call the hidden order, is given at the outset when the initial trading decision is made. We believe that the size of such orders is largely determined by the fund manager a priori, and is inﬂuenced by a combination of the funds under management and the timescale of the strategy, which is typically much longer than the time scale for completing the trade. The other key diﬀerences is that we do not assume a ﬁnal liquidation price, and we do not make a distinction between informed traders and noise traders. When taken together these diﬀering assumptions create key diﬀerences in the predictions of the model in comparison with Kyle.

In several studies based on data giving the identity of hidden orders, about a third of the dollar value of such institutional trades took more than a week to complete (Chan and Lakonishok [1993, 1995], Vaglica et al. [2008]). This conﬂicts with the standard model of market clearing presented in textbooks, which assumes that agents fully state their supply and demand and that prices

are set so that supply and demand are evenly matched. The fact that large orders are kept secret and executed incrementally implies that at any given time there may be a substantial imbalance of buyers and sellers. Eﬀective market clearing is delayed, by variable amounts that depend on ﬂuctuations in the size and signs of the unrevealed hidden orders.

We now describe a recently proposed simple model of order ﬂow that postulates the independence of trading activity of investors, and which is able to reproduce the long-memory properties of order ﬂow (Lillo et al. [2005]). In the simplest version of the model, assume that at any time there are K hidden orders present in the market. Initially the size V of these hidden orders are drawn from a distribution P(V ) and the sign i is randomly chosen. For simplicity we assume that V is an integer number. We indicate with Vi(t) the volume of hidden order i that has not yet been traded at time t. At each timestep t an existing hidden order i is chosen at random with uniform probability, and a unit volume of that order is traded, so that Vi(t + 1) = Vi(t) − 1. This generates a revealed order of unit volume and sign i. A hidden order i is removed if Vi(t + 1) = 0, i.e. when the hidden order is completely traded. When this happens a new hidden order is created with a random sign and a new size.

It is possible to ﬁnd a closed expression for the autocorrelation function of the trade sign Cτ as a function of the hidden order size distribution P(V ). The asymptotic behavior of Cτ can be obtained through a saddle point approximation. If the hidden order size is asymptotically Pareto distributed, i.e.

α V α+1

P(V ) ∼

, (4.2)

then the autocorrelation function of order sign behaves asymptotically as (Lillo et al. [2005])

Kα−2 α

1

Cτ ∼

τα−1. (4.3) Thus the model makes the falsiﬁable prediction that the exponent γ of the powerlaw asymptotic behavior of the autocorrelation of order sign is determined by the exponent α of the power-law asymptotic behavior of the hidden order size distribution through

α = γ + 1. (4.4) Since we observe that γ 0.5, this model predicts that α = 1.5.

It is worth noting that Lillo et al. [2005] also introduced a more general model where the number of hidden orders is not constant in time. Speciﬁcally, at each time t a new hidden order is generated with probability 0 < λ < 1 if K(t) > 0, or probability one if K(t) = 0. Although this model is not solved analytically, numerical simulation shows that the relation between the exponent of the autocorrelation of order sign and the exponent of order size distribution is the same

- as in the simpler model where the number of hidden orders is ﬁxed.

This model for the origin of correlation in order ﬂow is in principle empirically testable. The main diﬃculty arises from the lack of large and comprehensive databases of the hidden orders of investors. There are two ways to check the consistency of the theory. The ﬁrst one is to compare the distribution of trade sizes in block markets to the autocorrelation function of order signs in order book markets. In block markets trades are made bilaterally and the identity of counterparties is known. Brokers do not like order splitting and strongly discourage it. Thus block markets can be considered a crude proxy for observing the distributional properties of hidden orders12. In the next section we discuss evidence that suggest that block trade volume is indeed asymptotically power law distributed with an exponent α 1.5. For comparison13 the average measured values of γ for LSE stocks is γ = 0.57, close to γˆ = 0.59 as predicted by γˆ = α − 1. The second supporting evidence comes from a study of the Spanish stock exchange by Vaglica et al. [2008] who have inferred hidden orders using data with membership codes. This study will be discussed in Section 11.1.

### 4.4 Evidence based on exchange membership codes

Empirical testing is diﬃcult due to the fact that it is not easy to collect data on the behavior of individual investors. Nonetheless, partial information about the identity of participants can be obtained by making use of data that identiﬁes the broker or the member of the exchange who executes the trade, which we will simply call the membership code. There are many stock markets, such as the LSE, the Spanish Stock Exchange, the Australian Stock Exchange, and the NYSE, where it is possible to obtain data containing this information. It is important to stress that knowing the membership code is not the same as knowing the individual participant, since the member may either trade on its own account or may act

- as a broker for other trades, or may do both at once. Nonetheless, several recent papers have demonstrated that it is possible to extract useful information about the identity of individual traders using such information, e.g. showing that there are consistent behaviors that are persistent in time associated with particular membership codes, that such behaviors can be organized into a taxonomic tree, and that it is possible to detect the presence of large institutional trades (Lillo et al. [2008b], Zovko and Farmer [2007], Vaglica et al. [2008]).

Gerig et al. have used membership codes of the London Stock Exchange to test the hypothesis of the theory presented in Lillo et al. [2005]. The autocorrelation function of market order signs is computed by considering realized orders placed

12 The exception is that it is possible to split an order and trade with multiple brokers. 13 The error bars in computing both γ and α are substantial, as can be seen by computing them for sub-samples of the data, and the close agreement observed by Lillo et al. [2005] between γ and α−1 is probably fortuitious. Unfortunately there are still not good statistical methods for assigning conﬁdence intervals for exponents of power laws, particularly when the observations have long-memory, but the errors can be roughly assessed by examining sub-samples.

|All<br><br>Same Brokerage<br><br>Diff Brokerage<br><br>|
|---|

100

Autocorrelation

10−1

10−2

10−3

100 101 102 103

τ

- Figure 2. Autocorrelation of signs vs. transaction lag for transactions with same membership code, diﬀerent membership code, and all transactions irrespective of membership code, plotted on double logarithmic scale. The investigated stock is AstraZeneca (AZN) traded at LSE in the period 2000-2002.

by the same membership code or by diﬀerent membership codes separately. Figure 2 shows the autocorrelation function of market order signs with the same membership code, diﬀerent membership codes, and all transactions irrespective of membership code. The red circles are the autocorrelation function irrespective of the membership code and, as anticipated above, it well ﬁtted by a power law. When only transactions with the same membership code are considered (green triangles) the autocorrelation is still power law with a slightly smaller exponent. Moreover for a ﬁxed lag τ the autocorrelation function with the same membership code is one order of magnitude larger than the autocorrelation function irrespective of the membership code. Finally, when only transactions with different membership code are considered the autocorrelation function decays very rapidly to zero and it is clearly not consistent with power law behavior. Under the assumption that most investors use only a few brokers to execute a given hidden order, this plot strongly supports the hypothesis that the long memory of signs is due to the presence of investors that place many revealed orders of the same sign and that there is no clear sign of herding behavior among diﬀerent investors. It is in principle possible that herding happens between investors using the same broker, but not between investors with diﬀerent brokers; however the reasons why this would occur are unclear and it seems implausible that it could explain such a dramatic diﬀerence.

### 4.5 Evidence for heavy tails in volume

The theory developed above makes it clear that the distribution of trading volume play a key role in shaping many properties of the market, including the longmemory of order ﬂow, which we will show in turn has important consequences for market impact. In recent years there has been a debate about the statistical properties of trading volume. This is partly due to the fact that markets have diﬀerent structures and one should be careful in specifying which volume is considered in the analysis. Gopikrishnan et al. [2000] originally observed that volume of trades

- at the NYSE are asymptotically power law distributed. Speciﬁcally, they claimed that for large volumes the probability distribution scales as

P(V > x) ∼ x−3/2. (4.5)

This law has been termed the “half cubic” law. The NYSE, as many other ﬁnancial markets, employs two parallel markets which provide alternative methods of trading, called the on-book or ”downstairs” market, and the oﬀ-book or ”upstairs” market. Orders in the on-book market are placed publicly but anonymously and execution is completely automated. The oﬀ-book market, in contrast, operates through a bilateral exchange mechanism, via telephone calls or direct contact of the trading parties. The anonymous nature of the on-book market facilitates order splitting, i.e. large orders are split in smaller pieces and traded incrementally. On the other hand the oﬀ-book market is a block market, where large orders can be traded in a single transaction. The NYSE data used by Gopikrishnan et al. [2000] includes a mixture of order book trades and block trades. Since the typical size of block trades is much larger than the size of orders traded in the order book, the size of block trades dominates the tail of volume distribution.

This can be seen more clearly in a market (or database) where it is possible to separate block trades from order book trades. In ﬁgure 3 (from Lillo et al.

- [2005]) we show the cumulative distribution function of trading volume of oﬀbook trades, on-book trades, and the aggregate of both for a collection of 20 LSE stocks. The distribution of block trades is consistent with the power-law hypothesis of Eq. 4.5 with an exponent close to 1.5, whereas the distribution of order book trades is not consistent with the half-cubic law, and instead has a much thinner tail (see also Farmer and Lillo [2004] and Plerou et al. [2004]).

### 5 SUMMARY OF EMPIRICAL RESULTS FOR DIVERSE TYPES OF MARKET IMPACT

The relation between the transacted volume and the consequent expected price shift is called the price impact or alternatively the market impact function. Letting R be a price return associated with a trade of size V , the market impact a time l after the trade occurred is

I(V,l) = E[R|V,l].

[Figure 19]

[Figure 20]

[Figure 21]

[Figure 22]

|[Figure 23]<br><br>[Figure 24]<br><br>[Figure 25]<br><br>|
|---|

[Figure 26]

[Figure 27]

[Figure 28]

[Figure 29]

[Figure 30]

[Figure 31]

[Figure 32]

[Figure 33]

[Figure 34]

[Figure 35]

[Figure 36]

[Figure 37]

[Figure 38]

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

[Figure 53]

[Figure 54]

[Figure 55]

[Figure 56]

[Figure 57]

[Figure 58]

[Figure 59]

[Figure 60]

[Figure 61]

[Figure 62]

[Figure 63]

[Figure 64]

[Figure 65]

[Figure 66]

[Figure 67]

[Figure 68]

[Figure 69]

[Figure 70]

[Figure 71]

[Figure 72]

[Figure 73]

[Figure 74]

[Figure 75]

[Figure 76]

[Figure 77]

[Figure 78]

[Figure 79]

[Figure 80]

[Figure 81]

[Figure 82]

[Figure 83]

[Figure 84]

[Figure 85]

[Figure 86]

[Figure 87]

[Figure 88]

[Figure 89]

[Figure 90]

[Figure 91]

[Figure 92]

[Figure 93]

[Figure 94]

[Figure 95]

- Figure 3. Volume distributions of oﬀ-book trades (circles), on-book trades (diamonds), and the aggregate of both (squares). We show this for a collection of 20 diﬀerent stocks, normalizing the volume of each by the mean volume before combining. The dashed black lines have the slope found by the Hill estimator and are shown for the largest one percent of the data. Adapted from Lillo et al. [2005].

For many purposes it is useful to separate the dependence on volume from the dependence on time. One can make the hypothesis that the impact function can be written as a product of two functions, i.e.

I(V,t) = S(V )R(l)

In this section we will primarily discuss the dependence on volume, saving the discussion of time dependence for Section 6.

We are intentionally being vague at this stage about the deﬁnition of the return R and the volume V ; deﬁning these more precisely is one of the main points of this chapter. The way in which the market impact behaves depends on the market structure as well as on what one means by “return” and “volume”. Many studies have empirically investigated market impact with a range of diﬀerent results; we will argue that in many cases these diﬀerences stem from diﬀerences in what is being studied. The important distinctions that should be made are:

- • First of all, one can consider market impact of an individual transaction vs. an aggregate of many transactions. Aggregation here means that the market impact is conditioned on a given number of trades or to a given interval of time. We will discuss the volume dependence of individual impact in Section 5.1 and the time dependence in Sections 6.2 - 6.5, and we will study the properties of aggregate impact in Sections 5.2 and 6.8.

- • A second important aspect is the type of market exchange where the transactions take place. As we have said above, most ﬁnancial markets have upstairs or block markets as well as downstairs or orderbook markets. In the downstairs market trades are made by placing orders in a limit order book, and it is quite common to aggressively split large trading orders into many small pieces. The upstairs market trades are arranged bilaterally between individuals. As a result of the diﬀerent market structures the impacts can be quite diﬀerent.
- • A third factor that must be kept in mind is that large trading orders, which we will call hidden orders, are typically split into small pieces and executed incrementally. This is in contrast to realized orders, which are the actual orders that are traded, e.g. the pieces into which hidden orders are split. For realized orders the impacts may be part of a larger process of order splitting that is invisible with the data that we have here. The impacts of hidden orders may be quite diﬀerent than those of realized orders. The impacts of individual orders behave much like those of individual transactions, see the next bullet. We will discuss the impact of hidden orders in Section 6.7.
- • Finally, even if we have discussed market impact in terms of transacted volume, other events in the market have an impact on price. Speciﬁcally, in double auction market limit orders and cancellations can have a market impact that is diﬀerent from the impact of a market order.

In the following we will discuss the empirical regularities in these diﬀerent types of market impact.

### 5.1 Impact of individual transactions

We now discuss the impact of individual transactions in limit order book markets, whose volume we will denote by v Many studies have examined the market impact for a single transaction, and all have observed a concave function of the transaction volume v, i.e. one that increases rapidly for small v and more slowly for larger v. The detailed functional form, however, varies from market to market and even period to period. Early studies by Hasbrouck (Hasbrouck91) and Hausman, Lo and MacKinlay (Hausman92) found strongly concave functions, but did not attempt to ﬁt functional forms. Keim and Madhavan [1996] also observed a concave impact function for block trades. Based on Trades and Quotes (TAQ) data for a set of 1000 NYSE stocks the concavity of the market impact was interpreted by Lillo et al. [2003b] using the functional form

 vψ λ

E[r|v] =

(5.1)

The exponent ψ(v) is approximately 0.5 for small volumes and 0.2 for large volumes. Even normalizing the volume v by daily volume, the liquidity parameter λ varies for diﬀerent stocks; there is a clear dependence on market capitalization M that is well-approximated by the functional form λ ∼ Mδ, with δ ≈ 0.4.

[Figure 96]

[Figure 97]

| | | |
|---|---|---|
| | | |

| | | |
|---|---|---|
| | | |
| | | |

| | |
|---|---|
| | |

| | |
|---|---|
| | |

| | |
|---|---|
| | |
| | |

| | |
|---|---|
| | |
| | |
| | |

[Figure 98]

[Figure 99]

[Figure 100]

[Figure 101]

[Figure 102]

[Figure 103]

[Figure 104]

[Figure 105]

[Figure 106]

[Figure 107]

[Figure 108]

[Figure 109]

[Figure 110]

[Figure 111]

- Figure 4. Market impact function of buy market orders for a set of 5 highly capitalized stocks traded in the LSE, speciﬁcally AZN (ﬁlled squares), DGE (empty squares), LLOY (triangles), SHEL (ﬁlled circles), and VOD (empty circles). Trades of diﬀerent sizes are binned together, and the average size of the logarithmic price change for each bin is shown on the vertical axis. The dashed line is the best ﬁt of the market impact of VOD with a functional form described in Eq.5.1. The value of the ﬁtted exponent for VOD is ψ = 0.3.

Potters and Bouchaud (2003) analyzed stocks traded at the Paris Bourse and NASDAQ and found that a logarithmic form gave the best ﬁt to the data. For the London Stock Exchange, Farmer and Lillo [2004] and Farmer et al. [2005] found that for most stocks Eq. ( 5.1) was a good approximation with ψ = 0.3, independent of V . Hopman [2006] studied market impact on a thirty minute timescale in the Paris bourse for individual orders and found ψ ≈ 0.4, depending on the urgency of the order. Thus all the studies ﬁnd strongly concave functions, but report variations in functional form that depend on the market and possibly other factors as well. Figure 4 shows the price impact of buy market orders for

- 5 highly capitalized LSE stocks, i.e. AZN, DGE, LLOY, SHEL, and VOD. The price impact is well ﬁt by the relation E[r|v] ∝ v0.3.

### 5.2 Impact of aggregate transactions

Studies of aggregated market impact have produced variable results, reaching diﬀerent conclusions that we will argue depend substantially on the time scale for aggregation. The BARRA market impact model, an industry standard, uses the TAQ data aggregated on a half hour time scale (Torre [1997]). They compare ﬁts using Equation 5.1 and ﬁnd ψ ≈ 0.5; they obtain similar results using individual block data. Kempf and Korn [1999] studied data for futures on the DAX (the German stock index) on an ﬁve minute time scale and found a very concave

x 10−10

x 10−3

6

2

|N=1 N=8 N=64<br><br>N=512<br><br>|
|---|

|N=1 N=8 N=64<br><br>|
|---|

4

0

−2

2

−4

*R/VN

0

R

−6

−2

−8

−4

−10

−6

−0.5 −0.4 −0.3 −0.2 −0.1 0 0.1 0.2 0.3 0.4 0.5

−12

−6 −4 −2 0 2 4 6 x 106

V/V*N

V

- Figure 5. Aggregate market impact R(Q,N) for the LSE stock Astrazeneca for 2000-2002. In (a) we plot the shifted aggregate return R(Q,N) + R0 vs. the aggregate signed volume Q for three values of N. The arbitrary constant R0 is added to aid visualization; its values are R0 = {0,−3 × 10−3,−6 × 10−3} for N = 1,8 and 64 respectively. In (b) for each N we rescale both the horizontal and vertical axes by Q∗N = Q(95)N − Q(5)N , where Q(5)N is the

- 5% quantile and Q(95)N is the 95% quantile of Q.

#### functional form. Plerou et al. [2002] studied data from the NYSE during 1994-95 ranging from 5 to 195 minute time scales and ﬁt the market impact function with a hyperbolic tangent. They noted that at shorter time scales this functional form did not work well for small v; tanh(v) is linear for small v, but at short time scales (e.g. 5 or 15 minutes) they observed a nonlinear impact function, becoming more linear as they went toward longer time scales. Evans and Lyons [2002] studied foreign exchange rate transactions data for DM and Yen against the dollar at the daily scale over a four month period. They used the number of buyer initiated transactions minus the number of seller initiated transactions as a proxy for the signed order ﬂow volume v, and found a strong positive relationship to concurrent returns. Chordia and Subrahmanyam [2004] study impact for stocks in the S&P 500 at a daily time scale and perform linear regressions, but do not compare to other functional forms. For the Paris bourse Hopman [2006] measures aggregate order ﬂow as i iviψ, where the sum is taken over ﬁxed time intervals. At a daily scale he ﬁnds he gets the best linear regression against contemporary daily returns with ψ ≈ 0.5. He also documents that the slope of the regression decreases with increasing time scale. Finally, as discussed in more detail below, Gabaix et al. [2003, 2006] have made extensive studies of data from the New York, London and Paris stock markets on a ﬁfteen minute time scale, and ﬁnd exponents ψ ≈ 0.5.

#### What is the origin of these diﬀerences in the observed functional form of the aggregate market impact? Part of the diﬀerence comes certainly from the fact that these studies consider diﬀerent markets, diﬀerent assets, and diﬀerent time periods. However another important diﬀerence across studies is the time scale

of aggregation. There is no reason why the aggregate market impact over a 10 minute time interval should have the same functional form of that over a one hour time interval or over an interval that is deﬁned by 30 trades.

To have an idea of how the market impact changes its shape with aggregation scale consider a speciﬁc example. Let vt be the volume of transaction happening

- at time t (in event time). Let rt = log(pt+1/pt) be the corresponding log-return, where pt is the price of transaction t. For a sequence of N successive transactions

beginning at time t, let QN = Ni=1 t+ivt+i be the aggregate volume and RN =

N

i=1 rt+i be the aggregate return. The average market impact conditioned on volume is

R(Q,N) = E[RN|QN = Q], (5.2) i.e. it is the expected return associated with a signed volume ﬂuctuation Q. We write R(Q,N) to emphasize that this can depend both on the signed trading volume imbalance V and the number of transactions N. In Figure 5 we show empirical estimates for the market impact for the stock AZN, which is traded on the London Stock Exchange, from Lillo et al. [2008a]. In Figure 5 we show the market impact for diﬀerent values of N with oﬀsets added to the vertical axis to aid visualization. As one would expect, the scale increases with N. The shape of R(Q,N) also changes, becoming more linear with increasing N. This is illustrated more clearly in Figure 5(b), where we rescale the horizontal and vertical axes using a rescaling factor based only on QN. The renormalization makes the increasing linearity clearer. As N increases the market impact near Q = 0 becomes linear, and the size of the region that can be approximated as linear grows with increasing N. It also illustrates a surprising feature: The slope of the linear region decreases with N. These same basic features (increasing linearity and decreasing slopes) hold for all the stocks in our sample, in both the New York and London Stock Exchanges. This result shows that the shape and the scale of the aggregate market impact change with the aggregation scale. At short time scales the function is signiﬁcantly nonlinear, but at large aggregation scales the market impact becomes close to linear, and the slope of the impact decays with the aggregation scale. For this reason it is in general misleading to compare aggregate impact curves with diﬀerent scales, unless one has a theory for how the market impact depends on aggregation scale. This also shows why the studies mentioned above found diﬀerent forms of the market impact. In Section 6.8 we present some models that help to explain the behavior of aggregate impact observed in real data.

### 5.3 Hidden order impact

Because data for hidden orders, which are sometimes also called trading packages, are diﬃcult to obtain, there are only a few studies (Chan and Lakonishok [1993, 1995], Almgren et al. [2005], Vaglica et al. [2008]). These studies show that hidden orders can be extremely long, involving thousands of realized trades spread over

periods of many weeks or even months. As reviewed in Section 11.1, the most recent study by Vaglica et al. conﬁrms that hidden orders obey a power law distribution of size, which as we argue in Section 6 plays an important role in determining their impact.

The theoretical considerations for treating hidden orders are quite diﬀerent than those for individual orders, and they also very diﬀerent from those of aggregated anonymous orders. The reason is because such orders come from the same agent, creating bursts of orders in the order ﬂow which are all of the same sign. As we argued in Section 4.3, this generates strong correlations in order ﬂow that have to be compensated for, as discussed in Section 6. The volume dependence of hidden order impact is intimately connected to the temporal aspects, and so we save the development of the theory for hidden order impact for the next section.

### 5.4 Upstairs market impact

Market impact in the upstairs market has been studied by Keim and Madhavan [1996]. As in other cases they ﬁnd empirically that market impact is concave. They explain this based on a model for the diﬃculty of ﬁnding counterparties for trading. Ultimately, as pointed out by Gabaix et al. [2006], upstairs market impact should match hidden order impact, for the simple reason that the upstairs market is competing with the downstairs market, and if costs in the upstairs market are too high they have the option of splitting their trades up in the downstairs market. This is convenient because it implies that a theory for either market automatically gives a theory for the other.

### 6 THEORY OF MARKET IMPACT

In this section we develop theoretical explanations for both the volume dependence and the temporal dependence of market impact. As stressed in the previous section, there are several distinct types of impact that require a diﬀerent approach to their analysis. We begin in Section 6.1 by explaining why the impacts associated with individual trades are so concave, arguing that the dominant cause is selective liquidity taking. Then in Sections 6.2 - 6.5 we develop a theoretical approach to understanding the temporal behavior of impacts associated with individual trades. We show that the long-memory of order ﬂow and market eﬃciency play a crucial role, which one can take into account one of two ways. One can either assume a ﬁxed impact, in which case the future contribution to the impact of each trade must decay to zero with time, or one can assume a varying but permanent impact, which implies asymmetry liquidity. We show that these two approaches are equivalent. In Section 6.6 we present empirical results supporting these ideas. In Section 6.7 we develop a theory for the impact of hidden orders, i.e. linked sets of trades made by large investors. Finally in Section 6.8 we develop a theory for the aggregate impact of successive trades and show that it does a good job of explaining the empirical results of Section 5.2.

x 10−4

|True Impact<br><br>Virtual Impact<br><br>|
|---|

6

4

2

R

0

−2

−4

−6

−4 −3 −2 −1 0 1 2 3 4 x 105

V

- Figure 6. Comparison of virtual to true market impact. True impact is shown in blue circles, virtual impact in red triangles. The ﬁtted curve for true impact (solid black) is of the form f(v) = Avψ, with ψ = 0.3.

### 6.1 Why is individual transaction impact concave?

Let us consider ﬁrst the impact of individual transactions. Several diﬀerent theories have been put forth to explain why market impact for single transactions is concave. These can be grouped into three classes: (1) Size dependent informativeness of trades (e.g. due to stealth trading, as postulated by (Barclay and Warner [1993])), (2) average depth vs. price in the limit order book (Daniels et al. [2003]) and (3) selective liquidity taking (Farmer et al. [2004]).

The standard reason given for the concavity of market impact is that it reﬂects the informativeness of trades. If small trades carry almost as much information as large trades, then the price changes caused by small trades should be nearly as big as those for large trades. For example, this could be due to “stealth trading”, i.e. because informed traders keep their orders small to avoid revealing their superior knowledge (Barclay and Warner [1993]). Hypothesis (2), due to Daniels

- et al. [2003]), is that it reﬂects the accumulation of liquidity in the limit order book. I.e., the depth in the order book as a function of the price will determine the market impact for a market order as a function of its size. Hypothesis (3) is that this is due to selective liquidity taking, i.e. that liquidity takers submit large orders when liquidity is high and small orders when it is low (see Farmer
- et al. [2004]), Weber and Rosenow [2006], and Hopman [2006]). Theory (2) is easily ruled out by computing the average virtual market impact

- as a function of volume. This is deﬁned as the average price change that would instantaneously occur for an eﬀective market order of size v (Weber and Rosenow

- [2006]), Farmer and Zamani [2007]). In Figure 6 we show the virtual impact for

AZN, computed by hypothetically submitting orders for a range of diﬀerent values of v and measuring the immediate price response. This is done for each time when real eﬀective market orders were submitted. The resulting price response is a direct probe of the depth of the limit order book. The fact that the mechanical impact is linear to very good degree of approximation makes it clear that this is not the cause of the concavity of the real market impact function.

The selective liquidity taking (hypothesis (3)) means that agents condition the size of their transactions on liquidity, making large transactions when liquidity is high and small transactions when it is low. As shown by Farmer et al. [2004], for LSE stocks it is rare that a trade penetrates more than one price level14. For example, for Astrazeneca approximately 87% of the market orders creating an immediate price change have a volume equal to the volume at the opposite best. Moreover, approximately 97% of the market orders creating an immediate price change have a volume that is either equal to the opposite best or larger than this value but smaller than the sum of volume at the second best opposite price. This means that to a good approximation the market impact can be written in the very simple form

E[r|v] = P(+|v)E[r], (6.1) where P(+|v) is the probability that a trade of size v generates a nonzero return, i.e. the probability that v ≥ Φb, where Φb is the volume oﬀered or bid at the opposite best price. E[r] is the expected return given that there is a nonzero return, which is of the order of the bid-ask spread (see Section 7 for more precise statements). This demonstrates that trading orders that penetrate the opposite best are rare. This is because agents do not like to suﬀer price degradation more than the opposite best, and so condition the size of their orders on what is being oﬀered there.

We have now to explain why P(+|v) is a concave function. An explanation in terms of selective liquidity taking is the following. Suppose that the volume

- at the best is drawn from a distribution Pb(Φb) and suppose that the liquidity taker draws the volume v she would like to trade from another distribution and independently from Φb. If v < Φb she places a market order of size v, whereas if v > Φb she places a market order of size Φb. What is the probability P(+|v)

under this simple model? A straightforward calculation shows that P(+|v) =

v

0 Pb(Φb)dΦb, i.e. it is equal to the cumulative distribution of the volume at the best. This is an increasing and concave function of v that could be used to ﬁt the empirical P(+|v). Under this model the shape of the market impact is explained by P(+|v), i.e. by the conditioning of trading orders on the liquidity that is oﬀered. In other words, theory (3) does a good job of explaining, at least qualitatively, the data.

It is a matter of interpretation, however, whether this is also consistent with theory (1), i.e. that smaller trades are proportionately more informative than

14See Table 2 of Farmer et al.

larger trades. From one point of view, one can simply say that the market impact deﬁnes the informativeness of trades. If so, then it is obviously consistent. However, if it means that price changes are a response to the new information contained in trades, then the evidence presented above is inconsistent with theory (1). In the LSE the quoted volume is visible to all, and so except for occasional latency problems, in which the quote changes just before a trade is placed, the trader is aware of the quote when she places the trade. The fact that the size of the trade is strongly correlated with the size of the best quote implies that the size of the trade carries little new information. This does not mean that the trade is based on inferior information – it just means that other market participants do not learn much from its size when it occurs. It is the conditioning of trade size on best quotes that drives concavity, and not because the smaller trades are nearly as “informed” as the larger trades.

### 6.2 A ﬁxed permanent impact model

In the previous section we described how midquote prices react on average to market orders of a given volume v. The above discussion was restricted to the immediate impact, i.e. the impact that is felt immediately after a trade is completed. In general this can have both temporary and permanent components. In this section we will discuss the impact of individual transactions, i.e. the average midquote price change between just before the nth trade and just before the n + 1th trade. It is an empirical fact that this immediate impact, deﬁned as E[rn| nvn], is non zero and can be written as E[r| v] =  f(v), where f is a function that grows with v. Clearly, it is important to understand if and how this immediate impact evolves with time (which we will measure in terms of the sequence number of the trades). Is the impact of a trade permanent or transient? Is it ﬁxed or is it variable? How does it depend on the past order ﬂow history?

The simplest situation is that of a usual random walker, where position at any time is the sum over all past steps – however far in the past they might be. In ﬁnancial language, this corresponds to the case where the impact of a transaction is permanent, which translates into the following equation for the midquote price mn at time n:

rn = mn+1 − mn = nf(vn;Ωn) + ηn, (6.2) where ηn is an additional random term describing price changes not directly attributed to trading itself, for example the impact of news where quotes could instantaneously jump without any trade. We will assume here that ηn is independent on the order ﬂow and we set E[η] = 0 and E[η2] = Σ2. We have included a possible dependence of the impact on the instantaneous state Ωn of the order book. We expect such a dependence on general grounds: a market order of volume vn, hitting a large queue of limit orders, will in general impact the price very little. On the other hand, one expects a very strong correlation between the state

of the book Ωn and the the size of the incoming market order: large limit order volumes attract larger market orders.

The above equation can be written as: mn =

kf(vk;Ωk) +

ηk, (6.3)

k<n

k<n

which makes explicit the non-decaying nature of the impact in this model: k∂mn/∂vk (for k < n) does not decay as n−k grows. This simple model makes the following predictions for the lagged impact function R and the lagged return variance V :

R ≡ E[ n·(mn+ −mn)] = E[f]; V ≡ E[(mn+ −mn)2] = E[f2] + Σ2  , (6.4)

i.e. constant price impact and pure price diﬀusion, close to what is indeed observed empirically on small tick, liquid contracts. However if we consider the autocovariance of price returns we ﬁnd that

E[rnrn+τ] ∝ E[ n n+τ] ∼ τ−γ (6.5)

which means that price returns are strongly autocorrelated in time. This fact would violate market eﬃciency because price returns would be easily predictable even with linear methods. We therefore come to the conclusion that the empirically observed long memory of order ﬂow is incompatible with the random walk model above if prices are eﬃcient (Bouchaud et al. [2004], Lillo and Farmer [2004], Challet [2007]). In other words one of the assumptions of the random walk model above must be relaxed. Among the various possibilities we will relax either the assumption that price impact is permanent or the assumption that price impact is independent of the order ﬂow. As we will see these two possibilities are related one to each other, but for the sake of clarity we will present them in two diﬀerent subsections.

### 6.3 The MRR model

In order to illustrate the above concepts, let us discuss a slight variant of a model due to Madhavan, Richardson and Roomans (Madhavan et al. [1997]), which helps deﬁne various quantities and hone in on relevant questions. The assumptions of the model are (i) that all trades have the same volume vn = v and (ii) the n’s are generated by a Markov process with correlation ρ, which means that the expected value of n conditioned on the past only depends on

n−1 and is given by:

E [ n| n−1] = ρ n−1, (6.6) The case ρ = 0 corresponds to independent trade signs, whereas ρ > 0 describes positive autocorrelations of trade signs. Note that in this model, correlations decay exponentially fast, i.e.

C = E[ i i+ ] = ρ . (6.7)

which, as we discussed in Section 4, does not conform to reality.

The mrr model postulates that the mid-point mn evolves only because of unpredictable external shocks (or news) and because of the surprise component in the order ﬂow. This postulate of course automatically removes any predictability in the price returns and ensures eﬃciency. Under the assumption that the surprise component of the order ﬂow at the nth trade is given by n − ρ n−1, one writes the following evolution equation for the price15.

mn+1 − mn = ηn + θ[ n − ρ n−1], (6.8)

where η is the shock component, and the constant θ measures the size of trade impact.

These equations make it possible to compute several important quantities such as the lagged impact function deﬁned above (Eq. (6.4)). One may write:

n+ −1

mn+ − mn =

j=n

n+ −1

[ j − ρ j−1], (6.9)

ηj + θ

j=n

The full impact function is found to be constant, equal to: R = θ(1 − ρ2), ∀ (6.10)

We can also deﬁne the ‘bare’ impact of a single trade G0( ), which measures the inﬂuence of a single trade at time n− on the the mid-point at time n. In terms of G0( ), the mid-point is therefore written as:

n−1

n−1

G0(n − j − 1) j, (6.11)

mn =

ηj +

j=−∞

j=−∞

is here found to given by G0( = 0) = θ and G0( ≥ 1) = θ(1 − ρ): a part θρ of the impact instantaneously decays to zero after the ﬁrst trade, whereas the rest of the impact is permanent. The instantaneous drop of part of the impact compensates the sign correlation of the trades. Finally, the volatility, within this simpliﬁed version of the mrr model, reads:

V = θ2(1 − ρ2) . (6.12)

### 6.4 A transient impact framework

Compared to the above simplifying assumptions of the MRR model, the data shows that (i) the volumes v of the incoming market orders are very broadly distributed, with a power-law tail (see section 4.5); (ii) the sign time series n

15 The assumption that prices respond linearly to the order ﬂow is a very strong assumption.

has long range correlations C that decays again as a power-law ∼ c0 −γ with γ < 1, deﬁning a long memory process. The smallness of γ makes the correlation function C non-summable: the average relaxation time is inﬁnite, whereas the correlation time of the Markovian sign process in the above mrr model is ﬁnite, equal to (1 − ρ)−1.

In this section we relax the assumption that impact of a single trade is permanent in time. Rather, we ﬁnd that long range correlations in trades imply that the impact itself has to decay slowly with time. In the next section, we will discuss an alternative but equivalent model, where the impact is permanent but asymmetric and history dependent.

- 6.4.1 Transient impact and mean reversion What would happen if the impact of each trade was purely transient, for example an exponential decay in time? Eq. (6.2) would now read:

mn =

k<n

αn−k−1 kf(vk;Ωk) +

k<n

ηk, (0 ≤ α < 1). (6.13)

The lagged impact and the return variance would then be given by:

R = α −1E[f]; V = 2E[f2]

1 − α 1 − α2

+ Σ2 , (6.14)

i.e. a short-time volatility ≈ E[f2] + Σ2 larger than its long-time value Σ2, in which only the ‘news’ component survives. The price would exhibit signiﬁcant high frequency mean reversion: impact kicks it temporarily up and down, but the long term wandering of the price is unrelated to trading. Of course, one could be in a mixed situation where the impact decays exponentially but towards a positive value, in which case the long term volatility still involves an impact component. This conforms with conventional wisdom about eﬃcient markets: an increased value of high frequency volatility driven by the “tatonnement” process, and a long term volatility made up both of unexpected news and long-term impact of market orders, which translates private information into prices. However, recall that this does not conform to observations, which show volatility very nearly constant across all time scales (see Section 3.9).

What is the relation between the average R and the impact of a single trade, that we call G0( ) henceforth? If trades were uncorrelated, the two quantities would be identical, but trade correlations, as we shall see below, change the picture in a rather interesting way.

- 6.4.2 Mathematical theory of long term resilience The long term memory of trades is a priori paradoxical and hints towards a non trivial property of ﬁnancial markets, which can be called long-term resilience. Take again Eq. (6.11) with the assumption that single trade impact is lag independent: G0( ) = G0 and that volume ﬂuctuations can still be neglected. The

mid-price variance is easily computed to be:

V ≡ (mn+ − mn)2 = [Σ2 + G20] + 2G0

( − j)Cj. (6.15)

j=1

When γ < 1, the second term of the rhs can be approximated, when 1, by 2c0G0 2−γ/(1 − γ)(2 − γ), which grows faster than the ﬁrst term. In other words, the price would super-diﬀuse, or trend, at long times, with a volatility diverging with the lag . This of course does not occur: The market reacts to trade correlations so as to prevent the occurence of such trends. In fact, within the present linear model, the impact to single trades must be transient, rather than permanent. Before explaining why and how this occurs in practice, let us ﬁrst express mathematically how the eﬃciency of prices imposes strong constraints on the shape of the single trade impact function. For an arbitrary function G0( ), the lagged price variance can be computed explicitly and reads:

G20( − j) +

V =

0≤j< 

[G0( + j) − G0(j)]2 + 2∆( ) + Σ2 , (6.16)

j>0

where ∆( ) is the correlation induced contribution: ∆( ) =

G0( − j)G0( − k)Ck−j

0≤j<k< 

[G0( + j) − G0(j)][G0( + k) − G0(k)]Ck−j

+

0<j<k

G0( − j)[G0( + k) − G0(k)]Ck+j. (6.17)

+

0≤j<  k>0

Assume that G0( ) itself decays at large as a power-law, Γ0 −β. When β,γ < 1, the asymptotic analysis of ∆( ) yields:

∆( ) ≈ Γ20c0I(γ,β) 2−2β−γ, (6.18)

where I > 0 is a certain numerical integral. If the single trade impact does not decay (β = 0), we recover the above superdiﬀusive result. But as the impact decays faster, superdiﬀusion is reduced, until β = βc = (1 − γ)/2, for which ∆( ) grows exactly linearly with and contributes to the long term value of the volatility. However, as soon as β exceeds βc, ∆( ) grows sublinearly with , and impact only enhances the high frequency value of the volatility compared to its long term value Σ2, dominated by ‘news’. We therefore reach the conclusion that the long range correlation in order ﬂow does not induce long term correlations nor anticorrelations in the price returns if and only if the impact of single trades is transient (β > 0) but itself non-summable (β < 1). This is a rather odd situation

where the impact is not permanent (since the long time limit of G0 is zero) but is not transient either, because the decay is extremely slow. The convolution of this semi-permanent impact with the slow decay of trade correlations gives only a ﬁnite contribution to the long term volatility. The mathematical constraint β = βc will be given more ﬁnancial ﬂesh below.

Within the above framework, one can also compute the average impact function R . From Eq. (6.4) one readily obtains:

R = G0( ) +

G0( − j)Cj +

0<j< 

[G0( + j) − G0(j)]Cj. (6.19)

j>0

This equation can be understood as a way to extract the impact of single trades G0 from directly measurable quantities, such as R and Cn – see section 6.6 and Appendix 2. From a mathematical point of view, the asymptotic analysis can again be done when G0( ) decays as Γ0 −β. When β + γ < 1, one ﬁnds:

Γ(1 − γ) Γ(β)Γ(2 − β − γ)

π sinπ(1 − β − γ)

π sinπβ −

1−β−γ, (6.20)

R ≈ 1 Γ0c0

where we have explicitly given the numerical prefactor to show that it exactly vanishes when β = βc, which means that in this particular case one cannot satisfy oneself with the leading term. When β < βc, one ﬁnds that R diverges to +∞ for large , whereas for β > βc, R diverges to −∞, which is perhaps counter-intuitive, but means that when the decay of single trade impact is too fast, the accumulation of mean reverting eﬀects leads to a negative long term average impact – see Fig. (7). When β is precisely equal to βc, R tends to a ﬁnite positive value R∞: the decay of single trade impact precisely oﬀsets the positive correlation of the trades.

In the above framework, volume ﬂuctuations have been neglected. An extended version of the model, which is directly related to the discussion of the next section, is presented in Appendix 2 (see also Bouchaud et al. [2004]).

### 6.5 History dependent, permanent impact

- 6.5.1 Predictable order ﬂow and statistical eﬃciency An alternative interpretation of the above formalism is to assume that price impact is permanent, but history dependent as to ensure statistical eﬃciency of prices (Lillo and Farmer [2004], Farmer et al. [2006], Gerig [2007]). Let us consider a generalized MRR model:

rn = mn+1 − mn = ηn + θ( n − ˆ n), ˆ n = En[ n+1|I] (6.21)

where I is the information set available at time n. In line with our discussion in Section 3.8, we assume that in the market there are three types of traders. First of all there are directional traders (liquidity takers) which have large hidden

[Figure 112]

THEORY OF MARKET IMPACT 46

- Figure 7. Theoretical impact function R , from Eq. (6.19), and for values of β close to βc. When β = βc, R tends to a constant value as becomes large. When β < βc (slow decay of G0), R →∞ diverges to +∞, whereas for β > βc, R →∞ diverges to −∞.

orders to unload and, by placing many consecutive orders with the same sign, create a correlated order ﬂow. The second group of agents are the liquidity providers, who post bid and oﬀer and attempt to earn the bid-ask spread. The third group is made by noise traders, i.e. traders placing uncorrelated order ﬂow. Anticipating the discussion in Section7.3, it is indeed reasonable to assume that the strategies of the ﬁrst two type of agents will adjust in such a way to remove any predictability of the midpoint change, or in other words that En−1[rn|I] = 0

- as implied by Eq. (6.21) above. This is a plausible ﬁrst approximation, although one can expect (and indeed observes) deviations from strict unpredictability at high frequencies.

Within the above simpliﬁed model, in which we have neglected volume ﬂuctuations (see Appendix 2 for an attempt to include them), there are only two possible outcomes. Either the sign of the nth transaction matches the sign of the predictor En[ n+1|I], or they are opposite. Let us call rn+ and rn− the expected ex-post absolute value of the return of the nth transaction given that n either matches or does not match the predictor. If we indicate with ϕ+n and (ϕ−n) the ex ante probability that the sign of the n-th transaction matches (or disagrees) with the predictor n, we can rewrite En−1[rn|I] = 0 as:

ϕ+nrn+ − ϕ−nrn− = 0. (6.22) Within the MRR model as above, this means

rn+ = θ(1 − ˆ n) (6.23) rn− = θ(1 + ˆ n). (6.24)

This result shows that the most likely outcome has the smallest impact. We call this mechanism asymmetric liquidity: each transaction has a permanent impact, but the impact depends on the past order ﬂow and on its predictability. The price dynamics and the impact of orders therefore depend on (i) the order ﬂow process (ii) the information set I available to the liquidity provider, and (iii) the predictor used by the liquidity provider to forecast the order ﬂow.

- 6.5.2 Equivalence with the transient impact model In the following we will consider the case where the information set available to liquidity providers is restricted to the past order ﬂow. We call this information set anonymous because liquidity providers do not know the identity of the liquidity takers and are unable to establish whether or not two diﬀerent orders come from the same trader. We assume also that the predictor used by liquidity takers to forecast future order ﬂow comes from a linear model. In some cases, such as for an order ﬂow generated according to the model presented in Section 4.3, this may not be an optimal predictor. However linear time series models are probably the most widely used forecasting tools. Here we analyze a linear time series model based on the signs of executed transactions, and will assume a Kth order autoregressive AR model of the form

ˆ n =

K

i=1

ai n−i, (6.25)

where ai are real numbers that can be estimated on historical data using standard methods (see Lillo and Farmer [2004], Bouchaud et al. [2004] and Appendix 2). The MRR model corresponds to an AR(1) order ﬂow, with a1 = ρ and ak = 0 for k > 1, with an exponential decay of the correlation.

The resulting impact model, Eq. (6.21) with a general linear forcast of the order ﬂow is in fact equivalent, when K → ∞, to the temporary impact model of the previous section (see Appendix of Bouchaud et al. [2004]). It is easy to show that one can rewrite the generalized MRR model in terms of a propagator as

mn = mn−1 + θ n +

∞

i=1

[G(i + 1) − G(i)] n−i + ηn, θ = G(1). (6.26)

The equivalence is obtained with the relation:

θai = G(i + 1) − G(i) or G(i) = θ[1 −

- i−1
- j=1

aj]. (6.27)

- 6.5.3 More general information models In the previous section we have seen that the ﬁxed/temporary impact model is equivalent to the variable/permanent impact model under the additional assumptions that (i) the information set available to the liquidity provider is the set of

the past order ﬂow and (ii) that liquidity providers use a linear forecast model to predict the future order ﬂow from the past and to adjust price response. These two assumptions of the variable/permanent impact model are far from general. In the following we discuss the more general situations where a diﬀerent information set and forecast model can arise.

In most ﬁnancial markets order ﬂow is available in real time to all market participants and thus it is clear that any liquidity provider could use the past order ﬂow time series to trade eﬃciently. However in some cases participants can make use of information other than the time series of order ﬂow signs. There are often indirect clues about the identity of orders such as the consistent use of particular round lots for orders that arrive at regular intervals. Activity in block markets can also provide clues about the activity of large orders. Another case is when a trader is trying to execute her large order by a so-called “slicing and dicing” algorithm. The liquidity provider could be able to detect the presence of this trader and therefore the liquidity provider has additional information to add to her information set.

The algorithm used by the liquidity provider to forecast the future order ﬂow depends on the information set and on the degree of sophistication of the liquidity provider. Even if linear forecasting methods are widespread, they can lead to suboptimal predictions if the time series one is trying to forecast is strongly nonlinear. For example, in Section 4.3 we have discussed a microscopically based order ﬂow model which reproduces the correlation properties observed in the real order ﬂow. This model (Lillo, Mike, and Farmer 2005) is clearly non-linear. Despite the fact that an optimal forecast method for this order ﬂow model is not easily available, one can ﬁnd suboptimal non-linear forecast models that outperform the linear forecast method. When one incorporates non-linear forecast models in the variable/permanent impact model the price dynamics will not be equivalent to the ﬁxed/temporary model.

In conclusion, the variable/permanent model sets a general framework for describing the interaction between order ﬂow and price dynamics. In a paper in progress Gerig et al. (2008) show how diﬀerent assumptions on the information set and on the forecast method lead to diﬀerent functional forms of the impact of hidden orders and on the dynamical properties of prices.

- 6.5.4 Mechanisms for Asymmetric Liquidity Let us rephrase in more intuitive terms the results established above. Due to the small outstanding liquidity, order ﬂow must develop temporal correlations. This is such an obvious empirical fact that high frequency traders/market makers quickly come to learn about it, and adapt to it. In the simple mrr model where signs are exponentially correlated, the probability that a buy follows a buy is p+ = (1+ρ)/2. The unconditional impact of a buy is θ (see Eq. 7.9); however, a

second buy immediately following the ﬁrst has a reduced impact equal to R+1 = θ(1 − ρ). The second buy is not as surprising as the ﬁrst, and therefore should

impact the price less. A sell immediately following a buy, on the other hand, has an enhanced impact equal to R−1 = θ(1 + ρ), in such a way that the conditional average impact of the next trade is zero: p+R+1 + (1 − p+)R−1 ≡ 0 Gerig [2007]. This is the “asymmetric liquidity” eﬀect explained above (Lillo and Farmer [2004], Farmer et al. [2006], Gerig [2007], see also Bouchaud et al. [2006] where it is called “liquidity molasses”). This mechanism is expected to be present in general: because of the positive correlation in order ﬂow, the impact of a buy following a buy should be less than the impact of a sell following a sell – otherwise trends would appear.

But what are the mechanisms responsible for asymmetric liquidity, and how can they fail (in which case markets cease to be eﬃcient)? This is still an open empirical question which started to be investigated only recently. For example, Lillo and Farmer [2004] showed that when the order ﬂow becomes more predictable the probability that a market order triggers a price change is larger for market orders with the unexpected sign than for those with the expected one. Moreover the same authors showed that the ratio between the volume of the market order and the volume at the opposite best is lower (higher) for market orders with expected (unexpected) sign.

Another related basic mechanism is “stimulated reﬁll”: buy market orders trigger an opposing ﬂow of sell limit orders, and vice-versa (Bouchaud et al. [2006]). This rising wall of limit orders decreases the probability of further upward moves of the price, which is equivalent to saying that R+1 < R−1 , or else that the initial impact of the ﬁrst trade reverts at the second trade. This dynamical feedback between market orders and limit orders is therefore fundamental for the stability of markets and for enforcing eﬃciency. It can be tested directly on empirical data. For example, Weber and Rosenow [2005] have found strong evidence for an increased limit order ﬂow compensating market orders.

Since such a dynamical feedback is so important to reconcile correlation in order ﬂow with the diﬀusive nature of price changes, it is worth detailing its intimate mechanism a little further, and insisting on cases where this feedback may break down. Recall our discussion of the market ecology in section 3.8 – market participants can be, in a ﬁrst approximation, classiﬁed as a function of their trading frequencies. Large latent demand arises from low frequency participants; the decision to buy or to sell can be considered as ﬁxed over a time scale of a few hours or a few days, much longer than the average time between trades. These participants create long term correlations in the sign of the trades. Higher frequency traders try to make proﬁt from microstructural eﬀects and short time predictability. Even if institutionally designated market makers are no longer present in most electronic markets, these high frequency strategies are in fact akin to market making – they make money from providing liquidity to lower frequency traders. This is why we often (incorrectly) call this

category of participants “market makers”.16 So one should think of two rather large latent supply and oﬀer quantities that await for favorable conditions, both in terms of price and quantity, to be executed on the market. Then begins a kind of hide and seek game, where each side attempts to guess the available liquidity on the other side. A “tit-for-tat” process then starts, whereby market orders trigger limit orders and limit orders attracts market orders. A buy trade at the ask (say) is a signal that an investor is indeed willing to trade at that particular price. But the seller who placed a limit order at the ask is also, by deﬁnition, willing to trade at that price. The natural consequence is that a ﬂow of reﬁll orders is expected to occur at the ask immediately after a buy trade (and at the bid after a sell).

In other words, optimized execution strategies that look for micro-opportunities

impose strong correlations between market order ﬂow of one sign and limit order ﬂow of the opposite sign. Imagine a case where buy market orders eat up sell limit orders at the ask, with no reﬁll. The ask then moves up one tick. By making the price more expensive the ﬂow of buy market orders slows down and the probability that a sell limit order reappears at the previous ask increases. Imagine now that the reﬁll process is too intense; sell limit orders at the ask now pile up. This has two eﬀects: (i) the probability of a large market order that executes a large volume in one shot increases; (ii) the large volume at the ask decreases the probability of further sell limit orders joining the queue because the priority of these new orders is low. Both cases (no reﬁll or intense reﬁll) therefore induce a clear feedback mechanism ensuring local stability of the order book.

The above mechanism can be thought of as a dynamical version of the supplydemand equilibrium, in the following sense: incipient up trends quickly dwindle because as the ask moves up the buy pressure goes down while the sell pressure increases. Conversely, liquidity induced mean-reversion – that keeps the price low – attracts more buyers and soon gives way. Such a balance between liquidity taking and liquidity providing is at the origin of the subtle compensation between correlation and impact explained above. It is interesting to notice that several other dynamical systems operate similarly, with a competition between two antagonist systems – heartbeats is an interesting example: the sympathetic and parasympathetic system act in opposition to speed up/slow down the cardiac rythm.

One easily envisions that such a subtle dynamical equilibrium can quickly break down: for example, an upward ﬂuctuation in buy order ﬂow might trigger a momentary panic, with the opposing side failing to respond immediately. These liquidity micro-crisis are probably responsible for the large number of price jumps; if the feedback mechanism changes sign, this can even lead to crashes.

16Of course, the above distinction between participants must be taken with a grain of salt: low frequency decisions may be executed using smart high frequency algorithmic trading. In this case, the same participant is at the same time a low frequency trader and a market maker.

The tug-of-war is a vivid illustration of this phenomenon. A major challenge of microstructure theory is to turn the above qualitative story into a quantitative model for heavy tailed return distributions and volatility clustering, with interesting potential ideas on how to limit the occurence of these liquidity micro-crises. We are convinced that a consistent theory of hidden liquidity and stimulated reﬁll is well within reach at this stage.

### 6.6 Empirical results

The section reviews how the above ideas can be directly tested and measured on high frequency data.

We start with the full impact function, deﬁned by Eq. (6.4), which is easily measured – at least when the lag is not too large. When becomes of the order of the number of daily trades or more, the error bar on R quickly becomes large. The main features of R are however quite robust from stock to stock and also across diﬀerent markets. For example, R for France Telecom in 2002 is shown in Fig. (8). One sees a mild increase by a factor λ ∼ 2 between = 1 and

= 1000, before a saturation or maybe a decline for larger lags. This behaviour is quite typical, in particular the roughly two-fold increase between small lags and large lags. So R reveals some non trivial temporal structure – recall that R is constant within models where the midpoint reacts to surprise in order ﬂow. In an mrr setting, the ampliﬁcation factor λ should be 1/(1 − C1), which in found to be in the range 1.2 − −1.4, still too small to explain λ ∼ 2.

As noted above, one can in fact extract the theoretical impact of single trades G0( ) from the empirically measured impact R and the correlation between the sign of the trades C , using Eq. (6.19). This was done in Bouchaud et al. [2006], and indeed produces nice, power-law decaying G0( )’s – see Fig. (9) for a few examples. Within the above restrictive theoretical framework, this provides a direct proof of the transient nature of the impact of single market orders and the long term resilience of markets. This is quite important as far as execution strategies are concerned – see section 10.

We should however list a number of caveats. One is the assumption that the impact is time translation invariant, i.e. only the lag is relevant. This is clearly questionable, since strong intraday seasonality eﬀects are expected. For example, there are indications that the trade sign correlation function C for a given lag

is quite diﬀerent intraday and from one day to the next (Eisler et al. [2008]). Similarly, we expect that the single trade impact should decay diﬀerently intraday and overnight. Second, we have to a large extent discarded the interesting correlations between the state of the order book Ωn, the incoming volume vn and the resulting impact (see Eq. (6.2). All this complexity was replaced by an average description: nf(vn;Ωn) −→ n lnvn. Certainly, a reﬁned version is needed, in particular because the ﬂuctuations of f(vn;Ωn) will contribute to the diﬀusion properties (see Eq. (6.16)). Finally, we have chosen from the start to

0.012

0.01

0.008

R(l)(Euros)

0.006

0.004

FT (2002)

- FT (2001 - 1st semester)

- FT (2001 - 2nd semester)

0.002

0

1 10 100 1000 10000

Time (Trades)

- Figure 8. Average empirical response function R for FT, during three diﬀerent periods (ﬁrst and second semester of 2001 and 2002). We have given error bars for the 2002 data.

For the 2001 data, the y−axis has been rescaled such that R1 coincide with the 2002 result. R is seen to increase by a factor ∼ 2 between = 1 and = 100.

[Figure 113]

- Figure 9. Comparison betwen the empirically determined G0( ), extracted from R and C

using Eq.(6.19), and the power-law ﬁt Gf0( ) = Γ0/( 20 + 2)β/2, for a selection of four stocks: ACA, CA, EX, FP.

#### give a special role to market orders, as if only those impact the price. But this is not true: obviously limit orders also impact the price. In fact, it is precisely the impact of limit orders that oﬀsets that of market orders and leads to a decay of the single trade impact G0( ). In other words, we have studied an eﬀective model in terms of market orders only, dumping into G0( ) the counter-acting eﬀect of limit orders. A more symmetric version of the model, that treats market and limit orders on an equal footing, would be quite enticing (Eisler et al. [2008]).

#### We now consider some empirical evidence for asymmetric liquidity. Figure 10 shows the behavior of the conditional returns r+ and r− deﬁned in Eq. 6.24 as a function of the sign predictor ˆ . The data we show in Fig. (10) is for Astrazeneca, a stock traded at the LSE. The sign predictor is the linear predictor deﬁned in Eq. 6.24. The larger the absolute value of ˆ , the stronger the predictability of the next market order sign. We have plotted the average value of the return conditioned to be in the direction of the predictor, r+, and the average return when the sign of the predictor is wrong, r−. We see that r− is indeed larger than r+ and this diﬀerence increases with the predictability of the order ﬂow. This is a clear evidence for asymmetric liquidity. Note also that both r+ and r− are approximately described by a linear function of the predictor ˆ . This is expected under the model described in Section 6.5.1 (see Eq. 6.24). However the slopes of r+ and r− vs. ˆ are diﬀerent, challenging the implicit symmetric assumption (Eq. 6.24) in the MRR model. Other evidence for the build up of the “liquidity

[Figure 114]

- Figure 10. The expected return as a function of the sign predictor ˆ . The quantity r+ (r−) refer to trades with a sign that is equal (opposite) to the one of the predictor. The data are binned in such a way that each point contains an equal number of observations. Error bars are standard errors. Adapted from Gerig [2007].

molasses” accompanying the ﬂow of market order can be found in Bouchaud et al. [2006] and Weber and Rosenow [2005].

### 6.7 Impact of a large hidden order

We now want to calculate, within the above theoretical framework, the impact of an hidden order of size N. For simplicity, let us ﬁrst assume that the hidden order is made of N consecutive trades made by the same institution, though this remains “hidden” if trades are anonymous. Let us call m0 the price at the beginning of the hidden order and compute the average price mN+t observed t transactions after the completion of the hidden order. Within the generalized MRR model with a linear predictor of the order ﬂow, a straightforward calculation shows that

- i−1
- j=1

t+N

E[mN+t] − m0 =  θ

[1 −

aj] (6.28)

i=t+1

For t = 0 this expression gives the (temporary) total impact of the hidden order, while for t > 0 we can calculate the price reversion after the completion of the hidden order, and the permanent impact (if any) for t → ∞.

The above result can be generalized to the case where there is only one hidden order active at a given time, which mixes with a ﬂow of uncorrelated orders with a constant participation rate π. The total time needed to execute the hidden

order is then T = N/π. It is possible to show in this case that (Farmer, Gerig, Lillo, and Waelbroeck 2008):

 1 −

 . (6.29)

i/π

N

E[mN] − m0 =  θ

ak

i=1

k=1

Let us estimate the above formula in the case where the autocorrelation Cτ of order ﬂow asymptotically decays as a power law Cτ ∼ τ−γ for large τ. There are several diﬀerent ways of generating and forecasting long-memory processes. Here we assume that the participants observing public information model the time series with a FARIMA process. It is known (Beran [1994]) that for large k the best linear predictor coeﬃcients of a FARIMA process satisfy ak ≈ k−β−1 where β = (1 − γ)/2. For large k we can pass into the continuum limit and from Eq. 6.29 the impact is

N−1

E[mN] − m0 =  θ 1 +

i=1

Converting the sum to an integral gives

1 − 1 − (n/π)−β . (6.30)

2β−1πβ 1 − β

[(2N − 1)1−β − 1] ∼ πβN1−β. (6.31)

E[mN] − m0 ≈  θ 1 +

Thus, for a ﬁxed participation rate, the market impact asymptotically increases with the length of the hidden order as N1−β. A typical decay exponent for the autocorrelation of order signs is γ ≈ 0.5 (Lillo and Farmer [2004], Bouchaud et al. [2004]), which means that β ≈ 0.25. This means that according to the linear time series model the impact should increase as roughly the 3/4 power of the order size. An interesting property of this solution is that it depends on the speed of execution. The size of the impact varies as πβ. This means that the slower an order is executed, the less impact it has, and in the limit as the order is executed inﬁnitely slowly the impact goes to zero. Note however that if the execution time T = N/π is ﬁxed, the impact become linear with N but decays as T−β.

To investigate the reversion dynamics we make use again of the Eq. (6.28). We assume that the liquidity provider uses a FARIMA model to forecast order signs and for the sake of simplicity in the following we will assume that π = 1, i.e. that there are no noise traders. Realistically the regression made by the liquidity provider on past signs will use a ﬁnite lag K, leading to:

K

a(iK) n−i (6.32) where (Beran [1994]):

ˆ n =

i=1

a(iK) = −

K i

Γ(i − H + 1/2)Γ(K − H − i + 3/2) Γ(1/2 − H)Γ(K − H + 3/2)

(6.33)

and H = 1/2 − β is the Hurst exponent of the FARIMA process. It is possible to derive an analytical exact result for the permanent impact. In fact, from Eq.(6.28), one can obtain

K

a(jK)) = (6.34)

E[m∞] − m0 =  θN(1 −

j=1

4H−1√πΓ[H]sec[(K − H)π] Γ(3/2 + K − H]Γ[2H − 1 − K]

 θN

By using the Stirling’s formula and the reﬂection formula for the Gamma function one can show that for large K the permanent impact scales as

N Kβ

E[m∞] − m0 ∼  θ

. (6.35)

If K is inﬁnite, then E[m∞] − m0 = 0, i.e. the impact is completely temporary. This can be shown in the mathematically equivalent propagator model Bouchaud et al. [2004, 2006]. For a FARIMA forecast model with ﬁnite K (or equivalently if the sign autocorrelation function decays fast beyond time scale K), the permanent impact is non zero and is linear in N. Even if for large K the permanent impact is small, the convergence to zero with the memory K is very slow.

Another interesting issue that can be discussed within the model is the decay of the impact immediately after the end of the hidden order (deﬁned by Eq. (6.28)). One ﬁnds that the initial drop for t N is in fact very sharp for β < 1: mN+t − mN ∝ −t1−β, such that the slope of the decay is inﬁnite when t → 0 (in the continuous limit).

### 6.8 Aggregated impact

Impact is often measured not on a trade by trade level but rather on a coarse grained time scale, say ﬁve minutes or a day. One then speaks of positive correlations between signed order ﬂow and price returns. At the level of single trades, impact is strongly concave in volume and decays in time. How does this translate

- at a coarse-grained level? In Section 5.2 we have discussed this from an empirical point of view. Here we show how the impact theories we have developed so far make predictions about the impact function, following the approach of Lillo et al. [2008a].

Suppose one aggregates the returns and volumes of N consecutive trades (not necessarily from the same hidden order). Using the same notation as in Section

- 5.2, the total volume imbalance is QN = Nn=0−1 nvn. Conditioned to a particular value QN = Q, what is the average price return R(Q) ? The answer to this question depends on the order ﬂow and on the properties of the impact function. In the following we will consider two extreme cases. In the ﬁrst case we consider an unrealistic model where the order ﬂow is described by an independent identically

- distributed random process, and the impact is ﬁxed and permanent. In the second case we will consider a correlated order ﬂow and a ﬁxed/temporary impact model.
- 6.8.1 Independent identically distributed order ﬂow If the unconditional distribution of market order volume and the functional form of the impact function are known, it is possible to ﬁnd a closed expression for the impact R(Q). Consider a series of N transactions with signed17 volumes vi

corresponding to total return R = Ni=1 ri and total signed volume Q = Ni=1 vi. The expected return given Q can be written

1 PN(Q)

R(Q,N) ≡ E[R|Q] = RP(R|Q,N) dR =

RP(R,Q,N) dR, (6.36)

where PN(Q) is the probability density for Q. We assume that the N individual price impacts ri due to the IID signed volumes vi are given by a deterministic function18 ri = f(vi). Let the distribution of individual vi be p(vi). Then the joint distribution of vi is P(v1,...,vN) = p(v1)...p(vN). The integral above becomes

N

N

f(vi)δ(Q −

RP(R,Q,N) dR = dv1 ...dvNp(v1)...p(vN)

vi),

i=1

i=1

(6.37) where we introduced the Dirac delta function. By making use of the integral representation of the Dirac delta function, after some manipulations it is possible to rewrite R(Q,N) as

1 PN(Q)

N 2π

R(Q,N) =

dλe(N−1)h(λ)g(λ)e−iλQ (6.38)

where h(λ) is the logarithm of the Fourier transform of the volume distribution and g(λ) is the Fourier transform of the product of the volume distribution and the impact function. Moreover PN(Q) is the probability density that the total signed volume in the N trades is Q.

The functional form of the aggregate impact R(Q,N) can be calculated by integrating this expression. It is possible to show that many of the properties of the solution are robust, independent of the details of the model. For small values of Q the aggregate impact R(Q) is always linear with a slope which depends on N and on the details of the volume distribution and of the impact function. For example if the impact function is a power law function |v|ψ and the volume distribution decays asymptotically as P(V ) ∼ V −α−1, then for large N the aggregate impact behaves for small Q as

Q Nκ

R(Q,N) ∼

(6.39)

17 Only in this subsection we indicate with vi the signed and not the absolute value of volume. 18The results remain the same if a noise term is added to the impact function.

where κ depends in a non trivial way on α and ψ (see Lillo et al. [2008a]). For example, if volumes have a ﬁnite second moment and the impact function is concave then κ = 0; in constrast, if the second moment doesn’t exist, and the impact function is suﬃciently concave then κ > 0. The latter case agrees with what is seen in Fig. 5, where the slope of the aggregate impact decreases with N. Thus theories for the aggregate impact make falsiﬁable predictions connecting volumes, order ﬂow and impact.

- 6.8.2 Transient impact model Within the model of section 6.4 above, the aggregate impact reads:

R(Q,N) =

N−1

G0(N−n)E[qn|Q]+

n=0

m<0

[G0(N − m) − G0(−m)]E[qm|Q]. (6.40)

where qn = n lnvn and we assume that volumes are lognormally distributed (see

- Appendix 2). Because trades are long ranged correlated, the second term is nonzero. But one can show it is subdominant when N 1, so we discard it in a ﬁrst approximation. In the ﬁrst term, one can compute E[qn|Q] = x using the fact that the qns are, within the model, Gaussian with rms = s. Noting also that typical values of Q are of order N1−γ/2 N, one ﬁnally ﬁnds:

∞

sQ IN

2/2. (6.41)

duueus−u

, I = 2

x ≈

0

With R(Q,N) ≈ Γ0N1−βx/(1−β) and the above relation between β = (1−γ)/2, we ﬁnally ﬁnd the following result, written in a suggestive scaling form:

√

sΓ0 I(1 − β)

Q

N1−γ/2 . (6.42) This means that by rescaling the return and the signed volume by their respective root mean square value, one obtains at large N a limiting curve which is a straight line. Whereas for small N impact is strongly concave, impact becomes linear when N 1. One can go one step further and compute the leading non-linear correction in Q when N is large. One ﬁnds that it is negative, as a remnant of the small N concavity, and becomes noticeable at increasingly larger values of

N

R(Q,N) =

- Q ∼ N, as seen on empirical data – see Fig (5) below. The important conclusion of this model is that although the impact of indi-

vidual trades is concave and decays in time, the compensating eﬀect of correlated trades leads to a well deﬁned linear relation between order imbalance and returns at an aggregated level. This is important because such a relation is often interpreted as a manifestation of the permanent component of the impact.

Is this linear relation telling us that part of the trades have indeed predicted correctly the aggregated return (in Hasbrouck’s words) – see Hasbrouck [2007]? In light of the all the above results, it looks much more plausible to us that anonymous trades in fact statistically induce price changes, although in a quite non trivial and perhaps unexpected fashion.

### 7 THE DETERMINANTS OF THE BID-ASK SPREAD

In modern electronic markets, liquidity is self-organized, in the sense that any agent can choose, at any instant of time, to either provide liquidity or consume liquidity. The liquidity of the market is partially characterized by the bid-ask spread S, which sets the cost of an instantaneous round-trip of one share (a buy instantaneously followed by a sell, or vice versa).19 A liquid market is such that this cost is small. A question of both theoretical and practical crucial importance is to know what ﬁxes the magnitude of the spread in the self-organized set-up of electronic markets, and the relative merit of limit vs. market orders. In the economics literature (O’Hara [1995], Biais et al. [1997], Madhavan [2000], Glosten and Milgrom [1985]), the existence of the bid-ask spread is often attributed to three types of liquidity providing costs, Stoll [1978]:

- • (i) order processing costs (this includes the proﬁt of the market maker);
- • (ii) adverse selection costs: liquidity takers may have superior information on the future price of the stock, in which case the market maker loses money;
- • (iii) inventory risk: market makers may temporarily accumulate large long or short positions which are risky. If agents are risk-sensitive and have to limit their exposure, this may add extra-costs.

A somewhat surprising conclusion of early econometric studies is that order processing costs account for a large fraction of the spread. This may make sense in illiquid markets where market makers exploit a monopolistic situation to open up large spreads, but cannot be the correct picture in highly liquid, electronic markets in which market making is highly competitive. What we argue below is that the main determinant of the spread is in fact impact.

### 7.1 The basic economics of spread and impact

- 7.1.1 The average gain of market makers What is the basic economics behind a trade, i.e. the encounter between a liquidity taker and one (or several) liquidity provider(s)? Consider the sequence of all trades (not necessarily coming from the same hidden order). Let the nth trade

have volume vn and sign n. The proﬁt collectively made by liquidity providers on that given trade, marked to market at time n + is given by

Sn 2

GL(n,n + ) = vn n (mn + n

) − mn+ , (7.1)

where Sn is the value of the spread at that moment in time. Think of a buy trade n = +1. The above equation compares the money received by the liquidity

- provider when the trade occurs (vn(mn+ S

2 )) to its marked to market (midpoint)

n

19Other determinants of liquidity discussed in the literature are the depth of the order book and market resiliency, see Black [1971], Kyle [1985].

price at time n + . Symmetrically, the proﬁt made by the liquidity taker using market orders is GL(n,n+ ) = −GM(n,n+ ). The above equation clearly shows that the proﬁtability of market making comes from the spread (+Sn/2), while the losses are induced by market impact (− n(mn+ − mn)), which may or may not come from more informed traders (see below).

Neglecting for simplicity volume ﬂuctuations at this stage (vn ≡ v), and using Eq. (6.4), we see that the average gain of the market maker in the absence of extra costs is given by:

S 2

E[GL]( ) = v E[

] − R , (7.2)

which shows explicitly that for a given total market impact R , the spread S should be larger than a minimum value for market making strategies to be at all proﬁtable on a time scale – or else, for a given value of S, the impact function

- R should be as small as possible. We recover here the idea that it is in the interest of liquidity providers to control the growth of R by tuning the liquidity asymmetry.

In fact, the above reasoning neglects the cost of unwinding the market maker position, and a better estimate will be provided below. But the main message of the simple computation above is that the spread compensates for the impact of market orders. In the microstructure literature, this is refered to as ‘adverse selection’; as alluded to above, this implies that market orders originate from better informed traders, with an information on the future price on average worth R . But the same result would hold if impact was purely statistical, with no information content whatsoever. In fact, one could even revert the logic and claim that it is the spread that determines the impact: if some trader accepted to pay mn + Sn/2 for the stock, it is natural that the market as a whole revises its fair price estimate from mn to mn + αSn/2, where α ≥ 0 is a number measuring how trades inﬂuence the participants beliefs, leading to R∞ = αS/2. The mrr model with spread (see Section 7.2.2), in this context, assumes that market participants believe that the last traded price is indeed the correct price (α = 1). Clearly, in that model, the cost of a market order or the gain of a limit order are exactly zero. This leaves us, by the way, in the familiar but uncomfortable situation of the “no trade theorem”: if the spread is such that the information content of a market order is compensated, why would the informed trader trade at all?

- 7.1.2 How informed are the trades? So are some market orders informed? Can one ﬁnds convincing ex-post signatures of informed trades? A minimal deﬁnition of an informed trade is a trade that earns a proﬁt signiﬁcantly larger than the transaction costs (including both brokerage fees and market slippage). Introducing the signed return r(n,n + ) ≡ n(mn+ − mn), the proﬁt of the nth market order on time scale

- 0.8
- 1

0.6

P(r)r

0.4

informed trades

0.2

0

R(l)

-4 -2 0 2 4 r

- Figure 11. Two extreme cases for the distribution P(r ) of signed returns r . (a) Black curve: nearly all trades are uninformed but impact prices, leading to a symmetric P(r ) around a non zero average impact. (b) Red curve: most trades are uninformed and do not impact prices, while some trades are informed and predict correctly the future return, leading to a thick tail in the r > 0 region.

is:

Sn 2

GM(n,n + ) = vn r(n,n + ) −

. (7.3)

Note that by deﬁnition the average of r(n,n + ) is equal to the total impact R , which is positive. If one averages the above equation over all trades, one in fact ﬁnds that E[GM] is close to zero, which means that the spread compensates for the average impact, at least measured on short time scales (between a few seconds to a few days). More precisely, on liquid NYSE stocks in 2005 (when market makers were still present), one ﬁnds that E[GM] is zero within error bars, which means that, after transaction costs, market orders lose money on average. The situation is slightly better on liquid PSE stocks in 2002, where one ﬁnds E[GM] = gE(S)/2 with g ≈ 0.3 (see Fig. 14 below). This amounts to 3 − 5 bp per trade, close to the transaction costs. So, on average, and although market orders do impact prices, there does not seem to be much short term information in these orders – at least judging from their ex-post proﬁtability. The question of longer term information is of course left open here, simply because the statistics is not suﬃcient to judge the average proﬁtability of trades on long time scales, and also because long term drift eﬀects cannot be neglected (on average, buy trades are proﬁtable in the long run!).

We can look in more detail at the full distribution of r , P(r ), which contains much more information. Note that its second moment E[r2| ] is very close to the

volatility on scale , which soon becomes much larger than R2 when increases. Concerning the shape of P(r ), two extreme scenarios could occur (see Fig. 11 for a cartoon):

- • A small proportion of well informed trades predict the future price while a majority of trades are uninformed and do not impact the price at all. The distribution of r should then be composed of a broad blob, symmetric around r = 0, corresponding to uninformed trades, plus a hump (or more plausibly a broad shoulder) on the positive side, corresponding to well informed trades. The non zero value of E[r ] comes from these informed trades. This is the scenario behind, for example, the Kyle model, or the Glosten-Milgrom model.
- • All trades are equally weakly informed or even not informed, but all statistically impact prices. In this case one expects a symmetric broad blob, but around the average impact E[r ].

Empirically, the distribution of r is found to be very close to the second picture for corresponding to intra-day time scales. In particular, no noticeable asymmetry (beyond the existence of a non zero value of E[r ]) is observed on liquid stocks – see Fig. (12) for an example. This suggests that trades, on average, impact prices, but do not seem to ‘predict’ future prices – at least not on short time scales. The strong relation between order imbalance and price returns would then be tautological consequence of this impact (see section 6), and not a signature of ‘true’ information revelation.

### 7.2 Models for the bid-ask spread

- 7.2.1 The Glosten-Milgrom model One of the earliest theories of the spread that makes the above discussion is the sequential trade model of Glosten and Milgrom (Glosten and Milgrom [1985]). One assumes that market orders are either due (with some probability q) to

informed traders, who know the end of day price pf, or (with probability 1 − q) to noise traders. The value of q is assumed to be known by the market maker, which is not necessarily very realistic (a similar assumption is made within the Kyle model). The end of day price pf can either be above (p>) or below (p<) the open price. The probabilities for either outcome at the start of the day are δ+ = δ− = 1/2 for simplicity. But as trading occurs, either at the bid or at the ask, the market maker updates in a Bayesian way the value of δ+ = 1 − δ−: trades at the ask increase the value of δ+, while trades at the bid increase δ−. This leads to a certain update rule for δ+ as a function of the sign of the next trade, which we do not write here explicitly. Anticipating the value of δ± after the next trade allows the market maker to position his quotes in such a way as not to have ex-post regrets. More precisely:

a = δ+(+)p> + δ−(+)p<; b = δ+(−)p> + δ−(−)p<, (7.4)

[Figure 115]

- Figure 12. Probability distribution P(r ) of the quantity r = (mn+ − mn).εn (in Euros), for = 128. The data is again France Telecom during 2002. The negative part of the distribution has been folded back to positive r in order to highlight the small positive assymetry of the distribution. The average value R = E[r] ≈ 0.01 is shown as the vertical dashed line. The dashed-dotted line corresponds to the distribution of r − 0.01, for which no asymmetry of the type shown in Fig. (11) can be detected. This curve has been shifted upwards for clarity.

where (±) refers to the sign of the next trade. This leads to the following prediction for the bid-ask Sn after the nth trade:

Sn = 4qδ+(n)δ−(n)(p> − p<) (7.5)

where δ±(n) is the updated value of δ± after n trades (with δ±(0) = 1/2), and we have neglected terms of order q2 which must be small if this model is to be realistic. This model is by construction compatible with a random walk for the midpoint, with a volatility per trade σ1 proportional to the bid-ask spread, as will be reported below. It also predicts that the bid-ask spread declines on average thoughout the day, since the update rule drives δ+ either to zero or to one: as trading occurs, the market maker discovers more accurately which outcome is more likely. A detailed comparison of this model with empirical data is given in Wiesinger et al. [2008]. Here we simply note that as far as order of magnitude goes, the spread at the beginning of the day (when δ± = 1/2) is typically 0.1% whereas the daily volatility ﬁxes the order of magnitude of p> − p< to typically 2%, leading to q ∼ 0.05. Within this framework, one ﬁnds again that the fraction of short time ‘informed trades’ must be small. One also ﬁnds that in this model the spread decays exponentially fast with time, at variance with the slow, power law relaxation that has been observed (see Section 7.4).

- 7.2.2 The MRR model with a bid-ask spread The original mrr model is in fact slightly diﬀerent from the model described in Section 6.3. mrr model rather assumes that it is the ‘true’ fundamental price

pn, rather than the midpoint mn, which is impacted by the surprise in order ﬂow, and hence

pn+1 − pn = ηn + θ[ n − ρ n−1]. (7.6) mrr then specify a rule for the bid and ask price, which in turn allows one to compute the midpoint mn. Since market makers cannot guess the surprise of the next trade, they post a bid price bn and an ask price an given by:

an = pn + θ[1 − ρ n−1] + φ; bn = pn + θ[−1 − ρ n−1] − φ, (7.7)

where φ is the extra compensation claimed the market maker, covering processing costs and the shock component risk. The above rule ensures no ex-post regrets for the market maker: whatever the sign of the trade, the traded price is always the ‘right’ one. The midpoint m ≡ (a + b)/2 immediately before the nth trade is now given by:

mn = pn − θρ n−1, (7.8) whereas the spread is given by S = a − b = 2(θ + φ).

More generally, assuming that only the sign surprise matters, one can write, for arbitrary correlations between signs:

n+ −1

mn+ − mn =

j=n

n+ −1

{ j − Ej[ j+1]}, (7.9)

ηn + θ

j=n

where the last term is the conditional expectation of the next sign. In the Markovian case, Ej[ j+1] = ρ j, and we recover the above result. The impact function, in the general case, reads

R = θ [1 − C ]. (7.10)

Using Eq. (7.2), one sees that the long term proﬁt of market makers is zero. However, due to correlations between trades, the long time impact is enhanced compared to the short term impact by a factor

1 1 − C1

> 1. (7.11)

λ =

As discussed very generally above, spread and impact are two sides of the same coin. This is particularly clear within the mrr model, where the half-spread S/2 is set to be equal to the long term impact R∞ = θ. This means that the proﬁt of market makers is exactly zero (provided φ = 0), but also, as noted above, that the proﬁt of putatively informed market orders is zero. The spread in the MRR model is

S = 2(θ + φ) = 2(R∞ + φ) = 2λR1 + 2φ (7.12) where λ = (1 − ρ)−1. An alternative, enlightening derivation is provided in

- Appendix 3. One computes the mid-point volatility on scale , deﬁned as

1

σ2 =

(m +i − mi)2 . (7.13)

One ﬁnds a sum of a trade induced volatility θ2(1 − ρ)2 and a ‘news’ induced volatility Σ2:

σ12 = (mn+1 − mn)2 = Σ2 + θ2(1 − ρ)2 (7.14) and

ρ 1 − ρ

) = Σ2 + θ2(1 − ρ2) ≥ σ12. (7.15)

σ∞2 = Σ2 + θ2(1 − ρ)2(1 + 2

The mrr model therefore leads to two simple relations between spread, impact and volatility per trade

S = 2λR1 + 2φ; σ12 = R21 + Σ2, (7.16)

where λ = (1 − ρ)−1 and φ is any extra compensation claimed by market makers. These relations will be generalized to more realistic assumptions and tested empirically in the next two sections.

### 7.3 Limit vs. market orders: the microstructure phase diagram

- 7.3.1 Market order strategies As we have mentioned above, the gain (or cost) of a given market order can be

deﬁned as vn[r(n,n + ) − S

2 ]. This deﬁnition in fact marks the trade to market after trades and is often referred to as the realized spread (Bessembinder [2003], Stoll [2000]). The volume weighted averaged gain (over a large number of trades) of market orders over a long horizon 1 is therefore:20

n

E[vR1(v)] E[v] −

E[vS] 2E[v]

E[GM] ≈ λ

. (7.17)

In this expression we have introduced the volume dependent lagged impact function

R (v) = E[ n(mn+ − mn)|vn = v] (7.18)

and we have used the above deﬁnition of the ampliﬁcation factor λ: R 1 = λR1. In the plane x = E[vR1(v)]/E[v], y = E[vS]/E[v] (which will repeatedly be used below), the condition E[GM] = 0 deﬁnes a straight line of slope 2λ separating an upper region where market orders are on average costly from a region where single market orders are favored: see the red line in Fig. (13). For large spreads, the positive average cost of market order would deter their use; limit orders would then pile up and reduce the spread.

Below the red line of slope 2λ market orders have a negative cost, and one might be able to devise proﬁtable strategies based solely on market orders. The idea would be to try to beneﬁt from the impact term R∞ in the above balance equation. The growth of R ultimately comes from the correlation between trades, i.e. the succession of buy (sell) trades that typically follow a given buy (sell) market order. The simplest ‘copy-cat’ strategy which one can rigorously test on empirical data is to imagine placing a market order with vanishing volume fraction (so as not to aﬀect the subsequent history of quotes and trades), immediately following another market order. This strategy suﬀers on average from the impact of the initial trade, used as a guide to guess the direction of the market. Therefore, the proﬁt GCC of such a copy-cat strategy, marked to market after a long time and neglecting further unwinding costs, is reduced to:

E[vR1(v)] E[v] −

E[vS] 2E[v]

GCC = [λ − 1]

. (7.19)

By requiring that this gain is non-positive, one obtains a lower line in the plane x,y, of slope 2(λ − 1). Only below this green line can the above inﬁnitesimal

20Note that this deﬁnition neglects the fact that one single large market order may trigger transactions at several diﬀerent prices, up the order book ladder, and pay more than the nominal spread. Nevertheless this situation is empirically quite rare on the markets we are concerned with, and corresponds to only a few percents of all cases Farmer et al. [2004].

[Figure 116]

- Figure 13. General “phase diagram” in the plane x = E[vR1(v)]/E[v], y = E[vS]/E[v], showing several regions: (i) above the red line of slope 2λ, market orders are costly (on

average) and market making is proﬁtable; (ii) below the blue line of slope ≈ 2/(1 − C1), limit orders are costly and no market-making strategy is proﬁtable; (iii) above the black line of slope 2λβ, market making on time scale β−1 (or faster) is proﬁtable (PMM); (iv) below the green line of slope 2(λ − 1), copy-cat strategies can be proﬁtable (PCC). Since neither market orders nor liquidity providing should be systematically penalized for markets to ensure steady trading, we expect that markets should operate in the ‘neutral wedge’ in between the blue and the red line. Competition between liquidity providers should push the market towards the blue line. Since copy-cat strategies should not be proﬁtable either, the PCC green line cannot lie above this blue line. Note that the blue, red and black lines all coincide within the mrr model.

copy-cat strategy be proﬁtable. We therefore expect markets to operate above this line and below the red line of slope 2λ.

Note also that the long-time impact of an isolated market order, uncorrelated with the order ﬂow, is given by G0( 1) which is small (see section 6.2). These isolated market orders thus also have a positive cost equal to half the spread. The only way to beneﬁt from the average impact R is to free-ride on a wave of orders launched by others, as in the above copy-cat strategy. Let us now take the complementary point of view of limit orders and determine the region of proﬁtable market making strategies.

- 7.3.2 An inﬁnitesimal market making strategy We now compute the gain of a simple market making strategy which amounts to participating in a vanishing fraction of all trades through limit orders. The simplest strategy is to consider a market maker with a certain time horizon who

- provides an inﬁnitesimal fraction ϕ of the total available liquidity. As illustrated

by Eq. (7.17), the cost incurred by the market maker comes from market impact: the price move is anti-correlated with the accumulated position. When the crowd buys, the price goes up while the market making strategy accumulates a short position which would be costly to buy back later, and vice-versa.

We consider a steady-state market making strategy that avoids explicit unwinding costs. The strategy is such that tendered volume dynamically depends on the accumulated position, which insures that the inventory is always bounded. We choose the tendered fraction ϕ to be given by ϕi = ϕ0(1 + αVi ), where Vi is the (signed) position accumulated up to time i−, and = +1 for orders placed at the ask and = −1 for orders placed at the bid. This mean-reverting strategy ensures that the typical position is always bounded. One can now use this strategy for an arbitrary long time T; its proﬁt & loss is simply given by

T−1

GL =

ϕi ivi(mi + i

i=0

Si 2

). (7.20)

For large T one can replace this expression by its average,

Si 2

GL = TE[ϕi ivi(mi + i

)], (7.21)

with O(T0) corrections due to the residual position at T. This quantity has been computed in Wyart et al. [2006], and depends on the value of β = 1 − αϕ0E[v] that ﬁxes the typical time scale ∗ = (1 − β)−1 of the market making strategy. When β → 0 (fast market making), the gain per unit time and unit volume reduces to

E[vR1(v)] E[v]

GL(β → 0) Tϕ0E[v] ≈

E[vS] 2E[v]

[1 − C1] −

, (7.22) whereas β → 1, corresponding to slow market making, yields:

GL(β → 1) Tϕ0E[v]

E[vR1(v)] E[v]

E[vS] 2E[v] −

=

. (7.23)

The competition between impact and spread is more favorable to limit orders when the strategy is fast (β = 0) than when it is slow (β = 1). Imposing that there is a certain frequency β such that the gain of market making strategies is zero leads to a linear relation between spread and impact, generalizing the above mrr relation Eq. (7.16)

E[vR1(v)] E[v]

E[vS] E[v]

= 2λβ

. (7.24)

Using the empirical shape of R and C , the slope 2λβ is found to increase between ≈ 2/(1−C1) and 2λ when β increases from zero to one. When β → 1, λβ → λ and the lower limit of proﬁtability of very slow market making is precisely the red line

of Fig. (13) where market orders become proﬁtable. Faster strategies correspond to smaller values of λβ, closer to 1/(1 − C1), leading to an extended region of proﬁtability for market making. From the assumption that the above market making strategy for any value of β should be at best marginally proﬁtable (since one might ﬁnd more sophisticated strategies, which take full advantage of the correlations between signs and volumes), we ﬁnally obtain the following bound between spread and impact:

E[vR1(v)] E[v]

2 1 − C1

E[vS] E[v] ≤

, (7.25)

deﬁning the blue line of slope 2/(1−C1) in the x,y plane of Fig. (13). Consistently with the mrr model, when λ = 1/(1 − C1), the blue and red line of Fig. (13) exactly coincide. Using that fact that Rn1+ ≤ R(1n−1)+, a simple generalisation of the argument presented in Appendix 3 allows one to show directly that the cost of limit orders is indeed negative above the blue line.

Eqs. (7.17,7.25) and the resulting microstructural “phase diagram” of Fig. (13) are the central results of this section. The above analysis delineates, in the impact-spread plane, a central wedge bounded from above by a slope 2λ and from below by a slope ≈ 2/(1 − C1), within which both market orders and limit orders are viable. In the upper wedge, market orders would always be costly and would be substituted by limit orders. In the lower wedge, market making strategies, even at high frequencies, would never eke out any proﬁt. Such a market would not be sustainable in the absence of any incentive to provide liquidity. But if the spread happened to fall in this region, the enhanced ﬂow of market orders would soon reopen the gap between bid and ask. In the mrr model, this wedge reduces to a single line.

- 7.3.3 Comparison with empirical data In conclusion of the above theoretical section, one expects electronic markets to operate in the vicinity of the blue line of Fig. (13), i.e. there should be a linear

relation between spread and market impact with a slope close to 2/(1 − C1). This prediction has been tested on empirical data in Wyart et al. [2006], where diﬀerent markets were considered. The prediction can be tested in two diﬀerent ways – for a given stock across time, and across all diﬀerent stocks. In both cases, a rather convincing agreement with the theory is obtained. We show for example in Fig. (14) the cross-sectional test of Eq.(7.25) over 68 diﬀerent stocks of the pse in 2002. The relative values of the spread and the average impact varies by a factor 5 between the diﬀerent stocks, which makes it possible to test the linear relations (7.19,7.25). A linear ﬁt with zero intercept gives a slope of 2.86,21 while the average of 2/(1 − C1) over all stocks is found to be ≈ 2.64.

However, the situation appears to be diﬀerent on the nyse, where specialists are present. Plotting the data corresponding to the 155 most actively traded

21 The intercept of a two-parameter regression is in fact found to be slightly negative.

[Figure 117]

- Figure 14. 68 stocks of the Paris Stock Exchange in 2002. Each point corresponds to a

pair (y = vS / v , x = vR1 / v ), computed by averaging over the year. Both quantities are expressed in basis points. We also show the diﬀerent bounds, Eqs. (7.17,7.19,7.25), and a linear ﬁt that gives a slope of 2.86, while 2/(1 − C1) ≈ 2.64. The correlation is R2 = 0.90.

#### stocks on the nyse in 2005 in the spread-impact plane, one now ﬁnds that the empirical results cluster around the upper red line limit where market orders become costly – see Fig. (15). The regression has a signiﬁcantly larger slope of 3.3, larger than 2/(1−C1) ≈ 2.78, and a positive intercept 2φ ≈ 1.3 basis points.22 This suggests the existence of monopoly rents on nyse: even if there is some competition to provide liquidity with other market participants. Market makers post spreads that are systematically over-estimated compared to the situation in electronic markets, with a non-zero extrapolated spread 2φ for zero market impact. This result is in agreement with older studies on the nyse: Harris and Hasbrouck [1996] used data from the early 90’s to show that limit orders were more favorable than market orders; and Handa and Schwartz [1996] showed that pure limit order strategies were indeed proﬁtable. We refer to Wyart et al. [2006] for more discussion.

#### The empirical analysis therefore shows that on liquid markets, an approximate symmetry between limit and market orders holds, in the sense that neither market orders nor limit orders are systematically unfavorable. Markets operate in the ‘neutral wedge’ of Fig. (13). In fully electronic markets, competition for providing liquidity is eﬃcient in keeping the spread close to its lowest value. On markets

22This is ﬁve times smaller than the average spread, leading to φ/θ ∼ 0.25, much smaller than the result φ/θ ∼ 1 − 2 found within mrr model in 1990, or a similar value reported in Stoll [2000].

[Figure 118]

- Figure 15. 155 stocks of the nyse 2005. Each point corresponds to a pair (y = vS / v ,

x = vR1 / v ), computed by averaging over the year. Both quantities are expressed in basis points. We also show our bounds, Eqs. (7.17,7.19,7.25). The data shows clearly that market orders are less favorable than in the electronic Paris Bourse. The regression now has a positive intercept of 1.3 bp with an R2 = 0.87.

with specialists, such as the nyse, spreads appears to be signiﬁcantly larger market orders are now marginally costly on average.

Note that the above analysis does not require any model speciﬁc assumptions such as the nature of order ﬂow correlations or the fraction of informed trades, etc. In fact, the above results hold even if trades are all uninformed but still mechanically impact the price.

### 7.4 Spread dynamics after a temporary liquidity crisis

The above analysis has shown the existence of relations between market impact and the unconditional value of the spread. The spread, however, is a variable with interesting temporal dynamics. Several studies have characterized the statistical properties of spread. Generally these studies have found that the spread distribution is fat tailed and the time correlation properties are consistent with a long memory process (Plerou et al. [2005], Mike and Farmer [2008], Gu, Chen, and Zhou [2007]).

It is also interesting to ask how the spread responds after a temporary liquidity crisis. As we will describe in more detail in Section 8.1, even at the scale of individual transactions, price returns are heavy tailed, i.e it is not unfrequent to observe individual transactions triggering large price changes. This often happens because a market order removes all the volume at the best, and the next to best

occupied price level has a price very diﬀerent from the price at the best (Farmer et al. [2004]). As a consequence even a small order can create a large price change creating a very large spread. A large spread is what we mean here by a “temporary liquidity crisis”.

We will now describe the average dynamics followed by the spread as it converges to its ”typical” value. First of all a large spread is a strong incentive for limit orders inside the spread and a strong disincentive for market orders. Direct measurements of the order ﬂow conditional on the spread value conﬁrm this intuition (Mike and Farmer [2008], Ponzi et al. [2008]). The limit order ﬂow inside the spread has a limit price distribution which is roughly independent of spread size and monotonically decreasing when one moves from the same best toward the opposite best. This suggests that the typical spread dynamics is not a fast reversion to its typical value, but rather it is a slow process where each liquidity provider competes with the others to close the spread. Each player tries to do this as slowly as possible in order to get a more favorable price from the incoming market orders, but at the same time competition prevents this from being too slow. Empirically this slow decay has been measured in Zawadowski et al. [2006], Ponzi et al. [2008]. One way of quantifying the average dynamics is by computing the quantity, Ponzi et al. [2008],

G(τ|∆) = E(St+τ|St − St−1 = ∆) − E(St) (7.26)

where St is the spread at time t (in seconds). This quantity is the expected value of the spread at time t + τ conditional to the fact that at time zero there is a spread change of size ∆. Figure 16 shows this quantity for the stock AZN traded at the LSE as a function of τ for diﬀerent positive and negative values of ∆. The decay of G(τ|∆) as a function of τ is very slow and for large values of τ is compatible with a power law decay with a ﬁtted exponent in the range 0.4 − 0.5. A similar slow decay of the volatility after a shock has been reported in Lillo and Mantegna [2003], Zawadowski et al. [2006], Joulin et al. [2008].

- 8 LIQUIDITY AND VOLATILITY

- 8.1 Liquidity and large price changes

One of the best known statistical regularities of ﬁnancial time series is the fact that the empirical distribution of asset price changes is heavy tailed, i.e. there is a higher probability of extreme events than in a Gaussian distribution. This property has been veriﬁed by many authors on many diﬀerent ﬁnancial time series (for example, Mandelbrot [1963], Lux [1996], Gopikrishnan et al. [1998]). Extensive empirical analyses have shown that the distribution of price change over time intervals ranging from few minutes to one or few trading days is asymptotically distributed in a way that is approximately independent of the time interval size. Many estimates indicate that the part of the distribution describing large price

[Figure 119]

[Figure 120]

[Figure 121]

[Figure 122]

[Figure 123]

[Figure 124]

|[Figure 125]<br><br>[Figure 126]<br><br>[Figure 127]<br><br>[Figure 128]<br><br>[Figure 129]<br><br>[Figure 130]<br><br>[Figure 131]<br><br>[Figure 132]<br><br>[Figure 133]<br><br>|
|---|

[Figure 134]

[Figure 135]

[Figure 136]

[Figure 137]

[Figure 138]

[Figure 139]

[Figure 140]

[Figure 141]

[Figure 142]

[Figure 143]

[Figure 144]

[Figure 145]

[Figure 146]

[Figure 147]

- Figure 16. Conditional spread decay G(τ|∆) deﬁned in Eq. 7.26 for the stock AZN. The ﬁgure shows G(τ|∆) for diﬀerent positive values of ∆ (in ticks) corresponding to an opening of the spread at time lag τ = 0. Adapted from Ref. Ponzi et al. [2008].

changes is a power-law. For larger time intervals the asymptotic behavior of the return distribution becomes slowly consistent with a Gaussian tail in accordance with Central Limit Theorem. The heavy tailed property of large price change is important for ﬁnancial risk, since it means that large price ﬂuctuations are much more common than one might expect under a Gaussian hypothesis.

There have been several conjectures about the origin of heavy tails in prices. Two theories that make testable hypotheses about the detailed underlying mechanism are the subordinated random process theory of Clark [1973] and the recent theory of Gabaix et al. [2003]. The ﬁrst model has its origins in a proposal of Mandelbrot and Taylor [1967] that was developed by Clark. Mandelbrot and Taylor proposed that prices could be modeled as a subordinated random process Y (t) = X(τ(t)), where Y is the random process generating returns, X is Brownian motion and τ(t) is a stochastic time clock whose increments are independent and identically distributed and uncorrelated with X. Clark hypothesized that the time clock τ(t) is the cumulative trading volume in time t. In simple terms, the subordination hypothesis states that price changes would be Gaussian if one measured them in equal intervals of volume (or number of trades) rather than in real time intervals.

Gabaix et al.’s proposal, in contrast, is that high volume orders cause large price movements. They argue that the distribution of large trade size scales as P(V > x) ∼ x−α, where v is the volume of the trade and α ≈ 1.5. Based the assumption that agents maximize a ﬁrst order utility function, with a risk penalty

term that is proportional to standard deviation rather than variance, they claim that the average market impact function has the form ∆p ∝ V ψ, where ψ ≈ 0.5. From this follows that large price changes have a power law distribution with exponent α/ψ ≈ 3. For a critique of the empirical results and a rebuttal see Farmer and Lillo [2004], Plerou et al. [2004]

Both the Clark and the Gabaix theories emphasize the role of trading volume

- as the determinant of large price changes. Even if it is clear that volume has some role in determining price changes, recent studies show that trading volume could not be the key factor. In a recent paper Farmer et al. [2004] considered the distribution of returns generated by individual market orders. They showed that
- at even at this microscopic time scale price returns are heavily tailed, and more importantly, the size of price moves is essentially independent of the volume of the orders. Both these facts seriously challenge the explanation of fat tails based on volume ﬂuctuations. In this paper Farmer et al. showed that price returns associated with individual transactions are driven by liquidity ﬂuctuations. The authors proposed and tested a mechanism for explaining how liquidity ﬂuctuations determine large price changes. Even for the most liquid stocks in the London Stock Exchange, the limit order book often contains large gaps, corresponding to a block of adjacent price levels containing no quotes. When such a gap exists next to the best price, a new market order can remove the best quote and generate a large price change. At this time scale the distribution of large price changes merely reﬂects the distribution of gap sizes in the order book. The LSE data indicate that approximately 85% of the trades having a non zero price impact have a volume equal to the volume at the best. Moreover 97% of the trades having a non zero price impact generate a price change equal to the ﬁrst gap. In summary the ﬂuctuations of the gap sizes in the book are a key determinant of large price changes. The gap size is a measure of the liquidity available in the market as limit orders. Thus ﬂuctuations of liquidity, i.e. in the market’s ability to absorb new market orders, are the origin of large price changes, while the trading volume plays a minor role.

The above proposed mechanism raises the question of the importance of temporary liquidity crises, evidenced by large gaps in the book, for price changes over long time intervals. Although a deﬁnite answer is not available, there are three indications that short time scale and long time scale price ﬂuctuations may be related. First, the gap size displays long memory properties in time, Lillo and Farmer [2005]. This means that the gap size, i.e. the liquidity availability, is strongly correlated in time. Periods when the typical gap size is large are likely to be followed by periods of large gaps, i.e. liquidity availability is a persistent quantity. Second, it has been recently shown that the permanent component of the price impact is roughly proportional to the immediate impact caused by the trade (Ponzi et al. [2008]). Thus the distribution of permanent price impacts, which is closely related to the distribution of price changes over relatively long time intervals, is approximately the same as the distribution of temporary price

[Figure 148]

- Figure 17. Cumulative distribution of absolute (log)returns P(|r| > x) for the NYSE stock Procter & Gamble under diﬀerent time clocks, plotted on double logarithmic scale. The black circles refer to 15 min returns, the red squares refer to returns aggregated with a ﬁxed number of transactions, and the blue square shows the cumulative distribution obtained by randomly shuﬄing individual transaction returns and then aggregating them in a way that matches the number of transactions in each real time interval. The dashed black line corresponds to a normal distribution.

impacts, i.e. of gaps in the order book. The third indication concerns the relative importance of volume and liquidity in explaining aggregate price changes, which is discussed in more detail in the next section.

### 8.2 Volume vs. liquidity ﬂuctuations as proximate causes of volatility

The existence of a relation between volume and volatility has been known for a long time. This relation has been often interpreted as a causal relation, suggesting that volume (or number of transactions) is the driving factor determining volatility (Ane and Geman [2000]). In the previous section we discussed the subordination hypothesis, which states that returns would be Gaussian if measured in equal intervals of volume rather than in equal intervals of real time. The recent theory by Gabaix et al. (2003,2006) reaches the same conclusion. Here we present some evidence challenging this view and indicating that liquidity ﬂuctuations may be more important than volume in explaining volatility ﬂuctuations. The question can be posed in terms of Equation 3.1, i.e. ∆p = T (I)/λ: Which is more important in determining the size of price movements, T (I) or λ?

In a recent paper, Gillemot et al. [2006] have presented evidence based on several diﬀerent tests, involving comparisons of long-memory and regressions of the volatility in speciﬁc time intervals, showing that liquidity is a more important

determinant of volume. Even when one aggregates returns over a ﬁxed number of transactions (or volume) the return probability density function remains heavy tailed with properties very similar to those in ﬁxed intervals of time. A simple way to see this eﬀect is given in Figure 17, which shows the empirical probability P(|r| > x) as a function of x for the NYSE stock Procter & Gamble. Here r is the price return over a 15 minute time interval. Suppose returns are measured in transaction time, i.e. every 87 transactions rather than every 15 minutes, where 87 is chosen because it is the average number of transactions in 15 minutes (during the period from Jan 29, 2001 to December 31, 2003). The empirical distribution of transaction time returns matches that of real time returns very well. Since in this case the number of transaction is held constant, the shows that the heavy tail of the return distribution is not due to variations in the number of transactions. The same eﬀect is seen by aggregating transactions with volume rather than the number of transactions ﬁxed (see Gillemot et al. [2006] for details).

This result shows that the ﬂuctuation in number of trades or volume associated with a ﬂuctuating trading activity is not the main determinant of the heavy tails of the return distribution. To highlight this eﬀect, Figure 17 also shows the distribution of returns obtained from a surrogate distribution, constructed by randomly shuﬄing the returns of individual transactions and by aggregating them in a way that matches the number of transactions in each real time interval. In doing so the unconditional distribution of returns of individual transactions is preserved, as well as the ﬂuctuation properties of trading frequency, but any temporal correlations of individual trade returns are destroyed. The ﬁgure shows that the tail of the surrogate distribution is less heavy than the real one, indicating that ﬂuctuations and the time correlation properties of the reaction of prices to trades, i.e. liquidity, are more important than ﬂuctuations in trading frequency.

More supporting evidence for the importance of liquidity in determining volatility comes from a recent paper testing the microscopic random walk hypothesis against real data (Laspada et al. [2008]). The price dynamics can be described as a random walk in which the increments are due to individual transactions. Under the assumption that the sign and the size of the price increments are mutually independent stochastic processes, it is possible to derive an exact expression for the volatility expected in a time interval with a given number of transactions. When one tests this expression on real data, it is found that for one hour intervals the model consistently over-predicts the volatility of real price by about 70% and that this eﬀect becomes stronger as the length of the time interval increases. This fact suggests that the assumption of independence of size and sign of price changes is wrong. However data show that the contemporaneous correlation between size and sign of returns is non statistically signiﬁcant. By performing a series of shuﬄing experiments, Laspada et al. [2008] show that the discrepancy between the volatility of the model and of the data is caused by a subtle but long-memory non-contemporaneous correlation between the signs and sizes of individual returns. Therefore, even after controlling for the number of transactions

and the order imbalance in a given time interval, the random walk model has a strong bias in predicting the volatility, which is caused by the long-memory of liquidity. This once against indicats that volume is not the key factor in explaining volatility. The neglected subtle relation between return signs and sizes shows that ﬂuctuating liquidity is an important factor in explaining volatility23.

Finally, the correlation between large volumes and large returns was directly studied in Joulin et al. [2008], both for trade by trade data and for one-minute bins, with the conclusion that such a correlation is totally absent from the data.

### 8.3 Spread vs. volatility

It is worth investigating the relation between spread and volatility in the framework of the mrr model discussed above. In fact this model predicts a simple relation between volatility and impact, as can be seen from Eq. (7.16). Together with the relation between spread and impact discussed at length above, this suggests a direct link between volatility per trade and spread, which we motivate and test in this section.

By deﬁnition of the volatility per trade σ12 = E[(m +1 − m )2] and of the instantaneous impact ri,i+1 ≡ (mi+1 − mi). i, one has as an identity:24

σ12 ≡ E[ri,i2 +1]. (8.1)

The instantaneous impact ri,i+1 is expected to ﬂuctuate over time for several reasons. First, the volume of the trade, the volume in the book and the spread strongly ﬂuctuate with time (Mike and Farmer [2008], Wyart et al. [2006]). Large impact ﬂuctuations may also arise from quote revisions due to addition or cancellation of limit orders. Second, there might also be important news aﬀecting the ‘fundamental price’ of the stock. These may result in large, instantaneous jumps of the mid-point with virtually no trade at all. In order to account for both eﬀects, one may generalize the above mrr relation (Eq. 7.16) as in Bouchaud et al. [2004], Rosenow [2002], Wyart et al. [2006]:

σ12 = AR21 + Σ2, (8.2)

where R1 ≡ E[R1(v)] is the average impact after one trade, A is a coeﬃcient accounting for the variance of impact ﬂuctuations and Σ2 is the news component of the volatility (see Section 6.2). This relation holds quite precisely across different stocks of the pse, with a correlation of R2 = 0.96 (see Fig. (18)). Perhaps surprisingly, the exogenous ‘news volatility’ contribution Σ2 is found to be small.

- 23 In Section 6 we discuss how such a correlation is a consequence of the long memory of order ﬂow and of market eﬃciency. The asymmetric liquidity models described in Section 6 predict a reduction of volatility relative to what one would expect under an unconditional permanent impact model.
- 24Neglecting the extremely small drift contribution.

[Figure 149]

- Figure 18. Plot of σ12 vs. R21, showing that the linear relation Eq. (8.2) holds quite precisely with Σ2 = 0 and a ≈ 10.9. (The intercept of the best aﬃne regression is even found to be slightly negative). Data here corresponds to the 68 stocks of the pse in 2002. The correlation is very high: R2 = 0.96.

(The intercept of the best aﬃne regression is even found to be slightly negative). This could be related to the observation made in Farmer et al. [2004] that for most price jumps, some limit orders are cancelled too slowly and get ‘grabbed’ by fast market orders. This means that most of these events also contribute to the impact component R1.25 We can neglect Σ2 in the above equation; in this sense the volatility of the stocks can be mostly attributed to market activity and trade impact. This is in agreement with the conclusions of Evans and Lyons on currency markets (Evans and Lyons [2002]); see also the discussion in Bouchaud et al. [2004], Hopman [2006]).

A ﬁnal important assumption is that of universality. When the tick size is small enough and the typical number of shares traded is large enough, all stocks within the same market should behave identically up to a rescaling of the average spread and the average volume. In particular we assume that the statistics of (i) the volume of market orders (ii) the spread S and (iii) the impact R1, and the various correlations between these quantities are independent of the stock when these quantities are normalized by their average value. Empirical evidence for (at least approximate) universality can be found in Lillo et al. [2003b] and Bouchaud et al. [2002]. However, one expects that universality holds only for large cap,

25One could argue that our results simply show that the news volatility Σ itself is proportional to R1 and thus to the spread S. However, there is no reason why this should a priori be the case. For example, a model where rare jumps of typical amplitude J and probability per trade p 1 leads to Σ = √pJ, whereas the cost of such jumps, contributing to S, is pJ Σ.

small tick stocks – large tick stocks are not covered by the analysis below. Universality then implies that:

E[vS] = BE[v]E[S], E[vR1(v)] = B E[v]R1, (8.3)

where B,B are stock independent numbers. Eq. (8.3) accounts well for the Paris Stock Exchange data studied in Wyart et al. [2006], where it was found that: B ≈ 1.02 and B ≈ 1.80: the incoming volume and the spread are nearly uncorrelated, whereas the volume traded and the impact are correlated (B > 1), as expected.

Therefore, using Eq. (7.25) as an equality and Eqs. (8.2,8.3) with Σ2 = 0, we obtain the main result of this section:

E[S] = C σ1, (8.4)

where C is a stock independent numerical constant, which can be expressed using the constants introduced above as C = 2λB /

√

AB. This very simple relation between volatility per trade and average spread was noted in Bouchaud et al. [2004], Zumbach [2004], Wyart et al. [2006], and we present further data to support this conjecture. Therefore, the fact that the cost of limit and market orders should be nearly equal on average [Eqs.(7.17,7.25)] and the absence of a speciﬁc contribution of news to the volatility lead to a particularly simple relation between liquidity and volatility. As an important remark, we note that the above relation is not expected to hold for the volatility per unit time σ, since it involves an extra stock-dependent and time-dependent quantity, namely the the trading frequency f, through:

σ = σ1 f. (8.5)

The above predicted linear relation between spread and volatility per trade was tested empirically in Wyart et al. [2006] on small tick stocks. For example, the results for Paris Stock Exchange are shown in Fig. 19. One ﬁnds that Eq. (8.4) describes the data very well, with R2 values over 0.9. One can also check that there is an average intra-day pattern which is followed in close correspondence both by E[S] and σ1: spreads are larger at the opening of the market and decline throughout the day. Note that the trading frequency f increases as time elapses, which, using Eq. (8.5), explains the familiar U-shaped pattern of the volatility per unit time.

Note that there are two complementary economic interpretations of the relation σ1 ∼ S in small tick markets:

- • (i) Since the typical available liquidity in the order book is quite small, market orders tend to grab a signiﬁcant fraction of the volume at the best price; furthermore, the size of the ‘gap’ above the ask or below the bid is observed to be on the same order of magnitude as the bid-ask spread itself which therefore sets a natural scale for price variations. Hence both the impact and the volatility per trade are expected to be of the order of S, as observed.

[Figure 150]

- Figure 19. Test of Eq. (8.4) for 68 stocks from the Paris Stock Exchange in 2002, averaged over the entire year. The value of the linear regression slope is c ≈ 1.58, with R2 = 0.96

- • (ii) The relation can also be read backward as S ∼ σ1: when the volatility per trade is large, the risk of placing limit orders is large and therefore the spread widens until limit orders become favorable.

Therefore, there is a clear two-way feedback that imposes the relation σ1 ∼ S, and that can in fact lead to liquidity instabilities: large spreads create large volatilities, which in turn may open the spread more. A detailed study of such eﬀects would be highly valuable. On average, however, any deviation from the balance between spread and volatility tends to be corrected by the resulting relative ﬂow of limit and market orders. The result σ1 ∼ S therefore appears as a fundamental property of the market organization, which should be satisﬁed within any theoretical description of the micro-structure. This is an important constraint on models of order ﬂow; however, none of the simple models studied in the past (zero intelligence models Daniels et al. [2003], bounded-range models Foucault et al. [2005], Luckock [2003], Rosu [2005], or diﬀusion-reaction models Slanina [2001]) are able to predict the above structural relation between S and σ1 (see however Mike and Farmer [2008] for recent developments using a “low intelligence” model, as discussed in Section 9.3.3).

### 8.4 Market cap eﬀects

It is interesting to study the systematic dependence of the volatility and spread as a function of market capitalisation M. Across stocks, the volatility per unit time shows a systematic slow decrease with M, σ ∝ M−ϕ, where ϕ is small. The trading frequency f, on the other hand, increases with M as f ∝ Mζ. For

stocks belonging to the ftse-100, Zumbach ﬁnds ζ ≈ 0.44 (Zumbach [2004]), while for US stocks the scaling for f is less clear (Eisler and Kertecz [2006]), with apparently two regimes, one for M > 10 B$, where ζ ≈ 0.44 and the other for M < 10 B$, for which ζ ≈ 0.86. The average amount per trade vm, on the other hand, also increases with M, in such a way that f × vm is directly proportional to M. This last scaling holds with rather good accuracy and merely states that the total volume of transactions is proportional to market capitalisation, which is somewhat expected a priori. What is interesting is that this is insured by having both the frequency of trades and the volume per trade increase with M, and not, for example, the transaction frequency at ﬁxed amount per trade. The constant of proportionality is such that ∼ 10−3 of the total market cap is exchanged per day, on average, both in London and in New-York (Zumbach [2004], Eisler and Kertecz [2006]).

Combining the above two relations for the volatility per trade σ1 = σ/√f results in the following scaling law for the spread S,

ζ 2 ≈ 0.22. (8.6)

S ∼ σ1 ∝ M−ω, ω = ϕ −

The average spread therefore decreases with market capitalisation. This result is in good agreement with data from the lse, Zumbach [2004], and from the pse, Wyart et al. [2006]. It can also be directly be compared with the impact data of Lillo et al. [2003b] in the nyse, where it was established that:

v v

R1(v) ≈ M−0.3F M0.3

, (8.7)

where v is the average volume per trade for a given stock, and F a master curve that behaves approximately as a power-law with exponent b. Since spread and impact are proportional, this last result is directly comparable to Eq. (8.6). The average over v of the above result then leads to E[R1] ∼ M−ω with ω ≈ 0.3(1−b), which is in the range 0.15 − 0.25 (see section 5.1 above for a discussion of the value of b).

### 9 ORDER BOOK DYNAMICS

The previous section stresses the key role that liquidity plays in price formation. In double auction markets prices are formed in the limit order book. Thus one obvious approach to understanding liquidity is to investigate the causes of liquidity ﬂuctuations in the limit order book. Although the dynamics of liquidity is still very much an open question, several studies have identiﬁed statistical regularities in the behavior of limit order books and give some insight into the relationship between order ﬂow and liquidity.

- 9.1 Heavy tails in order placement and the shape of the order book There are several statistical regularities of limit orders placement. First of all,

- as mentioned above, limit order signs are also well described by a long memory process with an Hurst exponent very close to the one for market order signs. Lillo and Farmer [2004] reported a value of H = 0.69 for market orders and of H = 0.71 for limit orders.

Limit orders are characterized also by the limit price. The absolute value of the diﬀerence between the limit price and the best available price is a measure of the patience of the trader. Patient (impatient) traders submit limit orders very far from (close to) the spread. One of the statistical regularities recently observed in the microstructure of ﬁnancial markets is the power law distribution of limit order price in continuous double auction ﬁnancial markets (Bouchaud et al. [2002], Zovko and Farmer [2002]). Let b(t) − ∆ denote the price of a new buy limit order and a(t) + ∆ the price of a new sell limit order. Here a(t) is the best ask price and b(t) is the best sell price. The ∆ is measured at the time when the limit order is placed. It is found that ρ(∆) is very similar for buy and sell orders. Moreover for large values of ∆ the probability density function is well ﬁtted by a single power-law

ρ(∆) ∼

1 ∆1+µ

(9.1)

There is no consensus on the value of the exponent µ. Zovko and Farmer [2002] estimated the value µ = 1.5 for stocks traded at the London Stock Exchange, whereas Bouchaud et al. [2002] estimated the value µ = 0.6 for stocks traded

- at the Paris Stock Exchange. More recently Mike and Farmer [2008] ﬁtted the limit order distribution for LSE stocks with a Student’s distribution with 1.3 degrees corresponding to a value µ = 1.3. This power-law extends from 1 tick to over 100 ticks (sometimes even 1000 ticks), corresponding to a relative change of price of 5% to 50%. Such a broad distribution of limit order prices tells us that the opinion of market participants about the price of the stock in a near future could be anything from its present value to 50% above or below this value, with all intermediate possibilities. This means that market participants, quite oddly, anticipate the existence of large price jumps that would lead to trading opportunities.

A heavy tail in the distribution of relative limit price ∆ indicates that there is a large heterogeneity in the limit price, i.e. in the patience associated with each limit order. Patience is in turn related to the time scale the investor is willing to wait before her order is ﬁlled. The typical time to ﬁll26 of a limit order grows with ∆. In a recent study Lillo [2007] suggested that the origin of the heavy tails in the distribution of the relative limit price ∆ can be attributed to a heterogeneity of time scales characterizing the trading behavior of individual utility maximizers

26 The mean time to ﬁll of a limit order is inﬁnite if the price process can be approximated by a random walk. ”Typical” above means some other measure such as the median time to ﬁll.

[Figure 151]

[Figure 152]

- Figure 20. Left. Average shape of the order book. Right. Instantaneous shape of the order book.

investors, and tested this theory by using brokerage data from the LSE.

The order ﬂow and the interaction of orders determine the instantaneous state of the book Ωt. By averaging over time empirical studies consistently show that the average shape of the order book is roughly symmetric between the bid and oﬀer side of the book and is consistent across diﬀerent stocks (Bouchaud et al.

- [2002], Zovko and Farmer [2002], Mike and Farmer [2008]). They show that the maximum of the averaged book is not the best price, as shown in the left panel of Fig. 20, even though this is the most likely place for an order to be placed. In Section 9.3 we will present statistical models explaining this fact.

It is important to stress that the average shape of the book is very diﬀerent from the“typical” shape of the book. As Farmer et al. [2004] showed, for most LSE stocks the typical shape of the book is extremely sparse (see the right panel of Fig. 20). This occurs when the ratio between tick size and price is small, so that there are often many unoccupied price levels. As we discussed in Section 8.1, this fact has important consequences for the price impact of individual transactions and on the origin of large price ﬂuctuations.

### 9.2 Volume at best prices: the Glosten-Sandas model

The distribution of available volumes at the best can be ﬁtted by a gamma distribution with an exponent less than unity, meaning that the most probable value of the volume is much smaller than the average value. Both the value of the spread S and the quantity available at the bid and the ask, Φb,Φa, give information on the willingness of liquidity providers to enter a trade. One would like to understand the relation between these quantities – intuitively, large spreads are more favorable to liquidity providers and should attract larger volumes. More generally, it would be extremely interesting to have a theory for the shape of the

whole order book, i.e. the relation between the available volume and the distance from the best price.

The approach of Glosten and Sandas attempts to answer the above questions, within a framework where market orders are informed trades (Glosten [1994], Sandas [2001]). The idea is now that information is time dependent and modelled as a random variable that gives the predicted future variation of the midpoint, which we call (in conformity with the above notation) nr(n,n + ). Just before the nth trade, a liquidity provider considers the volume of the queue at the ask, Φa,n and decides to add an extra (inﬁnitesimal) limit order if its expected gain, conditional on execution, is greater than some minimum value Gmin ≥ 0. This reads:

Sn

2 − Gmin. (9.2) At this stage, Glosten and Sandas add several questionable assumptions. A crucial one is that the volume that the informed trader chooses to trade is proportional to the information he has: vn = αr(n,n+ ), independently of the shape of the book at that moment, and in particular of the available volume at the ask. He is prepared to walk up the book if necessary, which occurs with only a very small probability in practice: as discussed in Section 6.1, trading is, in fact, discretionary. Introducing the probability of information content P (r), and dropping the index n for convenience, the above conditional expectation inequality reads:

E[mn+ − mn| n = 1,vn ≥ Φa,n] ≤

+∞

rP (r)dr ≤

Φa/α

S 2 − Gmin

+∞

P (r)dr, (9.3)

Φa/α

where we have used the fact that information is assumed to be reliable, i.e. the expected mid-point change is indeed given by the informed trader prediction. In order to achieve a quantitative prediction, Sandas further assumes that P (r) has an exponential shape:27

Φa α

P (r) = βe−βr −→

+

1 β ≤

S 2

+ Gmin. (9.4)

In fact, this calculation can be reinterpreted to give the total volume of orders available Φ< at a price less or equal to p = m + S/2, and therefore makes a prediction for the shape of the order book:

Φ<(p) = α(p − m) − αGmin −

α β

, (9.5)

i.e. a linear order book with slope α and, in principle, a negative intercept. (The prediction for the buy side of the book is obvious by symmetry). Note that within

27This exponential assumption is in fact not so important. For example, a pure power-law distribution P (r) ∝ r−1−µ when r > r0 would lead to the following result instead: Φa/α ≤ (1 − µ−1)[S/2 + Gmin] (µ > 1).

this framework, the volume dependent impact of market orders is by assumption linear: R (v) = v/α, which we already know is quite a bad representation of real data, where impact is always strongly sublinear (see Section 5.1). Altogether, this model fares quite badly when compared with empirical data:

- • The order book intercept, which should be negative according to the model, is found to be positive when the model is ﬁtted to empirical data. suggesting negative costs for placing limit orders;
- • The slope α, when obtained from the slope of the order book, is found to be ten times larger than when obtained from direct impact estimates.
- • As mentioned above, the empirical shape of order books is non-monotonic, exhibiting a maximum away from the best price. This is not accounted for by the model.

The reason for such a failure is essentially that, as discussed in Section 6.1, as shown by Farmer et al. [2004], the volume of the incoming market order is in fact strongly correlated with the available volume at the best price. This is in fact why impact is sublinear in volume, and is at the heart of the liquidity game we have been detailing in the previous pages. One cannot consider that the market order ﬂow is an exogenous process to which the limit order ﬂow must adapt – rather, the two coevolve in a strongly intertwined manner.

One can however directly test Eq. (9.2) on empirical data, without any further theoretical assumptions, much as we did in the previous section. We choose

= 1,10,100 and identify a “neutral line” in the S,Φ plane separating the region (above that line) where executed limit orders are proﬁtable from a region where they are costly (see Fig. (21), and Eisler et al. [2008]). One sees that after the = 1 trade the separation line is ﬂat and is located around the value of the average spread. This means that the value of the spread is such that limit orders and markets order break even on average at high frequencies, as discussed in section 7.3. However, judged on longer time scales, the proﬁtability of a limit order behind a large preexisting order only becomes positive for spreads signiﬁcantly larger than the average. In other words, correlations between spread and volume, of the type predicted by the Glosten-Sandas model (Eq.9.2) indeed appear on longer time scales.

### 9.3 Statistical models of order ﬂow and order books

- 9.3.1 Zero intelligence models An alternative point of view is to model the order ﬂow directly as a stochastic process, decomposed into three components: market orders, addition of limit orders, and cancellation of limit orders. There is a long literature developing models of this type28. We will describe the approach of Daniels et al. [2003]

28 Examples of stochastic process models of limit order books include (Mendelson [1982], Cohen et al. [1985], Domowitz and Wang [1994], Bak et al. [1997], Bollerslev et al. [1997], Eliezer

[Figure 153]

- Figure 21. Neutral line for the proﬁtability of adding a new limit order at the best price, for three diﬀerent values of the horizon . The proﬁt is positive above and negative below the curves. The indicated time horizons are given in number of transactions. The curves were gained by averaging for the 10 most liquid stocks traded in the Paris Stock Exchange during the year 2002. Both volume and spread were normalized by their means for each stock before averaging. From Eisler et al. [2008]

(see also Smith et al. [2003]), which has the advantage that it make predictions that can be tested against real data. They assume that each elementary event is independent and concerns a ﬁxed ‘quantum’ of volume v. Buy and sell market orders are described by two Poisson processes of rate µ. Limit orders have a constant probability per unit time ρ to land anywhere they will not generate an immediate transaction, and existing limit orders have a probability ν to be cancelled. This model is of course highly schematic, since it neglects all correlations between market and limit orders, in particular, the “stimulated reﬁll” eﬀect that we argued to be so important. Another important eﬀect that is neglected is the dependence of the cancelling rate on the size of the queue: one can actually observe that the probability of cancellation decreases as the number of orders at that price increases.

A simple self-consistent argument makes it possible to estimate the size of the spread S in this model. The total ﬂux of limit orders between the mid-point and S/2 is by deﬁnition 0 S/2 d∆ρ(∆), where ∆ is the distance from the midpoint and we are allowing here for the possibility that ρ might depend on ∆. If we assume that S is suﬃciently small so that ρ is approximately constant, one ﬁnds

and Kogan [1998], Maslov [2000], Slanina [2001], Challet and Stinchcombe [2001], Daniels et al.

- [2003], Chiarella and Iori [2002], Bouchaud et al. [2002], Smith et al. [2003], Farmer et al. [2005], Mike and Farmer [2008]). See Smith et al. [2003] for a more detailed survey.

that this incoming ﬂux is ≈ ρ(0)S/2. Whenever µ > ρ(0)S/2, the rate of market order eats up the limit orders that appear within the spread completely, and the average volume present is close to zero. The cancellation term can be safely neglected if removal by market orders is more eﬃcient, i.e. when µ ν(0). But the argument breaks down when S ∼ 2µ/ρ(0), which sets the typical position of the best price, provided the tick size is small compared to S. The spread is therefore larger for larger market order rates, and smaller when the ﬂow of limit orders is larger, as expected intuitively. The above “scaling” result for the spread has been derived more quantitatively when ρ and ν are independent of ∆. One ﬁnds for the average spread:

µ ρ

E[S] =

ν µ

F(

), (9.6)

where F(u) is a monotonically increasing function that can be approximated as F(u) ≈ 0.28 + 1.86u3/4. Therefore, in the limit where cancellation can be neglected, one recovers the above result S ≈ 0.28µ/ρ(0). This prediction can be compared with empirical data by independently measuring the spread and the rates of the various processes (Farmer et al. [2005]). In view of the simplicity of the model, the agreement with data is quite good, but systematic deviations remain. In view of the importance of feedback mechanism that are neglected, this is hardly surprising.

The results above are interesting because they demonstrate that some properties of the limit order book are dictated more or less automatically by the structure of the continuous double auction itself. In particular, Equation 9.6 is an “equation of state” relating statistical properties of price formation to those of order ﬂow. This equation of state is clearly inaccurate due to the extreme assumptions that must be made to derive it. However, it has some reasonable level of empirical validity suggesting that such a relationship indeed exists for real markets. See the discussion concerning attempts to ﬁnd a more realistic equation of state in Section 9.3.3.

- 9.3.2 Statistical model of order book The above model can also explain the hump shape of the average order book. From a theoretical point of view, however, the problem is diﬃcult to handle: if one chooses a ﬁxed reference frame, the rates of incoming orders and cancellations change with the mid-point, while if one chooses the reference frame where the midpoint is ﬁxed, limit orders that are already present get shifted around. The main diﬃculty comes from the fact that the motion of the mid-point is dictated by the order ﬂow. In order to make progress, one can artiﬁcially decouple the motion of the mid-point and impose that it follows a random walk. An approximate quantitative theory of the volume in the book Φ(∆) can then be written as follows. Sell orders at distance ∆ from the current midpoint at time t are those which were placed there at a time t < t, and have survived until time t. These

orders (i) have not been cancelled; (ii) have not been crossed by the ask at any intermediate time t between t and t.

An order at distance ∆ at time t in the reference frame of the midpoint m(t) appeared in the order book at time t at a distance ∆+m(t)−m(t ). The average order book can thus be written, in the long time limit t → ∞, as

t

dt duρ(∆ + u)P (u|C(t,t ))e−ν(t−t ), (9.7)

Φst(∆) = lim

Φ(∆,t) =

t→∞

−∞

where P (u|C(t,t )) is the conditional probability that the time evolution of the price produces a given value of the mid-point diﬀerence u = m(t)−m(t ), given the condition that the path always satisﬁes ∆+m(t)−m(t ) ≥ 0 at all intermediate times t ∈ [t ,t].29 The evaluation of P requires the knowledge of the statistics of the price process, which we assume to be purely diﬀusive. In this case, P can be calculated using the method of images. One ﬁnds:

P (u|C(t,t )) =

- 1

√

- 2πDτ

u2 2Dτ − exp −

(2∆ + u)2 2Dτ

exp −

, (9.8)

where τ = t − t and D is the diﬀusion constant of the price process.

After a simple computation, one ﬁnally ﬁnds, up to a multiplicative constant which only aﬀects the overall normalisation,

∞

∆

Φst(∆) = Φ(∆,t → ∞) = e−α∆

duρ(u)e−αu,

duρ(u)sinh(αu)+sinh(α∆)

0

∆

(9.9) where α−1 = D/2ν measures the typical variation of price during the lifetime of an order ν−1.

The above formula depends on the statistics of the incoming limit order ﬂow, modeled by ρ(u). When ρ(u) = e−βu, all integrals can be perfomed explicitly and one ﬁnds:

αβ α − β

e−β∆ − e−α∆ , (9.10)

Φst(∆) = Φ0

which can easily be seen to be zero for ∆ = 0, reach a maximum and decay back to zero exponentially at large ∆. Here Φ0 is the total volume in the sell side of the book.

We have seen above that the limit order price distribution is characterized by a power law with exponent µ (see Eq. 9.1). When µ < 1, the parameter α in the above formula can be rescaled away in the limit where α−1 is much larger than the tick size (this is relevant for small tick stocks, where α−1 ∼ 10 ticks). In this

29We neglect here the ﬂuctuations of the spread. The condition should in fact read ∆+a(t)− a(t ) = ∆ + m(t) − m(t”) + (S(t) − S(t”))/2 ≥ 0.

[Figure 154]

- Figure 22. The average order book for a Poisson rate model with various choices of parameters (see Bouchaud et al. [2002]) and µ = .6. After rescaling the axes, the various results roughly fall on the same curve, which is well reproduced by the simple analytic approximation leading to Eq. (9.11), shown as the full line.

case, the shape of the average order book only depends on µ. In rescaled units δ = α∆, it is given by the following convergent integral:

Φst(∆) = e−δ

δ

duu−1−µ sinh(u) + sinh(δ)

0

∞

duu−1−µe−u. (9.11)

δ

For ∆ → 0, the average available volume vanishes in a singular way, as Φst(∆) ∝ ∆1−µ, whereas for ∆ → ∞, the average volume simply reﬂects the incoming ﬂow of orders: Φst(∆) ∝ ∆−1−µ. We have shown in Fig. 22 the average order book obtained numerically from the above Poisson model with a power-law order ﬂow, and compared it with Eq. (9.11), for various choices of parameters and µ = 0.6,

- as found for various stocks of the Paris Stock Exchange. After rescaling the two axes, the numerical models lead to very similar average order books, and the analytic approximation, although crude, appears rather eﬀective. The average shape of the order book therefore reﬂects the competition between a power-law ﬂow of limit orders with a ﬁnite lifetime, and the price dynamics that removes the orders close to the current price.

- 9.3.3 A simple empirical agent based model for liquidity ﬂuctuations We now return to discuss the problem of the relationship between order ﬂow and liquidity. The pure zero intelligence model of Daniels et al. [2003] was limited by

its extreme assumptions of Poisson processes and the use of a highly stylized simpliﬁed model for order placement. A model based on more realistic assumptions was made by Mike and Farmer [2008]. They made simple econometric models for order placement and cancellation, and showed that by simulating this model it was possible to reproduce many of the empirical features of prices, including a quantitative match for the distribution of returns and the distribution of the spread.

In Section 9.1 we discussed the remarkable heavy tails in order placement. This result applied only to orders placed inside the same best30. Mike and Farmer also studied the distribution of order prices for orders placed inside the spread or crossing the opposite best (i.e. those generating immediate transactions). Remarkably they found, in a certain sense described below, that the same power law behavior applied there as well. The frequency of order placement peaks at the same best and dies out on either side, and can be reasonably well ﬁt by a Student distribution (which has a power law tail). Under the rule that orders that cross the opposite best price are executed, this simple rule does a reasonably good job of explaining execution frequency. One of the predictions that emerges automatically is that when the spread is small it is more likely for an order to cross the opposite best, i.e. market orders become more likely. This at least partially explains the ‘stimulated reﬁll’ process mentioned earlier, since when the spread is large, orders chosen at random are more likely to fall inside the spread (and therefore accumulate in the limit order book), whereas when the spread is small executions are more likely. In fact, the model based on this relied on this eﬀect to preserve stability in the number of orders accumulating in the order book.

In this model the rate of cancellation was empirically found to depend on factors such as the number of orders in the order book, the imbalance in the order book, and the position of a given order relative to the opposite best price. Finally, it takes as an exogenous input the long-memory of order signs discussed in Section 4. When these three elements are put together (order placement, order sign and cancellation) it is possible to simulate this model, generating a time series of order books with the corresponding prices. Note that it is critical that there is feedback between price formation and the order placement process. The resulting series of prices are not eﬃcient, which is not surprising given that no eﬀort was made to make them so and there are no agents who can take advantage of ineﬃciencies.

Nonetheless, for a subset of stocks whose properties are similar to those that were used to build the model, which were called “type I” stocks, it does a good job of reproducing many of the properties of real prices31. In particular it provides

- 30 E.g. for buy orders the same best is the best bid; the power law applies to orders placed

at prices less than the best bid. The “opposite best” for buy orders is the best ask.

- 31 Type I stocks are those with reasonably low volatility and small tick size. Type II stocks

are those with high volatility, and Type III were stocks with large tick sizes. At this stage the

a good quantitative match with the distribution of returns and the distribution of the spread. This match includes not just the shape of the distributions, but their scale, including the absolute level of volatility. That is, for type I stocks a simulation of prices based on the measured parameters of the order ﬂow produces forecasts of volatility that make a good match in absolute terms, i.e. the predictions and measured values lie along the identity line. This provides further evidence for the existence of an equation of state relating order ﬂow and prices. (It remains to extend this model so that it also works well for types II and III).

To summarize, the interesting point about this model is that it suggests that volatility is directly related to fairly simple properties of the order ﬂow.

### 10 IMPACT AND OPTIMIZED EXECUTION STRATEGIES

The fact that trades impact prices is obviously detrimental to trading strategies: since, again, liquidity is so small, trades must typically be divided in small chunks and spread throughout the day. But because of impact, the price paid for the last lot is on average higher than the price for the ﬁrst lot. This poses a well deﬁned problem: what is the optimal trading proﬁle as a function of time of day, such that the average execution price is as low as possible compared to the decision price (a quantity often called ‘implementation shortfall’).

Assume that a trader has a total volume V to execute; he decides to cut his order in N trades, each of size v, with nv = V . His trading proﬁle φ(t) is such that the number of trades between t and t + dt is φ(t)dt. His own impact on the price of the stock at time t ≥ t is modeled as:

t

dtφ(t)G0(t − t)lnv, (10.1)

p(t ) − p0(t ) = P(0)

0

where G0 is the continuous time version of the single trade impact discussed in section 6.4. Using all the results obtained above, one has:

g0S fβ|t − t|β

G0(t − t ) =

, (10.2)

where g0 is a number of order unity (since impact and spread are proportional) and f the number of trades per unit time. We neglect here the possible dependence of the spread S and of f on time of day.

The total extra cost due to impact for a given proﬁle φ(t) is therefore given by:

T

dt

0

t

- 1

- 2

dt φ(t)G0(t − t )φ(t ) ≡

0

model only performs well for type I stocks.

T

dt

0

T

dt φ(t)G0(|t − t |)φ(t ), (10.3)

0

where T is the trading period (say one day). The above quantity should be minimized with the constraint that the total trading volume is ﬁxed, i.e.:

T

dtφ(t)v = V. (10.4)

0

This problem can easily solved using the method of functional derivatives with a Lagrange multiplier z to enforce the constraint. This leads to the following linear equation for the proﬁle:

T

dt G0(|t − t |)φ(t ) = z, (10.5)

0

where z is such that Eq. (10.4) is satisﬁed.

As a pedagogical example, let us assume that the impact decays exponentially as:

G0(τ) = G0 exp(−ατ) + G∞ (10.6) Thanks to the constraint Eq. (10.4), the value of G∞ can be reabsorbed in z and drops out of the computation: the permanent part of the impact is irrelevant to the optimisation of execution costs (although the resulting implementation shortfall, of course, depends on G∞). The solution of the optimisation problem then reads:

zα 2

G0φ∗(t) = zδ(t) + zδ(T − t) +

, (10.7) and the constraint is:32

1 G0

zαT 2

z 2

+

2

G0V 1 + αT/2

= V −→ z =

, (10.8)

so ﬁnally :

V 1 + αT/2

φ∗(t) =

α 2

δ(t) + δ(T − t) +

: (10.9)

the optimal proﬁle is composed of two peaks at the open and at the close of the day, and a ﬂat proﬁle in between. The ratio of the volume traded within the day to the volume traded at the open and at the close is αT/2: for a fast decaying impact (αT large), most of the volume should be spread out evenly intraday, whereas for a slowly decaying impact, trading should mostly concentrate at the open and at the close.

More generally, it can be shown that the solution to Eq. (10.5) is symmetric around T/2 and U-shaped (this is also mentioned in Hasbrouck [2007], ch. 15). In particular, when G0(τ) is given by Eq. (10.2), one ﬁnds that the optimal

32Note that the two delta functions only contribute to half of their “area” to the total volume, since they are at the edge of the integration range.

proﬁle diverges both at t = 0 and t = T, respectively as tβ−1 and (T − t)β−1. An approximate solution to Eq. (10.5) in that case reads:

Γ[2β] T2β−1Γ2[β]

tβ−1(T − t)β−1. (10.10)

φ∗(t) ≈ V

It is interesting to note that none of the parameters g0,S,f entering in the numerical evaluation of G0 appear in the shape of the proﬁle, since again these can be reabsorbed in the deﬁnition of z at an early stage of the computation.

A generic U-shape solution for the optimized execution proﬁle suggests an interesting interpretation of the observed U-shaped total traded volume as a function of the time of day.

### 11 TOWARD AN EMPIRICAL CHARACTERIZATION OF A MARKET ECOLOGY

The description of ﬁnancial markets we have depicted above is based on the assumption of the existence of diﬀerent degrees of heterogeneity among market participants. The ﬁrst level of heterogeneity is due to the existence of a broad distribution of scales among market participants. Here scale refers to any quantity that measures the typical size of the trades of an investor. Moreover the size of the hidden order determines the time horizon over which the order is worked and the number of transactions needed to complete the order.

As described in Section 3.8, the second degree of heterogeneity is due to the existence of (at least) two classes of agents acting systematically on opposite sides of the market. One group corresponds to liquidity providers and the other to liquidity takers. It would be extremely valuable to have a comprehensive empirical study that connects the heterogeneity of market participants with their strategy and with the properties of price dynamics. Unfortunately it is not easy to obtain databases containing this level of information. Some data providers are starting to release datasets containing information about the ﬁnancial institutions involved in the transaction and/or submission or cancellation of orders from the book. It is important to stress that such ﬁnancial institutions are not individual traders or agents, but rather are usually credit entities and investment ﬁrms which are members of the stock exchange and are entitled to trade at the exchange. Very often these institutions are both acting as brokers for other clients and trading for their own account. Although an institution may act on behalf of many individuals and institutions having diﬀerent strategies, recent ﬁndings show that in most cases it is possible to characterize an institution with an overall strategy, corresponding to that of the bulk of their trades. In the following two sections we present the results of two recent papers investigating the behavior of institutions in the Spanish Stock Exchange.

### 11.1 Identifying hidden orders

In a recent paper Vaglica et al. [2008] used brokerage data on transactions in the Spanish Stock Exchange to identify hidden orders and to characterize their statistical properties. The identiﬁcation of hidden orders is done by using an algorithm designed to identify segments of the inventory time series of an institution characterized by an approximately constant and statistically signiﬁcant drift term. The working hypothesis is that these segments are associated with hidden orders. A hidden order is characterized by the traded volume V , the number of transactions N, and the (real) time period T needed to complete the order33. It is found that the distribution of these quantities scale asymptotically for large values as

1 x2

P(V > x) ∼

1 x1.8

P(N > x) ∼

1 x1.3

P(T > x) ∼

. (11.1)

These relations show that the size of the hidden orders is asymptotically Pareto distributed in accordance with the hidden order model described in Section 4.3. It should be noted that the value of the exponent for V and for N is slightly larger than the value 1.5 expected by the theory described in Section 4.3 and a more careful testing of the theory is needed. The low value of the exponents indicates that the size of hidden orders is a very heterogeneous quantity, probably reﬂecting the heterogeneity of market participants. To test this hypothesis, Vaglica et al. [2008], have considered the distributional properties of hidden orders of individual brokerage codes. It is found that for the distribution of hidden order size of individual brokers is consistent with a lognormal distribution, whereas the pool of the hidden orders of all brokers is not consistent with a lognormal. This indicates that investor size heterogeneity is at the origin of the power law distribution of hidden order size.

The size variables of an hidden orders are clearly related to each other. If the volume V is large we expect that the number of transactions N and the time needed to complete the orders will also be large. The relation between the size variables reﬂects the strategic behavior chosen by the trader to work the order. By performing a principal component analysis to the hidden orders Vaglia et al. ﬁnd that

N ∼ V 1.1, T ∼ V 1.9, N ∼ T0.66. (11.2)

The fraction of variance explained by the ﬁrst eigenvalue is of the order of 88%, so these characterizations are reasonably sharp. The ﬁrst relation indicates that the number of transactions of a hidden order is roughly proportional to it size. This means that even if a trader needs to trade a large hidden order, she will not split the order in larger chunks. This observation is consistent with the empirical

33 In Vaglica et al. [2008] the investigated variables are the volume and the number of trades associated with those transactions characterizing the hidden order as a buy or a a sell hidden order.

[Figure 155]

- Figure 23. Contour plot of the correlation matrix of daily inventory variation of institutions trading the stock BBVA in 2003. This is plotted by sorting the ﬁrms in the rows and columns according to the strength of the correlation of their inventory variation with the return of the price of BBVA during the same period. Colors are chosen to highlight positive or negative ﬁrm daily inventory cross correlation values above a given signiﬁcance level. Speciﬁcally, yellow (blue) indicates positive (negative) cross correlation with a signiﬁcance of 2σ, whereas green (cyan) indicates positive (negative) cross correlation below 2σ. The thick black lines in the matrix are obtained from the bottom panel by partitioning the ﬁrms in three groups according to the value of the correlation between returns and inventory variation (smaller than −2σ, between −2σ and 2σ and larger than 2σ). Adapted from Lillo et al. [2008b].

ﬁnding that it is rare that the size of market orders is larger than the volume available at the opposite best (see Section 8.1 and Farmer et al. [2004]). The other two relations indicate that the larger the volume of the hidden order, the slower the trading rate. This result has also been veriﬁed by using other statistical hidden order detection algorithms and still needs to be properly understood. Finally it is worth noting that the relations of Eq 11.2 also hold approximately true when one considers hidden orders belonging to a single brokerage code. In other words the scaling relations of Eq. 11.2 are not the eﬀect of heterogeneity among traders.

### 11.2 Specialization of strategies

The presence of distinct classes of institutions and their mutual interaction has been investigated in a recent work by Lillo et al. [2008b]. This study clearly identiﬁes classes of institutions that are characterized by having a similar trading behavior. Speciﬁcally the study has focused on the cross correlation between the inventory variation of diﬀerent institutions. In general it is found that the cross

correlation of the inventory variation of diﬀerent institutions is often statistically signiﬁcant, for both positive and negative values. Principal component analysis reveals that the ﬁrst eigenvalue of the correlation matrix is associated with a factor that is strongly correlated with price return. To give an idea of the level of correlation of the activity between diﬀerent institutions, in Fig. 23 we show the contour plot of the correlation matrix of daily inventory variation of the institutions trading the stock BBVA in the Spanish Stock Exchange in 2003. Diﬀerent colors refer to diﬀerent levels of correlation (see caption). The institutions are sorted according to the value of the correlation of their inventory variation with the price return of BBVA. Two groups of ﬁrms are seen, one on the top left corner and the other on the bottom right corner.

The ﬁgure shows a clear block structure that makes it possible to identify communities of institutions characterized by a similar trading behavior. Speciﬁcally, the trading institutions can be partitioned in three subsets. The ﬁrst (see the bottom right corner in Fig. 23) is composed by institutions with an inventory variation positively correlated with price return, i.e. these institutions buy when the price goes up and sell when the price goes down. Moreover they are typically large institutions and have strongly autocorrelated order ﬂow, probably because of order splitting. The second subset (see the top left corner in Fig. 23) is composed of institutions whose inventory variation is negatively correlated with price return; these institutions buy when the price goes down and sell when the price goes up. The size of these institutions is very heterogeneous, as is the autocorrelation of their order ﬂow. Finally the third group is made up of uncategorized ﬁrms. As Figure 23 shows, the cross correlation between the inventory variation of an institution belonging to the ﬁrst group and an institution belonging to the second group is typically negative (blue areas in the top right and bottom left corners). This and other more direct evidence suggests that institutions belonging to these two groups are often trading counterparties.

### 12 CONCLUSIONS

In this review paper we discussed market impact on two diﬀerent, but overarching, levels. The ﬁrst level deals with ultra-high frequency scales: that of elementary transactions (a level that in physics is called “microscopic”). It is concerned with the phenomenological description and mathematical modelling of empirical observations on order ﬂow, impact, order book, bid-ask spread, etc., which are of direct interest for high frequency trading, execution and slippage control. Results on that front are surprisingly rich and to some extent unexpected. Among the most salient points, one ﬁnds that impact of individual trades is nonlinear (concave) in volume and has a nontrivial lag dependence, that can alternatively be thought of as a history-dependent impact. This is at variance with many simple models, including the famous Kyle model, where impact is assumed to be linear and permanent. The subtle temporal structure of impact can be traced back to

the long-memory in the ﬂuctuations of supply and demand. The compatibility of the long-memory in order ﬂow and the absence of predictability of asset returns has profound consequences on price formation,

The second level deals with phenomena on a longer “coarse-grained” time scale, and is more in line with the questions economists like to ask about markets and prices, such as: “Are prices in equilibrium?”, “What is the information content of these prices?”, or “Why is the volatility so high?”. Much as in physics, where the detailed understanding of the microscopic world provides invaluable insight on macroscopic phenomena, we believe that a consistent picture of the microstructure mechanisms will help put in perspective some of these traditional questions about markets and prices. From the set of results presented above, two concepts seem to emerge with possible far-reaching theoretical consequences:

- • (a) Because the outstanding liquidity of markets is always very small, trading is inherently an incremental process, and prices cannot be instantaneously in equilibrium, and cannot instantaneouly reﬂect all available information. There is nearly always a substantial oﬀset between latent oﬀer and latent demand, that only slowly gets incorporated in prices. Only on an aggregated level does one recover an approximately linear impact with a permanent component.
- • (b) On anonymous, electronic markets, there cannot be any distinction between “informed” trades and “uninformed” trades. The average impact of all trades must be the same, which means that impact must have a mechanical origin: if everything is otherwise held constant, the appearance of an extra buyer (seller) must on average move the price up (down).

The theory of rational expectations and eﬃcient markets has increasingly emphasized information and belittled the role of supply and demand, in contradiction with the intuition of traders and of the layman.34 The work we reviewed above underlines the role of ﬂuctuations in supply and demand, which may or may not be exogenous, and may or may not be informed in a traditional sense – it does not really matter. Attempts to estimate ex-post the fraction of truly informed trades leads to very small numbers, at least judged on a short time basis, meaning that the concept of informed trades is not very useful to understand what is going on in markets at high frequencies. But still, prices manage to be almost perfectly unpredictable, even on very short time scales. The conclusion is that any useful notion of information must be internal to the market: trades, order ﬂow, cancellations are information, whatever the ﬁnal cause of these events may be.

34 On this point, see the lucid discussion in Lyons [2001], from which we reproduce the following excerpt: Consider an example, one that clariﬁes how economist and practitioner worldviews diﬀer. The example is the timeworn reasoning used by practitioners to account for price movements. In the case of a price increase, practitioners will assert, “there were more buyers than sellers”. Like other economists, I smile when I hear this. I smile because in my mind the expression is tantamount to “price had to rise to balance demand and supply”.

We are aware that some of these ideas go strongly against the prevailing view in market microstructure theory, and entail a rather abrupt change of paradigm. We hope that this work will help clarify the issues and motivate further work to reconstruct a fully rigourous modelling framework, deeply rooted in the empirical data. Such data is now widely available and so abundant that it should be possible to raise the achievements of microstructure theory to the level of precision achieved in the physical sciences.

### ACKNOWLEGMENTS

We want to thank Klaus Schenk-Hoppe and Thorsten Hens for giving us the opportunity to write this review article, and for their patience. We also want to thank our collaborators on these matters, who helped us to shape our understanding of the subtle world of market microstructure and impact: R. Almgren,

- S. Ciliberti, C. Deremble, Z. Eisler, A. Gerig, L. Gillemot, E. Henry, A. Joulin, J. Kockelkoren, E. Moro, G. La Spada,Y. Lemperiere, R.N. Mantegna, S. Mike,

- A. Ponzi, M. Potters, G. Vaglica, H, Waelbroeck, J. Wieslinger, and M. Wyart. JDF gratefully acknowledges support from Bill Miller, Barclays Bank, and NSF grant HSD-0624351.

### APPENDIX 1: MECHANICAL VS. NON-MECHANICAL IMPACT

As we summarized in Section 3.4, there are two very diﬀerent views of what causes impact. The standard view is that it is essentially driven by information: the arrival of a trade signals new information, which causes market participants to update their valuations. But suppose a trade arrives that is really not based on any information? Does such a trade have a purely mechanical eﬀect on prices? If so, what is the nature of that eﬀect?

In Section 3.4 we already introduced one such notion of mechanical impact, imagining a standard market clearing framework in which agents randomly alter their excess demand functions asynchronously. As each agent alters her demand function she makes trades that generate market impact. Whether or not these are permanent depends on whether the alternations are permanent. Insofar as such alternations are permanent, the eﬀect on prices will also be permanent.

In this Appendix we examine another notion of mechanical impact for continuous double auctions. We deﬁne a mechanical impact as what happens if someone places an order in the order book if this order has no eﬀect on any future orders. We are essentially asking the question of what happens to the price if an order is injected into the order book at random, but no one pays any attention to it. We describe a method for analyzing order book data to answer this question (Farmer and Zamani [2007]). The essential result is that while there is a signiﬁcant instantaneous mechanical impact, due to the simple fact that such an order can consume the best quotes and move the midprice, but this impact decays to zero. This decay seems to follow a power law, decaying very fast initially and very

slowly later on. The reason for this decay is that orders are continually being removed from the order book, and as this happens the mechanical impact decays away. The the mechanical impact as deﬁned in this sense largely reﬂects the rate at which orders are ﬂushed out of the order book.

### 12.1 Deﬁnition of mechanical impact for order books

The following deﬁnition of mechanical impact makes the convenient simplifying assumption that the market framework is a continuous double auction. Consider the order ﬂow Ω = (ω1,ω2,...,ωt,...) consisting of individual orders ωt, which can be either new trading orders or cancellations of existing trading orders. Each individual order could be originated because of information relating to the value of the asset, or it could be originated “at random”, e.g. due a demand for liquidity driven by events having no bearing on the asset being traded.

Under the rules of the continuous double auction any initial limit order book and subsequent order ﬂow generates a unique sequence of limit order books, which correspond to a unique sequence of midprices. The auction A can be regarded as a deterministic function

bt+1 = A(bt,ωt+1)

that maps an order ωt and a limit order book bt onto a new limit order book bt+1. For a given order ﬂow Ωtt+τ = {ωt,ωt+1,...,ωt+τ} the auction A is applied to each successive order to generate the limit order book bt+τ at time t + τ,

bt+τ = Aτ(bt,Ωtt+τ).

The continuous double auction can thus be thought of as a deterministic dynamical system with initial condition b0 and exogenous input Ω.

Each limit order book bt deﬁnes a unique logarithmic midprice pt = p(bt). The midpoint price at time t + 1 can be written in term of the composition of the price operator p and the auction operator A as pt+1 = p ◦ A(bt,ωt+1). Thus, any initial limit order book bt and subsequent order ﬂow Ωtt+τ will generate a series of future prices pt+1,pt+2,...,pt+τ, where for example the last price pt+τ is

pt+τ = p ◦ Aτ(bt,Ωtt+τ). (12.1)

To give a precise meaning to mechanical impact, suppose we modify a particular order ωt and replace it by a new order ω t, while leaving the rest of the order ﬂow unaltered. Since by assumption this modiﬁcation does not aﬀect the rest of the order ﬂow, we can freely assume that it occurred for purely mechanical reasons. We can then compare the future stream of prices generated by the order ﬂow Ωtt+τ = {ωt,ωt+1,...,ωt+τ} to that generated by the altered order ﬂow Ω tt+τ = {ωt,ωt+1,...,ωt+τ}. E.g. for time t + τ, p t+τ = p ◦ Aτ(bt,Ω tt+τ).

This can be used to measure the mechanical impact of any existing order ωt by comparing the prices that are generated when ωt is present to those that

would have been generated if were were absent. We thus replace Ωtt+τ by Ω tt+τ = {0,ωt+1,...,ωt+τ}, where 0 in this case represents a null order, i.e. one that does not change the order book. We can then deﬁne the mechanical impact ∆pMτ (t) of the order ωt as

∆pMτ (t) = p ◦ Aτ(bt,Ωtt+τ) − p ◦ Aτ(bt,Ω tt++1τ). (12.2)

The real price p contains both the informational and mechanical impact of order ω, while in the hypothetical price p the mechanical impact is missing, i.e. it contains only the informational impact. Under subtraction only the mechanical impact remains. This isolates the part of the price impact that is “purely mechanical”, in the sense that it is generated solely by the eﬀect of placing an order in the book and observing its eﬀect under the deterministic operation of the continuous double auction. The information impact can be deﬁned as the portion of total impact that cannot be explained by mechanical impact, i.e.

∆pIτ = ∆pTτ − ∆pMτ ,

where ∆pTτ is the total impact. Whatever components of the total impact not explained by mechanical impact must be due to correlations between the order

ωt and other events. With the data we have it is impossible to say whether the placement of the order ωt causes changes in future events Ωt+1, or whether the properties of Ωt+1 are correlated with those of ωt due to a common cause. In either case, changes in price that are not caused mechanically must be due to information – either the information contained in ωt aﬀecting Ωt+1, or external information aﬀecting both ωt and Ωt+1. These ideas can be extended to apply to arbitrary modiﬁcations of the order stream, e.g. inﬁnitesimal modiﬁcation of order ωt, and to deﬁne mechanical generalization of elasticity (Zamani and Farmer [2008]).

### 12.2 Empirical results

This deﬁnition has been applied to several stocks in the London Stock Exchange and studied as a function of the order sequence number t (which as above simply labels the temporal sequence in which the orders are received). It is clear that the mechanical impact is highly variable. In some cases there is an initial burst of mechanical impact, which dies to zero and then remains there. In some cases there are long gaps in which the impact remains at zero and then takes on nonzero values after more than a thousand transactions. In other cases there is no mechanical impact at all.

Despite the extreme variability, when an average is taken over time a consistent pattern emerges. By deﬁnition for τ = 1 the impact is entirely mechanical, since the only order that can aﬀect the price is the reference event ωt. After τ = 1, however, the mechanical impact decays, so that on average by the time of the

0.3

0.25

|Total impact<br><br>Mechanical impact<br><br>|
|---|

0.2

PriceImpact

0.15

0.1

0.05

0

0 10 20 30 40 50 60 70 80 90 100

Event Time

- Figure 24. Average mechanical impact Et[ t∆pMτ (t)] (red squares) and total impact

Et[ t∆pTτ (t)] (blue stars), in units of the average spread, plotted as a function of number of the order sequence for the LSE stock AZN.

#### next transaction it is roughly half of its initial value, i.e. it is half of the total impact. In the limit as τ → ∞, for the stocks investigated in the LSE, to a good approximation for large τ the mechanical impact decays to zero as a power law ∆pMτ (t) ∼ τMα , with exponent αM ≈ 1.6. See the example given in Figure 24. For event time the total impact and mechanical impact are by deﬁnition the same at τ = 1. This is because in moving from τ = 0 to τ = 1 the only event that aﬀects the price is the reference event ωt – alterations in Ωt+1 cannot eﬀect ∆pT1 . For larger values of τ the mechanical impact decreases and the informational impact increases. As the example shows, over the timescale shown here (100 orders), when measured in units of the average spread, the mechanical impact is initially about 0.17, and then decays monotonically toward zero. In contrast the total impact increases toward what appears to be an asymptotically constant value slightly greater than 0.3. This the source of our statement that the initial value of mechanical impact is about half the asymptotic value of the total impact.

#### In thinking about this we should stress a few points. By requiring that any associated alterations of orders be considered information, we have taken a very strict deﬁnition of mechanical impact. Within our deﬁnition of informational there are two fundamentally diﬀerent ways in which placing or removing an order can be correlated with the placement or removal of other orders. One is that placing or removal of an order causes a change in the placement or removal of another order. The alternative, however, is that the placement or removal of the two orders are caused by the same external event, and are therefore correlated. From this point of view it can appear as if one order causes the other, simply because it happens to occur a bit earlier.

While it might be surprising that the mechanical eﬀect of order placement is completely temporary, in fact this has a trivial explanation: Once all the orders that were originally in the book when the reference order was placed, by deﬁnition all trace of the original order’s presence is gone, and so the mechanical impact is zero. Thus the power law decay of market impact that is a observed for mechanical impact is just a reﬂection of the rate at which orders turn over in the order book, and is not related to the decay of the total impact discussed in section 6.

### APPENDIX 2: VOLUME FLUCTUATIONS

How should one take into account volume ﬂuctuations in the formalism developed in Section 6.4? Since the volume of trades v is rather broadly distributed, the impact of trades could itself be highly ﬂuctuating as well. This is not so, because large trade volumes mostly occur when a comparable volume is available at the opposite best price, in such a way that the impact of large trades is in fact quite similar to that of small trades. Mathematically, we have seen that the average impact is a slow power law function vψ, or even a logarithm log v. As a simplifying limit, we postulate an logarithmic impact and a broad, log-normal distribution of v. The resulting impact of the nth trade qn = n lnvn is then a (zero mean) Gaussian random variable, which inherits long range correlations from the sign process. Suppose, as in the mrr model, that only the surprise in qn moves the price – this insures by construction that the price returns are uncorrelated. An elegant way to write this down mathematically is to express the (correlated) Gaussian variables qn in terms of a set of auxiliary uncorrelated Gaussian variables ηm, through:

K(n − m)ηm, E[ηmηm+ ] = δ ,0 (12.3)

qn =

m≤n

where K(.) a certain kernel such that the qn have the required correlations:35 C = E[qnqn+ ] ≡

K(m + n)K(m). (12.4)

m≥0

In the case where C decays as c0 −γ with 0 < γ < 1, it is easy to show that the asymptotic decay of K(n) should also be a power-law k0n−δ with 2δ − 1 = γ and k02 = c0Γ(δ)/Γ(γ)Γ(1 − δ). Note that 1/2 < δ < 1. Inverting Eq. (12.3) leads to:

Q(n − m)qm, (12.5)

ηn =

m≤n

35The following equation can be uniquely solved to extract K( ) from C , using the so-called Levinson-Durbin algorithm for solving Toepliz systems (see e.g. Percival [1992]).

where Q is the matrix inverse of K, such that m=0 K( −m)Q(m) = δ ,0. For a power-law kernel K(n) ∼ k0n−δ, one obtains Q(n) ∼ (δ−1)sinπδ/(πk0)nδ−2 < 0 for large n. Note that whenever δ < 1, one can show that ∞m=0 Q(m) ≡ 0.

When all qm,m ≤ n − 1 are known, the corresponding ξm,m ≤ n − 1 can be computed; the predicted value of the yet unobserved qn is then given by:

En−1[qn] =

and the surprise in qn is simply:

K(n − m)ηm, (12.6)

m<n

qn − En−1[qn] = K(0)ηn. (12.7) The generalization of the price equation of motion [Eq. (7.9)] is therefore:

mn+1 − mn = ξn + θK(0)ηn, (12.8)

which, again by construction, removes any predictability in the price returns. From this equation of motion one can derive G0( ) and R .36 From the expression of the ηs in terms of the qs, one ﬁnds:

G0( ) ≡ θK(0)

m=0

∞

−1

Q(m) = −θK(0)

m=

Q(m). (12.9)

Using the above asymptotic estimate of Q(.),we ﬁnally obtain

sin(πδ)K(0) πk0

G0( ) ∼ 1 θ

δ−1 ≡ Γ0 −β. (12.10)

Identifying the exponents leads to β = 1 − δ = 1 − γ/2, recovering the above equality. The quantity θ, relating surprise in order ﬂow to price changes, measures the so-called “information content” of the trades. It can be measured from empirical data using the above relation between prefactors.

Finally, from Eq.(12.8), one ﬁnds the full impact function: R = E[(mn+ − mn)qn] = θK(0)2, ∀ (12.11)

i.e. a completely ﬂat impact function, independent of , as in the simpliﬁed mrr model decribed above. However, if we assume with mrr that the fundamental price, rather than the midpoint, is impacted by the surprise in qn, we ﬁnd that the full impact function is again given by Eq. (7.10): R = θ[1 − C ], which increases with .

36We now deﬁne G0 as the impact of the q’s on the price.

### APPENDIX 3: THE BID-ASK SPREAD IN THE MRR MODEL

- A complementary point of view to that given in the main text is to analyze the cost of limit orders within the mrr model. The following argument is interesting because it can be, in essence, generalized to more complex cases as well. Suppose one wants to trade at a random instant in time. Compared to the initial midpoint value, the average execution cost of an inﬁnitesimal buy limit order is given by:

CL =

- 1

- 2 −

S 2

+

- 1

- 2 R1 + CL+ : (12.12)

with probability 1/2, the order is executed right away, S/2 below the mid-point; otherwise, the mid-point moves on average by a quantity R1, to which must be added the cost of a limit order conditioned to the last trade being a buy, CL+, for which a similar equation can be obtained:

CL+ =

- 1 − ρ

- 2 −

S 2

+

- 1 + ρ

- 2 R+1 + CL++ , (12.13)

with obvious notations. Since the mrr model is Markovian, one has R+1 = R1 and CL++ = CL+, so that:

CL+ = −

S 2

+

1 + ρ 1 − ρR1. (12.14)

Plugging this last relation in Eq. (12.12), we ﬁnally ﬁnd:

CL = −

S 2

+

1 1 − ρR1. (12.15)

Imposing that CL ≡ 0, one recovers the mrr relation between the spread and the asymptotic impact (see Eq. 7.16).

BIBLIOGRAPHY

*Bibliography

- R. Almgren, C. Thum, H. L. Hauptmann, and H. Li. Equity market impact. Risk, July, 2005.

T. Ane and H. Geman. Order ﬂow, transaction clock, and normality of asset returns. The Journal of Finance, 55(5):2259–2284, 2000.

P. Bak, M. Paczuski, and M. Shubik. Price variations in a stock market with many agents. Physica A-Statistical Mechanics and Its Applications, 246(3-4): 430–453, 1997.

- B. M. Barber, Y.-T. Lee, Y.-J. Liu, and T. Odean. Do individual day traders make money? evidence from taiwan. Technical report, U.C. Davis, 2004.

M. J. Barclay and J. B. Warner. Stealth trading and volatility. Journal of Financial Economics, 34:281–305, 1993.

J. Beran. Statistics for Long-Memory Processes. Chapman & Hall, New York, 1994.

- H. Bessembinder. Issues in assessing trade execution costs. Journal of Financial Markets, 6(3):233–257, 2003.

- B. Biais, T. Foucault, and P. Hillion. Microstructure des marches ﬁnanciers. Presses Universitaires de France. 1997.

F. Black. Towards a fully automated exchange. Review of Financial Analysts, 27:29, 1971.

- F. Black. Noise. Journal of Finance, 41(3):529–543, 1986. T. Bollerslev, I. Domowitz, and J. Wang. Order ﬂow and the bid-ask spread:

An empirical probability model of screen-based trading. Journal of Economic Dynamics and Control, 21(8-9):1471–1491, 1997.

J.-P. Bouchaud and R. Cont. A langevin approach to stock market ﬂuctuations and crashes. European Physics Journal B, 6:543–550, 1998.

J.-P. Bouchaud, Y. Gefen, M. Potters, and M. Wyart. Fluctuations and response in ﬁnancial markets: The subtle nature of “random” price changes. Quantitative Finance, 4(2):176–190, 2004.

J.-P. Bouchaud, J. Kockelkoren, and M. Potters. Random walks, liquidity molasses and critical response in ﬁnancial markets. Quantitative Finance, 6(2): 115–123, 2006.

J.-P. Bouchaud, M. Mezard, and M. Potters. Statistical properties of the stock order books: empirical results and models. Quantitative Finance, 2(4):251–256, 2002.

- J. Y. Campbell and R. J. Shiller. The dividend-price ratio and expectations of future dividends and discount factors. Review of Financial Studies, 1(3): 195–228, 1989.

M. Casdagli, S. Eubank, J. D. Farmer, and J. Gibson. State space reconstruction in the presence of noise. Physica D, 51:52–98, 1991. D. Challet. So you are making money in ﬁnancial markets. should you tell your friends how? Technical report, 2007. D. Challet and R. Stinchcombe. Analyzing and modeling 1+1d markets. Physica A, 300(1-2):285–299, 2001. L. K. Chan and J. Lakonishok. Institutional trades and intraday stock price behavior. Journal of Financial Economics, 33:173–199, 1993. L. K. Chan and J. Lakonishok. The behavior of stock prices around institutional trades. The Journal of Finance, 50(4):1147–1174, 1995. C. Chiarella and G. Iori. A simulation analysis of the microstructure of double auction markets. Quantitative Finance, 2:346–353, 2002. T. Chordia and A. Subrahmanyam. Order imbalance and individual stock returns: Theory and evidence. Journal of Financial Markets, 72:485–518, 2004. P. K. Clark. Subordinated stochastic process model with ﬁnite variance for speculative prices. Econometrica, 41(1):135–155, 1973.

- K. J. Cohen, R. M. Conroy, and S. F. Maier. Order ﬂow and the quality of the

market. In Y. Amihud, T. Ho, and R. A. Schwartz, editors, Market Making and the Changing Structure of the Securities Industry, pages 93–110. Rowman & Littleﬁeld, Lanham, 1985.

P. Curty and M. Marsili. Phase coexistence in a forecasting game Journal of Statistical Mechanics, P03013, 2006.

- D. M. Cutler, J. M. Poterba, and L. H. Summers. What moves stock prices? The Journal of Portfolio Management, 15(3):4–12, 1989.

M. G. Daniels, J. D. Farmer, L. Gillemot, G. Iori, and D. E. Smith. Quantitative model of price diﬀusion and market friction based on trading as a mechanistic random process. Physical Review Letters, 90(10):108102–108104, 2003.

J. B. Delong, A. Shleifer, L. H. Summers, and R. J. Waldmann. Positive feedback and destabilizing rational speculation. Journal of Finance, 45:379–395, 1990.

Z. Ding, C. W. J. Granger, and R. F. Engle. A long memory property of stock returns and a new model. Journal of Empirical Finance, 1(1):83–106, 1993.

- I. Domowitz and J. Wang. Auctions as algorithms: computerized trade execution and price discovery. Journal of Economic Dynamics and Control, 18(1):29–60, 1994.

Z. Eisler, J.-P. Bouchaud, and J. Kockelkoren. Technical report, 2008. in preparation. Z. Eisler and J. Kertecz. Size matters, some stylized facts of the market revisited. European Journal of Physics, B51:145–154, 2006.

D. Eliezer and I. I. Kogan. Scaling laws for the market microstructure of the interdealer broker markets. Technical report, http://www.arxiv.org/abs/condmat/9808240, 1998.

- R. Engle and J. Rangel. The spline GARCH model for unconditioanl volatlity and its global macroeconomic causes. Technical report, NYU and UCSD, 2005.

- M. D. D. Evans and R. K. Lyons. Order ﬂow and exchange rate dynamics. Journal of Political Economy, 110(1):170–180, 2002.

- J. Farmer, A. Gerig, F. Lillo, and S. Mike. Market eﬃciency and the long-memory of supply and demand: Is price impact variable and permanent or ﬁxed and temporary? Quantitative Finance, 6(2):107–112, 2006.

J. D. Farmer. Market force, ecology and evolution. Industrial and Corporate Change, 11(5):895–953, 2002. J. D. Farmer, L. Gillemot, F. Lillo, S. Mike, and A. Sen. What really causes large price changes? Quantitative Finance, 4(4):383–397, 2004. J. D. Farmer and F. Lillo. On the origin of power laws in ﬁnancial markets. Quantitative Finance, 314:7–10, 2004.

J. D. Farmer, P. Patelli, and I. Zovko. The predictive power of zero intelligence in ﬁnancial markets. Proceedings of the National Academy of Sciences of the United States of America, 102(6):2254–2259, 2005.

J. D. Farmer and N. Zamani. Mechanical vs. informational components of price impact. European Physical Journal B., 55:1899–2000., 2007.

- F. M. Fisher. Disequilibrium Foundations of Equilibrium Economics. Cambridge

University Press, Cambridge, 1983. T. Foucault, O. Kadan, and E. Kandel. Limit order book as a market for liquidity. The Review of Financial Studies, 18(4):1171–1217, 2005.

X. Gabaix, P. Gopikrishnan, V. Plerou, and H. Stanley. Institutional investors and stock market volatility. Quarterly Journal of Economics, 121:461–504, 2006.

X. Gabaix, P. Gopikrishnan, V. Plerou, and H. E. Stanley. A theory of power-law distributions in ﬁnancial market ﬂuctuations. Nature, 423:267–270, 2003. D. Gallagher and A. Looi. Trading behavior and the performance of daily institutional trades. Accounting and Finance, 46:125–147, 2006. A. Gerig. A Theory for Market Impact: How Order Flow Aﬀects Stock Price. PhD thesis, University of Illinois, 2007.

- L. Gillemot, J. D. Farmer, and F. Lillo. There’s more to volatility than volume. Quantitative Finance, 6(5):371–384, 2006.

L. Glosten. Is the electronic limit order book inevitable? Journal of Finance, 49

(4):1127–1161, 1994.

L. R. Glosten and P. R. Milgrom. Bid, ask, and transaction prices in a specialist market with heterogeneously informed traders. Journal of Financial Economics, 14(1):71–100, 1985.

P. Gopikrishnan, M. Meyer, L. Amaral, and H. Stanley. Inverse cubic law for the probability distribution of stock price variations. European Physical Journal

- B., 3:139–140, 1998.

P. Gopikrishnan, V. Plerou, X. Gabaix, and H. E. Stanley. Statistical properties of share volume traded in ﬁnancial markets. Physical Review E, 62(4):R4493– R4496, 2000. Part A.

- C. W. J. Granger and R. Joyeux. An introduction to long-range time series models and fractional diﬀerencing. Journal of Time Series Analysis, 1:15–30, 1980.

- S. J. Grossman. The Informational Role of Prices. MIT Press, Cambridge, 1989.

- S. J. Grossman and J. E. Stiglitz. On the impossibility of informationally eﬃcient markets. The American Economic Review, 70(3):393–408, 1980.

- G.-F. Gu, W. Chen, and W.-X. Zhou. Quantifying bid-ask spreads in the Chinese stock market using limit-order book data - Intraday pattern, probability distribution, long memory, and multifractal nature European Physical Journal

- B 57:81-87, 2007.

- O. Guedj and J.-P. Bouchaud. Experts earnings forecasts: Bias, herding and gossamer information. International Journal of Theoretical and Applied Finance, 8:933, 2005.
- P. Handa and R. A. Schwartz. Limit order trading. Journal of Finance, 51(5): 1835–61, 1996.

L. Harris and J. Hasbrouck. Market vs. limit orders: The superdot evidence and order submission strategy. The Journal of Financial and Quantitative Financial Analysis, 31(2):213–231, 1996.

J. Hasbrouck. Trades, quotes, inventories, and information. Journal of Financial Economics, 22(2):229–52, 1988. J. Hasbrouck. Empirical market microstructure: The institutions, economics and econometrics of securities trading. Oxford University Press, Oxford, 2007.

- C. Hopman. Do supply and demand drive stock prices? Quantitative Finance,

2006. To appear. J. R. M. Hosking. Fractional diﬀerencing. Biometrika, 68:165–176, 1981. A. Joulin, A. Lefevre, D. Grunberg, and J.-P. Bouchaud. Stock price jumps:

news and volume play a minor role. Technical report, 2008.

- D. B. Keim and A. Madhavan. The upstairs market for large-block transactions:analysis and measurement of price eﬀects. The Review of Financial Studies, 9(1):1–36, 1996.

- A. Kempf and O. Korn. Market depth and order size. Journal of Financial Markets, 2(1):29–48, 1999.

- A. S. Kyle. Continuous auctions and insider trading. Econometrica, 53:1315– 1335, 1985.

G. La Spada, J. D. Farmer, and F. Lillo. The non-trivial random walk of stock prices. European Journal of Physics, B., 2008. To appear.

- B. LeBaron and R. Yamamoto. Long-memory in an order-driven market. Physica A, 383:85–89, 2007.

F. Lillo. Limit order placement as an utility maximization problem and the origin of power law distribution of limit order prices. European Journal of Physics, 55:453–459, 2007.

F. Lillo and J. D. Farmer. The long memory of the eﬃcient market. Studies in Nonlinear Dynamics & Econometrics, 8(3), 2004.

F. Lillo and J. D. Farmer. The key role of liquidity ﬂuctuations in determining large price ﬂuctuations. Fluctuations and Noise Letters, 5:L209–L216, 2005. F. Lillo, J. D. Farmer, and G. A. A theory for aggregate market impact. Technical

report, Santa Fe Institute, 2008a. Unpublished research. F. Lillo, J. D. Farmer, and R. N. Mantegna. Master curve for price impact function. Nature, 421:129–130, 2003b. F. Lillo and R. N. Mantegna. Power-law relaxation in a complex system: Omori law after a ﬁnancial market crash. Physical Review E, 68(1), 2003. Part 2. F. Lillo, S. Mike, and J. D. Farmer. Theory for long memory in supply and demand. Physical Review E, 7106(6):066122, 2005.

F. Lillo, E. Moro, G. Vaglica, and R. Mantegna. Specialization and herding behavior of trading ﬁrms in a ﬁnancial market. New Journal of Physics, 10: 043019, 2008b.

- A. W. Lo. Long-term memory in stock market prices. Econometrica, 59(5): 1279–1313, 1991.

I. N. Lobato and C. Velasco. Long-memory in stock-market trading volume. Journal of Business & Economic Statistics, 18:410–427, 2000.

- H. Luckock. A steady-state model of the continuous double auction. Quantitative

Finance, 39:385–404, 2003.

- T. Lux. The stable paretian hypothesis and the frequency of large returns: an examination of major german stocks. Applied Financial Economics, 6(6):463– 475, 1996.

- R. Lyons. The microstructure approach to foreign exchange rates. MIT Press, Cambridge, MA, 2001.

Madhavan. Market microstructure: A survey. Journal of Financial Markets, 3: 205, 2000.

- A. Madhavan, M. Richardson, and M. Roomans. Why do security prices change? a transaction-level analysis of nyse stocks. The Review of Financial Studies, 10(4):1035–1064, 1997.
- B. Mandelbrot. The variation of certain speculative prices. The Journal of Business, 36(4):394–419, 1963.

B. Mandelbrot and J. W. van Ness. Fractional brownian motions, fractional noises and applications. SIAM Review, 10(4):422–437, 1968. B. B. Mandelbrot and H. M. Taylor. On distribution of stock price diﬀerences. Operations Research, 15(6):1057–1062, 1967.

- S. Maslov. Simple model of a limit order-driven market. Physica A-Statistical Mechanics and Its Applications, 278(3-4):571–578, 2000.

- H. Mendelson. Market behavior in a clearing house. Econometrica, 50(6):1505– 1524, 1982.

- S. Mike and J. Farmer. An empirical behavioral model of liquidity and volatility. Journal of Economic Dynamics and Control, 32:200–234, 2008.

P. Milgrom and N. Stokey. Information trade and common knowledge. Journal of Economic Theory, 26(1):17–27, 1982.

- T. Odean. Do investors trade too much? The American Economic Review, 89

(5):1279–1298, 1999.

- M. O’Hara. Market Microstructure Theory. Blackwell, Cambridge, 1995.
- N. H. Packard, J. P. Crutchﬁeld, J. D. Farmer, and R. S. Shaw. Geometry from a time seriees. Physical Review Letters, 45(9):712–716, 1980.

- D. Percival. Simulating gaussian random processes with speciﬁed spectra. Computing Science and Statistics, 24:534, 1992.

V. Plerou, P. Gopikrishnan, X. Gabaix, and H. E. Stanley. Quantifying stock price response to demand ﬂuctuations. Physical Review E, 66(2):article no. 027104, 2002.

V. Plerou, P. Gopikrishnan, X. Gabaix, and H. E. Stanley. On the origin of power laws in ﬁnancial markets. Quantitative Finance, 4:11–15, 2004.

V. Plerou, P. Gopikrishnan, and H. Stanley. Quantifying ﬂuctuations in market liquidity: Analysis of the bid-ask spread. Physical Review E., 71:046131–9, 2005.

- A. Ponzi, F. Lillo, and R. Mantegna. Market reaction to temporary liquidity crises and the permanent market impact. preprint at arXiv:physics/0608032v1.

- R. Roll. Orange juice and weather. American Economic Review, pages 861–880,

1984.

- B. Rosenow. Fluctuations and market friction in ﬁnancial trading. International Journal of Modern Physics C, 13(3):419–425, 2002.

- S. Ross. Neoclassical Finance. Princeton University Press, 2004.

- I. Rosu. A dynamic model of the limit order book. Technical report, 2005. P. Sandas. Adverse selection and comparative market making:empirical evidence

from a limit order market. The Review of Financial Studies, 14(3):705–734, 2001.

- J. K. Sebenius and J. Geanakoplos. Dont bet on it - contingent agreements with asymmetric information. Journal of the American Statistical Association, 78

(382):424–426, 1983. R. J. Shiller. Do stock prices move too much to be justiﬁed by subsequent changes in dividends? American Economic Review, 71(3):421–436, 1981. A. Shleifer. Clarendon Lectures: Ineﬃcient Markets. Oxford University Press, Oxford, 2000.

- F. Slanina. Mean-ﬁeld approximation for a limit order driven market model. Physical Review E, 64(5):article no.056136, 2001. Part 2.

- E. Smith, J. D. Farmer, L. Gillemot, and S. Krishnamurthy. Statistical theory of the continuous double auction. Quantitative Finance, 3(6):481–514, 2003.

- H. Stoll. Friction. Journal of Finance, 55:1479, 2000.

- H. R. Stoll. The supply of dealer services in securities markets. Journal of Finance, 33(4):1133–51, 1978.

F. Takens. Detecting strange attractors in turbulence. In D. Rand and L.-S. Young, editors, Dynamical Systems and Turbulence, volume 898, pages 366–

381. Springer-Verlag, Berlin, 1981.

N. Torre. BARRA Market Impact Model Handbook. BARRA Inc., Berkeley, 1997. G. Vaglica, F. Lillo, E. Moro, and R. Mantegna. Scaling laws of strategic behavior

and size heterogeneity in agent dynamics. Physical Review E., 77:0036110, 2008.

P. Weber and B. Rosenow. Order book approach to price impact. Quantitative Finance, 5:357–364, 2005. P. Weber and B. Rosenow. Large stock price changes: volume or liquidity? Quantitative Finance, 6(1):7–14, 2006. Z. Wiesinger, Z. Eisler, A. Joulin, and J.-P. Bouchaud. Technical report, 2008. In preparation.

- M. Wyart, J.-P. Bouchaud, J. Kockelkoren, M. Potters, and M. Vettorazzo. Relation between bid-ask spread, impact and volatility in double auction markets. Technical report, 2006.
- N. Zamani and J. D. Farmer. Decomposition of mechanical and informational components of orderﬂow. Technical report, Unﬁnished manuscript, 2008.

A. Zawadowski, G. Andor, and J. Kertecz. Short-term market reaction after extreme price changes of liquid stocks. Quantitative Finance, 4:283–295, 2006.

- I. Zovko and J. D. Farmer. The power of patience; a behavioral regularity in

limit order placement. Quantitative Finance, 2(5):387–392, 2002.

- I. Zovko and J. D. Farmer. Correlations and clustering in the trading of members of the London Stock Exchange. In S. Abe, T. Mie, H. Herrmann, P. Quarati, A. Rapisarda, and C. Tsallis, editors, Complexity, Metastability and Nonextensivity: An International Conference, AIP Conference Proceedings. Springer, 2007.

- G. Zumbach. How the trading activity scales with the company sizes in the ftse

100. Quantitative Finance, 4:441, 2004.

