[Figure 1]

2014 UKSim-AMSS 16th International Conference on Computer Modelling and Simulation

# Stock Price Prediction Using the ARIMA Model

1Ayodele A. Adebiyi., 2Aderemi O. Adewumi

1,2School of Mathematic, Statistics & Computer Science University of KwaZulu-Natal Durban, South Africa

email: {adebiyi, adewumia}@ukzn.ac.za

3Charles K. Ayo

3Department of Computer & Information Sciences Covenant University Ota, Nigeria

email: charles.ayo@covenantuniversity.edu.ng

Abstract— Stock price prediction is an important topic in finance and economics which has spurred the interest of researchers over the years to develop better predictive models. The autoregressive integrated moving average (ARIMA) models have been explored in literature for time series prediction. This paper presents extensive process of building stock price predictive model using the ARIMA model. Published stock data obtained from New York Stock Exchange (NYSE) and Nigeria Stock Exchange (NSE) are used with stock price predictive model developed. Results obtained revealed that the ARIMA model has a strong potential for short-term prediction and can compete favourably with existing techniques for stock price prediction.

Keywords- ARIMA model, Stock Price prediction, Stock market, Short-term prediction.

I. INTRODUCTION

Prediction will continue to be an interesting area of research making researchers in the domain field always desiring to improve existing predictive models. The reason is that institutions and individuals are empowered to make investment decisions and ability to plan and develop effective strategy about their daily and future endevours. Stock price prediction is regarded as one of most difficult task to accomplish in financial forecasting due to complex nature of stock market [1, 2, 3]. The desire of many investors is to lay hold of any forecasting method that could guarantee easy profiting and minimize investment risk from the stock market. This remains a motivating factor for researchers to evolve and develop new predictive models [4].

In the past years several models and techniques had been developed to stock price prediction. Among them are artificial neural networks (ANNs) model which are very popular due to its ability to learn patterns from data and infer solution from unknown data. Few related works that engaged ANNs model to stock price prediction are [5, 6, 7]. In recent time, hybrid approaches has also been engaged to improve stock price predictive models by exploiting the unique strength of each of them [2]. ANNs is from artificial intelligence perspectives.

ARIMA models are from statistical models perspectives. Generally, it is reported in literature that prediction can be done from two perspectives: statistical and artificial

