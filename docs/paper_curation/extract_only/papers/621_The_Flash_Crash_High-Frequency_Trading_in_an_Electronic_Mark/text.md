# The Flash Crash: High-Frequency Trading in an Electronic Market

ANDREI KIRILENKO, ALBERT S. KYLE, MEHRDAD SAMADI, and TUGKAN TUZUN∗

ABSTRACT We study intraday market intermediation in an electronic market before and during a period of large and temporary selling pressure. On May 6, 2010, U.S. ﬁnancial markets experienced a systemic intraday event – the Flash Crash – where a large automated selling program was rapidly executed in the E-mini S&P 500 stock index futures market. Using audit trail transaction-level data for the E-mini on May 6 and the previous three days, we ﬁnd that the trading pattern of the most active nondesignated intraday intermediaries (classiﬁed as High Frequency Traders) did not change when prices fell during the Flash Crash.

∗Kirilenko is with Imperial College London, Kyle is with the University of Maryland, Samadi is with Southern Methodist University, and Tuzun is with the Federal Reserve Board of Governors. We thank Robert Engle, Chester Spatt, Larry Harris, Cam Harvey, Bruno Biais, Simon Gervais, participants at the Western Finance Association Meeting, NBER Market Microstructure Meeting, Centre for Economic Policy Research Meeting, Q-Group Seminar, Wharton Conference in Honor of Marshall Blume, Princeton University Quant Trading Conference, University of Chicago Conference on Market Microstructure and High-Frequency Data, NYU-Courant Mathematical Finance Seminar, Columbia Conference on Quantitative Trading and Asset Management, and seminar participants at Columbia University, MIT, Boston University, Brandeis University, Boston College, UMass-Amherst, Oxford University, Cambridge University, the University of Maryland, Bank for International Settlements, Commodity Futures Trading Commission, Federal Reserve Board, and the International Monetary Fund, among others. The research presented in this paper was coauthored by Andrei Kirilenko, a former full-time CFTC employee, Albert Kyle, a former CFTC contractor who performed work under CFTC OCE contract (CFCE-09-CO-0147), Mehrdad Samadi, a former full-time CFTC employee and former CFTC contractor who performed work under CFTC OCE contracts (CFCE-11-CO-0122 and CFCE-13-CO-0061), and Tugkan Tuzun, a former CFTC contractor who performed work under CFTC OCE contract (CFCE-10-CO-0175). The Oﬃce of the Chief Economist and CFTC economists produce original research on a broad range of topics relevant to the CFTC’s mandate to regulate commodity futures markets and commodity options markets, and its expanded mandate to regulate the swaps markets pursuant to the Dodd-Frank Wall Street Reform and Consumer Protection Act. The analyses and conclusions expressed in this paper are those of the authors and do not reﬂect the views of the Federal Reserve System, the members of the Oﬃce of the Chief Economist, other CFTC staﬀ, or the CFTC itself. The Appendix can be found in the online version of the article on the Journal of Finance website.

On May 6, 2010, U.S. ﬁnancial markets experienced a systemic intraday event known as the “Flash Crash.” The CFTC-SEC (2010b) joint report describes the Flash Crash as follows:

“At 2:32 [CT] p.m., against [a] backdrop of unusually high volatility and thinning liquidity, a large fundamental trader (a mutual fund complex) initiated a sell program to sell a total of 75,000 E-mini [S&P 500 futures] contracts (valued at approximately $4.1 billion) as a hedge to an existing equity position. [...] This large fundamental trader chose to execute this sell program via an automated execution algorithm (“Sell Algorithm”) that was programmed to feed orders into the June 2010 E-mini market to target an execution rate set to 9% of the trading volume calculated over the previous minute, but without regard to price or time. The execution of this sell program resulted in the largest net change in daily position of any trader in the E-mini since the beginning of the year (from January 1, 2010 through May 6, 2010). [...] This sell pressure was initially absorbed by: high frequency traders (“HFTs”) and other intermediaries in the futures market; fundamental buyers in the futures market; and cross-market arbitrageurs who transferred this sell pressure to the equities markets by opportunistically buying E-mini contracts and simultaneously selling products like [the] SPY [(S&P 500 exchange-traded fund (“ETF”))], or selling individual equities in the S&P 500 Index. [...] Between 2:32 p.m. and 2:45 p.m., as prices of the E-mini rapidly declined, the Sell Algorithm sold about 35,000 Emini contracts (valued at approximately $1.9 billion) of the 75,000 intended. [...] By 2:45:28 there were less than 1,050 contracts of buy-side resting orders in the E-mini, representing less than 1% of buy-side market depth observed at the beginning of the day. [...] At 2:45:28 p.m., trading on the E-mini was paused for ﬁve seconds when the Chicago Mercantile Exchange (“CME”) Stop Logic Functionality was triggered in order to prevent a cascade of further price declines.1 [...] When trading resumed at 2:45:33 p.m., prices stabilized and shortly thereafter, the E-mini began to recover, followed by the SPY. [...] Even though after 2:45 p.m. prices in the E-mini and SPY were recovering from their severe declines, sell orders placed for some individual securities and ETFs (including many retail stop-loss orders, triggered by declines in prices of those securities) found reduced

1The CME’s Globex Stop Logic Functionality is an automated pre-trade safeguard procedure designed to prevent the execution of cascading stop orders that would cause “excessive” declines or increases in prices due to lack of suﬃcient depth in the central limit order book. In the context of this functionality,“excessive” is deﬁned as being outside of a predetermined “no bust” range. The no bust range varies from contract to contract; for the E-mini, it was set at 6 index points (24 ticks) in either direction. After Stop Logic Functionality is triggered, trading is paused for a certain period of time as the matching engine goes into what is called a “reserve state.” The length of the trading pause varies between 5 and 20 seconds from contract to contract; it was set at 5 seconds for the E-mini. During the reserve state, orders can be submitted, modiﬁed, or cancelled, but no executions can take place. The matching engine exits the reserve state by initiating the same auction opening procedure as it does at the beginning of each trading day. After the starting price is determined by the re-opening auction, the matching engine returns to the standard continuous matching protocol.

buying interest, which led to further price declines in those securities. [...] [B]etween 2:40 p.m. and 3:00 p.m., over 20,000 trades (many based on retail-customer orders) across more than 300 separate securities, including many ETFs, were executed at prices 60% or more away from their 2:40 p.m. prices. [...] By 3:08 p.m., [...] the E-mini prices [were] back to nearly their pre-drop level [...and] most securities had reverted back to trading at prices reﬂecting true consensus values.”

To illustrate the large and temporary decline in prices and the corresponding increase in trading volume on May 6, Figure 1 presents end-of-minute transaction prices (solid line) and minute-by-minute trading volume (dashed line) in the E-mini on May 6.

<Insert Figure 1>

The accumulation of the largest daily net short position of the year by a single trader over a matter of minutes can be thought of as a period of large and temporary selling pressure. Theory suggests that a period of large and temporary selling pressure can trigger a market crash even in the absence of a fundamental shock. Building on the Grossman and Miller (1988) framework, Huang and Wang (2008) develop an equilibrium model that links the cost of maintaining continuous market presence with market crashes even in the absence of fundamental shocks and with perfectly oﬀsetting idiosyncratic shocks. In their model, market crashes emerge endogenously when a sudden excess of sell orders overwhelms the insuﬃcient risk-bearing capacity of market makers. Because the provision of continuous market presence is costly, market makers choose to maintain equilibrium risk exposures that are too low to oﬀset large but temporary liquidity imbalances. In the event of a large enough sell order, the liquidity on the buy side can only be obtained after a price drop that is large enough to compensate increasingly reluctant market makers for taking on additional risky inventory.

Weill (2007) presents an equilibrium model of optimal dynamic inventory adjustment of competitive capital-constrained intermediaries faced with large and temporary selling

pressure. This framework begins with an exogenous negative aggregate shock to outside investors’ marginal utility of holding the asset, which leads to a sharp price drop. During and immediately following the price drop, there is no change in intermediaries’ inventories. As intermediaries anticipate that the marginal utilities of some outside investors’ will begin to increase and the selling pressure will subside, they ﬁnd it optimal to dynamically accumulate a long position, during which time market prices rise. They then unwind their inventory just as market prices reach their initial level. As shown in Figure 1 of Weill (2007), the co-movement between intermediary inventories and prices varies over time, suggesting that this relationship is dynamic. More generally, Nagel (2012) shows that return reversals are related to the risk-bearing capacity of intermediaries.

Intermediation is an essential function in markets in which buyers and sellers do not arrive simultaneously. As technology has transformed the way ﬁnancial assets are traded, intermediation has been increasingly provided by market participants without formal obligations. An important question is how nondesignated intraday intermediaries behave during periods of large and temporary buying or selling pressure in automated ﬁnancial markets.

In this paper, we empirically examine intraday market intermediation in an electronic market before and during a period of large and temporary selling pressure.2 We use audit trail account-level transaction data in the E-mini S&P 500 stock index futures

2We use the term intraday intermediation instead of market making or liquidity provision because the two latter terms have become associated with aﬃrmative obligations to provide two-sided quotes, serve a customer base, and maintain “fair and orderly markets.” Market making has also been formally recognized in a plethora of government regulations, regulations by self-regulatory organizations, and court decisions. Intraday intermediation, in contrast, does not necessarily entail designated market making or mandatory liquidity provision. Intraday intermediation can be provided by not only designated market makers, but also by proprietary traders trading exclusively for their own trading accounts without acting in any agency capacity such as, for example, routing customer order ﬂow or providing customer advice (see Committee on the Global Financial System (2014)). The term intraday intermediation is also distinct from the notion of ﬁnancial intermediation, which refers to the process of asset transformation “by purchasing assets and selling liabilities” (see Madhavan (2000)).

