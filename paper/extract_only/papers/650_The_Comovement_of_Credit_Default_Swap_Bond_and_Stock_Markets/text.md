 
 
 
 
DISCUSSION PAPER SERIES 
 
 
 
     ABCD 
 
www.cepr.org 
 
 
 
Available online at: www.cepr.org/pubs/dps/DP4674.asp and www.ssrn.com/abstract=635981
 
www.ssrn.com/xxx/xxx/xxx
  
 
 
 
 
 
 No. 4674 
 
THE COMOVEMENT OF CREDIT 
DEFAULT SWAP, BOND AND STOCK 
MARKETS: AN EMPIRICAL ANALYSIS 
 
 
Lars Norden and Martin Weber 
 
 
  FINANCIAL ECONOMICS 
 
 
 

ISSN 0265-8003 
THE COMOVEMENT OF CREDIT  
DEFAULT SWAP, BOND AND STOCK  
MARKETS: AN EMPIRICAL ANALYSIS 
Lars Norden, Universität Mannheim 
Martin Weber, Universität Mannheim and CEPR 
 
Discussion Paper No. 4674 
October 2004 
Centre for Economic Policy Research 
90–98 Goswell Rd, London EC1V 7RR, UK 
Tel: (44 20) 7878 2900, Fax: (44 20) 7878 2999 
Email: cepr@cepr.org, Website: www.cepr.org 
This Discussion Paper is issued under the auspices of the Centre’s research 
programme in FINANCIAL ECONOMICS. Any opinions expressed here are 
those of the author(s) and not those of the Centre for Economic Policy 
Research. Research disseminated by CEPR may include views on policy, but 
the Centre itself takes no institutional policy positions. 
The Centre for Economic Policy Research was established in 1983 as a 
private educational charity, to promote independent analysis and public 
discussion of open economies and the relations among them. It is pluralist 
and non-partisan, bringing economic research to bear on the analysis of 
medium- and long-run policy questions. Institutional (core) finance for the 
Centre has been provided through major grants from the Economic and 
Social Research Council, under which an ESRC Resource Centre operates 
within CEPR; the Esmée Fairbairn Charitable Trust; and the Bank of 
England. These organizations do not give prior review to the Centre’s 
publications, nor do they necessarily endorse the views expressed therein. 
These Discussion Papers often represent preliminary or incomplete work, 
circulated to encourage discussion and comment. Citation and use of such a 
paper should take account of its provisional character. 
Copyright: Lars Norden and Martin Weber 

CEPR Discussion Paper No. 4674 
October 2004 
ABSTRACT 
The Comovement of Credit Default Swap,  
Bond and Stock Markets: An Empirical Analysis* 
This Paper analyses the empirical relationship between credit default swap, 
bond and stock markets during the period 2000-02. Focusing on the 
intertemporal comovement, we examine weekly and daily lead-lag 
relationships in a vector autoregressive model and the adjustment between 
markets caused by cointegration. First, we find that stock returns lead CDS 
and bond spread changes. Second, CDS spread changes Granger cause 
bond spread changes for a higher number of firms than vice versa. Third, the 
CDS market is significantly more sensitive to the stock market than the bond 
market and the magnitude of this sensitivity increases when credit quality 
becomes worse. Finally, the CDS market plays a more important role for price 
discovery than the corporate bond market. 
JEL Classification: C32, G10 and G14 
Keywords: credit derivatives, credit risk, credit spreads and lead-lag 
relationship 
Lars Norden 
Lehrstuhl für ABWL, Finanzwirtschaft  
Insbesondere Bankbetriebslehre   
Universität Mannheim 
68131 Mannheim   
GERMANY   
Email: norden@bank.bwl.uni-mannheim.de 
 
 
 
For further Discussion Papers by this author see: 
www.cepr.org/pubs/new-dps/dplist.asp?authorid=157749 
Martin Weber 
Lehrstuhl für ABWL, Finanzwirtschaft  
Insbesondere Bankbetriebslehre   
Universität Mannheim 
68131 Mannheim   
GERMANY 
Tel: (49 62) 1181 1532  
Fax: (49 62) 1181 1534  
Email: weber@bank.bwl.uni-mannheim.de  
 
For further Discussion Papers by this author see: 
www.cepr.org/pubs/new-dps/dplist.asp?authorid=119269 
*The authors wish to thank Jens Grunert, Volker Kleff, Markus Mentz, Ingmar 
Nolte, Winfried Pohlmeier, Valeri Voev, and two members of the credit 
derivatives department from the bank who provided the CDS data for helpful 
comments and suggestions. The financial support of the German National 
Science Foundation is gratefully acknowledged. 
Submitted 09 September 2004 

 
2
1. Introduction 
In efficient markets default risk of firms should be reflected by market prices of financial 
claims on these firms. Theory suggests that there is a close link between market prices of 
different claims, for example stocks and bonds, because their value depends on the distribu-
tion of the market value of the firm’s assets. Less obvious is the empirical relationship be-
tween market prices of different credit-sensitive claims for the same firm. In particular, the 
link between the heavily growing credit derivatives market1 and traditional cash markets has 
only been explored on a limited scale so far. For this reason, we empirically analyze the co-
movement of single name credit default swap (CDS), bond and stock markets at the individ-
ual firm-level to investigate if and how these markets are connected and whether default-risk 
related information is reflected earlier in certain markets than in others. 
Besides cash markets, we are particularly interested in the credit default swap market for 
the following reasons: First, from a theoretical perspective, CDS should reflect pure issuer 
default risk, and no facility or issue specific risk, making these instruments a potentially 
“ideal” benchmark for measuring and pricing credit risk. Second, CDS have turned out to 
clearly dominate other types of credit derivatives such as credit linked notes or total return 
swaps in terms of market volume and standardization.  
On the one hand, we replicate parts of the analyses of Blanco, Brennan, and Marsh (2004), 
Longstaff, Mithal, and Neis (2003), Berndt et al. (2004), and Zhu (2004). Analyzing weekly 
and daily data from an international sample of 58 firms over the period 2000-2002, we find 
that stock returns clearly lead both CDS and bond spread changes from the same firm. Fur-
thermore, CDS spread changes Granger cause bond spread changes for a higher number of 
firms than vice versa which confirms results from related studies. A cointegration analysis of 
CDS and bond spreads and a corresponding vector error correction model reveal that the CDS 
                                                 
1 See European Central Bank (2004), Fitch Ratings (2003), British Bankers’ Association (2002) for an overview. 

 
3
market mainly contributes to price discovery which is in line with Blanco, Brennan, and 
Marsh (2004). 
On the other hand, we extend related work in the following two ways. First, note that our 
data set is richer because it covers a larger number of firms, a longer time-period, and obser-
vations from US and non-US underlyings. Second, we investigate a couple of new issues. It 
turns out that the strength of lead-lag relationships statistically depends on the average credit 
rating of the firm but not on its size. Moreover, we find that the contribution to price discov-
ery of the CDS market relative to the bond market is substantially stronger for US than for 
non-US reference entities. Finally, the result that Granger causality of the CDS market for the 
bond market (and not vice versa) prevails can be detected for firms with and without cointe-
grated credit spreads. 
These findings contribute to research on market efficiency and might be useful for market 
participants who rely on price data from different markets for trading, monitoring, or hedging 
against credit risk [see, e.g., Berndt et al. (2004) who compare the implied default risk in CDS 
spreads and Moody’s KMV’s EDFs]. In addition, regulators increasingly pay attention to the 
evolution of markets for credit risk transfer, investigating the opportunities from an improved 
risk allocation in the financial system and threats from a potential increase in systemic risk.2 
Moreover, for the first time, the Basel Committee on Banking Supervision (2004) has pro-
vided a proposal that explicitly recognizes the risk reducing effect of credit risk transfer in-
struments like CDS in a new capital adequacy framework for banks. 
The remainder of the paper is organized as follows. In Section 2, we briefly review the lit-
erature on the empirical relationship between market prices of different claims for the same 
firm and propose a set of hypotheses. Section 3 describes the data set and presents descriptive 
                                                 
2 See European Central Bank (2004), Deutsche Bundesbank (2004), and Bank for International Settlements 
(2003). Since July 2003 the Reserve Bank of Australia regularly publishes CDS spreads as complementary 
indicators of credit risk, see Arsov and Gizycki (2003). 

 
4
statistics. In Section 4, we analyze lead-lag relationships, the strength of the intertemporal 
comovement and the adjustment process between CDS and bond spreads. The paper con-
cludes with Section 5. 
 
2. Overview of related literature and hypotheses 
Before turning to the analysis, we briefly review the empirical literature that relates to our 
following three research questions and propose a set of hypotheses: 
a) What is the relationship between CDS, bond and stock markets at the firm-level? In 
particular, can we detect lead-lag relationships? 
b) If lead-lag relationships exist, what is their strength and which factors affect their 
magnitude? 
c) How do CDS and bond markets contribute to price discovery? 
Research on question a) deals with the contemporaneous and intertemporal comovement of 
stock and corporate bond markets and, since recently, the CDS market. Note that earlier stud-
ies are based on portfolio performance data at a relatively low frequency [see, e.g., Blume, 
Keim and Patel (1991), Cornell and Green (1991)]. For example, Fama and French (1993) 
investigate which risk factors are able to explain monthly returns of stock and corporate bond 
portfolios in the period 1963-1991. They identify three stock-market factors (overall excess 
market return, firm size, and book-to-market equity ratio) and two bond-market factors (term 
structure spread, default risk spread) whereas the two bond-market factors establish the link 
between both markets. All five factors seem to explain the common contemporaneous varia-
tion in bond and stock returns and the cross-sectional average returns reasonably well.  
Subsequently, academics began to analyze the bond-stock market relationship at the indi-
vidual firm-level, in a lead-lag framework, and with data from a higher frequency (weekly, 
daily, hourly). For example, Kwan (1996) runs pooled and individual time-series regressions 

 
5
to explain weekly changes of corporate bond yields with changes of same-maturity treasury 
yields and contemporaneous, leading and lagging stock returns. Main results are that changes 
of treasury yields have a significant positive impact whereas contemporaneous and lagged 
stock returns have a significantly negative impact on bond yield changes. These results are 
interpreted as evidence for the hypothesis that individual bond and stock prices are driven by 
firm-specific information that is related to the expected value of the firm’s assets rather than 
to the volatility of the firm’s asset returns. Additionally, firm-specific-information seems to be 
embedded first into stock prices because lagged stock returns have significant impact on bond 
yield changes whereas lagged bond yield changes have neither statistical nor economic impact 
on current stock returns. 
Alexander, Edwards, and Ferri (2000) investigate the relationship between daily stock and 
high-yield bond returns at the individual firm-level during the period 1994-1997. Relying on 
different regression models, they find a significantly positive but economically weak correla-
tion between daily high-yield bond returns and firms’ stock excess returns. In addition, they 
look at the bond-stock return relationship around wealth transferring events. Essentially, they 
detect a negative comovement around these events and a positive one in other periods. This 
result is interpreted as one possible explanation for the low time-series correlation between 
stock and bond returns. 
Hotchkiss and Ronen (2002) analyze the informational efficiency of the high yield corpo-
rate bond market using daily and hourly price data from the year 1995. Applying a vector 
autoregressive (VAR) model, they do not find support for the view that stock portfolio returns 
lead bond portfolio returns. However, they detect a significantly positive but economically 
weak contemporaneous correlation between stock and bond returns which is, however, judged 
as non-causal. Since a comparative analysis of pricing errors indicates that market quality is 
not poorer for bonds, they conclude that the considered bond market sample is information-

 
6
ally efficient, even relative to the stock market. However, it is not clear whether these results 
would hold for firms from the investment-grade level as well. 
Longstaff, Mithal, and Neis (2003) examine weekly lead-lag relationships between CDS 
spread changes, corporate bond spreads and stock returns of US firms in a VAR framework. 
They find that both stock and CDS markets lead the corporate bond market which provides 
support for the hypothesis that information seems to flow first into stock and credit deriva-
tives markets and then into corporate bond markets. However, in their sample there is no clear 
lead of the stock market with respect to the CDS market and vice versa. 
Given this literature, we propose the following hypotheses concerning the intertemporal 
relationship between the stock, bond and CDS market: 
H1: Positive stock returns are associated with negative CDS spread changes and nega-
tive bond spread changes. 3 
As stated by Kwan (1996), we expect that stock and bond prices move in the same direction 
when new information relates to the expected firm value. If the latter rises due to unexpect-
edly high earnings, the stock price will go up because stockholders will benefit from im-
proved earnings and the price (yield to maturity) of corporate debt will rise (fall) because 
default risk is reduced. Note that this inverse relationship between stock returns and credit 
spread changes is consistent with studies that have analyzed the determinants of credit spreads 
[see, e.g., Collin-Dufresne, Goldstein, and Martin (2001), Aunon-Nerin et al. (2002), Blanco, 
Brennan, and Marsh (2004), Avramov, Jostova, and Philipov (2004)]. 
H2: The stock market and the CDS market lead the bond market. 
                                                 
