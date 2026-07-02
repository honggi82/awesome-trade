# arXiv:2003.01859v1[q-fin.ST]29Feb2020

## Applications of deep learning in stock market prediction: recent progress

#### Weiwei Jiang∗

Department of Electronic Engineering, Tsinghua University, Beijing 100084, China

### Abstract

Stock market prediction has been a classical yet challenging problem, with the attention from both economists and computer scientists. With the purpose of building an eﬀective prediction model, both linear and machine learning tools have been explored for the past couple of decades. Lately, deep learning models have been introduced as new frontiers for this topic and the rapid development is too fast to catch up. Hence, our motivation for this survey is to give a latest review of recent works on deep learning models for stock market prediction. We not only category the diﬀerent data sources, various neural network structures, and common used evaluation metrics, but also the implementation and reproducibility. Our goal is to help the interested researchers to synchronize with the latest progress and also help them to easily reproduce the previous studies as baselines. Base on the summary, we also highlight some future research directions in this topic.

Keywords: Stock market prediction, deep learning, machine learning, feedforward neural network, convolutional neural network, recurrent neural network

### 1. Introduction

Stock market prediction is a classical problem in the intersection of ﬁnance and computer science. For this problem, the famous eﬃcient market hypoth-

∗Corresponding author. E-mail address: jiangweiwei@mail.tsinghua.edu.cn

Preprint submitted to Elsevier Journal March 5, 2020

esis (EMH) gives a pessimistic view and implies that ﬁnancial market is efﬁcient (Fama, 1965), which maintains that technical analysis or fundamental analysis (or any analysis) would not yield any consistent over-average proﬁt to investors. However, many researchers disagree with EMH (Malkiel, 2003). Some studies are trying to measure the diﬀerent eﬃciency levels for mature and emerging markets, while other studies are trying to build eﬀective prediction models for stock markets, which is also the scope of this survey.

The eﬀort starts with the stories of fundamental analysis and technical analysis. Fundamental analysis evaluates the stock price based on its intrinsic value, i.e., fair value, while technical analysis only relies on the basis of charts and trends. The technical indicators from experience can be further used as handcrafted input features for machine learning and deep learning models. Afterwards, linear models are introduced as the solutions for stock market prediction, which include autoregressive integrated moving average (ARIMA) (Hyndman & Athanasopoulos, 2018) and generalized autoregressive conditional heteroskedasticity (GARCH) (Bollerslev, 1986). With the development of machine learning models, they are also applied for stock market prediction, e.g., Logistic regression and support vector machine (Alpaydin, 2014).

Our focus in this survey would be the latest emerging deep learning, which is represents by various structures of deep neural networks (Goodfellow et al., 2016). Powered by the collection of big data from the Web, the parallel processing ability of graphics processing units (GPUs), and the new convolutional neural network family, deep learning has achieved a tremendous success in the past few years, for many diﬀerent applications including image classiﬁcation (Rawat & Wang, 2017; Jiang & Zhang, 2020), object detection (Zhao et al., 2019), time series prediction (Brownlee, 2018; Jiang & Zhang, 2018), etc. With a strong ability of dealing with big data and learning the nonlinear relationship between input features and prediction target, deep learning models have shown a better performance than both linear and machine learning models on the tasks that include stock market prediction.

In the past few years, both the basic tools for deep learning and the new

prediction models are undergoing a rapid development. With the continuous improved programming packages, it becomes easier to implement and test a novel deep learning model. Also, the collection of online news or twitter data provides new sources of predicting stock market. More recently, graph neural networks using various knowledge graph data appear as new ideas. The study for stock market prediction is not limited to the academia. Attracted by the potential proﬁt by stock trading powered by the latest deep learning models, asset management companies and investment banks are also increasing their research grant for artiﬁcial intelligence which is represented by deep learning models nowadays.

Since there are many new developments in this area, this situation makes it diﬃcult for a novice to catch up with the latest progress. To alleviate this problem, we summarize the latest progress of deep learning techniques for stock market prediction, especially those which only appear in the past three years. We also present the trend of each step in the prediction workﬂow in these three years, which would help the new-comers to keep on the right track, without wasting time on obsolete technologies.

We focus on the application of stock market, however, machine learning and deep learning methods have been applied in many ﬁnancial problems. It would be beyond the scope of this survey to cover all these problems. However, the ﬁndings presented in this survey would also be insightful for other time series prediction problems in the ﬁnance area, e.g., exchange rate or cryptocurrency price prediction.

We also pay a special attention to the implementation and reproducibility of previous studies, which is often neglected in similar surveys. The list of open data and code from published papers would not only help the readers to check the validity of their ﬁndings, but also implement these models as baselines and make a fair comparison on the same datasets. Based on our summary of the surveyed papers, we try to point out some future research directions in this survey, which would help the readers to choose their next movement.

Our main contribution in this survey are summarized as follows:

- 1. We summarize the latest progress of applying deep learning techniques to stock market prediction, especially those which only appear in the past three years.
- 2. We give a general workﬂow for stock market prediction, based on which the previous studies can be easily classiﬁed and summarized. And the future studies can refer to the previous work in each step of the workﬂow.
- 3. We pay a special attention to implementation and reproducibility, which is often neglected in similar surveys.
- 4. We point out several future directions, some of which are on-going and help the readers to catch up with the research frontiers.

The rest of this survey is organize as follows: Section 2 presents related work; Section 3 gives an overview of the papers we cover; Section 4 describes the major ﬁndings in each step of the prediction workﬂow; Section 5 gives the discussion about implementation and reproducibility; Section 6 points up some possible future research directions; We conclude this survey in Section 7.

### 2. Related Work

Stock market prediction has been a research topic for a long time, and there are some review papers accompanied with the development and ﬂourishment of deep learning methods prior to our work. While their focus could also be applications of deep learning methods, stock market prediction could only be one example of many ﬁnancial problems in these previous surveys. In this section, we list some of them in a chronological order and discuss our motivation and unique perspectives.

Back to 2009, Atsalakis & Valavanis (2009) surveys more than 100 related published articles that focus on neural and neuro-fuzzy techniques derived and applied to forecast stock markets, with the discussion of classiﬁcations of input data, forecasting methodology, performance evaluation and performance measures used. Li & Ma (2010) gives a survey on the application of artiﬁcial neural networks in forecasting ﬁnancial market prices, including the forecast of

stock prices, option pricing, exchange rates, banking and ﬁnancial crisis. Nikfarjam et al. (2010) surveys some primary studies which implement text mining techniques to extract qualitative information about companies and use this information to predict the future behavior of stock prices based on how good or bad are the news about these companies.

Aguilar-Rivera et al. (2015) presents a review of the application of evolutionary computation methods to solving ﬁnancial problems, including the techniques of genetic algorithms, genetic programming, multi-objective evolutionary algorithms, learning classiﬁer systems, co-evolutionary approaches, and estimation of distribution algorithms. Cavalcante et al. (2016) gives an overview of the most important primary studies published from 2009 to 2015, which cover techniques for preprocessing and clustering of ﬁnancial data, for forecasting future market movements, for mining ﬁnancial text information, among others. Tk´ˇc & Verner (2016) provides a systematic overview of neural network applications in business between 1994 and 2015 and reveals that most of the research has aimed at ﬁnancial distress and bankruptcy problems, stock price forecasting, and decision support, with special attention to classiﬁcation tasks. Besides conventional multilayer feedforward network with gradient descent backpropagation, various hybrid networks have been developed in order to improve the performance of standard models.

More recently, Xing et al. (2018) reviews the application of cutting-edge NLP techniques for ﬁnancial forecasting, which would be concerned when text including the ﬁnancial news or twitters is used as input for stock market prediction. Rundo et al. (2019) covers a wider topic both in the machine learning techniques, which include deep learning, but also the ﬁeld of quantitative ﬁnance from HFT trading systems to ﬁnancial portfolio allocation and optimization systems. Nti et al. (2019) focuses on the fundamental and technical analysis, and ﬁnd that support vector machine and artiﬁcial neural network are the most used machine learning techniques for stock market prediction. Based on its review of stock analysis, Shah et al. (2019) points out some challenges and research opportunities, including issues of live testing, algorithmic trading, self-defeating,

long-term predictions, and sentiment analysis on company ﬁlings.

Diﬀerent from other related works that cover more papers from the computer science community, Reschenhofer et al. (2019) reviews articles covered by the Social Sciences Citation Index in the category Business, Finance and gives more insight on economic signiﬁcance. It also points out some problems in the existing literature, including unsuitable benchmarks, short evaluation periods, and nonoperational trading strategies.

Some latest reviews are trying to cover a wider range, e.g., Shah et al. (2019) covers machine learning techniques applied to the prediction of ﬁnancial market prices, and Sezer et al. (2019) covers more ﬁnancial instruments. However, our motivation is to catch up with the research trend of applying deep learning techniques, which have been proved to outperform traditional machine learning techniques, e.g., support vector machine in most of the publications, with only a few exceptions, e.g., Ballings et al. (2015) ﬁnds that Random Forest is the top algorithm followed by Support Vector Machines, Kernel Factory, AdaBoost, Neural Networks, K-Nearest Neighbors and Logistic Regression, and Ersan et al. (2019) ﬁnds that K-Nearest Neighbor and Artiﬁcial Neural Network both outperform Support Vector Machines, but there is no obvious pros and cons between the performances of them. With the accumulation of historical prices and diverse input data types, e.g., ﬁnancial news and twitter, we think the advantages of deep learning techniques would continue and it is necessary to keep updated with this trend for the future research.

Compared with Sezer et al. (2019), whose focus is deep learning for ﬁnancial time series forecasting and a much longer time period (from 2005 to 2019 exactly), we focus on the recent progress in the past three years (2017-2019) and a narrower scope of stock price and market index prediction. For readers who are also interested in other ﬁnancial instruments, e.g., commodity price, bond price, cryptocurrency price, etc., we would refer them to this work. We also care more about the implementation workﬂow and result reproducibility of previous studies, e.g., dataset and code availability, which is a problem that has drawn the attention from the AI researchers (Gundersen & Kjensmo, 2018). We

would also pay more attention to the uniqueness of stock market prediction (or ﬁnancial time series forecasting) from general time series prediction problems, e.g., the evaluation of proﬁtability besides prediction accuracy.

### 3. Overview

In this section, we give an overview of the papers we are going to review in this study. All the works are searched and collected from Google Scholar, with searching keywords such as deep learning, stock prediction, stock forecasting, etc. Most of the covered papers (115 out of 124) are published in the past three years (2017-2019). In total, we cover 56 journal papers, 58 conference papers and 10 preprint papers. These preprint papers are all from arXiv.org, which is a famous website for e-print archive and we cover these papers to keep updated with the latest progress. The top source journals & conferences sorted by the number of papers we cover in this study are shown in Table 1 and Table 2, respectively.

Table 1: List of top source journals and the number of papers we cover in this study.

Journal Name Paper Count Expert Systems with Applications 12 IEEE Access 5 Neurocomputing 3 Complexity 2 Journal of Forecasting 2 Knowledge-Based Systems 2 Applied Soft Computing 2 Mathematical Problems in Engineering 2 PLOS ONE 2 Others in total 24

In this study, the major focus would be the prediction of the close prices of individual stocks and market indexes. Some ﬁnancial instrument whose price is

Table 2: List of top conferences and the number of papers we cover in this study.

Conference Name Paper Count International Joint Conferences on Artiﬁcial Intelligence (IJCAI)

4

International Joint Conference on Neural Networks (IJCNN)

4

Conference on Information and Knowledge Management (CIKM)

3

International Conference on Neural Information Processing (ICONIP)

3

Annual Meeting of the Association for Computational Linguistics (ACL)

2

IEEE Symposium Series on Computational Intelligence (SSCI)

2

Hawaii International Conference on System Sciences (HICSS)

2

ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD)

2

IEEE International Conference on Tools with Artiﬁcial Intelligence (ICTAI)

2

Others in total 34

bounded to the market index is also covered, e.g., some exchange-traded fund (ETF) or equity index futures that track the underlying market index. For intraday prediction, we would also cover mid-price prediction for limit order books. Other ﬁnancial instruments are not mentioned in this study, e.g., bond price and cryptocurrency price. More speciﬁcally, if the target to predict the speciﬁc value of the prices, we classify it as a regression problem, and if the target is to predict the price movement direction, e.g., going up or down, we classify it as a classiﬁcation problem. Most studies are considering the daily

prediction (105 of 124) and only a few of them are considering the intraday prediction (18 of 124), e.g., 5-minute or hourly prediction. Only one of the 124 papers is considering both the daily and intraday situations (Liu & Wang, 2019).

Based on the target output and frequency, the prediction problems can be classiﬁed into four types: daily classiﬁcation (52 of 124), daily regression (54 of 124), intraday classiﬁcation (8 of 124) and intraday regression (11 of 124). A detailed paper count of diﬀerent prediction problem types is shown in Figure 1. The reason behind this could be partially justiﬁed by the diﬃculty of collecting the corresponding data. The daily historical prices and news titles are easier to collect and process for research, while the intraday data is very limited in the academia. We would further discuss the data availability in Section 5.

| |
|---|

| |
|---|

| |
|---|

Figure 1: The paper count of diﬀerent problem types.

#### Surveyed markets as well as the most famous stock market index in these

markets are shown in the Table 3. The paper count of diﬀerent surveyed markets is shown in Figure 2 1. Most of the studies would focus on one market, while some of them would evaluate their models on multiple markets 2. Both mature markets (e.g., US) and emerging markets (e.g., China) are gaining a lot of attention from the research community in the past three years.

Table 3: List of surveyed markets and stock indexes.

Country Index Description US S&P 500 Index of 505 common stocks issued by 500 large-

cap companies

US Dow Jones Industrial Average

Index of 30 major companies

US NASDAQ Composite

US NYSE Composite

Index of common companies in NASDAQ stock market

Index of common companies in New York Stock Exchange

US RUSSEL 2000 Index of bottom 2,000 stocks in the Russell 3000 Index China SSE Composite Index of common companies in Shanghai Stock Exchange China CSI 300 Index of top 300 stocks in Shanghai and Shenzhen stock exchanges

Hong Kong

HSI Hang Seng Index of the largest companies in Hong Kong Exchange

Continued on next page

- 1An exception of using Europe for Ballings et al. (2015), in which 5767 publicly listed European companies are covered.
- 2Due to the diﬀerences of trading rules, we list mainland China, Hong Kong and Taiwan separately.

Table 3 – continued from previous page Country Index Description Japan Nikkei 225 Index of 225 large companies in Tokyo Stock

Exchange Korea Korea Compos-

Index of common companies in Korea Stock Exchange

ite

India BSE 30 Index of 30 companies exist in Bombay Stock Exchange India NIFTI 50 Index of 50 companies exist in National Stock Exchange England FTSE 100 Index of 100 companies in London Stock Ex-

change Brazil IBOV Bovespa Index of 60 stocks France CAC 40 Index of 40 stocks most signiﬁcant stocks in Eu-

ronext Paris Germany DAX Index of 30 major German companies in Frankfurt Stock Exchange Turkey BIST 100 Index of 100 stocks in Borsa Istanbul Stock Ex-

change Argentina MER Merval Index in Buenos Aires Stock Exchange Bahrain BAX Bahrain All Share Index of 42 stocks Chile IPSA Ipsa Index of 40 most liquid stocks Australia All Ordinaries Index of 500 largest companies in Australian Securities Exchange

### 4. Prediction Workﬂow

Given diﬀerent combinations of data sources, previous studies explored the use of deep learning models to predict stock market price/movement. In this

Figure 2: The paper count from diﬀerent markets.

section, we summarize the previous studies in a general workﬂow with four steps that most of the studies follow: Raw Data, Data Processing, Prediction Model and Model Evaluation. In this section, we would discuss each step separately and reveal a general approach that the future work can easily reproduce.

- 4.1. Raw Data The ﬁrst step of predicting is to collect proper data as the basis. It could be

the intrinsic historical prices with the assumption that history repeats itself, or the extrinsic data sources that aﬀect the stock market. In the eﬃcient-market hypothesis, asset prices already reﬂect all available information. However, in practice many researchers do not agree with this conclusion, thus many diﬀerent extrinsic sources of data are used for stock market prediction, e.g., Weng

et al. (2017) compares the usage of market data, technical indicators, Wikipedia traﬃc, Google news counts, and generated features, and Liu et al. (2019b) covers market data, fundamental data, knowledge graph, and news.

- 4.1.1. Data Types In this part, we categories the raw data that are commonly used for stock

market prediction into seven types:

- • Market data: market data includes all trading activities that happen in a stock market, e.g., open/high/low/close prices, trading volume, etc. It is used as both input features (e.g., the historical prices in a look-back window) and prediction target (e.g., the close price of the next day).
- • Text data: text data refer to the text contributed by individuals, e.g., social media, news, web searches, etc. As a type of alternative data, these data are hard to collect and process, but may provide useful information that is not included in market data. Sentiment analysis can be applied on these text data and produce a sentiment factor (e.g., positive, neural, or negative) that can be further used for prediction.
- • Macroeconomics data: macroeconomics data reﬂects the economic circumstances of a particular country, region or sector, e.g., Consumer Price Index (CPI), Gross domestic product (GDP), etc. These indicators are related with the stock market in the sense that they indicate how healthy the overall stock market is and can provide conﬁrmation as to the quality of a stock market advance or decline.
- • Knowledge graph data: there are some kind of relationship between diﬀerent companies and diﬀerent markets, e.g., the movement of stocks in the same sector may be aﬀected by the same news. Powered by the recently developed graph neural networks, the knowledge graph data from open sources such as FreeBase (Bollacker et al., 2008) and Wikidata 3 can now

3https://www.wikidata.org/

be used to improve the prediction performance.