market over the period May 3 through 6, 2010.3 Guided by the literature on inventory management by intermediaries (see O’Hara (1995) and Hasbrouck (2006), among others), we classify trading accounts that do not accumulate large directional positions and whose inventories display mean-reversion during May 3 through 5 as intraday intermediaries. If an account is classiﬁed as an intermediary on any of these three days, we keep it in the same category on May 6, 2010. Importantly, this approach does not require that an intermediary maintain low inventory on the day of the Flash Crash. We further separate intraday intermediaries into High Frequency Traders and Market Makers.4 As their category name suggests, High Frequency Traders participate in a markedly larger proportion of trading than Market Makers.5

Theory suggests that intermediaries optimally adjust inventory in relation to falling prices. If the intermediaries’ risk-bearing capacity is overwhelmed, they become unwilling to accumulate more inventory without large price concessions. Consistent with the theory of limited risk-bearing capacity of intermediaries, the combined net inventories of the accounts classiﬁed as intraday intermediaries over the four days of our sample, including May 6, did not exceed 6,000 E-mini contracts – a sum that is an order of magnitude smaller than the large sell program of 75,000 contracts documented in CFTC-SEC (2010b). In contrast to Weill (2007), during the period of large and temporary selling pressure on May 6, we ﬁnd that both categories of intraday intermediaries also accumulate net long inventory positions as prices decline.

To examine the dynamic risk-bearing capacity of intermediaries before and during

- 3The CFTC-SEC report’s narrative of the Flash Crash in the E-mini was based in part on the