3 Alternatively, Kwan (1996) argues that positive stock returns may be associated with positive CDS and bond 
spread changes when new information relates to the volatility of the firm’s asset return. A firm’s equity can be 
interpreted as a call long on the firm value, corporate debt can be interpreted as a combined position of a default-
free bond long and a put short on the firm value. Since equity and corporate debt are long and short positions in 
options that relate to the value of the firm, their prices should move in opposite directions with respect to volatil-
ity changes. However, Kwan cannot provide empirical evidence for this volatility-based reasoning. 

 
7
In an intertemporal setting, we expect the stock market to lead the bond market for the follow-
ing reasons. First, there is some prior empirical evidence which suggests that information is 
reflected earlier in the stock than in the bond market [see Kwan (1996), Longstaff, Mithal, 
and Neis (2003)]. Second, institutional features of the stock market facilitate a continuous 
flow of transactions which is not the case in the bond market where short positions are more 
difficult to establish. Third, the number of traders, trades and the trading volume is clearly 
higher in the stock market than in the corporate bond market. The CDS market is also ex-
pected to lead the bond market because of the first two arguments mentioned above.  
With regard to question b) which refers to the magnitude of the market comovement, we 
state the following hypotheses: 
H3: The link between the CDS and the stock market is stronger than the link between 
the bond and the stock market. 
In the CDS market pure issuer credit risk is traded whereas in the bond market issue-specific 
credit risk and market risk are traded in a bundle. Accordingly, hypothesis H3 states that CDS 
spread changes should exhibit a stronger sensitivity to stock returns than bond spread 
changes. First empirical evidence is provided by Blanco, Brennan, and Marsh (2004). They 
follow Collin-Dufresne, Goldstein, and Martin (2001) in analyzing the determinants of CDS 
spread changes and corporate bond spread changes and find that the impact of firm-specific 
stock returns is stronger on CDS spreads changes than on corporate bond spread changes. 
H4: The magnitude of the relationship between CDS/bond spread changes and stock 
returns positively depends on a firm’s creditworthiness. 
CDS and bond spread changes from low-grade firms should exhibit a higher sensitivity to 
stock returns than those from high-grade firms. This relationship has been detected in earlier 
studies for bond spread changes and stock returns [see Blume, Keim, and Patel (1991), Cor-
nell and Green (1991), Kwan (1996), Collin-Dufresne, Goldstein, and Martin (2001), and 

 
8
Avramov, Jostova, and Philipov (2004)]. The underlying reasoning is as follows: equity bears 
the ultimate form of credit risk because it represents the most subordinated claim in the capi-
tal structure of a firm. Hence, CDS and bond spread changes from high risk firms should be 
linked more strongly to stock returns than those from low risk firms. 
H5: The magnitude of the relationship between CDS/bond spread changes and stock 
returns negatively depends on a firm’s size. 
CDS and bond spread changes from relatively small firms should exhibit a higher sensitivity 
to stock returns than those from relatively large firms if size is related to default risk. 
Finally, question c), i.e. the dynamic adjustment of firm-specific credit spreads from dif-
ferent markets (CDS, corporate bond), has been analyzed by Blanco, Brennan, and Marsh 
(2004) for a sample of 33 firms (16 from the US, 17 from Europe) from January 2001 to June 
2002. The application of cointegration tests to CDS and bond spread time series and results 
from a corresponding vector error correction model (VECM) reveal that price discovery takes 
predominantly place in the CDS market. In a similar study, Zhu (2004) examines the same 
question for a sample of 24 firms (hereof 19 from the US) during the period 1999-2002. Ac-
cording to this study, spread levels in both markets can considerably deviate from each other 
in the short run. The dynamic analysis reveals that both markets are strongly linked in the 
long-run. Interestingly, the CDS market plays a more important role in price discovery than 
the bond market in the case of US firms while the opposite holds for European firms. With 
respect to question c) we propose the following hypothesis: 
H6: Price discovery takes mainly place in the CDS market. 
This hypothesis can be substantiated by the following arguments. First, the CDS market is 
more flexible and less capital-intense because only premia but no bond prices have to be paid. 
Second, CDS traders can easily go long and short in credit risk (i.e. buy or sell protection) 
while shortening bonds is more difficult. Third, bond spreads from the secondary market 

 
9
depend on the available number and specifics of the outstanding bonds which is related to the 
new bond issue activity of the firms whereas the CDS market is more standardized (in terms 
of tenor, notional, currency etc.) and less dependent on primary bond market issuances. 
 
3.  
Description of the data 
3.1. 
Data collection, treatment and final composition 
We collect data on CDS, stock and corporate bond markets, risk free interest rates and in-
dividual firm characteristics. CDS data are provided by a large European bank which is 
among the world’s top 25 credit derivatives counterparties and by CreditTrade, a large CDS 
trading platform. It covers the time period July 2, 1998 to December 2, 2002 and includes 
CDS quotes and additional contractual information for more than 1000 reference entities 
(Corporates, Financials, and Sovereigns). CDS quotes are selected in the following manner: 
First, we exclude all quotes on sovereigns due to the lack of stock prices for these entities. 
Second, we calculate the mid spread from bid and offer quotes. Third, we take the mean per 
day if multiple mid spreads and/or transaction spreads were observed on a given day. Fourth, 
since the number of CDS price observations per firm is relatively low in 1998 and 1999, we 
select all firms with at least 100 daily senior CDS price observations for a maturity of five 
years in each of the years 2000-2002.4 This selection procedure leads to a sample of 90 firms 
from Europe, the United States, and Asia. We then add time-series of daily common stock 
closing prices and the corresponding total return indices obtained from Thomson Financial 
Datastream. 
Furthermore, we examine outstanding corporate debt of these 90 firms using Bloomberg 
data. We apply the following filter rules to obtain a sample of suitable corporate bonds: (1) 
bonds are issued with a fixed coupon and are non-callable, non-puttable and not convertible, 
                                                 
4 The five-year maturity represents the benchmark in the CDS market, see British Bankers’ Association (2002). 

 
10
(2) bonds are quoted in US-Dollar, Pound Sterling or Euro, (3) bonds rank senior unsecured 
(required seniority for deliverable assets according to the ISDA Master Agreement for CDS), 
(4) bond price time series exist during 2000-2002 and indicate liquid trade (matrix priced 
bonds were excluded). In addition to generic mid-market closing bond prices and yield to 
maturities, we gathered bond characteristics like ISIN, issue and maturity date, coupon, no-
tional, currency, payment frequency, day convention and first coupon day. 
Moreover, we collect daily default-free interest rate term structures. Although government 
bond yield curves seem to be the first choice, we also consider interest rate swap curves for 
USD, GBP and EUR since related studies provide evidence that swap rates might be the more 
appropriate benchmark [see, e.g., Houweling and Vorst (2002)]. Government bond yield 
curves come from the Federal Reserve Board’s, the Bank of England’s and Deutsche Bundes-
bank’s web page. Additionally, we obtain a synthetic EUR yield curve from the Statistical 
Office of the European Communities (EuroStat). Interest rate swap curves are taken from 
Thomson Financial DataStream. Since daily CDS spreads refer to a constant maturity (usually 
3, 5, 7, 10 years with 5 year as benchmark), we have to compare these spreads with constant 
maturity bond spreads. As constant maturity bond spreads are not observable, we create, if the 
corresponding bond data are available, a synthetic five-year constant maturity bond spread for 
each firm by linearly interpolating the daily yields of two actual bonds with maturity above 
and below five years and subtract the five-year default-free interest rate.5 
The data are completed with individual firm characteristics (market capitalization in local 
currency and Euro, region, industry code) from Thomson Financial DataStream. Additionally, 
histories of credit ratings from Moody’s (issuer rating, senior unsecured), Standard & Poor’s 
                                                 
5 See Hull, Predescu, and White (2003), Blanco, Brennan, and Marsh (2004) and Longstaff, Mithal, and Neis 
(2003, 2004) for a similar methodology. Longstaff, Mithal, and Neis (2004) point out that this model-
independent approach, if used for pricing issues, may underestimate the default risk in investment-grade bonds 
and overestimate it for below-investment-grade bonds. 

 
11
(long term foreign currency issuer credit) and Fitch Ratings (senior unsecured, long term 
foreign currency debt) are taken from Bloomberg.6  
The final data set consists of 58 firms7 with observations from the years 2000-2002 (see 
Appendix A for the sample composition). It covers 70% of the world’s top 20 most actively 
traded corporate reference entities in terms of frequency of occurrence [see Fitch Ratings 
(2003)]. 35 of the 58 firms (=60%) come from Europe, 20 from the USA (=35%) and 3 from 
Asia (=5%). The most important industries are financials (=31%), telecommunication (=14%) 
and automotive (=12%). Table 1 presents characteristics of the firms and bonds included in 
our final sample: 
 
(insert Table 1 here) 
 
Panel A reveals that both average firm size (measured by market capitalization in Euro) 
and average creditworthiness (measured by the rating) decline over the sampling period. The 
first observation is due to the overall baisse in the European and North American stock mar-
kets and, additionally for US firms, partially due to the development of the US Dollar-Euro 
exchange rate.8 The deterioration of the firms’ ratings reflects the rise of leverage and/or 
earnings problems in some industries (e.g. telecommunication or automotive). Panel B pre-
sents characteristics of 58 synthetic five-year constant maturity bonds which were created by 
interpolating, at least, one bond with maturity below five years and another with maturity 
above five years (see Appendix B for disaggregated bond characteristics). As can be seen, 
                                                 
6 We constructed two aggregated rating systems. The first was created by mapping agency credit ratings on a 
numerical 17 grade scale (AAA / Aaa = 1, AA+ / Aa1 = 2, ..., CCC / Caa1 and below = 17). The second, less 
fine, resulted from a mapping on a six grade scale (AAA /Aaa = 1, AA / Aa = 2, ..., B / B = 6). 
7 The decrease of the sample is due to the fact that 32 firms had to be dropped because their outstanding bonds 
did not meet our selection criteria. 
8 Starting from 1.01 USD/EUR on January 3, 2000 the value of the Euro declined down to 0.85 USD/EUR on 
June 29, 2001. The exchange rate recovered at the end of the sampling period reaching again the parity. 

 
12
notionals of bonds below and above five years to maturity amount to roughly 0.5 billion EUR. 
Approximately 45% of the bonds are denominated in Euro and US dollar respectively and the 
remainder in Pound sterling. 
 
3.2. 
Descriptive analysis of market data 
We now shortly describe the market data, the time-series properties and analyze the con-
temporaneous link between markets with correlations. 
Table 2 exhibits five-year senior CDS spreads (CDS) and five-year constant maturity 
bond spreads (BSS) over swap rates and government bond yields (BSG) by year and rating. 
There are several interesting aspects to be mentioned: First, looking at the rows, one can 
easily see that mean spreads are in line with the ordinal ranking by credit ratings. Second, 
looking at the columns, we find an increasing average spread per rating category over the 
sampling period for CDS and BSS. This observation may be due to the different population in 
each cell, the decline of swap rates, a deterioration of the average credit qualities within each 
grade, or due to a rise of the average risk premia [see Berndt et al. (2004) who find that risk 
premiums for a given probability of default vary considerably over time]. Third, and most 
important, looking at investment-grade spreads (AAA-BBB), we clearly see that CDS spreads 
are much closer to bond spreads above swap rates than spreads above government bond 
yields. The latter evidence confirms results of Houweling and Vorst (2002), Hull, Predescu, 
and White (2003) and Blanco, Brennan, and Marsh (2004). Since corporate bond spreads 
above swap rates are much closer to CDS spreads, we do not use corporate bond spreads 
above government yields for subsequent analyses. 
 
(insert Table 2 here) 
 

 
13
Figure 1 displays time series of daily cross-sectional means and medians of CDS and BSS 
over the entire sampling period. As indicated in Table 2, it can be seen that CDS and bond 
spreads were relatively close to each other in the years 2000 (CDS: 41 bps, BSS: 43 bps) and 
2001 (CDS: 71 bps, BSS: 62 bps). On the one hand, since summer 2001, we observe a posi-
tive basis for mean spreads (CDS: 119 bps, BSS: 85 bps) which persists until the end of the 
sampling period (see Figure 1a). On the other hand, Figure 1b reveals that median spreads of 
CDS and corporate bonds remain quite close to each other although a small positive basis 
becomes visible.  
 
(insert Figure 1 here) 
 