- • Image data: inspired by the success of convolutional neural networks in 2D image processing, e.g., classiﬁcation and object detection, candlestick charts are used as input images for stock prediction. While satellite and CCTV images or videos are used to monitor the situation of companies and may be helpful for stock price prediction, they are never used in the surveyed papers because of the prohibitive cost of collection and the potential privacy leakage risk.
- • Fundamental data: the most common type of fundamental data is the accounting data, which is reported quarterly, e.g., assets, liabilities, etc. It is less used in studies with deep learning models because the low frequency of reporting and also the inaccuracies of the reporting date, e.g., the fundamental data published is indexed by the last date included in the report and precedes the date of the release, which brings in a risk of using future information.
- • Analytics data: analytics data refers to the data that can be extracted from reports (e.g., recommendation for selling or buying a stock) that are provided by investment banks and research ﬁrms, who make an indepth analysis of companies’ business models, activities, competitions, etc. These reports provide valuation information, while they may be costly and shared among diﬀerent consumers, who all want to use this information to make a proﬁt.

Diﬀerent types or raw data are accompanied with diﬀerent levels of diﬃculty for obtaining and processing, and the usage of diﬀerent data types is shown in Figure 3. For deep learning models, a huge amount of input data is necessary for the training of a complex neural network model. In this case, market data is the best choice and used for the most as it provides the largest amount of data sample, while the other data types usually have a smaller size. Text data is used for the second most, with the popularity of social media and online news

website and the easier use of web crawlers to get the text data. An extreme case is the analytics data, which is never used in the surveyed studies, because of both the data sparsity and the high cost to access.

There is also a trend in Figure 3 that more diverse data types are used in

- 2018 and 2019, compared to the studies in 2017. It indicates the fact that it is harder to get a better prediction result based on only the market data. It also reﬂects the development of new tools so that new types of data can be used for prediction, e.g., graph neural networks for knowledge graph data.

| |
|---|

| |
|---|

| |
|---|

| | | |
|---|---|---|
| | | |
| | | |

Figure 3: The usage of diﬀerent raw data types.

- 4.1.2. Data Length To evaluate the performance of diﬀerent models, historical data is necessary

for evaluation. However, there is a tradeoﬀ of choosing the data length. A short

time period of data is not suﬃcient to show the eﬀective and has a higher risk of overﬁtting, while a long time period takes the risk of traversing diﬀerent market styles and present out-of-dated results. Besides, the data availability and cost are factors that needs to be taken into consideration when choosing the data length.

The distribution of time periods of data used in the surveyed papers is shown in Figure 4. It is more expensive to get intraday data with a good quality and most of the previous studies involving intraday prediction would use a time period less than one year.

| |
|---|

| |
|---|

Figure 4: The distribution of data length.

For a single prediction, lag is used to denote the time length of the input data to be used by the model, e.g., in the daily prediction, a lag of 30 days means the data in the past 30 days are used to build the input features. For technical indicators, lag is often set as an input parameters and vary a lot in

previous studies from 2 to 252 time periods. Correspondingly, horizon is used to denote the time length of the future to be predicted by the model. Most of the studies focus on a short-term prediction horizon, e.g., one day or ﬁve minutes, with only a few exceptions for a longer horizon such as ﬁve days or ten days.

- 4.2. Data Processing

- 4.2.1. Missing Data Imputation The problem of missing data is not as severe as in other domains, e.g.,

sensor data, because the market data is more reliable and well supported and maintained by the trading markets. However, to align multiple types of data with diﬀerent sampling frequencies, e.g., market data and fundamental data, the data with a lower sampling frequency should be inserted in a forward way by propagating the last valid observation forward to next valid, to avoid data leakage of the future information.

- 4.2.2. Denoising With many irrational behaviors in the stock trading process, the market

data is ﬁlled with noise, which may misrepresent the trend of price change and misguide the prediction. As a signal processing technique, wavelet transform has been used to eliminate noise in stock price time series (Bao et al., 2017; Liang et al., 2019). Another approach to eliminate noisy data in Sun et al. (2017) is the use of the kNN-classiﬁers, based on two training sets with diﬀerent labels in a data preparation layer.

- 4.2.3. Feature Extraction For machine learning models, feature engineering is the process of extracting

input features from raw data based on domain knowledge. Combined with raw data, these handcrafted features are used as input for the prediction models and can substantially boost machine learning model performance.

For market data, technical analysis is a feature extraction approach that builds various indicators for forecasting the direction of prices based on his-

torical prices and volumes, e.g., moving average, or moving average convergence/divergence (MACD). These technical indicators can be further used to design simple trading strategies. Technical indicators are also used to build image inputs, e.g., 15 diﬀerent technical indicators with a 15-days periods are used to construct a 15 × 15 sized 2D images in Sezer & Ozbayoglu (2018).

While the feature extraction techniques represented by technical analysis for market data have been used and validated for many years, the tools for extracting features from text data have made a greater progress in the past few years, owing to the various deep learning models developed for natural language processing. Before the popularity of machine learning models, the bag-of-words (BoW) model (Harris, 1954) is used as a representation of text that describes the occurrence of words within a document. In recent years, machine learning and deep learning models show an improved performance for word embedding. Given the sequence of words, the word2vec model (Mikolov et al., 2013), which are shallow and two-layer neural networks, can be used to embed each of these words in a vector of real numbers and has been used in Liu et al. (2019a,c); Lee & Soo (2017). Global Vectors for Word Representation (GloVe) (Pennington et al., 2014) is another word embedding method proposed by Stanford University, in which each of the word vectors has a dimension of 50, and has been used in Tang & Chen (2018).

Stock markets are highly aﬀected by some public events, which can be extracted from online news data and used as input features. Ding et al. (2015) uses a neural tensor network to learn event embeddings for representing news documents. Hu et al. (2018b) uses a news embedding layer to encode each news into a news vector. Wang et al. (2019b) uses a convolution neural network (CNN) layer to extract salient features from transformed event representations.

From sentiment aspect, the text data can be further analyzed and a sentiment vector can depict each word, which may present the positive or negative opinions for the future direction of stock prices. For sentiment analysis, Jin et al. (2019) uses CNN and Mohan et al. (2019) uses Natural Language Toolkit (NLTK) (Loper & Bird, 2002). Lien Minh et al. (2018) even proposes a sen-

timent Stock2Vec embedding model trained on both the stock news and the Harvard IV-4 psychological dictionary, which may not be directly related to stock market prediction.

Oﬀ-the-shelf commercial software is also available for linguistic features and sentiment analysis. For example, Kumar et al. (2019) employs Linguistic Inquiry and Word Count (LIWC) (Tausczik & Pennebaker, 2010) to ﬁnd out the linguistic features in the news articles, which includes the text analysis module along with a group of built-in dictionaries to count the percentage of words reﬂecting diﬀerent emotions, thinking styles, social concerns, and even parts of speech.

Distribution of Combinations of Input Features

Historical Prices

35.83%

Historical Prices+Technical Indicators

25.00%

0.83% Historical Prices+Image

0.83% Historical Prices+Macroeconomics

0.83%

Historical Prices+Fundamental+Knowledge Graph+Text

0.83%

0.83% Historical Prices+Fundamental+Text

0.83% Historical Prices+Knowledge Graph+Technical Indicators

1.67% Historical Prices+Knowledge Graph+Text

1.67% Historical Prices+Knowledge Graph

Historical Prices+Technical Indicators+Fundamental+Macroeconomics

3.33%

Image

3.33%

13.33%

5.00% Text

5.83%

Historical Prices+Text

Historical Prices+Technical Indicators+Text

Historical Prices+Technical Indicators+Macroeconomics

Figure 5: Distribution of combinations of input features.

For knowledge graph data used more recently, the TransE model (Bordes et al., 2013) is a computationally eﬃcient predictive model that satisfactorily represents a one-to-one type of relationship and has been used in Liu et al. (2019c).

Based on the input raw data and extracted features, we show the distribution

of diﬀerent combinations of input features in Figure 5 and the detailed article lists in Table 4. From Figure 5, historical prices and technical indicators are the most commonly used input features and followed by text and macroeconomics data. This could be explained by the easier accessing and processing of market data than other data types.

Table 4: Article Lists of combinations of input features.

Combination Article List Historical Prices Chen et al. (2019); Ding & Qin (2019); Zhou et al. (2019a); Nguyen et al. (2019); Yang et al. (2017); Li & Tam (2017); Li et al. (2017b); Sachdeva et al. (2019); Nikou et al.; Tsantekidis et al. (2017b); Liu & Chen (2019); Qin et al. (2017); Siami-Namini et al. (2019); Guang et al. (2019); Zhao et al. (2017); Althelaya et al. (2018); Baek & Kim (2018); Liang et al. (2019); Fischer & Krauss (2018); Pang et al. (2018); Tran et al. (2018); Tsantekidis

- et al. (2017a); Chen et al. (2018a); Wang et al. (2019a); Zhang et al. (2017b); Karathanasopoulos & Osman (2019); Hollis et al. (2018); Kim & Kang (2019); Cao & Wang (2019); Selvin et al.

- (2017); de A. Arajo et al. (2019); Wang & Wang

(2015); Zhang et al. (2019a, 2017a); Wu & Gao

- (2018); Long et al. (2019); Cao et al. (2019); Hossain et al. (2018); Eapen et al. (2019); Zhan

- et al. (2018); Lei (2018); Chong et al. (2017); Siami-Namini et al. (2018)

Continued on next page

Assis et al. (2018); Cheng et al. (2018); Nelson et al. (2017); Gunduz et al. (2017); Sanboon et al. (2019); Chen & Ge (2019); Stoean et al. (2019); Al-Thelaya et al. (2019); Yu & Wu (2019); Li et al. (2019a); Gao & Chai (2018); Chung & Shin (2018); Yan & Ouyang (2018); Sethia & Raut (2019); Sun et al. (2019); Zhang et al. (2019b); Chen et al. (2017); Zhou et al. (2018); Borovkova & Tsiamas (2019); Chen et al. (2019); Feng et al. (2019a); Sun et al. (2017); Yang et al. (2018); Ticknor (2013); Song et al. (2019); Gken et al. (2016); Singh & Srivastava (2017); Patel et al. (2015); Liu & Song

Indicators

- (2017); Merello et al. (2019)

Historical Prices + Text Jin et al. (2019); Li et al. (2019b); Liu et al.

- (2019a); Liu & Wang (2019); Wang et al.
- (2019b); Xu & Cohen (2018); Matsubara et al.

- (2018); Tang & Chen (2018); Huang et al.

(2018); Wu et al. (2018); Kumar et al. (2019); Li et al. (2017a); Tang et al. (2019); Huynh et al. (2017); Mohan et al. (2019); Hu et al. (2018a)

Historical Prices + Technical Indicators + Macroeconomics

Dingli & Fournier (2017); de Oliveira et al. (2013); Zhong & Enke (2017); Bao et al. (2017); Tsang et al. (2018); Hoseinzade & Haratizadeh (2019); Hoseinzade et al. (2019)

Continued on next page

Vargas et al. (2017); Liu et al. (2019c); Oncharoen & Vateekul (2018); Lien Minh et al.

Indicators + Text

(2018); Lee & Soo (2017); Chen et al. (2018b)

Text Liu et al. (2018); Hu et al. (2018b); Ding et al. (2015, 2014) Image Sezer & Ozbayoglu (2018); Sim et al. (2019);

Historical Prices + Technical Indicators + Fundamental + Macroeconomics

Historical Prices + Knowledge Graph

Historical Prices + Knowledge Graph + Text

Historical Prices + Knowledge Graph + Technical Indicators

Historical Prices + Fundamental data + Text

Historical Prices + Fundamental + Knowledge Graph + Text

Historical Prices + Macroeconomics

Lee et al. (2019); Sezer & Ozbayoglu (2019)

Ballings et al. (2015); Niaki & Hoseinzade

(2013)

Kim et al. (2019); Chen et al. (2018c)

Deng et al. (2019)

Matsunaga et al. (2019)

Tan et al. (2019)

Liu et al. (2019b)

Jiang et al. (2018)

Historical Prices + Image Kim & Kim (2019)

- 4.2.4. Dimensionality Reduction It is possible that many features are highly correlated with each other, e.g.,

the technical indicators which are all calculated from historical open/high/low/close

prices and volume. To alleviate the corresponding problem of deep learning model’s overﬁtting, dimensionality reduction for the input features has been adopted as a preprocessing technique for stock market prediction.

Principal component analysis (PCA) is a commonly used transformation technique that uses Singular Value Decomposition of the input data to project it to a lower dimensional space and has been used in Gao & Chai (2018); Zhang et al. (2019b); Zhong & Enke (2017); Wang & Wang (2015); Singh & Srivastava (2017); Chong et al. (2017). Zhong & Enke (2017) even gives a comparison between diﬀerent versions of PCA, and ﬁnds that the PCA-ANN model give a slightly higher prediction accuracy for the daily direction of SPY for next day, compared to the use of fuzzy robust principal component analysis (FRPCA) and kernel-based principal component analysis (KPCA).

For dimensionality reduction, the other options include independent components analysis (ICA) (Sethia & Raut, 2019), autoencoder (Chong et al., 2017), restricted Boltzmann machine (Chong et al., 2017), empirical mode decomposition (EMD) (Cao et al., 2019; Zhou et al., 2019a), and sub-mode coordinate algorithm (SMC) (Huang et al., 2018). Huang et al. (2018) ﬁrst utilizes tensor to integrate the multi-sourced data and further proposes an improved SMC model to reduce the variance of their subspace in each dimension produced by the tensor decomposition.

Feature selection is another way of dimensionality reduction, by choosing only a subset of input features. Chi-square method (Zheng et al., 2004) and maximum relevance and minimum redundancy (MRMR) (Peng et al., 2005) are two common used feature selection techniques. Chi-square method decides whether a categorical predictor variable and the target class variable are independent or not. High chi-squared values indicate the dependence of the target variable on the predictor variable. Minimum redundancy maximum relevance uses a heuristic to minimize redundancy while maximizing relevance to select promising features for both continuous and discrete inputs, through F-statistic values. Chi-square method is used in Gunduz et al. (2017); Kumar et al. (2019) and maximum relevance and minimum redundancy is used in Kumar et al.

(2019).

Other options for feature selection include rough set attribute reduction (RSAR) (Lei, 2018), autocorrelation function (ACF) and partial correlation function (PCF) (Wu & Gao, 2018), the analysis of variance (ANOVA) (Niaki & Hoseinzade, 2013), and maximal information coeﬃcient feature selection (MICFS) (Yang et al., 2018).

- 4.2.5. Feature Normalization & Standardization Given diﬀerent input features with varying scales, feature normalization and

standardization are used to guarantee that some machine learning models can work and also help to improve the model’s training speed and performance. Feature normalization refers to the process of rescaling the input feature by the minimum and range, to make all the values lie between 0 and 1 (Wang & Wang, 2015; Gunduz et al., 2017; Li et al., 2017b; Singh & Srivastava, 2017; Althelaya

- et al., 2018; Althelaya et al., 2018; Baek & Kim, 2018; Chen et al., 2018a; Chung & Shin, 2018; Gao & Chai, 2018; Hossain et al., 2018; Hu et al., 2018a; Lien Minh et al., 2018; Pang et al., 2018; Tang & Chen, 2018; Tsang et al., 2018; Yang et al., 2018; Zhan et al., 2018; Al-Thelaya et al., 2019; de A. Arajo et al.,

2019; Cao et al., 2019; Cao & Wang, 2019; Ding & Qin, 2019; Lee et al., 2019; Li et al., 2019b; Sachdeva et al., 2019; Sethia & Raut, 2019; Tang et al., 2019), or between -1 and 1 (Ticknor, 2013; Zhang et al., 2017b; Sezer & Ozbayoglu, 2018). Feature standardization means subtracting a measure of location and dividing by a measure of scale, e.g., the z-score method that subtracts the mean and divides by the standard deviation (Tsantekidis et al., 2017a,b; Zhang et al., 2019b; Li et al., 2019a).

- 4.2.6. Data Split For evaluation of diﬀerent prediction models, in-sample/out-of-sample split

or train/validation/test split of data samples is commonly used in machine learning and deep learning ﬁelds. The model is trained with the training or in-sample data set, the hyper-parameters is ﬁne-tuned on the validation data set optional,

and the ﬁnal performance is evaluated on the test or out-of-sample data set. k-fold cross validation is further used to split the dataset into k consecutive folds, and k-1 folds is used as the training set, while the last fold is then used as a test set.

As a special case, train-validation-test split with a rolling (or sliding, moving, walk-forward) window is also often used for time series tasks including stock prediction (Bao et al., 2017; Nelson et al., 2017; Fischer & Krauss, 2018; Gao & Chai, 2018; Zhou et al., 2018; Nguyen & Yoon, 2019; Kim et al., 2019; Sun

- et al., 2019; Wang et al., 2019a). The process of a rolling train-validation-test split is shown in Figure 6(a), where only the latest part of data samples are used for a new training round of prediction models. Another variant is to use successive training sets, which are union set of the rolling training set that come before them, as shown in Figure 6(b).

|| |
|---|
|
|---|

|| |
|---|
|
|---|

(a)

(b)

Figure 6: The example or rolling training-validation-test data splits. (a) Rolling training set; (b) Successive training set.

- 4.2.7. Data Augmentation Data augmentation techniques have been widely used for image classiﬁcation

and object detection tasks and proved to eﬀectively enhance the classiﬁcation and detection performance. However, it is less used for time series tasks including stock prediction, even though the size of stock price time series is not comparable to the size of public image datasets, which usually have millions of sample and even more in recent years.

There are still a few works that explore the usage of data augmentation. Zhang et al. (2017a) ﬁrstly clusters diﬀerent stocks based on their retracement probability density function and combines all the day-wise information of the same stock cluster as enlarged training data. In the ModAugNet framework proposed in Baek & Kim (2018), the authors choose 10 companies’ stock that are highly correlated to the stock index and augment the data samples by using the combinations of 10 companies taken 5 at a time in an overﬁtting prevention LSTM module, before feeding the data samples to a prediction LSTM module for stock market index prediction.

- 4.3. Prediction Model Most of the prediction models belong to a supervised learning approach,

when training set is used for the training and test set is used for evaluation. Only a few of the studies use semi-supervised learning when the labels are not available in the feature extraction step. We further classify the various prediction models into three types: standard models and their variants, hybrid models, and other models. For standard models, three families of deep learning models, namely, feedforward neural network, convolutional neural network and recurrent neural network, are used a lot. And we category the use of generative adversarial network, transfer learning, and reinforcement learning into other models. These models only appear in recent years and are still in an early stage of being applied for stock market prediction.