intelligence techniques [2]. ARIMA models are known to be robust and efficient in financial time series forecasting especially short-term prediction than even the most popular ANNs techniques ([8, 9, 10]. It has been extensively used in field of economics and finance. Other statistics models are regression method, exponential smoothing, generalized autoregressive conditional heteroskedasticity (GARCH). Few related works that has engaged ARIMA model for forecasting includes [11, 12, 13, 14, 15, 16].

In this paper extensive process of building ARIMA models for short-term stock price prediction is presented. The results obtained from real-life data demonstrated the potential strength of ARIMA models to provide investors short-term prediction that could aid investment decision making process.

The rest of the paper is organized as follows. Section 2 presents brief overview of ARIMA model. Section 3 describes the methodology used while section 4 discusses the experimental results obtained. The paper is concluded in section 5.

II. ARIMA MODEL

Box and Jenkins in 1970 introduced the ARIMA model. It also referred to as Box-Jenkins methodology composed of set of activities for identifying, estimating and diagnosing ARIMA models with time series data. The model is most prominent methods in financial forecasting [1, 12, 9]. ARIMA models have shown efficient capability to generate short-term forecasts. It constantly outperformed complex structural models in short-term prediction [17]. In ARIMA model, the future value of a variable is a linear combination of past values and past errors, expressed as follows:

## Yt =φ0+φ1Yt−1+φ2Yt−2+...+φpYt−p+εt−θε1 t−1−θε2 t−2−...− θε q t−q

(1) where,

Yt is the actual value and εt is the random error at t, φiand θj are the coefficients, p and q are integers that are often referred to as autoregressive and moving average, respectively.

[Figure 2]

978-1-4799-4923-6/14 $31.00 © 2014 IEEE DOI 10.1109/UKSim.2014.67

[Figure 3]

105

[Figure 4]

[Figure 5]

[Figure 6]

[Figure 7]

The steps in building ARIMA predictive model consist of model identification, parameter estimation and diagnostic checking [18].

III. METHODOLOGY

The method used in this study to develop ARIMA model for stock price forecasting is explained in detail in subsections below. The tool used for implementation is Eviews software version 5. Stock data used in this research work are historical daily stock prices obtained from two countries stock exchanged. The data composed of four elements, namely: open price, low price, high price and close price respectively. In this research the closing price is chosen to represent the price of the index to be predicted. Closing price is chosen because it reflects all the activities of the index in a trading day.

To determine the best ARIMA model among several experiments performed, the following criteria are used in this study for each stock index.

- • Relatively small of BIC (Bayesian or Schwarz Information Criterion)
- • Relatively small standard error of regression (S.E. of regression)
- • Relatively high of adjusted R2
- • Q-statistics and correlogram show that there is no significant pattern left in the autocorrelation functions (ACFs) and partial autocorrelation functions (PACFs) of the residuals, it means the residual of the selected model are white noise.

The subsections below described the processes of ARIMA model-development. A. ARIMA (p, d, q) Model for Nokia Stock Index

Nokia stock data used in this study covers the period from 25th April, 1995 to 25th February, 2011 having a total number of 3990 observations. Figure 1 depicts the original pattern of the series to have general overview whether the time series is stationary or not. From the graph below the time series have random walk pattern.

[Figure 8]

Figure 1: Graphical representation of the Nokia stock closing price index

- Figure 2 is the correlogram of Nokia time series. From the graph, the ACF dies down extremely slowly which simply means that the time series is nonstationary. If the series is not stationary, it is converted to a stationary series by differencing. After the first difference, the series “DCLOSE” of Nokia stock index becomes stationary as shown in figure 3 and figure 4 of the line graph and correlogram respectively.

[Figure 9]

Figure 2: The correlogram of Nokia stock price index

[Figure 10]

- Figure 3: Graphical representation of the Nokia stock price index after differencing.

[Figure 11]

- Figure 4: The correlogram of Nokia stock price index after first differencing

In figure 5 the model checking was done with Augmented Dickey Fuller (ADF) unit root test on “DCLOSE” of Nokia stock index. The result confirms that the series becomes stationary after the first-difference of the series.

[Figure 13]

Figure 5: ADF unit root test for DCLOSE of Nokia stock index.

Table 1 shows the different parameters of autoregressive (p) and moving average (q) among the several ARIMA model experimented upon . ARIMA (2, 1, 0) is considered the best for Nokia stock index as shown in figure 6. The model returned the smallest Bayesian or Schwarz information criterion of 5.3927 and relatively smallest standard error of regression of 3.5808 as shown in figure 6.

|[Figure 14]|
|---|

Figure 6: ARIMA (2, 1, 0) estimation output with DCLOSE of Nokia index.

Figure 7 is the residual of the series. If the model is good, the residuals (difference between actual and predicted values) of the model are series of random errors. Since there are no significant spikes of ACFs and PACFs, it means that the residual of the selected ARIMA model are white noise, no other significant patterns left in the time series. Therefore, there is no need to consider any AR(p) and MA(q) further.

[Figure 15]

Figure 7: Correlogram of residuals of the Nokia stock index.

In forecasting form, the best model selected can be expressed as follows:

Yt =θ1Yt−1 + θ2Yt−2 + εt (2)

∧

εt = Yt −Yt (i.e., the difference between the actual value of the series and the forecast value)

where,

TABLE I: STATISTICAL RESULTS OF DIFFERENT ARIMA PARAMETERS FOR NOKIA STOCK INDEX

|ARIMA|BIC|Adjusted R2|S.E. of Regression|
|---|---|---|---|
|(1, 0, 0)|5.3936|0.9907|3.5824|
|(1, 0, 1)|5.3950|0.9907|3.5817|
|(2, 0, 0)|6.1061|0.9811|5.1157|
|(0, 0, 1)|8.8324|0.7126|19.9942|
|(0, 0, 2)|8.8871|0.6964|20.5490|
|(1, 1, 0)|5.3956|0.0002|3.5860|
|(0, 1, 0)|5.3937|0.0000|3.5859|
|(0, 1, 1)|5.3953|0.0002|3.5854|
|(1, 1,2)|5.3941|0.0035|3.5800|
|(2, 1, 0)|5.3927|0.0033|3.5808|
|(2, 1, 2)|5.3947|0.0031|3.5812|

The bold row represent the best ARIMA model among the several experiments.

B. ARIMA (p, d, q) Model for Zenith Bank Index

The stock data of Zenith bank used in this study covered the period from 3rd January, 2006 to 25th February, 2011 with total of 1296 observations. Figure 8 is the original pattern of the series. From the graph there was upward movement of the index from 2006 and downward movement is observed

from 2008 possibly because of world financial crisis experienced at that time.

[Figure 17]

- Figure 8: Graphical representation of the Zenith Bank stock index closing price.
- Figure 9 is the correlogram of the time series of Zenith

bank stock index. From the graph of the correlogram, the ACF dies down extremely slowly which simply means that the time series is nonstationary. If the series is not stationary, there is need to convert to stationary series by differencing. After the first difference, the series “DCLOSE” of Zenith bank stock index becomes stationary as shown in figure 10 and figure 11 of the line graph and correlogram of the series after first differencing.

|[Figure 18]|
|---|

Figure 9: The correlogram of Zenith Bank stock price index

[Figure 19]

- Figure 10: Graphical representation of the Zenith bank stock index first differencing

|[Figure 20]|
|---|

- Figure 11: The correlogram of Zenith bank stock price index after first differencing.
- Figure 12 is the ADF unit root test on “DCLOSE” of the

series which also indicates the first difference of the series becomes stationary.

[Figure 22]

Figure 12: ADF unit root test for DCLOSE of Zenith bank stock index.

Table 2 shows the different parameters of autoregressive (p) and moveing average (q) of the ARIMA model in order to get the best fitted model. ARIMA (1, 0, 1) is relatively the best model as indicated in figure 13. The model returned the smallest Bayesian or Schwarz information criterion of 2.3736 and relatively smallest standard error of regression of 0.7872 as shown in figure 13.

|[Figure 23]|
|---|

- Figure 13: ARIMA (1, 0, 1) estimation output with DCLOSE of Zenith bank index.
- Figure 14 is the correlogram of residual of the seies. From the figure it is obvious there is no significant spike of ACFs and PACFs. This means that the residual of this selected ARIMA model are white noise. There is no other significant

patterns left in the time series and there is no need for further consideration of another AR(p) and MA(q).

[Figure 24]

Figure 14: Correlogram of residuals of the Zenith bank stock index.

In forecasting form, the best model selected can be expressed as follows: Yt =φ1Yt−1 − θ1εt−1 + εt (3) where,

∧

εt = Yt −Yt (i.e., the difference between the actual value of the series and the forecast value)

TABLE II: STATISTICAL RESULTS OF DIFFERENT ARIMA PARAMETERS FOR ZENITH BANK STOCK INDEX

|ARIMA|BIC|Adjusted R2|S.E. of Regression|
|---|---|---|---|
|(1, 0, 0)|2.4385|0.9970|0.8151|
|(1, 0, 1)|2.3736|0.9972|0.7872|
|(2, 0, 0)|3.3682|0.9925|1.2974|
|(0, 0, 1)|6.9285|0.7372|7.6951|
|(0, 0, 2)|6.9815|0.7228|7.9018|
|(1, 1, 0)|2.3659|0.0708|0.7860|
|(0, 1, 0)|2.4338|0.0000|0.8151|
|(0, 1, 1)|2.3693|0.0669|0.7873|
|(1, 1,2)|2.3714|0.0701|0.7863|
|(2, 1, 0)|2.4370|0.0031|0.8144|
|(2, 1, 2)|2.4412|0.0036|0.8142|

The bold row represent the best ARIMA model among the several experiments

IV. RESULTS AND DISCUSSION

The experimental results of each of stock index are discussed in the subsection below.

A. Result of ARIMA Model for Nokia Stock Price Prediction Table 3 is the result of the predicted values of ARIMA

(2, 1, 0) considered the best model for Nokia stock index.

- Figure 15 gives graphical illustration of the level accuracy of the predicted price against actual stock price to see the performance of the ARIMA model selected. From the graph, is obvious that the performance is satisfactory.

TABLE III: SAMPLE OF EMPIRICAL RESULTS OF ARIMA (2,1,0) OF NOKIA STOCK INDEX.

|Sample Period|Actual Values|Predicted Values|
|---|---|---|
|1/3/2010|13.28|13.58|
|2/3/2010|13.51|13.69|
|3/3/2010|13.86|13.80|
|4/3/2010|13.78|13.91|
|5/3/2010|14.13|14.02|
|8/3/2010|14.17|14.13|
|9/3/2010|14.12|14.24|
|10/3/2010|14.56|14.35|
|11/3/2010|14.49|14.45|
|12/3/2010|14.84|14.56|
|15/3/2010|14.81|14.67|
|16/3/2010|15.14|14.77|
|17/3/2010|15.42|14.88|
|18/3/2010|15.28|14.98|
|19/3/2010|15.07|15.09|
|22/3/2010|15.11|15.19|
|23/3/2010|15.26|15.30|
|24/3/2010|15.07|15.40|
|25/3/2010|15.20|15.50|
|26/3/2010|15.46|15.60|
|29/3/2010|15.42|15.71|
|30/3/2010|15.41|15.81|
|31/3/2010|15.54|15.91|

[Figure 26]

Figure 15: Graph of Actual Stock Price vs Predicted values of Nokia Stock Index

B. Result of ARIMA Model for Zenith Bank Stock Price Prediction

In this case, ARIMA (1, 0, 1) was selected as the best model for Zenith bank stock index after several adjustment of the autoregressive (p) and moving average (q) parameters in Eviews software used. Table 4 contained the predicted values of the model selected and figure 16 is the graph of predicted price against actual stock price to demonstrate the correlation of accuracy. From the graph, the performance of the ARIMA model selected is quite impressive as there are some instances of closely related of actual and predicted values.

TABLE IV: SAMPLE OF EMPIRICAL RESULTS OF ARIMA (1,0,1) OF ZENITH BANK INDEX

|Sample Period|Actual Values|Predicted Values|
|---|---|---|
|1/3/2010|16.19|15.83|
|2/3/2010|15.98|15.86|
|3/3/2010|15.71|15.89|
|4/3/2010|15.50|15.91|
|5/3/2010|15.70|15.94|
|8/3/2010|15.75|15.97|
|9/3/2010|15.86|15.99|
|10/3/2010|16.00|16.02|
|11/3/2010|16.19|16.05|
|12/3/2010|16.99|16.08|
|15/3/2010|17.83|16.10|
|16/3/2010|17.71|16.13|
|17/3/2010|17.50|16.16|
|18/3/2010|16.85|16.18|
|19/3/2010|17.69|16.21|
|22/3/2010|18.00|16.24|
|23/3/2010|18.00|16.26|
|24/3/2010|17.85|16.29|
|25/3/2010|17.89|16.31|
|26/3/2010|18.11|16.34|
|29/3/2010|19.01|16.37|
|30/3/2010|19.96|16.39|
|31/3/2010|18.97|16.42|

[Figure 28]

- Figure 16: Graph of Actual Stock Price vs Predicted values of Zenith Bank Stock Index

V. CONCLUSION

This paper presents extensive process of building ARIMA model for stock price prediction. The experimental results obtained with best ARIMA model demonstrated the potential of ARIMA models to predict stock prices satisfactory on short-term basis. This could guide investors in stock market to make profitable investment decisions. With the results obtained ARIMA models can compete reasonably well with emerging forecasting techniques in short-term prediction.

REFERENCES

- [1] P. Pai and C. Lin, “A hybrid ARIMA and support vector machines model in stock price prediction”, Omega vol.33 pp. 497-505, 2005
- [2] J.J. Wang, J.Z. Wang, Z.G. Zhang and S.P. Guo, “Stock index forecasting based on a hybrid model”, Omega vol.40 pp.758-766, 2012.
- [3] L.Y. Wei, “A hybrid model based on ANFIS and adaptive expectation genetic algorithm to forecast TAIEX”, Economic Modelling vol. 33 pp. 893-899, 2013.

- [4] G.S. Atsalakis, E.M Dimitrakakis. and C.D. Zopounidis, “Elliot Wave Theory and neuro-fuzzy systems, stock market prediction: The WASP system”, Expert Systems with Applications, vol. 38, pp.9196– 9206, 2011.
- [5] S. K.Mitra, “Optimal Combination of Trading Rules Using Neural Networks”, International Business Research, vol. 2, no. 1, pp. 86-99, 2009.
- [6] G.S. Atsalakis and P.V. Kimon, “Forecasting stock market short-term trends using a neuro-fuzzy methodology”, Expert Systems with Applications, vol. 36, no. 7, pp.10696–10707, 2009.
- [7] M.M. Mohamed, “Forecasting stock exchange movements using neural networks: empirical evidence from Kuwait”, Expert Systems with Applications, vol. 27, no. 9, pp.6302–6309, 2010.
- [8] L.C. Kyungjoo, Y. Sehwan and J. John, “Neural Network Model vs. SARIMA Model In Forecasting Korean Stock Price Index (KOSPI), Issues in Information System, vol. 8 no. 2, pp. 372-378, 2007.
- [9] N. Merh, V.P. Saxena, and K.R. Pardasani, “A Comparison Between Hybrid Approaches of ANN and ARIMA For Indian Stock Trend Forecasting”, Journal of Business Intelligence, vol. 3, no.2, pp. 23-43, 2010.
- [10] J. Sterba and Hilovska, “The Implementation of Hybrid ARIMA Neural Network Prediction Model for Aggregate Water Consumption Prediction”, Aplimat- Journal of Applied Mathematics, vol.3, no.3, pp.123-131, 2010.
- [11] C. Javier, E. Rosario, J.N. Francisco and J.C. Antonio, “ARIMA Models to Predict Next Electricity Price”, IEEE Transactions on Power Systems vol. 18 no.3, pp.1014-1020, 2003.
- [12] N. Rangan and N. Titida, “ARIMA Model for Forecasting Oil Palm Price”, Proceedings of the 2nd IMT-GT Regional Conference on Mathematics, Statistics and Applications, Universiti Sains Malaysia, 2006.
- [13] M. Khasel, M. Bijari, and G.A.R Ardali, , “Improvement of AutoRegressive Integrated Moving Average models using Fuzzy logic and pp. 956-967, 2009.
- [14] C. Lee, C. Ho, “Short-term load forecasting using lifting scheme and ARIMA model”, Expert System with Applications, vol.38, no.5, pp.5902-5911, 2011.
- [15] M. Khashei, M. Bijari, G. A. R. Ardal, “Hybridization of autoregressive integrated moving average (ARIMA) with probabilistic neural networks”, Computers and Industrial Engineering, vol. 63, no.1, pp.37-45, 2012
- [16] C. Wang, “A comparison study of between fuzzy time series model and ARIMA model for forecasting Taiwan Export”, Expert System with Applications, vol.38, no.8, pp.9296-9304, 2011.
- [17] A. Meyler, G. Kenny and T. Quinn, “Forecasting Irish Inflation using ARIMA Models”, Central Bank of Ireland Research Department, Technical Paper, 3/RT/1998.
- [18] B.G. Tabachnick and L.S. Fidell, “Using multivariate statistics”, 4th ed., Person Education Company, USA 2001.