In a next step, we examine time-series properties like stationarity and autocorrelation of 
the individual CDS, bond and stock time series. This is an important issue because if time-
series are non-stationary and serially correlated, the usual OLS regression approach is no 
longer applicable. In particular, one might find a spurious (but not an economic) relationship 
between two variables. Table 3 summarizes results of three different stationarity tests9 and 
displays autocorrelation coefficients for weekly/daily level and change data. Panel A reveals 
that the null hypothesis that level time-series (stock prices, CDS and BSS) are non-stationary 
(stationary) is rejected for a small (large) number of firms. For example, only one firm exhib-
its not a non-stationary daily stock price time-series according to the Phillips-Perron test. The 
opposite is found for daily time-series of stock returns and spread changes. In at least 54 of 58 
cases the time-series of returns and first differences are no longer considered to be non-
stationary. Panel B presents mean autocorrelation coefficients for weekly and daily data. 
                                                 
9 Note that the Augmented Dickey-Fuller and the Phillips-Perron test have a null hypothesis of non-stationarity 
whereas the Kwiatkowski-Phillips-Schmidt-Shin (KPSS) test has a null hypothesis of stationarity. We consider 
tests with different null hypotheses to ensure that results are robust to the power of the tests. 

 
14
Whereas autocorrelation of level time-series is typically high10, it is relatively low for weekly 
and daily change data except for daily bond spread changes at lag 1 (-0.19). Since these re-
sults indicate that time-series of stock prices and spread levels are non-stationary and strongly 
autocorrelated while stock returns and spread changes are not, we subsequently focus on the 
latter variables. 
 
 
(insert Table 3 here) 
 
To get a first impression of the contemporaneous comovement of the three markets, we 
examine pairwise rank correlation of weekly and daily time-series at the firm-level. The 
corresponding results are summarized in Table 4. The mean rank correlation of weekly stock 
returns and CDS spread changes is -0.25 with 35 of 58 individual correlation coefficients 
being significantly different from zero at the 0.01-level. Interestingly, CDS spread changes 
exhibit a stronger negative correlation with stock returns than bond spread changes (-0.25 vs. 
-0.13). The difference between the means of ρS(R, ∆CDS) and ρS(R, ∆BSS) is significant at 
the 0.01-level when using a two-sided non-parametric Wilcoxon sign rank test or a simple t-
test. Differentiating by the geographic origin of a firm, we find that stock returns of US firms 
exhibit a slightly stronger negative correlation with CDS than European firms. Furthermore, 
correlations get more pronounced for firms with a relatively bad credit rating at the beginning 
of our sampling period.11 Looking at industries, we detect a much stronger correlation of 
stock returns from telecommunication firms with CDS and bond spread changes (-0.36, -0.23) 
than for other firms (-0.25, -0.08). Additionally, correlation of stock returns and CDS spread 
                                                 
10 Autocorrelation coefficients of levels decline from closely below 1.00 at lag 1 to 0.70-0.78 at lag 5 for weekly 
data and to 0.94 - 0.95 at lag 5 for daily data. 
11 An analysis based on a 17-grade-rating-scale reveals that this relationship is not a monotonous one. Moving 
from AA to A leads to a more pronounced correlation, but moving from A to BBB reduces the correlation. This 
observation might be due to a small number of observations in some grades. 

 
15
changes for financials is higher than for non-financial firms. Similar results are found for the 
correlation of daily changes. 
 
(insert Table 4 here) 
 
4. Analysis of the intertemporal relationship between markets 
4.1. 
Lead-lag relationships between CDS, bond and stock markets 
In this section, we analyze the intertemporal comovement of CDS spread changes, bond 
spread changes and stock returns for each firm in the sample. More specifically, we try to 
explain current stock returns, CDS spreads changes and bond spread changes with a three-
dimensional vector autoregressive model [see, e.g., Stock and Watson (2001), Gujarati (2003) 
for an overview]. We think that a VAR approach is appropriate for our purpose because it has 
exactly been developed to capture lead-lag relationships within and between stationary vari-
ables. Moreover, it represents a simultaneous equation estimation. Therefore, we do not have 
to estimate single equation distributed models that include lags and leads12 because a VAR 
model entirely captures the intertemporal relationships simultaneously. Our basic model 
specification is the following:13 
                                                 
12 Kwan (1996) estimates a single-equation model with contemporaneous bond yield changes as dependent and 
contemporaneous stock returns as well as its leads and lags as independent variables. We avoid including leading 
variables on the right-hand side of the model because their impact is difficult to interpret in terms of (Granger-) 
causality [see Gujarati (2003), p. 712-713]. 
13 Note that our analysis differs from Longstaff, Mithal and Neis (2003) with regard to the following three 
aspects: i) they analyze weekly data, we examine daily and weekly data, ii) their sample is confined to US firms, 
our data set is an international one, iii) they calculate bond spreads above US Treasury bond yields, we consider 
swap rates as default-free benchmark rate. 

 
16
 
t
p
t
P
p
p
p
t
P
p
p
p
t
P
p
p
t
t
p
t
P
p
p
p
t
P
p
p
p
t
P
p
p
t
t
p
t
P
p
p
p
t
P
p
p
p
t
P
p
p
t
BSS
CDS
R
BSS
BSS
CDS
R
CDS
BSS
CDS
R
R
3
1
3
1
3
1
3
3
2
1
2
1
2
1
2
2
1
1
1
1
1
1
1
1
ε
δ
γ
β
α
ε
δ
γ
β
α
ε
δ
γ
β
α
+
∆
+
∆
+
+
=
∆
+
∆
+
∆
+
+
=
∆
+
∆
+
∆
+
+
=
−
=
−
=
−
=
−
=
−
=
−
=
−
=
−
=
−
=
∑
∑
∑
∑
∑
∑
∑
∑
∑
  
 
 
 
 
 
    (1) 
 
with Rt: stock return in t, ∆CDSt: CDS spread change in t, ∆BSSt: change of a synthetic 5-
year corporate bond spread in t, p: lag order index, εt: disturbance term in t. 
 
Subsequently, we apply this model to weekly and daily time-series from the three markets 
at the individual firm-level. The analysis of weekly data is carried out to allow for compara-
bility with related studies. In addition, we focus on daily data because different markets may 
respond differently to new information in the short term but they are likely to align after some 
days. For the above model specification, the lag structure and the maximum lag order P has to 
be determined given the trade off between over-parameterization (and the corresponding loss 
of degrees of freedom) and over-simplification. Various methods, for example, the Akaike- or 
Hannan-Quinn-information criteria or step-wise likelihood-ratio tests, have been developed 
for this issue.14 Either one follows these criteria15 and selects the appropriate lag order accord-
ingly and/or one relies on theoretical reasoning and, if available, prior empirical findings 
about the underlying economic relationships. Since the maximum lag order should capture the 
overall information processing and aggregation time in each of the three markets, we think 
that a lag structure without gaps and a maximal lag of order 2 seems reasonable for weekly 
                                                 
14 The objective of these information criteria is to optimize the overall model’s ability to fit the observed time-
series as accurately as possible. For this purpose, the variance of the residuals is minimized, but any additional 
inclusion of further lagged variables is penalized by an increase of this variance. 
15 For weekly (daily) data the Akaike information criterion suggests a lag order of 2 (4), the Hannan-Quinn 
criterion one of 1 (2) and a likelihood-ratio test one of 3 (9). Numbers are medians of the individual criteria from 
all 58 firms. 

 
17
data16 and one of order 5 (spanning lag 1 for weekly data) should be appropriate for daily 
data. 
 
Table 5 reports model estimation results for the individual firms with weekly (Panel A) 
and daily data (Panel B). For weekly data17 and lags 1-2, the R2 and the p-value from a F-test 
indicate that stock returns are the least forecastable and bond spread changes the most 
forecastable variable. Columns 3, 6 and 9 display the number of coefficients that are 
significantly different from zero at the 0.01-level.18 We report the number of cases in which 
the coefficients are jointly different form zero [Granger-causal, see Granger (1969)] in 
columns 4, 7 and 10. Whereas lagged CDS and bond spread changes have little impact on 
stock returns, the latter significantly lead CDS spread changes in 19 of 58 cases at the 0.01-
level. Note that the relationship is negative for all firms which provides clear evidence in 
favor of hypothesis H1.19 In addition, the CDS market seems to lead the bond market at lag 
order one in 23 of 58 cases. Note that both the frequency of a significant impact and the 
magnitude of the median coefficient tends to decline if one moves from lag 1 to lag 2 in most 
of the cases. Summing up, these findings are support for hypothesis H2. 
Furthermore, there is clear indication that the residuals of each equation come from a 
white noise process on the basis of a Ljung-Box test (including lags 1-8). Additionally, 
applying Bartlett’s periodogram-based test the white noise property of the residuals cannot be 
                                                 
16 See Kwan (1996), Longstaff, Mithal, and Neis (2003) who include weekly lags of order 1 and 2. 
17 Stock returns and spread changes in table 5 refer to the Wednesday-Wednesday interval. To study the robust-
ness of these results with regard to a potential day-of-the-week effect, we re-estimate the VAR model with 
observations from the intervals Monday-Monday, ..., and Friday-Friday. Results of each of the week-day inter-
vals are very close to those reported in table 5. The average R2 for the stock return equations across the five 
week-day intervals is 0.0507, for the ∆CDS equation 0.1011, and for the ∆BSS equation 0.1389. In addition, the 
number of firms that exhibit significant coefficients for lagged variables is very similar across the five week 
intervals. 
18 Note that our findings remain qualitatively the same if we adopt a significance level of 0.05 or 0.10 for the 
estimated regression coefficients and Granger causality tests. 
19 This result is consistent with the correlation analysis from Section 3.2 and Kwan (1996) who detects a nega-
tive relationship between stock returns and bond yield to maturity-changes for the same firms. 

 
18
rejected for any of the firms. Overall, this analysis of residuals indicates that OLS 
assumptions are respected. 
 
(insert Table 5 here) 
 
Panel B reports the median coefficients and the number of coefficients that are signifi-
cantly different from zero at the 0.01-level for the daily VAR model with lags 1 to 5. Interest-
ingly, we obtain qualitatively similar results as for the weekly data. The number of firms 
whose lagged CDS and bond spread changes significantly explain contemporaneous stock 
returns is relatively low and median coefficients are close to zero. In contrast, lags 1-5 of 
stock returns Granger cause CDS spread changes from 39 of 58 firms. Note that, as found for 
weekly data, the relationship is negative, which is consistent with H1, and the magnitude of 
the median coefficient and the number of significant coefficients of lagged stock returns 
decreases as the lag order ascends. Bond spread changes are predictable with past CDS spread 
changes (lags 1-5 are jointly significant or Granger causal for 33 of 58 firms) and, for a 
smaller number of firms, with lagged stock returns. Again, the economic impact of the stock 
market on bond spreads tends to decline if the lag length increases. With regard to the in-
tertemporal relationship between CDS and bond spread changes, Granger causality tests for a 
0.01-level of significance reveal that i) ∆CDS cause ∆BSS but not vice versa at 18 firms, ii) 
∆CDS cause ∆BSS and vice versa at 15 firms, iii) ∆BSS cause ∆CDS at 4 firms and iv) nei-
ther ∆CDS cause ∆BSS nor vice versa at 21 firms. While there is reciprocal Granger causality 
for a considerable number of firms, we find that the one-way impact of lagged ∆CDS on 
∆BSS is observed more often than the opposite relationship. Similarly to weekly data, the 
fraction of variance explained and the number of firms with very low F-test p-values is small-

 
19
est for the stock market and highest for the bond market equation. Hence, results for daily 
data represent support for H2 too. 
Finally, as done for weekly data, we check whether the residuals from the three equations 
respect the underlying regression assumptions. On the one hand, applying a Ljung-Box test, 
we find that residuals from the stock return equation come predominantly from a white noise 
process whereas those from the CDS and BSS equation are not considered as white noise for a 
considerable number of firms. On the other hand, according to Bartlett’s test, we cannot reject 
the hypothesis that residuals come from a white noise process for any firm. Overall, we deem 
the results in line with OLS assumptions. 
For robustness purposes, we examine additional issues that may influence the results ob-
tained from the VAR model in the remainder of this section. First, we investigate whether the 
observed lead-lag relationships are influenced by asynchronous price observations. Since 
previous findings suggest that the stock market leads both other markets, but stock prices do 
not exactly refer to the same point in time as CDS spreads and bond spreads, we repeat our 
analyses for stock returns that are lagged by one day to explicitly favor both other markets. 
Essentially, results are very close to those obtained previously: Even stock returns lagged by 
one day are the least forecastable and bond spread changes remain the most forecastable 
variable. 
Second, we include the contemporaneous change of the five-year swap rate as exogenous 
variable in the VAR model to control for changes in the interest rate level that may influence 
both stock returns and spread changes. Overall, for daily (weekly) data we find a significantly 
positive but economically small impact of contemporaneous swap rate changes on stock 
returns for 48 (35) firms and a significantly negative impact on ∆CDS for 18 (25) firms and 

 
20
∆BSS for 48 (38) firms.20 More important, previous results (number of significant coeffi-
cients, magnitude of coefficients, Granger causality) do not change much in the sense that 
stock returns remain the least predictable variable (median R2=0.0704) and bond spread 
changes the most predictable variable (median R2=0.2528). 
Third, we check whether our findings remain robust if we control for changes in the im-
plied equity volatility which represents an important determinant of credit spreads [see Collin-
Dufresne, Goldstein, and Martin (2001)]. Since we do not have data about firm-specific eq-
uity volatilities, we include contemporaneous and lagged changes of CBOE’s implied volatil-
ity index (VIX) as exogenous variable in the VAR model.21 Essentially, most of the 
previously found lead-lag relationships turn out to be robust with regard to the inclusion of 
the volatility measure. The estimated coefficients are significantly negative at the 0.01-level 
for 50 firms (lag 1: 36) in the stock return equation, significantly positive for 26 firms (lag 1: 
14) in the ∆CDS equation, and significantly positive for 8 firms (lag 1: 17) in the ∆BSS equa-
tion. In contrast to Table 5, the median-R2 for stock returns (0.1603) becomes higher than that 
for the two other markets which may be a consequence of the close connection between stock 
returns and volatility. However, as found earlier, ∆CDS remains less forecastable (median-
R2=0.1182) than ∆BSS (median-R2=0.1567). 
Fourth, the VAR model is estimated separately with data from the first and second half 
(Jan 2000 – Jun 2001, Jul 2001 – Dec 2002) of the sampling period to investigate whether our 
findings are stable over time. Basically, estimation results for the sub-periods are similar to 
those reported in Table 5. However, it is noteworthy that the leading role of the stock market 
in comparison to both other markets increases over time. Furthermore, the CDS market does 
                                                 