In this part, we are focusing on the usage of diﬀerent types of deep learning models, instead of diving into the details of each model. For a more detailed introduction to deep learning models, we refer the readers to Goodfellow et al. (2016). The abbreviations of machine learning and deep learning methods are shown in Table 5.

Table 5: Abbreviations of machine learning and deep learning methods.

Abbreviation Full Name Preprocessing Techniques BoF Bag-of-feature BoW Bag-of-words CEAM Cycle Embeddings with Attention Mechanism CEEMDAN Complete Ensemble Empirical Mode Decomposition with Adap-

tive Noise EMD Empirical Mode Decomposition MACD Moving Average Convergence / Divergence MOM Momentum N-BoF Neural Bag-of-Feature PCA Principal Components Analysis RS Rough Set RSI Relative Strength Index SMA Simple Moving Average SMC Sub-mode Coordinate Algorithm WT Wavelet Transform (2D)2PCA 2-Directional 2- Dimensional Principal Component Analysis Optimization Algorithms HM Harmony Memory GA Genetic Algorithm ISCA Improved Sine Cosine Algorithm GWO Grey Wolf Optimizer PSO particle swarm optimization WOA Whale Optimization Algorithm SCA Sine Cosine Algorithm

Continued on next page

Linear Models AR Autoregressive ARMA Autoregressive Moving Average ARIMA Autoregressive Integrated Moving Average EMA Estimated Moving Average GARCH Generalized Autoregressive Conditional Heteroskedasticity LDA Linear Discriminant Analysis LR Linear Regression PLR Piecewise Linear Regression MA Moving Average MR Mean Reversion MCSDA Multilinear Class-speciﬁc Discriminant Analysis MDA Multilinear Discriminant Analysis MTR Multilinear Time-series Regression WMTR Weighted Multilinear Time-series Regression Machine Learning Models AB AdaBoost ANFIS Adaptive Neuro-fuzzy Inference System kNN k-Nearest neighbor Lasso Lasso Regression Logit Logistics Regression MKL Multiple Kernel Learning MRFs Markov Random Fields RF Random Forest Ridge Ridge Regression SVM Support Vector Machine SVR Support Vector Regression

Continued on next page

Deep Learning Models AE Autoencoder ANN Artiﬁcial Neural Network BGRU Bidirectional GRU BiLSTM bi-directional long short-term memory BPNN Backpropagation Neural Network CapTE Capsule network based Transformer Encoder CF-DA-RNN DA-RNN with cycle value CH-RNN Cross-modal Attention based Hybrid Recurrent Neural Network CNN Convolutional Neural Network DA-RNN Dual-Stage Attention-Based RNN DBN Deep Belief Network DEM Dilation-erosion Model DGM Deep Neural Generative Model DIDLNN Deep Increasingdecreasing-linear Neural Network DMN Dendrite Morphological Neuron DNN Deep Neural Network ELM Extreme Learning Machines eLSTM Tensor-based Event-LSTM EMD2FNN Empirical Mode Decomposition and Factorization Machine

based Neural Network EMD2NN Empirical Mode Decomposition based Neural Network FDNN Fuzzy Deep Neural Network FFNN Feedforward Neural Network FNN Factorization Machine based Neural Network GAN Generative Adversarial Network GCNN Graph Convolutional Neural network

Continued on next page

GNN Graph Neural Network GRU Gated Recurrent Unit HAN Discriminative Deep Neural Network with Hierarchical Atten-

tion HCAN Hierarchical Complementary Attention Network HGAN Hierarchical Graph Attention Network KDTCN Knowledge-Driven Temporal Convolutional Network LNNN Linear and Nonlinear Neural Network LSTM Long Short Term Memory MAFN Multi-head Attention Fusion Network MGU Minimal Gated Unit MLP Multilayer Perceptron MS-CNN Multi-Scale CNN MSTD-RCNN Multi-Scale Temporal Dependent Recurrent Convolutional Neu-

ral Network NARXT Nonlinear Autoregressive Neural Network with Exogenous Tak-

ens Inputs NN Neural Network PELMNN Prediction Evolutionary Levenberg-marquardt Neural Networks RBFNN Radial Basis Function Neural Network RBM Restricted Boltzmann Machines RNN Recurrent Neural Network SAEs Stacked Autoencoders SFM State Frequency Memory SRCGUs Selective Recurrent Neural Networks with Random Connectiv-

ity Gated Unit STNN Stochastic Time Eﬀective Function Neural Network Continued on next page

TABL Temporal Attention Augmented Bilinear Layer TGC Temporal Graph Convolution TSLDA Generative Topic Model Jointly Learning Topics and Sentiments WMN Wavelet Neural Network WDBPNN Wavelet De-noising based BPNN 1D CNN One-dimensional Convolutional Neural Networks

Some of the earlier work use ANNs as their prediction models and study the eﬀect of diﬀerent combinations of input features (Niaki & Hoseinzade, 2013; de Oliveira et al., 2013; Zhong & Enke, 2017). In this survey, we use ANN to refer to the neural networks which only have one or zero hidden layers, and DNN to refer to those which have two or more hidden layers. The list of standard models or their variants is shown in Table 6. We organize the standard models into three major types:

- • Feedforward neural network (FFNN). It is the simplest type of artiﬁcial neural network wherein connections between the nodes do not form a cycle. An artiﬁcial neural networks (ANN) are learning models inspired by biological neural networks, and the neuron in an ANN consists of an aggregation function which calculates the sum of the inputs, and an activation function which generates the outputs. An autoencoder (AE) is a subset of ANN which has the same number of nodes in the input and output layers. When ANN has two or more hidden layers, we denote it as deep neural network (DNN) is this survey. We also category the following models into this family because they share a similar structure: backpropagation neural network (BPNN), multilayer perceptron (MLP), extreme learning machines (ELM) where the parameters of hidden nodes need not be tuned, deep increasingdecreasing-linear neural network (IDLNN) where

- each layer is composed of a set of increasingdecreasing-linear processing units (de A. Arajo et al., 2019), stochastic time eﬀective function neural network (STEFNN) (Wang & Wang, 2015), radial basis function network (RBFN) that uses radial basis functions as activation functions.
- • Convolutional neural network (CNN). Designed for processing two-dimensional images, each group of neurons, which is also called a ﬁlter, performs a convolution operation to a diﬀerent region of the input image and the neurons share the same weights, which reduces the number of parameters compared to the densely connected feedforward neural network. Pooling operations, e.g., max pooling, are used to reduce the original size and can be used for multiple times, until the ﬁnal output is concatenated to a dense layer. Powered by the parallel processing ability of graphics processing unit (GPU), the training of CNN has been shortened and CNN has achieved an astonishing performance for image related tasks and competitions. By reducing the convolutional and pooling operations to a single temporal dimension, 1D CNN is proposed for time series classiﬁcation and prediction, e.g., Deng et al. (2019) uses a 1-D fully-convolutional network (FCN) architecture, where each hidden layer has the same length as the input layer, and zero padding is added to keep subsequent layers the same length as previous ones.
- • Recurrent neural network (RNN). Compared with feedforward neural network, recurrent neural network is an artiﬁcial neural network wherein connections between the nodes form a cycle along a temporal sequence, which helps it to exhibit temporal dynamic behavior. However, normal RNNs are bothered by the vanishing gradient problem in practice, when the gradients of some of the weights start to shrink or enlarge if the network is unfolded too many times. Long short-term memory (LSTM) networks are RNNs that solve the vanishing gradient problem, where the hidden layer is replaced by recurrent gates called forget gates. Gated recurrent unit (GRU) is another RNN that uses forget gates, but has fewer parameters

than LSTM. Bi-directional RNN are RNNs that connect two hidden layers of opposite directions to the same output. Both bi-directional LSTM (BiLSTM) and bi-directional GRU (BGRU) have been used for stock market prediction.

While standard models perform well at early stages of research, their variants are further developed to improve the prediction performance. One approach is to use stacked models, where neural network sub-models are embedded in a larger stacking ensemble model for training and prediction. Another approach is to introduce the attention mechanism (Treisman & Gelade, 1980) into recurrent neural network models, in which attention is a generalized pooling method with bias alignment over inputs.

There are also some types that we list separately:

- • Restricted Boltzmann machine (RBM) is a generative stochastic artiﬁcial neural network that can learn a probability distribution over its set of inputs. And a deep belief network (DBN) can be deﬁned as a stack of RBMs. DBNs have been used in Li et al. (2017b); Karathanasopoulos & Osman (2019) for stock prediction.
- • Sequence to sequence (seq2seq) model is based on the encoder-decoder architecture to generate a sequence output for a sequence input, in which both the encoder and the decoder use recurrent neural networks. Seq2seq model has been used in Liu & Wang (2019) for stock prediction.

While our focus in this survey is not the linear models or the traditional machine learning models, they are often used as baselines for comparison with deep learning models.

Some often used linear prediction models are as follows:

- • Linear regression (LR). Linear regression is a classical linear model that tries to ﬁt the relationship between the predicted target and the input variables with a linear model, in which the parameters can be learned in the least squares approach.

- • Autoregressive integrated moving average (ARIMA). ARIMA is a generalization of the autoregressive moving average (ARMA) model, which describes a weakly stationary stochastic process with two parts, namely, the autoregression (AR) and the moving average (MA). Compared with ARMA, ARIMA is capable of dealing with non-stationary time series, by introducing an initial diﬀerencing step, which is referred as the integrated part in the model.
- • Generalized autoregressive conditional heteroskedasticity (GARCH). GARCH is also a generation of the autoregressive conditional heteroscedasticity (ARCH) model, which describes the error variance as a function of the actual sizes of the previous time periods’ error terms. Instead of using AR model in ARCH, GARCH assumes an ARMA model for the error variance, which generalizes ARCH.

Similarly, some often used machine learning models are as follows:

- • Logistics regression (Logit). Logistics regression can be seen as a generalized linear model, in which a logistic function is used to model the probabilities of a binary target of being 0 or 1. It is suitable for the classiﬁcation of price movements, e.g., going up or down.
- • Support vector machine/regression (SVM/SVR). Support vector machine is a classical and powerful tool for classiﬁcation with a good theoretical performance guarantee and has been widely adopted before the popularity of deep learning models. SVM tries to learn a hyperplane to distinguish the training samples that maximize distance of the decision boundary from training samples. Combine with the kernel trick, which maps the input training samples into high-dimensional feature spaces, SVM can eﬃciently perform non-linear classiﬁcation tasks. Support vector regression is the regression version of SVM.
- • k-nearest neighbor (kNN). kNN is a non-parametric model for both classiﬁcation and regression, in which the output is the class most common or

the average of the values among k nearest neighbors. A useful technique is to assign weights to the neighbors when combing their contributions.

Given the predicted movement direction or prices, a long-short strategy can be further designed to perform trading based on the prediction model, e.g., if the predicted direction is going up, long it, otherwise short it. A simple baseline is the Buy&Hold Strategy, which buys the asset at the beginning and hold it to the end of the testing period, without any further buying or selling operations (Niaki & Hoseinzade, 2013; Sezer & Ozbayoglu, 2018).

Technical indicators are also often used for designing baseline trading strategies, e.g., momentum strategy, which is introduced in Jegadeesh & Titman (1993), is a simple strategy of buying winners and selling losers. MACD (Appel & Dobson, 2007) consists of the MACD line and the signal line, and the most common MACD strategy buys the stock when the MACD line crosses above the signal line and sells the stock when the MACD line crosses below the signal line (Lee et al., 2019). In our surveyed papers, RSI (14 days, 70-30) and SMA (50 days) are used to design baseline trading strategies (Sezer & Ozbayoglu, 2018).

Table 6: List of standard models or their variants.

Article Prediction Model Baselines Feedforward Neural Network Type de Oliveira et al. (2013) ANN N/A Niaki & Hoseinzade

ANN Logit, Buy&Hold Strategy

(2013)

Ticknor (2013) DNN ARIMA

- Ding et al. (2014) DNN SVM
- Ding et al. (2015) DNN BoW+SVM, structed event tuple+ANN

Wang & Wang (2015) PCA+STNN BPNN, PCA+BPNN, STNN Continued on next page

Gken et al. (2016) HM-ANN ANN, GA-ANN Chen et al. (2017) DNN ARMA-GARCH, ARMAX-

GARCH, ANN Chong et al. (2017) DNN AR Singh & Srivastava

(2D)2PCA+RBFNN RBFNN, RNN

(2017)

Sun et al. (2017) Stacked Denoising Autoencoder

SVM, Logit, ANN

Zhong & Enke (2017) PCA+ANN N/A Hu et al. (2018a) ISCABPNN BPNN, GWO-BPNN, PSO-

BPNN, WOA-BPNN, SCABPNN

de A. Arajo et al. (2019) DIDLNN ARIMA, SVM, MLP, LNNN (Yolcu et al., 2013), DEM (Arau´jo, 2011), DMN (Zamora & Sossa, 2017), NARXT (Menezes Jr & Barreto, 2008), PELMNN (Asadi et al., 2012)

Song et al. (2019) DNN DNN Convolutional Neural Network Type Dingli & Fournier

CNN Logit, SVM

- (2017)

Gunduz et al. (2017) CNN Logit Selvin et al. (2017) 1-D CNN RNN, LSTM, ARIMA Tsantekidis et al.

CNN SVM, MLP

- (2017a)

Continued on next page

Sezer & Ozbayoglu

- (2018)

CNN Buy&Hold Strategy, RSI (14 days, 70-30), SMA (50 days), LSTM and MLP

Yang et al. (2018) multichannel CNN SVM, ANN, CNN Hoseinzade & Haratizadeh (2019)

CNN PCA+ANN (Zhong & Enke, 2017), ANN (Kara et al., 2011), CNN (Gunduz et al., 2017)

Cao & Wang (2019) 1-D CNN DNN, SVM Deng et al. (2019) KDTCN ARIMA, LSTM, CNN, TCN Sezer & Ozbayoglu

- (2019)

CNN Buy&Hold

Sim et al. (2019) CNN ANN, SVM Recurrent Neural Network Type Huynh et al. (2017) BGRU LSTM, GRU, DNN (Ding et al.,

2014), DNN (Peng & Jiang, 2016)

Li & Tam (2017) WT+LSTM LSTM

- Li et al. (2017a) LSTM SVM Nelson et al. (2017) LSTM MLP, RF

Tsantekidis et al.

- (2017b)

LSTM SVM, MLP

- Zhang et al. (2017a) GRU SVM
- Zhang et al. (2017b) SFM AR, LSTM Zhao et al. (2017) LSTM RNN, SVM, RF, AB Althelaya et al. (2018) bidirectional and

ANN, LSTM

stacked LSTM

Continued on next page

Althelaya et al. (2018) Stacked LSTM BiLSTM, BGRU, Stacked

GRU, MLP Baek & Kim (2018) LSTM DNN, RNN Cheng et al. (2018) Attention LSTM N/A Chung & Shin (2018) GA+LSTM N/A Fischer & Krauss

LSTM RF, DNN, Logit

- (2018)

Gao & Chai (2018) LSTM MA, EMA, ARMA, GARCH,

SVM, FFNN, and LSTM Hollis et al. (2018) Attention LSTM LSTM Huang et al. (2018) SMC+LSTM SVM, PCA+SVM, TeSIA (Li

et al., 2016a), SMC+TeSIA Jiang et al. (2018) RNN with attention RNN

- Liu et al. (2018) HCAN BoW (Joachims, 1998), FastText (Joulin et al., 2017), Structured-Event (Ding et al., 2014), IAN (Ma et al., 2017)

Lien Minh et al. (2018) two-stream GRU LSTM, GRU Siami-Namini et al.

LSTM ARIMA

- (2018)

Tsang et al. (2018) LSTM WT+SAEs+LSTM (Bao et al., 2017)

Xu & Cohen (2018) StockNet Random Guess, ARIMA, RF, TSLDA (Nguyen & Shirai, 2015), HAN (Hu et al., 2018b)

Yan & Ouyang (2018) WT+LSTM MLP, SVM, kNN Continued on next page

Borovkova & Tsiamas

stacked LSTM Lasso, Ridge

- (2019)

Cao et al. (2019) EMD+LSTM, CEEMDAN+LSTM

LSTM, SVM, MLP

Chen & Ge (2019) Attention LSTM LSTM Chen et al. (2019) EMD-Attention LSTM MLP, LSTM, EMD-LSTM, At-

tention LSTM Ding & Qin (2019) LSTM RNN, LSTM Feng et al. (2019a) Adversarial Attentive

MOM, MR, StockNet (Xu & Cohen, 2018), LSTM (Nelson et al., 2017), Attentive RNN (Qin et al., 2017)

LSTM

Liang et al. (2019) WT+LSTM LSTM

- Liu et al. (2019b) GRU N/A Kim & Kang (2019) weighted LSTM with

MLP, 1D CNN, stacked LSTM, LSTM with attention

Attention

Mohan et al. (2019) LSTM ARIMA, Facebook Prophet,

LSTM Nguyen et al. (2019) Dynamic LSTM LSTM Nikou et al. LSTM ANN, SVM, RF Sachdeva et al. (2019) LSTM N/A Sanboon et al. (2019) LSTM SVM, MLP, DT, RF, Logit,

kNN Sethia & Raut (2019) LSTM GRU, ANN, SVM Siami-Namini et al.

BiLSTM LSTM, ARIMA

- (2019)

Continued on next page

Tan et al. (2019) eLSTM SVM, DT, ANN, LSTM, AZFin Text (Schumaker & Chen, 2009), TeSIA (Li et al.,

- 2016a)

Tran et al. (2018) TABL Ridge, FFNN, LDA, MDA, MTR, WMTR (Tran et al., 2017b), MCSDA (Tran et al.,

- 2017a), BoF, N-BoF (Passalis et al., 2017), SVM, MLP, CNN (Tsantekidis et al., 2017a), LSTM (Tsantekidis et al., 2017b)

Wang et al. (2019b) BiLSTM Random guess, ARIMA, SVM,

MLP, HAN (Hu et al., 2018b) Other Types

