# Testing Asymmetric-Information Asset Pricing Models∗

Bryan Kelly New York University

Alexander Ljungqvist New York University and CEPR

January 8, 2009

Abstract

We test models of asset pricing under asymmetric information using plausibly exogenous variation in the supply of information caused by the closure or restructuring of brokerage ﬁrms’ research operations. Consistent with predictions derived from a Grossman and Stiglitz-type model, share prices and uninformed investors’ demands fall as information asymmetry increases. Cross-sectional tests support the comparative statics. Prices and uninformed demand experience larger declines, the more investors are uninformed, the larger and more variable is turnover, the more uncertain is the asset’s payoﬀ, and the noisier is the better-informed investors’ signal. We show that prices fall because expected returns become more sensitive to a liquidity-risk factor.

∗We thank Anat Admati and Brad Barber as well as seminar audiences at Columbia GSB for helpful suggestions. We are grateful to Stephen Brown of Emory University for sharing his PIN data and to Ashwani Kaul and Rajiv Kumar at Reuters Estimates for generous help in assembling parts of our dataset. All errors are our own. Address for correspondence: Stern School of Business, New York University, 44 West Fourth Street, New York NY 10012-1126. Kelly: Phone 212-998-0368; e-mail bkelly@stern.nyu.edu. Ljungqvist: Phone 212-998-0304; fax 212-995-4220; e-mail al75@nyu.edu.

The aim of the paper is to empirically examine the fundamental driving forces of asset pricing

models under asymmetric information. These are typically noisy rational expectations equilibrium

models in which some investors are better informed than others. In equilibrium, prices reveal

informed investors’ superior information only partially due to the presence of noise in the form of

random supply of the risky asset. Random supply might reﬂect ‘noise traders’ whose demands are

independent of information. Prominent examples of such models include Grossman and Stiglitz

(1980), Hellwig (1980), Admati (1985), Wang (1993), and Easley and O’Hara (2004).

To derive empirical predictions representative of these models, Section I adapts the Grossman

and Stiglitz model to show that an increase in information asymmetry leads, not surprisingly, to

a fall in share price and a reduction in uninformed investors’ demand for the risky asset. Simple

expressions for equilibrium prices reveal that the channel linking information asymmetry and price

is liquidity risk: Price falls because the asset’s exposure to liquidity risk increases. The model’s

comparative statics relate the changes in price and demand to the fraction of investors who are

better informed, the supply and liquidity of the asset, the uncertainty about the asset’s payoﬀ, and

the noisiness of the better-informed investors’ signal.

Testing a model of asset pricing with asymmetric information poses a tricky identiﬁcation chal-

lenge. Imagine regressing the change in investor demand on the change in a proxy for information

asymmetry, such as the stock’s bid-ask spread. Interpreting the coeﬃcient would be hard if, as is

likely, there are omitted variables (such as changes in the riskiness of the company’s cash ﬂows)

which simultaneously aﬀect spreads and demand. Another problem is reverse causality. Spreads

may increase precisely because uninformed demand is expected to fall. To overcome simultaneity,

we need an instrument for the degree of information asymmetry in the asset market.

The Grossman and Stiglitz model and its descendants suggest what such an instrument might

1

look like: An exogenous change in the cost of information about an asset’s payoﬀs. These models

demonstrate how an increase in information cost will increase information asymmetry by inducing

fewer investors to purchase information. Exogeneity means, in this case, that the change in infor-

mation cost must aﬀect prices and demands only via its eﬀect on the asymmetry of information.

Cost changes would have to be independent of all other underlying determinants of asset prices and

demands, particularly the asset’s future payoﬀs.

Equity research analysts are among the most inﬂuential information producers in ﬁnancial

markets. We argue that their presence or absence aﬀects the extent of information asymmetry.

Suppose investors are heterogenous in their information costs. All those whose costs exceed the

price at which an analyst sells his research will purchase it. If the analyst were to stop selling

research, investors would have to fall back on alternative information sources, and for some, the

cost of becoming informed would exceed the beneﬁt. (For instance, hedge funds or mutual funds

likely have relatively low-cost substitute information sources, but retail investors presumably do

not.) Thus, information asymmetry would increase.

Consider the extreme case of a market in which each stock is covered by exactly one analyst.

The ideal experiment would be to randomly ban analysts from researching some stocks. Because

the cost of information substitutes for buyers of analyst research must (weakly) exceed the analyst’s

asking price, the average cost of information will increase for the stocks that randomly lose research,

and information asymmetry will increase as a result. An econometrician could then measure the

eﬀect of information asymmetry on equilibrium asset prices and investor demands.

Our empirical approach is to identify a quasi-experiment of this nature. We compile a list of

events in which brokerage ﬁrms terminated research coverage of large sets of stocks. Coverage ter-

minations will qualify as a valid instrument if they satisfy two conditions. First, they must correlate

with an increase in information asymmetry. This will result if information costs are heterogeneous,

- as we have argued. Second, they must aﬀect price and demand only through their eﬀect on infor-

mation asymmetry. Most coverage terminations do not satisfy this exclusion restriction. Instead,

they typically reﬂect a negative change in the analyst’s view of the company’s future prospects and

so are endogenous (McNichols and O’Brien (1997)). However, we are able to identify a subset of

14,939 coverage terminations over the period 2000-2005 that are plausibly exogenous in the sense

that they result from closures or downsizing of brokerage ﬁrms’ research operations, rather than

an analyst’s decision to selectively drop coverage on some stocks but continue it on others.1 We

discuss the exogenous shocks that led to this restructuring in Section II, where we also show that

sample terminations correlate with increases in information asymmetry while passing various tests

of the exclusion restriction, as required for exogeneity.2,3

We test the model’s predictions in Section III. As predicted, both price and uninformed demand

fall following a coverage termination. Cumulative abnormal returns average between −51 and

−56 basis points on the day of an exogenous coverage termination, depending on the benchmark.

Institutional investors—which are more likely to be better informed—increase their holdings of

aﬀected stocks while retail investors—who are more likely to be uninformed—sell. Cross-sectional

tests support the comparative statics. Prices and uninformed demand experience larger declines,

the more investors are uninformed, the larger and more variable is turnover, the more uncertain

is the asset’s payoﬀ, and the noisier is the signal. Finally, using standard empirical models of

- 1Coverage terminations should not be confused with ‘stopped coverage.’ The latter is a temporary suspension of coverage and occurs most frequently when a subject of coverage raises capital with the brokerage ﬁrm’s help.
- 2Our instrument is similar in spirit to Hong and Kacperczyk’s (2007). Like us, these authors exploit exogenous variation in coverage (in their case, variation due to mergers among brokerage ﬁrms with overlapping coverage universes), though their focus is diﬀerent. Their main ﬁnding is that reduced coverage leads to more optimistic earnings forecasts as competition among analysts decreases.
- 3We are interested in coverage terminations purely as an instrument with which to identify changes in the supply of information. For studies focusing on terminations per se, see Khorana, Mola, and Rau (2007), Scherbina (2008), Kecskes and Womack (2007), and Ellul and Panayides (2007). Each of these papers uses endogenous terminations.

expected returns, we show that the loading on a factor proxying for liquidity risk increases following

exogenous coverage terminations. This supports the liquidity-risk channel of the model.

Our tests contribute to the literature by providing direct evidence of the role of asymmetric

information in asset pricing. With one notable exception, discussed below, the literature has mainly

focused on the role of liquidity in asset pricing, perhaps because liquidity is considerably easier to

measure than information asymmetry. Relevant empirical studies include Pastor and Stambaugh

(2003), Amihud and Mendelson (1986), Amihud (2002), Hasbrouck and Seppi (2001), Bekaert,

Harvey, and Lundblad (2007), Jones (2002), and Eleswarapu (1997). Following theoretical models

such as Amihud and Mendelson (1986), Acharya and Pedersen (2005), and Huang (2003), these

studies treat liquidity as exogenous. Our ﬁndings suggest that liquidity varies with information

asymmetry, consistent with microstructure models such as Kyle (1985) and Glosten and Milgrom

(1985). Thus, one fundamental driver of asset prices appears to be information asymmetry, con-

sistent with models such as Grossman and Stiglitz (1980), Hellwig (1980), Admati (1985), Wang

(1993), and Easley and O’Hara (2004).

The notable exception is the empirical literature that uses Easley and O’Hara’s (1992) PIN

measure to proxy for information asymmetry. PIN is based on the idea that the presence of privately

informed traders can be noisily inferred from order ﬂow imbalances. Easley et al. (1996) show that

PIN correlates with measures of liquidity such as bid-ask spreads, while Easley, Hvidkjær, and

O’Hara (2002) ﬁnd that PIN aﬀects expected returns.4 The advantage of our approach relative to

this literature is that it exploits exogenous variation in information asymmetry rather than relying

on a proxy for information asymmetry whose potential correlations with unobserved variables are

unknown.

4PIN is controversial. Mohanram and Rajgopal (2006) ﬁnd that PIN is not priced beyond Easley et al.’s (2002) sample period. Duarte and Young (2008) show that PIN is only priced to the extent that it proxies for illiquidity.

## I. The Model

The setup follows Grossman and Stiglitz (1980). There is a unit mass of investors who have identical

initial wealth, W0, and are risk-averse with CARA utility of consumption −e−C.5 Investors trade

in period one and consume in period 2. There is a risk-free asset with gross return R and a risky

asset with aggregate supply X ∼ N(X,σ¯ 2x) and payoﬀ u = θ + η, with η ∼ N(0,σ2u). Investors know θ and can engage in research at cost c > 0 which results in a noisy signal s about the risky asset’s payoﬀ innovation, η: s = η + v, with v ∼ N(0,σ2v). When investor i observes the signal, his information set, Fi, includes both s and the equilibrium price, P, though price information is then redundant. When s is not observed, P contains useful conditioning information for payoﬀ u.

In addition to the investors, there may or may not be an analyst, working for a brokerage

ﬁrm, who can also produce signal s. We assume the analyst disseminates s (in the form of earn-

ings forecasts, research reports, or trading recommendations) for free. This mirrors institutional

practice: Investors are not charged for each analyst report they receive, so at the margin, the cost

of observing the analyst’s signal is zero. Brokers recoup the cost of producing research through

account fees, trading commissions, or cross-subsidies from market-making or investment banking.6

In the analyst’s presence, s is public information, so information is symmetric. In his absence,

we are in the Grossman-Stiglitz (1980) world where investors must decide whether to produce the

signal themselves. Grossman and Stiglitz show that in equilibrium, some fraction 0 < δ < 1 of the

investors become informed. Thus, in the analyst’s absence, information is asymmetric.

Following Grossman and Stiglitz (1980), we assume that investors do not observe aggregate

supply X. The three random variables of the model (X, η, and v) are assumed to be independent.

5The risk aversion coeﬃcient is assumed equal to unity for simplicity and without loss of generality. 6We leave the brokerage ﬁrm’s incentive to disclose the analyst’s signal unmodeled. For models that endogenize

this decision, see Admati and Pﬂeiderer (1986), Fishman and Hagerty (1995), or Veldkamp (2006).

##### A. Equilibrium Eﬀects

To determine the equilibrium eﬀects of a coverage termination, we compare prices and demands

for the risky asset in the symmetric information case, which results from an analyst’s presence, to

the asymmetric information case that occurs in the analyst’s absence. The following proposition

summarizes the equilibrium changes when the analyst ceases to produce research on the asset.

Proposition 1: Following a coverage termination, a) the price of the risky asset falls by

∆EP ≡ E[Pasymm − Psymm] = −σu4σ4vX¯ σ2x (1 − δ) R (σ2u + σ2v) σ2x σ4v + σ2v δ σ2u σx2 + σ2u δ2 + σv2 δ2

< 0 (1)

and b) a measure 1 − δ of investors reduce their demand for the risky asset by selling part of their

holdings to investors who choose to become informed. Informed demand increases by the amount

(1 − δ)σ2u σ2v X¯ σx2 σ2x σ4v + σ2v δ σ2u σ2x + σ2u δ2 + σ2v δ2

∆EID =

> 0. (2)

Proof: See Appendix A.

##### B. Discussion

CARA utility combined with the Gaussian nature of the random variables implies that investors

optimize their demands by trading oﬀ mean and variance conditional on their information set.

