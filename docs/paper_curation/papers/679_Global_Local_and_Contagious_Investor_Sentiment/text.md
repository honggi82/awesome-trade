# Global, Local, and Contagious Investor Sentiment ∗

Malcolm Baker Harvard Business School and NBER mbaker@hbs.edu

Jeﬀrey Wurgler NYU Stern School of Business and NBER jwurgler@stern.nyu.edu

Yu Yuan University of Iowa Tippie College of Business yu-yuan@uiowa.edu

March 18, 2009

Abstract

We construct indexes of investor sentiment for six major stock markets and decompose them into one global and six local indexes. Relative market sentiment is correlated with the relative prices of dual-listed companies, validating the indexes. Both global and local sentiment are contrarian predictors of the time series of major markets’ returns. They are also contrarian predictors of the time series of cross-sectional returns within major markets: When sentiment from either global or local sources is high, future returns are low on various categories of diﬃcult to arbitrage and diﬃcult to value stocks. Sentiment appears to be contagious across markets based on tests involving capital ﬂows, and this presumably contributes to the global component of sentiment.

∗We thank Alexander Ljungqvist, Jay Ritter, and EUROFIDAI for providing data. We thank Rob Engle, Karen Lewis, and seminar participants of the Volatility Institute at NYU Stern for helpful comments. Baker gratefully acknowledges ﬁnancial support from the Division of Research of the Harvard Business School, and Yuan gratefully acknowledges ﬁnancial support from the Weiss Center for International Financial Research.

## 1 Introduction

The global stock market crash of 2007 and 2008 was extraordinary. The MSCI World Index of developed markets fell roughly 50 percent in dollar terms. Emerging markets fell further, with the MSCI Emerging Markets Index falling 66 percent from peak to trough. China’s market index dropped 71 percent in dollar terms, following warnings of a stock market bubble by such authorities as Warren Buﬀett, Alan Greenspan, and even local Chinese regulators.

This paper explores how both global and local investor sentiment aﬀect major stock markets. We also investigate whether and how sentiment spreads across markets. In the context of the most recent crash, our investigation addresses the question of whether the housing and banking crises actually did cause the present value of corporate payouts to fall by half in most countries, and by even more in emerging markets, or instead whether part of these returns may reﬂect shifts in sentiment distinct from economic fundamentals. That is, to the extent that optimism led stocks to be overvalued before the crash, pessimism led them to be undervalued after, or both, large crashes may be explained by somewhat less catastrophic (and perhaps more plausible) declines in global proﬁtability.

We construct quantitative sentiment indexes for six stock markets: Canada, France,

Germany, Japan, the United Kingdom, and the United States. We construct indexes of “total” investor sentiment for each country by forming the ﬁrst principal component of several time series proxies for sentiment. We decompose the six total sentiment indices into a single “global” index and six “local” indices. The data are annual from 1980 to 2005 and drawn from several international sources. Sentiment is intrinsically diﬃcult to measure precisely, so we begin with an index validation test based on duallisted shares, i.e. Siamese twins. These are pairs of securities that have equal cash ﬂow claims but trade in diﬀerent markets and sometimes at substantially diﬀerent prices.

We document that twins’ relative prices are positively related to the relative local sentiment indexes of their respective markets. This is a relatively clean experiment that supports the empirical validity of our indexes. We then ask how sentiment aﬀects stock markets more broadly. The basic supposition is that if sentiment drives prices too far, we may observe corrections in the form of return predictability. We start with regressions to predict market returns. We pool six markets together for power in our short sample. Total sentiment is a contrarian predictor of country-level market returns. The eﬀect of total sentiment derives from approximately equal contributions from global and local components; each contain distinct and statistically signiﬁcant predictive power. These results are similar for both value- and equal-weighted market returns.

Next we consider the eﬀect of sentiment on the time-series of cross-sectional returns. Baker and Wurgler (2006, 2007) predict that broad waves of sentiment will have greater eﬀects on hard to arbitrage and hard to value stocks; these stocks will exhibit high “sentiment beta.” Conﬁrming this, we ﬁnd that when a country’s total sentiment is high, future returns are relatively low for its small, high return volatility, growth, and distressed stocks. This extends prior US evidence to international markets. Furthermore, as with the time series results, this predictability derives both from global and local components of sentiment.

Our ﬁnal investigation considers whether sentiment is contagious across countries. We use the absolute value of US capital ﬂows with the other ﬁve sample countries to obtain cross-sectional variation in the extent of integration between these markets. We ﬁnd that not only do local and global sentiment predict the cross-section of those countries returns, but so does US sentiment in those countries linked with the US by signiﬁcant capital ﬂows. While much more research can be done along these lines, this result suggests that capital ﬂows represent one mechanism by which global sentiment

develops and propagates.

Our study contributes to an emerging literature studying the role of investor sentiment in both corporate ﬁnancing and asset pricing. In addition to the papers mentioned above, Brown and Cliﬀ (2004), Lemmon and Portnaiguina (2006), Qiu and Welch (2004), and other papers have investigated the role of investor sentiment in US stock market returns. Yu and Yuan (2009) argue that sentiment has major eﬀects on the mean-variance relationship in the stock market, with the tradeoﬀ between risk and expected return emerging only in low sentiment periods. Baker and Wurgler (2008) investigate how it aﬀects, and connects, the cross-section of stock returns and government bond returns while Bekart, Baele, and Inghelbrecht (2008) discuss sentiment and the time-series relationships between government bond and stock market returns. Baker and Wurgler (2000) regard sentiment as aﬀecting aggregate ﬁnancing patterns.

Section 2 explains the method of construction of the sentiment indexes. Section 3 reports the results of the validation test. Section 4 uses sentiment to predict the time series of market returns, and Section 5 considers the time series of the cross-section of returns. Section 6 examines sentiment contagion. Section 7 concludes.

## 2 Total, global, and local sentiment indexes

### 2.1 Basic empirical approach

We employ a strategy for measuring international markets sentiment that is similar to Baker and Wurgler’s (2006) strategy for US sentiment. Their general approach takes as given that there is no perfect index of investor sentiment. Instead, there are a number of available, imperfect sentiment proxies that are likely to contain some component of investor sentiment along with a degree of non-sentiment, idiosyncratic

variation. The common sentiment component is then estimated as the ﬁrst principal component of the proxies.

Here, we are constrained by the availability of international sentiment proxies. We use the same set of proxies for all markets although an argument could be made that the principal components methodology should tolerate diﬀerent proxies for diﬀerent markets. One proxy is a quantity that we refer to as the volatility premium and simply identiﬁes times when valuations on high-volatility stocks are high or low relative to valuations on low volatility stocks. This is by analogy to Baker and Wurglers use of the dividend premium, which as the relative valuation of dividend- and non-dividendpaying stocks is highly inversely related to the volatility premium. We can’t form the dividend premium in some markets because dividends are relatively uncommon and, perhaps related, dividends do not appear to be viewed by local investors as connoting “stability” in the way they do among US investors.

The second and third proxies we employ are derived from IPO data. They involve the total volume of IPOs and their initial returns (often called underpricing). Extremely low long-run returns to IPOs have been noted by Stigler (1964), Ritter (1991), and Loughran, Ritter, and Rydkvist (1994), highly suggestive of successful market timing relative to a market index; subsequent work has shown that equity issues forecast low market returns as well. Regarding the use of initial returns on IPOs, it is again often noted that they increase in “hot” markets, for example, average ﬁrst-day returns on US IPOs approached a remarkable 70% at the peak of the Internet bubble.

The fourth proxy we employ is market turnover. Baker and Stein (2004) point out that when shorting is relatively costly, sentimental investors are more likely to trade (and add liquidity) when they are optimistic. Sheinkman and Xiong (2003) provide a complementary argument for using turnover as a proxy for sentiment. So, as with the

other three measures, we expect a positive relationship between the observed proxy and underlying sentiment.

### 2.2 Sentiment proxy data and deﬁnitions