- Li et al. (2017b) DBN N/A Matsubara et al. (2018) DGM SVM, MLP Liu & Wang (2019) seq2seq model with at-

AZFin Text (Schumaker & Chen, 2009), DL4S (Akita

tention

- et al., 2016), DA-RNN (Qin
- et al., 2017), MKL, ELM (Li et al., 2016b)

Karathanasopoulos & Osman (2019)

DBN MACD, ARMA

We further categories the hybrids into two classes, namely, the hybrid models between deep learning models and traditional models, and the hybrid models

between diﬀerent deep learning models.

The list of hybrid models between deep learning models and traditional models is shown in Table 7. Li et al. (2019b) formulates a sentiment-ARMA model to incorporate the news articles as hidden information and designs a LSTM-based DNN, which consists of three components, namely, LSTM, VADER model and diﬀerential privacy mechanism that integrates diﬀerent news sources. To deal with strong noise, Liu & Song (2017) uses weak ANNs to get some information without over-ﬁtting and get better results by combining the weak results together using optimized bagging. Wu & Gao (2018) uses AdaBoost algorithm to generate both training samples and ensemble weights for each LSTM predictor and the ﬁnal prediction results are the combination of all the LSTM predictors with ensemble weights.

Table 7: List of hybrid models between deep learning models and traditional models.

Article Prediction Model Baselines Patel et al. (2015) SVRANN SVR-RF, SVR-SVR Liu & Song (2017) Bagging+ANN SVM, ANN, GA-ANN, RF Yang et al. (2017) Bagging+ANN N/A Assis et al. (2018) RBM+SVM SVM

- Chen et al. (2018b) RNN+AdaBoost MLP, SVR, RNN Lei (2018) 2RS-WNN BP-NN, RBF-NN, ANFIS-NN,

SVM, WNN, RS-WNN

Wu & Gao (2018) AB-LSTM ARIMA, MLP, SVR, ELM, LSTM, AB-MLP, AB-SVR, AB-ELM

- Chen et al. (2019) PLR+CNN+Dual Attention Mechanism based Encoder-Decoder

SVR, LSTM, CNN, LSTM CNN (Lin et al., 2017), TPM NC

Continued on next page

Table 7 – continued from previous page Article Prediction Model Baselines Li et al. (2019b) LSTM+ARIMA LSTM Li et al. (2019a) RNN with high-order

LSTM, attention based LSTM Encoder-Decoder (Bahdanau et al., 2014), DA-RNN (Qin et al., 2017)

MRFs

Sun et al. (2019) ARMA-GARCH-NN DNN, LSTM Zhou et al. (2019a) EMD2FNN ANN, FNN, EMD2NN,

WDBPNN (Wang et al., 2011), Long-short Strategy

The list of hybrid models between diﬀerent deep learning models is shown in Table 8. Two popular combinations are the combination of CNN and RNN structures and the combination of diﬀerent RNNs.

For the former case, TreNet (Lin et al., 2017) hybrids LSTM and CNN for stock trend classiﬁcation. Zhang et al. (2019b) proposes a deep learning model, comprising three main building blocks that include a standard convolutional layer, an Inception Module and a LSTM layer. Guang et al. (2019) uses convolutional units to extract multi-scale features that precisely describe the state of the ﬁnancial market and capture temporal, and uses a recurrent neural network to capture the temporal dependency and complementary across diﬀerent scales.

For the latter case, Al-Thelaya et al. (2019) proposes a forecasting model, using a combination of LSTM autoencoder and stacked LSTM network. Wang et al. (2019a) proposes a hybrid model, consisting of stochastic recurrent networks, the sequence-to-sequence architecture, the self- and inter-attention mechanism, and convolutional LSTM units. Liu & Chen (2019) proposes an elective Recurrent Neural Networks with Random Connectivity Gated Unit (SRCGUs) that train random connectivity LSTMs, GRUs and MGUs simultaneously.

Table 8: List of hybrid models between diﬀerent deep learning models.

Article Prediction Model Baselines Bao et al. (2017) WT+SAEs+LSTM WT+LSTM, LSTM, RNN Lee & Soo (2017) RNN+CNN LSTM Qin et al. (2017) DA-RNN ARIMA, NARX RNN (Diaconescu, 2008), EncoderDecoder (Cho et al., 2014), attention based LSTM EncoderDecoder (Bahdanau et al., 2014)

Vargas et al. (2017) CNN+LSTM DNN (Ding et al., 2014, 2015),

CNN (Ding et al., 2015) Chen et al. (2018a) DNN+AE+RBM ANN, ELM, RBFNN Hossain et al. (2018) LSTM+GRU MLP, RNN, CNN Hu et al. (2018b) Hybrid Attention Net-

RF, MLP, GRU, BGRU, Temporal-Attention-RNN, News-Attention-RNN

works

Oncharoen & Vateekul

CNN+LSTM N/A

(2018)

Pang et al. (2018) AE+LSTM DBN, MLP, DBN+MLP Tang & Chen (2018) CNN+LSTM LSTM, FFNN, CNN Wu et al. (2018) CH-RNN DA-RNN (Qin et al., 2017) Zhan et al. (2018) 1D CNN+LSTM LSTM, GRU Al-Thelaya et al. (2019) LSTM AE+stacked

LSTM, MLP

LSTM

Eapen et al. (2019) CNN+BiLSTM SVR

Continued on next page

Table 8 – continued from previous page Article Prediction Model Baselines Guang et al. (2019) MSTD-RCNN SVM, RF, FDNN, TreNet (Lin et al., 2017), SFM RNN (Hu & Qi, 2017), MS-CNN (Cui et al., 2016)

Jin et al. (2019) CNN+LSTM+Attention LSTM Kim & Kim (2019) CNN+LSTM CNN, LSTM Liu & Chen (2019) SRCGUs MGUs, GRUs and LSTMs Long et al. (2019) CNN+RNN RNN, LSTM, CNN, SVM,

Logit, RF, LR

Tang et al. (2019) MAFN MA, RF, XGBoost, SVR, Adversarial Attentive LSTM (Feng et al., 2019a), HAN (Hu et al., 2018b), StockNet (Xu & Cohen, 2018)

Wang et al. (2019a) A Convolutional LSTM Based Variational Seq2seq Model with Attention

CNN, LSTM, seq2seq model with attention

Yu & Wu (2019) CEAM+DA-RNN DA-RNN (Qin et al., 2017), CFDA-RNN Zhang et al. (2019b) CNN+LSTM SVM, MLP, CNN (Tsantekidis et al., 2017a)

We list other types of models in Table 9. We category ﬁve types of models in this part, which have not been fully explored for stock market prediction but already show some promising results.

- • Generative adversarial network (GAN). GAN is introduced by Goodfellow

- et al. (2014), in which a discriminative net D learns to distinguish whether a given data instance is real or not, and a generative net G learns to confuse D by generating high quality fake data. This game between G and D would lead to a Nash equilibrium. Since the introduction of GAN, it has been applied in multiple image-related tasks, especially for image generation and enhancement, and generates a large family of variants. Inspired the success of GANs, Zhou et al. (2018) proposes a generic GAN framework employing LSTM and CNN for adversarial training to predict high-frequency stock market.
- • Graph neural network (GNN). GNN is designed to utilize graph-structured data, thus capable of utilizing the network structure to incorporate the interconnectivity of the market and make better predictions, compared to relying solely on the historical stock prices of each individual company or on hand-crafted features (Matsunaga et al., 2019). Chen et al. (2018c) ﬁrst constructs a graph including 3,024 listed companies based on investment facts from real market, then learns a distributed representation for each company via node embedding methods applied on the graph, and applies three-layer graph convolutional networks to predict. Kim et al.

(2019) uses LSTM for the individual stock prediction task and GRU for the index movement prediction task where an additional graph pooling layer is needed.

- • Capsule Network. Diﬀerent from the method of CNNs and RNNs, the capsule network increases the weights of similar information through its dynamic routing, which is proposed by Sabour et al. (2017) and displaces the pooling operation used in conventional convolution neural network. Liu et al. (2019a) is the ﬁrst to introduce the capsule network for the problem of stock movements prediction based on social media and show that the capsule network is eﬀective for this task.
- • Reinforcement learning. Unlike supervised learning, reinforcement learning trains an agent to choose the optimal action given a current state, with

- the goal to maximize cumulative rewards in the training process. Reinforcement learning can be applied for stock prediction with the advantage of using information from not only the next time step but from all subsequent time steps (Lee et al., 2019). Reinforcement learning is also used for building algorithmic trading systems (Deng et al., 2016).
- • Transfer learning. Transfer learning can be used in training deep neural networks with a small amount of training data and a reduced training time, by tuning the pre-trained model on a larger training dataset, e.g., Nguyen & Yoon (2019) trains a LSTM base model on 50 stocks and transfers parameters for the prediction model on KOSPI 200 or S&P 500.

Table 9: List of other types of models.

Article Prediction Model Baselines Generative Adversarial Network Zhou et al. (2018) GAN ARIMA-GARCH, ANN, SVM Zhang et al. (2019a) GAN LSTM, ANN, SVM Graph Neural Network Chen et al. (2018c) GCNN LR, LSTM Feng et al. (2019b) TGC SFM RNN (Zhang et al.,

2017b), LSTM

Kim et al. (2019) HGAN MLP, CNN, LSTM, GCNN (Chen et al., 2018c), TGC (Feng et al., 2019b)

Matsunaga et al. (2019) GNN LSTM Capsule Network

Continued on next page

Table 9 – continued from previous page Article Prediction Model Baselines Liu et al. (2019a) CapTE TSLDA (Nguyen & Shirai, 2015), HAN (Hu et al., 2018b), HCAN (Xu & Cohen, 2018), CH-RNN (Wu et al., 2018)

Reinforcement Learning Lee et al. (2019) Deep Q-Network+CNN FC network, CNN, and LSTM,

momentum, MACD

Transfer Learning Hoseinzade et al. (2019) Transfer Learn-

PCA+ANN (Zhong & Enke, 2017), ANN (Kara et al., 2011), CNN (Gunduz et al., 2017), CNN (Hoseinzade & Haratizadeh, 2019)

ing+CNN

Nguyen & Yoon (2019) Transfer Learning+LSTM

SVM, RF, KNN, LSTM (Fischer & Krauss, 2018)

We show the change trend of models used in the past three years in Figure 7. RNN Models are used for the most, but the ratio drops with the emerging new models in 2019. We also show the change of common optimizers used in our surveyed papers in Figure 8, which include Adam (Kingma & Ba, 2014), stochastic gradient descent (SGD), RMSprop (Tieleman & Hinton, 2012), AdaDelta (Zeiler, 2012). Adam has been used the most for stock prediction, which is a combination of RMSprop and stochastic gradient descent with momentum and presents several beneﬁts, e.g., computationally eﬃciency and little memory requirement.

For the baselines used in the survey studies, both linear, machine learning and deep learning models are covered. The change of baseline models used is

| | | |
|---|---|---|
| | | |
| | | |

| |
|---|

| |
|---|

| |
|---|

| | | |
|---|---|---|
| | | |
| | | |

Figure 7: The usage of diﬀerent models.

shown in Figure 9. With the further exploration of deep learning models for stock prediction, their ratio as baselines keeps increasing in the past three years.

- 4.4. Model Evaluation In this part, we category the evaluation metrics for the prediction models

mentioned in the last part into four types:

- • Classiﬁcation metrics. Classiﬁcation metrics are used to measure the model’s performance on movement prediction, which is modeled as a classiﬁcation problem. Common used metrics include accuracy (which is the correct number of prediction for directional change), precision, recall, sensitivity, speciﬁcity, F1 score, macro-average F-score, Matthews correlation coeﬃcient (which is a discrete case for Pearson correlation coeﬃcient), average AUC score (area under Receiver Operating Characteristic

| |
|---|

| |
|---|

Figure 8: The usage of diﬀerent optimizers.

curves (Fawcett, 2006)), Theil’s U coeﬃcient, hit ratio, average relative variance, etc. Confusion matrices and boxplots for daily accuracy are also used for classiﬁcation performance analysis (Guang et al., 2019; Zhong & Enke, 2017; Zhang et al., 2019b).

- • Regression metrics. Regression metrics are used to measure the model’s performance on stock/index price prediction, which is modeled as a regression problem. Common used metrics include mean absolute error (MAE), root mean absolute error (RMAE), mean squared error (MSE), normalized MSE (NMSE), root mean squared error (RMSE), relative RMSE, normalized RMSE (NRMSE), mean absolute percentage error (MAPE), root mean squared relative error (RMSRE), mutual information, R2 (which is the coeﬃcient of determination).

| |
|---|

| |
|---|

| |
|---|

| | | |
|---|---|---|
| | | |

Figure 9: The usage of diﬀerent baselines.

- • Proﬁt Analysis. Proﬁt analysis evaluates whether the predicted-based trading strategy can bring a proﬁt or not. It is usually evaluated from two aspects, the return and the risk. The return is the change in value on the stock portfolio and the risk can be evaluated by maximum drawdown (Zhou et al., 2019a), which is the largest peak-to-trough decline in the value of a portfolio and represents the max possible loss, or the annualized volatility(Karathanasopoulos & Osman, 2019). Sharpe Ratio is a comprehensive metric with both the return and risk into consideration, which is the average return earned in excess of the risk-free per unit of volatility (Sharpe, 1994). More detailed analysis about the transactions is given in Sezer & Ozbayoglu (2018, 2019).
- • Signiﬁcance Analysis. In order to determine if there is signiﬁcant diﬀer-

ence in terms of predictions when comparing the deep learning models to the baselines, Kruskal-Wallis (Kruskal & Wallis, 1952) and DieboldMariano (Diebold & Mariano, 2002) tests can be used to test the statistical signiﬁcance, which decides a statistically better model. They are not used often for stock prediction, with only a few studies in 2019 (Kumar et al., 2019; Zhang et al., 2019b).

The detailed list of studies using each metrics (as well as the metrics’ abbreviations) is shown in Table 10.

Table 10: Article Lists archived by diﬀerent evaluation metrics.

Metrics Article List Classiﬁcation Metrics

Continued on next page

Accuracy de Oliveira et al. (2013); Niaki & Hoseinzade (2013); Ding et al. (2014, 2015); Chen et al. (2017); Dingli & Fournier (2017); Huynh et al. (2017); Li & Tam (2017); Liu & Song (2017); Nelson et al. (2017); Selvin et al. (2017); Singh & Srivastava (2017); Sun et al. (2017); Vargas

- et al. (2017); Weng et al. (2017); Yang et al.

- (2017); Zhang et al. (2017a); Zhao et al. (2017); Assis et al. (2018); Chen et al. (2018a,c,b); Cheng et al. (2018); Fischer & Krauss (2018); Gao & Chai (2018); Hu et al. (2018b); Huang

et al. (2018); Liu et al. (2018); Liu & Wang (2019); Matsubara et al. (2018); Lien Minh

- et al. (2018); Oncharoen & Vateekul (2018); Pang et al. (2018); Sezer & Ozbayoglu (2018); Tang & Chen (2018); Tran et al. (2018); Wu

- et al. (2018); Yang et al. (2018); Zhou et al.

(2018); de A. Arajo et al. (2019); Chen & Ge (2019); Deng et al. (2019); Feng et al. (2019a); Guang et al. (2019); Karathanasopoulos & Osman (2019); Lee et al. (2019); Li et al. (2019b,a); Liu et al. (2019b,a); Long et al. (2019); Merello

- et al. (2019); Nguyen & Yoon (2019); Sanboon

- et al. (2019); Song et al. (2019); Sun et al.

(2019); Tan et al. (2019); Tang et al. (2019); Wang et al. (2019b)

Continued on next page

Precision Gunduz et al. (2017); Li et al. (2017a); Nelson et al. (2017); Tsantekidis et al. (2017a,b); Cheng et al. (2018); Lien Minh et al. (2018); Tran et al. (2018); Sezer & Ozbayoglu (2018); Li et al. (2019a); Wang et al. (2019a); Zhang et al. (2019b) Recall Gunduz et al. (2017); Li et al. (2017a); Nelson et al. (2017); Tsantekidis et al. (2017a,b); Cheng et al. (2018); Lien Minh et al. (2018); Tran et al. (2018); Sezer & Ozbayoglu (2018); Li et al. (2019a); Zhang et al. (2019b)

Sensitivity Sim et al. (2019) Speciﬁcity Sim et al. (2019) F1 score (F1) Gunduz et al. (2017); Li et al. (2017a); Nelson

et al. (2017); Sun et al. (2017); Tsantekidis et al. (2017a,b); Zhang et al. (2017a); Cheng et al. (2018); Jiang et al. (2018); Sezer & Ozbayoglu (2018); Tran et al. (2018); Deng et al. (2019); Guang et al. (2019); Li et al. (2019a); Wang et al. (2019b); Zhang et al. (2019b)

Macro-average F-score (MAFS) Hoseinzade & Haratizadeh (2019); Hoseinzade et al. (2019)

Matthews Correlation Coeﬃcient (MCC)

Ding et al. (2014, 2015); Singh & Srivastava (2017); Huang et al. (2018); Matsubara et al. (2018); Tsang et al. (2018); Cao & Wang (2019); Feng et al. (2019a); Liu et al. (2019a); Merello et al. (2019); Tan et al. (2019); Tang et al. (2019)

Continued on next page

Average AUC Score (AUC) Ballings et al. (2015); Jiang et al. (2018); Borovkova & Tsiamas (2019); Zhang et al. (2019b)

Theil’s U Coeﬃcient (Theil’s U) de Oliveira et al. (2013); Bao et al. (2017); Yan & Ouyang (2018); de A. Arajo et al. (2019) Hit Ratio (Hit) Singh & Srivastava (2017); Hu et al. (2018a); Sim et al. (2019)

Average Relative Variance (ARV)

de A. Arajo et al. (2019)

Regression Metrics Mean Absolute Error (MAE) Patel et al. (2015); Chong et al. (2017); Li

- et al. (2017b); Qin et al. (2017); Althelaya
- et al. (2018); Althelaya et al. (2018); Baek & Kim (2018); Chen et al. (2018b); Chung & Shin (2018); Gao & Chai (2018); Hossain et al.

- (2018); Lei (2018); Al-Thelaya et al. (2019); Cao