20 Note that the inclusion of lag 1 of the five-year swap rate change as additional exogenous variable does not 
alter this finding. The coefficients of lagged swap rate changes are insignificant for most of the firms. 
21 Although our sample includes European, US and Asian firms, we simplify the robustness check by relying 
only on the VIX index which reflects the implied volatility of S&P 500 stocks. The correlation between VIX and 
VDAX (volatility index for the German stock market index DAX) is 0.84 during the sampling period. 

 
21
not lead the bond market in the first half but it clearly does in the second half, reflecting the 
on-going evolution of the CDS market. Finally, the variance explained increases over time in 
all markets without altering the finding that stock returns are the least and bond spread 
changes the most forecastable variable. 
Summarizing, our findings suggest that there is a negative relationship between stock re-
turns and CDS/bond spreads changes and that the first clearly lead the latter. In addition, it 
turns out that CDS spread changes are more frequently able to forecast bond spread changes 
than vice versa in recent years.22 The latter result is in line with findings from Longstaff, 
Mithal and Neis (2003). However, in opposite to that study, we find a definite lead of the 
stock market relative to the CDS market. One reason for this difference may be the sample 
composition: while Longstaff, Mithal, and Neis (2003) exclusively analyze US firms, we 
examine an international sample with 35 of 58 firms coming from Europe. If the CDS market 
for US reference entities is more developed than for European firms, which is not implausible, 
results can be reconciled. This issue will be addressed in more detail in section 4.3. 
 
4.2. 
The strength of the intertemporal comovement 
Having investigated the existence and the direction of lead-lag relationships between mar-
kets so far, we now examine the magnitude of the previously estimated coefficients to test 
hypotheses H3, H4 and H5.  
An analysis of the sensitivity of the CDS and bond spread changes to the lagged stock re-
turns indicates that the CDS market is significantly more sensitive to stock returns than the 
bond market (weekly data: -15.62 vs. –5.93, daily data: -14.67 vs. -9.27) which represents 
support for H3 and is in line with findings from Blanco, Brennan, and Marsh (2004). Apply-
ing a non-parametric Wilcoxon sign rank test to the difference of β2, t-1 and β3, t-1 shows that 
                                                 
22 This result is confirmed in a two-dimensional VAR model which only includes ∆CDS and ∆BSS. 

 
22
β2, t-1 is significantly smaller (in absolute terms higher) at the 0.01-level for weekly data and at 
the 0.05-level for daily data.23 The difference becomes significant at the 0.01-level for daily 
and weekly data if we compare the firm-specific sum of the significant lag coefficients. 
Moreover, as stated in hypotheses H4 and H5, we investigate whether the magnitude of 
the coefficients β2, t-p und β3, t-p is related to a firm’s creditworthiness and size. With respect to 
the first issue, we compare the firm-specific coefficients with the duration-weighted 17-grade 
rating scale. Results for all firms and daily data are plotted in Figure 2. 
 
(insert Figure 2) 
 
It can be seen that the estimated sensitivity of ∆CDS and ∆BSS on lagged stock returns is 
negatively associated with a firm’s average creditworthiness. However, while this relationship 
is quite pronounced for the CDS market24, indicated by a rank correlation coefficient of -0.46 
that is significant different from zero at the 0.01-level, it is not significant for the bond market 
at all. Note that this result also holds for the sum of significant coefficients and for the sub-
sample of firms that exhibit coefficients that are significant at the 0.01-level. These findings 
provide partial evidence in favor of H4 since the hypothesized relationship has been found for 
the CDS but not for the bond market. Repeating the same kind of analysis for firm size, we 
note a positive but insignificant relationship between the magnitude of β2, t-p und β3, t-p and 
firm size (market capitalization in EUR or log market capitalization). This result leads to a 
rejection of H5 because the expected influence of a firm’s size is not significant. 
                                                 
23 The difference is significant at the 0.01-level if we compare the firm-specific sum of the significant coeffi-
cients of all lags for weekly and daily data. 
24 See Norden and Weber (2004) for related, event-study based evidence. They find that both the CDS and the 
stock market react more strongly to negative rating announcements for firms with a relatively bad “old” rating 
than for firms with a relatively good “old” rating. 

 
23
To study the impact of potential determinants of spread sensitivities in a multivariate set-
ting, we estimate two cross-sectional regressions with β2, t-1 and β3, t-1 as dependent variables 
respectively and the duration-weighted rating, the firm size, and dummy variables that mark 
telecommunication firms, financial firms and region as independent variables. Essentially, 
results indicate a significantly negative impact of the rating, the telecommunication dummy 
and the US dummy variable on the dependent variable β2, t-1 (R2=0.42). With regard to the 
sensitivity of the contemporaneous bond spread changes β3, t-1 on lagged stock returns, we 
only observe a significantly negative impact of the US dummy variable (R2=0.24). 
 
4.3. 
Adjustment process between CDS spreads and bond spreads 
In the remainder, we extend our previous analysis with a test of hypothesis H6. Since two 
related studies have shown that CDS spreads and corporate bonds spreads from the same firm 
are not uncommonly cointegrated [see Blanco, Brennan, and Marsh (2004) and Zhu (2004)], 
we take a closer look at the intertemporal relationship between these two kinds of spreads and 
leave the stock market aside. 
The existence of a cointegration relationship between the levels of two non-stationary 
variables means that a linear combination of these variables is stationary and should be 
explicitly taken into account in an VAR-analysis of change data [see Engle and Granger 
(1987), p. 259]. Cointegrated variables move together in the long run but may deviate from 
each other in the short run (see Figure 1) which can be interpreted as a permanent adjustment 
process towards an economic equilibrium. A model that considers this adjustment process is 
called a vector error correction model (VECM) and corresponds to a vector autoregressive 
model that is augmented by an error correction term. The two-dimensional VECM is specified 
as follows:25 
                                                 
25 In the remaining analysis we essentially follow Blanco, Brennan, and Marsh (2004). 

 
24
 
1
0
0
1
1
2
1
2
1
2
1
2
2
1
1
1
1
1
1
1
1
−
−
−
−
=
−
=
−
−
=
−
=
−
−
−
=
+
∆
+
∆
+
+
=
∆
+
∆
+
∆
+
+
=
∆
∑
∑
∑
∑
t
t
t
t
p
t
P
p
p
p
t
P
p
p
t
t
t
p
t
P
p
p
p
t
P
p
p
t
t
BSS
CDS
Z
with
BSS
CDS
Z
BSS
BSS
CDS
Z
CDS
β
α
ε
γ
β
λ
α
ε
γ
β
λ
α
  
 
 
 
 
 
 
(2) 
 
Given the observation that CDS frequently exceed BSS (see Table 2), the coefficients λ1 
and λ2 of the error correction term Zt-1 can be interpreted as follows. If the bond market con-
tributes to the adjustment process, λ1 will be significantly negative and if the CDS market 
contributes to the adjustment process, λ2 will be significantly positive. In the case that both 
markets play a role, we expect both coefficients to be significant and signed as explained 
before. Subsequently, we first test whether there exists a significant cointegration relationship 
between CDS and BSS for each firm. Second, we estimate a VECM-model for all firms at 
which spreads are cointegrated and then interpret the coefficients of the error correction term. 
Main results from these to two steps are summarized in Table 6: 
 
(insert Table 6 here) 
 
 
Table 6 provides several interesting results concerning the adjustment process between 
CDS spreads and bond spreads. As reported in Panel A, we detect a significant cointegration 
relationship between the spreads for 36 of 58 firms.26 It turns out that the share of firms with 
cointegrated spreads is higher among US firms (15/20=75%) than among European ones 
(20/35=57%) which is consistent with results from Blanco, Brennan, and Marsh (2004) and 
                                                 
26 Analyzing another data set for a shorter period of time Blanco, Brennan, and Marsh (2004) discover cointegra-
tion of spreads at 27 of 33 firms. Zhu (2004) detects cointegration of spreads for 15 of 24 firms. 

 
25
Zhu (2004). Analyzing the relative importance of the CDS and bond market for price discov-
ery, we find that mean and median λ1 is negative and λ2 is positive for all firms. The Gonzalo-
Granger measure [see Gonzalo and Granger (1995)], defined as GG = λ2 / (λ2 - λ1) with λ1 ≠ 
λ2, indicates which of both markets contributes more to price discovery.27 For all firms at 
which cointegration between spreads exists, the mean (median) of the GG-measure amounts 
to 0.69 (0.79) indicating that most of the price discovery occurs in the CDS market which 
provides empirical evidence in favor of hypothesis H6.28 Differentiating across regions, it 
turns out that the CDS market plays a more important role for price discovery than the bond 
market for US reference entities (mean GG=0.84) than for European firms (mean GG=0.58). 
This difference is significant at the 0.05-level on the basis of a non-parametric Wilcoxon rank 
sum test. Note that results get more pronounced, in particular the difference between US and 
European firms, for the 21 firms at which cointegration is significant at the 0.01-level. 
 
Panel B presents the number of significant coefficients and their sign for firms at which a 
cointegration of spreads cannot be rejected at the 0.10-level (0.01-level in brackets). Basi-
cally, these numbers confirm results of Panel A in the sense of statistical significance. We 
find that for 19 firms price discovery takes significantly place only in the CDS market and for 
additional 8 firms in the CDS and the bond market. In the case of 8 firms CDS spreads adjust 
to changes of the bond spreads.29 Moreover, the exclusive contribution of the CDS market 
relative to the bond market is more frequently significant for US firms (10/15=67%) than for 
European firms (8/20=40%). In addition, we investigate whether the origin of the reference 
entity or the currency in which the bonds are denominated is better suited to summarize the 
                                                 
27 If both coefficients are significantly different from zero, correctly signed and the GG-measure is equal to 0.5, 
both markets contribute to price discovery at the same degree. For GG=0 only the bond market contributes and 
for GG=1 only the CDS market contributes to price discovery. 
28 Blanco, Brennan, and Marsh (2004) find that the CDS market contributes roughly 80% of price discovery. 
29 See Zhu (2004). For a sample of 24 firms, it has been found that only the CDS market accounts for price 
discovery at 13 firms, only the bond market at 5 firms, and both markets at 5 firms. 

 
26
adjustment behavior of spreads. We find that both variables are, as expected, highly correlated 
but that the origin of the firm and not the currency matters. For example, the spread adjust-
ment process for Ericsson whose sampled bonds are denominated in USD, is more alike to 
other European firms than to US firms.  
Figure 3 displays the error correction coefficients λ1 and λ2 for all firms with cointegrated 
spreads differentiating by the geographical origin of the firm. It is visible that the bond market 
considerably contributes to price discovery for European firms, while for US firms the CDS 
market is more important for price discovery than the bond market. 
 
(insert Figure 3 here) 
 