(The details can be found in Appendix A.) A coverage termination changes only the uninformed

investors’ information set. From their perspective, a coverage termination increases the conditional

payoﬀ variance while having a mean zero eﬀect on their expected payoﬀ. This lowers uninformed

demand and thus equilibrium price. At a lower price, informed investors, whose payoﬀ beliefs are

unchanged, are induced to increase their demand until the market-clearing condition is satisﬁed.

Why does payoﬀ uncertainty increase from the perspective of the uninformed? In the analyst’s

absence, the uninformed do not observe s and so base their demand solely on the observed price,

P. However, P is not fully revealing, because investors do not observe aggregate supply, X. As a

result, the uninformed cannot simply back out the informed investors’ signal from observed prices;

they cannot tell whether a price change reﬂects a change in aggregate supply or a change in the

signal. Instead, they noisily infer the signal by forming an expectation of payoﬀ u conditional on

observed price P. Thus, a coverage termination exposes the uninformed to aggregate supply risk.

More formally, Appendix A shows that, under rational expectations, both the symmetric and

asymmetric-information equilibrium prices are linear in the signal and aggregate supply:

θ R

Psymm =

σ2u R

σ2u R(σu2 + σ2v)

s −

+

σ2u σ2u + σ2v

(1 −

)X (3)

Pasymm = c1 + c2s + c3X (4)

where c2 > 0 and c3 < 0 (the precise expressions can be found in Appendix A). Following Brennan

and Subrahmanyam (1996) and Amihud (2002), we can interpret X as trade volume and the

coeﬃcient on X as the price impact of trade. As the following corollary shows, the eﬀect of a

coverage termination is to increase the price impact of trade:

- Corollary 1: Let the price impact of trade be deﬁned as ∂P/∂X. Then the change in price impact

of trade following a coverage termination is given by the quantity

∆(∂P/∂X) = c3 +

1 R

= −

σu2 σ2u + σ2v

σ2u R

(1 −

) (5)

σ2v σ2u δ + σ2v σ2x σ2x σ2v2 + δ2 + δ σ2u σ2x σv2 + σ2u δ2

σ2u σ2u + σv2

+ σu2 1 −

< 0.

Corollary 1 says that price falls as information asymmetry increases because price becomes more

sensitive to liquidity risk. Thus, we have:

- Corollary 2: Following a coverage termination, the asset’s expected return increases as the asset’s

exposure to liquidity risk increases.

In a factor-model setting, for instance, we would thus expect the loading on a factor proxying

for liquidity risk to increase following an exogenous coverage termination.

##### C. Robustness

In common with Grossman and Stiglitz (1980), our model makes two simplifying assumptions:

There is a single risky asset, and there is a single signal s which can be produced by both the

analyst and investors. Neither assumption is restrictive.

Easley and O’Hara (2004) extend the Grossman-Stiglitz model to multiple assets and show that

information risk cannot be diversiﬁed away even in large portfolios. Intuitively, the uninformed are

- at an informational disadvantage for every asset in their portfolio and so information risk is priced

in equilibrium in the way we have modeled it.

Multiple signals also do not change the conclusions. Suppose there are N analysts publishing

a public signal and M other signals that may be purchased at cost cj > 0. An analyst’s departure

corresponds to a (weakly) positive shift in the cost schedule for the menu of possible signal combi-

nations. In equilibrium, investors consume all the free signals and a Grossman and Stiglitz solution

determines consumption of the costly signals. Any signal combination an investor consumed before

the analyst’s departure is more expensive now, so fewer signals are consumed. In the new equilib-

rium, prices drop due to the decrease in the supply of information and the accompanying increase

in overall payoﬀ uncertainty following a coverage termination.

##### D. Testable Implications

To guide our empirical analysis, we derive the following comparative statics.

The more investors become informed following a coverage termination, the fewer investors are

aﬀected by the loss of analyst information. Thus, we have:

- Implication 1: The larger the fraction of informed investors among the company’s shareholders,

the smaller is the negative price impact of a coverage termination and the smaller is the resulting

increase in informed demand for the company’s stock:

∂∆EP ∂δ

=

2δ(1 − δ) + σ2v σx2 σ4u σ4v X¯ σ2x σ2x σv4 + σ2v δ2 + σv2 δ σ2u σ2x + σ2u δ2 2 R

> 0

∂∆EID ∂δ

= −σ2v σ2u X¯ σx2 σx2 σ4v + σ2v σu2 σ2x + δ( σ2v + σ2u)(2 − δ) σ2x σ4v + σv2 δ2 + σ2v δ σ2u σx2 + σ2u δ2 2

< 0.

Corollary 1 states that a coverage termination increases the (negative) sensitivity of price to

aggregate supply because the uninformed have a harder time ﬁltering the signal from the price.

Thus, stocks with larger aggregate supply experience larger price and demand changes:

- Implication 2: The greater is mean aggregate supply, the larger is the negative price impact of a

coverage termination and the greater is the resulting increase in informed demand for the stock:

= −σ2x σ4v σ4u (1 − δ) ( σ2u + σ2v)R σ2x σv4 + δ2 + δ σ2u σ2x σ2v + σ2u δ2

∂∆EP ∂X¯

< 0

∂∆EID ∂X¯

(1 − δ) σ2u σ2v σ2x σ2x σ4v + σ2v δ2 + σ2v δ σ2u σ2x + σ2u δ2

=

> 0.

In the absence of an analyst, the uninformed infer the signal from the observed price. This

inference problem is harder the more variable are the aggregate supply and payoﬀ, which in turn

increases the value of analyst research to the uninformed. Thus, we have the following implications:

- Implication 3a: The more variable is aggregate supply, the larger is the negative price impact of

a coverage termination and the greater is the resulting increase in informed demand for the stock:

= −σu4 σv4 X¯ δ2 (1 − δ) σ2x σv4 + σ2v δ2 + σv2 δ σ2u σ2x + σ2u δ2 2 R

∂∆EP ∂σ2x

< 0

∂∆EID ∂σ2x

=

(1 − δ) σ2u σ2v X¯ δ2 σ2u + σ2v σ2x σ4v + σv2 δ2 + σ2v δ σ2u σx2 + σ2u δ2 2

> 0.

- Implication 3b: The more variable is the asset’s payoﬀ, the larger is the negative price impact of

a coverage termination and the greater is the resulting increase in informed demand for the stock:

= −σ2u σv6 X¯ σ2x (1 − δ) σ2v σ2u σ2x + 2 σ2u δ2 + 2 σx2 σv4 + 2 σv2 δ2 + σ2v δ σ2u σ2x R ( σ2u + σ2v)2 σ2x σ4v + σ2v δ2 + σ2v δ σu2 σ2x + σ2u δ2 2

∂∆EP ∂σu2

< 0

∂∆EID ∂σ2u

=

(1 − δ) σv4 X¯ σ2x σv2 σ2x + δ2 σ2x σ4v + σv2 δ2 + σ2v δ σ2u σx2 + σ2u δ2 2

> 0.

The eﬀect of signal noise is more complicated. Consider the two extreme cases. If the signal

is very precise, the uninformed can ﬁlter the signal from the observed price very eﬀectively, so

losing the signal has a negligible impact on demand and prices. If the signal is so noisy as to be

essentially uninformative, it is of little use to the informed who therefore have little informational

advantage over the uninformed. As a result, a coverage termination results in negligible information

asymmetry among investors and so has little impact on demand and prices. In between these two

extremes, losing a noisy but informative analyst signal increases the uninformed investors’ inference

problem and so leads to a price fall and a decrease in uninformed demand. Thus, we have:

- Implication 4: The eﬀect of signal noise on the price impact of a coverage termination is U-

shaped, while its eﬀect on the change in informed demand is inverse U-shaped:

= −σ4u σ2v X¯ σx2 (1 − δ) 2 σ2u σv2 δ2 + σ2v δ σ4u σ2x + 2 σ4uδ2 − σx2 σ6v

∂∆EP ∂σ2v

R ( σu2 + σv2)2 σ2x σ4v + σ2v δ2 + σ2v δ σ2u σ2x + σ2u δ2 2 < 0 iﬀ

2 σu2 σ2v δ2 + σ2v δ σ4u σ2x + 2 σ4uδ2 σ2x σ6v

> 1 ∂∆EID ∂σ2v

(1 − δ) σ2u X¯ σx2 σ2u δ2 − σ2x σv4

=

σ2x σ4v + σ2v δ2 + σ2v δ σ2u σx2 + σ2u δ2 2 > 0 iﬀ

σ2uδ2 σx2σ4v

> 1.

## II. Identiﬁcation

Identiﬁcation of the eﬀects of an increase in information asymmetry on asset prices and investor

demands requires an instrument. To satisfy the exclusion restriction, the instrument must correlate

with an increase in information asymmetry but must not otherwise correlate with price or demands.

As McNichols and O’Brien (1997) observe, coverage changes are usually endogenous and so

do not generally satisfy the exclusion restriction. Coverage terminations, in particular, are often

viewed as implicit sell recommendations (Scherbina (2008)). The resulting share price fall may

hence reﬂect the revelation of an analyst’s negative view of a ﬁrm’s prospects rather than the eﬀect

of reduced research coverage. Similarly, an analyst may drop a stock because institutional investors

have lost interest (Xu (2006)). If institutional interest correlates with price, price may fall following

coverage terminations for reasons unrelated to changes in information asymmetry.

##### A. Identiﬁcation Strategy

To avoid these biases, we exploit what we argue is exogenous variation in research coverage in-

duced by restructuring among brokerage ﬁrms over the period 2000 to 2005. Brokerage ﬁrms have

traditionally subsidized their research departments with revenue from trading (“soft dollar commis-

sions”), market-making, and investment banking. Each of these revenue streams diminished in the

early 2000s. The prolonged decline in trading volumes that accompanied the bear market of 2000-

2003 along with increased competition for order ﬂow reduced brokerage revenue and income from

market-making activities. More recently, soft dollar commissions have attracted renewed regulatory

interest, culminating in tightened S.E.C. rules adopted in 2006.7 At the same time, institutional

clients are increasingly banning the use of soft dollars.8 And concerns that analysts publish biased

research to please investment banking clients (Michaely and Womack (1999), Dugar and Nathan

(1995), Lin and McNichols (1998)) have led to new regulations, such as the 2003 Global Settlement,

which have made it harder for the investment banking division to cross-subsidize research.

Brokerage ﬁrms have responded to these adverse changes in the economics of producing research

by closing or downsizing their research operations. A subset of them have done so in a way likely

to be uninformative about the future prospects of the companies whose coverage they terminated.

###### A.1. Closures

Using news sources accessed through Factiva, we identify 20 brokerage ﬁrms that closed their

research departments between 2000 and 2005. These range from large ﬁrms (e.g., Wells Fargo,

- 7The SEC’s new interpretative guidance of the safe-harbor rule under Section 28(e) of the 1934 Securities Exchange Act is available at http://www.sec.gov/rules/interp/2006/34-54165.pdf.
- 8According to the TABB Group, a consultancy, nearly 90% of all larger institutional investors stopped or decreased use of soft dollars between 2004 and 2005 (BusinessWire, June 1, 2005).

8/2005) to smaller outﬁts (e.g., Schwab’s Soundview Capital Markets division, 10/2004) and en-

compass both retail-oriented ﬁrms (e.g., First Montauk, 2/2004) and institutional brokerage houses

(e.g., Emerald Research, 7/2001) and brokers with either generalist (e.g., ABN Amro, 3/2002) or

specialist coverage (e.g., Conning & Co., 10/2001).

Press reports make it clear that the closures are unlikely to have been motivated by negative

information about individual stocks and so likely satisfy the exclusion restriction. For example,

commenting on his decision to close down IRG Research, CEO Thomas Clarke blamed regulation:

“With the brokerage industry facing some of the most far-reaching regulatory changes within the last 30 years, including S.E.C. rulings regarding the use of soft dollars and possibly the unbundling of research and trading costs, we could not see the economics working in our favor without substantial additional investment.” (Dow Jones, June 28, 2005)

Dutch bank ABN Amro closed its loss-making U.S. equities and corporate ﬁnance business in

March 2002. Among the 950 redundancies were 28 senior analysts who, along with junior team

members, covered nearly 400 U.S. stocks. Board member Sergia Rial commented on the reasons:

“We’re withdrawing from businesses in which we’re strategically ill-positioned and cannot create a sustainable proﬁt stream, whether the market turns around or not.” (Chicago Tribune, March 26, 2002)

Regional broker George K. Baum closed its capital markets division in October 2000, blaming

lack of proﬁtability even during the booming late 1990s:

“Neither the retail brokerage nor equity capital markets divisions made money in the past two years.” (Knight Ridder Tribune Business News, Oct. 13, 2000)

We identify the stocks aﬀected by the 20 brokerage closures using the coverage table of Reuters

Estimates, which lists, for each stock, the dates during which each broker and analyst in the Reuters

database actively cover a stock. When dating the terminations, we use the time stamp of the ﬁrst

press release announcing the brokerage closure. This allows us to pinpoint the precise trading day

on which investors can ﬁrst react to the news.

###### A.2. Sector Terminations

While 20 brokers got out of research altogether, more than 150 brokers downsized their research

departments between 2000 and 2005. In 2003, for instance, Goldman Sachs, Morgan Stanley, and

J.P. Morgan reportedly cut research staﬃng by between 15 and 25 percent (Reuters, May 23, 2003).

In many cases, brokers ﬁred entire sector teams as opposed to individual analysts covering part

of a sector. We focus on such sector terminations to reduce the likelihood that brokers selectively

ﬁred analysts whose stocks had poor future prospects (which could violate the exclusion restriction).

Later in this section, we report evidence suggesting that sector terminations do not reﬂect past or

future sector performance in our data.

To illustrate, on May 23, 2003, Citigroup dropped coverage of eight of the 43 sectors its analysts

had covered, namely metals/mining, life sciences, utilities, healthcare services, airlines, industrials,

specialty chemicals, and telecom equipment/wireless. On Oct. 12, 2001, Wachovia Securities laid oﬀ

the eight analysts who covered technology hardware, telecommunications, and consumer durables.

To identify sector terminations, we ﬁrst search the Reuters coverage table for days on which a

brokerage ﬁrm terminates coverage of at least 75% of the stocks it had been covering in a sector. As

sector deﬁnitions vary by broker, we deﬁne sectors using S&P’s six-digit GICS codes.9 We do not

impose a 100% termination rate within a GICS sector to allow for the possibility that GICS do not

9Bhojraj, Lee, and Oler (2003) compare four industry classiﬁcations, concluding that “GICS classiﬁcations are signiﬁcantly better at explaining stock return co-movements, as well as cross-sectional variations in valuation multiples, forecasted and realized growth rates, R&D expenditures, and various key ﬁnancial ratios.” There are currently 68 GICS sectors at the six-digit level. See www2.standardandpoors.com/spf/xls/index/gics map aug2008.xls.

coincide precisely with a given broker’s sector deﬁnition;10 our results are not sensitive to this. In

addition, we search in Factiva and Bloomberg for announcements of sector terminations not already

identiﬁed in the Reuters data. Finally, we mine three text archives of analyst reports (Investext,

Thomson One, and the client-intranet of a large brokerage house) for client notices announcing

sector terminations.11 Such termination notices are mandatory under NYSE Rule 472(f)(5) and

NASD Rule 2711(f)(5) which require that:

“[A] member provide notice to customers that it is terminating research coverage of an issuer that is the subject of a research report. ... [I]f the research analyst covering the subject company has left the member, or where the member has terminated coverage on an industry or sector ... the rationale for termination will be required.” The broker must give notice “... using the means of dissemination equivalent to those it ordinarily uses to provide the customer with its research reports.”12

The rules were brought in to prevent brokerage ﬁrms from terminating coverage secretly. Under

the rules, the broker’s clients learn of the coverage termination directly from the broker. In fact,

the news is quickly disseminated to the wider market. As a proxy for wider dissemination, we

search the Dow Jones marketwatch.com service. We ﬁnd that this website typically reports news

of terminations within one day of the termination notices. Moreover, marketwatch.com provides a

synopsis of the broker’s reason for termination, allowing non-clients to infer whether a stock was

terminated for endogenous or exogenous reasons.

There is considerable overlap between the sector terminations identiﬁed from Reuters, the news

reports, and the text archives. In the rare instances where the sources disagree on announcement

- 10Suppose some oil & gas stocks (GICS code 101020) are covered by the energy team. If the broker ﬁres the oil &

gas team but not the energy team, we will observe less than 100% of the oil & gas GICS coverage being terminated.

- 11Search terms used include: “Terminate/discontinue/withdraw/suspend/cease/drop/stop coverage”, “Not

rated/covered”. The vast majority of termination notices identiﬁed this way relate to individual companies (not sectors) which are dropped for endogenous-sounding reasons, such as “The company no longer ﬁts with our core investment objectives and coverage universe;” “owing to potential bankruptcy proceedings;” or “because of the company’s relatively low institutional ownership, low retail interest, and low trading volume.” We do not include such terminations in our sample as they likely violate the exclusion restriction.

12The ﬁrst quote is from http://www.sec.gov/rules/sro/34-48252.htm. The second quote is from http://ﬁnra.complinet.com/en/display/display main.html?rbid=2403&element id=3675.

dates, we choose the earliest one. For news reports and for many of the termination notices from

the text archives, we have time stamps and so can pinpoint announcements with great precision.13

###### A.3. Sample

Combining the broker-closure and sector terminations, we have 21,782 candidate events. We then

apply the following ﬁlters. First, using CRSP delisting codes, we remove 434 stocks that were

involuntarily delisted from an exchange within three months of a termination notice. Second, we

remove 5,396 terminations that are followed by a reinitiation by the same analyst at a new employer,

or by a diﬀerent analyst at the original brokerage ﬁrm, within three months of the drop.14 Finally,

we exclude 528 REITs, 326 ADRs, 80 non-common stocks and closed-end funds (i.e., CRSP share

codes > 12), and 79 companies without valid CRSP permno identiﬁers.

Our ﬁnal sample consists of 14,939 coverage terminations, 1,793 of which are due to brokerage

closures. The sample includes 4,022 unique stocks and spans all Fama-French industries, 172

brokerage houses, and 1,552 analysts.15 The sample contains 1,816 terminations in 2000, 1,720 in

2001, 3,593 in 2002, 2,685 in 2003, 2,391 in 2004, and 2,734 in 2005. In 1,347 cases, the termination

left a stock without any analyst coverage. We refer to these as orphaned stocks.

Table I compares summary statistics for the size, liquidity, and return volatility of the stocks in

our sample to the CRSP universe of publicly traded U.S. stocks and to the universe of U.S. stocks

covered by at least one brokerage ﬁrm according to Reuters Estimates or I/B/E/S. Sample stocks

- 13We deliberately do not use data from I/B/E/S or First Call to date terminations. Ellul and Panayides (2007), who do, comment: “The date that we use is the one when the last estimate of the EPS estimate is recorded by either I/B/E/S and/or FirstCall. In practice, this is the date when the analyst’s report is communicated to I/B/E/S and FirstCall. It is not necessarily the date when the analyst’s report is published.” Kecskes and Womack (2007) face a similar problem, and resort to conducting their event study at an annual frequency. The news reports, termination notices, and the Reuters Estimates coverage table we use do not suﬀer from this shortcoming.
- 14If clients know, or believe, that coverage will shortly be re-initiated, the expected change in information asymmetry may be negligible, and the data bear this out: The average price fall for the 5,396 re-initiations we screened out is one-tenth the size of the average price fall in our ﬁnal sample.
- 15We identify the analyst covering the stock from the name on the termination notice or the Reuters coverage table where available, or else from the I/B/E/S earnings forecast database.

are on average larger and more liquid than the average stock in the CRSP universe. The comparison

to the Reuters and I/B/E/S universe shows that this reﬂects a general tendency among analysts to

cover larger and more liquid stocks. In addition, sample stocks – like Reuters and I/B/E/S stocks

more generally – are less volatile than CRSP stocks. On average, 6.4 analysts covered a sample

stock before a coverage drop, in line with covered stocks more generally. Overall, the average

sample ﬁrm looks similar to the average ﬁrm in the Reuters Estimates and I/B/E/S databases, in

terms of size, liquidity, volatility, and analyst coverage.

##### B. Do Terminations Increase Information Asymmetry?

Identiﬁcation requires that coverage terminations increase information asymmetries among in-

vestors. We use four popular empirical measures to proxy for information asymmetries: Easley

et al.’s (1997) probability of informed trading (PIN), bid-ask spreads, Amihud’s (2002) illiquidity

measure, and Lesmond et al.’s (1999) measure of illiquidity based on the number of zero or miss-

ing return days. In addition, we examine changes in earnings surprises and return volatilities at

earnings releases around coverage terminations.16

Throughout, we use diﬀerence-in-diﬀerence (DiD) tests to help remove biases due to omitted

variables or secular trends aﬀecting similar companies at the same time (Ashenfelter and Card

(1985)). For instance, bid-ask spreads may fall over time due to decimalization or competition

from ECNs, obscuring the eﬀect of the termination treatment. To remove common inﬂuences, DiD

tests compare the change in a variable of interest for treated ﬁrms to the contemporaneous change

for a set of control ﬁrms matched to have similar characteristics but which are themselves unaﬀected

by the treatment. Given our focus on asset pricing, we follow Hong and Kacperczyk (2007) and

16For brevity, the tests focus on the whole sample. In the subsample of closure-related terminations, we ﬁnd results that are at least as strong economically, and in most instances considerably stronger. These are available on request.

match ﬁrms on the Fama-French (1993) and Carhart (1997) pricing factors using the Daniel et al.

(1997) algorithm. Speciﬁcally, we randomly choose as controls for ﬁrm i ﬁve unique ﬁrms in the

same size, book-to-market, and momentum quintile in the month of June prior to a termination,

subject to the condition that control ﬁrms did not themselves experience a termination in the

quarter before and after the event. In view of the evidence from Table I that ﬁrms with analyst

coverage are larger and more liquid than CRSP ﬁrms in general, we also require that controls must

be covered by one or more analysts in the three months before the event.

###### B.1. Results

Table II, Panel A reports results for PIN. If our coverage terminations increase information asym-

metries, we expect PIN to increase. We obtain PIN data for 12,011 of our sample events from

Stephen Brown (see Brown, Hillegeist, and Lo (2004)). Even though the data are only available

quarterly, the results are quite precisely estimated. Net of the change among control ﬁrms, PIN

increases on average by 1.6% between the quarter before a termination and the quarter after. This

and the following statistics are each highly statistically signiﬁcant.17

Panel B reports changes in bid-ask spreads around coverage terminations. (This and the next

two statistics are computed from daily data over either six- or 12-month estimation windows ending

10 days before and starting 10 days after a termination announcement.) Spreads decline for both

sample and control stocks, presumably reﬂecting the benign eﬀects of decimalization etc., but they

decline more slowly for sample stocks. As a result, the diﬀerence-in-diﬀerence tests show that

bid-ask spreads increase relative to control stocks following coverage termination, by around 3.3%.

This is consistent with an increase in information asymmetry.

17Both closure-related and sector terminations naturally cluster in time by broker. This poses a problem for standard cross-sectional tests, so we bootstrap the standard errors following Politis and Romano (1994). We report p-values based on the dependent block bootstrap with 10,000 replications and Politis and White (2004) block lengths.

Wang (1994) predicts that the correlation between absolute return and dollar volume increases

in information asymmetry. Panel C tests this prediction using changes in Amihud’s (2002) illiquidity

measure (AIM). For the six-month window, AIM averages −3.892 before and −3.966 after a cov-

erage termination, implying that the correlation between absolute return and volume decreases.18

The diﬀerence-in-diﬀerences, on the other hand, averages 0.046, implying an increase in information

asymmetry following coverage terminations. The 12-month estimate is similarly positive, averaging

0.075. These estimates correspond to a 1.2% and 1.9% average increase in AIM, respectively.

An alternative measure of illiquidity is due to Lesmond et al. (1999). A large number of zero-

return or missing-return days in a given estimation window may indicate an illiquid stock. Panel

D shows that this number increases by 7.1% and 13.1% following a coverage termination, net of

the control-ﬁrm change and measured over six- and 12-month windows, respectively.

Our ﬁnal test focuses on earnings announcements. Following coverage terminations, we expect