et al. (2019); Chen et al. (2019); Ding & Qin

- (2019); Jin et al. (2019); Karathanasopoulos & Osman (2019); Liu & Chen (2019); Nikou et al.; Nguyen et al. (2019); Tang et al. (2019); Yu & Wu (2019); Zhang et al. (2019a); Zhou et al. (2019a)

Root Mean Absolute Error (RMAE)

Kim & Kim (2019)

Continued on next page

Mean Squared Error (MSE) Patel et al. (2015); Li et al. (2017b); Zhang

- et al. (2017b); Zhong & Enke (2017); Baek & Kim (2018); Chung & Shin (2018); Hollis
- et al. (2018); Hossain et al. (2018); Liu & Wang

(2019); Pang et al. (2018); Zhan et al. (2018); de A. Arajo et al. (2019); Eapen et al. (2019); Feng et al. (2019b); Karathanasopoulos & Osman (2019); Nguyen et al. (2019); Nikou et al.; Sachdeva et al. (2019); Stoean et al. (2019)

Normalized MSE (NMSE) Chong et al. (2017) Root Mean Squared Error (RMSE)

de Oliveira et al. (2013); Chong et al. (2017); Lee & Soo (2017); Li et al. (2017b); Qin et al. (2017); Singh & Srivastava (2017); Althelaya et al. (2018); Althelaya et al. (2018); Chen et al. (2018a,b); Gao & Chai (2018); Lei (2018); Siami-Namini et al. (2018); Al-Thelaya et al. (2019); Cao et al. (2019); Cao & Wang (2019); Chen et al. (2019); Chen et al. (2019); Jin et al. (2019); Karathanasopoulos & Osman (2019); Kim & Kim (2019); Liu & Chen (2019); Nikou et al.; Sethia & Raut (2019); Siami-Namini et al. (2019); Sun et al. (2019); Tang et al. (2019); Yu & Wu (2019); Zhang et al. (2019a); Zhou et al. (2019a)

Relative RMSE (rRMSE) Patel et al. (2015); Nguyen et al. (2019) Normalized RMSE (NRMSE) Kumar et al. (2019)

Continued on next page

Mean Absolute Percentage Error (MAPE)

de Oliveira et al. (2013); Ticknor (2013); Patel et al. (2015); Bao et al. (2017); Li & Tam (2017); Qin et al. (2017); Singh & Srivastava (2017); Yang et al. (2017); Baek & Kim (2018); Chen et al. (2018a,b); Chung & Shin (2018); Gao & Chai (2018); Hossain et al. (2018); Lei (2018); Wu & Gao (2018); Tsang et al. (2018); Yan & Ouyang (2018); de A. Arajo et al. (2019); Cao et al. (2019); Chen et al. (2019); Jin et al. (2019); Karathanasopoulos & Osman (2019); Kim & Kim (2019); Kumar et al. (2019); Mohan et al. (2019); Nguyen et al. (2019); Sachdeva et al. (2019); Yu & Wu (2019); Zhang et al. (2019a); Zhou et al. (2019a)

Root Mean Squared Relative Error (RMSRE)

Zhou et al. (2018)

Mutual Information (MUL) Chong et al. (2017)

R2 Bao et al. (2017); Althelaya et al. (2018); Althelaya et al. (2018); Al-Thelaya et al. (2019); Chen et al. (2019); Jin et al. (2019); Liu & Chen (2019); Sethia & Raut (2019)

Proﬁt Metrics

Continued on next page

Return Niaki & Hoseinzade (2013); Ding et al. (2015); Bao et al. (2017); Chen et al. (2017); Lee & Soo (2017); Singh & Srivastava (2017); Zhong & Enke (2017); Fischer & Krauss (2018); Hu et al. (2018b); Matsubara et al. (2018); Oncharoen & Vateekul (2018); Sezer & Ozbayoglu (2018); Wu et al. (2018); Tsang et al.

- (2018); Yang et al. (2018); Chen & Ge (2019); Feng et al. (2019b); Hoseinzade & Haratizadeh
- (2019); Karathanasopoulos & Osman (2019); Kim & Kim (2019); Lee et al. (2019); Long et al.

(2019); Matsunaga et al. (2019); Merello et al. (2019); Sezer & Ozbayoglu (2019); Stoean et al. (2019); Song et al. (2019); Sun et al. (2019); Wang et al. (2019a); Zhang et al. (2019a); Zhou et al. (2019a)

Maximum Drawdown Zhou et al. (2019a) Annualized Volatility Karathanasopoulos & Osman (2019) Sharpe Ratio Chen et al. (2017); Fischer & Krauss (2018); Sezer & Ozbayoglu (2018); Hoseinzade & Haratizadeh (2019); Karathanasopoulos & Osman (2019); Matsunaga et al. (2019); Merello et al. (2019); Stoean et al. (2019); Wang et al. (2019a); Zhou et al. (2019a)

Signiﬁcance Analysis Kruskal-Wallis Test Zhang et al. (2019b) Diebold-Mariano Test Kumar et al. (2019)

We further show the change of classiﬁcation and regression metrics in Figure 10 and Figure 11. For classiﬁcation metrics, accuracy and F1 score are the most often used, followed by precision, recall, and MCC. For regression metrics, RMSE and MAPE are the most often used, followed by MAE and MSE.

| |
|---|

| |
|---|

| |
|---|

Figure 10: The usage of diﬀerent classiﬁcation metrics.

### 5. Implementation and Reproducibility

- 5.1. Implementation In this section, we pay a special attention to the implementation details of

the papers we survey, which is less discussed before in previous surveys.

We ﬁrstly investigate the programming language used for the implementation of machine learning and deep learning models. Among them, Python is becoming the dominant choice in the past three years as shown in Figure 12,

| | | |
|---|---|---|
| | | |
| | | |

| |
|---|

| |
|---|

| |
|---|

| | | |
|---|---|---|
| | | |
| | | |

| | | |
|---|---|---|
| | | |
| | | |

Figure 11: The usage of diﬀerent regression metrics.

which provides a bunch of packages and frameworks for model implementation purpose, e.g., Keras 4, TensorFlow 5, PyTorch 6, Theano 7, scikit-learn 8. Other choices include R, Matlab, Java, etc. We show the speciﬁc paper list using different programming languages and frameworks in Table 11. From Table 11, Keras and TensorFlow are the dominant frameworks for deep learning-based stock market prediction research. For further reference, the readers may refer to Hatcher & Yu (2018) for a comprehensive introduction of deep learning tools.

- 4http://keras.io/. Keras has been incorporated in TensorFlow 2.0 and higher versions.
- 5https://www.tensorflow.org/
- 6https://pytorch.org/
- 7http://deeplearning.net/software/theano/. It is a discontinued project and not rec-

ommended for further use.

- 8https://scikit-learn.org/stable/index.html

| |
|---|

| |
|---|

| |
|---|

Figure 12: The trend of diﬀerent programming languages for stock market prediction.

Table 11: List of programming languages and frameworks for stock market prediction.

Language Framework Articles Python Keras Zhang et al. (2017b); Sezer & Ozbayoglu (2018); Hossain et al. (2018); Eapen et al. (2019); SiamiNamini et al. (2018); Fischer & Krauss (2018); Althelaya et al. (2018); Baek & Kim (2018); Althelaya et al. (2018); Lien Minh et al. (2018); Sezer & Ozbayoglu (2019); Hoseinzade & Haratizadeh (2019); Al-Thelaya et al. (2019); Liu & Chen (2019); Nguyen & Yoon (2019); Chen & Ge (2019); Sachdeva et al. (2019); Lee & Soo (2017); Li et al. (2017a); Nguyen et al. (2019); Gunduz et al. (2017); Huynh et al. (2017); Chen et al. (2019); Zhang et al. (2019b)

60

Continued on next page

Python TensorFlow Feng et al. (2019b); Kim et al. (2019); Sezer & Ozbayoglu (2018); Dingli & Fournier (2017); Sim et al. (2019); Song et al. (2019); Liu et al. (2019c); Xu & Cohen (2018); Eapen et al. (2019); Zhan et al. (2018); Huang et al. (2018); Fischer & Krauss (2018); Althelaya et al. (2018); Gao & Chai (2018); Althelaya et al. (2018); Zhao et al. (2017); Vargas et al. (2017); Lee et al. (2019); Sezer & Ozbayoglu (2019); AlThelaya et al. (2019); Qin et al. (2017); Liu & Chen (2019); Chen & Ge (2019); Nguyen et al. (2019); Ding & Qin (2019); Zhang et al. (2019b); Borovkova & Tsiamas (2019)

Python PyTorch Yu & Wu (2019) Python Theano Zhang et al. (2017b); Chong et al. (2017); Siami-

Namini et al. (2018); Pang et al. (2018); Tsantekidis et al. (2017a) Python scikit-learn Liu et al. (2019c); Eapen et al. (2019); Gao &

Chai (2018); Zhao et al. (2017); Nguyen & Yoon

(2019)

Python N/A Cao et al. (2019); Wu et al. (2018); Li et al. (2019a); Siami-Namini et al. (2019); Jin et al.

(2019); Chen et al. (2018b)

Matlab N/A Ticknor (2013); Zhong & Enke (2017); Singh & Srivastava (2017); Wu & Gao (2018); Lei (2018); Pang et al. (2018); Chen et al. (2018a)

R nnet Ballings et al. (2015); Chen et al. (2017) Continued on next page

R N/A Weng et al. (2017); Singh & Srivastava (2017); Fischer & Krauss (2018); Kumar et al. (2019)

Java N/A Pang et al. (2018) Node.js N/A Assis et al. (2018)

Deep learning models require a larger amount of computation for training, and GPU has been used to accelerate the convolutional operations involved. With the need of processing multiple types of input data, especially the text data, the need for GPU would keep increasing in this research area. We give a list of diﬀerent types of GPU used in the surveyed papers in Table 12. Cloud computing is another solution when GPU is not available locally. There are many commercial choices of cloud computing services, e.g., Amazon Web Services 9, Google Cloud 10, and Microsoft Azure 11. However, they are not widely adopted in current study of stock market prediction and no previous study covered in this survey mentions the usage of cloud service explicitly.

- 5.2. Result Reproducibility While deep learning techniques have been proved to be eﬀective in many

diﬀerent problems and most of the previous studies have proven their eﬀectiveness for time series forecasting problems, while there are still doubts and concerns, e.g., in the M4 open forecasting competition with 100,000 time series which started on Jan 1, 2018 and ended on May 31, 2018, statistical approaches outperform pure ML methods (Makridakis et al., 2018a) and there are similar results with the dataset of the earlier M3 competition (Makridakis et al., 2018b).

- 9https://aws.amazon.com/
- 10https://cloud.google.com/
- 11https://azure.microsoft.com/

Table 12: List of GPUs used for stock market prediction.

GPU Type (all from NVIDIA) Articles Tesla P100 Zhang et al. (2019b) GeForce GTX 1060 Song et al. (2019) GeForce GTX 1080 Ti Eapen et al. (2019) Quadro P2000 Nguyen et al. (2019) TITAN X Chong et al. (2017); Lien Minh et al. (2018);

Chen & Ge (2019) TITAN Xp Chen & Ge (2019) TITAN RTX Wang et al. (2019a) Not speciﬁed Xu & Cohen (2018); Fischer & Krauss (2018);

Guang et al. (2019)

These studies also question the reproducibility and replicability in the previous papers which use ML methods.

While it is beyond the scope of this study to check the result of each paper, we instead investigate the data and code availability of the surveyed papers, which are two important aspects for the result reproducibility. Some of the source journals would require or recommend the data and code submitted as supplementary ﬁles for peer review, e.g., PLOS ONE. In other cases, the authors would share their data and code proactively, for the consideration that following works can easily use them as baselines, which gains a higher impact for their publications.

- 5.2.1. Data Availability There are many free data sources on the Internet for the research purpose of

stock market prediction. For historical price and volume, the ﬁrst choice should be the widely used Yahoo! Finance 12, which provides free access to data including stock quotes, up-to-date news, international market data, etc., and has

12https://finance.yahoo.com/

been mentioned at least in 25 out of 124 papers. Other similar options include Tushare 13, which can be used to crawl historical data of China stocks. Some stock markets would also provide the download service of historical data on their oﬃcial websites. For macroeconomic indicators, International Monetary Fund (IMF) 14 and World Bank 15 are good choices to explore. For ﬁnancial news, previous studies would crawl some major news sources, e.g., CNBC 16, Reuters 17, Wall Street Journal 18, Fortune 19, etc. Social networking websites, e.g., Twitter 20 and Sina Weibo 21, provide web Application Programming Interface (API) for the access of their data (usually preprocessed and anonymous). And researchers could ﬁlter the ﬁnancial related tweet using companies’ names as keywords. For relational data, Wikidata 22 provides relations between companies such as supplier-consumer relation and ownership relation.

There are many commercial choices too, e.g., Bloomberg 23, Wind 24, Quantopian 25, Investing.com 26. Online brokers such as Interactive Brokers 27 also provide data-related services. There are also some well-established databases for research purpose and contain many diﬀerent types of ﬁnancial data, which can be used for stock market prediction and other ﬁnancial problems. One example is the CSMAR database 28, which provides ﬁnancial statements and stock trading data for Chinese companies, including balance sheets, income statements,

- 13https://tushare.pro/
- 14https://www.imf.org/
- 15https://www.worldbank.org/
- 16https://www.cnbc.com/
- 17https://www.reuters.com/
- 18https://www.wsj.com/
- 19https://fortune.com/
- 20https://twitter.com/
- 21https://www.weibo.com/
- 22https://www.wikidata.org/wiki/Wikidata:Main_Page
- 23https://www.bloomberg.com/
- 24https://www.wind.com.cn/
- 25https://www.quantopian.com/
- 26https://www.investing.com/
- 27https://www.interactivebrokers.com/
- 28http://us.gtadata.com/

cash ﬂows, stock prices and returns, market returns and indices, and other data on Chinese equities. Another example is Wharton Research Data Services (WRDS) 29, which provides access to many ﬁnancial, accounting, banking, economics, marketing, and public policy databases through a uniform, web-based interface.

Data competition websites, e.g., Kaggle 30, are also becoming a good choice of data repository for stock market prediction. And quantitative companies could collaborate with these websites to host stock market prediction competitions, e.g., Two Sigma Financial Modeling Challenge 31, which is organized by a hedge fund named Two Sigma 32.

Even though most of the data sources are available on the Internet, it would be more convenient for replicability if the authors could release the exact dataset they use. In Table 13, we list those with the data description and link, for those data which is hosted in software host websites such as Github 33, cloud services, researcher’s own website, and data competition websites such as Kaggle. For the mid-price prediction of limit order book data, there is a benchmark dataset provided by Ntakaris et al. (2017) and has been used in the following studies (Tran et al., 2018).

Table 13: List of articles with public available data links.

Articles Data Description & Link Bao et al. (2017) CSI 300, Nifty 50, Hang Seng index, Nikkei 225, S&P500 and DJIA index from Jul-01-2008 to Sep-30-2016. Link: https://doi.org/10. 6084/m9.figshare.5028110

Continued on next page

- 29https://wrds-web.wharton.upenn.edu/
- 30https://www.kaggle.com/
- 31https://www.kaggle.com/c/two-sigma-financial-modeling
- 32https://www.twosigma.com/
- 33https://github.com/

Qin et al. (2017) One-minute stock prices of 104 corporations under NASDAQ 100 and the index value of NASDAQ 100 from Jul-26-2016 to Apr28-2017. Link: http://cseweb.ucsd.edu/ ~yaq007/NASDAQ100_stock_data.html

Zhang et al. (2017b) The daily opening prices of 50 stocks in US among 10 sectors from 2007 to 2016. Link: https://github.com/z331565360/ State-Frequency-Memory-stock-prediction/ tree/master/dataset (also used in Feng et al. (2019a))

Hollis et al. (2018) Historical data and Thomson Reuters news since 2007. Link: https://www.kaggle.com/ c/two-sigma-financial-news

Huang et al. (2018) 78 A-share stocks in CSI 100 and 13 popular HK stocks in the year 2015 and 2016. Financial web news dataset: https://pan.baidu.com/s/ 1mhCLJJi; Guba dataset: https://pan.baidu. com/s/1i5zAWh3

Wu et al. (2018) Prices and Twitter for 47 stocks listed in S&P 500 from January 2017 to November 2017. Link: https://github.com/wuhuizhe/CHRNN (also used in Liu et al. (2019a))

Continued on next page

Xu & Cohen (2018) Historical data of 88 high-trade-volume-stocks in NASDAQ and NYSE markets from Jan-012014 to Jan-01-2016. Link: https://github. com/yumoxu/stocknet-dataset (also used in Feng et al. (2019a))

- Feng et al. (2019a) Data from previous studies (Zhang et al., 2017b; Xu & Cohen, 2018). Link: https://github. com/fulifeng/Adv-ALSTM/tree/master/data
- Feng et al. (2019b) Historical price data, Sector-industry relations, and Wiki relations between their companies such as supplier-consumer relation and ownership relation for 1,026 NASDAQ and 1,737 NYSE stocks from Jan-03-2017 to Dec-08-

2017. Link: https://github.com/fulifeng/ Temporal_Relational_Stock_Ranking/tree/ master/data

Liu & Chen (2019) 6 top banks in US from 2008 to 2016. Link: https://www.kaggle.com/rohan8594/ stock-data

Kim & Kim (2019) Minute SPY ticker data from Oct-14-2016 to Oct-16-2017. Link: https://dx.doi.org/10. 6084/m9.figshare.7471568

Sim et al. (2019) Minute data of the S&P 500 index from 10:30 pm on Apr-03-2017, to 2:15 pm on May-022017. Link: https://www.kesci.com/home/ dataset/5bbdc2513631bc00109c29a4/files

Continued on next page

Stoean et al. (2019) 25 companies listed under the Romanian stock market from Oct-16-1997 to Mar-132019. Link: https://doi.org/10.6084/m9. figshare.7976144.v1

Liu et al. (2019c) News headlines from Thomson Reuters and Cable News Network for 6 stocks in US markets. Link: https://github.com/linechany/ knowledge-graph