The data sources used to form our sentiment proxies are summarized in Table 1 and summary statistics are given country by country in Table 2. The volatility premium (PV OL) is the year-end log of the ratio of the value-weighted average market-to-book ratio of high volatility stocks to that of low volatility stocks. High (low) volatility denotes one of the top (bottom) three deciles of the variance of the previous year’s monthly returns, where decile breakpoints are determined country by country. This variable was available for the full sample. Its cross-country mean of approximately 0.50 denotes that the market-to-book ratio of high volatility stocks has on average been slightly higher than that of low volatility stocks, but in each country this relationship has occasionally been reversed.

The number of IPOs (NIPO) is the log of the total number of IPOs that year. The initial returns on IPOs (RIPO) represents the average initial (typically, ﬁrstday) return on that year’s oﬀerings. The returns are equal-weighted across ﬁrms. Both variables were available for all countries.1 In US, the annual number of IPOs has ranged from 64 from 953 in the sample period (exponentiating the Min and Max values from Table 2), and the average initial return on IPOs has ranged from around 7% to 53%. Most other countries have also experienced wide variations in these quantities over time.

Market turnover (TURN) is the log of total market turnover, i.e. total dollar volume over the year divided by total capitalization at the end of the prior year. We detrend this with an up-to-ﬁve year moving average. We were able to obtain market-

1In our sample period from 1980 to 2005, French IPO data was not available for 1980 through 1982, and Germany data was not available for 2003 through 2005.

level turnover statistics for all markets except Germany. All markets except Japan display a positive trend in turnover in the sample period.2

### 2.3 Total sentiment indexes

The total sentiment index coeﬃcients for each country are reported in the loadings column of Table 2. The index coeﬃcients are estimated using the ﬁrst principal component of each of the sentiment proxies, all measured contemporaneously. The resulting indexes are linear functions of the within-country standardized values of the proxies and thus have mean zero:

SENT(Total,Canada,t) = 0.37PV OL(t) + 0.16NIPO(t) + 0.44RIPO(t) + 0.39TURN(t)

SENT(Total,France,t) = −0.03PV OL(t) + 0.41NIPO(t) + 0.35RIPO(t) + 0.47TURN(t) SENT(Total,Germany,t) = 0.13PV OL(t) + 0.52NIPO(t) + 0.52RIPO(t)

SENT(Total,Japan,t) = 0.40PV OL(t) + 0.16NIPO(t) + 0.43RIPO(t) + 0.37TURN(t) SENT(Total,UK,t) = 0.39PV OL(t) + 0.23NIPO(t) + 0.33RIPO(t) + 0.35TURN(t) SENT(Total,US,t) = 0.36PV OL(t) + 0.31NIPO(t) + 0.32RIPO(t) + 0.35TURN(t)

where the country subscripts on the proxies have been suppressed. French IPO data was not available for 1980 through 1982, however, so to keep these data points we project the French sentiment values during 1980 through 1982 by the linear combination of the contemporaneous sentiment values of Canada, Japan, UK, and US. Similarly, German data for 2003 through 2005 is ﬁlled.

With only one exception, the sentiment proxies enter positively into the total indexes. The exception is the volatility premium in France, which is not positively correlated with the other proxies (-0.12 with RIPO and -0.17 with TURN). The

2For Canada, France, and US, the data are obtained from the single source. However, for Japan and UK, the data from two diﬀerent sources have to be combined to provide long series from 1980 to 2005. To make the series from diﬀerent sources consistent, we adjust the later series to have the same standard deviations with the early series in the overlapping periods, by multiplying the later series by a constant. Hence, some Japan and UK numbers may not present the actual detrended log turnover, but the whole series consistently exhibit the turnover variations in the two countries.

least-positive coeﬃcient is the volatility premium in Germany’s index, which is the consequence of the unusually high correlation between the IPO-based proxies. The two proxies that are robustly important across all countries are RIPO and TURN.

We standardize the total sentiment indexes deﬁned above and plot them in Figure

- 1. The Internet bubble of the late 1990s, and its subsequent crash, is clearly represented not only in the US but in at least three other countries. These results serve as a reminder that Germany’s Neuer Markt, France’s Nouveau Marche, and London’s TECHMark–only the last of which still exists–were overseas cousins of the more familiar Nasdaq in both composition and performance.3 Another common feature appears to be a dip in the early 1990s.
- 2.4 Global and local sentiment indexes

We separate the total sentiment indexes into one global and six local components. The global index is the ﬁrst principal component of the six total indexes. The loadings are reported in Table 3:

SENT(Global,t) = 0.21SENT(Total,Canada,t) + 0.21SENT(Total,France,t)

+0.25SENT(Total,Germany,t) + 0.22SENT(Total,Japan,t)

+0.27SENT(Total,UK,t) + 0.27SENT(Total,US,t)

The US is widely considered the world’s bellwether market. Consistent with this, the US total sentiment index exhibits a high degree of commonality with other countries’ indexes and so it receives a high loading in the global index (at 0.27, it is tied with the UK).

The standardized version of the global index is plotted in Figure 2. Not surpris-

3Other examples include the Italian Nuovo Mercato, the Nordic New Market, and approximately ten other European markets that opened between 1996 and 2001.

ingly, the ﬁgure indicates that global sentiment rose steadily through the mid-1990s, peaked in 1999 and 2000, and then dropped by a few standard deviations within three years. Before entering the Internet bubble, global sentiment had declined from the late 1980s to the early 1990s.

Local indexes are deﬁned as the components of the total indexes orthogonal to the global index. That is, we regress the total sentiment indexes on the global index in every country respectively and deﬁne local indexes as the residuals. We standardize these and plot them in Figure 2.

Needless to say, qualitative interpretations of any of the indexes involve a considerable degree of conjecture, and this may be most true of the local indexes. Nonetheless a few remarks on the US local index may be useful. The index reaches high levels in the early 1980s, perhaps reﬂecting speculative activity in biotech and natural resources shares that was concentrated in the US. The index declines somewhat following the 1987 crash. Perhaps because the technological advances of the Internet were concentrated in the US, the local index suggests that the sentiment associated with the bubble may have materialized there (and in Canada) ﬁrst. Interestingly, while US total sentiment was high at the Internet’s peak, it was not uniquely high relative to other countries in the sample. However, US-speciﬁc sentiment did decline to an unusual degree with the crash, probably reﬂecting the combination of the crash and the terrorist attacks against the US on September 11, 2001.

## 3 Validation with Siamese twins

### 3.1 The Siamese twins

Dual-listed companies, often termed “Siamese twins,” provide a good laboratory in which to test the validity of our indexes. A twin pair comprises two companies

which are incorporated in diﬀerent countries and whose shares trade locally in those countries but, frequently as a result of a merger, have contractually agreed to operate their business as one and divide its cash ﬂows to shareholders in a ﬁxed ratio. The pair of Royal Dutch and Shell Transport is still the best-known example, despite their recent uniﬁcation.

As documented by Rosenthal and Young (1990), Froot and Dabora (1999), and De Jong, Rosenthal, and Van Dijk (2008), the Siamese twins generally trade at prices that diﬀer from the ﬁxed cash ﬂow ratio, sometimes by considerable amounts. Froot and Dabora provide the most comprehensive examination of why these price gaps occur. They consider six explanations but conclude that none of them is valid.4 One residual explanation that they and others have proposed, but heretofore have been unable to test, is that twins’ relative prices are inﬂuenced by market-speciﬁc sentiment shocks.5

With our putative sentiment measures, we are able to examine this explanation directly. To the extent that it is borne out in the data, it lends support to the joint hypothesis that our sentiment indexes are valid and that the drivers of the Siamese twins’ price gaps include local sentiment.

### 3.2 Data and results

We obtain data on the relative prices of all current or recent Siamese twin pairs from 1981 through 2002 from Mathias Van Dijk at http://mathijsavandijk.com/duallisted-companies. We can use only the subset in which at least one twin trades in a