more volatile returns around earnings announcements (as more uncertainty is left unresolved; see

West (1988)) and greater absolute earnings surprises (if post-termination consensus forecasts reﬂect

reduced information sets). Panel E conﬁrms these predictions. Log daily return volatility in the

three days around earnings announcements increases by 2% net of the change among control ﬁrms,

while the average magnitude of earnings surprises increases by 10.8%.

###### B.2. Summary

Each proxy in Table II yields evidence consistent with the interpretation that information asym-

metry increases following coverage terminations. Thus, our terminations sample appears to satisfy

the ﬁrst of the two conditions for identiﬁcation. Before we turn to the second, we brieﬂy discuss

18This illustrates the importance of using a diﬀerence-in-diﬀerences estimator. The numerator of AIM is stationary (a return) whereas the denominator is non-stationary (price · volume). If returns are constant over time but dollar volumes increase, ∆AIM will generally be negative.

untabulated results for the subsample of closure-related terminations and for orphaned stocks.

Closure-related terminations behave just like the sample overall, with similar-sized changes in our

proxies for information asymmetry. In the case of orphans, we ﬁnd considerably larger changes,

indicating that these suﬀer the greatest increase in information asymmetry. To illustrate, AIM

increases by between 17.1% and 24.7% when a stock becomes an orphan, while absolute earnings

surprises increase by 36.8% on average.

##### C. Are Sample Terminations Exogenous?

Closure-related terminations satisfy the exclusion restriction unless brokerage ﬁrms closed their

research departments because their analysts had negative private signals about the stocks they

covered. In view of the quotes in Section A.1., it seems more likely that brokerage ﬁrms quit

research for strategic and ﬁnancial reasons (often in the context of withdrawal from investment

banking more generally) than to mask negative news about companies their analysts covered.

Sector terminations are trickier. The exclusion restriction would be violated if brokers system-

atically chose to terminate sectors whose characteristics correlate with variables of interest, such

as value or demand. Whether they do so is an empirical question we can test.

We model a brokerage ﬁrm’s choice of which sectors to stop covering at time t using McFadden’s

(1974) choice model. For each broker, the choice set from which sector terminations are drawn

includes all sectors the broker covers at time t. The unit of analysis is hence a broker-sector pair.

The dependent variable equals one if a sector is chosen for termination and zero otherwise. To be

included in the estimation sample, we require that the brokerage ﬁrm drop at least one sector at

time t (so we model the choice of which sectors are terminated conditional on the ﬁrm’s decision

to restructure). We exclude brokerage ﬁrms that close down their research departments altogether

(i.e., those that terminate every sector they cover).

Brokers are assumed to select those sectors whose termination will maximize their expected

proﬁt. We parameterize expected proﬁt as a function of sector performance (namely, prior and

future sector returns and prior and future sector earnings surprises); sector characteristics (return

volatility, a proxy for competition from other brokers, and two proxies for the revenue a sector

generates for that particular brokerage ﬁrm by way of trading commissions and investment banking

fees); and analyst characteristics (an Institutional Investor ‘all-star’ indicator, the analyst’s forecast

accuracy relative to his sector-matched peers at other brokerage ﬁrms, his experience, and his tenure

with the broker). The precise variable deﬁnitions can be found in Table III.

The model is estimated using probit without (column 1) or with random brokerage-ﬁrm eﬀects

(column 2). We ﬁnd no evidence that brokers terminate sectors with poor past or poor anticipated

stock performance. The same goes for earnings surprises: Brokers do not terminate sectors whose

earnings have recently disappointed, nor do they terminate sectors whose subsequent earnings will

fall short of consensus. The coeﬃcient estimates are not only statistically insigniﬁcant, they are

also economically small, as the marginal eﬀects in Table III indicate. These results suggest that

sector termination choices are not information-driven. Instead, brokers are signiﬁcantly more likely

to drop sectors that produce low commission or investment banking revenue as well as those covered

by inexperienced, recently hired, unrated analysts with poor forecasting records.19

As a ﬁnal test of the exclusion restriction, we test directly whether sample terminations are

uninformative about the aﬀected stocks’ future prospects, as required for identiﬁcation. Suppose at

time t, a broker terminates coverage. If this signals private information about the stock, we should

be able to predict its future performance from the fact that coverage was terminated. Testing this

19Though not shown, year eﬀects are not statistically signiﬁcant. Brokers thus appear not to herd in which sectors they terminate in a given year.

requires an assumption about the nature of the signal. Assume that it is negative information

about t + 1 earnings that is not yet reﬂected in the consensus earnings forecast dated t − 1 (i.e.,

before other analysts knew of the coverage termination). When earnings are eventually announced,

they will fall short of the t − 1 consensus, resulting in a negative earnings surprise. If, on the other

hand, the termination is exogenous, earnings will not diﬀer systematically from consensus.

We implement this test in a panel of CRSP companies over the period 2000Q1 to 2006Q1. (We

ﬁlter out companies with share codes greater than 12, leaving 4,148 ﬁrms and 65,629 ﬁrm-quarters.)

The dependent variable is earnings surprise, deﬁned as (EPSt+1 − consensus forecastt−1)/(book

value of assets per sharet+1). Earnings and forecast data come from I/B/E/S. The variables of

interest are two indicators. The ﬁrst identiﬁes the sample terminations. Its coeﬃcient should be

statistically zero if sample terminations are uninformative about future earnings. The second iden-

tiﬁes 16,354 non-sector (and so likely endogenous) terminations available in the Reuters Estimates

coverage table.20 Here, we expect a negative coeﬃcient. We also control for lagged earnings sur-

prises, returns and return volatility measured over the prior 12 months, the log number of brokers

covering the stock, and year eﬀects.21 This yields the following estimates:

return − 4.814

L(earnings surprise) + .466

volatility + .228

earnings surprise = .364

# brokers

.370

.017

.040

.019

−.128

endogenous termination + .016

sample termination + year eﬀects

.042

.040

The adjusted R2 is 14.6%. We report heteroskedasticity-consistent standard errors (clustered on

CRSP permno) below the coeﬃcients. Earnings surprises are serially correlated, more positive for

- 20We identify 53,092 ‘endogenous’ terminations from the Reuters coverage table. Endogenous terminations tend to cluster, as multiple brokers drop coverage of the same stock at or around the same time. Thus, there is an endogenous termination in only 16,354 of the 65,629 ﬁrm-quarters in the panel.
- 21Adding ﬁrm ﬁxed eﬀects to control for unobserved heterogeneity in ﬁrm characteristics halves the eﬀect of one control (volatility) but otherwise does not alter our results.

high-return and low-volatility companies and among ﬁrms covered by many analysts. Controlling

for these eﬀects, earnings surprises are signiﬁcantly more negative following ‘endogenous’ termi-

nations (p = 0.002). On average, an endogenous termination is followed by a quarterly earnings

surprise that is 21.6% more negative than the sample average over this period. The 14,939 sample

terminations, by contrast, are neither statistically nor economically related to subsequent earnings

surprises. This is consistent with sample terminations being uninformative and thus exogenous.

## III. The Eﬀect of Information Asymmetry on Price and Demands

##### A. Change in Price

To test the ﬁrst part of Proposition 1, we compute cumulative abnormal returns (CARs) using two

benchmarks (the market model and the Fama-French three-factor model) from the close on the day

before the termination announcement to the close on the announcement day [–1,0], one day later

[–1,+1], or three days later [–1,+3]. Table IV reports the results for the overall sample (Panel A)

as well as the subsample of terminations that do not coincide with a negative earnings surprise

(Panel B) and the subsample of closure-related terminations (Panel C), and broken down by the

number of other brokers covering the stock (Panel D). In each case, CARs are highly statistically

signiﬁcant, regardless of how we compute standard errors.

Consistent with Proposition 1, price falls following the announcement of a coverage termination.

For the sample as a whole, CARs range from −51 to −71 basis points (not annualized).22 For the

median sample ﬁrm, this amounts to a fall in market value of between $1.8 and $2.1 million.

Could confounding events be driving this result? If our terminations are truly exogenous, we

22Despite the widespread view that endogenous coverage terminations are implicit sell recommendations, we are not aware of studies estimating announcement returns for such implicit sells. For explicit sell recommendations (i.e., downgrades to sell), Womack (1996) ﬁnds average three-day excess returns of −3.87%.

eﬀectively have a randomized trial and controls for confounding events are superﬂuous. Analysis

of one particular event, coincident negative earnings surprises, illustrates. There are about as few

coincident negative earnings surprises as chance alone would predict. When these are excluded,

CARs range from −47 to −60 basis points, barely changing the result.

Among the subsample of closure-related terminations, CARs are more negative than in the

sample as a whole, averaging between −1.13% and −4.02% depending on benchmark. Stratiﬁed by

coverage, CARs increase monotonically (become less negative) the more brokers continue to cover

a stock. To illustrate, over the [-1,0] interval, orphaned stocks lose 99 basis points in the market

model, while stocks covered by more than 15 other analysts lose only 35 basis points. This suggests

that the degree of information asymmetry decreases in the extent of analyst coverage.

Though not shown, we ﬁnd no evidence that these price falls are temporary. After one month,

for instance, CARs still average −47 basis points.

##### B. Changes in Demand

According to Proposition 1, investors who choose to become informed following a coverage ter-

mination increase their holdings while the uninformed sell. Although we cannot identify directly

who becomes informed, it seems plausible that retail investors are less likely to produce their own

research than are institutional investors, which not only likely have a cost advantage in producing

research themselves but often also maintain trading accounts with multiple brokerage ﬁrms and so

face a relatively smaller loss of analyst information to begin with. We thus assume that a larger

fraction of institutions than of retail investors becomes informed.23

23In an auxiliary test, we compare the price impact of sample terminations at two types of brokerage ﬁrms: Those that serve both retail and institutional investors, and those that serve only institutional investors. (Brokers are classiﬁed based on information from the annual Factbook of the Securities Industry and Financial Markets Association.) Announcement-day CARs are signiﬁcantly lower for terminations at institution-only brokers, averaging −18 vs. −61 basis points using the three-factor model. This is consistent with our assumption that institutions are

Unfortunately, we have no high-frequency trading data with which to estimate changes in in-

stitutional and retail demand.24 Instead, we use the quarterly CDA/Spectrum data to compute

the change in the fraction of a sample company’s outstanding stock held by institutions required

to ﬁle 13f reports.25 Panel A of Table V shows that 13f institutions as a group increase their

holdings from 61.9% to 62.9% of shares outstanding following the average termination (p < 0.001).

Net of the contemporaneous change in control ﬁrms, the average increase is 0.9 percentage points

(p < 0.001). Thus, 13f institutions are unusually large net buyers following coverage terminations.

If institutions are more likely to generate their own research than are retail investors, this result is

consistent with Proposition 1.

For robustness, Panel B provides similar evidence for the subsample of closure-related termina-

tions. Panel C shows a breakdown of the mean net changes in institutional holdings by the number

of brokers covering the stock. While not monotonic, institutional holdings increase the most, and

retail holdings decrease the most, when coverage drops to zero.26

##### C. Testing the Comparative Statics: Price

To test the price-related comparative statics in Implications 1 through 4, we regress Fama-French

announcement-day CARs on proxies for the ﬁve parameters of the model: δ (the fraction of informed

investors), X¯ (mean aggregate supply), σ2x (variance of aggregate supply), σ2u (payoﬀ variance), and σ2v (signal noise).27 We also control for whether the termination coincides with a negative earnings surprise as well as ﬁrm ﬁxed eﬀects (using CRSP permnos) and announcement-year eﬀects.

less aﬀected by terminations.

- 24Trade size is sometimes used to infer retail trades, but decimalization in January 2001 and the growth in algorithmic trading mean that small trades are no longer viewed as a good proxy for retail trades.
- 25Investment companies and professional money managers with over $100 million under management are required to ﬁle quarterly 13f reports. Reports may omit holdings of fewer than 10,000 shares or $200,000 in market value.
- 26Xu (2006) ﬁnds that institutions reduce their ownership of orphaned stocks in a sample that does not screen out endogenous terminations. Xu’s ﬁnding is consistent with the view that endogenous terminations are implicit sells.
- 27Results are robust to using market-model CARs and alternative estimation windows.

Our main proxy for δ is the fraction of the company’s stock held by institutional investors, call