- 5.2.2. Code Availability Github has been the mainstream platform of hosting source code in the

computer science ﬁeld. However, only a small number of studies would release their code for now, in the area of stock market prediction. In Table 14, we list the articles with public code repositories. A short description of each method is mentioned, and the details can be found in Section 4 and the original documents.

### 6. Future Directions

Based on our review of recent works, we give some future directions in this section, which aims to bring new insight to interested researchers.

- 6.1. New Models Diﬀerent structures of neural networks are not fully studied for stock pre-

diction, especially those who only appear in recent years. There are two steps where deep learning models involve in stock prediction, namely, Data Processing and Prediction Model in Section 4. While we already covered some latest eﬀort of applying new models in this survey, e.g., the attention mechanism and generative adversarial networks, there are still a huge space to explore for new

Table 14: List of articles with public code links.

Articles Method Description & Link Weng et al. (2017) Artiﬁcial neural networks (ANN), decision trees (DT), and support vector machines (SVM) in R. Link: https://github.com/binweng/ ShinyStock

Zhang et al. (2017b) State frequency memory (SFM) recurrent network. Link: https: //github.com/z331565360/ State-Frequency-Memory-stock-prediction

Hu et al. (2018b) Hybrid attention network (HAN). Link: https://github.com/gkeng/ Listening-to-Chaotic-Whishpers--Code

Xu & Cohen (2018) A deep generative model named StockNet. Link: https://github.com/yumoxu/ stocknet-code

- Feng et al. (2019a) Adversarial attentive LSTM. Link: https:// github.com/fulifeng/Adv-ALSTM
- Feng et al. (2019b) Relational stock ranking (RSR). Link: https://github.com/fulifeng/Temporal_ Relational_Stock_Ranking

Kim et al. (2019) Hierarchical graph attention network (HATS). Link: https://github.com/dmis-lab/hats

Lee et al. (2019) Deep Q-Network. Link: https://github.com/lee-jinho/ DQN-global-stock-market-prediction/

models. For example, for sentiment analysis of text data, Transformer (Vaswani et al., 2017) and pre-trained BERT (Bidirectional Encoder Representations from Transformers) (Devlin et al., 2018) are widely used in natural language process-

ing, but is less discussed for ﬁnancial news analysis.

- 6.2. Multiple Data Sources Observed from our discussion in Section 4, it is not wise to design a stock

prediction solution based on a single data source, e.g., market data, as it has been heavily used in previous studies and it would be very challenging to outperform existing solutions. A better idea is to collect and use multiple data sources, especially those which are less explored in the literature (Zhou et al., 2019b).

- 6.3. Cross-market Analysis Most of the existing studies focus on only one stock market, in the sense

that stock markets diﬀer from each other because of the trading rules, while diﬀerent markets may share some common phenomenon that can be leveraged for prediction by approaches such as transfer learning. There are already a few studies showing positive results for cross-market analysis (Hoseinzade & Haratizadeh, 2019; Lee et al., 2019; Merello et al., 2019; Nguyen & Yoon, 2019; Hoseinzade et al., 2019), it is worth exploring in the following studies. In Lee et al. (2019), the model is trained only on US stock market data and tested on the stock market data of 31 diﬀerent countries over 12 years. Even though the authors do not use the terminology of transfer learning, it is a practice of model transfer.

- 6.4. Algorithmic Trading The prediction is not the end of the journey. Good prediction is one factor

to make money in the stock market, but not the whole story. Some of the studies have evaluated the proﬁt and risk of the trading strategies based on the prediction result, as we discussed in Section 4.4. However, these strategies are simple and intuitive, which may be impractical limited by the trading rules. The transaction cost is often omitted or simpliﬁed, which makes the conclusion less persuasive. Another problem is the adaption for diﬀerent market styles,

as the training of deep learning models is time-consuming. These studies are not suﬃcient for building a practical algorithmic trading system. One possible direction is deep reinforcement learning, which has recent successes in a variety of applications and is also been used in a few studies for stock prediction and trading (Xiong et al., 2018; Lee et al., 2019). It has advantages of simulating more possible cases and making a faster and better trading choice than human traders.

### 7. Conclusion

Inspired by the rapid development and increasing usage of deep learning models for stock market prediction, we give a review of recent progress by surveying more than 100 related published articles in the past three years. We cover each step from raw data collection and data processing to prediction model and model evaluation and present the research trend from 2017 to 2019. We also pay a special attention to the implementation of deep learning models and the reproducibility of published articles, with the hope to accelerate the process of adopting published models as baselines (maybe with new data input). With some future directions pointed up, the insight and summary in the survey would help to boost the future research in related topics.

### Acknowledgement

Weiwei Jiang: Conceptualization; Data curation; Formal analysis; Funding acquisition; Investigation; Methodology; Project administration; Resources; Software; Supervision; Validation; Visualization; Roles/Writing - original draft; Writing - review & editing.

### References

de A. Arajo, R., Nedjah, N., Oliveira, A. L., & de L. Meira, S. R. (2019). A deep increasingdecreasing-linear neural network for ﬁnancial

time series prediction. Neurocomputing, 347, 59 – 81. URL: http: //www.sciencedirect.com/science/article/pii/S0925231219303194. doi:https://doi.org/10.1016/j.neucom.2019.03.017.

Aguilar-Rivera, R., Valenzuela-Rend´n, M., & Rodrı´guez-Ortiz, J. (2015). Genetic algorithms and darwinian approaches in ﬁnancial applications: A survey. Expert Systems with Applications, 42, 7684 – 7697. URL: http://www.sciencedirect.com/science/article/pii/ S0957417415003954. doi:https://doi.org/10.1016/j.eswa.2015.06.001.

Akita, R., Yoshihara, A., Matsubara, T., & Uehara, K. (2016). Deep learning for stock prediction using numerical and textual information. In 2016 IEEE/ACIS 15th International Conference on Computer and Information Science (ICIS) (pp. 1–6). doi:10.1109/ICIS.2016.7550882.

Al-Thelaya, K. A., El-Alfy, E.-S. M., & Mohammed, S. (2019). Forecasting of bahrain stock market with deep learning: Methodology and case study. In 2019 8th International Conference on Modeling Simulation and Applied Optimization (ICMSAO) (pp. 1–5). IEEE.

Alpaydin, E. (2014). Introduction to machine learning. MIT press.

Althelaya, K. A., El-Alfy, E. M., & Mohammed, S. (2018). Stock market forecast using multivariate analysis with bidirectional and stacked (lstm, gru). In 2018 21st Saudi Computer Society National Computer Conference (NCC) (pp. 1– 7). doi:10.1109/NCG.2018.8593076.

Althelaya, K. A., El-Alfy, E.-S. M., & Mohammed, S. (2018). Evaluation of bidirectional lstm for short- and long-term stock market prediction. In 2018 9th International Conference on Information and Communication Systems (ICICS) (pp. 151–156). IEEE.

Appel, G., & Dobson, E. (2007). Understanding MACD. Traders Press.

Arau´jo, R. d. A. (2011). A class of hybrid morphological perceptrons with application in time series forecasting. Knowledge-Based Systems, 24, 513– 529.

Asadi, S., Hadavandi, E., Mehmanpazir, F., & Nakhostin, M. M. (2012). Hybridization of evolutionary levenberg–marquardt neural networks and data pre-processing for stock market prediction. Knowledge-Based Systems, 35, 245–258.

Assis, C. A., Pereira, A. C., Carrano, E. G., Ramos, R., & Dias, W. (2018). Restricted boltzmann machines for the prediction of trends in ﬁnancial time series. In 2018 International Joint Conference on Neural Networks (IJCNN) (pp. 1–8). IEEE.

Atsalakis, G. S., & Valavanis, K. P. (2009). Surveying stock market forecasting techniques part ii: Soft computing methods. Expert Systems with Applications, 36, 5932 – 5941. URL: http: //www.sciencedirect.com/science/article/pii/S0957417408004417.

doi:https://doi.org/10.1016/j.eswa.2008.07.006.

Baek, Y., & Kim, H. Y. (2018). Modaugnet: A new forecasting framework for stock market index value with an overﬁtting prevention lstm module and a prediction lstm module. Expert Systems with Applications, 113, 457 – 480. URL: http://www.sciencedirect.com/science/article/pii/ S0957417418304342. doi:https://doi.org/10.1016/j.eswa.2018.07.019.

Bahdanau, D., Cho, K., & Bengio, Y. (2014). Neural machine translation by jointly learning to align and translate. arXiv preprint arXiv:1409.0473, .

Ballings, M., den Poel, D. V., Hespeels, N., & Gryp, R. (2015). Evaluating multiple classiﬁers for stock price direction prediction. Expert Systems with Applications, 42, 7046 – 7056. URL: http: //www.sciencedirect.com/science/article/pii/S0957417415003334.

doi:https://doi.org/10.1016/j.eswa.2015.05.013.

Bao, W., Yue, J., & Rao, Y. (2017). A deep learning framework for ﬁnancial time series using stacked autoencoders and long-short term memory. PLOS ONE, 12, 1–24. URL: https://doi.org/10.1371/journal.pone.0180944. doi:10.1371/journal.pone.0180944.

Bollacker, K., Evans, C., Paritosh, P., Sturge, T., & Taylor, J. (2008). Freebase: a collaboratively created graph database for structuring human knowledge. In Proceedings of the 2008 ACM SIGMOD international conference on Management of data (pp. 1247–1250).

Bollerslev, T. (1986). Generalized autoregressive conditional heteroskedasticity. Journal of econometrics, 31, 307–327.

Bordes, A., Usunier, N., Garcia-Duran, A., Weston, J., & Yakhnenko, O. (2013). Translating embeddings for modeling multi-relational data. In Advances in neural information processing systems (pp. 2787–2795).

Borovkova, S., & Tsiamas, I. (2019). An ensemble of lstm neural networks for high-frequency stock market classiﬁcation. Journal of Forecasting, .

Brownlee, J. (2018). Deep Learning for Time Series Forecasting: Predict the Future with MLPs, CNNs and LSTMs in Python. Machine Learning Mastery.

Cao, J., Li, Z., & Li, J. (2019). Financial time series forecasting model based on ceemdan and lstm. Physica A: Statistical Mechanics and its Applications, 519, 127 – 139. URL: http: //www.sciencedirect.com/science/article/pii/S0378437118314985.

doi:https://doi.org/10.1016/j.physa.2018.11.061.

Cao, J., & Wang, J. (2019). Stock price forecasting model based on modiﬁed convolution neural network and ﬁnancial time series analysis. International Journal of Communication Systems, 32, e3987. URL: https://onlinelibrary. wiley.com/doi/abs/10.1002/dac.3987. doi:10.1002/dac.3987. arXiv:https://onlinelibrary.wiley.com/doi/pdf/10.1002/dac.3987.

E3987 IJCS-18-0961.R2.

Cavalcante, R. C., Brasileiro, R. C., Souza, V. L., Nobrega, J. P., & Oliveira, A. L. (2016). Computational intelligence and ﬁnancial markets: A survey and future directions. Expert Systems with Applications, 55, 194 – 211. URL: http://www.sciencedirect.com/science/article/pii/ S095741741630029X. doi:https://doi.org/10.1016/j.eswa.2016.02.006.

Chen, H., Xiao, K., Sun, J., & Wu, S. (2017). A double-layer neural network framework for high-frequency forecasting. ACM Transactions on Management Information Systems (TMIS), 7, 11.

Chen, L., Chi, Y., Guan, Y., & Fan, J. (2019). A hybrid attention-based emdlstm model for ﬁnancial time series prediction. In 2019 2nd International Conference on Artiﬁcial Intelligence and Big Data (ICAIBD) (pp. 113–118). IEEE.

Chen, L., Qiao, Z., Wang, M., Wang, C., Du, R., & Stanley, H. E. (2018a). Which artiﬁcial intelligence algorithm better predicts the chinese stock market? IEEE Access, 6, 48625–48633.

Chen, S., & Ge, L. (2019). Exploring the attention mechanism in lstm-based hong kong stock price movement prediction. Quantitative Finance, 19, 1507– 1515.

Chen, W., Yeo, C. K., Lau, C. T., & Lee, B. S. (2018b). Leveraging social media news to predict stock index movement using rnn-boost. Data & Knowledge Engineering, 118, 14–24.

Chen, Y., Lin, W., & Wang, J. Z. (2019). A dual-attention-based stock price trend prediction model with dual features. IEEE Access, 7, 148047–148058. doi:10.1109/ACCESS.2019.2946223.

Chen, Y., Wei, Z., & Huang, X. (2018c). Incorporating corporation relationship via graph convolutional neural networks for stock price prediction. In Proceedings of the 27th ACM International Conference on Information and Knowledge Management CIKM ’18 (pp. 1655–1658). New York,

NY, USA: ACM. URL: http://doi.acm.org/10.1145/3269206.3269269. doi:10.1145/3269206.3269269.

Cheng, L.-C., Huang, Y.-H., & Wu, M.-E. (2018). Applied attention-based lstm neural networks in stock prediction. In 2018 IEEE International Conference on Big Data (Big Data) (pp. 4716–4718). IEEE.

Cho, K., Van Merri¨enboer, B., Gulcehre, C., Bahdanau, D., Bougares, F., Schwenk, H., & Bengio, Y. (2014). Learning phrase representations using rnn encoder-decoder for statistical machine translation. arXiv preprint arXiv:1406.1078, .

Chong, E., Han, C., & Park, F. C. (2017). Deep learning networks for stock market analysis and prediction: Methodology, data representations, and case studies. Expert Systems with Applications, 83, 187 – 205. URL: http://www.sciencedirect.com/science/article/pii/ S0957417417302750. doi:https://doi.org/10.1016/j.eswa.2017.04.030.

Chung, H., & Shin, K.-s. (2018). Genetic algorithm-optimized long short-term memory network for stock market prediction. Sustainability, 10, 3765.

Cui, Z., Chen, W., & Chen, Y. (2016). Multi-scale convolutional neural networks for time series classiﬁcation. arXiv preprint arXiv:1603.06995, .

Deng, S., Zhang, N., Zhang, W., Chen, J., Pan, J. Z., & Chen, H. (2019). Knowledge-driven stock trend prediction and explanation via temporal convolutional network. In Companion Proceedings of The 2019 World Wide Web Conference WWW ’19 (pp. 678–685). New York, NY, USA: ACM. URL: http://doi.acm.org/10.1145/3308560.3317701. doi:10. 1145/3308560.3317701.

Deng, Y., Bao, F., Kong, Y., Ren, Z., & Dai, Q. (2016). Deep direct reinforcement learning for ﬁnancial signal representation and trading. IEEE transactions on neural networks and learning systems, 28, 653–664.

Devlin, J., Chang, M.-W., Lee, K., & Toutanova, K. (2018). Bert: Pre-training of deep bidirectional transformers for language understanding. arXiv preprint arXiv:1810.04805, .

Diaconescu, E. (2008). The use of narx neural networks to predict chaotic time series. Wseas Transactions on computer research, 3, 182–191.

Diebold, F. X., & Mariano, R. S. (2002). Comparing predictive accuracy. Journal of Business & economic statistics, 20, 134–144.

Ding, G., & Qin, L. (2019). Study on the prediction of stock price based on the associated network model of lstm. International Journal of Machine Learning and Cybernetics, (pp. 1–11).

- Ding, X., Zhang, Y., Liu, T., & Duan, J. (2014). Using structured events to predict stock price movement: An empirical investigation. In Proceedings of the 2014 Conference on Empirical Methods in Natural Language Processing (EMNLP) (pp. 1415–1425).
- Ding, X., Zhang, Y., Liu, T., & Duan, J. (2015). Deep learning for event-driven stock prediction. In Twenty-fourth international joint conference on artiﬁcial intelligence.

Dingli, A., & Fournier, K. S. (2017). Financial time series forecasting–a deep learning approach. Int. J. Mach. Learn. Comput, 7, 118–122.

Eapen, J., Bein, D., & Verma, A. (2019). Novel deep learning model with cnn and bi-directional lstm for improved stock market index prediction. In 2019 IEEE 9th Annual Computing and Communication Workshop and Conference (CCWC) (pp. 0264–0270). doi:10.1109/CCWC.2019.8666592.

Ersan, D., Nishioka, C., & Scherp, A. (2019). Comparison of machine learning methods for ﬁnancial time series forecasting at the examples of over 10 years of daily and hourly data of dax 30 and s&p 500. Journal of Computational Social Science, (pp. 1–31).

Fama, E. F. (1965). The behavior of stock-market prices. The journal of Business, 38, 34–105.

Fawcett, T. (2006). An introduction to roc analysis. Pattern recognition letters, 27, 861–874.

Feng, F., Chen, H., He, X., Ding, J., Sun, M., & Chua, T.-S. (2019a). Enhancing stock movement prediction with adversarial training. In Proceedings of the Twenty-Eighth International Joint Conference on Artiﬁcial Intelligence, IJCAI-19 (pp. 5843–5849). International Joint Conferences on Artiﬁcial Intelligence Organization. URL: https://doi.org/10.24963/ijcai.2019/810. doi:10.24963/ijcai.2019/810.

Feng, F., He, X., Wang, X., Luo, C., Liu, Y., & Chua, T.-S. (2019b). Temporal relational ranking for stock prediction. ACM Trans. Inf. Syst., 37, 27:1–27:30. URL: http://doi.acm.org/10.1145/3309547. doi:10.1145/3309547.

Fischer, T., & Krauss, C. (2018). Deep learning with long shortterm memory networks for ﬁnancial market predictions. European Journal of Operational Research, 270, 654 – 669. URL: http: //www.sciencedirect.com/science/article/pii/S0377221717310652.

doi:https://doi.org/10.1016/j.ejor.2017.11.054.

Gao, T., & Chai, Y. (2018). Improving stock closing price prediction using recurrent neural network and technical indicators. Neural Computation, 30, 2833–2854. URL: https://doi.org/10.1162/neco_a_01124. doi:10.1162/ neco\_a\_01124. arXiv:https://doi.org/10.1162/neco a 01124. PMID: 30148707.

Goodfellow, I., Bengio, Y., & Courville, A. (2016). Deep learning. MIT press.