preliminary analysis contained in the original version of this paper (see footnote 22 of CFTC-SEC

- (2010b).

- 4Throughout the paper we employ the following convention: we use upper case letters whenever we

refer to the categories that we deﬁne, e.g., Market Makers and High Frequency Traders and lower case letters whenever we refer to general type of activity, e.g., market making and high frequency trading.

5Accounts classiﬁed as High Frequency Traders based on inventory and volume patterns might be representative of a subset of all high frequency trading strategies.

the Flash Crash, we empirically study the second-by-second co-movement of their inventory changes and price changes over May 3 through 6. We ﬁnd that inventory changes of High Frequency Traders exhibit a statistically signiﬁcant relationship with both contemporaneous and lagged price changes and that this relationship did not change when prices fell during the Flash Crash. However, the statistical relationship between Market Maker inventory changes and price changes did change during the Flash Crash compared with the previous three days.

Moreover, we ﬁnd that inventory changes of Market Makers are negatively related to contemporaneous price changes, consistent with theories of traditional market making (see Hendershott and Seasholes (2007), among others). In contrast, inventory changes of High Frequency Traders are positively related to contemporaneous price changes. Foucault, Roell, and Sandas (2003), Menkveld and Zoican (2016), and Budish, Cramton, and Shim (2015) provide theoretical mechanisms through which the inventories of intermediaries may positively co-move with price changes at high frequencies. These studies suggest that if certain traders can react marginally faster to a signal, they can adversely select stale quotes of marginally slower market makers, engaging in “stale quote sniping” or “latency arbitrage.” Consequently, faster traders are able to trade ahead of price changes at short time horizons.

Consistent with the theory of “stale quote sniping,” we ﬁnd that over May 3 through 5, when High Frequency Traders are net buyers in a given second, prices increase in the following second and remain higher over the subsequent 20 seconds. We examine the extent to which High Frequency Traders’ trading activity precedes price changes and ﬁnd that High Frequency Traders lift a disproportionate amount of the ﬁnal best ask depth before an increase in the best ask level and provide a disproportionate proportion of depth ﬁrst transacted against at the new price level.

Our main contribution is empirically studying theories of intermediation during a pe-

riod of large and temporary selling pressure. The closest studies to ours are Brogaard, Hendershott, and Riordan (2016), who study high frequency traders as classiﬁed by NASDAQ during the 2008 short-sale ban and Brogaard et al. (2016), who study the activity of high frequency traders as classiﬁed by NASDAQ around extreme price movements.6 In contrast, we focus on trading during the Flash Crash in the inclusive, centralized Emini market with individual account IDs and use the entire universe of trading accounts. Our analysis makes use of a detailed and comprehensive set of transaction-level data in the E-mini three days before and on the day of the Flash Crash. Focusing on trading in the E-mini during the Flash Crash provides two additional advantages. Unlike the U.S. equity markets, there are no market maker obligations in the fully electronic E-mini. Thus, a focus on trading in the E-mini during the Flash Crash may help us understand the potential implications of not imposing market making obligations as markets become more automated, especially during periods of market stress. Furthermore, all of the trading in the E-mini takes place in one venue. Consequently, our results are not aﬀected by the fragmentation of trading, and we are able to study the entire universe of

6Since the release of CFTC-SEC (2010b), a number of studies have examined the Flash Crash. For example, Madhavan (2012) studies the propagation of the Flash Crash to ETFs where trades were disproportionately broken and ﬁnds that ETFs that traded at stub quote price levels were characterized by a relatively high degree of trading fragmentation. Menkveld and Yueshen (2016) study the trading of the large sell program during the Flash Crash and argue that the arbitrage relationship between the E-mini and the S&P 500 ETF (SPY) may have broken down during the Flash Crash and subsequent recovery. Easley, Lopez, and O’Hara (2011) apply the Volume Synchronized Probability of Informed Trading (VPIN) measure to the day of the Flash Crash and ﬁnd abnormal levels of “order-ﬂow toxicity” in the hours leading up to the crash. Market data vendor and commentator Nanex also analyzes trading during the Flash Crash and argues that the large fundamental seller never submitted marketable orders. In contrast, Menkveld and Yueshen (2016) document that “half of the sell orders were limit orders, the other half market orders.” While these studies contribute to our overall understanding of how the Flash Crash became a systemic ﬁnancial marketwide event, we focus on the trading of intraday intermediaries in the stock index futures market, where, according to the CFTC–SEC (2010b) report, the triggering event occurred.

trading of a given account in the E-mini June 2010 contract.7

The rest of the paper proceeds as follows. In Section I, we discuss the market structure of the E-mini and the data employed in this paper. In Section II, we present our empirical methodology and results. In Section III, we conclude.

## I. Institutional Background and Data

### A. The E-mini S&P 500 Futures Market

The CME introduced the E-mini contract in 1997. The E-mini owes its name to the fact that it is traded electronically and in denominations ﬁve times smaller than the original S&P 500 futures contract. Since its introduction, the E-mini has become a popular instrument to hedge exposures to baskets of U.S. stocks or to speculate on the direction of the entire stock market. The E-mini contract attracts the highest dollar volume among U.S. equity index products (futures, options, or exchange-traded funds). Hasbrouck (2003) shows that of all U.S. equity index products, the E-mini contributes the most to the price discovery of the U.S. stock market. The contracts are cashsettled against the value of the underlying S&P 500 equity index at expiration dates in March, June, September, and December of each year. The contract with the nearest expiration date, which attracts the majority of trading activity, is called the “frontmonth” contract. In May 2010, the front-month contract was the contract expiring in

7A number of studies have analyzed the behavior of high frequency traders as classiﬁed by NASDAQ using data from NASDAQ exchanges only (see Brogaard, Hendershott, and Riordan (2014, 2016), Carrion (2013), Hirschey (2016) and Brogaard et al. (2016), inter alia). However, as of the end of Q3, 2010, trading on NASDAQ exchanges represented approximately a third of Tape C (the tape for NASDAQ stocks) trading volume. Our approach also diﬀers from studies that attempt to infer the behavior of high frequency traders from aggregate market data (see Hendershott, Jones, and Menkveld

- (2011), Hasbrouck and Saar (2013), and Conrad, Wahal, and Xiang (2015), inter alia). We are also able to study the trading of all accounts active in the E-mini rather than the trading of one high frequency

- trader or institutional investor (see Menkveld (2013) and Menkveld, and Yueshen (2016), respectively).

June 2010. The notional value of one E-mini contract is $50 multiplied by the S&P 500 stock index. During May 3 - 6, 2010, the S&P 500 index ﬂuctuated slightly above 1,000 points, making each E-mini contract worth about $50,000. The minimum price increment, or “tick” size, of the E-mini is 0.25 index points, or $12.50; a price move of one tick represents a ﬂuctuation of about 2.5 basis points. The E-mini trades exclusively on the CME Globex trading platform, a fully electronic limit order market. Trading takes place 24 hours a day with the exception of one 15-minute technical maintenance break each day. The CME Globex matching algorithm for the E-mini follows a “price-time priority” rule in that orders oﬀering more favorable prices are executed ahead of orders with less favorable prices, and orders with the same prices are executed in the order they were received by Globex. The market for the E-mini features both pre- and post-trade transparency. Pre-trade transparency is provided by transmitting to the public in real time the quantities and prices for buy and sell orders resting in the central limit order book up or down 10 tick levels from the last transaction price. Post-trade transparency is provided by transmitting to the public prices and quantities of executed transactions. The identities of individual traders submitting, canceling, or modifying bids and oﬀers, as well as those whose orders have been executed, are not made available to the public.

### B. Data

Our sample consists of intraday audit trail transaction-level data for the E-mini S&P 500 June 2010 futures contract for the sample period spanning May 3 - 6, 2010. These data come from the Trade Capture Report (TCR), which the CME provides to the CFTC.8 For each of the four days, we examine all regular transactions occurring during

8Due to the highly conﬁdential nature of these data and commonality across certain trading accounts, we aggregate trading accounts into trader categories. Prior to the release of this paper, all matters related to the aggregation of data, presentation of results, and sharing of the results with the public were reviewed by the CFTC.

the 405-minute period starting at the opening of the market for the underlying stocks at 8:30 a.m. CT (CME Globex is in the Central Time Zone) or 9:30 a.m. ET and ending at the time of the technical maintenance break at 3:15 p.m. CT, 15 minutes after the close of trading in the underlying stocks. For each transaction, we use ﬁelds with the account identiﬁers for the buyer and the seller, the price and quantity transacted, the date and time (to the nearest second), a sequence ID number that sorts trades into chronological order within one second, a ﬁeld indicating whether the trade resulted from a limit (both marketable and nonmarketable) or market order, an order ID that assigns multiple trade executions to the original order, and an “aggressiveness” indicator stamped by the CME Globex matching engine as “N” for a resting order and “Y” for an order that executed against a resting order. We do not study message-level data and, thus, do not observe activity for orders that did not execute.

### C. Descriptive Statistics

Market-level descriptive statistics are presented in Table I. We report statistics separately for May 3 to 5 and May 6. Statistics in the May 3 to 5 column represent three-day averages.

<Insert Table I>

Trading volume and the number of trades on May 6 were more than double the average daily trading volume over the previous three days. Volatility measured as the log of the intraday price range was also signiﬁcantly larger on May 6.9 The average trade size on both May 3 - 5 and May 6 was approximately ﬁve contracts. Over 90%

9In the Internet Appendix, we present the daily ﬁve-minute realized variance of the SPY for 2004 to 2013 and ﬁnd that the daily realized variances observed on May 3 - 5 were not abnormal.

of trading and trading volume were executed via limit orders (both marketable and non-marketable).

## II. Methodology and Results

We classify over 15,000 unique accounts trading in the E-mini into intraday intermediaries and other categories of traders to provide an empirical analysis of intraday intermediation before and during the Flash Crash. We then study the behavior of the most active intermediaries deﬁned as High Frequency Traders in more detail.

### A. Trader Categories

Over 15,000 unique accounts traded in the E-mini during our sample period. Traders in the E-mini, including those that buy and sell throughout a trading day, do not have formal designations such as market makers, dealers, or specialists. To classify accounts as intraday intermediaries, we adopt a data-driven approach based on trading activity and inventory patterns. Our deﬁnition of intraday intermediaries is designed to capture traders who follow a strategy of consistently buying and selling throughout a trading day while maintaining low levels of inventory.10

Market intermediaries can be broadly deﬁned as “traders who can ﬁll gaps arising from imperfect synchronization between the arrivals of buyers and sellers” (see Grossman and Miller (1988)). This deﬁnition implies that intermediaries often participate in a signiﬁcant proportion of transactions (see Glosten and Milgrom (1985) and Kyle (1985)) and that intermediaries’ inventories are mean-reverting at a relatively high frequency (see Garman (1976), Amihud and Mendelson (1980), and Ho and Stoll (1983), among

10We use a broad deﬁnition of intermediation to classify accounts as intraday intermediaries that does not use the relationship between intermediary trading and prices or price ﬂuctuations.

others). Empirically, intraday mean-reversion in inventories and relatively high trading volume are salient characteristics of intermediation (see Hasbrouck and Soﬁanos (1993), and Madhavan and Smidt (1993)). A growing literature on the most active intermediaries variously deﬁnes them as fast traders, high frequency traders, or high frequency market makers (see Ait-Sahalia and Saglam (2016), Jovanovic and Menkveld (2016), Biais, Foucault, and Moinas (2015), as well as empirical studies by Menkveld (2013), Brogaard, Hendershott, and Riordan (2014), and Carrion (2013), and a survey by Jones (2013)).

A trader is classiﬁed as an intraday intermediary if it holds small intraday and endof-day net positions relative to its daily trading volume over May 3 - 5, 2010, irrespective of its trading behavior on May 6. To be classiﬁed as an intraday intermediary, a trader denoted by j must meet criteria (i) with respect to its daily trading volume (V olj,d), where d denotes a trading day, (ii) with respect to its end-of-day position (NPj,d,t=405) relative to its daily trading volume, where t denotes each minute during a trading day, and (iii) with respect to its intraday minute-by-minute inventory (NPj,d,t) pattern.

We set the following speciﬁc levels for each criterion (to simplify notation, we suppress the subscript j and set beginning-of-day inventories for all trading accounts to zero (NPj,d,t=0 = 0)):

(i) An account must trade 10 or more contracts on at least one of the three days prior to the Flash Crash (May 3, 4, and 5, 2010).

V old ≥ 10,

According to the data, this volume cutoﬀ is a conservative way to ﬁrst remove accounts that do not trade an economically signiﬁcant amount before categorizing intraday

intermediaries.11

(ii) The three-day average of the absolute value of the ratio of the account’s end-ofday net position to its daily trading volume must not exceed 5%.

3

|NPd,t=405| V old

d=1

3 ≤ 5%.

Speciﬁcally, we compute the daily ratio of a trader’s end-of-day position to its daily trading volume on May 3, 4, and 5, compute the absolute value of the ratios for each day, and calculate the three-day average of the absolute values of the ratio.

(iii) The three-day average of the square root of the account’s daily mean of squared end-of-minute net position deviations from its end-of-day net position over its daily trading volume must not exceed 0.5%.

405

3

(NPd,t−VNPol d,t=405

1 405

)2 3 ≤ 0.5%.

d

t=1

d=1

These cutoﬀ levels are speciﬁc to our sample and may need to be adjusted if applied in other markets.12

Of the accounts that are classiﬁed as intraday intermediaries, we further classify the 16 most active accounts, that is, those with the highest number of trades over May 3 -

- 11In setting the volume cutoﬀ, there is a tradeoﬀ. On the one hand, the number of contracts traded needs to be large enough to ensure that economically small traders are not mistakenly categorized as intraday intermediaries, but not so high that accounts characterized by consistent buying and selling are mistakenly categorized as Small Traders. Using a back-of-the-envelope approximation from Table II, the average number of contracts traded per day by an average Small Trader is 1.98 ((2,397,639 × 0.005)/6,065 ≈ 1.98). The corresponding approximation for intraday intermediaries is 5,255 contracts ((2,397,639 × 0.4471)/204 ≈ 5,255). There is a signiﬁcant diﬀerence between these diﬀerent types of categories in the data. However, rather than making the volume cutoﬀ larger, we apply two additional criteria that also link to the theory and empirical evidence of intermediation.
- 12Kirilenko, Mankad, and Michailidis (2013) conﬁrm the qualitative intuition of our classiﬁcation using a dynamic unsupervised machine learning method that does not rely on user-speciﬁed cutoﬀs.

5, as High Frequency Traders.13 The other intraday intermediary accounts are classiﬁed as Market Makers. A High Frequency Trader is thus similar to a Market Maker in all respects, except that High Frequency Traders participate in a signiﬁcantly greater number of trades.14 If an account is classiﬁed as a High Frequency Trader or a Market Maker over May 3 - 5, 2010, it remains in the same category for May 6, 2010, as well. As previously mentioned, this restriction does not require that a High Frequency Trader or a Marker Maker maintain low inventory relative to volume on the day of the Flash Crash.15

We classify all other traders as Small Traders, Fundamental Buyers, and Fundamental Sellers. We call the remaining accounts Opportunistic Traders. Unlike High Frequency Traders and Market Makers, these trader categories are classiﬁed separately for each of the four trading days, including May 6, 2010.16

On each day, an account is classiﬁed as a Small Trader if it trades fewer than 10 contracts. Over 6,000 out of the 15,000 accounts are classiﬁed as Small Traders. The

- 13Results are qualitatively similar when we classify the most active accounts based on trading volume. According to Figure 2 below, there is also a large diﬀerence in the trading volume between the 16th and 17th ranked intraday intermediaries in terms of daily trading volume.
- 14High Frequency Traders trade signiﬁcantly more frequently than any other trader category, including Market Makers. Over May 3 - 5, 15 High Frequency Traders were active on average. The three-day average of the High Frequency Traders’ daily number of trades per second is 5.98. In contrast, over May 3 - 5, 189 Market Makers were active on average and the three-day average of the Market Makers’ daily number of trades per second is 2.14. These estimates suggest that on average a High Frequency Trader

- trades about 30 times more often than a Market Maker. While we do not observe the messages or latency of traders with our data, Clark-Joseph (2014) applies our classiﬁcation methodology to message-level data and conﬁrms that High Frequency Traders submit messages in the millisecond environment. Hayes et al. (2012) conﬁrm our classiﬁcation with simulated data calibrated on the E-mini.

- 15Sixteen unique accounts were classiﬁed as High Frequency Traders over May 3 - 6, of which, 14 of the 16 accounts traded on May 3, all 16 accounts traded on May 4, and 15 of the 16 accounts traded on May 5. No new accounts that satisfy the criteria of High Frequency Traders enter the E-mini on May 6. The accounts classiﬁed as High Frequency Traders based on inventory and volume patterns may be representative of a subset of all high frequency trading strategies as deﬁned by the SEC (2014) concept release on market structure.
- 16The rationale for classifying Small, Fundamental, or Opportunistic traders separately each day is that they may trade only on one day. It is also possible that the same account can be classiﬁed diﬀerently on diﬀerent days. For example, an account can be a Fundamental Buyer on one day, a Small Trader on another day, and a Fundamental Seller or Opportunistic Trader on yet another day.

Small Traders category likely captures retail traders (see Kaniel, Saar, and Titman (2008), and Seasholes and Zhu (2010) among others). Small Traders account for less than 1% of the total trading volume in our sample.

On each day, an account is classiﬁed as a Fundamental Buyer if it trades 10 contracts or more and accumulates a net long end-of-day position equal to at least 15% of its total trading volume for the day. Similarly, an account is classiﬁed as a Fundamental Seller if it trades 10 contracts or more and the absolute value of its net short position at the end of the day is at least 15% of its total trading volume for the day. This category is meant to capture accounts that accumulate signiﬁcant directional positions on a given day and most likely reﬂects trading patterns of institutional investors with longer holding horizons (see Anand et al. (2013), and Puckett and Yan (2011), among others).

The remaining accounts are categorized as Opportunistic Traders. Opportunistic Traders move in and out of positions throughout the day but adjust their net holdings with signiﬁcantly larger ﬂuctuations and lower frequency than intraday intermediaries. Opportunistic Traders may follow a variety of arbitrage trading strategies, including cross-market arbitrage (for example, long futures/short securities), statistical arbitrage, and news arbitrage (buy if the news indicators are positive/sell if the news indicators are negative). Opportunistic Traders may also engage in providing intermediation across days or weeks rather than intraday.

Our classiﬁcation methodology is based entirely on directly observed individual inventory and trading volume patterns of traders. Unlike many other markets, traders in our data set do not have designations due to regulatory, reporting, or other mandatory or voluntary disclosure requirements. In that regard, our classiﬁcation diﬀers from papers that use NASDAQ data, which classify high frequency traders using a variety of qualitative and quantitative criteria, or the approach of Biais, Declerck, and Moinas (2016) which uses a combination of a proprietary/agency ﬂag along with quantitative

criteria. Our approach also diﬀers from those that use only qualitative criteria to identify traders such as Kurov and Lasser (2004), who use a proprietary/agency code, Joint Staﬀ Report (2015) on the October 15 “Flash Rally” in U.S. Treasuries, which classiﬁes accounts based on their organizational structure or Chaboud et al. (2014), who use a ﬂag provided by a trading platform.

Figure 2 provides a visual representation of two of our classiﬁcation dimensions: trading activity and end-of-day positions for all but the Small Traders, whose activity is negligible. The four panels correspond to each of the four trading days. The shaded areas are stylistically drawn to cover the areas populated by the individual trading accounts that fall into each of the categories based on their trading volume (vertical axis) and end-of-day position scaled by market trading volume (horizontal axis).17

<Insert Figure 2>

According to Figure 2, the ecosystem of the E-mini market consists of ﬁve fairly distinct clusters of traders: Fundamental Buyers, Fundamental Sellers, High Frequency Traders, Opportunistic Traders, and Market Makers. In terms of their trading activity, High Frequency Traders stand out from all the other trading categories and are clearly distinct from Market Makers. By accumulating a signiﬁcant negative inventory, the cloud of Fundamental Sellers spreads out to the left of the origin, while the cloud of Fundamental Buyers spreads out to the right. Opportunistic Traders overlap to some extent with all of the other categories of traders.

Average indicators of trading activity for all categories of traders are presented in

- Table II. Panel A presents averages for the three days prior to the Flash Crash (May 3 17For conﬁdentiality reasons, we do not present trading volume or net position of individual accounts.

to 5, 2010), while Panel B presents indicators for the day of the Flash Crash (May 6, 2010).

<Insert Table II>

According to Table II, during the three days prior to the Flash Crash, 15 High Frequency Traders on average accounted for an average of 34.22% of the total trading volume and 189 Market Makers, on average accounted for an additional 10.49% of total trading volume. On the day of the Flash Crash, their respective shares of total trading volume dropped to 28.57% and 9.00%, respectively.18

Table II also presents average trade-weighted and volume-weighted “Aggressiveness Ratios,” deﬁned as the percentage of trades or contracts in which a side of the trade was the marketable side as opposed to a nonexecutable (that is, passive or resting). Over May 3 to 5, 2010, the three-day average of the volume-weighted proportions of aggressive trade executions by High Frequency Traders and Market Makers are 49.86% and 34.99%, respectively. On May 6, 2010, the proportions are only slightly diﬀerent at 46.59% and 32.49%, respectively.19 On May 6, trades of Fundamental Sellers resulted from markedly larger portions of orders that were executed than the other trader categories. Over 99% of High Frequency Traders’ and Market Makers’ trades result from limit orders, while only 65% of Small Traders’ trades result from limit orders.

### B. Intermediation and the Flash Crash

Theory links liquidity crashes to the risk-bearing capacity of intermediaries. Huang and Wang (2008, 2010) develop an equilibrium framework in which market crashes

18Some accounts classiﬁed as Market Makers for May 3 to 5 did not trade on May 6. 19During the re-opening auction after the triggering of the Stop Logic Functionality on May 6, 2010,

both sides of transactions were marked as passive.

emerge endogenously when a sudden excess of sell orders overwhelms the insuﬃcient risk-bearing capacity of market makers. Further, Ait-Sahalia and Saglam (2016) link elevated price volatility with tighter inventory bounds for “high frequency” intermediaries, reﬂecting their capacity to bear risk associated with increased volatility.

The risk-bearing capacity of intermediaries can be identiﬁed by the observed bounds of their net positions.20 Figure 3 presents the end-of-minute net inventories of Market Makers and High Frequency Traders alongside the price level of the E-mini. The dashed lines plot Market Makers’ and High Frequency Traders’ net positions, while the solid lines plot the price level of the E-mini. The top four panels present the net position of Market Makers over May 3 to 6, while the bottom four panels present the net positions of High Frequency Traders.

<Insert Figure 3>

On each of the four days in our sample, High Frequency Traders never accumulated inventories greater than approximately 4,000 contracts, which is much smaller than the size of the 75,000-contract order of the large sell program documented in CFTC-SEC (2010b).21 Similarly, Market Makers do not take on net inventories that exceed 1,500 contracts in either direction. These ﬁndings are consistent with the theory of the limited

- 20See, for example, the inventory control models such as those in Amihud and Mendelson (1980) and Ho and Stoll (1983), among others. For empirical analysis, see Madhavan and Smidt (1993) and Hasbrouck and Soﬁanos (1993), among others.
- 21In the Internet Appendix, we also document an approximately 30,000-contract trade imbalance between Fundamental Sellers and Fundamental Buyers in the minutes leading up to the Flash Crash. This imbalance is nearly an order of magnitude larger than the documented inventory capacity of High Frequency Traders. In addition, we show that the majority of the Fundamental Trader trade imbalance was picked up by Opportunistic Traders, who may be able to take on larger inventories in the E-mini because they are simultaneously selling shares in equity markets in order to conduct crossmarket arbitrage. The most active Opportunistic Traders in our sample also took on signiﬁcant long inventories during the Flash Crash, likely while engaging in cross-market arbitrage. We present their net inventories under the title “High Frequency Arbitragers” in the Internet Appendix. Our results are consistent with the notion that the imbalance between Fundamental Sellers and Buyers was larger than the risk-bearing capacity of both High Frequency Traders and Market Makers.

risk-bearing capacity of intermediaries during a liquidity crash, as intraday intermediaries did not take on larger inventories compared with their pre-May 6 inventories. In contrast to Weill (2007), during the period of large and temporary selling pressure on May 6, we ﬁnd that both categories of intraday intermediaries also accumulate net long inventory positions as prices decline.22

On May 6, as discussed in CFTC-SEC (2010b), shortly before the Stop Logic Functionality was triggered during the Flash Crash, High Frequency Traders aggressively liquidated approximately 2,000 contracts accumulated earlier, which coincided with signiﬁcant additional price declines. In contrast, Market Makers did not liquidate the inventories that they had accumulated in the early minutes of the Flash Crash until after the Stop Logic Functionality was activated.23

To empirically examine the risk-bearing capacity of intraday intermediaries before and during the Flash Crash, we examine the second-by-second co-movement between the inventory changes of High Frequency Traders and Market Makers and market prices. Hasbrouck and Soﬁanos (1993) estimate vector autoregressions that include price changes, signed orders, and NYSE specialist inventory positions. More recently, Hendershott and Menkveld (2014) examine dynamics between the NYSE specialist inventories and prices, and Brogaard, Hendershott, and Riordan (2014) examine co-movements between high frequency traders as deﬁned by NASDAQ and price changes, further decomposing price changes into permanent and temporary price changes.

We employ an empirically similar approach to establish a baseline statistical relationship between changes in inventories and changes in prices over May 3 to 5, 2010. With this baseline analysis, we simply examine the co-movement of intraday intermediary in-

- 22The partial consistency of our empirical results with Weill (2007) could be due to the fact the Flash Crash takes place in an automated central limit order market, while Weill (2007) studies a market in which outside investors must be connected to each other by intermediaries.
- 23For additional description of the trading activity during the seconds prior to the activation of the Stop Logic Functionality, see the Internet Appendix.

ventories and price changes without making causal inferences, as prices and inventories are jointly determined. We employ this baseline analysis separately for High Frequency Traders and Market Makers to account for possible diﬀerences in statistical relationships. Our baseline inventory and price regression is given as24

∆yt = α + φ · ∆yt−1 + δ · yt−1 +

20

[βi · ∆pt−i/0.25] + t, (1)

i=0

where yt and ∆yt denote the inventories and changes in inventories of High Frequency Traders or Market Makers for each second of a trading day, t = 0 corresponds to the opening of stock trading on the NYSE at 8:30:00 a.m. CT (9:30:00 ET) and t = 24,300 denotes the close of Globex at 15:15:00 CT (4:15:00 p.m. ET), and ∆pt denotes the price change in index point units between the high-low midpoint of second t−1 and the high-low midpoint of second t to account for bid-ask bounce. To convert price changes into the number of ticks, we divide ∆p by 0.25.25 We present t-statistics obtained from White (1980) standard errors.26

<Insert Table III>

In all baseline speciﬁcations, the regression coeﬃcient on the lagged intermediary inventory level is negative, reﬂecting the mean-reversion of High Frequency Trader and Market Maker inventories. High Frequency Trader inventory changes are positively related to contemporaneous and lagged price changes in both speciﬁcations up to four lags. By the 10th lagged price change, High Frequency Traders inventory changes become negatively related to price changes. In contrast, Market Maker inventory changes

- 24To allay concerns of nonstationarity, we ﬁrst-diﬀerence intraday intermediary inventories and market prices.
- 25For reference, we also estimate the same regressions without the contemporaneous price change. See the Internet Appendix.
- 26In Augmented Dickey Fuller tests, we reject the null of a unit root for all variables.

are negatively related to contemporaneous price changes but are generally positively related to lagged price changes.27 Hendershott and Seasholes (2007) argue that market makers are willing to accommodate trades to less patient investors only if they are able to buy (sell) at a discount (premium) relative to future prices. Thus, the inventories of intermediaries should coincide with buying and selling pressure, which causes price movements that subsequently reverse themselves, implying a negative contemporaneous relationship between market maker inventories and prices. Although the co-movement between Market Maker inventory changes and price changes ﬁts this paradigm, its High Frequency Trader counterpart does not. The fact that the regression coeﬃcients of High Frequency Traders lagged inventory levels are larger than their Market Maker counterparts may speak to the diﬀerence in holding horizon and inventory mean-reversion of these two categories.28

To test whether the statistical relationship between intermediary inventory changes and price changes signiﬁcantly changed during the Flash Crash, we estimate the following regressions:

∆yt = α + φ∆yt−1 + δyt−1 + Σ20i=0[βi × pt−i/0.25]

+ DtD{αD + φD∆yt−1 + δDyt−1 + Σ20i=0[βiD × pt−i/0.25]}

+ DtU{αU + φU∆yt−1 + δUyt−1 + Σ20i=0[βiU × pt−i/0.25]} + t.

In these regressions, we stack observations from May 3, May 4, May 5, and May 6 and include two sets of interaction terms, DtD and DtU. where DtD corresponds to the

- 27The contemporaneous price change coeﬃcient for High Frequency Traders is statistically distinguishable from its Market Maker counterpart at the 1% level.
- 28Results are qualitatively similar when we when we incorporate lead price changes in these regressions and when we include more price change and inventory lags. See the Internet Appendix.

“down” period of the Flash Crash and DtU corresponds to the “up” period (between 13:32:00 and 13:45:28 CT and between 13:45:33 and 14:08:00 CT, respectively).29 The interaction coeﬃcients measure diﬀerences between the coeﬃcient estimates for the respective periods of the Flash Crash and for the non-Flash Crash periods. Results are presented in Table IV.

<Insert Table IV>

For High Frequency Traders, during the “down” phase of the Flash Crash, all interaction coeﬃcients except for the fourth lagged price change are statistically insigniﬁcant - that is, the statistical relationship between High Frequency Traders’ inventory changes and price changes did not signiﬁcantly change in the seconds during which the price of the E-mini fell. During the “up” phase, which commenced after a ﬁve-second pause in trading, seven coeﬃcients changed - notably, the coeﬃcients on the interaction terms of the contemporaneous price change and the ﬁrst two lagged price change interaction coeﬃcients are negative and signiﬁcant. We construct an F-test from the R2 estimated from the baseline regression presented in Table III and fail to reject the null that the interaction coeﬃcients are jointly distinguishable from zero, lending little evidence to the view that High Frequency Traders’ trading pattern changed.30

In contrast to High Frequency Traders, the contemporaneous and lagged price change interaction coeﬃcients are statistically signiﬁcant for Market Makers during both the “down” and “up” phases of the Flash Crash. During the “down” and “up” phases, the correlation between the Market Maker inventory changes and contemporaneous prices

- 29Since we study intraday intermediation before and during the Flash Crash, we exclude the observations after 14:08:00 (CT) on May 6.
- 30In the Internet Appendix, we document that it is the “down” phase of the Flash Crash that best corresponds to the period of large and temporary selling pressure, as the net selling of Fundamental Sellers exceeds the net buying of Fundamental Buyers by 33,944 contracts. Only one interaction coeﬃcient is statistically signiﬁcant for High Frequency Traders during this period

increased, while the correlation between the lagged prices and inventories decreased. The net eﬀect of these positive and negative changes (sum of the signiﬁcant coeﬃcients) is close to zero, suggesting that the co-movement between Market Maker inventories and prices appears to have shifted down the lag structure. We construct an F-test from the R2 estimated from the baseline regression presented in Table III and reject the null that the interaction coeﬃcients are jointly distinguishable from zero at the 1% level.

The change in co-movement between Market Makers’ inventories and prices during the Flash Crash is consistent with the theory of liquidity crashes when intermediation is endogenous. CFTC-SEC (2010b) also indicates a reduced number of Market Makers during periods of the Flash Crash. In contrast, the mean-reversion of High Frequency Traders’ inventory, as well as the co-movement between the inventories of High Frequency Traders and market prices did not signiﬁcantly change during the Flash Crash.

### C. High Frequency Traders

To better understand High Frequency Traders’ responses to the Flash Crash, we conduct additional empirical analyses of their intraday trading behavior. A developing theoretical literature models the behavior of High Frequency Traders diﬀerently than that of a traditional market marker. Broadly speaking, in these models faster intraday traders are able to “snipe” stale orders of slower market participants (see, for example, Foucault, Roell, and Sandas (2003), Cvitanic and Kirilenko (2010), Budish, Cramton, and Shim (2015), and Menkveld and Zoican (2016)). Quote sniping provides an economic rationale through which the inventories of faster intraday traders may positively co-move with price changes at high frequencies. Empirically, Harris and Schultz (1998) study the trading of the so-called SOES Bandits who picked oﬀ stale dealer quotes in NASDAQ stocks. A testable empirical pattern consistent with these predictions entails certain

traders regularly trading ahead of price changes at short time horizons.

We conduct two sets of tests that further analyze the statistical relationship between changes in the net positions of High Frequency Traders and market prices at very short time horizons. In the ﬁrst set of tests, we analyze how prices change up to 20 seconds after High Frequency Traders trade. Figure 4 illustrates the results. The upper-left panel presents results for High Frequency Traders buy events over May 3 to 5, the upper-right panel presents results for High Frequency Traders buy events on May 6, and the lowerleft and lower-right panels present corresponding results for High Frequency Traders sell events.31

<Insert Figure 4>

When High Frequency Traders are net buyers over May 3 to 5, prices rise by 17% of a tick in the next second then begin to gradually fall; 20 seconds after a net buy by High Frequency Traders, prices remain 15% of a tick higher. The total eﬀect of net buy High Frequency Traders’ trades can be separated into net aggressive and net passive buy trades. When High Frequency Traders buy aggressively, prices rise by 20% of a tick in the next second, continue rising into the next second, stabilize at about 23% of a tick during seconds 2 to 11, and then begin to gradually fall; 20 seconds after a net aggressive buy by High Frequency Traders, prices remain 15% of a tick higher. When High Frequency Traders buy passively, prices rise by 2% of a tick in the next second, prices then slowly trend downward to about negative 3% of a tick at the 20th second. The results are nearly the same for High Frequency Traders’ sell trades, with the notable

31For an “event-second” in which High Frequency Traders are net buyers, net aggressive buyers, and net passive buyers, value-weighted average prices paid by the High Frequency Traders in that second are subtracted from the value-weighted average prices for all trades in the same second and each of the following 20 seconds. The results are averaged across event-seconds, weighted by the magnitude of the High Frequency Traders’ net position change in the event-second. Price diﬀerences on the vertical axis are given in the number of ticks ($12.50 per one E-mini contract).

exception that while prices do decrease in the ﬁrst second for passive High Frequency Traders’ sell trades, they never cross into negative territory and, in fact, drift upward to about 12% of a tick 19 seconds later. The results are qualitatively similar on May 6, though prices appear to have a larger and more persistent response after sales by High Frequency Traders. It is important to note that prices increase in the second after High Frequency Traders complete their position change and not during the second that High Frequency Traders change their position, consistent with timing ability and not just the mechanical result of the price impact of marketable orders. This ﬁnding also cannot be explained by persistence in High Frequency Traders’ inventory changes as one-second High Frequency Traders inventory changes are not autocorrelated, as can be seen in

- Table III. In the second set of tests, we directly study the theory of quote sniping by ana-

lyzing how High Frequency Traders trade before and after decreases in the best bid or increases in the best oﬀer. In a centralized limit order book market, a pattern consistent with stale quote sniping involves traders lifting posted depth just prior to a price change and then oﬀsetting their position immediately at the new price level. Despite not directly examining limit order book data, the exact sequence of transactions and an aggressive/passive ﬂag allows us to infer trader activity around price change events in the centralized E-mini order book in trade and volume time. We deﬁne a price increase (decrease) event as the best ask (bid) price increasing (decreasing). This deﬁnition ensures that we do not consider bid-ask bounces as price change events. When the best ask (bid) price increases (decreases), we count backwards the number of contracts traded at the “old” best ask price preceding the price change event. When we get to 100 contracts, we stop and attribute each side of the 100 contracts traded to one of the six categories of traders, add up the contract sides for each category, and calculate for each category the percentage share of trading volume for the last 100 contracts traded at the “old”

best ask (bid) price before the price increase (decrease). We then compute averages for each category’s overall price increase and decrease events over May 3 to 5 and May 6. Similarly, we calculate the percentage shares of aggressive and passive volume for the 100 contracts at the ”new” best price after the price change. Our choice of examining the last and ﬁrst 100 contracts traded around a price change event is motivated by the fact that the average posted depth at the best bid and oﬀer during our sample was roughly 500 contracts. Furthermore, over May 3 to 5, 98.67 contracts were traded per second on average.32 Results are presented in Table V.

<Insert Table V>

Table V has four panels. Panel A presents price increase events over May 3 to 5. Panel B presents price decrease events over May 3 to 5. Panels C and D present price increase and decrease events on May 6, respectively. In each panel, the last column presents the volume participation of diﬀerent categories of traders without conditioning on price changes.

As shown in the last column of Panel A, when not conditioning on price changes, High Frequency Traders account for 34.04% of aggressive trading at the best ask price level. The share of High Frequency Traders’ aggressive volume rises to 57.70% at the best ask price level before price increase events and falls to 14.84% at the new best ask price level after price increase events.33 On the passive side, High Frequency Traders account for 34.33% of total passive volume at the best ask price level. However, the share of High Frequency Traders’ passive volume at the best ask falls to 28.72% before

- 32Results are qualitatively similar for 20 and 50 contracts, as well as for 10, 25, and 50 transactions. See the Internet Appendix. p-values associated with the averages and diﬀerences between High Frequency Traders and Market Makers are always less than 1%.
- 33These diﬀerences are statistically signiﬁcant at the 1% level.

a price increase event and rises to 37.93% at the new best ask price level after a price increase event.34

For price decrease events, as shown in Panel B, the results are essentially symmetric. High Frequency Traders account for 55.20% of aggressive sell volume for the last 100 contracts traded before a price decrease event, compared with 34.17% when not conditioning on price changes. The share of High Frequency Traders’ aggressive volume decreases to 15.04% at the new bid price after a price decrease event. On the passive side, High Frequency Traders account for 34.45% of the total passive volume at the best bid price level. The share of High Frequency Traders’ passive volume falls to 27.41% before a price increase event and rises to 38.31% traded at the new best bid price level after a price decrease event. Panels C and D show that the behavior of High Frequency Traders is qualitatively similar on May 6.35

In contrast, Market Makers follow a noticeably more passive trading strategy than High Frequency Traders. According to Panel A, Market Makers account for 13.48% of passive volume at the ask and only 7.27% of the aggressive volume at the ask. For the last 100 contracts at the old ask, Market Makers’ share of volume increases relatively modestly, from 7.27% to 8.78% of aggressive volume at the old best ask price level. However, Market Makers’ share of passive volume at the old best ask price also increases, from 13.48% to 15.80%.

These results suggest that High Frequency Traders behave diﬀerently than traditional market makers. The behavior of High Frequency Traders is empirically more consistent

- 34The respective pre-price change event and post-price change event for the High Frequency Traders’ aggressive and passive participation rates over May 3 to 5 are statistically distinguishable at the 1% level.
- 35There were increases in the participation rate by Opportunistic Traders on the aggressive side of trades on May 6. For example, Opportunistic Traders’ share of the aggressive volume at the ask price before a price increase increases from 19.21% over May 3 to 5 to 34.26% on May 6. Similarly, their share of aggressive volume at the bid price before a price decrease increases from 20.99% over May 3 to 5 to 33.86% on May 6.

with the theories of quote sniping or latency arbitrage than theories of traditional market making (see Glosten and Milgrom (1985)).36 Our results, which are based on all trading in the E-mini, strengthen partial-sample results based on equity trading on NASDAQ (see, for example, Brogaard, Hendershott, and Riordan (2014)). We also directly link our empirical design and results to the theory of quote sniping.

## III. Conclusion

In this paper, we study intraday intermediation in the fully automated E-mini S&P 500 futures market before and during the Flash Crash, which was a period of large and temporary selling pressure. Our results suggest that the behavior of nondesignated intraday intermediaries is consistent with the theory of limited risk-bearing capacity: they did not take on large risky inventories relative to the large and temporary selling pressure on May 6. However, unlike textbook market makers, the most active intraday intermediaries (classiﬁed as High Frequency Traders) did not signiﬁcantly alter their inventory dynamics when faced with large liquidity imbalances.

For a period of time, the Flash Crash seemed like an isolated event. However, ﬂash events in the U.S. Treasury markets on October 15, 2014 reignited discussion about the vulnerability of liquid automated markets to severe dislocations and disruptive trading. Our empirical approach provides a framework to study intraday market dynamics before and during such systemic events, which may be a feature of the “new normal.”

36Without a sample of message-level data, we cannot determine whether High Frequency Traders become more aggressive in response to other traders changing their orders or private information, though the resulting trade patterns of either are consistent with quote sniping. Empirical patterns consistent with quote sniping that we document at a higher frequency do not preclude negative correlations of inventories and price changes at lower frequencies, as High Frequency Traders may employ heterogeneous strategies.

###### Initial submission: December 30, 2010; Accepted: June 8, 2016 Editors: Bruno Biais, Michael R. Roberts, and Kenneth J. Singleton

## REFERENCES

Ait-Sahalia, Yacine, and Mehmet Saglam, 2016, High frequency market making, Working paper, Princeton University.

Amihud, Yakov, and Haim Mendelson, 1980, Dealership market: Market making with inventory, Journal of Financial Economics 8, 31-53.

Anand, Amber, Paul Irvine, Andy Puckett, and Kumar Venkataraman, 2013, Institutional trading and stock resiliency: Evidence from the 2007-2009 ﬁnancial crisis, Journal of Financial Economics 108, 773-797.

Biais, Bruno, Fany Declerck, and Sophie Moinas, 2016, Who supplies liquidity, how and when?, Working paper, University of Toulouse.

Biais, Bruno, Thierry Foucault, and Sophie Moinas, 2015, Equilibrium fast trading, Journal of Financial Economics 116, 292-313.

Brogaard, Jonathan, Allen Carrion, Thibaut Moyaert, Ryan Riordan, Andriy Shkilko, and Konstantin Sokolov, 2016, High-frequency trading and extreme price movements, Working paper, University of Washington.

Brogaard, Jonathan, Terrence Hendershott, and Ryan Riordan, 2014, High-frequency trading and price discovery, Review of Financial Studies 27, 2267-2306.

Brogaard, Jonathan, Terrence Hendershott, and Ryan Riordan, 2016, High-frequency trading and the 2008 short sale ban, Working paper, University of Washington.

Budish, Eric, Peter Cramton, and John Shim, 2015, The high-frequency trading arms race: Frequent batch auctions as a market design response, Quarterly Journal of Economics 130, 1547-1621.

Carrion, Allen, 2013, Very fast money: High-frequency trading on the NASDAQ, Journal of Financial Markets 16, 680-711.

- CFTC-SEC Staﬀ Report, 2010a, Preliminary ﬁndings regarding the market events of May 6.
- CFTC-SEC Staﬀ Report, 2010b, Findings regarding the market events of May 6.

Chaboud, Alain, Benjamin Chiquoine, Erik Hjalmarsson, and Clara Vega, 2014, Rise of the machines: Algorithmic trading in the foreign exchange market, Journal of Finance 69, 2045-2084.

Clark-Joseph, Adam, 2014, Exploratory trading, Working paper, University of Illinois.

Committee on the Global Financial System, 2014, Market-making and proprietary trading: Industry trends, drivers and policy implications.

Conrad, Jennifer, Sunil Wahal, and Jin Xiang, 2015, High-frequency quoting, trading, and the eﬃciency of prices, Journal of Financial Economics 116, 271-291.

Cvitanic, Jaksa, and Andrei Kirilenko, 2010, High frequency traders and asset prices, Working paper, California Institute of Technology.

Easley, David, Marcos Lopez, and Maureen O’Hara, 2011, The microstructure of the “Flash Crash”: Flow toxicity, liquidity crashes, and the probability of informed trading, Journal of Portfolio Management 37, 118-128.

Foucault, Thierry, Alisa Roell, and Patrik Sandas, 2003, Market making with costly monitoring: An analysis of the SOES controversy, Review of Financial Studies 16, 345-384.

Garman, Mark, 1976, Market microstructure, Journal of Financial Economics 3, 257275.

Glosten, Lawrence, and Paul Milgrom, 1985, Bid, ask and transaction prices in a specialist market with heterogeneously informed traders, Journal of Financial Economics 14, 71-100.

Grossman, Sanford, and Merton Miller, 1988, Liquidity and market structure, Journal of Finance 43, 617-633.

Harris, Jeﬀrey, and Paul Schultz, 1998, The trading proﬁts of SOES bandits, Journal of Financial Economics 50, 39-62.

Hasbrouck, Joel, 2003, Intraday price formation in U.S. equity index markets, Journal of Finance 58, 2375-2400.

Hasbrouck, Joel, 2006, Empirical Market Microstructure: The Institutions, Economics, and Econometrics of Securities Trading (Oxford University Press, Oxford).

Hasbrouck, Joel, and Gideon Saar, 2013, Low-latency trading, Journal of Financial Markets 16, 646-679.

Hasbrouck, Joel, and George Soﬁanos, 1993, The trades of market makers: An empirical analysis of NYSE specialists, Journal of Finance 48, 1565-1593.

Hayes, Roy, Mark Paddrik, Andrew Todd, Steve Yang, Peter Beling, and William Scherer, 2012, An agent based model of the E-mini S&P 500 applied to Flash Crash analysis, IEEE Conference on Computational Intelligence for Financial Engineering & Economics, 1-8.

Hendershott, Terrence, Charles Jones, and Albert Menkveld, 2011, Does algorithmic trading improve liquidity? Journal of Finance 66, 1-33.

Hendershott, Terrence, and Albert Menkveld, 2014, Price pressures, Journal of Financial Economics 114, 405-423.

Hendershott, Terrence, and Mark Seasholes, 2007, Market maker inventories and stock prices, American Economic Review 97, 210-214.

Hirschey, Nicholas, 2016, Do high-frequency traders anticipate buying and selling pressure? Working paper, London Business School.

Ho, Thomas, and Hans Stoll, 1983, The dynamics of dealer markets under competition, Journal of Finance 38, 1053-1074.

Huang, Jennifer, and Jiang Wang, 2008, Liquidity and market crashes, Review of Financial Studies 22, 2607-2643.

Huang, Jennifer, and Jiang Wang, 2010, Market liquidity, asset prices, and welfare,

Journal of Financial Economics 95, 107-127. Joint Staﬀ Report, 2015, The U.S. Treasury Market on October 15, 2014. Jones, Charles, 2013, What do we know about high-frequency trading? Working paper,

Columbia University. Jovanovic, Boyan, and Albert Menkveld, 2016, Middlemen in limit order markets, Working paper, New York University. Kaniel, Ron, Gideon Saar, and Sheridan Titman, 2008, Individual investor trading and stock returns, Journal of Finance 63, 273-310.

Kirilenko, Andrei, Shawn Mankad, and George Michailidis, 2013, Discovering the ecosystem of an electronic ﬁnancial market with a dynamic machine-learning method, Algorithmic Finance 2, 151-165.

Kurov, Alexander, and Dennis Lasser, 2004, Price dynamics in the regular and E-mini futures market, Journal of Financial and Quantitative Analysis 39, 365-384.

Kyle, Albert, 1985, Continuous auctions and insider trading, Econometrica 53, 13151336.

Madhavan, Ananth, 2000, Market microstructure: A survey, Journal of Financial Markets 3, 205-258.

Madhavan, Ananth, 2012, Exchange-traded funds, market structure, and the Flash Crash, Financial Analysts Journal 68, 20-35.

Madhavan, Ananth, and Seymour Smidt, 1993, An analysis of changes in specialist inventories and quotations, Journal of Finance 48, 1595-1628.

Menkveld, Albert, 2013, High frequency trading and the new market makers, Journal of Financial Markets 16, 712-740.

Menkveld, Albert, and Bart Yueshen, 2016, The Flash Crash: A cautionary tale about highly fragmented markets, Working paper, VU University Amsterdam.

Menkveld, Albert, and Marius Zoican, 2016, Need for speed? Exchange latency and

liquidity, Working paper, VU University Amsterdam. Nagel, Stefan, 2012, Evaporating liquidity, Review of Financial Studies 25, 2005-2039. O’Hara, Maureen, 1995, Market Microstructure Theory (Blackwell, Cambridge, MA). Puckett, Andy, and Xuemin Yan, 2011, The interim trading skills of institutional in-

vestors, Journal of Finance 66, 601-633. Seasholes, Mark, and Ning Zhu, 2010, Individual investors and local bias, Journal of Finance 65, 1987-2010. SEC, 2014, Equity Market Structure Literature Review Part II: High Frequency Trading. Weill, Pierre-Olivier, 2007, Leaning against the wind, Review of Economic Studies 74, 1329-1354. White, Halbert, 1980, A heteroskedasticity-consistent covariance matrix estimator and a direct test for heteroskedasticity, Econometrica 48, 817-838.

#### Table I Market Descriptive Statistics

This table presents summary statistics for the June 2010 E-mini S&P 500 futures contract. The ﬁrst column presents averages calculated for May 3 through 5, 2010, between 8:30 and 15:15 CT. The second column presents statistics for May 6, 2010 between 8:30 and 15:15 CT. Volume is the number of contracts traded. The number of traders is the number of trading accounts that traded at least once during a trading day. Order size and trade size are measured in number of contracts. The use of limit orders is presented in both percent of the number of transactions and trading volume. Volatility is calculated as the natural logarithm of maximum price over minimum price within a trading day.

May 3–5 May 6 Daily Trading Volume 2,397,639 5,094,703 # of Trades 446,340 1,030,204 # of Traders 11,875 15,422 Trade Size 5.41 4.99 Limit Orders % Volume 95.45% 92.44% Limit Orders % Trades 94.36% 91.75% Volatility (Log High-Low Price Range) 1.54% 9.82% Return -0.02% -3.05%

#### SummaryStatisticsofTraderCategories

#### TableII

sizeoftheexecutedportionofanorderwithineachtradercategory.LimitOrders%ofvolumeisathree-dayaverage

through5,2010from8:30to15:15CT.Percentageoftradingvolumeisathree-dayaverageofthedailypercentage

oftotaltradesforeachtradercategory.TradeSize(Avg.)isathree-dayaverageofthedailyaccount-levelaverage

Thistablepresentssummarystatisticsfortradercategories.PanelApresentsthree-dayaveragestatisticsforMay3

oftotaltradingvolumeforeachtradercategory.Percentageoftradesisathree-dayaverageofthedailypercentage

ofthepercentageoftradercategorytradingvolumethatresultedfrommarketableandnonmarketablelimitorders.

tradesizewithineachtradercategory.OrderSize(Avg.)isathree-dayaverageofthedailyaccount-levelaverage

AggRatioVol-Weightedisathree-dayaverageofthepercentageoftradercategorytradingvolumethatresulted

SmallTraders0.50%2.22%6,0651.221.2570.09%58.54%

TraderType%Volume%ofTrades#TradersTradeSizeOrderSizeLimitOrdersAggRatio

HighFrequencyTraders34.22%32.56%155.6914.75100.00%49.86%

OpportunisticTraders30.79%33.34%3,5044.988.8092.14%50.49%

(Avg.)(Avg.)%VolumeVol-Weighted

FundamentalBuyers11.89%10.15%1,0136.3414.0991.26%58.40%

MarketMakers10.49%11.63%1894.887.9299.61%34.99%

FundamentalSellers12.11%10.10%1,0886.5014.2092.18%54.98%

(Avg.)(Avg.)%Volume

Volume#ofTrades#TradersTradeSizeOrderSizeLimitOrders

All2,397,639446,34011,8755.4110.8395.45%

frommarketableorders.PanelBpresentsstatisticsforMay6from8:30to15:15CT.

PanelA:May3–5Three-DayAverage

SmallTraders0.25%1.04%6,8801.201.2463.61%63.63%

TraderType%Volume%ofTrades#TradersTradeSizeOrderSizeLimitOrdersAggRatio

HighFrequencyTraders28.57%29.35%164.859.86100.00%46.59%

OpportunisticTraders40.13%39.64%5,8085.0510.0687.39%52.98%

(Avg.)(Avg.)%VolumeVol-Weighted

FundamentalBuyers12.01%11.54%1,2635.1510.4388.84%56.43%

MarketMakers9.00%11.48%1793.895.8899.64%32.49%

FundamentalSellers10.04%6.95%1,2767.1921.2989.99%55.30%

(Avg.)(Avg.)%Volume

Volume#ofTrades#TradersTradeSizeOrderSizeLimitOrders

All5,094,7031,030,20415,4224.999.7692.443%

PanelB:May6

#### Table III Baseline Regression: Net Holdings and Prices

This table presents estimated coeﬃcients for the regression: ∆yt = α + φ∆yt−1 + δyt−1 +

20

i=0[βi × ∆pt−i/0.25] + t. The dependent variable is the change in holdings of High Frequency Traders or Market Makers, as indicated. Both changes in holdings, ∆yt, and lagged holdings, yt−1, are in contracts. Price changes, ∆pt−i, are in ticks. The sampling frequency is one second. t-statistics, calculated using the White (1980) estimator are reported in parentheses. Observations are stacked for May 3 through 5.

∆ NP HFT ∆ NP MM Intercept -1.64 -0.53

(-3.54) (-3.33) ∆NPHFTt−1 -0.01

(-0.69) NPHFTt−1 -0.01

(-11.77) ∆NPMMt−1

(-0.79) NPMMt−1 -0.004

(-8.93) ∆Pt 32.09 -13.54

(18.44) (-23.83)

- ∆Pt−1 17.18 -1.22 (12.58) (-2.71)
- ∆Pt−2 8.36 2.16 (7.15) (4.99)
- ∆Pt−3 5.09 2.53 (4.93) (5.97)
- ∆Pt−4 3.91 2.65 (3.62) (6.54)
- ∆Pt−5 1.81 2.50 (1.56) (5.91)
- ∆Pt−6 -0.08 2.16 (-0.07) (5.42)
- ∆Pt−7 -1.00 1.84

- (-0.97) (4.96)

∆Pt−8 -1.76 1.47

- (-1.56) (3.83)

- ∆Pt−9 -1.81 0.45 (-1.70) (1.19)
- ∆Pt−10 -3.90 0.52

- (-3.78) (1.37)

∆Pt−11 -4.73 -0.03

- (-4.70) (-0.07)

- ∆Pt−12 -3.46 0.15 (-3.33) (0.41)
- ∆Pt−13 -3.80 0.27

- (-3.74) (0.72)

∆Pt−14 -4.77 0.32

- (-4.70) (0.86)

- ∆Pt−15 -2.74 -0.19 (-2.63) (-0.53)
- ∆Pt−16 -2.21 -0.64 (-2.09) (-1.72)
- ∆Pt−17 -2.52 -0.10

- (-2.45) (-0.26)

∆Pt−18 -4.36 0.04

- (-3.96) (0.12)

∆Pt−19 -4.21 0.57

- (-4.16) (1.51)

∆Pt−20 -5.86 -0.12

- (-5.86) (-0.33)

#obs 72837 72837 Adj − R2 0.019 0.026

#### Table IV High Frequency Traders and Market Makers: The Flash Crash

This table presents estimated coeﬃcients for the regression: ∆yt = α+φ∆yt−1 +∆yt−1 + Σ20i=0[βi × pt−i/0.25] + DtD{αD + φD∆yt−1 + δDyt−1 + Σ20i=0[βiD × pt−i/0.25]} + DtU{αU + φU∆yt−1 + δUyt−1 + Σ20i=0[βiU × pt−i/0.25]} + t over May 3 through 6, 2010 with dummy variables DtD and DtU included to interact with observations during the “Down” (from 13:32:00 CT to 13:45:28 CT) and “Up” (from 13:45:33 CT to 14:08:00 CT) phases of the Flash Crash. The period between 13:45:28 CT and 13:45:33 CT corresponds to the ﬁvesecond pause in trading; there are no changes in prices or inventory during the ﬁve-second pause. The cutoﬀ for observations on May 6, 2010 is 14:08:00 CT. The dependent variable the change in holdings of High Frequency Traders or Market Makers, as indicated. Both changes in holdings, ∆yt, and lagged holdings, yt−1, are in contracts. Price changes, ∆pt−i, are in ticks. Estimates are computed for second-by-second observations. t-statistics, calculated using the White (1980) estimator are reported in parentheses.

Variable ∆ NP HFT ∆ NP MM Variable (cont) ∆ NP HFT ∆ NP MM Variable (cont) ∆ NP HFT ∆ NP MM Intercept -2.04 -0.48 InterceptD 9.22 9.15 InterceptU 2.27 0.49

(-4.78) (-3.34) (1.19) (2.41) (0.55) (0.33) ∆NPt−1 -0.005 -0.024 ∆NPtD−1 -0.031 -0.024 ∆NPtU−1 0.004 0.085

(-0.69) (-3.31) (-0.80) (-0.63) (0.10) (2.74) NPt−1 -0.005 -0.005 NPtD−1 -0.002 -0.007 NPtU−1 -0.001 0.000

(-12.95) (-10.78) (-0.38) (-1.62) (-0.21) (-0.17) ∆Pt 31.47 -15.48 ∆PtD 1.29 14.13 ∆PtU -40.83 14.29

(16.89) (-21.96) (0.18) (6.73) (-12.18) (13.68)

- ∆Pt−1 14.96 -0.54 ∆PtD−1 -3.02 11.44 ∆PtU−1 -9.60 5.63 (12.17) (-1.23) (-0.57) (5.11) (-3.44) (7.12)
- ∆Pt−2 6.24 2.69 ∆PtD−2 -6.84 1.87 ∆PtU−2 -9.72 -1.83 (5.36) (5.99) (-1.26) (0.81) (-3.57) (-2.20)
- ∆Pt−3 3.02 2.65 ∆PtD−3 -4.16 -2.03 ∆PtU−3 -3.97 -2.47 (3.31) (7.14) (-0.69) (-1.22) (-1.61) (-3.75)
- ∆Pt−4 1.92 2.74 ∆PtD−4 -9.74 -4.91 ∆PtU−4 -1.12 -2.51 (2.04) (7.78) (-1.98) (-3.11) (-0.49) (-3.70)
- ∆Pt−5 0.63 2.21 ∆PtD−5 -10.94 -3.45 ∆PtU−5 1.86 -2.86 (0.64) (5.99) (-1.57) (-2.25) (0.75) (-4.36)
- ∆Pt−6 -1.89 1.99 ∆PtD−6 0.59 -2.91 ∆PtU−6 4.27 -2.45 (-2.03) (5.72) (0.11) (-1.86) (1.78) (-3.71)
- ∆Pt−7 -2.85 1.92 ∆PtD−7 -1.66 -2.71 ∆PtU−7 -4.54 -3.38 (-2.89) (5.18) (-0.31) (-1.59) (-1.73) (-5.05)
- ∆Pt−8 -2.52 1.43 ∆PtD−8 2.45 -2.97 ∆PtU−8 1.79 -1.65 (-2.68) (4.33) (0.44) (-1.92) (0.76) (-2.76)
- ∆Pt−9 -2.59 0.48 ∆PtD−9 -4.32 -2.98 ∆PtU−9 2.69 -1.64 (-2.76) (1.44) (-0.61) (-1.70) (1.12) (-2.54)
- ∆Pt−10 -5.18 0.91 ∆PtD−10 3.93 -3.40 ∆PtU−10 4.41 -1.52

- (-4.66) (2.12) (0.50) (-1.78) (1.76) (-2.22)

∆Pt−11 -5.07 -0.05 ∆PtD−11 9.84 -6.35 ∆PtU−11 6.01 -0.36

- (-5.76) (-0.16) (1.30) (-2.96) (2.27) (-0.51)

- ∆Pt−12 -4.05 -0.10 ∆PtD−12 8.38 -0.73 ∆PtU−12 4.37 -0.79 (-4.46) (-0.31) (1.07) (-0.37) (1.34) (-1.26)
- ∆Pt−13 -3.86 -0.07 ∆PtD−13 11.92 -4.69 ∆PtU−13 10.02 0.28

- (-4.27) (-0.20) (1.64) (-2.10) (3.34) (0.43)

∆Pt−14 -4.36 0.28 ∆PtD−14 -8.56 0.79 ∆PtU−14 1.64 -0.59

- (-5.01) (0.84) (-1.29) (0.41) (0.62) (-0.98)

- ∆Pt−15 -2.05 -0.17 ∆PtD−15 8.46 -5.41 ∆PtU−15 1.47 -0.09 (-2.27) (-0.50) (1.17) (-2.55) (0.64) (-0.15)
- ∆Pt−16 -2.01 -0.39 ∆PtD−16 -3.25 3.92 ∆PtU−16 1.07 0.99

- (-2.10) (-1.11) (-0.41) (1.80) (0.37) (1.56)

∆Pt−17 -2.67 0.01 ∆PtD−17 6.24 -1.57 ∆PtU−17 5.19 0.48

- (-3.05) (0.02) (0.81) (-0.69) (2.13) (0.75)

∆Pt−18 -3.89 0.19 ∆PtD−18 -8.62 0.86 ∆PtU−18 7.37 -0.69

- (-4.10) (0.58) (-1.05) (0.42) (2.58) (-1.12)

- ∆Pt−19 -3.50 0.70 ∆PtD−19 -1.05 -3.07 ∆PtU−19 -0.75 -0.88 (-3.88) (2.08) (-0.12) (-1.39) (-0.30) (-1.44)
- ∆Pt−20 -5.30 -0.33 ∆PtD−20 -2.32 3.13 ∆PtU−20 4.88 -0.06 (-5.82) (-1.00) (-0.30) (1.36) (2.14) (-0.09)

###### # of Obs 93092 93092 Adjusted R2 0.021 0.036

#### Table V Shares of Passive and Aggressive Trading Volume Around Price Increase and Price Decrease Events

This table presents each trader category’s share of aggressive and passive trading volume for the last 100 contracts traded before a price increase event or price decrease event and the ﬁrst 100 contracts traded at the new higher (lower) price after a price increase (decrease) event. For comparison purposes, this table also presents the unconditional share of aggressive and passive trading volume of each trader category. Trading categories are High Frequency Traders (Hft), Market Makers (Mm), Fundamental Buyers (Buyer), Fundamental Sellers (Seller), Opportunistic Traders (Opp), and Small Traders (Small). To emphasize the symmetry between buying and selling, the rows for Buyer and Seller in Panels B and D have been reversed relative to Panels A and C.

- Panel A: Trading at the Best Ask Around Price Increase Events, May 3–5, 2010 Last 100 Contracts First 100 Contracts Volume at Best Ask

Passive Aggressive Passive Aggressive Passive Aggressive Hft 28.72% 57.70% 37.93% 14.84% 34.33% 34.04% Mm 15.80% 8.78% 19.58% 7.04% 13.48% 7.27% Buyer 6.70% 11.61% 4.38% 26.17% 4.57% 21.53% Seller 16.00% 2.65% 11.82% 7.09% 16.29% 5.50% Opp 32.27% 19.21% 25.95% 43.39% 30.90% 31.08% Small 0.51% 0.04% 0.34% 1.46% 0.44% 0.58%

- Panel B: Trading at the Best Bid Around Price Decrease Events, May 3–5, 2010

Last 100 Contracts First 100 Contracts All Volume at Best Bid Passive Aggressive Passive Aggressive Passive Aggressive

- Hft 27.41% 55.20% 38.31% 15.04% 34.45% 34.17% Mm 15.49% 8.57% 20.64% 6.58% 13.79% 7.45% Seller 5.88% 11.96% 3.83% 24.87% 5.67% 20.91% Buyer 17.98% 3.22% 12.71% 8.78% 15.40% 6.00% Opp 32.77% 20.99% 24.18% 43.41% 30.30% 30.89% Small 0.47% 0.06% 0.34% 1.32% 0.39% 0.58%

Panel C: Trading at the Best Ask Around Price Increase Events, May 6, 2010

Last 100 Contracts First 100 Contracts All Volume at Best Ask Passive Aggressive Passive Aggressive Passive Aggressive

- Hft 28.46% 38.86% 30.55% 14.84% 30.94% 26.98% Mm 12.95% 5.50% 13.88% 5.45% 12.26% 5.82% Buyer 6.31% 17.49% 5.19% 21.76% 5.45% 20.12% Seller 13.84% 3.84% 14.30% 5.71% 14.34% 4.40% OPP 38.26% 34.26% 35.94% 51.87% 36.86% 42.37% Small 0.19% 0.06% 0.16% 0.37% 0.16% 0.31%

###### Panel D: Trading at the Best Bid Around Price Decrease Events, May 6, 2010

Last 100 Contracts First 100 Contracts All Volume at Best Bid

Passive Aggressive Passive Aggressive Passive Aggressive Hft 28.38% 38.67% 30.13% 14.59% 30.09% 26.29% Mm 12.27% 5.04% 14.85% 5.64% 12.05% 5.88% Seller 4.19% 16.46% 3.77% 21.21% 3.82% 17.55% Buyer 15.83% 5.90% 13.89% 6.97% 15.27% 7.26% Opp 39.12% 33.86% 37.15% 51.10% 38.56% 42.68% Small 0.21% 0.08% 0.21% 0.48% 0.21% 0.34%

[Figure 1]

- Figure 1: Prices and trading volume of the E-mini S&P 500 stock index futures contract. Source: “Preliminary Findings Regarding the Market Events of May 6, 2010.” This ﬁgure presents minute-by-minute transaction prices and trading volume of the June 2010 E-mini S&P futures contract on May 6, 2010 between 8:30 and 15:15 CT. Trading volume is calculated as the number of contracts traded during each minute. Transaction price is the last transaction price of each minute.

[Figure 2]

##### Figure 2: Trading accounts, trading volume, and net position scaled by market trading volume. This ﬁgure presents trader categories superimposed (as shaded areas) over all individual trading accounts ranked by their trading volume and net position scaled by market trading volume. The panels reﬂect trading activity in the June 2010 E-mini S&P 500 futures contract for May 3 through 6, 2010.

[Figure 3]

- Figure 3: Net position of Market Makers and High Frequency Traders. This ﬁgure presents the net position (left vertical axis) of Market Makers and High Frequency Traders and market transaction prices (right vertical axis) in the June 2010 E-mini S&P 500 futures contract over one-minute intervals during May 3, 4, 5, and 6 between 8:30 and 15:15 CT. Net position is calculated as the diﬀerence between the total open long and total open short positions of Market Makers and High Frequency Traders at the end of each minute. Transaction price is the last market transaction price each minute. The top panel presents the net positions of Market Makers and the bottom panel presents the net positions of High Frequency Traders.

[Figure 4]

- Figure 4: High Frequency Traders’ trading and prices. This ﬁgure illustrates how prices change after HFT trading activity in a given second. The upper-left panel presents results for buy trades for May 3 through 5, 2010, the upper-right panel presents results for buy trades on May 6, 2010 and the lower-left and lower-right panels present corresponding results for sell trades. For an “event-second” in which High Frequency Traders are net buyers, net Aggressive Buyers, and net Passive Buyers, value-weighted average prices paid by the High Frequency Traders in that second are subtracted from the value-weighted average prices for all trades in the same second and each of the following 20 seconds. The results are averaged across event-seconds, weighted by the magnitude of High Frequency Traders’ net position change in the event-second. The upper-left panel presents results for May 3 through 5, the upper-right panel presents results for May 6, and the lower two panels present results for sell trades calculated analogously. Price diﬀerences on the vertical axis are scaled so that one unit equals one tick ($12.50 per contract).