it ϕ. We do not claim that every institution will choose to become informed (i.e., that δ = ϕ).

For the proxy to work, we only require that δ correlate positively with ϕ. This will be the case if

institutions are more likely to become informed than retail investors. We use the ﬁrst two moments

of the distribution of log daily share turnover to proxy for X¯ and σ2x. The proxy for payoﬀ variance

σu2 is the standard deviation of the year-on-year growth rate in quarterly earnings per share. We

parameterize signal noise σ2v as a function of the number of other analysts covering the stock and the quality of the analyst whose coverage is lost. Stocks covered by fewer analysts should have noisier signals, while high-quality analysts presumably produce more informative signals, so their terminations should lead to larger price falls.

Table VI reports the results. The adjusted R2 of 37.2% in column 1 suggests this model has

reasonable ﬁt. With one exception, all coeﬃcients are statistically signiﬁcant at the 5% level or

better, and all have the predicted sign. Price falls are larger, the smaller are institutional holdings,

the larger and more variable is turnover, the more volatile is earnings growth (p = 0.081), the fewer

analysts cover the stock, and for terminations involving all-stars or more experienced analysts or

those with high relative forecast accuracy. Economically, the largest eﬀect is ∂∆EP/∂X¯. A one

standard deviation in our proxy for X¯ is associated with a fall in price of 31 basis points, all else

equal. The smallest eﬀect is ∂∆EP/∂σ2u (−5.4 basis points). Our ﬁndings are robust to restricting the sample to closure-related terminations (column 2). All signs are unchanged and the economic magnitude of each eﬀect is stronger (with the exception of the extent of coverage and analyst experience, which become statistically insigniﬁcant). Column 3 returns to the sample as a whole and adds the size of the brokerage ﬁrm’s retail and institutional sales forces as further proxies for (1 − δ) and δ, respectively. Interestingly, only the

size of the retail sales force appears to matter: The larger the retail sales force, the more negative

the price change (p = 0.005); a one standard deviation increase (say, from Ladenburg, Thalman

to Prudential Securities) is associated with a 10.3 basis point lower CAR. The fact that the size

of the broker’s institutional sales force has no eﬀect is consistent with our assumption that retail

investors are more sensitive to changes in research coverage while institutions are more likely to

become informed some other way.

Recall that Implication 4 predicts a U-shaped relation between ∆EP and signal noise. In column 4, we add the level and square of analyst forecast dispersion as further proxies for σv2. The data provide some support for a U-shaped relation: The coeﬃcient for the level of forecast dispersion is negative (p = 0.099) while that for the squared term is positive (p = 0.034). However, the implied minimum is in the far right tail of the empirical distribution of forecast dispersion, so as a practical matter, in our data, ∆EP decreases in all our proxies for signal noise.

##### D. Testing the Comparative Statics: Demands

To test the demand-related comparative statics in Implications 1 through 4, we estimate the same

four speciﬁcations as in the previous section but use the diﬀerence-in-diﬀerence change in institu-

tional holdings as the dependent variable. This is deﬁned as in Section III.B and is intended to

proxy for the change in informed demand, ∆EID.

The results, shown in Table VII, generally support the implications. In column 1, the signs for ∂∆EID/∂δ, ∂∆EID/∂X,¯ ∂∆EID/∂σ2x, and ∂∆EID/∂σ2u are all as predicted, and each coeﬃcient is highly statistically signiﬁcant. (Recall that the expected signs of the demand eﬀects are exactly opposite to those for the price eﬀects.) Only one of our proxies for signal noise, the analyst’s all-star status, is signiﬁcant; it has the predicted positive sign. Restricting the sample to closure-related

terminations (shown in column 2) gives less precisely estimated coeﬃcients, and we lose support

for ∂∆EID/∂X¯ > 0 and ∂∆EID/∂σ2x > 0. Controlling for the size of the broker’s sales force (in column 3) improves the signiﬁcance of two signal noise proxies, all-star status and experience. Adding forecast dispersion and its square (in column 4) provides support for the predicted inverse U-shaped relation between changes in informed demand and signal noise.

Our results for changes in demand are generally noisier than those for changes in price. This is

not surprising, given the quarterly nature of the 13f institutional ownership data. We view these

results as encouraging, though, given the data limitations, they should be interpreted with caution.

##### E. Testing Corollary 2: Change in Expected Returns

Falling prices following an increase in information asymmetry suggest that investors’ expected

returns have increased. Corollary 2 states that expected returns increase because aﬀected stocks

become more sensitive to liquidity risk. To test this prediction, we estimate the following model:

ri,te = αi + (βi + ∆βiPostIt∈Post + ∆βiPost&TermIt∈PostIi∈Term)Factorst + i,t (7)

where ri,te is stock i’s month-t return in excess of the riskfree rate; It∈Post is an indicator for the post-

event period; Ii∈Term identiﬁes ﬁrms in the terminations sample (as opposed to matched controls,

selected as before); and Factorst is a vector which includes the three Fama-French factors (MKT,

SMB, and HML) and a liquidity factor, LIQ.28 We use LIQ to proxy for liquidity risk. Table

VIII reports results for three alternative versions of LIQ: Sadka’s (2006) liquidity factor (Panel A),

Pastor and Stambaugh’s (2003) nontraded liquidity factor (Panel B), and Pastor and Stambaugh’s

traded liquidity factor (Panel C).

28We do not include Carhart’s (1997) momentum factor because several studies ﬁnd that momentum is largely driven by liquidity, which is our focus. See Pastor and Stambaugh (2003) and Sadka (2006).

Regression (7) allows us to measure whether a stock’s factor loadings change following a termi-

nation, compared to otherwise similar control ﬁrms which experience no termination. This eﬀect

is captured by the diﬀerence-in-diﬀerences term, ∆βPosti &Term. To estimate the model, we impose

the restriction that ∆βiPost and ∆βPosti &Term are common to all ﬁrms and use a two-step approach analogous to that of Pastor and Stambaugh (2003); the details of the estimation can be found in Table VIII.29 The model is estimated with monthly data using 12-, 18-, or 24-month windows ending the month before a termination or beginning one month after.

The results are consistent with Corollary 2. With three alternative liquidity factors and three estimation windows, we have nine sets of results. In each, the estimate for ∆βLIQPost&Term is positive, signiﬁcantly so in six of the nine. These results suggest that the returns of companies experiencing coverage terminations become more sensitive to liquidity risk, relative to matched ﬁrms with unchanged analyst coverage. Economically, the eﬀects are largest using Sadka’s (2006) liquidity factor. Relative to the pre-termination means, liquidity betas in Panel A increase by between 5.9% and 8.3%. (The corresponding increases in Panels B and C range from 1.6% to 6.4%.)

In each speciﬁcation, post-termination returns load signiﬁcantly less strongly on the market

factor. Changes in loadings on the SMB and HML factors, on the other hand, are model-speciﬁc.

Using the Sadka (2006) factor, the changes are statistically zero (see Panel A). Using the Pastor-

Stambaugh (2003) factors, ∆βSMBPost&Term is positive and signiﬁcant for the traded liquidity factor with 18- or 24-month estimation windows (see Panel C), though note that data for this factor are available only through 2004. ∆βPostHML&Term is positive and signiﬁcant using either Pastor-Stambaugh factor with 18- or 24-month estimation windows (see Panels B and C).

29Like theirs, ours is a system of asset return equations for thousands of ﬁrms with time-varying factor loadings. The cross-equation parameter restrictions and two-step approach allow us to reduce the parameterization of the model and increase the precision of the estimates in a computationally eﬃcient way. For further details, see Pastor and Stambaugh (2003, p. 665).

The overall eﬀect of the changes in factor loadings is to increase the expected returns of stocks

experiencing coverage terminations. For example, using mean factor returns for our sample period,

the changes in coeﬃcients in Panel A imply that expected returns increase by between 14 and 44

basis points a year.30

## IV. Conclusion

We test models of asset pricing under asymmetric information using plausibly exogenous variation

in the supply of information caused by the closure or restructuring of brokerage ﬁrms’ research

operations. Consistent with predictions we derive from a Grossman and Stiglitz-type model, we

ﬁnd that share prices and uninformed investors’ demands fall in response to exogenous terminations

of analyst coverage. In the cross-section, the magnitudes of these falls are consistent with the

comparative statics of the model: They are larger, the more investors are uninformed, the larger

and more variable is turnover, the more uncertain is the asset’s payoﬀ, and the noisier is the better-

informed investors’ signal. Finally, we show that prices fall because expected returns become more

sensitive to a factor proxying for liquidity risk.

Beyond providing relatively direct empirical support for asymmetric-information models of asset

prices, we hope that our quasi-experiment can serve as a useful instrument for empirical work in

other applications that examines the eﬀects of information asymmetry. In this spirit, we intend to

make our set of exogenous coverage terminations available to fellow researchers.

30The increase in expected returns implies that realized post-termination returns will exceed a benchmark that fails to account for the factor loading changes. In other words, unless the benchmark is suitably adjusted, ﬁrms experiencing a termination will appear to eventually bounce back, generating positive abnormal returns (or alpha).

## References

Acharya, Viral, and Lasse Heje Pedersen, 2005, Journal of Financial Economics 77, 375-410. Admati, Anat, 1985, A noisy rational expectations equilibrium for multi-asset securities markets, Econometrica 53, 629-658. Admati, Anat, and Paul Pﬂeiderer, 1986, A monopolist market for information, Journal of Economic Theory 39, 400-438. Amihud, Yakov, 2002, Illiquidity and stock returns: Cross-section and time series eﬀects, Journal of Financial Markets 5, 31-56. Amihud, Yakov, and Haim Mendelson, 1986, Asset pricing and the bid-ask spread, Journal of Financial Economics 17, 223-249. Ashenfelter, Orley, and David Card, 1985, Using the longitudinal structure of earnings to estimate the eﬀect of training programs, Review of Economics and Statistics 67, 648-660. Bekaert, Geert, Campbell R. Harvey, and Christian Lundblad, 2007, Liquidity and expected returns: Lessons from emerging markets, Review of Financial Studies 20, 1783-1831.

Bhojraj, Sanjeev, Charles M.C. Lee, and Derek Oler, 2003, What’s my line? A comparison of industry classiﬁcation schemes for capital market research, Journal of Accounting Research 41, 745-771.

Boehmer, Ekkehart, James Musumeci, and Annette B. Poulsen, 1991, Event-study methodology under conditions of event-induced variance, Journal of Financial Economics 30, 253-272.

Brennan, Michael J., and Avanidhar Subrahmanyam, 1996, Market microstructure and asset pricing: On the compensation for illiquidity in stock returns, Journal of Financial Economics 41, 441–464.

Brown, Stephen, Stephen A. Hillegeist, and Kin Lo, 2004, Conference calls and information asymmetry, Journal of Accounting and Economics 37, 343-366.

Brown, Stephen J., and Jerold B. Warner, 1980, Measuring security price performance, Journal of Financial Economics 8, 205-258.

Carhart, Mark, 1997, On persistence in mutual fund performance, Journal of Finance 52, 57-82. Cowan, Arnold R., 1992, Nonparametric event study tests, Review of Quantitative Finance and Accounting 2, 343-358. Daniel, Kent, Mark Grinblatt, Sheridan Titman, and Russ Wermers, 1997, Measuring mutual fund performance with characteristics-based benchmarks, Journal of Finance 52, 1035-1058. Duarte, Jeﬀerson, and Lance A. Young, 2008, Why is PIN priced?, Journal of Financial Economics, forthcoming.

Dugar, Amitabh, and Siva Nathan, 1995, The eﬀects of investment banking relationships on ﬁnancial analysts’ earnings forecasts and investment recommendations, Contemporary Accounting Research 12, 131-160.

Easley, David, and Maureen O’Hara, 1992, Time and the process of Security price Adjustment, Journal of Finance 47, 577-605.

Easley, David, and Maureen O’Hara, 2004, Information and the cost of capital, Journal of Finance 59, 1553-1583.

Easley, David, Søren Hvidkjær, and Maureen O’Hara, 2002, Is information risk a determinant of asset returns?, Journal of Finance 57, 2185-2221.

Easley, David, Nicholas M. Kiefer, and Maureen O’Hara, 1997, A day in the life of a very common stock, Review of Financial Studies 10, 805-835.