In addition to these findings, it is noteworthy that the fraction of variance explained in the 
two-equation-VECM is higher for ∆BSS (median R2=0.1481) than for ∆CDS (median 
R2=0.0814). Moreover, the R2 of the VECM-equation with ∆CDS (∆BSS) as dependent vari-
able exhibits a significantly negative (positive) rank correlation with the GG-measure. In 
other words: the higher the fraction of variance explained is in the ∆BSS-equation, the closer 
the GG-measure is to one, indicating the leading role of the CDS market. However, although 
we have explicitly taken into account the cointegration of spreads, the model’s ability to 
explain spread changes does not increase very much in comparison to the simpler VAR ap-
proach from Section 4.1.30 
Finally, testing for Granger causality in the VECM leads to the following results for firms 
at which cointegration of spreads has been detected: i) ∆CDS cause ∆BSS (and not vice 
                                                 
30 For comparison purposes, we also re-estimate a modified version of the three-dimensional VAR model from 
Section 4.1 that additionally includes the error correction term Zt-1 in each of the three equations. Again, stock 
returns remain the least forecastable variable (median R2=0.0388) and bond spread change the most forecastable 
variable (median R2=0.1719). For the CDS equation we obtain a median R2 of 0.1146. Testing the residuals for 
white noise produces similar results as for the VAR model from Section 4.1. 

 
27
versa) for 10 firms, ii) ∆BSS cause ∆CDS (and not vice versa) for only 3 firms, iii) ∆CDS 
cause ∆BSS and vice versa for 11 firms and iv) neither ∆CDS cause ∆BSS nor vice versa for 
12 firms. Applying the same tests to firms at which no significant cointegration of spreads has 
been found yield: i) ∆CDS cause ∆BSS (and not vice versa) for 8 firms, ii) ∆BSS cause ∆CDS 
(and not vice versa) at only 1 firm, iii) ∆CDS cause ∆BSS and vice versa at 4 firms and iv) 
neither ∆CDS cause ∆BSS nor vice versa at 9 firms. Obviously, there are no significant dif-
ferences in Granger causality for firms with and without cointegrated spreads which indicate 
that results from Section 4.1 are robust. 
 
5. Conclusion 
In this paper, we investigate the empirical relationship between the heavily growing credit 
default swap (CDS), the corporate bond and the stock market at the firm-level for an interna-
tional sample over the period 2000-2002. More specifically, we focus on the intertemporal 
comovement, in particular on lead-lag relationships and on the adjustment process between 
markets. 
 
First, analyzing the firm-specific market comovement by means of a three-dimensional 
vector autoregressive model, we find that weekly and daily stock returns are negatively asso-
ciated with CDS and bond spread changes. Second, stock returns are the least predictable and 
bond spread changes the most predictable variable which is in line with Longstaff, Mithal, 
and Neis (2003). Moreover, CDS spread changes Granger-cause bond spread changes for a 
considerably higher number of firms than vice versa. Third, the negative intertemporal rela-
tionship between the CDS and stock market is more pronounced than the one between the 
bond and stock market. Fourth, the sensitivity of the CDS market to prior stock market 
movements is significantly related to the firm’s average creditworthiness but not to firm size. 
CDS spread changes from low-grade firms are more sensitive to lagged stock returns than 

 
28
those from firms with a relatively good rating. Interestingly, there is no such rating depend-
ency for the sensitivity of bond spread changes to lagged stock returns. Fifth, for the majority 
of the sampled firms we detect cointegration of CDS and bond spreads. A vector error correc-
tion analysis reveals that the CDS market contributes more to price discovery than the bond 
market which is consistent with findings from Blanco, Brennan, and Marsh (2004). Whereas 
the adjustment process for European firms is more dispersed between both markets, it almost 
entirely takes place in the bond market in the case of US firms indicating the leading role of 
the CDS market. Finally, a comparison of Granger causality tests for firms with and without 
cointegrated spreads confirms that in both groups CDS spread changes Granger cause bond 
spread changes for a higher number of firms than vice versa. 
 
Although our empirical analysis is somehow limited due to data imperfections and meth-
odological issues, we think it essentially captures the relationship between the three markets 
and basically confirms findings from related studies. Besides the need for a larger interna-
tional data set, and if available transaction prices instead of quotes, further research should 
consider institutional features of the CDS market (credit events, settlement terms, currency 
etc.) and their influence on the relationship of CDS spreads to prices of other credit risk sensi-
tive claims for the same firm. Moreover, a corresponding study without the stock market 
analysis, could be carried out for a sample of sovereign reference entities which represent the 
most liquid segment of the CDS market. Furthermore, as the CDS market appears to be a 
more flexible place for price discovery than the bond market, it would be interesting to ana-
lyze the informational efficiency of the CDS market in critical times which could be defined 
by pronounced increases in the implied equity volatility of a specific firm, an industry, or the 
general market. Finally, another promising avenue for research is to decompose CDS and 
bond spreads in default and non-default components and compare their dynamics across 
markets [for a first investigation see Longstaff, Mithal, and Neis (2004)]. 

 
29
Appendix A: Sample composition and median CDS spreads by year 
No. Firm
2000
2001
2002
1
COMMERZBANK AG
13
22
32
636
2
DRESDNER BANK AG
12
18
18
731
3
VOLKSWAGEN AG
26
35
45
739
4
DEUTSCHE BANK AG
12
20
26
650
5
IBERDROLA SA
26
30
39
742
6
SOCIETE GENERALE
13
18
22
740
7
RENAULT SA
44
67
100
700
8
TOKYO ELECTRIC POWER CO
10
20
32
538
9
TOYOTA MOTOR CORP
10
22
20
564
10
KOREA DEVELOPMENT BANK
112
122
73
654
11
KON PHILIPS ELECTRONICS NV
31
55
87
739
12
VOLVO AB
-
90
73
363
13
MERRILL LYNCH & CO INC
35
45
78
739
14
CITIGROUP INC
23
32
40
703
15
ALTRIA GROUP
110
85
110
741
16
MORGAN STANLEY DEAN WITTER & CO
29
49
59
735
17
GOLDMAN SACHS GROUP INC
36
52
62
757
18
TELEFONICA SA
43
89
106
750
19
FRANCE TELECOM SA
43
146
369
761
20
BNP PARIBAS SA
13
18
19
655
21
BT GROUP - BRITISH TELECOM
37
105
96
759
22
NATIONAL GRID GROUP PLC
26
41
59
742
23
SAINSBURY J LTD
-
33
31
338
24
IMPERIAL CHEMICAL INDUSTRIES PLC
44
96
139
678
25
INVESTOR AB
26
35
80
690
26
ERICSSON AB
22
162
599
722
27
BANK OF AMERICA CORP
27
36
40
712
28
FORD MOTOR CREDIT CO
43
95
251
692
29
SANPAOLO IMI SPA
16
20
23
709
30
WELLS FARGO & CO
26
28
31
641
31
WALT DISNEY CO
21
33
83
678
32
LEHMAN BROTHERS HOLDINGS INC
65
71
73
734
33
BEAR STEARNs INC
57
73
69
731
34
GENERAL MOTORS ACCEPTANCE CORP
39
95
175
705
35
PEARSON PLC
55
59
96
637
36
MARKS & SPENCER PLC
28
55
45
739
37
ENDESA SA
26
35
48
704
38
DEUTSCHE TELEKOM AG
43
115
251
750
39
HOUSEHOLD FINANCE CORP
60
77
185
719
40
BOEING CORP
19
28
63
710
41
IBM CORP
21
42
57
689
42
CARREFOUR SA
26
29
29
739
43
REPSOL YPF SA
27
53
353
730
44
KPN NV
43
245
234
756
45
DAIMLERCHRYSLER AG
27
125
142
746
46
FIAT SPA
41
100
401
759
47
LOCKHEED MARTIN CORP
72
74
73
710
48
TOTALFINAELF SA
19
18
23
715
49
VODAFONE GROUP PLC
42
66
94
761
50
UNITED UTILITIES PLC
63
55
50
588
51
COX COMMUNICATIONS INC
75
121
303
539
52
BANK ONE CORP
35
54
39
729
53
DEERE & CO
34
54
72
692
54
HILTON HOTELS CORP
-
175
290
494
55
KONINKLIJKE AHOLD NV
59
51
85
705
56
BRITISH AMERICAN TOBACCO PLC
85
60
65
687
57
LAFARGE SA
44
65
78
675
58
BANCO SANTANDER CENTRAL HISPANO 
13
29
40
708
Median CDS spreads
No. of obs.
 

 
30
Appendix B: Characteristics of the corporate bonds 
This table presents main characteristics of corporate bonds with a maturity of five years or below during the 
sampling period which were selected to construct the synthetic five year constant-maturity bond. 
 
No. Issuer
ISIN
Bloomberg 
no.
Currency
Notional
Coupon
Issue date
Maturity date
Payment 
frequency
Convention
1
Commerzbank
DE0003922399
EE1554133
DEM
50.000,00
8,000
11.10.94
11.10.04
A
ISMA 30/360
2
Dresdner Finance B.V.
DE0004132253
TT3177884
EUR
511.291,88
6,250
11.03.94
11.03.04
A
Act/Act
3
Volkswagen Int Fin
DE0004104708
TT3147234
DEM
1.000.000,00
7,000
26.05.93
26.05.03
A
ISMA 30/360
4
Deutsche Bank
DE0003040465
EC1242139
EUR
500.000,00
3,500
28.04.99
28.04.04
A
Act/Act
5
Iberdrola Intl.
XS0106975229
EC2304441
EUR
25.000,00
5,510
27.01.00
27.01.05
A
Act/Act
6
Societe Generale
FR0100786120
FF1037291
EUR
76.224,51
6,500
15.03.95
15.03.04
A
Act/Act
7
Renault SA
XS0048887409
TT3174113
FRF
2.000.000,00
6,250
02.03.94
02.03.04
A
ISMA-30/360
8
Tokyo Electric Power Co
XS0095626569
EC1116507
EUR
750.000,00
4,000
24.03.99
24.03.04
A
Act/Act
9
Toyota Motor Credit Corp
XS0101844792
EC1777001
USD
250.000,00
6,750
30.09.99
30.09.04
A
ISMA 30/360
10 Korea Development Bank
US500630AY49
EC1248458
USD
1.000.000,00
7,125
22.04.99
22.04.04
SA
ISMA 30/360
11 Kon. Philips Electronics N.V.
US718448AC78
DD0020527
USD
250.000,00
7,750
14.04.94
15.04.04
SA
30/360
12 Volvo Treasury
XS0102706776
EC1849933
EUR
1.000.000,00
5,125
12.10.99
12.10.04
A
Act/Act
13 Merrill Lynch & Co. 
XS0080348260
MM1295185
USD
500.000,00
6,750
24.09.97
24.09.04
A
ISMA 30/360
14 Citigroup Inc
US172967AW18
EC1178127
USD
750.000,00
5,800
31.03.99
15.03.04
SA
30/360
15 Altria Group Inc
US718154CH83
DD1107547
USD
500.000,00
7,500
07.04.97
01.04.04
SA
30/360
16 Morgan Stanley Dean Witter
US617446DE61
EC0890805
USD
2.000.000,00
5,625
20.01.99
20.01.04
SA
30/360
17 Goldman Sachs Group
US38141GAK04
EC2209640
USD
750.000,00
7,500
28.01.00
28.01.05
SA
30/360
18 Telefonica Europe B.V.
XS0118006377
EC2933116
EUR
1.000.000,00
6,125
21.09.00
21.09.05
A
Act/Act
19 France Telecom
FR0000583270
FF1023184
EUR
228.673,53
5,750
08.11.93
08.11.04
A
Act/Act
19 France Telecom
FR0000483653
EC3052106
EUR
1.000.000,00
6,125
10.11.00
10.11.05
A
Act/Act
20 BNP Paribas
XS0047262513
TT3169071
EUR
609.796,00
6,500
03.12.93
03.12.04
A
ISMA 30/360
21 British Telecom PLC
XS0045856316
TT3162233
GBP
500.000,00
7,125
15.09.93
15.09.03
A
ISMA 30/360
22 British Gas Intl Finance
XS0042735240
TT3140270
GBP
200.000,00
8,125
31.03.93
31.03.03
A
ISMA 30/360
23 J. Sainsbury PLC
XS0110680229
EC2494648
GBP
100.000,00
6,875
27.04.00
27.04.05
A
ISMA 30/360
24 ICI Investments BV
GB0004582788
ZZ2043995
GBP
100.000,00
10,000
15.04.86
15.04.03
A
ISMA 30/360
25 Investor AB
XS0096108120
EC1165249
EUR
400.000,00
4,250
13.04.99
13.04.06
A
Act/Act
26 Ericsson AB
XS0093071768
EC0749464
USD
300.000,00
5,188
10.12.98
10.12.03
A
ISMA 30/360
27 Bank of America Corp
US638585BJ73
EC0087048
USD
450.000,00
6,125
23.07.98
15.07.04
SA
30/360
28 Ford Motor Credit Co.
US345397SH76
EC1040772
USD
2.000.000,00
5,750
23.02.99
23.02.04
SA
30/360
29 San Paolo IMI
XS0109620640
EC2893583
EUR
15.000,00
5,450
31.03.00
31.03.05
A
Act/Act
30 Wells Fargo Company
US949746AA96
EC1616050
USD
1.500.000,00
6,625
28.07.99
15.07.04
SA
ISMA 30/360
31 Walt Disney Company
US254687AM80
TT3274467
USD
1.300.000,00
6,750
27.03.96
30.03.06
SA
30/360
32 Lehman Brothers Holdings Inc
US524908BZ26
EC1170801
USD
1.250.000,00
6,625
26.03.99
01.04.04
SA
30/360
33 Bear Stearns Co Inc
US073902BS60
EC2210960
USD
850.000,00
7,625
01.02.00
01.02.05
SA
30/360
34 General Motors Corp
US370442AX38
MM1353430
USD
500.000,00
6,250
29.04.98
01.05.05
SA
30/360
35 Pearson PLC
XS0052937587
TT3191133
GBP
125.000,00
9,500
04.10.94
04.10.04
A
ISMA 30/360
36 Marks & Spencer Finance
XS0091642354
EC0537158
GBP
50.000,00
6,160
16.10.98
17.10.03
A
ISMA 30/360
37 International Endesa BV
XS0085656600
MM1336922
USD
500.000,00
5,875
31.03.98
31.03.03
A
ISMA 30/360
38 Deutsche Telekom Int Fin
XS0113743289
EC2696911
EUR
2.250.000,00
6,125
06.07.00
06.07.05
A
Act/Act
39 Household Finance Corp
US441812FV10
DD1070158
USD
250.000,00
7,250
18.07.96
15.07.03
SA
30/360
40 Boeing Corp
US097023AL95
DD5296247
USD
300.000,00
6,350
21.06.93
15.06.03
SA
30/360
41 IBM Corp
XS0095989793
EC1178002
USD
160.000,00
5,100
08.04.99
08.04.03
SA
ISMA 30/360
42 Carrefour SA
XS0100126431
EC1596823
EUR
1.000.000,00
4,375
29.07.99
15.09.04
A
Act/Act
43 Repsol Intl Finance BV
XS0094812814
EC1008225
EUR
1.725.000,00
3,750
23.02.99
23.02.04
A
Act/Act
44 Koninklijke KPN NV
XS0099230715
EC1514891
EUR
1.250.000,00
4,000
30.06.99
30.06.04
A
Act/Act
45 DaimlerChrysler Intl Fin
DE0002849809
EC0879261
EUR
200.000,00
3,500
29.01.99
29.01.04
A
Act/Act
46 Fiat Finance & Trade
XS0095927504
EC1146298
EUR
1.000.000,00
3,750
31.03.99
31.03.04
A
Act/Act
47 Lockheed Martin Corp
US539821AL25
DD5284532
USD
300.000,00
6,750
18.03.93
15.03.03
SA
30/360
48 Total Fina Elf S.A.
DE0001930402
TT3341738
DEM
250.000,00
5,250
07.07.97
23.12.03
A
ISMA 30/360
49 Vodafone Finance BV
DE0003516605
EC1745487
EUR
2.500.000,00
4,875
08.09.99
08.09.04
A
Act/Act
50 United Utilities Water plc
XS0119256427
EC3060984
EUR
120.000,00
6,000
18.10.00
01.12.05
A
ISMA 30/360
51 Cox Communications Inc
US22404QAE89
MM1313574
USD
100.000,00
6,690
19.09.97
20.09.04
SA
30/360
52 Bank One Corp
US06422NCN49
EC1023521
USD
500.000,00
5,625
17.02.99
17.02.04
SA
30/360
53 Deere & Co
US244199AX30
EC1596062
USD
250.000,00
6,550
19.07.99
15.07.04
SA
30/360
54 Hilton Hotels Corp
XS0044959855
TT3140056
GBP
125.000,00
8,875
11.08.93
11.08.03
A
ISMA 30/360
55 Ahold Finance USA Inc
XS0112351662
EC2610268
EUR
1.500.000,00
6,375
08.06.00
08.06.05
A
Act/Act
56 BAT Intl Finance PLC
XS0096054282
EC1160182
EUR
1.500.000,00
4,250
14.04.99
14.04.04
A
Act/Act
57 Lafarge
FR0000495483
EC1532208
EUR
500.000,00
4,375
15.07.99
15.07.04
A
Act/Act
58 Santander Intl (C.I.)
DE0002310307
MM1351533
DEM
500.000,00
5,000
21.04.98
21.04.05
A
ISMA 30/360 
 

 
31
Appendix B (continued): 
This table presents main characteristics of corporate bonds with a maturity of more than five years during the 
sampling period which were selected to construct the synthetic five year constant-maturity bond. 
 