Goodfellow, I., Pouget-Abadie, J., Mirza, M., Xu, B., Warde-Farley, D., Ozair, S., Courville, A., & Bengio, Y. (2014). Generative adversarial nets. In Advances in neural information processing systems (pp. 2672–2680).

Guang, L., Xiaojie, W., & Ruifan, L. (2019). Multi-scale rcnn model for ﬁnancial time-series classiﬁcation. arXiv preprint arXiv:1911.09359, .

Gundersen, O. E., & Kjensmo, S. (2018). State of the art: Reproducibility in artiﬁcial intelligence. In Thirty-Second AAAI Conference on Artiﬁcial Intelligence.

Gunduz, H., Yaslan, Y., & Cataltepe, Z. (2017). Intraday prediction of borsa istanbul using convolutional neural networks and feature correlations. Knowledge-Based Systems, 137, 138–148.

Gken, M., zalc, M., Boru, A., & Dosdoru, A. T. (2016). Integrating metaheuristics and artiﬁcial neural networks for improved stock price prediction. Expert Systems with Applications, 44, 320 – 331. URL: http://www.sciencedirect.com/science/article/pii/ S0957417415006570. doi:https://doi.org/10.1016/j.eswa.2015.09.029.

Harris, Z. S. (1954). Distributional structure. Word, 10, 146–162.

Hatcher, W. G., & Yu, W. (2018). A survey of deep learning: Platforms, applications and emerging research trends. IEEE Access, 6, 24411–24432. doi:10.1109/ACCESS.2018.2830661.

Hollis, T., Viscardi, A., & Yi, S. E. (2018). A comparison of lstms and attention mechanisms for forecasting ﬁnancial time series. arXiv preprint arXiv:1812.07699, .

Hoseinzade, E., & Haratizadeh, S. (2019). Cnnpred: Cnn-based stock market prediction using a diverse set of variables. Expert Systems with Applications, 129, 273–285.

Hoseinzade, E., Haratizadeh, S., & Khoeini, A. (2019). U-cnnpred: A universal cnn-based predictor for stock markets. arXiv preprint arXiv:1911.12540, .

Hossain, M. A., Karim, R., Thulasiram, R., Bruce, N. D. B., & Wang, Y. (2018). Hybrid deep learning model for stock price prediction. In 2018 IEEE

Symposium Series on Computational Intelligence (SSCI) (pp. 1837–1844). doi:10.1109/SSCI.2018.8628641.

Hu, H., & Qi, G.-J. (2017). State-frequency memory recurrent neural networks. In Proceedings of the 34th International Conference on Machine LearningVolume 70 (pp. 1568–1577). JMLR. org.

Hu, H., Tang, L., Zhang, S., & Wang, H. (2018a). Predicting the direction of stock markets using optimized neural networks with google trends. Neurocomputing, 285, 188 – 195. URL: http: //www.sciencedirect.com/science/article/pii/S0925231218300572.

doi:https://doi.org/10.1016/j.neucom.2018.01.038.

Hu, Z., Liu, W., Bian, J., Liu, X., & Liu, T.-Y. (2018b). Listening to chaotic whispers: A deep learning framework for news-oriented stock trend prediction. In Proceedings of the Eleventh ACM International Conference on Web Search and Data Mining WSDM ’18 (pp. 261–269). New York, NY, USA: ACM. URL: http://doi.acm.org/10.1145/3159652.3159690. doi:10.1145/3159652.3159690.

Huang, J., Zhang, Y., Zhang, J., & Zhang, X. (2018). A tensor-based sub-mode coordinate algorithm for stock prediction. In 2018 IEEE Third International Conference on Data Science in Cyberspace (DSC) (pp. 716–721). doi:10. 1109/DSC.2018.00114.

Huynh, H. D., Dang, L. M., & Duong, D. (2017). A new model for stock price movements prediction using deep neural network. In Proceedings of the Eighth International Symposium on Information and Communication Technology (pp. 57–62). ACM.

Hyndman, R. J., & Athanasopoulos, G. (2018). Forecasting: principles and practice. OTexts.

Jegadeesh, N., & Titman, S. (1993). Returns to buying winners and selling

losers: Implications for stock market eﬃciency. The Journal of ﬁnance, 48, 65–91.

Jiang, W., & Zhang, L. (2018). Geospatial data to images: A deep-learning framework for traﬃc forecasting. Tsinghua Science and Technology, 24, 52– 64.

- Jiang, W., & Zhang, L. (2020). Edge-siamnet and edge-triplenet: New deep learning models for handwritten numeral recognition. IEICE Transactions on Information and Systems, 103.
- Jiang, X., Pan, S., Jiang, J., & Long, G. (2018). Cross-domain deep learning approach for multiple ﬁnancial market prediction. In 2018 International Joint Conference on Neural Networks (IJCNN) (pp. 1–8). doi:10.1109/IJCNN. 2018.8489360.

Jin, Z., Yang, Y., & Liu, Y. (2019). Stock closing price prediction based on sentiment analysis and lstm. Neural Computing and Applications, (pp. 1–17).

Joachims, T. (1998). Text categorization with support vector machines: Learning with many relevant features. In European conference on machine learning (pp. 137–142). Springer.

Joulin, A., Grave, E.,´ Bojanowski, P., & Mikolov, T. (2017). Bag of tricks for eﬃcient text classiﬁcation. In Proceedings of the 15th Conference of the European Chapter of the Association for Computational Linguistics: Volume 2, Short Papers (pp. 427–431).

Kara, Y., Boyacioglu, M. A., & Baykan, O.¨ K. (2011). Predicting direction of stock price index movement using artiﬁcial neural networks and support vector machines: The sample of the istanbul stock exchange. Expert systems with Applications, 38, 5311–5319.

Karathanasopoulos, A., & Osman, M. (2019). Forecasting the dubai ﬁnancial market with a combination of momentum eﬀect with a deep belief network.

Journal of Forecasting, 38, 346–353. URL: https://onlinelibrary. wiley.com/doi/abs/10.1002/for.2560. doi:10.1002/for.2560. arXiv:https://onlinelibrary.wiley.com/doi/pdf/10.1002/for.2560.

- Kim, R., So, C. H., Jeong, M., Lee, S., Kim, J., & Kang, J. (2019). Hats: A hierarchical graph attention network for stock movement prediction. arXiv preprint arXiv:1908.07999, .
- Kim, S., & Kang, M. (2019). Financial series prediction using attention lstm. arXiv preprint arXiv:1902.10877, .
- Kim, T., & Kim, H. Y. (2019). Forecasting stock prices with a feature fusion lstm-cnn model using diﬀerent representations of the same data. PloS one, 14, e0212320.

Kingma, D. P., & Ba, J. (2014). Adam: A method for stochastic optimization. arXiv preprint arXiv:1412.6980, .

Kruskal, W. H., & Wallis, W. A. (1952). Use of ranks in one-criterion variance analysis. Journal of the American statistical Association, 47, 583–621.

Kumar, B. S., Ravi, V., & Miglani, R. (2019). Predicting indian stock market using the psycho-linguistic features of ﬁnancial news. arXiv preprint arXiv:1911.06193, .

Kyle, K., & Crossley, S. A. (2015). Automatically assessing lexical sophistication: Indices, tools, ﬁndings, and application. Tesol Quarterly, 49, 757–786.

Lee, C.-Y., & Soo, V.-W. (2017). Predict stock price with ﬁnancial news based on recurrent convolutional neural networks. In 2017 Conference on Technologies and Applications of Artiﬁcial Intelligence (TAAI) (pp. 160–165). IEEE.

Lee, J., Kim, R., Koh, Y., & Kang, J. (2019). Global stock market prediction based on stock chart images using deep q-network. arXiv preprint arXiv:1902.10948, .

Lei, L. (2018). Wavelet neural network prediction method of stock price trend based on rough set attribute reduction. Applied Soft Computing, 62, 923 – 932. URL: http://www.sciencedirect.com/science/article/pii/ S1568494617305689. doi:https://doi.org/10.1016/j.asoc.2017.09.029.

Li, C., Song, D., & Tao, D. (2019a). Multi-task recurrent neural networks and higher-order markov random ﬁelds for stock price movement prediction: Multi-task rnn and higer-order mrfs for stock price classiﬁcation. In Proceedings of the 25th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining KDD ’19 (pp. 1141–1151). New York, NY, USA: ACM. URL: http://doi.acm.org/10.1145/3292500.3330983. doi:10.1145/3292500.3330983.

Li, J., Bu, H., & Wu, J. (2017a). Sentiment-aware stock market prediction: A deep learning method. In 2017 International Conference on Service Systems and Service Management (pp. 1–6). IEEE.

Li, Q., Chen, Y., Jiang, L. L., Li, P., & Chen, H. (2016a). A tensor-based information framework for predicting the stock market. ACM Transactions on Information Systems (TOIS), 34, 1–30.

Li, X., Li, Y., Yang, H., Yang, L., & Liu, X.-Y. (2019b). Dp-lstm: Diﬀerential privacy-inspired lstm for stock prediction using ﬁnancial news. arXiv preprint arXiv:1912.10806, .

Li, X., Xie, H., Wang, R., Cai, Y., Cao, J., Wang, F., Min, H., & Deng, X. (2016b). Empirical analysis: stock market prediction via extreme learning machine. Neural Computing & Applications, 27, 67–78.

- Li, X., Yang, L., Xue, F., & Zhou, H. (2017b). Time series prediction of stock price using deep belief networks with intrinsic plasticity. In 2017 29th Chinese Control And Decision Conference (CCDC) (pp. 1237–1242). IEEE.
- Li, Y., & Ma, W. (2010). Applications of artiﬁcial neural networks in ﬁnancial

- economics: A survey. In 2010 International Symposium on Computational Intelligence and Design (pp. 211–214). volume 1.
- Li, Z., & Tam, V. (2017). Combining the real-time wavelet denoising and longshort-term-memory neural network for predicting stock indexes. In 2017 IEEE Symposium Series on Computational Intelligence (SSCI) (pp. 1–8). IEEE.

Liang, X., Ge, Z., Sun, L., He, M., & Chen, H. (2019). Lstm with wavelet transform based data preprocessing for stock price prediction. Mathematical Problems in Engineering, 2019.

Lien Minh, D., Sadeghi-Niaraki, A., Huy, H. D., Min, K., & Moon, H. (2018). Deep learning approach for short-term stock trends prediction based on twostream gated recurrent unit network. IEEE Access, 6, 55392–55404. doi:10. 1109/ACCESS.2018.2868970.

Lin, T., Guo, T., & Aberer, K. (2017). Hybrid neural networks for learning the trend in time series. In Proceedings of the Twenty-Sixth International Joint Conference on Artiﬁcial Intelligence CONF (pp. 2273–2279).

- Liu, G., & Wang, X. (2019). A numerical-based attention method for stock market prediction with dual information. IEEE Access, 7, 7357–7367. doi:10. 1109/ACCESS.2018.2886367.
- Liu, H., & Song, B. (2017). Stock trends forecasting by multi-layer stochastic ann bagging. In 2017 IEEE 29th International Conference on Tools with Artiﬁcial Intelligence (ICTAI) (pp. 322–329). doi:10.1109/ICTAI.2017.00058.

Liu, J., & Chen, S. (2019). Non-stationary multivariate time series prediction with selective recurrent neural networks. In Paciﬁc Rim International Conference on Artiﬁcial Intelligence (pp. 636–649). Springer.

Liu, J., Lin, H., Liu, X., Xu, B., Ren, Y., Diao, Y., & Yang, L. (2019a). Transformer-based capsule network for stock movement prediction. In Proceedings of the First Workshop on Financial Technology and Natural Language Processing (pp. 66–73).

Liu, J., Lu, Z., & Du, W. (2019b). Combining enterprise knowledge graph and news sentiment analysis for stock price prediction. In Proceedings of the 52nd Hawaii International Conference on System Sciences.

Liu, Q., Cheng, X., Su, S., & Zhu, S. (2018). Hierarchical complementary attention network for predicting stock price movements with news. In Proceedings of the 27th ACM International Conference on Information and Knowledge Management CIKM ’18 (pp. 1603–1606). New York, NY, USA: ACM. URL: http://doi.acm.org/10.1145/3269206.3269286. doi:10.1145/3269206.3269286.

Liu, Y., Zeng, Q., Ordieres Mer´e, J., & Yang, H. (2019c). Anticipating stock market of the renowned companies: A knowledge graph approach. Complexity, 2019.

Long, W., Lu, Z., & Cui, L. (2019). Deep learning-based feature engineering for stock price movement prediction. Knowledge-Based Systems, 164, 163 – 173. URL: http://www.sciencedirect.com/science/article/ pii/S0950705118305264. doi:https://doi.org/10.1016/j.knosys.2018. 10.034.

Loper, E., & Bird, S. (2002). Nltk: the natural language toolkit. arXiv preprint cs/0205028, .

Ma, D., Li, S., Zhang, X., & Wang, H. (2017). Interactive attention networks for aspect-level sentiment classiﬁcation. arXiv preprint arXiv:1709.00893, .

- Makridakis, S., Spiliotis, E., & Assimakopoulos, V. (2018a). The m4 competition: Results, ﬁndings, conclusion and way forward. International Journal of Forecasting, . URL: http://www. sciencedirect.com/science/article/pii/S0169207018300785. doi:https://doi.org/10.1016/j.ijforecast.2018.06.001.
- Makridakis, S., Spiliotis, E., & Assimakopoulos, V. (2018b). Statistical and machine learning forecasting methods: Concerns and ways forward. PLOS

ONE, 13, 1–26. URL: https://doi.org/10.1371/journal.pone.0194889. doi:10.1371/journal.pone.0194889.

Malkiel, B. G. (2003). The eﬃcient market hypothesis and its critics. Journal of economic perspectives, 17, 59–82.

Matsubara, T., Akita, R., & Uehara, K. (2018). Stock price prediction by deep neural generative model of news articles. IEICE TRANSACTIONS on Information and Systems, 101, 901–908.

Matsunaga, D., Suzumura, T., & Takahashi, T. (2019). Exploring graph neural networks for stock market predictions with rolling window analysis. arXiv preprint arXiv:1909.10660, .

Menezes Jr, J. M. P., & Barreto, G. A. (2008). Long-term time series prediction with the narx network: An empirical evaluation. Neurocomputing, 71, 3335– 3343.

Merello, S., Ratto, A. P., Oneto, L., & Cambria, E. (2019). Ensemble application of transfer learning and sample weighting for stock market prediction. In 2019 International Joint Conference on Neural Networks (IJCNN) (pp. 1–8). IEEE.

Mikolov, T., Chen, K., Corrado, G., & Dean, J. (2013). Eﬃcient estimation of word representations in vector space. arXiv preprint arXiv:1301.3781, .

Mohan, S., Mullapudi, S., Sammeta, S., Vijayvergia, P., & Anastasiu, D. C. (2019). Stock price prediction using news sentiment analysis. In 2019 IEEE Fifth International Conference on Big Data Computing Service and Applications (BigDataService) (pp. 205–208). IEEE.

Nelson, D. M., Pereira, A. C., & de Oliveira, R. A. (2017). Stock market’s price movement prediction with lstm neural networks. In 2017 International Joint Conference on Neural Networks (IJCNN) (pp. 1419–1426). IEEE.

Nguyen, D. H. D., Tran, L. P., & Nguyen, V. (2019). Predicting stock prices using dynamic lstm models. In International Conference on Applied Informatics (pp. 199–212). Springer.

Nguyen, T. H., & Shirai, K. (2015). Topic modeling based sentiment analysis on social media for stock market prediction. In Proceedings of the 53rd Annual Meeting of the Association for Computational Linguistics and the 7th International Joint Conference on Natural Language Processing (Volume 1: Long Papers) (pp. 1354–1364).

Nguyen, T.-T., & Yoon, S. (2019). A novel approach to short-term stock price movement prediction using transfer learning. Applied Sciences, 9, 4745.

Niaki, S. T. A., & Hoseinzade, S. (2013). Forecasting s&p 500 index using artiﬁcial neural networks and design of experiments. Journal of Industrial Engineering International, 9, 1.

Nikfarjam, A., Emadzadeh, E., & Muthaiyah, S. (2010). Text mining approaches for stock market prediction. In 2010 The 2nd International Conference on Computer and Automation Engineering (ICCAE) (pp. 256–260). volume 4. doi:10.1109/ICCAE.2010.5451705.

Nikou, M., Mansourfar, G., & Bagherzadeh, J. (). Stock price prediction using deep learning algorithm and its comparison with machine learning algorithms. Intelligent Systems in Accounting, Finance and Management, .

Ntakaris, A., Magris, M., Kanniainen, J., Gabbouj, M., & Iosiﬁdis, A. (2017). Benchmark dataset for mid-price prediction of limit order book data. arXiv preprint arXiv:1705.03233, .

Nti, I. K., Adekoya, A. F., & Weyori, B. A. (2019). A systematic review of fundamental and technical analysis of stock market predictions. Artiﬁcial Intelligence Review, (pp. 1–51).

de Oliveira, F. A., Nobre, C. N., & Zarate, L. E. (2013). Applying artiﬁcial neural networks to prediction of stock price and improvement of the directional

prediction index–case study of petr4, petrobras, brazil. Expert Systems with Applications, 40, 7596–7606.

Oncharoen, P., & Vateekul, P. (2018). Deep learning for stock market prediction using event embedding and technical indicators. In 2018 5th International Conference on Advanced Informatics: Concept Theory and Applications (ICAICTA) (pp. 19–24). doi:10.1109/ICAICTA.2018.8541310.

Pang, X., Zhou, Y., Wang, P., Lin, W., & Chang, V. (2018). An innovative neural network approach for stock market prediction. The Journal of Supercomputing, . URL: https://doi.org/10.1007/s11227-017-2228-y. doi:10.1007/s11227-017-2228-y.

Passalis, N., Tsantekidis, A., Tefas, A., Kanniainen, J., Gabbouj, M., & Iosiﬁdis, A. (2017). Time-series classiﬁcation using neural bag-of-features. In 2017 25th European Signal Processing Conference (EUSIPCO) (pp. 301–305). IEEE.