Easley, David, Nicholas M. Kiefer, Maureen O’Hara, and Joseph B. Paperman, 1996, Liquidity, information, and infrequently traded stocks, Journal of Finance 51, 1405-1436.

Eleswarapu, Venkat R., 1997, Cost of Transacting and Expected Returns in the Nasdaq market, Journal of Finance 52, 2113-2127.

Ellul, Andrew, and Marios Panayides, 2007, Do ﬁnancial analysts restrain insiders’ informational advantage?, Unpublished working paper, Indiana University.

Fishman, Michael J., and Kathleen M. Hagerty, 1995, The incentive to sell ﬁnancial market information, Journal of Financial Intermediation 4, 95-115.

Glosten, Lawrence R., and Paul R. Milgrom, 1985, Bid, ask and transaction prices in a specialist market with heterogeneously informed traders, Journal of Financial Economics 14, 71-100.

Grossman, Sanford J., and Joseph Stiglitz E., 1980, On the impossibility of informationally eﬃcient markets, American Economic Review 70, 393-408.

Hasbrouck, Joel, and Duane J. Seppi, 2001, Common factors in prices, order ﬂows and liquidity, Journal of Financial Economics 59, 383-411.

Hellwig, Martin F., 1980, On the aggregation of information in competitive markets, Journal of Economic Theory 22, 477-498.

Hong, Harrison, and Jeﬀrey D. Kubik, 2003, Analyzing the analysts: Career concerns and biased earnings forecasts, Journal of Finance 58, 313-351.

Hong, Harrison, and Marcin Kacperczyk, 2007, Competition and bias, Unpublished working paper, Princeton University.

Huang, Ming, 2003, Liquidity shocks and equilibrium liquidity premia, Journal of Economic Theory 109, 104-129.

Kecskes, Ambrus, and Kent Womack, 2007, Adds and drops of analyst coverage: Does the stock market overreact?, Unpublished working paper, Dartmouth College.

Khorana, Ajay, Simona Mola, and P. Raghavendra Rau, 2007, Is there life after loss of analyst coverage?, Unpublished working paper, Purdue University.

Kyle, Albert S., 1985, Continuous auctions and insider trading, Econometrica 53, 1315-1335. Jones, Charles M., 2002, A century of stock market liquidity and trading costs, Unpublished working paper, Columbia University. Lesmond, David A., Joseph P. Ogden, and Charles A. Trzcinka, 1999, A new estimate of transaction costs, Review of Financial Studies 12, 1113-1141. Lin, Hsiou-wei, and Maureen F. McNichols, 1998, Underwriting relationships, analysts’ earnings forecasts and investment recommendations, Journal of Accounting and Economics 25, 101-127. McFadden, Daniel L., 1974, Conditional Logit Analysis of Qualitative Choice Behavior, in Frontiers in Econometrics, edited by Paul Zarembka, New York: Academic Press.

McNichols, Maureen, and Patricia C. O’Brien, 1997, Self-selection and analyst coverage, Journal of Accounting Research 35, 167-199.

Michaely, Roni, and Kent L. Womack, 1999, Conﬂict of interest and the credibility of underwriter analyst recommendations, Review of Financial Studies 12, 653-686.

Mohanram, Partha, and Shiva Rajgopal, 2007, Is information risk (PIN) priced?, Unpublished working paper, Columbia University.

Pastor, Lubos, and Robert F. Stambaugh, 2003, Liquidity risk and expected stock returns, Journal of Political Economy 111, 642-685.

Politis, Dimitris N., and Halbert White, 2004, Automatic block-length selection for the dependent bootstrap, Econometric Reviews 23, 53-70.

Politis, Dimitris N., and Joseph P. Romano, 1994, The stationary bootstrap, Journal of the American Statistical Association 89, 1303-1313.

Sadka, Ronnie, 2006, Momentum and post-earnings-announcement drift, Journal of Financial Economics 80, 309-349.

Scherbina, Anna, 2008, Suppressed negative information and future underperformance, Review of Finance 12, 533-565.

Veldkamp, Laura, 2006, Media frenzies in markets for ﬁnancial information, American Economic Review 96, 577-601.

- Wang, Jiang, 1993, A model of intertemporal asset prices under asymmetric information, Review of Economic Studies 60, 249-282.
- Wang, Jiang, 1994, A model of competitive stock trading volume, Journal of Political Economy 102, 127-168. West, Kenneth D., 1988, Dividend innovations and stock price volatility, Econometrica 56, 37-61.

Womack, Kent, 1996, Do brokerage analysts’ recommendations have investment value?, Journal of Finance 51, 137-167.

Xu, Li, 2006, Institutional investing activities and ﬁrms’ information environments before and after sell-side analyst coverage initiation and termination, Unpublished working paper, Duke University.

## Appendix A: Proof of Proposition 1

In all cases, investor i solves max

E[−eCi|Fi] s.t. Ci = R(W0 − D˜i) + D˜i(u − RP), i ∈ {informed,uninformed} (8)

D˜i

where D˜i is investor i’s demand for the risky asset, and subscript i denotes whether or not the investor observes the signal. Optimal demand is therefore given by

E[u|Fi] − RP V [u|Fi]

Di =

(9)

where V [u|Fi] denotes the variance of u conditional on information set Fi.

- Case 1: Symmetric Information An informed investor’s expectation for the risky asset payoﬀ, making use of the multivariate

Gaussian nature of the model, is

E[u|Fi] = E[u|s] = θ +

σ2u σ2u + σ2v

s (10)

while the variance of u conditional on the signal is

V [u|s] = σ2u 1 −

σu2 σ2u + σ2v

. (11)

The current case assumes symmetry with all investors informed. The market-clearing condition

equates total optimal demand under symmetric information with total supply, Dinformed = X, implying

Psymm =

1 R

(E[u|s] − XV [u|s]) (12)

=

1 R

θ +

σ2u σu2 + σ2v

s − σu2(1 −

σ2u σ2u + σ2v

)X (13)

- Case 2: Asymmetric Information In the absence of an analyst, a fraction δ of the investors pay c to obtain the payoﬀ signal s.

Uninformed investors base their demand solely on the observed price. To do this, they must ﬁlter from the price a noisy inference of the informed investors’ signal. Under rational expectations, the uninformed know the price is linear in the informed investors’ signal and the asset’s supply, that is,

P = c1 + c2s + c3X. (14)

For now, we use this price form as a conjecture to be veriﬁed in equilibrium, at which point we also solve for the constants c1, c2, and c3.

The conditional moments of u given an uninformed investor’s information set are:

c2σ2u c22(σu2 + σ2v) + c32σ2x

(c2s + c3[X − X¯]) (15)

E[u|FUI] = E[u|P] = θ +

c22σ2u c22(σ2u + σv2) + c23σx2

V [u|P] = σ2u 1 −

. (16)

When a fraction δ of investors are informed, the equilibrium price is found from the marketclearing condition δDinformed + (1 − δ)Duninformed = X, giving

−1 δE[u|s] V [u|s]

(1 − δ) V [u|P]

(1 − δ)E[u|P] V [u|P] − X (17)

δ V [u|s]

1 R

Pasymm =

+

+

We can use conditional moments (15) and (16) to show that Pasymm is indeed linear in the informed investors’ signal and the asset’s supply. Matching the coeﬃcients on s and X with the conjectured form (14) and solving for c2 and c3 gives

δ σ2u δ + σ2v σ2x R σ2x σv4 + δ2 + δ σ2u σ2x σ2v + σu2 δ2

c2 =

(18)

c3 = −σ2v σ2u δ + σ2v σ2x R σ2x σv4 + δ2 + δ σu2 σ2x σ2v + σ2u δ2

. (19)

Finally, we can write c1 as a function of c2 and c3:

c1 =

−1

c22 σ2u c22 ( σ2u + σ2v) + c32 σ2x

1 − δ R

θ R −

c2 c3 X¯ c22 σ2u + σ2v + c32 σx2 −1 1 −

−1 −1

−1

σ2u σ2u + σv2

c22 σ2u c22 ( σ2u + σv2) + c32 σ2x

1 − δ σ2u

δ σ2u

1 −

1 −

×

+

. (20)

The expressions shown in Proposition 1 follow directly from using these solutions in the price and demand expressions, and noting that the unconditional expectations of the signal and supply are zero and X¯, respectively.

- Table I. Coverage Terminations: Summary Statistics. The sample consists of 14,939 coverage terminations (though the sample size varies depending on the availability of variables of interest). This table reports summary statistics for the market value of equity, share turnover (monthly volume divided by shares outstanding), daily return volatility, and the extent of coverage for each stock in the terminations sample; the CRSP universe (share codes 10 and 11); and the universe of stocks with analyst coverage in the union of the Reuters and I/B/E/S databases. For each firm in the terminations sample, we calculate equity value and turnover in the month prior to the first termination date. For the universes of CRSP stocks and covered stocks, these are first computed as monthly averages for 2002 (the midpoint of our sample period) firm-by-firm and then averaged cross-sectionally. Annualized volatility for terminations is the standard deviation of daily continuously compounded returns in the six-month period ending one month prior to a termination, times √252 (a sample firm is omitted from this calculation if it has fewer than three months, or 66 trading days, of non-missing returns.) For the universes of CRSP stocks and covered stocks, volatilities are the annualized daily standard deviations for firms in these samples during calendar year 2002. We exclude firms with fewer than 200 nonmissing return observations in the CRSP database. The number of brokers covering a stock in our terminations sample over the three months prior to the drop is based on combining data from the Reuters and I/B/E/S datasets. The broker count for the universe of covered stocks represents the number of unique brokers that covered each stock in the Reuters or I/B/E/S databases during the three months prior to June 30, 2002. The broker counts are then averaged cross-sectionally.

Universe of Terminations sample

CRSP universe in 2002

covered stocks in 2002 Equity market value ($m)

Mean 3,782.4 2,197.2 3,254.5 Median 533.3 145.8 384.8 Range 1.5 – 367,265 3.0 – 369,002 0.9 – 369,002

Monthly turnover

Mean 0.16 0.11 0.14 Median 0.10 0.06 0.09 Range 0 – 2.58 0 – 2.96 0 – 2.86

Daily return volatility (annualized %)

Mean 65.6 71.8 65.2 Median 56.7 58.9 55.6 Range 11.5 – 332.2 5.4 – 606.0 5.4 – 519.3

Number of brokers covering stock

Mean 6.4 5.9 Median 4.0 4.0 Range 1 – 43 1 – 46

Number of firms 4,022 5,796 3,827

- Table II. The Effect of Coverage Terminations on Information Asymmetry. The table reports cross-sectional means of proxies for information asymmetry before and after a termination for sample stocks and their matched controls. For each sample termination, a control group is formed by randomly selecting five stocks with the same Daniel et al. (1997) style-benchmark assignment in the month of June prior to a termination, subject to the conditions that control firms a) were covered by one or more analysts in the three months before the event and b) did not themselves experience a coverage termination in the quarter before and after the event. (We lose 1,395 events involving stocks that do not satisfy Daniel et al.’s data conditions. We also drop observations that have no viable controls for a given test. The number of observations ranges from around 12,000 to around 14,000.) We then calculate a difference-in-

difference test for each sample stock i, DiD =(posti − prei) −(post − preControl Group i), and report the cross-sectional mean. We also report the mean percentage change (DiD/mean before – 1). Panel A reports the mean probability of informed trading for stocks in the termination sample in the quarters immediately preceding and following the quarter in which the coverage termination occurred. We use Stephen Brown’s quarterly PIN estimates. Panel B reports changes in bid-ask spreads. Spreads are computed as (ask–bid)/(ask+bid)/2 using daily closing bid and ask data from CRSP. This and the next two statistics are averaged over six-month and 12-month windows ending 10 days prior to the termination announcement or starting 10 days after the announcement date. Panel C reports changes in the log Amihud illiquidity measure. This is defined as the natural log of the ratio of the stock return to the dollar trading volume and scaled by 106; see Amihud (2002, p. 43). Panel D reports the changes in the number of days with zero or missing returns in CRSP (using missing return codes -66, -77, -88, and -99). Panel E reports the effects of terminations on quarterly earnings announcements. The first measure is the log of daily return volatility in a three-day window around earnings announcements for all earnings announcements occurring in a one-year window before or after the drop. The second measure is the mean absolute value of quarterly earnings surprises in a one-year window before or after the drop. A surprise is defined as the absolute value of actual quarterly earnings minus the latest I/B/E/S consensus estimate before the earnings announcement, scaled by book value of equity per share, and multiplied by 100 for expositional purposes. Earnings surprise cannot be computed for orphaned stocks. To adjust for potential cross-sectional dependence due to overlapping estimation windows, p-values for the difference-in-difference tests are calculated using a block bootstrap (with optimal block length chosen according to the optimality criterion of Politis and White (2004)).