- 4They consider explanations based on “discretionary uses of dividend income by parent companies; diﬀerences in parent expenditures; voting rights issues; currency ﬂuctuations; ex-dividend-date timing issues; and tax-induced investor heterogeneity. Only that latter hypothesis can explain some (but not all) of the facts.”
- 5De Jong et al. ﬁnd that twins arbitrage strategies appear to present a large amount of noise trader (i.e. sentiment) risk as in De Long, Shleifer, Summers, and Waldmann (1990). But they also are unable to directly test a sentiment explanation directly.

market we study. Three sets of twins have both companies in our sample markets and provide 51 annual observations. These three pairs all involve the US and the UK.6 Six more sets of twins have one company in our sample markets and provide 23 additional observations. Including them allows us to study a twin pair that involves France as well.7

We take annual observations on the year-end log price ratio, appropriately scaled such that a value of 0 represents theoretical parity, and regress the price deviation across the two countries on the year-end diﬀerence between investor sentiment:

- P1,t

- P2,t

- P1,t−1

- P2,t−1

) = a + b(SENT1∗,t − SENT2∗,t) + c log(

log(

) + ut

where SENT∗ alternately means total sentiment or local sentiment. In the sample that includes twins with only one company present in our sample markets, we set SENT2∗ to zero. We control for the lagged relative price level because the dependent variable is empirically quite persistent; because the sentiment indexes are not measured without error; and because both sentiment indexes have been standardized, removing any diﬀerences in means (or scales).

Table 4 shows that the relative level of investor sentiment is signiﬁcantly related to the relative level of twins’ prices. The magnitude of the coeﬃcient is highly statistically signiﬁcant and reasonably important.8 In Panel A, the standard deviation of the log price ratio is 9.3%, while the standard deviation of the total sentiment gap is

- 0.95, so a one-standard deviation change in the latter is associated with a change in

- 6Royal Dutch (US) and Shell Transport (UK) from 1981 through 2002; Smithkline Beecham H shares (US) and Smithkline Beecham E shares (UK) from 1990 through 1996; and Unilever NV (US) and Unilever PLC (UK) from 1981 through 2002.
- 7BHP Billiton PLC (UK and Australia) for 2002; Brambles Industries (UK and Australia) for 2002; Dexia (France and Belgium) for 1997 through 1999; Elsevier (UK) and Reed International (Netherlands) for 1994 through 2002; Rio Tinto Ltd (UK) and Rio Tinto PLC (AU) for 1996 through 2002; and Allied Zurich (UK) and Zurich Allied (Switzerland) for 1999 and 2000.
- 8The Newey-West Standard deviation is used to calculate p value, to adjust the autocorrelations in residuals.

the log price ratio of 1.61 × 0.95 = 1.53% or approximately one-sixth of a standard deviation.

In Table 4, we use both total and local measures of sentiment. Recall that local sentiment is total sentiment less global sentiment times a loading on global sentiment that varies by country. For this reason the diﬀerence between two countries measures of local sentiment is not the same as the diﬀerence between the same countries measures of total sentiment. The gap between these two diﬀerences reﬂects a diﬀerential sensitivity to global sentiment. This extra diﬀerence in total sentiment measures arguably has an impact on the diﬀerential pricing. Indeed, the results are slightly stronger when we focus on total sentiment diﬀerences in Table 4.

This experiment provides some validation of our international sentiment index measures. This complements US-based studies that have previously argued from a variety of perspectives that sentiment is present in the individual proxies that we employ. As an aside, the results here also represent a ﬁnding of signiﬁcant interest in itself with respect to understanding the Siamese twins phenomenon.

## 4 Sentiment and market-level returns

### 4.1 Prior evidence and market-level data

In the Introduction we suggested that investor sentiment may have played a role in the recent global crash. Other speculative episodes often mentioned with at least oblique reference to sentiment include the rise in US share values in the late 1920s, the subsequent crash in 1929, and depressed values through the mid 1930s; the October 1987 crash that Cutler, Poterba, and Summers (1989) cannot connect to signiﬁcant fundamental news; the Internet bubble and crash of the late 1990s and early 2000s for which many have argued the same; the previously noted Chinese market bubble

of the mid-2000s and the global crash in stock markets of 2007 and 2008 (which remains relatively unstudied in this context). Baker and Wurgler (2006) review other anecdotes involving US (total) investor sentiment from the early 1960s through the mid 2000s.

The empirical literature has employed sentiment proxies and indexes as contrarian market-level return predictors only sporadically and mainly in the US context. Kothari and Shanken (1997) discuss the predictability of the aggregate book-tomarket ratio for annual US market returns. The argue for a sentiment-type explanation at least around the Great Crash based on evidence of predictably negative risk premia, strong evidence against market eﬃciency since rational risk premia must be positive. Baker and Wurgler (2000) adopt this approach using the equity share in total equity and debt issues and ﬁnd results consistent with Kothari and Shanken. Tests of based on returns Henderson, Jegadeesh, and Weisbach (2006) extend the predictability evidence to international markets. Baker and Wurgler (2007) ﬁnd some evidence that an index similar to that estimated here predicts market-level US returns, and Brown and Cliﬀ (2004) also consider US market returns but do not ﬁnd evidence of predictability.

Returns for one market obviously have less power to reject the null of no market return predictability than returns for a panel of six countries (Ang and Bekaert (2007) discuss this further), although due to cross-correlation this amounts to fewer than six independent observations per period. In this paper, we collect monthly market return data from Datastream, which cover the stocks from the largest exchange in a country except US.9

9For US, Datastream covers the stocks from NYSE, AMEX, and Nasdaq.

### 4.2 Predictability of market return

We pool monthly returns from 1981-2006 for our countries and regress the monthly returns over the calendar years on beginning-of-year investor sentiment index values:

- RMKT,t = a + dSENTtTotal−1 + ut
- RMKT,t = b + eSENTtGlobal−1 + fSENTtLocal−1 + ut

Due to the cross-correlation in returns our signiﬁcance tests are based on monthclustered standard errors.

Table 5 shows that across these six markets, total investor sentiment serves as a statistically signiﬁcant contrarian predictor of market returns. The economic signiﬁcance of the predictability is rather large. All sentiment indexes are standardized; a one-standard-deviation increase in a country’s total investor sentiment index is associated with value-weighted (equal-weighted) market returns that are lower by 5.0 (6.4) percentage points over the coming year. The marginally stronger eﬀect for equalweighted returns presumably comes about because small stocks tend to be harder to value (due to spottier information) and to arbitrage (due to generally greater costs and risks). This logic is developed a bit further in the next section, which focuses solely on cross-sectional tests. Excluding the US, which is useful because sentiment has been most extensively studied in that market, leaves the results essentially unchanged.

Interestingly, these results are driven independently by global and local sentiment. The point estimates suggest that global sentiment is marginally more important than local sentiment, but not by a statistically signiﬁcant amount. As a ﬁrst approximation we can regard their contributions to market-level predictive regressions as essentially equal. Again, excluding the US leaves these results unchanged. Overall, Table 5

represents new and fairly strong evidence that sentiment aﬀects markets around the world.

## 5 Sentiment and cross-section of returns

### 5.1 Prior evidence and ﬁrm-level data

The dimension of predictability that Baker and Wurgler (2006) focus on and Brown and Cliﬀ (2004) and Lemmon and Portniaguina (2006) also investigate is how the level of US total sentiment aﬀects the cross-section of predicted returns. Brown and Cliﬀ ﬁnd little support for this prediction using their various sentiment measures, while Lemmon and Portniaguina ﬁnd stronger evidence of sentiment as a contrarian predictor of small stocks and low institutional ownership stocks but not value or momentum portfolios. Qui and Welch (2007) also use sentiment to predict small stocks.10

Baker and Wurgler ﬁnd robust predictability of the time series of the cross-section using a US index similar to that used here. Relative to prior work, their sentiment proxies may be more informative and/or the predictions that they test may be sharper. First, they observe that sentiment should have relatively stronger eﬀects on stocks that are “hard to arbitrage”; those that arbitrageurs ﬁnd relatively costly or risky to trade against mispricings. This leads such stocks’ aggregate demand curves to be more downward sloping and thus their prices more sensitive to sentiment-driven demand shifts.11 Second and slightly more novel, they argue that sentiment should

- 10A few of these papers use consumer conﬁdence as a sentiment index, but it is somewhat ambiguous whether its power comes from true sentiment or through some connection to economic fundamentals. Consumer conﬁdence predicts consumer buying, which translates into corporate proﬁtability in a fundamental respect. The indexes constructed here are also quite imperfect but suﬀer less from this particular problem.
- 11For example, liquidity risk as in Acharya and Pedersen (2005); arbitrage risk in Wurgler and Zhuravskaya (2000); transaction costs and asymmetric information as in Amihud and Mendelson (1986); predatory trading risk as in Brunnermeier and Pedersen (2004); noise trader risk as in De

have relatively stronger eﬀects on stocks that are ”hard (highly subjective) to value.” Both extremely high or low valuations on such stocks can be plausibly defended by sentimental investors, as beﬁts their current sentiment.

The basic empirical prediction of all this is that sentiment may serve as a contrarian predictor of “high sentiment beta” portfolios. Conveniently, several key stock portfolios are classiﬁable as either relatively easy to arbitrage and easy to value or as relatively hard to arbitrage and hard to value, making this prediction straightforward to test.12 Examples of stock portfolios with high sentiment beta characteristics are small, high volatility, non-dividend paying, unproﬁtable, distressed, or extreme growth portfolios; their complement portfolios are lower, even perhaps negative sentiment beta.

One empirical subtlety involves how to capture growth and distress characteristics using value or sales growth portfolios. Baker and Wurgler predict and ﬁnd evidence that the eﬀects of sentiment on these portfolios are roughly U-shaped. Very high book-to-market or very low (negative) sales growth can be associated with distress; very low book-to-market can be associated with extreme growth, as is very high sales growth. In other words, when sorting stocks along value or sales growth dimensions, high sentiment beta stocks commonly reside in the extreme high and low deciles where staid, low sentiment beta stocks are typically found in the middle. We account for this U-shape in our tests involving these portfolios.13

Our cross-sectional portfolios are formed based on four ﬁrm or stock characteristics that are easy to gather for our markets: ﬁrm size, total risk, book-to-market ratio, and sales growth. Returns and market capitalization are obtained from Datastream.

Long et al. (1990); and short-selling costs as in D’Avolio (2002), Duﬃe, Garleanu, and Pedersen

(2002), Geczy, Musto, and Reed (2002), and Ofek and Richardson (2002);

- 12Notably, momentum doesn’t fall clearly in either set, likely explaining why sentiment has not

been a successful predictor of such portfolios.

- 13Not accounting for this nonmonotonicity in sentiment beta explains why some prior research

found no clear connection between sentiment and value portfolios.

Book values and annual sales are downloaded from Worldscope. Total risk is the volatility of monthly total returns over the prior year. Decile breakpoints vary by country-year.

### 5.2 Predicting the time series of the cross-section

Simple two-way sorts are presented in Tables 6 and 7. We sort stocks across years according to whether the level of their total sentiment index is positive or negative. The basic predictions are borne out. High sentiment periods are associated with

- 1.59 percentage point lower monthly returns on top-decile volatility stocks than low sentiment periods. Cumulated across twelve months, this is a quite large eﬀect. High sentiment periods also portend 1.16 lower returns on the bottom capitalization decile portfolio, also a large eﬀect. As expected, the eﬀect of sentiment is much smaller on low volatility stocks or large stocks.

As mentioned above, we predict a somewhat U-shaped eﬀect of sentiment on bookto-market and sales growth portfolios. This is borne out reasonably well in both types of portfolios, but more strongly in the sales growth portfolios. There, high sentiment periods forecast 95 basis points lower monthly returns on bottom-decile sales growth portfolios and 1.06 percentage points lower returns on top-decile portfolios. This contrasts with high sentiment forecasting only 55 to 62 basis points lower monthly returns on middle-decile sales growth portfolios, expected to contain lower sentiment beta stocks in this particular sort. Cumulated over the year, the diﬀerences between the extreme and middle deciles are of meaningful magnitude, though not as strong

- as the volatility and capitalization results. Table 7 repeats these sorts for the ﬁve markets excluding the US market. The

results indicate eﬀects of very similar economic signiﬁcance. Next we move to time series regressions to predict long-short portfolios. This

provides a simpler setting in which to conduct hypothesis tests and also allows us to look at the separate eﬀects of global and local sentiment. The basic regression models are:

it=short,t = a + dSENTtTotal−1 + ut RX

it=long,t − RX

RX

it=short,t = b + eSENTtGlobal−1 + fSENTtLocal−1 + ut

it=long,t − RX

Again the signiﬁcance tests incorporate month-clustered standard errors.

The results for the total sentiment column in Table 8 are consistent with those from the sorts. In ﬁve out of six hypothesis tests, the eﬀect of total sentiment is statistically signiﬁcant and the remaining long-short portfolio, which sorts on distress by using high value against medium value, is of the expected sign and signiﬁcant

- at the 20% level (10% in a one-sided test, which is arguably more appropriate). Some calculation will conﬁrm that the economic signiﬁcance of the eﬀects implied by these estimates is similar to that from the sorts in prior tables, with the eﬀects for the volatility portfolios again being particularly large. This is consistent with the intuition that sorting on volatility leads to particularly clear contrasts on both arbitrage risk and valuation ambiguity dimensions.

We also test for the eﬀects of global versus local sentiment in Table 8. For size and volatility portfolios, the results show that both types of sentiment aﬀect the crosssection of returns. The economic eﬀects for the volatility portfolios are, once again, particularly large. In every case the predictability is of the hypothesized expected sign. Similar to our time-series results, there is no consistent pattern in whether global or local sentiment is more economically or statistically signiﬁcant for cross-sectional portfolios. Global sentiment is statistically signiﬁcant at the 10% level in two of six portfolios in two-sided tests, and ﬁve out of six in one-sided tests. Local sentiment is

signiﬁcant at the 10% level in four out of six in two-sided tests and ﬁve out of six in one-sided tests.

We conclude from this evidence that total sentiment plays a nontrivial role in determining cross-sectional return characteristics in major international markets. This extends prior evidence from the US market. Furthermore, and more interesting, both global and local components of investor sentiment play a role in the cross-section of returns.

## 6 Sentiment contagion

Our results suggest that both global and local sentiment aﬀect stock prices. When global and local sentiment are high, future local stock returns are low, and particularly so for small and volatile stocks, and those that are at both ends of the spectrum of growth and distress. The local sentiment eﬀects extend the evidence from the US on sentiment and the cross section of stock returns. The eﬀect of global sentiment suggests a more novel mechanism. In particular, sentiment from one country may be contagious.

There are two sources of contagion. One possibility is that investors in one country are optimistic about investment prospects in another, bidding up the shares of that particular country. This sort of sentiment, using our measures, will be captured by local sentiment. Local sentiment rises with the local volatility premium, the local number of IPOs, the local ﬁrst day return on IPOs, and the local rate of share turnover. These are local measures, but they reﬂect capital market activity, which in principle can come from foreign as well as local investors. The evidence in Klibanov, Lamont, and Wizman (1998) and Hwang (2009), who examine the pricing of closedend funds, are suggestive of this channel.

Another possibility is that investors in one country - say the US - are simply opti-

mistic and this leads to a shift into risky assets more broadly, including international equities. US sentiment will then aﬀect prices in another target country, above and beyond local sentiment, provided that our measure of local sentiment is not absolutely complete, as it surely is not, and provided that there is a robust ﬂow of private capital from the US into the target. We test this hypothesis in Table 9. We regress future returns of size, volatility, growth, and distress portfolios in the ﬁve countries excluding US on lagged sentiment in the local country as before. But, we now include US sentiment, and importantly US sentiment interacted with capital ﬂows from the US to each of the ﬁve other countries.

it=low,t = a + bSENTtTotal−1 + cSENTtTotal,US−1 + d|Flowt−1|

it=high,t − RX

RX

+eSENTtTotal,US−1 × |Flowt−1| + ut

The data on capital ﬂows come from US Treasury Bulletin and are normalized by the market value of the foreign stock market. In every case where the eﬀect of sentiment of the local country is statistically signiﬁcant, there is also a strong and conditional eﬀect of US sentiment. Provided the capital ﬂows between the US and Canada, to take an example, are high, then US sentiment has the same eﬀect on hard-to-value and diﬃcult-to-arbitrage Canadian stocks as Canadian sentiment. This suggests that sentiment is contagious. When US investors have high sentiment, this spreads to other countries through private capital ﬂows.

## 7 Conclusion and implications

This paper makes four main contributions. The ﬁrst is to construct practical indexes of investor sentiment for six major stock markets and global markets as a whole. We construct sentiment indexes for Canada, France, Germany, Japan, the United

Kingdom, and the United States, and from these total sentiment indexes we extract one global and six local, or country-speciﬁc, indexes. Importantly, we validate these indexes, to the extent we are able to do so, by successfully relating them to Siamese twins share prices.

The second and third contributions of the paper are to test whether investor sentiment aﬀects the time series of international market-level returns as well as the time series of the cross-section of international stock returns. We ﬁnd that sentimentboth global and localis a statistically and economically signiﬁcant contrarian predictor of market returns as well as the relative returns on high-sentiment-beta stocks. The high-sentiment-beta portfolios that we consider are small, high volatility, distressed, and growth portfolios. In a sense, all of these results are consistent with theoretical predictions, so they further validate the indexes.

Our fourth contribution is to investigate of how global sentiment emerges and propagates. We ﬁnd evidence that it emerges at least in part because sentiment is contagious across markets, and at least one of the mechanisms at play is international capital ﬂows. Ours is a simple investigation of the contagion question; we believe there is considerable scope for further research.

We return to the events introduced at the beginning of this paper: the recent, devastating global stock market crash. Although this occurred too recently to be included in our sample, our results may contain at least slightly optimistic messages. As sentiment has played a signiﬁcant role in past bubbles and crashes, there is reason to harbor hope that expected global cash ﬂows have not declined by one half, but rather markets have overshot the decline justiﬁed by a rational look at fundamentals. Alternatively, current valuation levels may be justiﬁed but prior levels may have been inﬂated by sentiment. This interpretation is less consoling in terms of the outlook for future returns.

#### In any event, this event has stimulated an important discussion in economic policy circles, including at the Federal Reserve, about whether bubbles should be ex ante identiﬁed and managed. Measuring and understanding the dynamics of investor sentiment is the ﬁrst step in answering these policy questions.

## References

Aghion, Philippe, and Jeremy Stein, 2004, Growth Versus Margins: The Destabilizing Consequences of Giving the Stock Market What It Wants, Working paper, Harvard Business School.

Amihud, Yakov, and Haim Mendelson, 1986, Asset Pricing and the Bid-Ask Spread, Journal of Financial Economics, 17, 223-249.

Ang, Andrew, and Geert Bekaert, 2007, Stock Return Predictability: Is It There? Review of Financial Studies, 20, 651-707.

Bekaert, Geert, Lieven Baele, and Koen Inghelbrecht, 2008, The Determinants of Stock and Bond Return Comovements, Working Paper, Columbia University.

Bekaert, Geert, Campbell R. Harvey, Christian T. Lundblad, and Stephan Siegel, 2008, What Segments Equity Markets? Working paper, Columbia University.

Baker, Malcolm, and Jeremy Stein, 2004, Market Liquidity as A Sentiment Indicator, Journal of Financial Markets 7, 271-299.

Baker, Malcolm, and Jeﬀrey Wurgler, 2000, The Equity Share in New Issues and Aggregate Stock Returns, Journal of Finance, 55, 2219-2257.

- Baker, Malcolm, and Jeﬀrey Wurgler, 2006, Investor Sentiment and the Cross-Section of Stock Returns, Journal of Finance, 61, 1645-1680.
- Baker, Malcolm, and Jeﬀrey Wurgler, 2007, Investor Sentiment in the Stock Market, Journal of

- Economic Perspectives, 21, 129-151.
- Baker, Malcolm, and Jeﬀrey Wurgler, 2008, Government Bonds and the Cross-Section of Stock Returns, Working paper,Harvard Business School.

Brown, Gregory W., and Michael T. Cliﬀ, 2004, Investor Sentiment and the Near-Term Stock Market, Journal of Empirical Finance, 11, 1-27.

Brunnermeier, Markus, and Lasse Pedersen, 2005, Predatory Trading, Journal of Finance, 60, 18251863.

Cutler, David M., James M. Poterba, and Lawrence H. Summers, 1989, What Moves Stock Prices? Journal of Portfolio Management, 15, 4-12.

DAvolio, Gene, 2002, The Market for Borrowing Stock, Journal of Financial Economics, 66, 271-306.

De Jong, Abe, Leonard Rosenthal, and Mathijs A. Van Dijk, 2008, The Risk and Return of Arbitrage in Dual-Listed Companies, Review of Finance, forthcoming.

De Long, Bradford J., Andrei Shleifer, Lawrence H. Summers, and Robert Waldmann, 1990, Noise Trader Risk in Financial Markets, Journal of Political Economics, 98, 703-738.

Duﬃe, Darrell, Nicolae Garleanu, and Lasse H. Pedersen, 2002, Securities Lending, Shorting, and Pricing, Journal of Financial Economics, 66, 307-339.

Edmans, Alex, Diego Garcia, and Oyvind Norli, 2007, Sports Sentiment and Stock Returns, Journal

of Finance, 62, 1967-1998.

Forbes, Kristin J. and Roberto Rigobon, 2002, No Contagion, Only Interdependence: Measuring Stock Market Comovements, Journal of Finance, 43, 2223-2261.

Froot, Kenneth A. and Emile M. Dabora, 1999, How Are Stock Prices Aﬀected by the Location of Trade? Journal of Financial Economics, 53, 189-216.

Geczy, Christopher C., David K. Musto, and Adam V. Reed, 2002, Stock Are Special Too: An Analysis of the Equity Leading Market, Journal of Financial Economics 66, 241-269.

Henderson, Brian J., Narasimhan Jegadeesh, and Michael S. Weisbach, 2006, World Markets for Raising New Capital, Journal of Financial Economics, 82, 63-101.

Hwang, Byoung-Hyoun, 2009, Country-Speciﬁc Sentiment and Security Prices paper, Working paper, Emory University.

Klibanoﬀ, Peter, Owen Lamont, and Thierry Wizman, 1998, Investor Reaction to Salient News in Country Closed-End Funds, Journal of Finance, 53, 673-699.

Kothari, S.P., Jay A. Shanken, 1997, Book-to-market, Dividend Yield, and Expected Market Returns: A Time-series Analysis, Journal of Financial Economics, 44, 169-203.

Lemmon, Mike and Evgenia Portnaiguina, Consumer Conﬁdence and Asset Prices: Some Empirical Evidence, 2006, Review of Financial Studies, 19, 1499-1529.

Loughran, Tim, Jay R. Ritter, and Kristian Rydqvist, 1994, Initial Public Oﬀerings: International Insights, Paciﬁc-Basin Finance Journal, 2, 165-199.

Ofek, Eli and Matthew Richardson, 2002, DotCom Mania: The Rise and Fall of Internet Stocks, Journal of Finance, 58, 1113-1138.

Ritter, Jay, 1991, The Long-Run Performance of Initial Public Oﬀerings, Journal of Finance 46, 3-27.

Rosenthal, Leonard and Colin Young, 1990, The Seemingly Anomalous Price Behavior of Royal Dutch/Shell and Unilever N.V./PLC, Journal of Financial Economics, 26, 123-141.

Scheinkman, Jose, and Wei Xiong, 2003, Overconﬁdence and speculative bubbles, Journal of Political Economy 111, 1183-1219.

Stigler, George J., 1964, Public Regulation of the Securities Markets, Journal of Business 37, 117142.

Qiu, Lily, and Ivo Welch, 2004, Investor Sentiment Measures, Working paper, Brown University.

Wurgler, Jeﬀrey, and Katia Zhuravskaya, 2002, Does Arbitrage Flatten Demand Curves for Stocks? Journal of Business, 75, 583-608.

Yu, Jianfeng, and Yu Yuan, 2009, Investor Sentiment and the Mean-Variance Relation, Working paper, University of Iowa.

- Table1:DataResources

NIPO1984-1991FromJogandSrivastavathroughtheupdatedversionofLoughran,etal.(1994)

RIPO1984-1991FromJogandSrivastavathroughtheupdatedversionofLoughran,etal.(1994)

CanadaNIPO1980-1983FromJogandRidingthroughtheupdatedversionofLoughran,etal.(1994)

CanadaRIPO1980-1983FromJogandRidingthroughtheupdatedversionofLoughran,etal.(1994)

RIPO1999-2005FromDealogicthroughtheupdatedversionofLoughran,etal.(1994)

AllcountriesStockreturn1980-2005Datastream(http://www.datastream.com/default.htm)

1980-2005Worldscope(http://www.thomsonreuters.com/)Bookvalue

Japan,UK,andUSNIPO1980-2005TheupdatedversionofLoughran,etal.(1994)

NIPO1992-2005TheupdatedversionofLoughran,etal.(1994)

1983-2005TheupdatedversionofLoughran,etal.(1994)FranceNIPO

Japan,UK,andUSRIPO1980-2005TheupdatedversionofLoughran,etal.(1994)

RIPO1992-2005TheupdatedversionofLoughran,etal.(1994)

FranceRIPO1983-1998TheupdatedversionofLoughran,etal.(1994)

(http://bear.cba.uﬂ.edu/ritter/Int2008.pdf)

PanelC.IPOFirst-dayReturns(RIPO)

PanelA.VolatilityPremium(PVOL)

PanelB.IPOVolume(NIPO)

GermanyNIPO1980-2002FromLjungqvist

GermanyRIPO1980-2002FromLjungqvist

CountryItemPeriodDataSource

Marketvalue1980-2005Datastream

- Table1:DataResources,Continued

CountryItemPeriodDataSource

1980-1989GlobalFinancialData(https://www.globalﬁnancialdata.com/)JapanDollarvolume

FranceDollarvolume1980-2005EUROFIDAI(http://www.euroﬁdai.org/)

PanelD.Turnover(TURN)

1980-2005EUROFIDAIFranceMarketvalue

Canada,UK,andUSDollarvolume1980-2005Datastream

Dollarvolume1990-2005Datastream

Canada,Japan,UK,andUSMarketvalue1980-2005Datastream

(NIPO)isthelogannualnumberofinitialpublicoﬀerings.Thethirdmeasure(RIPO)istheaverageannualﬁrst-day

Dataresourcesforrawmeasuresofinvestorsentimentfrom1980to2005.Theﬁrstmeasure(PVOL)istheyear-endlog

ratioofthevalue-weightedaveragemarket-to-bookratiosofhighvolatilestocksandlowvolatilestocks.Thesecondmeasure

returnsofinitialpublicoﬀerings.Thefourthmeasure(TURN)isdetrendedlogturnover.

#### Table2:TotalSentiment,1980to2005

0.210.30-0.351.030.77(0.00)0.390.280.290.541.00(0.17)(0.15)(0.00)(.)TURN

-0.051.97-5.882.650.74(0.00)0.370.300.270.481.00(0.14)(0.19)(0.01)(.)TURN

0.160.30-0.590.620.92(0.00)0.47-0.170.670.501.00(0.43)(0.00)(0.02)(.)TURN

MeanSDMinMaxPValueTotalSENTPVOLNIPORIPOTURNPVOLNIPORIPOTURN

0.070.06-0.040.240.86(0.00)0.440.560.041.00(0.00)(0.86)(.)RIPO

0.110.070.020.260.69(0.00)0.35-0.120.261.00(0.58)(0.23)(.)RIPO

0.120.12-0.000.430.92(0.00)0.520.080.751.00(0.71)(0.00)(.)RIPO

0.310.220.070.860.85(0.00)0.430.610.021.00(0.00)(0.93)(.)RIPO

CorrelationsLoadingsCorrelationswithPValues

2.700.831.614.260.31(0.12)0.160.061.00(0.76)(.)NIPO

3.390.731.614.690.80(0.00)0.410.231.00(0.29)(.)NIPO

3.020.851.795.120.93(0.00)0.520.111.00(0.60)(.)NIPO

4.340.732.645.140.32(0.11)0.160.141.00(0.50)(.)NIPO

0.110.55-1.031.49-0.06(0.79)-0.031.00(.)PVOL

0.720.43-0.011.600.74(0.00)0.371.00(.)PVOL

0.520.61-1.041.620.24(0.28)0.131.00(.)PVOL

0.540.63-0.362.040.79(0.00)0.401.00(.)PVOL

withSentimentComponentsTotalSENT

PanelC.Germany

PanelA.Canada

PanelB.France

PanelD.Japan

#### Table2:TotalSentiment,Continued

0.881.17-0.813.630.80(0.00)0.350.600.370.371.00(0.00)(0.06)(0.06)(.)TURN

0.220.26-0.280.680.78(0.00)0.350.400.520.401.00(0.04)(0.01)(0.04)(.)TURN

MeanSDMinMaxPValueTotalSENTPVOLNIPORIPOTURNPVOLNIPORIPOTURN

0.160.120.060.610.75(0.00)0.330.640.151.00(0.00)(0.45)(.)RIPO

0.170.110.070.530.70(0.00)0.320.550.141.00(0.00)(0.48)(.)RIPO

CorrelationsLoadingsCorrelationswithPValues

4.410.692.565.430.53(0.01)0.230.281.00(0.16)(.)NIPO

5.830.754.166.860.68(0.00)0.310.411.00(0.04)(.)NIPO

0.280.47-0.531.550.88(0.00)0.391.00(.)PVOL

0.390.48-1.041.810.80(0.00)0.361.00(.)PVOL

withSentimentComponentsTotalSENT

PanelE.UK

PanelF.US

#### Means,standarddeviations,andcorrelationsformeasuresofinvestorsentiment.Theﬁrstmeasure(PVOL)istheyear-end

#### Totaldayreturnsofinitialpublicoﬀerings.Thefourthmeasure(TURN)isdetrendedlogturnover.SENT,totalsentiment,

#### measure(NIPO)isthelogannualnumberofinitialpublicoﬀerings.Thethirdmeasure(RIPO)istheaverageannualﬁrst-

#### logratioofthevalue-weightedaveragemarket-to-bookratiosofhighvolatilestocksandlowvolatilestocks.Thesecond

#### istheﬁrstprincipalcomponentofthefourmeasureswithinonecountry.

- Table3:GlobalandLocalSentiment,1980to2005

US0.82(0.00)0.270.620.440.730.220.341.00(0.00)(0.03)(0.00)(0.27)(0.08)(.)

CanadaFranceGermanyJapanUKUSCanadaFranceGermanyJapanUKUS

US0.33-0.140.25-0.55-0.781.00(0.10)(0.51)(0.21)(0.00)(0.00)(.)

PValueCanadaFranceGermanyJapanUKUSCanadaFranceGermanyJapanUKUSGlobalSENT

UK0.77(0.00)0.270.230.390.480.711.00(0.26)(0.05)(0.01)(0.00)(.)

UK-0.38-0.16-0.300.501.00(0.05)(0.44)(0.13)(0.01)(.)

Japan0.59(0.00)0.220.100.290.151.00(0.64)(0.15)(0.48)(.)

Japan-0.35-0.11-0.621.00(0.08)(0.61)(0.00)(.)

CorrelationswithLoadingsCorrelationsAmongSixTotalSentimentsPValues

CorrelationsAmongSixLocalSentimentsPValues

Germany-0.13-0.081.00(0.53)(0.71)(.)

Germany0.78(0.00)0.250.370.441.00(0.06)(0.02)(.)

France-0.481.00(0.01)(.)

France0.61(0.00)0.210.031.00(0.90)(.)

Canada0.56(0.00)0.211.00(.)

Canada1.00(.)

PanelA:TotalandGlobalSentiment

PanelB:LocalSentiment

GlobalSentiment

GlobalTotalGlobalsentiment(SENT)istheﬁrstprincipalcomponentofthesixtotalsentimentindexes(SENT)inCanada,

LocalFrance,Germany,Japan,UK,andUS.Localsentiment(SENT)istheorthogonalresidualfromtheregression,

TotalGlobalLocalSENT=bSENT+SENT,withinacountry.i

Table 4: Time Series Regressions for Siamese Twins

N(Obs) Constant SENT1∗,t − SENT2∗,t log(PP1,t−1

) R2 ×102

2,t−1

Panel A. Both twins in sample countries Total Sentiment 51 0.01 1.61 0.77 72%

[.05] [.03] [.00] Local Sentiment 51 0.01 0.93 0.77 70%

[.05] [.05] [.00] Panel B. At least one twin in sample countries Total Sentiment 74 0.01 1.27 0.64 50%

[.29] [.09] [.00] Local Sentiment 74 0.01 0.65 0.63 49% [.15] [.12] [.00]

- P1,t

- P2,t

- P1,t−1

- P2,t−1

) = a + b(SENT1∗,t − SENT2∗,t) + c log(

log(

) + ut

The dependent variable is the annual log deviation of the relative price of Siamese twins. The independent variables are the diﬀerence between total sentiment or local sentiment and the lagged log deviation. Panel A reports the results from the sample containing three twins, for which we have sentiment values for both countries. The sample in Panel B includes additional six twins, for which we only have sentiment values for one side. We assume the sentiment values on the other side as zeros. The Newey-West p values are in braces.

Table 5: Time Series Regressions for Country-Level Index Returns, 1981 to 2006

SENTtTotal−1 SENTtGlobal−1 SENTtLocal−1 d p(d) R2 e p(e) f p(f) R2

- Panel A. Including US

VW -0.43 [.01] 0.7% -0.43 [.05] -0.27 [.06] 0.9% EW -0.55 [.00] 1.0% -0.51 [.02] -0.40 [.02] 1.4%

- Panel B. Excluding US

VW -0.45 [.01] 0.7% -0.42 [.07] -0.26 [.03] 1.0% EW -0.55 [.00] 1.0% -0.50 [.04] -0.43 [.01] 1.2%

- RMKT,t = a + dSENTtTotal−1 + ut (1)
- RMKT,t = b + eSENTtGlobal−1 + fSENTtLocal−1 + ut (2)

Regressions of country-level value- and equal-weighted index returns on lagged SENTTotal (in equation (1)), or on lagged SENTGlobal and lagged SENTLocal (in equation (2)). In Panel A, the sample includes monthly country-level index returns from 1981 to 2006 in the six countries: Canada, France, Germany, Japan, UK, and US. In Panel B, the sample excludes US data. The ﬁrst column shows the results from equation (1), and the second column shows the results from equation (2). Clustered p values are in braces.

#### Table6:Two-waySorts:TotalSentimentandFirmCharacteristics,1981to2006

|10110551|-0.17-0.480.31<br><br>1.030.480.55<br><br>-1.20-0.96-0.24<br><br>-1.020.04-1.06<br><br>-1.49-0.16-1.33<br><br><br>0.480.210.27<br><br>0.500.440.06<br><br>0.290.74-0.45<br><br>0.22-0.290.51<br><br>0.34-0.050.40<br><br>0.440.360.09<br><br>-0.10-0.410.31|
|---|---|
|12345678910|High0.670.900.890.970.981.040.930.810.650.50σ<br><br>Low1.061.221.401.541.611.701.721.771.902.09<br><br>Diﬀerence-0.40-0.32-0.50-0.58-0.63-0.66-0.79-0.96-1.24-1.59<br><br>MEHigh1.751.200.870.770.680.710.680.710.730.73<br><br>Low2.912.191.831.581.581.431.371.351.331.42<br><br>Diﬀerence-1.16-0.99-0.97-0.80-0.90-0.72-0.69-0.64-0.60-0.69<br><br>BE/MEHigh0.850.830.790.840.910.920.900.931.111.36<br><br>Low1.941.581.511.581.491.631.691.731.762.23<br><br>Diﬀerence-1.09-0.75-0.72-0.74-0.58-0.71-0.79-0.81-0.65-0.88<br><br>GSHigh0.630.750.891.061.021.141.151.201.130.97<br><br>Low1.581.541.551.511.671.661.801.691.832.03<br><br>Diﬀerence-0.95-0.79-0.66-0.44-0.65-0.52-0.65-0.49-0.70-1.06|

- 0.970.981.040.930.810.650.50-0.17-0.480.31
- 1.541.611.701.721.771.902.091.030.480.55

-0.80-0.90-0.72-0.69-0.64-0.60-0.690.480.210.27

- 0.840.910.920.900.931.111.360.500.440.06
- 1.581.491.631.691.731.762.230.290.74-0.45

1.511.671.661.801.691.832.030.440.360.09

- 0.770.680.710.680.710.730.73-1.020.04-1.06
- 1.581.581.431.371.351.331.42-1.49-0.16-1.33

-0.44-0.65-0.52-0.65-0.49-0.70-1.06-0.10-0.410.31

-0.74-0.58-0.71-0.79-0.81-0.65-0.880.22-0.290.51

1.061.021.141.151.201.130.970.34-0.050.40

-0.58-0.63-0.66-0.79-0.96-1.24-1.59-1.20-0.96-0.24

4567891010110551−−−

DecileOverallTotalSENT−t1

#### Totalandsalesgrowth(GS).Wereportequal-weightedportfolioreturnsovermonthswheretotalsentiment(SENT)from

#### Foreachmonth,weformtenportfoliosaccordingtothetotalrisk(σ),ﬁrmsize(ME),book-to-marketratio(BE/ME),

#### thetwoaverages.Thesampleincludesmonthlyreturnsfrom1981to2006inthesixcountries:Canada,France,Germany,

#### thepreviousyearendishigherthanwithin-countrymedian,lowerthanwithin-countrymedian,andthediﬀerencebetween

#### Japan,UK,andUS.

#### Table7:Two-waySorts:TotalSentimentandFirmCharacteristics,ExcludingUS,1981to2006

|10110551|-0.19-0.600.41<br><br>1.040.420.62<br><br>-1.23-1.02-0.21<br><br>-0.840.06-0.90<br><br>-1.40-0.14-1.26<br><br><br>0.560.200.36<br><br>0.360.360.00<br><br>0.140.65-0.51<br><br>0.22-0.290.51<br><br>0.520.050.47<br><br>0.550.430.12<br><br>-0.04-0.380.35|
|---|---|
|12345678910|High0.510.780.790.860.910.980.820.710.540.32σ<br><br>Low1.001.181.391.541.621.711.741.791.872.04<br><br>Diﬀerence-0.49-0.39-0.60-0.68-0.71-0.73-0.92-1.08-1.33-1.72<br><br>MEHigh1.501.150.760.730.600.630.580.630.660.66<br><br>Low2.852.101.831.561.591.451.391.361.331.45<br><br>Diﬀerence-1.35-0.95-1.07-0.83-0.99-0.82-0.81-0.73-0.67-0.80<br><br>BE/MEHigh0.840.810.730.780.840.820.780.810.971.20<br><br>Low2.021.611.531.591.511.641.701.721.722.17<br><br>Diﬀerence-1.18-0.80-0.80-0.81-0.67-0.81-0.91-0.92-0.75-0.96<br><br>GSHigh0.470.590.790.990.941.061.061.131.120.99<br><br>Low1.561.501.511.481.681.661.841.701.872.11<br><br>Diﬀerence-1.09-0.91-0.72-0.50-0.74-0.60-0.78-0.57-0.75-1.12|

- 0.860.910.980.820.710.540.32-0.19-0.600.41
- 1.541.621.711.741.791.872.041.040.420.62

-0.83-0.99-0.82-0.81-0.73-0.67-0.800.560.200.36

- 0.780.840.820.780.810.971.200.360.360.00
- 1.591.511.641.701.721.722.170.140.65-0.51

- 0.990.941.061.061.131.120.990.520.050.47
- 1.481.681.661.841.701.872.110.550.430.12

- 0.730.600.630.580.630.660.66-0.840.06-0.90
- 1.561.591.451.391.361.331.45-1.40-0.14-1.26

-0.50-0.74-0.60-0.78-0.57-0.75-1.12-0.04-0.380.35

-0.81-0.67-0.81-0.91-0.92-0.75-0.960.22-0.290.51

-0.68-0.71-0.73-0.92-1.08-1.33-1.72-1.23-1.02-0.21

4567891010110551−−−

DecileOverallTotalSENT−t1

#### Totalsalesgrowth(GS).Wereportequal-weightedportfolioreturnsovermonthswheretotalsentiment(SENT)fromthe

#### Foreachmonth,weformtenportfoliosaccordingtothetotalrisk(σ),ﬁrmsize(ME),book-to-marketratio(BE/ME),and

#### twoaverages.Thesampleincludesmonthlyreturnsfrom1981to2006intheﬁvecountries:Canada,France,Germany,

#### previousyearendishigherthanwithin-countrymedian,lowerthanwithin-countrymedian,andthediﬀerencebetweenthe

#### Japan,andUK.

Table 8: Time Series Regressions for Cross-Sectional Returns, 1981 to 2006

SENTtTotal−1 SENTtGlobal−1 SENTtLocal−1 d p(d) R2 e p(e) f p(f) R2

Panel A. Size and Risk ME SMB -0.40 [.00] 0.7% -0.21 [.06] -0.34 [.00] 0.7% σ High-Low -0.79 [.00] 2.0% -0.76 [.00] -0.40 [.01] 2.4% Panel B. Growth Opportunities BE/ME Medium-Low 0.25 [.01] 0.5% 0.18 [.19] 0.15 [.08] 0.5% GS High-Medium -0.28 [.02] 0.8% -0.22 [.17] -0.14 [.12] 0.7% Panel C. Distress BE/ME High-Medium -0.14 [.19] 0.3% -0.14 [.29] -0.08 [.41] 0.4% GS Medium-Low 0.27 [.00] 1.0% 0.12 [.20] 0.20 [.01] 0.7%

it=short,t = a + dSENTtTotal−1 + ut (1) RX

it=long,t − RX

RX

it=short,t = b + eSENTtGlobal−1 + fSENTtLocal−1 + ut (2)

it=long,t − RX

Regressions of long-short equal-weighted portfolio returns on lagged SENTTotal (in equation (1)), or on lagged SENTGlobal and lagged SENTLocal (in equation (2)). The ﬁrst column shows the results from equation (1), and the second column shows the results from equation (2). The sample includes monthly returns from 1981 to 2006 in the six countries: Canada, France, Germany, Japan, UK, and US. The long-short portfolios are formed based on ﬁrm characteristics (X): ﬁrm size (ME), total risk (σ), book-to-market ratio (BE/ME), and sale growth (GS). High includes the top two deciles; low includes the bottom two deciles; medium includes the middle two deciles. Equal-weighted monthly returns are matched to SENTTotal, SENTGlobal, or SENTLocal from previous end. Clustered p values are in braces.

Table 9: Time Series Regressions for Sentiment Contagion, 1981 to 2006

Constant SENTtTotal−1 SENTtUS−1 |Flowt−1| SENTtUS−1× R2

|Flowt−1| Panel A. Size and Risk ME SMB 0.32 -0.30 0.23 0.49 -0.37 1.8%

[.20] [.02] [.34] [.00] [.02] σ High-Low -0.19 -0.51 -0.15 0.34 -0.31 3.8%

[.52] [.00] [.67] [.01] [.03] Panel B. Growth Opportunity BE/ME Medium-Low -0.19 0.18 -0.34 0.02 0.21 0.6%

[.41] [.09] [.14] [.85] [.09] GS High-Medium 0.43 -0.13 -0.20 -0.14 -0.19 1.0% [.05] [.08] [.34] [.10] [.03]

Panel C. Distress BE/ME High-Medium 0.05 -0.08 -0.29 0.20 0.08 1.0%

[.77] [.41] [.13] [.02] [.35] GS Medium-Low 0.17 0.23 -0.25 0.06 0.16 1.4% [.15] [.00] [.05] [.42] [.01]

it=short,t = a + bSENTtTotal−1 + cSENTtUS−1 + d|Flowt−1| +eSENTtUS−1 × |Flowt−1| + ut

it=long,t − RX

RX

The dependent variable is the long-short equal-weighted portfolio return from the ﬁve countries: Canada, France, Germany, Japan, and UK. |Flowt−1| is the absolute value of the normalized capital ﬂow between US and the other ﬁve countries. It is normalized by the market value of the foreign stock market. The long-short portfolios are formed based on ﬁrm characteristics (X): ﬁrm size (ME), total risk (σ), book-tomarket ratio (BE/ME), and sale growth (GS). High includes the top two deciles; low includes the bottom two deciles; medium includes the middle two deciles. Clustered p values are in braces.

#### Figure 1: The Total Sentiment, 1980 to 2005

- 0
- 1
- 2
- 3

- 0
- 1
- 2
- 3

- 0
- 1
- 2
- 3

| |
|---|

| |
|---|

| |
|---|

TotalSENT

TotalSENT

TotalSENT

−1

−1

−1

−2

−2

−2

−3

−3

−3

1980 1990 2000

1980 1990 2000

1980 1990 2000

CN

FR

BD

- 0
- 1
- 2
- 3

| |
|---|

TotalSENT

−1

−2

−3

1980 1990 2000

JP

- 0
- 1
- 2
- 3

| |
|---|

TotalSENT

−1

−2

−3

1980 1990 2000

UK

- 0
- 1
- 2
- 3

| |
|---|

TotalSENT

−1

−2

−3

1980 1990 2000

US

Total sentiment, SENTTotal, is the ﬁrst principal component of the four measures within one country. The ﬁrst measure (PV OL) is the year-end log ratio of the value-weighted average market-to-book ratios of high volatile stocks and low volatile stocks. The second measure (NIPO) is the log annual number of initial public oﬀerings. The third measure (RIPO) is the average annual ﬁrst-day returns of initial public oﬀerings. The fourth measure (TURN) is detrended log turnover.

Figure 2: The Global and Local Sentiment, 1980 to 2005

| |
|---|

2

GlobalSENT

0

−2

1980 1990 2000

Gobal

| |
|---|

2

LocalSENT

LocalSENT

0

−2

1980 1990 2000

CN

| |
|---|

2

LocalSENT

0

−2

1980 1990 2000

FR

| |
|---|

2

0

−2

1980 1990 2000

BD

| |
|---|

2

LocalSENT

LocalSENT

0

−2

1980 1990 2000

JP

| |
|---|

2

LocalSENT

0

−2

1980 1990 2000

UK

| |
|---|

2

0

−2

1980 1990 2000

US

##### Global sentiment (SENTGlobal) is the ﬁrst principal component of the six total sentiment indexes (SENTTotal) in Canada, France, Germany, Japan, UK, and US. Local sentiment (SENTLocal) is the orthogonal residual from the regression, SENTTotal = bi SENTGlobal+ SENTLocal, within a country.