No.
Issuer
ISIN
Bloomberg no.
Currency
Notional
Coupon
Issue date
Maturity date
Payment 
frequency
Convention
1
Commerzbank
DE0001848083
EC0980572
EUR
1.500.000,00
4,250
16.02.99
25.10.09
A
Act/Act
2
Dresdner Finance B.V.
XS0087184312
TT3420722
EUR
758.678,25
5,250
20.05.98
04.01.09
A
Act/Act
3
Volkswagen Int Fin
XS0142019479
EC5077994
EUR
1.000.000,00
5,375
25.01.02
15.01.12
A
Act/Act
4
Deutsche Bank
DE0002312857
TT3368392
EUR
1.224.284,87
5,000
30.04.98
04.01.09
A
Act/Act
5
Iberdrola Intl.
XS0097762065
EC1350411
EUR
600.000,00
4,500
25.05.99
25.05.09
A
Act/Act
6
Societe Generale
FR0100113937
FF1028019
EUR
49.545,93
6,800
19.03.96
19.03.07
A
Act/Act
7
Renault SA
FR0000495699
EC1556298
EUR
500.000,00
5,125
21.07.99
21.07.06
A
Act/Act
7
Renault SA
FR0000483083
EC2976081
EUR
500.000,00
6,375
19.10.00
19.10.07
A
Act/Act
8
Tokyo Electric Power Co
XS0096998561
EC1263309
EUR
1.000.000,00
4,375
14.05.99
14.05.09
A
Act/Act
9
Toyota Motor Credit Corp
US892332AH00
EC0784057
USD
300.000,00
5,500
14.12.98
15.12.08
SA
30/360
10
Korea Development Bank
US500630AM01
TT3278757
USD
750.000,00
7,250
22.05.96
15.05.06
SA
ISMA 30/360
11
Kon. Philips Electronics N.V.
US718448AB95
DD5305659
USD
250.000,00
7,250
24.08.93
15.08.13
SA
30/360
12
Volvo Treasury
FR0000109647
TT3342033
EUR
152.449,00
6,125
11.06.97
11.06.09
A
ISMA 30/360
13
Merrill Lynch & Co. 
US590188JP48
EC1008209
USD
2.000.000,00
6,000
17.02.99
17.02.09
SA
ISMA 30/360
14
Citigroup Inc
US172967AX90
EC1178168
USD
750.000,00
6,200
31.03.99
15.03.09
SA
ISMA 30/360
15
Philip Morris Comp Corp
XS0099837832
EC1568996
USD
500.000,00
7,500
16.07.99
16.07.09
A
ISMA 30/360
16
Morgan Stanley Dean Witter
US617446AB59
US617446AB59
USD
100.000,00
10,000
28.06.88
15.06.08
SA
30/360
17
Goldman Sachs Group
US38141MMP31
EC1046498
USD
220.000,00
6,500
23.02.99
25.02.09
SA
30/360
18
Telefonica S.A.
ES0278430931
EC1141273
EUR
500.000,00
4,500
14.04.99
14.04.09
A
Act/Act
19
France Telecom
FR0000583288
FF1036368
EUR
914.694,10
5,750
07.02.97
25.04.07
A
Act/Act
19
France Telecom
XS0126164812
EC3574349
EUR
3.500.000,00
6,750
14.03.01
14.03.08
A
Act/Act
20
BNP Paribas
XS0089305469
EC0090984
EUR
600.000,00
5,625
07.08.98
07.08.08
A
ISMA 30/360
21
British Telecom PLC
XS0052067583
TT3189525
GBP
300.000,00
8,625
23.08.94
26.03.20
A
ISMA 30/360
22
British Gas Intl Finance
XS0044417375
TT3155062
GBP
250.000,00
8,875
08.07.93
08.07.08
A
ISMA 30/360
23
J. Sainsbury PLC
XS0132125112
EC4118245
GBP
300.000,00
6,500
11.07.01
11.07.12
A
Act/Act
24
ICI Investments BV
XS0079094891
MM1260221
GBP
300.000,00
7,625
21.08.97
21.08.07
A
ISMA 30/360
25
Investor AB
XS0088607931
MM1210358
EUR
300.000,00
5,250
30.06.98
30.06.08
A
Act/Act
26
Ericsson AB
XS0097717358
EC1349611
USD
500.000,00
6,500
20.05.99
20.05.09
A
ISMA 30/360
27
Bank of America Corp
US066050CV50
EC0984251
USD
1.500.000,00
5,875
08.02.99
15.02.09
SA
ISMA 30/360
28
Ford Motor Credit Co.
US345397SM61
EC1921211
USD
5.000.000,00
7,375
28.10.99
28.10.09
SA
ISMA 30/360
29
San Paolo IMI
IT0001211496
II1061961
EUR
258.228,00
5,390
16.03.98
17.03.10
A
Act/Act
30
Wells Fargo Company
EC0967645
EC0967645
USD
200.000,00
5,625
03.02.99
03.02.09
SA
30/360
31
Walt Disney Company
US25469HBD44
DD5314966
USD
125.000,00
5,800
27.10.93
27.10.08
SA
30/360
32
Lehman Brothers Holdings Inc
US52490BQ27
DD1126778
USD
250.000,00
7,200
19.08.97
15.08.09
SA
30/360
33
Bear Stearns Co Inc
US073902BR87
EC2041472
USD
800.000,00
7,625
07.12.99
07.12.09
SA
30/360
34
General Motors Corp
US370442AY11
MM1365079
USD
500.000,00
6,375
29.04.98
01.05.08
SA
30/360
35
Pearson PLC
GB0006777725
TT2007348
GBP
100.000,00
10,500
13.06.88
13.06.08
A
ISMA 30/360
36
Marks & Spencer Finance
XS0138137285
EC4710371
GBP
375.000,00
6,375
07.11.01
07.11.11
A
Act/Act
37
International Endesa BV
XS0095981972
EC1152171
USD
350.000,00
6,000
07.04.99
07.04.09
A
ISMA 30/360
38
Deutsche Telekom Int Fin
DE0002317807
TT3435043
EUR
2.000.000,00
5,250
20.05.98
20.05.08
A
Act/Act
39
Household Finance Corp
US441812GA63
EC0127471
USD
500.000,00
6,375
28.07.98
01.08.10
SA
30/360
40
Boeing Corp
US09700WAK99
MM1339926
USD
15.000,00
6,580
29.12.97
15.01.09
SA
30/360
41
IBM Corp
US45920QBX16
EC0890441
USD
100.000,00
5,500
15.01.99
15.01.09
SA
30/360
42
Carrefour SA
FR0000492282
EC1090496
EUR
1.000.000,00
4,500
18.03.99
18.03.09
A
Act/Act
43
Repsol Intl Finance BV
XS0110487062
EC2479870
EUR
1.175.000,00
6,000
05.05.00
05.05.10
A
Act/Act
44
Koninklijke KPN NV
XS0091945419
EC0591007
EUR
1.500.000,00
4,750
05.11.98
05.11.08
A
Act/Act
45
DaimlerChrysler Intl Fin
XS0126467124
EC3583522
EUR
2.500.000,00
6,125
21.03.01
21.03.06
A
Act/Act
46
Fiat Finance & Trade
XS0107525403
EC2237518
EUR
1.000.000,00
6,250
24.02.00
24.02.10
A
Act/Act
47
Lockheed Martin Corp
US539830AL32
EC2005832
USD
1.000.000,00
8,200
23.11.99
01.12.09
SA
30/360
48
Total Fina Elf S.A.
FR0000207003
FF1031807
EUR
373.502,50
6,750
08.07.96
25.10.08
A
Act/Act
48
Total Fina Elf S.A.
FR0000186173
EC1215960
EUR
300.000,00
3,875
05.05.99
05.05.06
A
Act/Act
49
Vodafone Finance BV
DE0003084505
EC1375731
EUR
3.000.000,00
4,750
27.05.99
27.05.09
A
Act/Act
50
United Utilities Water plc
XS0095536909
EC1100253
EUR
600.000,00
4,875
18.03.99
18.03.09
A
Act/Act
51
Cox Communications Inc
US224044AG22
DD1022506
USD
150.000,00
7,625
27.06.95
15.06.25
SA
30/360
51
Cox Communications Inc
US22404QAD07
MM1225745
USD
60.000,00
7,030
06.11.96
06.11.06
SA
30/360
52
Bank One Corp
US06423AAD54
EC1599066
USD
1.000.000,00
6,875
22.07.99
01.08.06
SA
30/360
52
Bank One Corp
US06423AAN37
EC4322730
USD
1.250.000,00
6,000
08.08.01
01.08.08
SA
ISMA 30/360
53
John Deere Capital Corp
US244217BC81
EC1059582
USD
300.000,00
6,000
25.02.99
15.02.09
SA
30/360
54
Hilton Hotels Corp
XS0100088755
EC1597649
GBP
175.000,00
7,250
29.07.99
29.07.08
A
ISMA 30/360
55
Koninklijke Ahold NV
NL0000118560
EC3070249
EUR
200.000,00
6,375
30.11.00
30.11.07
A
Act/Act
56
BAT Intl Finance PLC
XS0094703799
EC0991710
EUR
1.700.000,00
4,875
25.02.99
25.02.09
A
Act/Act
57
Lafarge
FR0000208761
FF1032714
EUR
152.450,00
5,400
03.02.98
03.02.08
A
Act/Act
57
Lafarge SA
FR0000481665
EC2734035
EUR
700.000,00
6,375
26.07.00
26.07.07
A
Act/Act
58
Santander Intl (C.I.)
DE0002302353
TT3422868
DEM
500.000,00
5,375
11.03.98
12.02.08
A
ISMA 30/360 
 

 
32
References 
Alexander, G., Edwards, A., Ferri, M., 2000. What does Nasdaq’s High-Yield bond market 
reveal about bondholder-stockholder conflicts? Financial Management 29, 23-39. 
Arsov, I., Gizycki, G., 2003. New measures of credit risk. Reserve Bank of Australia Bulletin, 
July 2003, 10-14. 
Aunon-Nerin, D., Cossin, D., Hricko, T., Huang, Z., 2002. Exploring for the determinants of 
credit risk in credit default swap transaction data: is fixed-income markets’ information 
sufficient to evaluate credit risk? International Center for Financial Asset Management 
and Engineering, Research Paper No. 65, December 2002. 
Avramov, D., Jostova, G., Philipov, A., 2004. Corporate credit risk changes: common factors 
and firm-level fundamentals. Working Paper, April 20, 2004. 
Bank for International Settlements, 2003. Credit risk transfer. Committee on the Global Fi-
nancial System, Working Paper, January 2003. 
Basel Committee on Banking Supervision, 2004. International convergence of capital meas-
urement and capital standards, a revised framework, June 2004. 
Berndt, A., Douglas, R., Duffie, D., Ferguson, M., Schranz, D., 2004. Measuring default risk 
premia from default swap rates and EDFs. Working Paper, March 29, 2004. 
Blanco, R., Brennan, S., Marsh, I., 2004. An empirical analysis of the dynamic relationship 
between investment-grade bonds and credit default swaps. July 22, 2004, forthcoming 
Journal of Finance. 
Blume, M., Keim, D., Patel, S., 1991. Returns and volatility of low-grade bonds 1977-1989. 
Journal of Finance 46, 49-74. 
British Bankers’ Association, 2002. BBA Credit Derivatives Report 2001/2002. London. 
Collin-Dufresne, P., Goldstein, R., Martin, J., 2001. The determinants of credit spread 
changes. Journal of Finance 56, 2177-2207. 

 
33
Cornell, B., Green, K., 1991. The investment performance of low-grade bond funds. Journal 
of Finance 46, 29-48. 
Deutsche Bundesbank, 2004. Credit risk transfer instruments: their use by German banks and 
aspects of financial stability. Monthly Report April, 27-45. 
Engle, R., Granger, C., 1987. Co-integration and error correction: representation, estimation, 
and testing. Econometrica 55, 251-276. 
European Central Bank, 2004. Credit risk transfer by EU banks: activities, risks and risk 
management, May 2004. 
Fama, E., French, K., 1993. Common risk factors in the returns on stocks and bonds. Journal 
of Financial Economics 33, 3-56. 
Fitch Ratings, 2003. Global credit derivatives: a qualified success. Special Report, September 
24, 2003. 
Gonzalo, J., Granger, C., 1995. Estimation of common long-memory components in cointe-
grated systems. Journal of Business and Economic Statistics 13, 27-35. 
Granger, C., 1969. Investigating causal relations by econometric models and cross-spectral 
methods. Econometrica 37, 424-438. 
Gujarati, D., 2003. Basic Econometrics. 4th ed., McGraw-Hill, New York. 
Hotchkiss, E., Ronen, T., 2002. The informational efficiency of the corporate bond market: an 
intraday analysis. Review of Financial Studies 15, 1325-1354. 
Houweling, P., Vorst, T., 2002. An empirical comparison of default swap pricing models. 
Working Paper, Erasmus University Rotterdam. 
Hull, J., Predescu, M., White, A., 2003. The relationship between credit default swap spreads, 
bond yields, and credit rating announcements. Forthcoming Journal of Banking and Fi-
nance. 

 
34
Kwan, S., 1996. Firm-specific information and the correlation between individual stocks and 
bonds. Journal of Financial Economics 40, 63-80. 
Longstaff, F., Mithal, S., Neis, E., 2003. The credit-default swap market: is credit protection 
priced correctly? Working Paper, August 2003. 
Longstaff, F., Mithal, S., Neis, E., 2004. Corporate yield spreads: default risk or liquidity? 
New evidence from the credit-default swap market. National Bureau of Economic Re-
search, Working Paper 10418, April 2004. 
Norden, L., Weber, M., 2004. Informational efficiency of credit default swap and stock mar-
kets: the impact of credit rating announcements. CEPR Discussion Paper No. 4250, forth-
coming Journal of Banking and Finance. 
O’Kane, D., McAdie, R., 2001. Explaining the basis: cash versus default swaps. Lehman 
Brothers, May 2001. 
Stock, J., Watson, M., 2001. Vector autoregressions. Journal of Economics Perspectives 15, 
Fall, 101-115. 
Zhu, H., 2004. An empirical comparison of credit spreads between the bond market and the 
credit default swap market. BIS Working Paper No. 160, August 2004. 

 
35
Table 1: Firm and bond characteristics 
Panel A: Firms by size and rating 
 