Economic magnitude (percentage Before After Before After DiD DiD = 0 change)

Terminations Control group Mean p-value

- Panel A: PIN PIN 0.142 0.144 0.152 0.152 0.002 0.002 1.6%
- Panel B: Bid-ask spreads 6-month window 0.206 0.183 0.232 0.201 0.007 <0.001 3.4% 12-month window 0.206 0.156 0.229 0.172 0.007 0.002 3.3%
- Panel C: Amihud illiquidity measure (AIM) 6-month window -3.892 -3.966 -3.585 -3.706 0.046 <0.001 1.2% 12-month window -3.889 -4.069 -3.562 -3.816 0.075 <0.001 1.9%
- Panel D: Missing and zero-return days 6-month window 3.505 3.675 3.927 3.848 0.249 <0.001 7.1% 12-month window 7.133 6.948 8.223 7.107 0.931 <0.001 13.1%
- Panel E: Earnings announcements Volatility 1.360 1.293 0.857 0.763 0.028 <0.001 2.0% Earnings surprise 0.760 0.890 0.816 0.864 0.082 <0.001 10.8%

- Table III. Conditional Choice Model of Sector Terminations. We test whether a brokerage firm terminates sector coverage selectively based on the sector’s past or future performance, which would undermine our claim that sector terminations contain no information relevant to the valuation of the stocks that lose coverage. The test is a based on a McFadden (1974) choice model. We model a brokerage firm’s choice of which sectors to stop covering at time t. To be included in the estimation sample, we require that the brokerage firm drop at least one sector at time t (so we model the choice of which sectors are terminated conditional on the firm’s decision to downsize research). We exclude brokerage firms that close down their research departments altogether (i.e., those that drop every sector they cover). For each broker, the choice set from which sector terminations are drawn includes all sectors the broker covers at time t. The unit of analysis is hence a broker-sector pair. The dependent variable equals one if a sector is chosen for termination and zero otherwise. Brokers are assumed to select those sectors whose termination will maximize their expected profit. Sectors are defined using six-digit GICS codes and sector terminations are identified from the sources described in Section II. The explanatory variables are defined as follows. Prior and future sector performance is measured as average market-adjusted cumulative returns in the sector over the twelve months before and after the decision date, respectively, using the CRSP value-weight index to make the market adjustment. Prior and future sector earnings surprises are measured as realized quarterly earnings per share minus consensus (i.e., median) forecasts and scaled by book value of equity per share, averaged over the prior four or next four quarters, respectively, and across stocks in the same GICS code. Sector characteristics include return volatility (measured over the prior twelve months and averaged across stocks in the same GICS); a proxy for competition from other brokers (the log of one plus the number of other brokers covering the sector during the three months preceding the termination decision); and two proxies for the fee income a sector generates for the brokerage firm in question, in the form of trading commissions and investment banking fees. To proxy for trading commissions, we compute the log aggregate dollar trading volume of only those stocks in a sector that the brokerage firm covered in the month before the termination decision. Sectors in which the brokerage firm covers few stocks, or with covered stocks that are associated with low dollar trading volumes, generate lower trading commissions. To proxy for the investment banking fees a brokerage firm earns in a given sector, we compute the log of the aggregate equity proceeds raised in the 12 months prior to a termination decision by those companies in the sector whose stocks were covered by the brokerage firm’s analyst and for which the brokerage firm acted as the lead underwriter. (We use data for the prior 12 months since equity issuance is a relatively rare event.) Analyst characteristics include a dummy set equal to one if the analyst covering the sector was ranked first, second, or third in his sector in the annual Institutional Investor (II) all-star rankings (as of the October issue preceding the sector termination); the analyst’s forecast accuracy relative to his sectormatched peers at other brokerage firms (constructed as in Hong and Kubik (2003)); his experience (the log of one plus the number of years the analyst has contributed forecasts to I/B/E/S); and his tenure with the broker (the log of one plus the number of years the analyst has worked for this brokerage firm). Where more than one analyst covers a sector, we compute the maximum value across team members, though our results are not sensitive to this coding. The model is estimated using probit without (column 1) or with random brokerage-firm effects (column 2). In column (1), standard errors are clustered within brokerage firms to reduce the influence of overlapping observations. The random-effects probit in column (2) cannot accommodate clustered standard errors. We use ***, **, *, and † to denote statistical significance at the 0.1%, 1%, 5%, and 10% levels (two-sided), respectively. In addition to the probit coefficients, we report marginal effects as well as economic effects (i.e., marginal effects times a one-standard deviation change in continuous covariates).

### Table III. Continued.

Dependent variable =1 if broker terminates sector coverage, = 0 otherwise

[Figure 1]

[Figure 2]

Economic effect Marginal

Economic

Marginal

effect Coefficient s.e.

effect (dF/dx)

(dF/dx times s.d.)

Coefficient s.e.

effect (dF/dx)

(dF/dx times s.d.)

Sector performance market-adjusted return in prior 12 months -0.061 -0.006 -0.003 -0.066 -0.008 -0.003

0.065 0.064

market-adjusted return in next 12 months -0.025 -0.002 -0.001 0.020 0.002 0.001

0.088 0.089

average earnings surprise in prior 4 quarters -0.006 -0.001 0.000 -0.010 -0.001 -0.001

0.039 0.040

average earnings surprise in next 4 quarters 0.059 0.006 0.003 0.059 0.007 0.004

0.044 0.044

Sector characteristics return volatility in prior 12 months -0.846† -0.082 -0.006 -1.060* -0.123 -0.009

0.467 0.442

no. of other brokers covering the sector -0.007 -0.001 0.000 -0.072 -0.008 -0.005

0.049 0.049

log lagged monthly dollar trading volume -0.058*** -0.006 -0.008 -0.037† -0.004 -0.006

0.018 0.020

log equity proceeds raised through broker, LTM -0.070*** -0.007 -0.016 -0.063*** -0.007 -0.018

0.013 0.014

###### Analyst characteristics

=1 if one or more team members are II “all-stars” -0.584*** -0.049 -0.049 -0.575*** -0.059 -0.059

0.077 0.075

analyst relative forecast accuracy -1.682*** -0.164 -0.015 -1.613*** -0.188 -0.017

0.258 0.256

log analyst experience -0.066 -0.006 -0.004 -0.081* -0.009 -0.006

0.043 0.041

log analyst tenure with broker -0.061* -0.006 -0.005 -0.039 -0.005 -0.004

0.026 0.029

Diagnostics Brokerage-firm random effects No Yes Wald-test: random effects = 0 (χ2) n.a. 52.7*** Wald-test: all coef. = 0 (χ2) 267.5*** 196.1*** Wald-test: all year effects = 0 (χ2) 4.2 3.5 Observed probability 0.063 0.063 Pseudo-R2 8.4 % 9.6 % No. of observations 8,804 8,804

- Table IV. Changes in Price Around Coverage Terminations. We compute abnormal returns over three different windows using two separate benchmarks: The market model and the Fama-French three-factor model. (Results are nearly identical if we include a Carhart (1997) momentum factor in the Fama-French model.) We use the CRSP value-weight index to proxy for the market return. We report these abnormal return metrics for the overall sample (Panel A) as well as the subsample of terminations that do not coincide with a negative earnings surprise within one week of the termination date (Panel B) and the subsample of closure-related terminations (Panel C), and broken down by the number of other brokers covering the stock in the three months preceding the coverage termination, based on pooling data from Reuters Estimates and I/B/E/S (Panel D). To correct for after-hours announcements, we use time stamps to determine the first trading day after the announcement where available. Abnormal returns are reported in percent. We report test statistics that control for event-induced variance changes. For the market model abnormal returns, we report both the parametric Boehmer, Musumeci, and Poulsen (1991) standardized crosssectional test and Cowan’s (1992) non-parametric generalized sign test statistic (separated by “/”). For the Fama-French model, we report Brown and Warner’s (1980) “crude dependence adjustment” t-test and the generalized sign test (separated by “/”). We use ***, **, and * to denote statistical significance at the 0.1%, 1%, and 5% levels (two-sided), respectively. The sample falls short of 14,939 because we require 50 trading days of pre-event stock prices to estimate the model parameters.

# of other brokers covering the stock in the prior 3 months

Fama-French three-factor model

Estimation window: Close on day before termination to …

No. of obs. Market model

- Panel A: All terminations … close on day of termination [-1,0] 14,890 -0.56 ***/*** -0.51 ***/*** … close on day +1 [-1,+1] 14,890 -0.64 ***/*** -0.60 ***/*** … close on day +3 [-1,+3] 14,890 -0.71 ***/*** -0.66 ***/***
- Panel B: Terminations excluding coincident negative earnings surprises … close on day of termination [-1,0] 14,405 -0.52 ***/*** -0.47 ***/*** … close on day +1 [-1,+1] 14,405 -0.58 ***/*** -0.55 ***/*** … close on day +3 [-1,+3] 14,405 -0.60 ***/*** -0.57 ***/***
- Panel C: Closure-related terminations … close on day of termination [-1,0] 1,788 -1.66 ***/*** -1.14 ***/*** … close on day +1 [-1,+1] 1,788 -2.59 ***/*** -1.97 ***/*** … close on day +3 [-1,+3] 1,788 -4.02 ***/*** -2.91 ***/***
- Panel D: Terminations by number of brokers covering the stock … close on day of termination [-1,0] 0 1,330 -0.99 ***/*** -0.94 ***/***

1-5 3,847 -0.72 ***/*** -0.65 ***/*** 6-10 3,353 -0.54 ***/*** -0.47 ***/***

11-15 2,383 -0.43 ***/*** -0.40 ***/***

>15 3,977 -0.35 ***/*** -0.31 ***/*** … close on day +1 [-1,+1] 0 1,330 -1.03 ***/*** -1.03 ***/***

1-5 3,847 -0.74 ***/*** -0.69 ***/*** 6-10 3,353 -0.55 ***/*** -0.50 ***/***

11-15 2,383 -0.58 ***/*** -0.55 ***/***

>15 3,977 -0.52 ***/*** -0.50 ***/*** … close on day +3 [-1,+3] 0 1,330 -1.23 ***/** -1.29 ***/**

1-5 3,847 -0.72 ***/*** -0.65 ***/*** 6-10 3,353 -0.63 ***/** -0.56 ***/* 11-15 2,383 -0.76 ***/*** -0.69 ***/***

>15 3,977 -0.56 ***/*** -0.53 ***/***

- Table V. Changes in Institutional Holdings Around Coverage Terminations. The table reports the quarterly change in institutional investors’ holdings of stocks that experience coverage terminations. We report the mean fraction of total stock outstanding that is held in aggregate by institutional investors filing 13f reports in the quarter before and the quarter after a termination. We then calculate a difference-in-difference test, DiD

=(posti − prei) −(post − preControl Group i), that is, the difference between the pre- and post-termination change for sample stock i less the average change for control stocks. We also report percentage changes (DiD/mean before – 1). Control groups are formed as described in Table II. Panel A reports these statistics for the entire sample of coverage terminations.

- Panel B restricts the sample to closure-related terminations. Panel C provides a breakdown by the number of other brokers covering the stock in the three months preceding the coverage termination, using the whole sample. The 13f data are taken from Thomson Financial’s CDA/Spectrum database. We lose 2,342 events involving stocks that do not satisfy DGTW’s data conditions and 29 events with missing 13f data for either the sample firm or the controls. To adjust for potential crosssectional dependence due to overlapping estimation windows, p-values for the difference-in-difference tests are calculated using a block bootstrap (with optimal block length chosen according to the optimality criterion of Politis and White

(2004)). Significance levels of “own”-difference test statistics (posti – prei) are similar (not reported).

# of other brokers covering the stock in the Terminations Control group