Patel, J., Shah, S., Thakkar, P., & Kotecha, K. (2015). Predicting stock market index using fusion of machine learning techniques. Expert Systems with Applications, 42, 2162 – 2172. URL: http: //www.sciencedirect.com/science/article/pii/S0957417414006551.

doi:https://doi.org/10.1016/j.eswa.2014.10.031.

Peng, H., Long, F., & Ding, C. (2005). Feature selection based on mutual information criteria of max-dependency, max-relevance, and min-redundancy. IEEE Transactions on pattern analysis and machine intelligence, 27, 1226– 1238.

Peng, Y., & Jiang, H. (2016). Leverage ﬁnancial news to predict stock price movements using word embeddings and deep neural networks. In Proceedings of the 2016 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (pp. 374–379). San Diego, California: Association for Computational Linguistics. URL: https://www.aclweb.org/anthology/N16-1041. doi:10.18653/ v1/N16-1041.

Pennington, J., Socher, R., & Manning, C. D. (2014). Glove: Global vectors for word representation. In Proceedings of the 2014 conference on empirical methods in natural language processing (EMNLP) (pp. 1532–1543).

Qin, Y., Song, D., Chen, H., Cheng, W., Jiang, G., & Cottrell, G. W. (2017). A dual-stage attention-based recurrent neural network for time series prediction. In Proceedings of the Twenty-Sixth International Joint Conference on Artiﬁcial Intelligence, IJCAI-17 (pp. 2627–2633).

Rawat, W., & Wang, Z. (2017). Deep convolutional neural networks for image classiﬁcation: A comprehensive review. Neural computation, 29, 2352–2449.

Reschenhofer, E., Mangat, M. K., Zwatz, C., & Guzmics, S. (2019). Evaluation of current research on stock return predictability. Journal of Forecasting, .

Roshan, W., Gopura, R., & Jayasekara, A. (2011). Financial forecasting based on artiﬁcial neural networks: Promising directions for modeling. In 2011 6th International Conference on Industrial and Information Systems (pp. 322– 327). doi:10.1109/ICIINFS.2011.6038088.

Rundo, F., Trenta, F., di Stallo, A. L., & Battiato, S. (2019). Machine learning for quantitative ﬁnance applications: A survey. Applied Sciences, 9, 5574.

Sabour, S., Frosst, N., & Hinton, G. E. (2017). Dynamic routing between capsules. In Advances in neural information processing systems (pp. 3856– 3866).

Sachdeva, A., Jethwani, G., Manjunath, C., Balamurugan, M., & Krishna, A. V. (2019). An eﬀective time series analysis for equity market prediction using deep learning model. In 2019 International Conference on Data Science and Communication (IconDSC) (pp. 1–5). IEEE.

Sanboon, T., Keatruangkamala, K., & Jaiyen, S. (2019). A deep learning model for predicting buy and sell recommendations in stock exchange of thailand using long short-term memory. In 2019 IEEE 4th International Conference on Computer and Communication Systems (ICCCS) (pp. 757–760). IEEE.

Schumaker, R. P., & Chen, H. (2009). Textual analysis of stock market prediction using breaking ﬁnancial news: The azﬁn text system. Acm Transactions on Information Systems, 27, 1–19.

Selvin, S., Vinayakumar, R., Gopalakrishnan, E. A., Menon, V. K., & Soman, K. P. (2017). Stock price prediction using lstm, rnn and cnn-sliding window model. In 2017 International Conference on Advances in Computing, Communications and Informatics (ICACCI) (pp. 1643–1647). doi:10.1109/ ICACCI.2017.8126078.

Sethia, A., & Raut, P. (2019). Application of lstm, gru and ica for stock price prediction. In S. C. Satapathy, & A. Joshi (Eds.), Information and Communication Technology for Intelligent Systems (pp. 479–487). Singapore: Springer Singapore.

Sezer, O. B., Gudelek, M. U., & Ozbayoglu, A. M. (2019). Financial time series forecasting with deep learning: A systematic literature review: 2005-2019. arXiv preprint arXiv:1911.13288, .

- Sezer, O. B., & Ozbayoglu, A. M. (2018). Algorithmic ﬁnancial trading with deep convolutional neural networks: Time series to image conversion approach. Applied Soft Computing, 70, 525 – 538. URL: http://www.sciencedirect.com/science/article/pii/ S1568494618302151. doi:https://doi.org/10.1016/j.asoc.2018.04.024.
- Sezer, O. B., & Ozbayoglu, A. M. (2019). Financial trading model with stock bar chart image time series with deep convolutional neural networks. arXiv preprint arXiv:1903.04610, .

Shah, D., Isah, H., & Zulkernine, F. (2019). Stock market analysis: A review and taxonomy of prediction techniques. International Journal of Financial Studies, 7, 26.

Sharpe, W. F. (1994). The sharpe ratio. Journal of portfolio management, 21, 49–58.

Siami-Namini, S., Tavakoli, N., & Namin, A. S. (2019). A comparative analysis of forecasting ﬁnancial time series using arima, lstm, and bilstm. arXiv preprint arXiv:1911.09512, .

Siami-Namini, S., Tavakoli, N., & Siami Namin, A. (2018). A comparison of arima and lstm in forecasting time series. In 2018 17th IEEE International Conference on Machine Learning and Applications (ICMLA) (pp. 1394–1401). doi:10.1109/ICMLA.2018.00227.

Sim, H. S., Kim, H. I., & Ahn, J. J. (2019). Is deep learning for image recognition applicable to stock market prediction? Complexity, 2019.

Singh, R., & Srivastava, S. (2017). Stock prediction using deep learning. Multimedia Tools and Applications, 76, 18569–18584. URL: https://doi.org/ 10.1007/s11042-016-4159-7. doi:10.1007/s11042-016-4159-7.

Song, Y., Lee, J. W., & Lee, J. (2019). A study on novel ﬁltering and relationship between input-features and target-vectors in a deep learning model for stock price prediction. Applied Intelligence, 49, 897–911. URL: https://doi.org/ 10.1007/s10489-018-1308-x. doi:10.1007/s10489-018-1308-x.

Stoean, C., Paja, W., Stoean, R., & Sandita, A. (2019). Deep architectures for long-term stock price prediction with a heuristic-based strategy for trading simulations. PloS one, 14.

Sun, H., Rong, W., Zhang, J., Liang, Q., & Xiong, Z. (2017). Stacked denoising autoencoder based stock market trend prediction via k-nearest neighbour data selection. In D. Liu, S. Xie, Y. Li, D. Zhao, & E.-S. M. El-Alfy (Eds.), Neural Information Processing (pp. 882–892). Cham: Springer International Publishing.

Sun, J., Xiao, K., Liu, C., Zhou, W., & Xiong, H. (2019). Exploiting intra-day patterns for market shock prediction: A machine learning approach. Expert Systems with Applications, 127, 272–281.

Tan, J., Wang, J., Rinprasertmeechai, D., Xing, R., & Li, Q. (2019). A tensorbased elstm model to predict stock price using ﬁnancial news. In Proceedings of the 52nd Hawaii International Conference on System Sciences.

Tang, J., & Chen, X. (2018). Stock market prediction based on historic prices and news titles. In Proceedings of the 2018 International Conference on Machine Learning Technologies ICMLT ’18 (pp. 29–34). New York, NY, USA: ACM. URL: http://doi.acm.org/10.1145/3231884.3231887. doi:10.1145/3231884.3231887.

Tang, N., Shen, Y., & Yao, J. (2019). Learning to fuse multiple semantic aspects from rich texts for stock price prediction. In International Conference on Web Information Systems Engineering (pp. 65–81). Springer.

Tausczik, Y. R., & Pennebaker, J. W. (2010). The psychological meaning of words: Liwc and computerized text analysis methods. Journal of language and social psychology, 29, 24–54.

Ticknor, J. L. (2013). A bayesian regularized artiﬁcial neural network for stock market forecasting. Expert Systems with Applications, 40, 5501 – 5506. URL: http://www.sciencedirect.com/science/article/pii/ S0957417413002509. doi:https://doi.org/10.1016/j.eswa.2013.04.013.

Tieleman, T., & Hinton, G. (2012). Lecture 6.5-rmsprop: Divide the gradient by a running average of its recent magnitude. COURSERA: Neural networks for machine learning, 4, 26–31.

Tk´ˇc, M., & Verner, R. (2016). Artiﬁcial neural networks in business: Two decades of research. Applied Soft Computing, 38, 788 – 804. URL: http://www.sciencedirect.com/science/article/pii/ S1568494615006122. doi:https://doi.org/10.1016/j.asoc.2015.09.040.

Tran, D. T., Gabbouj, M., & Iosiﬁdis, A. (2017a). Multilinear class-speciﬁc discriminant analysis. Pattern Recognition Letters, 100, 131–136.

Tran, D. T., Iosiﬁdis, A., Kanniainen, J., & Gabbouj, M. (2018). Temporal attention-augmented bilinear network for ﬁnancial time-series data analysis. IEEE transactions on neural networks and learning systems, 30, 1407–1418.

Tran, D. T., Magris, M., Kanniainen, J., Gabbouj, M., & Iosiﬁdis, A. (2017b). Tensor representation in high-frequency ﬁnancial data for price change prediction. In 2017 IEEE Symposium Series on Computational Intelligence (SSCI) (pp. 1–7). IEEE.

Treisman, A. M., & Gelade, G. (1980). A feature-integration theory of attention. Cognitive psychology, 12, 97–136.

Tsang, G., Deng, J., & Xie, X. (2018). Recurrent neural networks for ﬁnancial time-series modelling. In 2018 24th International Conference on Pattern Recognition (ICPR) (pp. 892–897). doi:10.1109/ICPR.2018.8545666.

Tsantekidis, A., Passalis, N., Tefas, A., Kanniainen, J., Gabbouj, M., & Iosiﬁdis, A. (2017a). Forecasting stock prices from the limit order book using convolutional neural networks. In 2017 IEEE 19th Conference on Business Informatics (CBI) (pp. 7–12). IEEE volume 1.

Tsantekidis, A., Passalis, N., Tefas, A., Kanniainen, J., Gabbouj, M., & Iosiﬁdis, A. (2017b). Using deep learning to detect price change indications in ﬁnancial markets. In 2017 25th European Signal Processing Conference (EUSIPCO) (pp. 2511–2515). IEEE.

Vargas, M. R., de Lima, B. S. L. P., & Evsukoﬀ, A. G. (2017). Deep learning for stock market prediction from ﬁnancial news articles. In 2017 IEEE International Conference on Computational Intelligence and Virtual Environments for Measurement Systems and Applications (CIVEMSA) (pp. 60–65). doi:10.1109/CIVEMSA.2017.7995302.

Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser,  L., & Polosukhin, I. (2017). Attention is all you need. In Advances in neural information processing systems (pp. 5998–6008).

Wang, J., Sun, T., Liu, B., Cao, Y., & Zhu, H. (2019a). Clvsa: A convolutional lstm based variational sequence-to-sequence model with attention for predicting trends of ﬁnancial markets. In Proceedings of the 28th International Joint Conference on Artiﬁcial Intelligence (pp. 3705–3711). AAAI Press.

Wang, J., & Wang, J. (2015). Forecasting stock market indexes using principle component analysis and stochastic time eﬀective neural networks. Neurocomputing, 156, 68 – 78. URL: http: //www.sciencedirect.com/science/article/pii/S0925231215000090.

doi:https://doi.org/10.1016/j.neucom.2014.12.084.

Wang, J.-Z., Wang, J.-J., Zhang, Z.-G., & Guo, S.-P. (2011). Forecasting stock indices with back propagation neural network. Expert Systems with Applications, 38, 14346 – 14355. URL: http: //www.sciencedirect.com/science/article/pii/S0957417411007494.

doi:https://doi.org/10.1016/j.eswa.2011.04.222.

Wang, Y., Li, Q., Huang, Z., & Li, J. (2019b). Ean: Event attention network for stock price trend prediction based on sentimental embedding. In Proceedings of the 10th ACM Conference on Web Science WebSci ’19 (pp. 311–320). New York, NY, USA: ACM. URL: http://doi.acm.org/10.1145/3292522. 3326014. doi:10.1145/3292522.3326014.

Weng, B., Ahmed, M. A., & Megahed, F. M. (2017). Stock market one-day ahead movement prediction using disparate data sources. Expert Systems with Applications, 79, 153–163.

Wu, H., Zhang, W., Shen, W., & Wang, J. (2018). Hybrid deep sequential modeling for social text-driven stock prediction. In Proceedings of the 27th ACM International Conference on Information and Knowledge Management CIKM ’18 (pp. 1627–1630). New York, NY, USA: ACM. URL: http://doi. acm.org/10.1145/3269206.3269290. doi:10.1145/3269206.3269290.

Wu, Y., & Gao, J. (2018). Adaboost-based long short-term memory ensem-

ble learning approach for ﬁnancial time series forecasting. Current Science

(00113891), 115.

Xing, F. Z., Cambria, E., & Welsch, R. E. (2018). Natural language based ﬁnancial forecasting: a survey. Artiﬁcial Intelligence Review, 50, 49–73.

Xiong, Z., Liu, X.-Y., Zhong, S., Yang, H., & Walid, A. (2018). Practical deep reinforcement learning approach for stock trading. arXiv preprint arXiv:1811.07522, .

Xu, Y., & Cohen, S. B. (2018). Stock movement prediction from tweets and historical prices. In Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) (pp. 1970–1979). Melbourne, Australia: Association for Computational Linguistics. doi:10. 18653/v1/P18-1183.

Yan, H., & Ouyang, H. (2018). Financial time series prediction based on deep learning. Wireless Personal Communications, 102, 683–700. URL: https:// doi.org/10.1007/s11277-017-5086-2. doi:10.1007/s11277-017-5086-2.

Yang, B., Gong, Z.-J., & Yang, W. (2017). Stock market index prediction using deep neural network ensemble. In 2017 36th Chinese Control Conference (CCC) (pp. 3882–3887). IEEE.

Yang, H., Zhu, Y., & Huang, Q. (2018). A multi-indicator feature selection for cnn-driven stock index prediction. In L. Cheng, A. C. S. Leung, & S. Ozawa (Eds.), Neural Information Processing (pp. 35–46). Cham: Springer International Publishing.

Yolcu, U., Egrioglu, E., & Aladag, C. H. (2013). A new linear & nonlinear artiﬁcial neural network model for time series forecasting. Decision support systems, 54, 1340–1347.

Yu, M.-H., & Wu, J.-L. (2019). Ceam: A novel approach using cycle embeddings with attention mechanism for stock price prediction. In 2019 IEEE Interna-

tional Conference on Big Data and Smart Computing (BigComp) (pp. 1–4). IEEE.

Zamora, E., & Sossa, H. (2017). Dendrite morphological neurons trained by stochastic gradient descent. Neurocomputing, 260, 420–431.

Zeiler, M. D. (2012). Adadelta: an adaptive learning rate method. arXiv preprint arXiv:1212.5701, .

- Zhan, X., Li, Y., Li, R., Gu, X., Habimana, O., & Wang, H. (2018). Stock price prediction using time convolution long short-term memory network. In W. Liu, F. Giunchiglia, & B. Yang (Eds.), Knowledge Science, Engineering and Management (pp. 461–468). Cham: Springer International Publishing.

- Zhang, J., Rong, W., Liang, Q., Sun, H., & Xiong, Z. (2017a). Data augmentation based stock trend prediction using self-organising map. In D. Liu, S. Xie, Y. Li, D. Zhao, & E.-S. M. El-Alfy (Eds.), Neural Information Processing (pp. 903–912). Cham: Springer International Publishing.
- Zhang, K., Zhong, G., Dong, J., Wang, S., & Wang, Y. (2019a). Stock market prediction based on generative adversarial network. Procedia Computer Science, 147, 400 – 406. URL: http: //www.sciencedirect.com/science/article/pii/S1877050919302789. doi:https://doi.org/10.1016/j.procs.2019.01.256. 2018 International Conference on Identiﬁcation, Information and Knowledge in the Internet of Things.
- Zhang, L., Aggarwal, C., & Qi, G.-J. (2017b). Stock price prediction via discovering multi-frequency trading patterns. In Proceedings of the 23rd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining KDD ’17 (pp. 2141–2149). New York, NY, USA: ACM. URL: http:// doi.acm.org/10.1145/3097983.3098117. doi:10.1145/3097983.3098117.

Zhang, Z., Zohren, S., & Roberts, S. (2019b). Deeplob: Deep convolutional neu-

ral networks for limit order books. IEEE Transactions on Signal Processing, 67, 3001–3012.

- Zhao, Z., Rao, R., Tu, S., & Shi, J. (2017). Time-weighted lstm model with redeﬁned labeling for stock trend prediction. In 2017 IEEE 29th International Conference on Tools with Artiﬁcial Intelligence (ICTAI) (pp. 1210–1217). doi:10.1109/ICTAI.2017.00184.

Zhao, Z.-Q., Zheng, P., Xu, S.-t., & Wu, X. (2019). Object detection with deep learning: A review. IEEE transactions on neural networks and learning systems, 30, 3212–3232.

Zheng, Z., Wu, X., & Srihari, R. (2004). Feature selection for text categorization on imbalanced data. ACM Sigkdd Explorations Newsletter, 6, 80–89.

Zhong, X., & Enke, D. (2017). Forecasting daily stock market return using dimensionality reduction. Expert Systems with Applications, 67, 126 – 139. URL: http://www.sciencedirect.com/science/article/pii/ S0957417416305115. doi:https://doi.org/10.1016/j.eswa.2016.09.027.

Zhou, F., Zhou, H.-m., Yang, Z., & Yang, L. (2019a). Emd2fnn: A strategy combining empirical mode decomposition and factorization machine based neural network for stock market trend prediction. Expert Systems with Applications, 115, 136–151.

Zhou, X., Pan, Z., Hu, G., Tang, S., & Zhao, C. (2018). Stock market prediction on high-frequency data using generative adversarial nets. Mathematical Problems in Engineering, 2018.

Zhou, Z., Gao, M., Liu, Q., & Xiao, H. (2019b). Forecasting stock price movements with multiple data sources: Evidence from stock market in china. Physica A: Statistical Mechanics and its Applications, (p. 123389).