Size (in millions of Euro) represents a firm’s market capitalization in local currency converted with the daily 
Euro exchange rate. Rating is an aggregated rating obtained from a mapping of Moody’s, Standard & Poor’s and 
Fitch’s credit ratings on a numerical 17 grade scale (AAA / Aaa= 1, AA+ / Aa1 = 2, ..., CCC /Caa1 and below = 
17). 
 
Size (mil. EUR) 
 
10% quantile 
50% quantile 
90% quantile 
Mean 
 
Jan 2000 
4,739 
24,156 
134,225 
44,378 
 
Jun 2001 
4,981 
30,038 
113,404 
47,546 
 
Dec 2002 
3,414 
20,322 
79,635 
32,121 
Rating (in %) 
 
1 
2 
3
4
5
6
7
8
9
10 
11 
12 Mean St.D.
 
Jan 2000 
0 3.6 7.1 16.1 28.6 19.6 10.7
5.4
5.4
3.6 
0 
0 
5.6
1.8
 
Jun 2001 
0 1.8 1.8 14.3 23.2 25.0 14.3
7.1
8.9
3.6 
0 
0 
6.1
1.8
 
Dec 2002 
0 1.8 1.8
8.9 19.6 19.6 12.5 14.3 14.3
3.6 1.8 1.8 
6.7
2.1
 
Panel B: Bonds by notional, coupon, maturity, and currency 
 
Bond data consist of one synthetically created five-year constant maturity bond per firm if, at least, two actual 
bonds with a maturity below and above five years during the sampling period existed (n=58 firms). All numbers 
refer to the time period 2000-2002, notionals are converted in EUR with the daily exchange rate, percentages are 
weighted by the number of observations. 
 
Notional (in ‘000 EUR) 
Median of bonds with maturity ≤ 5 years 
511,291 
 
Median of bonds with maturity > 5 years 
539,432 
Coupon (in %) 
Median of bonds with maturity ≤ 5 years 
6.160 
 
Median of bonds with maturity > 5 years 
6.125 
Maturity (in years) 
Median of bonds with maturity ≤ 5 years 
2.94 
 
Median of bonds with maturity > 5 year 
7.53 
Currency (in %) 
EUR 
46.5 
 
USD 
41.4 
 
GBP 
12.1 
 
 

 
36
Table 2: Mean CDS and bond spreads by year and rating 
 
CDS represents a five-year maturity CDS spread that refers to senior unsecured debt. BSS and BSG are the 
differences between a synthetic five-year constant maturity corporate bond yield and the equivalent currency 
five-year LIBOR interest swap rate or government bond yield. The table shows mean spreads per year and rating 
category. Spreads stem from 58 firms and are noted in basis points. In brackets, we report the underlying number 
of observations. 
 
Variable 
Year \ Rating 
1 
2-4 
5-7 
8-10 
11-13 
Total 
 
 
(AAA, Aaa) 
(AA, Aa) 
(A, A) 
(BBB, Baa) 
(BB, Ba) 
 
CDS 
2000 
- 
24.51 
(2,940) 
43.05 
(7,162) 
65.97 
(1,605) 
- 
41.53 
(11,707) 
 
2001 
- 
27.56 
(2,519) 
62.12 
(8,400) 
133.99 
(2,905) 
357.81 
(8) 
71.09 
(13,832) 
 
2002 
- 
36.88 
(2,157) 
76.49 
(6,616) 
189.00 
(4,091) 
647.76 
(324) 
118.95 
(13,188) 
 
Total 
- 
29.02 
(7,616) 
60.25 
(22,178) 
147.46 
(8,601) 
640.78 
(332) 
78.45 
(38,727) 
BSS 
2000 
- 
18.46 
(3,382) 
47.43 
(5,783) 
74.25 
(1,824) 
- 
42.97 
(10,989) 
 
2001 
- 
20.60 
(2,594) 
56.94 
(7,940) 
111.90 
(2,886) 
136.89 
(9) 
61.78 
(13,429) 
 
2002 
- 
25.63 
(2,111) 
59.98 
(6,581) 
138.10 
(3,820) 
330.5 
(332) 
84.56 
(12,844) 
 
Total 
- 
21.02 
(8,087) 
55.22 
(20,304) 
115.58 
(8,530) 
325.39 
(341) 
64.08 
(37,262) 
BSG 
2000 
- 
66.34 
(3,275) 
121.80 
(5,587) 
153.08 
(1,767) 
- 
109.91 
(10,629) 
 
2001 
- 
59.44 
(2,490) 
105.31 
(7,604) 
155.71 
(2,783) 
189.43 
(7) 
107.38 
(12,884) 
 
2002 
- 
52.80 
(2,034) 
92.96 
(6,336) 
166.38 
(3,685) 
370.51 
(320) 
115.40 
(12,375) 
 
Total 
- 
60.60 
(7,799) 
106.02 
(19,527) 
159.92 
(8,235) 
366.64 
(327) 
110.89 
(35,888) 
 

 
37
Table 3: Stationarity and autocorrelation of firm-specific time series 
Panel A reports the number of firms for which the null hypothesis of non-stationary data (stationary data) can be 
rejected by means of an Augmented Dickey-Fuller-test and a Phillips-Perron-test (Kwiatkowski-Phillips-
Schmidt-Shin (KPSS) test) with lags 1-8 for weekly data and lags 1-40 for daily data. Level (Change) refers to 
the stock price (log stock return), the CDS spread (first difference of CDS spreads) and the BSS spread (first 
difference of BSS spreads). All data come from 58 firms over the period 2000-2002. Panel B presents median 
autocorrelation coefficients of log stock returns, CDS spread changes and BSS spread changes for lags 1-5. 
 
Panel A: Stationarity tests 
 
Stock price 
 
CDS 
 
BSS 
Weekly data (Wed-Wed) 
Level 
Change 
 
Level 
Change 
 
Level 
Change 
Augmented Dickey-Fuller test 
1 
58 
 
1 
57 
 
2 
57 
Phillips-Perron test 
1 
58 
 
3 
58 
 
2 
58 
KPSS test 
43 
0 
 
41 
0 
 
22 
1 
Daily data 
 
 
 
 
 
 
 
 
Augmented Dickey-Fuller test 
1 
58 
 
5 
58 
 
0 
58 
Phillips-Perron test 
1 
58 
 
14 
58 
 
7 
58 
KPSS test 
43 
0 
 
38 
0 
 
29 
0 
 
Panel B: Median autocorrelation of stock returns and spread changes 
Weekly data (Wed-Wed) 
Lag 1 
Lag 2 
Lag 3 
Lag 4 
Lag 5 
Stock returns 
-0.08
-0.03
0.05
-0.08
0.00 
CDS spread changes 
0.07
0.01
-0.04
-0.10
0.02 
BSS spread changes 
-0.09
0.02
0.08
-0.04
-0.01 
Daily data 
 