Economic magnitude

[Figure 3]

prior 6 No. of Before After Before After Mean p-value (percentage bin months obs. drop drop drop drop DiD DiD = 0 change)

- Panel A: All terminations (in %) All 12,568 61.9 62.9 58.3 58.5 0.9 <0.001 1.4%
- Panel B: Closure sample (in %) All 1,473 61.0 61.4 57.9 57.6 0.6 0.023 1.0%
- Panel C: Terminations by number of brokers covering the stock (in %)

- 0 0 1,078 36.6 37.3 39.5 38.9 1.4 <0.001 3.7%
- 1 1-5 3,081 55.4 56.9 50.6 51.1 1.0 <0.001 1.7%
- 2 6-10 2,863 67.0 67.8 60.8 61.1 0.6 0.009 0.9%
- 3 11-15 2,072 68.7 70.0 64.5 64.7 1.1 <0.001 1.6%
- 4 >15 3,474 67.1 68.1 66.4 66.5 0.8 <0.001 1.2%

- Table VI. Cross-sectional Determinants of Changes in Price. We test the cross-sectional predictions of the model presented in Section I by regressing Fama-French-adjusted cumulative abnormal returns around coverage terminations on proxies for δ(the fraction of informed investors); X (mean aggregate supply); (variance of aggregate supply); (payoff variance); and (signal noise). The main proxy for δis the

###### σx σu2 σv2

2

fraction of the company’s stock held by institutional investors as of the quarter-end prior to the termination, estimated from 13f data. In column (3), we add the size of the brokerage firm’s sales force (i.e., the number of registered representatives), taken from the Factbook of the Securities Industry and Financial Markets Association and dated January 1 of the termination year. Mean and variance of aggregate supply are based on the first two moments of the distribution of log daily turnover, estimated over the six months ending one month prior to the termination. Our proxy for payoff variance is the standard deviation of the year-on-year growth rate in quarterly earnings per share, using up to 20 quarters of data prior to the termination. We parameterize signal noise as a function of the number of remaining analysts covering the stock; three proxies for the quality of the analyst whose coverage is lost (see Table III); and (in column 4) the level and square of analyst forecast dispersion, defined as the time series mean of the standard deviation of analyst EPS forecasts in the year prior to the termination, scaled by book value per share. We also control for whether the termination coincides with a negative earnings surprise as well as firm fixed effects (using CRSP permnos) and announcement-year effects. (To conserve space, the firm and year effects are not reported.) Column (2) restricts the sample to closure-related terminations. Heteroskedasticity-consistent standard errors, clustered on CRSP permnos, are reported in italics beneath the coefficient estimates. We use ***, **, *, and † to denote significance at the 0.1%, 1%, 5%, and 10% levels (two-sided), respectively.

Dependent variable: Fama-French CAR [-1,0], in % (1) (2) (3) (4)

[Figure 4]

[Figure 5]

δ 13f holdings in quarter before drop 0.489** 1.356* 0.451* 0.551**

0.191 0.679 0.209 0.200

(1−δ) log no. of retail registered representatives -0.032**

0.011

δ log no. of institutional registered reps 0.005

0.019

X mean daily log turnover -0.301*** -0.785*** -0.291*** -0.304***

0.045 0.189 0.050 0.049

σx std. dev. of log turnover -0.351** -1.198** -0.331* -0.312*

2

0.131 0.460 0.142 0.147

- σu std. dev. of earnings growth -0.361† -1.487† -0.341 -0.370†

0.207 0.909 0.279 0.210

2

- σv log no. other brokers covering the stock 0.186*** 0.100 0.179*** 0.161***

2

0.046 0.181 0.051 0.050

σv =1 if covering analyst was an “all-star” -0.323* -2.041** -0.290* -0.276*

2

0.138 0.727 0.140 0.140

σv log experience of covering analyst -0.139** -0.377 -0.156** -0.142**

2

0.049 0.230 0.054 0.050

σv relative forecast accuracy of covering analyst -0.858* -8.824*** -1.018* -1.035**

2

0.353 1.484 0.401 0.354

σv analyst forecast dispersion -4.991†

2

3.027

σv analyst forecast dispersion2 10.046*

2

4.732

=1 if coincides w/ neg. earnings surprise -2.829*** -2.478† -3.084*** -2.844***

0.689 1.277 0.763 0.693

Adjusted R-squared 37.2% 15.6% 39.3% 36.3% Wald test: all coef. = 0 8.3*** 7.5*** 7.6*** 7.4*** No. of observations 13,371 1,579 11,484 12,791

- Table VII. Cross-sectional Determinants of Changes in Informed Demand. We test the cross-sectional predictions of the model presented in Section I by regressing a proxy for changes in informed demand around coverage terminations on proxies for δ(the fraction of informed investors); X (mean aggregate supply);

(variance of aggregate supply); (payoff variance); and (signal noise). Our proxy for the change in informed

###### σx σu2 σv2

2

demand is the difference-in-difference (DiD) change in the fraction of the company’s stock held by institutional investors from the quarter before to the quarter after a coverage termination, net of the mean contemporaneous change in institutional holdings in matched control firms. See Table V for details of the construction. The proxies for the independent covariates are as defined in Table VI. We also control for whether the termination coincides with a negative earnings surprise as well as firm fixed effects (using CRSP permnos) and announcement-year effects. (To conserve space, the firm and year effects are not reported.) As in Table V, we lose 2,342 events involving stocks that do not satisfy DGTW’s data conditions and 29 events with missing 13f data for either the sample firm or the controls. The number of observations used in each regression depends on data availability for the proxies. Column (2) restricts the sample to closure-related terminations. Heteroskedasticity-consistent standard errors, clustered at the CRSP permno level, are reported in italics beneath the coefficient estimates. We use ***, **, *, and † to denote statistical significance at the 0.1%, 1%, 5%, and 10% levels (twosided), respectively.

Dependent variable: DiD change in 13f holdings

[Figure 6]

[Figure 7]

(1) (2) (3) (4)

δ 13f holdings in quarter before drop -0.443*** -0.343*** -0.459*** -0.444***

0.024 0.069 0.027 0.020

(1−δ) log no. of retail registered representatives 0.000

0.000

δ log no. of institutional registered reps -0.001

0.001

X mean daily log turnover 0.016*** 0.019 0.015*** 0.015***

- 0.004 0.014 0.004 0.003

std. dev. of log turnover 0.014*** -0.003 0.012** 0.014***

- 0.004 0.014 0.004 0.004

σx

2

- σu

2

- σv

2

std. dev. of earnings growth 2.810*** 6.459** 2.852*** 2.869***

0.654 2.203 0.730 0.559

log no. other brokers covering the stock 0.001 -0.013 0.000 0.001

- 0.003 0.015 0.004 0.003

=1 if covering analyst was an “all-star” 0.007† 0.013 0.009* 0.007†

- 0.004 0.029 0.004 0.004

σv

2

###### σv

2

log experience of covering analyst 0.000 -0.001 0.003* 0.003*

0.000 0.001 0.001 0.001

σv

2

relative forecast accuracy of covering analyst 0.013 -0.037 0.013 0.013

0.009 0.037 0.010 0.010

σv

2

analyst forecast dispersion 0.013*

0.006

σv

2

analyst forecast dispersion2 -0.003*

0.001

=1 if coincides w/ neg. earnings surprise -0.017* 0.035 -0.013† -0.017***

0.007 0.038 0.008 0.007

Adjusted R-squared 45.3% 19.9% 48.1% 45.4% Wald test: all coef. = 0 30.7*** 4.0*** 24.1 26.9*** No. of observations 11,591 1,355 9,974 11,364

### Table VIII. Changes in Factor Loadings Following Coverage Terminations.

The table reports changes in equity return factor loadings around coverage terminations. We estimate four-factor models of firms’ monthly stock returns in excess of the risk-free rate, denoted e

ri,t . The four factors are MKT (the excess of the

mo -fr ren

nthly market return over the risk ee rate); SMB (the diffe ce between the monthly returns of a value-weighted portfolio of small stocks and one of large stocks); HML (the difference between the monthly returns of a value-weighted portfolio of high book-to-market stocks and one of low book-to-market stocks); and one of three liquidity-risk factors, LIQ: Sadka’s (2006) liquidity factor (Panel A), Pastor and Stambaugh’s (2003) nontraded liquidity factor (Panel B), and Pastor and Stambaugh’s traded liquidity factor (Panel C). The MKT, SMB, and HML factor series come from Kenneth French’s website. All three LIQ factor series come from WRDS. Note that data for Pastor and Stambaugh’s traded liquidity factor in

- Panel C is only available through 2004. The regression model is estimated with monthly data using 12-, 18-, or 24-month windows ending the month before a termination and beginning one month after. (If the termination occurred after the 15th day of a month, the post-termination window starts in the second month following the event.) The model takes the form

ri,t =α + (β + Δ β I ∈ + Δβ & I ∈ I ∈ )Factors +ε, , where It∈Post is an indicator for the post-event period; Ii∈Term identifies firms in the terminations sample (as opposed to matched control firms, identified as in Table II); and Factors is a vector wh

e

Post i i

Post Term t Post

t Post i Term t i t

The n-difference coefficients ΔβPost&Term capture o erience

difference-i

ich includes the aforementioned factors.

eth mpared to otherwise similar control firms that exp

wh

er a stock’s risk loadings change following a termination, c no termin n. To estimate the model, we impose the restricti a tw -ste approach analogous to Pastor and Stambaugh’s equ and control groups, we concatenate the pre- and post-even retur serie . In el firm-by-firm

atio hat ΔβPost and Post&Term are co on to all firms p

and o )- 3) minatio l

on t ations (1

Δβ

mm ach f

use 1 . Specificall for e irm in he ter n

(1

t t s a

y,

- im s step 1, we estimate the above mod βˆ Factorst

s S and

tack al s’ dat construct

a a si e cross ls

n nd firm in ngl sectional t eL residua

= t −α − . tep, pooled r ion

using O

η ri,

e

i,t

i

i

vari η = c + (ΔβPostI + ΔβPost&TermI I )Factor % of th o

egress

le in

ab a second-s , deal with o tliers, we trim 0.5

We use these residuals as the dependent i,t t∈Post t∈Post i∈Term st +νi,t . To

u

e observati ns from

h t (Results are robust to degree of trimm no control firms with sufficient data

e also exclude samp w h

eac ail. ing and to winsorizing the residuals instead.) W le firms for hic are availabl To save space, we report only the coefficients of interest, ΔβPost&Te ependence arising from th orrelatio ina ues, re square br nt estimates, are calculat block b (with blo of 20).

e.

rm

. To adjust for potential d ackets below the coefficie

e serial c ed using a

n of term ootstrap

tions, p-val ck length

ported in

Change ading minations relat o trol firm st&Term)

s for ter ive to c s (ΔβPo

in factor lo n

mation

Row Esti

[Figure 8]

[Figure 9]

# window MKT SMB HML LIQ

###### Panel A: Sadka liquidity factor

(1) 12-month -0.08 00 0. 70

0.

00 0.

[<.001] .982] [<.001

[0

[0.750] ]

- (2) 18-month -0 [0.643

01 0.

[0.686] ]

- (3) 24-month -0 [0

04 0.

[0.052] ]

trade factor

- (4) 12-month -0.05 0. 0.02 [ 0.170] ]
- (5) 18-m .03 0.

.0

- (6) 24-m .05 0.

- -0.05 .01 0. 68 [<.001] ] [<.001
- -0.07 .01 0. 59 [<.001] .821] [<.001

###### Panel B: Pastor-Stambaugh non d liquidity

00 0.03

[0.004] 0.618] [ [0.085

- onth -0.06 0.01 0 02 [<.001] [0.325] [0 68] [0.004]
- onth -0.07 0.01 0 01 [<.001] [0.766] [0 06] [0.323] augh tr idity fact

.0

###### Panel C: Pastor-Stamb

###### aded liqu or

(7) 12-month -0.10 01 0.07

0. 0.02

[<.001] .350] [0.00

[0 [0.138] 2]

(8) 0. 0.03

18-month -0.06 06 0.02

] [ [0.046 0 47]

[<.001 <.001] ] [ .1

(9) 24-month -0.06 0.04 0.04 0.04

[<.001] [0.018] [<.001] [<.001]