Stock returns 
-0.01
-0.04
-0.02
-0.02
-0.01 
CDS spread changes 
0.02
0.02
0.01
0.02
0.01 
BSS spread changes 
-0.22
0.03
-0.04
0.05
-0.01 
 

 
38
Table 4: Contemporaneous correlation of firm-specific time-series 
 
Spearman’s rank correlation coefficients ρS are calculated for a pair of firm-specific time series (daily and 
weekly log stock returns R, CDS spread changes ∆CDS, and bond spread changes ∆BSS). Data stem from 58 
firms over the period 2000-2002 and the rating is as of January 2000. All correlation coefficients (except in the 
first rows) are medians. 
 
 
 
Weekly data 
 
Daily data 
 
 
ρS(R, ∆CDS) 
ρS(R, ∆BSS) 
ρS(∆CDS,∆BSS)
 
ρS(R, ∆CDS) 
ρS(R, ∆BSS) 
ρS(∆CDS,∆BSS) 
Overall 
Mean 
-0.25 
-0.13 
0.25 
 
-0.10 
-0.02 
0.09 
 
Median 
-0.27 
-0.09 
0.22 
 
-0.11 
-0.01 
0.05 
 
p < 0.01 
35 
15 
28 
 
31 
11 
15 
 
p < 0.05 
42 
18 
34 
 
39 
14 
23 
 
p < 0.10 
44 
21 
39 
 
43 
17 
25 
Region 
Europe 
-0.27 
-0.10 
0.28 
 
-0.09 
-0.03 
0.08 
 
USA 
-0.31 
-0.08 
0.21 
 
-0.12 
0.01 
0.03 
 
Asia 
0.00 
-0.07 
0.09 
 
-0.07 
-0.01 
0.04 
Rating 
2-4 
-0.15 
-0.04 
0.18 
 
-0.06 
-0.01 
0.03 
 
5-7 
-0.31 
-0.12 
0.21 
 
-0.11 
0.00 
0.03 
 
8-10 
-0.25 
-0.09 
0.22 
 
-0.12 
-0.03 
0.07 
Industry Telco 
-0.36 
-0.23 
0.49 
 
-0.16 
-0.11 
0.25 
 
Rest 
-0.25 
-0.08 
0.20 
 
-0.10 
0.00 
0.03 
 
Financ. 
-0.35 
-0.08 
0.21 
 
-0.13 
0.00 
0.03 
 
Rest 
-0.26 
-0.10 
0.22 
 
-0.11 
-0.01 
0.07 
 

 
39
Table 5: VAR estimation results 
Our VAR model consists of three-equations with the log stock return (Rt), the CDS spread change (∆CDSt), and 
the bond spread change (∆BSSt) as dependent variables respectively. Numbers represent median coefficients 
(columns 2, 5, and 8) and the absolute frequency of firms for which the coefficient of the explanatory variable is 
significantly different from zero at the 0.01-level (columns 3, 6, and 9). Columns 4, 7, 10 report the number of 
firms for which we can reject the null hypotheses at a 0.01-level (Wald test) that lags 1 to P have no joint ex-
planatory power (the Wald test for p=5 corresponds to a Granger causality test). For each equation we addition-
ally show the median R2, median p-value from a standard F-Test and the number of firms which exhibit a F-test 
p-value below 0.01. The hypothesis that the residuals come from a white-noise process is tested with a Ljung-
Box (LB) test (weekly data: lags 1-8, daily data: lags 1-40) and Bartlett’s test (B) for each equation and firm 
separately. Data stem from 58 firms over the period 2000-2002.  
 
Panel A: Estimation results for weekly data (Wed-Wed) 
 
Column: (1) 
(2) 
(3) (4)  
(5) 
(6) (7)  
(8) 
(9) (10) 
Dep. Var.  
Rt 
 
 
 
∆CDSt 
 
 
 
∆BSSt 
 
 
Rt-1 
-0.06 
5 
 
 
-15.62 
19 
 
 
-5.93 
4 
 
Rt-2 
-0.03 
1 
 
 
-5.25 
2 
13 
 
-5.40 
5 
5 
∆CDSt-1 
0.00 
3 
 
 
0.01 
9 
 
 
0.16 
23 
 
∆CDSt-2 
0.00 
0 
2 
 
0.01 
9 
 
 
0.09 
8 
24 
∆BSSt-1 
0.00 
2 
 
 
-0.01 
3 
 
 
-0.18 
26 
 
∆BSSt-2 
0.00 
2 
4 
 
0.00 
6 
6 
 
-0.08 
10 
 
Const. 
0.00 
0 
 
 
0.18 
0 
 
 
0.21 
0 
 
Median R2 
0.0568 
 
 
 
0.0952 
 
 
 
0.1281 
 
 
Median p-val. F 
0.1799 
 
 
 
0.0189 
 
 
 
0.0021 
 
 
No. F-test p<0.01 9 
 
 
 
27 
 
 
 
35 
 
 
Residuals: 
 
 
 
 
 
 
 
 
 
 
 
No. LB-p. <0.01 
2 
 
 
 
11 
 
 
 
9 
 
 
No. B-p. <0.01 
0 
 
 
 
0 
 
 
 
1 
 
 
 
Panel B: Estimation results for daily data 
 
Column: (1) 
(2) 
(3) (4)  
(5) 
(6) (7)  
(8) 
(9) (10) 
Dep. Var.  
Rt 
 
 
 
∆CDSt 
 
 
 
∆BSSt 
 
 
Rt-1 
-0.01 
9 
 
 
-14.67 
32 
 
 
-9.27 
21 
 
Rt-2 
-0.04 
5 
 
 
-7.09 
20 
36 
 
-6.21 
6 
21 
Rt-3 
-0.02 
4 
 
 
-5.70 
15 
35 
 
-1.44 
0 
20 
Rt-4 
-0.01 
3 
 
 
-4.25 
12 
37 
 
-2.89 
2 
20 
Rt-5 
-0.02 
1 
 
 
-0.68 
2 
39 
 
-1.19 
1 
19 
∆CDSt-1 
0.00 
3 
 
 
-0.02 
23 
 
 
0.08 
20 
 
∆CDSt-2 
0.00 
2 
4 
 
-0.01 
15 
 
 
0.05 
12 
23 
∆CDSt-3 
0.00 
1 
5 
 
-0.02 
11 
 
 
0.05 
10 
25 
∆CDSt-4 
0.00 
0 
5 
 
0.02 
12 
 
 
0.04 
8 
30 
∆CDSt-5 
0.00 
0 
5 
 
0.01 
4 
 
 
0.03 
9 
33 
∆BSSt-1 
0.00 
2 
 
 
0.03 
16 
 
 
-0.27 
47 
 
∆BSSt-2 
0.00 
2 
2 
 
0.02 
13 
19 
 
-0.09 
28 
 
∆BSSt-3 
0.00 
6 
6 
 
0.00 
6 
18 
 
-0.08 
22 
 
∆BSSt-4 
0.00 
2 
4 
 
0.01 
4 
19 
 
0.00 
10 
 
∆BSSt-5 
0.00 
1 
4 
 
0.00 
5 
19 
 
0.00 
6 
 
Const. 
0.00 
0 
 
 
0.04 
0 
 
 
0.04 
0 
 
Median R2 
0.0323 
 
 
 
0.0977 
 
 
 
0.1479 
 
 
Median p-val. F 
0.0991 
 
 
 
0.0000 
 
 
 
0.0000 
 
 
No. F-p. <0.01 
12 
 
 
 
54 
 
 
 
57 
 
 
Residuals: 
 
 
 
 
 
 
 
 
 
 
 
No. LB-p. <0.01 
4 
 
 
 
27 
 
 
 
16 
 
 
No. B-p. <0.01 
0 
 
 
 
0 
 
 
 
0 
 
 
 

 
40
Table 6: Results from cointegration tests and VECM estimation 
 
Pane A reports results from a Johansen test for cointegration (likelihood ratio or trace test) between the CDS 
spread level and the bond spread level above swap rates (BSS). The coefficients of the error correction term 
(lagged residuals from the cointegration equation) λ1 and λ2 are estimated in a two-equation vector error correc-
tion model (VECM) with ∆CDSt and ∆BSSt as endogenous variables and lags 1-5. GG is the Gonzalo-Granger 
measure of price discovery is calculated as GG = λ2 / (λ2 - λ1). For firms with a GG measure higher than one 
(0.10-level: 7 firms, 0.01-level: 2 firms) or lower than zero (0.10-level: 2 firms, 0.01-level: no firm) we replace 
the original values by one and zero for the calculation of means and medians. Panel B reports the frequency of 
significant and correctly signed coefficients λ1 and λ2 (at the 0.01-level) for firms at which cointegration is 
present at the 0.10-level (0.01-level in brackets). 
 
Panel A: Cointegration tests and error correction coefficients 
Cointegration between spreads at the 0.10-level 
 
No. of firms 
Mean λ1
Median λ1
Mean λ2
Median λ2
Mean GG Median GG
Europe 
20 / 35 
-0.0299
-0.0204
0.0299
0.0292
0.55 
0.58
USA 
15 / 20 
-0.0117
-0.0059
0.0678
0.0587
0.84 
0.93
Asia 
1 / 3 
0.0076
-
0.0910
-
1.09 
-
All firms 
36 / 58 
-0.0208
-0.0109
0.0474
0.0377
0.69 
0.79
Cointegration between spreads at the 0.01-level 
 
No. of firms 
Mean λ1
Median λ1
Mean λ2
Median λ2
Mean GG Median GG
Europe 
11 /35 
-0.0457
-0.0482
0.0357
0.0293
0.47 
0.38
USA 
10 / 20 
-0.0103
-0.0045
0.0837
0.0680
0.91 
0.95
Asia 
0 / 3 
-
-
-
-
- 
-
All firms 
21 /58 
-0.0288
-0.0131
0.0586
0.0448
0.68 
0.78
 
Panel B: Sign and significance of error correction coefficients 
 
Only bond market 
contributes 
Only CDS market 
contributes 
λ2 > 0 
Both markets 
contribute 
λ1 < 0 and λ2 > 0 
Unclear 
interpretation 
Total 
Europe 
6 (4) 
8 (3) 
5 (4) 
1 (0) 
20 (11) 
USA 
2 (0) 
10 (8) 
3 (2) 
0 (0) 
15 (10) 
Asia 
0 (0) 
1 (0) 
0 (0) 
0 (0) 
1 (0) 
All firms 
8 (4) 
19 (11) 
8 (6) 
1 (0) 
36 (21) 
 
 

 
41
Figure 1: Time-series of CDS and bond spreads 
Fig. 1a (Fig. 1b) displays times series of daily cross-sectional mean (median) spreads. CDS spreads are indicated 
by a solid line, bond spreads by a dotted line. 
 
 
ratedate
 micds5sen
 mbs5swap
03jan2000
02dec2002
0
50
100
150
200
  
ratedate
 meicds5sen
 mebs5swap
03jan2000
02dec2002
0
50
100
150
200
 
 
Fig. 1a: Mean spreads 
 
 
   Fig. 1b: Median spreads 
 
 

 
42
Figure 2: Sensitivity of ∆CDS and ∆BSS on lagged stock returns vs. rating 
Fig. 2a displays the coefficient for stock return at lag 1 in equation 2 (with ∆CDS as left-hand variable) and Fig. 
2b displays the coefficient for the stock return at lag 1 in equation 3 (with ∆BSS as left-hand variable). Spear-
man’s rank correlation is -0.46*** for Fig. 2a and –0.09 for Fig. 2b. 
 
b17
mrat17
1
2
3
4
5
6
7
8
9
10
11
12
-140
-100
-60
-20
20
1
2
3
4
5
6
7
8
9
10
11
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
47
48
49
50
51
52
53
54
55
56
57
58
 
b33
mrat17
1
2
3
4
5
6
7
8
9
10
11
12
-140
-100
-60
-20
20
1
2
3
4
5
6
7
8
9
10
11
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
47
48
49
50
51
52
53
54
55
56
57
58
Fig. 2a: β2, t-1 vs. rating
Fig. 2b: β3, t-1 vs. rating
 
 

 
43
Figure 3: Error correction coefficients for European and US firms 
Fig. 3a (Fig. 3b) displays the coefficients λ1 and λ2 from a two-equation vector error correction model for Euro-
pean (US) firms for which cointegration of CDS and bond spreads cannot be rejected at the 0.10-level. 
 
l2
l1
-.1
-.05
0
.05
.1
-.1
-.05
0
.05
.1
.15
.2
1
5
7
11
20
25
26
35
36
37
42
43
44
45
46
48
50
55
56
57
l2
l1
-.1
-.05
0
.05
.1
-.1
-.05
0
.05
.1
.15
.2
13
14
15
16
17
27
30
31
32
33
34
39
41
47
52
  
 
         Fig. 3a: European firms 
 
 
  Fig. 3b: US firms 
 
 
 
 
 
