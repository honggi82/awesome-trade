NBER WORKING PAPER SERIES

AGGREGATE AND FIRM-LEVEL STOCK RETURNS DURING PANDEMICS, IN REAL TIME

Laura Alfaro Anusha Chari Andrew N. Greenland Peter K. Schott

Working Paper 26950 http://www.nber.org/papers/w26950

NATIONAL BUREAU OF ECONOMIC RESEARCH 1050 Massachusetts Avenue Cambridge, MA 02138 April 2020

This paper is preliminary and incomplete. We thank Nick Barberis, Lorenzo Caliendo, Patrick Conway, Teresa Fort, Mihai Ion, Ed Kaplan, John Lopresti, and seminar participants from Duke and UNC TEAM working group as well as the CEPR Covid-Economics virtual seminar series for comments and suggestions. We thank Alex Schott and Mengru Wang for excellent research assistance. The views expressed herein are those of the authors and do not necessarily reflect the views of the National Bureau of Economic Research.

NBER working papers are circulated for discussion and comment purposes. They have not been peerreviewed or been subject to the review by the NBER Board of Directors that accompanies official NBER publications.

© 2020 by Laura Alfaro, Anusha Chari, Andrew N. Greenland, and Peter K. Schott. All rights reserved. Short sections of text, not to exceed two paragraphs, may be quoted without explicit permission provided that full credit, including © notice, is given to the source.

Aggregate and Firm-Level Stock Returns During Pandemics, in Real Time Laura Alfaro, Anusha Chari, Andrew N. Greenland, and Peter K. Schott NBER Working Paper No. 26950 April 2020, Revised May 2020 JEL No. E27,F1,G12

## ABSTRACT

We show that unexpected changes in the trajectory of COVID-19 infections predict US stock returns, in real time. Parameter estimates indicate that an unanticipated doubling (halving) of projected infections forecasts next-day decreases (increases) in aggregate US market value of 4 to 11 percent, indicating that equity markets may begin to rebound even as infections continue to rise, if the trajectory of the disease becomes less severe than initially anticipated. Using the same variation in unanticipated projected cases, we find that COVID-19-related losses in market value at the firm level rise with capital intensity and leverage, and are deeper in industries more conducive to disease transmission. These relationships provide important insight into current record job losses. Measuring US states' drops in market value as the employment weighted average declines of the industries they produce, we find that states with milder drops in market value exhibit larger initial jobless claims per worker. This initially counter-intuitive result suggests that investors value the relative ease with which labor versus capital costs can be shed as revenues decline.

Laura Alfaro Harvard Business School Morgan Hall 263 Soldiers Field Boston, MA 02163 and NBER lalfaro@hbs.edu

Anusha Chari 301 Gardner Hall CB#3305, Department of Economics University of North Carolina at Chapel Hill Chapel Hill, NC 27599 and NBER achari@unc.edu

Andrew N. Greenland Elon University 50 Campus Drive Elon, NC 27244 agreenland@elon.edu

Peter K. Schott Yale School of Management 165 Whitney Avenue New Haven, CT 06511 and NBER peter.schott@yale.edu

# 1 Introduction

The tension between Wall-Street and Main Street during the COVID-19 pandemic is palpable. In the early weeks of the outbreak, US equity markets dropped 35 percent. Then, even as reported infections continued to rise, and jobless claims surged, the stock market rallied. In this paper we investigate how information about the expected impact of pandemics is incorporated into aggregate and ﬁrm-level stock returns, day by day. Our results provide a rationale for the seemingly divergent paths of the US equity and labor markets.

We begin by showing that unanticipated changes in predicted infections based on daily reestimation of simple epidemiological models of infectious disease forecast next-day stock returns. While our focus is on the current COVID-19 crisis in the United States, we ﬁnd a similar pattern during the 2003 SARS outbreak in Hong Kong. In each case, larger changes in model predictions are associated with greater changes in market returns, in both directions.1

Estimates for the United States thus far indicate that a doubling (halving) of predicted COVID19 infections is associated with a decline (increase) of 4 to 10 percent in the Wilshire 5000 index. These ﬁndings are consistent with investors using such models to update their beliefs about the economic consequences of the outbreak, in real time. They suggest that equity markets may partially recover, and become less responsive to new cases, if the trajectory of the pandemic becomes less severe than initially anticipated, and more certain. As a consequence, they provide an explanation for the confusion expressed in recent newspaper articles about the recovery of the US stock market in April: this recovery coincides with a ﬂattening out of unanticipated changes in predicted infections.2

We use the same variation in predicted infections to examine exposure to COVID-19 at the industry and ﬁrm levels. We show that industries more conducive to virus transmission – Accommodations, Entertainment and Transportation – exhibit the greatest exposure to the pandemic, and the largest declines in market value. Education, Professional Services and Finance, by contrast, are less sensitive, likely due to a greater ability to continue operations online. At the ﬁrm level, we ﬁnd that COVID-19-driven changes in market value are almost universally negative, that they vary widely both within and across sectors, and that more capital-intensive, more debt-laden, and less proﬁtable ﬁrms exhibit larger declines.3

We interpret these results as signaling investors’ expectation that ﬁrms which are more able to shed costs during the pandemic will have smaller losses, and thus relatively higher returns.4 As debt is non-dischargable, and nearly all property, plant and equipment is sunk in a macroeconomic downturn of COVID-19’s magnitude, debt-laden and capital-intensive ﬁrms are less likely to be able to reduce costs as revenues decline. Labor-intensive ﬁrms’ relatively high returns, by contrast, reﬂect the relative ease with which workers (versus capital) can be furloughed or dismissed as the economy contracts.

Further evidence in favor of this mechanism comes from an analysis of jobless claims across regions. We construct county- and state-level measures of equity market exposure to COVID-19 as the employment weighted average COVID-19-related change in market value across the 4-digit NAICS sectors they produce (Bartik, 1991). We interpret this exposure as the translation of

- 1We are expanding the set of countries we analyze for the COVID-19 outbreak, and are investigating other pandemics, e.g., the 2009 H1N1 outbreak. These results will appear in a future draft.
- 2See, for example, “Prescient or Pollyannaish? Explaining the Market’s Rally” in the April 18, 2020 edition of the Wall Street Journal.
- 3Ramelli and Wagner (2020) and Albuquerque et al. (2020) also document the negative association between market returns and debt during COVID-19.
- 4Baker et al. (2020) show that a near ubiquitous decline in US consumption during late March and April.

unanticipated news about the pandemic from ﬁrms to states.

Using a diﬀerence-in-diﬀerences speciﬁcation, we demonstrate that states with milder average declines in market value exhibit greater growth in initial jobless claims per worker. This initially counter-intuitive ﬁnding is consistent with the negative relationship between ﬁrm capital intensity, leverage and market returns noted above. Highly leveraged, more capital-intensive ﬁrms likely have less ﬂexibility with respect to reducing costs during the pandemic than labor-intensive ﬁrms, as property, plant and equipment cannot be shed as easily as labor during the extreme economic contraction. Thus, states with a greater proportion of labor-intensive ﬁrms exhibit less decline in average market value, but greater proportional shedding of workers. To the best of our knowledge, we are the ﬁrst to use equity prices to quantify the spatial incidence of a macroeconomic shock, and among the ﬁrst to examine regional variation in COVID-19-driven initial jobless claims.5

Our analysis contributes to several literatures. First, we add to the very large body of research on asset pricing that examines the predictability of stock returns (e.g. Campbell and Shiller (1988), Fama and French (1988)) and, more speciﬁcally, to recent research examining the ﬁnancial market consequences of COVID-19, lead by Ramelli and Wagner (2020). One set of papers in this burgeoning literature associates Ball and Brown (1968) and Fama et al. (1969) style abnormal returns during the pandemic to various ﬁrm characteristics.6 A second group seeks to identify channels of ﬁrm exposure via ex-ante observable ﬁrm or aggregate characteristics.7

While similar in spirit, our analysis diﬀers from these two sets of papers both methodologically and quantitatively, as we relate returns to exogenous changes in investors’ information about the trajectory of the pandemic, as it unfolds. Speciﬁcally, we model cumulative infections during an outbreak as following either an exponential or a logistic curve. We re-estimate the parameters of these models each day of the outbreak using information on reported cases up to that day. More precisely, we predict infections for trading day t using the cumulative counts as of the end of days t − 1 and t − 2. The diﬀerences in these forecasts represent unanticipated changes in the trajectory of the disease due to newly available information, and we examine how they covary with both aggregate and ﬁrm-level market returns on day t.8

As a robustness exercise, we demonstrate that the information in daily predicted infections dominates the most recent change in reported infections in forecasting stock returns. This dominance is understandable, in that the anticipated portion of the most recent reported case growth has already been priced into equities. It is precisely the unanticipated portion of this growth, however, that updates investors’ expectations regarding the eventual number of infections, the speed with which that number may be reached, and the associated economic consequences. Indeed, jumps in estimated share of the population that ultimately will be infected, or the growth rate of infections, signal larger potential declines in demand for goods and services, especially those which might facilitate transmission. Changes in these parameters may also indicate greater shocks to labor supply due to sickness or implementation of social distancing policies, further hampering aggregate demand (Guerrieri et al., 2020). In a related robustness exercise, we show that our results for the United States are robust to the inclusion of coarse controls for changes in federal and local policy.

Relative to existing research on the ﬁnancial implications of COVID-19, our approach oﬀers

5Closely related is Greenland et al. (2019) who use equity market derived measures to explore the employment consequences of the United States’ granting Permanent Normal Trade Relations to China in 2001.

- 6See, for example, Ramelli and Wagner (2020); Albuquerque et al. (2020); Ru et al. (2020).
- 7See, for example, Baker et al. (2020); Fahlenbrach et al. (2020); Ding et al. (2020); ? 8We emphasize that we are not epidemiologists and are not outlining a method to characterize the true path of

pandemics. Nor are we, like Piguillem and Shi (2020) and Berger et al. (2020), trying to infer the eﬃcacy of various intervention strategies. Such eﬀorts, while of immense value, require data which may not be available until after the outbreak is substantially underway. Rather, we view real-time changes in the predicted severity of an outbreak as potentially useful summary statistics of its ultimate economic consequences.

three beneﬁts. First, it does not require us to calculate ﬁrms’ expected normal rate of return with the aid of an asset pricing model – e.g. the CAPM (Sharpe, 1964a) – estimated during a period before COVID-19. In fact, estimates of abnormal returns utilizing such models may be misspeciﬁed if their true values can be inferred only in the presence of disaster risk (Bai et al., 2019). Second, our approach yields ﬁrm-level measures of exposure without identifying their channels ex-ante, and without attributing all aggregate movement in returns to COVID-19. Given the unprecedented nature of this event, this beneﬁt is sizeable. Finally, by exploiting changes in the forecasted trajectory of the pandemic between market close on day t − 1 and opening on day t, our approach exploits only new information about the trajectory of the pandemic and therefore can rationalize both market upswings and downturns. Our ﬁndings suggest that investors, facing substantial uncertainty about the true economic fallout of this realized tail risk (Knight, 1921; Keynes, 1937), may be availing themselves of changes in daily case forecasts as a summary statistic for the ultimate scale and economic fallout of the epidemic.

Our paper also contributes to the very large literature in public health which attempts to explain the trajectory of infections during a pandemic.9 In contrast to that research, we link changes in the estimated parameters and predictions of these models in real time to economic outcomes. To reiterate, we do not claim that the evolution of a pandemic must follow a purely exponential or logistic growth path. Rather, we explore whether the predictions of these models are informative of economic conditions, as manifest in their correlation with the market.10

Finally, this paper relates to a rapidly emerging literature studying the aggregate economic consequences of COVID-19, and a more established literature investigating earlier pandemics. Barro et al. (2020) draws parallels between COVID-19 and the “Spanish Flu” to forecast changes in economic activity, while Baker et al. (2020) documents that the COVID-19 pandemic is the ﬁrst infectious disease outbreak whose mention in the press is associated with a large daily market movement. Our analysis complements the equity market studies of Gormsen and Koijen (2020) and Baker et al. (2020), who link COVID-19 ﬁnancial market reactions to future GDP growth. It also relates to the labor market studies of Cajner et al. (2020) and Coibion et al. (2020), which analyze employment trends during COVID-19, and the examinations of labor market interactions during COVID-19 more directly in Humphries et al. (2020) and Bartik et al. (2020). In contrast to these eﬀorts, we exploit exogenous variation in investors’ expectations about the pandemic’s trajectory to identify aggregate and ﬁrm-level exposure, which we then link to labor market outcomes.

This paper proceeds as follows. Section 2 provides a brief description of infectious disease models and how investors might link the predictions of these models and to asset prices. Sections 3 and 4 apply our framework to COVID-19 and SARS. Section 5 concludes.

# 2 Modeling

In this section we outline how infectious disease outbreaks can be modeled in real time, and how investors might make use of the model’s estimated parameters.

### 2.1 Simple Models of Infectious Diseases

Exponential and logistic growth models are frequently used in biology and epidemiology to model infection and mortality. An exponential model,

9Early contributions to this literature include Ross (1911), Kermack and McKendrick (1927), Kermack and McKendrick (1937) and Richards (1959).

10For an interesting discussion on the complexities associated with modeling an outbreak in real time, see https: //fivethirtyeight.com/features/why-its-so-freaking-hard-to-make-a-good-covid-19-model/.

Ct = ae(rt) (1)

predicts the cumulative number of cases on day t, Ct, as a function of the growth rate of infections in that country, r, the initial number of infected persons a, and time. In an exponential model, the number of infections per day continues to climb indeﬁnitely. While clearly unrealistic ex-post, the exponential growth model is consistent with early stage pandemic growth rates.

In a logistic model (Richards, 1959), by contrast, the growth in infections grows exponentially initially, but then declines as the stock of infections approaches the population’s “carrying-capacity,” i.e., the cumulative number of people that ultimately will be infected. Carrying capacity is generally less than the full population. The cumulative number of infections on day t is given by

k

Ct =

1 + ce(−rt), (2) where k is the carrying, c is a shift parameter (characterizing the number of initially infected persons) and r is the growth rate. Figure 1 provides an example of logistic infections for three diﬀerent growth rates (2.5, 5 and and 7.5 percent) assuming k = 250 and c = 50. For each growth rate, we plot both the number of new cases each day (right axis) and the cumulative number of cases up to each day (left axis). As indicated in the ﬁgure, higher growth rates both shorten the time required to reach carrying capacity and increase the peak number of infections.

Figure 1: New and Cumulative New Cases Under the Logistic Model

[Figure 1]

Source: Authors’ calculations. Figure compares new and cumulative infections from days 1 to 200 assuming a logistic model with k = 250 and c = 50 and noted growth rates (r).

Given data on the actual evolution of infections, the two parameters in equation 1 and the three parameters in equation 2 can be updated each day using the sequence of infections up to that date. We estimate these sequences using STATA’s nonlinear least squares command (nl).11 This command requires a vector of starting values, one for each parameter to be estimated.

We encounter two problems during our estimation of logistic functions in our applications below. First, estimates for each day t are sensitive to the choice of starting values for that day, particularly in the initial days of the pandemic. This feature of the estimation is not surprising: when the number of cases is relatively small, a wide range of logistic curves may be consistent with the data, and the objective function across them may be relatively ﬂat.

11We are exploring other estimation procedures for use in a future draft, including use of SIR and SEIR models, e.g., Li et al. (2020) and Atkeson (2020).

To increase the likelihood that our parameter estimates represent the global solution, we estimate 500 epidemiological models for each day, 250 for the logistic case, and 250 for the exponential case. In each iteration we use a diﬀerent vector of starting values. For each day t, our ﬁrst starting values are the estimated coeﬃcients from the prior day, if available.12 In the case of the logistic model, we then conduct a grid search deﬁned by all triples {r,c,k} such that

r ∈ {0.01,0.21,0.41,0.61,0.81} c ∈ { ct−1,2 ∗ ct−1,4 ∗ ct−1,...,10 ∗ ct−1} k ∈ { kt−1,2 ∗ kt−1,3 ∗ kt−1,...,10 ∗ kt−1

where hats over variables indicate prior estimates, and superscripts indicate the day on which they are estimated. If more than one of these initial starting values produces estimates, we choose the parameters from the model with the highest adjusted R2. We estimate the exponential model similarly.

The second, more interesting, problem that we encounter during estimation of the logistic outbreak curves is that STATA’s nl routine may fail to converge. This failure generally occurs in the transition from relatively slow initial growth to subsequent, more obviously exponential growth

- as the pandemic proceeds. During this phase of the outbreak, the growth in the number of new cases each day is too large to ﬁt a logistic function, i.e., the drop in the growth of new cases necessary to estimate a carrying capacity has not yet occurred.13

In our application below, we re-estimate both exponential and logistic parameters each day of an outbreak. To ﬁx ideas, we simulate a 200-day cumulative logistic disease outbreak by generating a sequence of Ct = 1+cek(−rt) + | t| for t ∈ (1 : 200), assuming k = 250, r = .025, c = 50 and | t| is the absolute value of a draw from a standard normal distribution. For each day t, we estimate logistic and exponential parameters using the sequence of simulated infections up to that day.

Figure 2 displays the results. Both sets of parameter estimates are volatile in the early stage of the outbreak. Logistic parameters are not available from days 47 through 78 due to lack on convergence, but settle down shortly thereafter, as the data increasingly conform to underlying logistic path. Exponential parameters are available for each day, but do not settle down as time goes on. The intuition for the unending increase in at and decline in rt is as follows: because the simulated data are logistic, the only way to reconcile them with an exponential function is to have the estimate of initial exposure ( at) rise as the estimate of the growth rate, rt, drops.

- 12If the prior day did not converge, we use the most recent prior day for which we have estimates.
- 13In a future draft we will consider an estimation strategy that nests these functions.

#### Figure 2: Parameter Estimates Using Simulated Logistic Pandemic

[Figure 2]

Source: authors’ calculations. The left panel plots the sequence of logistic parameters, kt, ct and rt, estimated using the information up to each day t on simulated data (see text). Right panel of Figure plots the analogous sequence of exponential parameters, at and rt, using the same data. Missing estimates indicate lack of convergence (see text). Circles represent estimates. Solid lines connect estimates.

Figure 3 compares predicted cumulative cases for each model for each day t using the parameter

estimates from day t − 1. We denote these predictions Ctt−1, where the superscript t − 1 refers to the timing of the information used to make the prediction, and the subscript refers to the day being predicted. As illustrated in the ﬁgure, predictions for the two models line up reasonably well during the initial phase of the pandemic. Their 95 percent conﬁdence intervals (not shown) cease overlapping on t = 104. After this point, the exponential model continues to project an ever-increasing number of infections, while the logistic model’s predictions head towards the “true” carrying capacity of 250.

Figure 3: Simulated Pandemic Daily Predictions ( Ctt−1)

[Figure 3]

Source: authors’ calculations. Figure compares simulated “actual” cumulative infections to predicted infections ( Ctt−1) under the logistic and exponential models. The prediction for each day t is based on the information available up to day t − 1. The two vertical lines in the ﬁgure note when the 95 percent conﬁdence intervals of the two models’ predictions (not shown) initially diverge, and when the logistic model’s estimates ﬁrst indicate that its inﬂection point has passed.

### 2.2 Modeling Economic Impact

Predicted cumulative cases for day t based on day t−1 information, Ctt−1, can be compared to the day t forecast made with day t − 2 information, Ctt−2. The log diﬀerence in these predictions,

∆ln Ct−2,−1 = ln Ctt−1 − ln Ctt−2 , (3)

captures unexpected changes in severity of the outbreak between these two days.14 This potentially noisy “news” may be an important input into investors’ assessment of the economic impact of a pandemic. For example, jumps in estimated growth rates or carrying capacites signal larger potential declines in demand, reducing ﬁrm revenue. Increases in these parameters may also presage more substantial declines in labor supply, or the implementation of social distancing policies that further reduce demand (Guerrieri et al., 2020).

# 3 Application to COVID-19

In this section we provide real-time estimates of the outbreak parameters and infection predictions for COVID-19 in the United States. We then examine the relationship between changes in these predictions and both aggregate and ﬁrm-level returns in the United States.

### 3.1 Epidemiological Model Paremeters

Data on the cumulative number of COVID-19 cases in the United States as of each day are from the Johns Hopkins Coronavirus Resource Center.15 The ﬁrst COVID-19 case appeared in China in November of 2019, while the ﬁrst cases in the United States and Italy appeared on January 20, 2020. Our analysis begins on January 22, 2020, the ﬁrst day that the World Health Organization began issuing situation reports detailing new case emergence internationally. Appendix Figure A.1 displays the cumulative reported infections in the United States from January 22 through April 10, 2020.

We estimate logistic and exponential parameters (equations 1 and 2) for the United States by day as discussed in Section 2.1. The daily parameter estimates for the logistic estimation, kt, ct and rt are displayed the left panel of Figure 4, while those for the exponential model, at and rt, are reported in the right panel. Gaps in the time series in either ﬁgure represent lack of convergence.

Logistic parameter estimates for the United States fail to converge after February 23, when the number of cases jumps abruptly from 15 to 51. That no parameter estimates are available after this date suggests that growth in new cases observed thus far is inconsistent with a leveling oﬀ, or carrying capacity, at least according to our estimation method. The exponential model, by contrast, converges for all days. As a result, we focus on the exponential model for the remainder of our analysis.

As the sharp changes in US exponential model parameters suggest, predicted cumulative infections vary substantially depending upon the day in which the underlying parameters are estimated.

- 14Timing is as follows: the number of infections on day t − 1 is observed after the market closes on that day but

before the market opens on day t. This day t − 1 information is used to predict the number of cases for day t, Ctt−1, which is compared to Ctt−2.

- 15These data can be downloaded from https://github.com/CSSEGISandData/COVID-19 and visualized at https:

//coronavirus.jhu.edu/map.html.

#### Figure 4: Parameter Estimates for COVID-19

[Figure 4]

Source: Johns Hopkins Coronavirus Resource Center and authors’ calculations. The left panel plots the sequence of logistic parameters, kit, cit and rit, estimated using the cumulative infections in the US up to each day t. Right panel plots the analogous sequence of exponential parameters, ait and rit, using the same data. Missing estimates indicate lack of convergence (see text). Circles represent estimates. Solid lines connect estimates. Data currently extend to Friday March 27, 2020.

Figure 5 highlights this variability by comparing predicted cumulative infections based on the information available as of February 29 and March 7, 13, 21 and 28. The left panel displays these projections in levels, while the right panel uses a log scale. The ﬁve colored lines in the ﬁgure trace out each set of predictions. Dashed lines highlight 95 percent conﬁdence intervals around these predictions. Finally, the conﬁdence intervals are shaded for all days following the day upon which the prediction is based. To promote readability, we restrict the ﬁgure to the period after February 29. The black, solid line in the ﬁgure represents actual reported cases.

Figure 5: Predicted Cumulative Cases Using Diﬀerent Days’ Estimates (COVID-19)

[Figure 5]

Source: Johns Hopkins Coronavirus Resource Center and authors’ calculations. Figure displays predicted cases for the United States from March 18 onwards using the cumulative reported cases as of ﬁve dates: February 29, March 7, March 13, March 21 and March 28. Dashed lines represent 95 percent conﬁdence intervals. Conﬁdence intervals are shaded for all days after the information upon which the predictions are based.

Predicted cumulative infections based on information as of February 29 are strikingly lower than predictions based on information as of March 21 due to the jump in reported cases between those days. Indeed, according to the parameter estimates from March 21, US cases would number close to 300 thousand by the end of March. Equally striking is the downward shift in predicted cumulative cases that occurs between March 21 and March 28. It is precisely these kinds of changes in predicted cumulative cases that our analysis seeks to exploit.

Figure 6 uses the exponential parameter estimates in Figure 4 to plot Ctt−1 and Ctt−2, i.e., the predicted number of cases on day t using the information up to day t−1 and day t−2. Magnitudes for these cumulative cases are reported on the left axis.

#### Figure 6: Daily Logistic Predictions ( Ctt−1 and ∆ln( Ct−2,−1)) for COVID-19

[Figure 6]

Source: Johns Hopkins Coronavirus Resource Center and authors’ calculations. Left axis reports the predicted cumulative cases for day t

using information as of day t − 1, Ctt−1, and day t − 2, Ctt−2, under the exponential model. Right axis reports the log change in these two

predictions, ∆ln( Ct−2,−1). Data currently extend to Friday April 10, 2020.

The right axis in Figure 6 reports ∆( Ct−2,−1), the log diﬀerence in these two predictions. Intu-

itively, Ctt−1 and Ctt−2 for the most part track each other closely. The former rises above the latter on days when reported cases jump, while the reverse happens when new cases are relatively ﬂat.

The scalloped pattern of exhibited by Ctt−2 after March 25 captures the relatively smooth decline in ait and rise in rit (displayed in Figure 4) required for the exponential function to capture the increasingly logistic data.

### 3.2 Aggregate US Returns During COVID-19

We examine the link between changes in model predictions and aggregate US stock via the Wilshire 5000 index.16 We choose this index for its breadth, but note that results are qualitatively similar for other US market indexes.

Figure 7 plots the daily log change in the Wilshire 5000 index against unanticipated increases

in cases, ∆ln( Ct−2,−1). Their negative relationship indicates that returns are higher when the diﬀerence in predictions is lower, and vice versa. In particular, the approximate 20 percent decline in predicted cases that occurs on March 24 coincides with a greater than 9 percent growth in the market index.

We compare aggregate equity returns on day t to the diﬀerence in forecasts for that day formally using an OLS regression,

∆ln(Indext) = α + γ1 ∗ ∆ln Ct−2,−1 + γ2Xt + t. (4)

where ∆ln(Indext) is the daily log change in either opening-to-opening or closing-to-closing prices in the Wilshire 5000, and Xt represents a vector of controls, e.g., changes in policy.17 The estimation period consists of 52 trading days from January 22 to April 10.18 The unit of observation is one

16Data for the Wilshire 5000 are downloaded from Yahoo Finance. 17We are currently exploring more ﬂexible speciﬁcations, e.g., those which might capture the switch between

exponential and logistic models, as well as those which reveal any over- or undershooting of reactions. 18The actual number of trading days between these two dates is 50. We lose 3 days due to lack of estimates in the

#### Figure 7: Change in Predicted COVID-19 Cases (∆ Ct−2,−1) vs Aggregate Market Returns

[Figure 7]

Source: Johns Hopkins Coronavirus Resource Center, Yahoo Finance and authors’ calculations. Figure displays the daily log change in the Wilshire 5000 index against the log change in predicted cases under the exponential model for day t based on day t−1 and day t−2 information. Sample period is January 22 to April 10, 2020.

day.

Table 1: Changes in Predicted COVID-19 Cases (∆ Ct−1,−2) vs Market Open Returns

(1) (2) (3) (4) (5) (6) ∆Ln(Open) ∆Ln(Open) ∆Ln(Open) ∆Ln(Open) ∆Ln(Open) ∆Ln(Open)

∆Ln( C−2,−1) -0.040∗∗∗ -0.049∗∗ -0.061∗∗ -0.063∗∗ -0.085∗∗ -0.055∗∗

(0.013) (0.024) (0.024) (0.025) (0.033) (0.025) ∆Ln(C−2,−1) 0.019 0.026 0.028 0.006

(0.028) (0.026) (0.026) (0.033) I(∆SIndex) -0.014

(0.014) ∆Ln(SIndex) -0.055 (0.061) Fiscal Stimulus 0.017

(0.013) Constant -0.007∗ -0.005 -0.008∗∗ -0.007∗ -0.006 -0.008∗

(0.004) (0.004) (0.004) (0.004) (0.004) (0.004) Observations 47 47 47 47 43 47 R2 0.084 0.069 0.078 0.121 0.144 0.118 Daily Adjustment N Y Y Y Y Y

Source: Johns Hopkins Coronavirus Resource Center and authors’ calculations. ∆Ln(Opent) and ∆Ln(Closet) are the daily log changes in the opening (i.e., day t − 1 to day t open) and closing values of the Wilshire 5000. ∆ln( Ct−2,−1) is the change in predicted cases. ∆ln(Ct−2,−1) is the change in actual observed cases between days t − 2 and t − 1. ∆ln(Ct−1,0) is the change in actual observed cases between days t − 1 and t. Robust standard errors in parenthesis. Columns 2-6 divide all variables by the number of days since the last observation (i.e., over weekends). Sample period is January 22 to April 10, 2020.

initial days of the outbreak.

#### Table 2: Change in Predicted COVID-19 Cases (∆ Ct−2,−1) vs Market Close Returns

(1) (2) (3) (4) (5) (6) ∆Ln(Close) ∆Ln(Close) ∆Ln(Close) ∆Ln(Close) ∆Ln(Close) ∆Ln(Close)

∆Ln( C−2,−1) -0.067∗∗ -0.080∗∗ -0.089∗∗∗ -0.093∗∗∗ -0.146∗∗∗ -0.089∗∗∗

(0.030) (0.030) (0.031) (0.034) (0.041) (0.032) ∆Ln(C−1,−0) 0.033 0.055 0.065∗ 0.034

(0.031) (0.037) (0.035) (0.032) I(∆SIndex) -0.021

(0.018) ∆Ln(SIndex) -0.091 (0.076) Fiscal Stimulus -0.005 (0.018) Constant -0.009 -0.005 -0.010∗∗ -0.010∗∗ -0.010∗∗ -0.010∗∗

(0.006) (0.005) (0.004) (0.004) (0.004) (0.004) Observations 47 47 47 47 43 47 R2 0.092 0.086 0.103 0.145 0.224 0.104 Daily Adjustment N Y Y Y Y Y

Source: Johns Hopkins Coronavirus Resource Center and authors’ calculations. ∆Ln(Opent) and ∆Ln(Closet) are the daily log changes in the opening (i.e., day t − 1 to day t open) and closing values of the Wilshire 5000. ∆ln( Ct−2,−1) is the change in predicted cases for day t using information from days t − 1 anfd t − 2. ∆ln(Ct−2,−1) is the change in actual observed cases between days t − 2 and t − 1. ∆ln(Ct−1,0) is the change in actual observed cases between days t − 1 and t. Robust standard errors in parenthesis. Columns 2-6 divide all variables by the number of days since the last observation (i.e., over weekends). Sample period is January 22 to April 10, 2020.

Coeﬃcient estimates as well as robust standard errors are reported in Tables 1 and 2, where the former focuses on the daily opening-to-opening return and the latter on the daily closing-to-closing return. Coeﬃcient estimates in the ﬁrst column of each table indicate that a doubling of predicted cases using information from day t − 1 versus day t − 2 leads to average declines of -7.0 and -3.8 percent for closing and opening prices respectively. These eﬀects are statistically signiﬁcant at conventional levels.

In the second and subsequent columns of each table, we adjust the dependent and independent variables by the number of days since the last trading day. This adjustment insures that changes which transpire across weekends and holidays, when markets are closed, are not spuriously large compared to those that take place across successive calendar days. As indicated in the second column of each table, relationships remain statistically signiﬁcant at conventional levels and now have the interpretation of daily growth rates. Here, a doubling of predicted cases per day leads to average declines of 8.6 percent for closing and 4.8 percent for opening prices.

In column 3 of each table, we examine whether the explanatory power of ∆ Ct−2,−1 remains after controlling for a simple, local proxy of outbreak severity, the most recent change in reported cases. We use a slightly diﬀerent variable in each table to account for the timing of the opening and closing returns. For the opening price regressions, we use ∆Ln(C−2,−1) under the assumption that the only information available to predict the opening price on day t is the diﬀerence in reported cases from days t − 2 and t − 1. For the closing price regressions, however, we use ∆Ln(C−1,0) to informally allow for the possibility that, although day t cases are not oﬃcially available until after closing, some information might “leak out” during day t trading.

In both cases, these measures are positive but not statistically signiﬁcant at conventional levels. Moreover, they have little impact on our coeﬃcients of interest. These results suggest that the primary role local increases in reported cases play in determining market value is through their contribution to the overall sequence of reported infections, manifest in the estimated model parameters.

In the ﬁnal three columns of Tables 1 and 2 we examine the robustness of our results to including coarse controls for policy. As the COVID-19 pandemic has unfolded in the United States, state and local governments as well as the federal government have undertaken various measures to control its spread and limit the economic burden the disease itself imposes. Enactment of such policies is by deﬁnition correlated with the severity of the outbreak, and some of them may be designed to stabilize equity markets, confounding our results.

We consider two controls for policy. The ﬁrst is a country-level index developed at Oxford University, the Government Response Stringency Index (SIndex), which tracks travel restrictions, trade patterns, school openings, social distancing and other such measures, by country and day.19 We make use of this index in two ways in columns 4 and 5 of Tables 1 and 2. First, we include an indicator function I{∆SIndex} which takes a value equal to one if the index changes on day t. Second, we use log changes in the index itself, ∆Ln(SIndex). As indicated in the tables, neither covariate is statistically signiﬁcant at conventional levels, and their inclusion has little impact on the coeﬃcient of interest.

Our second control for policy is a coarse measure of ﬁscal stimulus. This dummy variable is set to one for four days (chosen by the authors) upon which major ﬁscal policies were enacted. The “Coronavirus Preparedness and Response Supplemental Appropriations Act, 2020”, which appropriated 8.3 billion dollars for preparations for the COVID-19 outbreak, was signed into law on March 6. Then, from March 25 to March 27, Congress voted for and the President signed into law the 2 trillion dollar “Coronavirus Aid, Relief, and Economic Security Act.” As reported in the table, this dummy variable, too, is statistically insigniﬁcant at conventional levels, and exerts no inﬂuence on the coeﬃcient of interest.

Policy variables’ lack of statistical signiﬁcance is somewhat puzzling. One explanation for this outcome is that these measures are a function of the information contained in the cumulative reported cases, and therefore retain no independent explanatory power. On the other hand, the various government policies included in the SIndex may have oﬀsetting eﬀects. For example, while social distancing measures might be interpreted by the market as a force that reduces the economic severity of the crisis, they may also be taken as a signal that the crisis is worse than publicly available data suggest. At present, we do not have the degrees of freedom to explore the impact of individual elements of the this index, but plan to do so in a future draft when inclusion of additional countries in the analysis allows for panel estimation.

### 3.3 Firm-Level US Returns During COVID-19

In this section we examine the relationship between unanticipated changes in predictions and returns

- at the ﬁrm level using the OLS regression

Rjt = δ + βjC−2−1 ∗ ∆ln Ct−2,−1 + βjMKT ∗ ∆ln(Indext) + t, (5)

where the dependent variable is the daily return of ﬁrm j on day t. The second term on the right-hand side accounts for the possibility that COVID-19 is no diﬀerent than any other aggregate

19This index can be downloaded from https://www.bsg.ox.ac.uk/research/research-projects/ oxford-covid-19-government-response-tracker.

shock, and that a ﬁrm’s return during the pandemic merely reﬂects its more general co-movement with the market (Sharpe, 1964b). When this term is included, βjC−2−1 represents the ﬁrm’s return in excess of its covariance with the market.

The sample period is January 22 to April 10, 2020. Data are taken from Bloomberg and Yahoo ﬁnance.20 In the analysis that follows, we focus on the sample of 4070 ﬁrms incorporated in the United States for which we observe returns during the sample period. These ﬁrms span 505 six-digit NAICS classiﬁcations and 249 4-digit NAICS classiﬁcations.

We run this regression separately for each ﬁrm j, yielding 4070 estimates. Their distribution is

summarized in the kernal density reported in Figure 8. In black, we plot the distribution of βjC−2,−1, the measure of exposure from the regression that does not control for the market index. Intuitively,

given the behavior of the overall market discussed above, we ﬁnd that the overwhelming majority of βjC−2,−1 are below zero, indicating that ﬁrms’ returns generally have a negative relationship with predicted increases in cumulative infections. In red, we plot the distribution of βjC−2,−1|MKT, our notation for the measure of exposure estimated in the presence of the market index. While the bulk of exposures remain negative, the distribution shifts clearly to the right.21

−2−1|MKT j

Figure 8: Distribution of US Firms’ Sensitivity to COVID-19: βjC−2−1 vs βC

[Figure 8]

Source: Johns Hopkins Coronavirus Resource Center, Bloomberg, Yahoo Finance and authors’ calculations. Figure reports the distribution of ﬁrm sensitivities to unanticipated

changes in exponential model predictions, ∆ Ct−2,−1, estimated using equation 5. βjC−2−1 measures total ﬁrm exposure while βC

−2−1|MKT

j removes “typical” co-movement with the market. Sample period is January 22 to April 10, 2020.

The left panel of Figure 9 summarizes ﬁrms’ exposure to COVID-19 by two-digit NAICS sector. While sectors clearly vary in (and are sorted by) their median level of exposure, there is substantial variation across ﬁrms within sectors. The right panel of the ﬁgure plots ﬁrms’ average exposure

20We use Yahoo for stock prices, as we lost immediate access to Bloomberg terminals on March 18. We use the Bloomberg data to ﬁlter our Yahoo sample as follows. We match ﬁrms by ticker from January, 22 to March 18. If returns from the two sources diﬀer by 0.01 on more than one day, or if they diﬀer by more than 1 on any day, we deem that ﬁrm’s returns unreliable and drop them from the analysis. The remaining returns have an in-sample correlation of 99.6 percent during the overlap period.

2196 percent of βjC−2,−1 are negative, while 65 percent of βjC−2,−1|MKT are below zero.

by sector against their average daily returns between January 17, the last trading day prior to the United States’ ﬁrst case, and April 10. We compute a ﬁrm’s mean daily return over this period, Rj, where the bar denotes an average, as the geometric mean of its daily returns, Rjt.

All sectors exhibit a negative average return in response to the COVID-19 shock. Firms producing products more conducive to virus transmission (and therefore more heavily aﬀected by the imposition of social distancing) – Accommodations, Entertainment, and Transportation – exhibit

more negative values for βjC−2−1 and relatively larger declines in daily average returns. The position of Mining, in the extreme lower left position of the ﬁgure, is also unsurprising given the implications

of the sharp contraction in US economic activity on energy use.22 Agriculture, Utilities, Education, Professional Services and FIRE (Finance, Insurance and Real Estate) are towards the upper right of the ﬁgure. These sectors are less exposed to COVID-19 due either to their necessity or their ability to conduct business online, and experience relatively less negative average returns.

Figure 9: US Firms’ Sensitivity to COVID-19 ( βjC), by NAICS Sector

[Figure 9]

Source: Johns Hopkins Coronavirus Resource Center, Bloomberg, Yahoo Finance and authors’ calculations. Figure reports the distribution of ﬁrm sensitivities ( βjC) to unanticipated changes in exponential model projections, ∆ Ct−2,−1, estimated using equation 5. Geometric average of daily returns calculated from January 17 - April 10, 2020.

Table 3 investigates the correlates of exposure to COVID-19 by regressing βjC−2−1 on a series of ﬁrms’ pre-pandemic attributes: total assets (Assetsj), total assets less property, plant and equipment (Assets!jPPE), PPE, employment (Emp), operating proﬁt (OpProfit), cash and debt.23 For ease of interpretation, all independent variables have been converted to z-scores, so that coeﬃcients are in units of standard deviations of the dependent variable.

Coeﬃcient estimates in the ﬁrst column of the table indicate that βjC−2−1 is more negative for ﬁrms with greater assets and PPE, and more positive for ﬁrms with larger employment and operating proﬁt. Each of these coeﬃcients is statistically signiﬁcant at conventional levels. In column 2 (and for the remainder of the table), we net PPE out of total assets and ﬁnd that while its explanatory power dissipates, the signs on PPE, employment and operating proﬁt remain the same. One explanation for the result with respect to PPE is that investors are more apt to bid down the stock prices of capital-intensive ﬁrms that cannot reduce costs during the pandemic. To the extent that ﬁrms ﬁnd it easier to furlough workers than shed their ﬁxed assets, the market values of labor-intensive ﬁrms will fall relatively less.

- 22Returns in mining, which include oil and gas extraction, are also aﬀected by recent disagreements within OPEC, which are potentially endogenous to the pandemic.
- 23Firm attributes are from Compustat for the latest reporting period available, the fourth quarter of 2019. We match ﬁrms to balance sheet information in Compustat via their CUSIP numbers.

#### Table 3: Firm Attributes and COVID-19 Exposure ( βjC−2−1)

##### (1) (2) (3) (4) (5) (6) (7)

βjC−2−1 βjC−2−1 βjC−2−1 βjC−2−1 βjC−2−1 βjC−2−1 βjC−2−1 Ln(Assetsj) -0.0053∗∗

(0.002)

Ln(Assets!jPPE) -0.0015 0.0003 0.0037∗ -0.0004 0.0069∗∗∗ 0.0040 (0.002) (0.002) (0.002) (0.002) (0.002) (0.003)

Ln(PPEj) -0.0101∗∗∗ -0.0066∗∗∗ -0.0060∗∗ -0.0042 -0.0077∗∗∗ -0.0029 0.0059∗ (0.003) (0.002) (0.002) (0.003) (0.002) (0.003) (0.004)

Ln(Empj) 0.0098∗∗∗ 0.0042∗ 0.0040∗ 0.0045∗∗ 0.0053∗∗ 0.0041∗ -0.0000 (0.002) (0.002) (0.002) (0.002) (0.002) (0.002) (0.003)

Incomej 0.0034∗∗∗ 0.0026∗∗∗ 0.0027∗∗∗ 0.0024∗∗∗ 0.0025∗∗∗ 0.0026∗∗∗ 0.0020∗∗∗ (0.001) (0.001) (0.001) (0.001) (0.001) (0.001) (0.001)

Ln(Cashj) -0.0026 -0.0042∗∗ -0.0056∗∗∗ (0.002) (0.002) (0.002)

Ln(Debtj) -0.0069∗∗∗ -0.0073∗∗∗ -0.0063∗∗∗ (0.002) (0.002) (0.002)

Constant -0.0773∗∗∗ -0.0749∗∗∗ -0.0744∗∗∗ -0.0775∗∗∗ -0.0764∗∗∗ -0.0771∗∗∗ -0.0758∗∗∗ (0.001) (0.001) (0.001) (0.001) (0.001) (0.001) (0.001)

Observations 2615 2305 2277 1842 1815 1815 1790 R2 0.026 0.009 0.009 0.017 0.010 0.019 0.175 NAICS-4 FE N N N N N N Y

Source: Johns Hopkins Coronavirus Resource Center, Bloomberg, Yahoo Finance, Compustat and authors’ calculations. Table reports results of cross-sectional OLS regression of ﬁrms’ estimated exposure to COVID-19 from equation 6, βjC−2−1, on their pre-pandemic levels of total assets, total assets less property, plant and equipment (AssetsjPPE), PPE, employment, operating proﬁt, cash and debt. Firm attributes are from Compustat for the latest reporting period available, the fourth quarter of 2019. Robust standard errors reported in parenthesis below coeﬃcients.

In columns 3 and 4, we add two ﬁrm attributes, cash and debt, intended to capture key elements of ﬁrm’s capital structure that may aﬀect survival during the pandemic. As indicated in the table, results are similar with the addition of cash. In column 4, however, PPE becomes marginally signiﬁcant with the addition of debt, indicating that it may be ﬁrms with large capital stocks ﬁnanced by debt that is the key determinant of ﬁrms’ exposure. Such a relationship is consistent with the ﬁndings of Ramelli and Wagner (2020), who also emphasize the constraining role that debt may play during the economic downturn that accompanies a severe pandemic. As information on ﬁrm debt is not available for approximately 400 ﬁrms, we re-estimate in column 5 the speciﬁcation from column 2 for the subset of ﬁrms for which debt is available. Results are similar.

In columns 6 and 7 we include all covariates in the regression without, and then with, fourdigit NAICS ﬁxed eﬀects. Results are similar in both cases, with the exception of coeﬃcient on employment becoming insigniﬁcant and the sign on PPE coeﬃcient ﬂipping from negative to positive. The latter may reﬂect the fact that, after controlling for ﬁrm’s debt and the overall capital intensity of the ﬁrm’s sector (via their ﬁxed eﬀects), larger ﬁrms are estimated to have less negative exposure to COVID-19. We note that the R2 of this regression increases substantially with the inclusion of industry ﬁxed eﬀects, suggesting ﬁrms’ primary industries contain substantial information about their exposure.

Having identiﬁed key channels of ﬁrm exposure to COVID-19, we assess the quantitative importance of this exposure in ﬁrms’ returns over the sample period using a cross-sectional OLS

regression,

Rj = ν1 βjC−2−1 + ν2 βjMKT + ξj. (6) Here, as above, Rj is the geometric average of ﬁrm j’s return from January 22 to April 10, and βjC−2−1 and βjMKT are its exposures to the log changes in predicted cumulative infections and the US market index (Wilshire 5000) estimated in equation 5. To the extent that exposure to COVID19 inﬂuences ﬁrm returns beyond their co-movement with the market, both terms in equation 6 are expected to have explanatory power.24

Table 4: Average Firm Returns and COVID-19 ( βjC−2−1) vs Market Exposure ( βjMKT)

Rj Rj

βjC−2,−1 0.050∗∗∗ 0.023∗∗∗ (0.008) (0.007)

βjMKT -0.007∗∗∗ (0.001)

Constant -0.006∗∗∗ -0.003∗∗∗ (0.001) (0.001)

Observations 4070 4070 R2 0.114 0.198

Source: Johns Hopkins Coronavirus Resource Center, Bloomberg, Yahoo Finance and authors’ calculations. Table reports results of cross-sectional OLS regression of ﬁrms’ average return between January 22 and April 10,

rj, on βjC and βjMKT, the coeﬃcient estimates from equation 5. Robust standard errors reported in parenthesis below coeﬃcients. The standard deviations of rj, βjC and βjMKT are 0.008, 0.051 and 0.043.

Results are reported in Table 4, where the ﬁrst column focuses solely on ﬁrms’ sensitivity to COVID-19, and the second column includes both exposures. The coeﬃcient estimate in column 1, 0.050, implies that a one standard deviation increase in βjC−2,−1 is associated with a 0.33 standard deviation reduction in average daily returns, a sizable inﬂuence.25 The estimate for βjC−2,−1 in column 2 indicate that this inﬂuence remains even after accounting for ﬁrms’ sensitivity to the market (which as noted above is also directly impacted by COVID-19). Here, the magnitude of the coeﬃcient, 0.023, implies that a one standard deviation increase in exposure to COVID-19 is associated with a 0.11 standard deviation decrease in daily returns, or roughly one quarter of the magnitude of the implied impact of a standard deviation change in market exposure.

- 24This regression similar in spirit to those proposed by Fama and MacBeth (1973), though here we use a single

cross section rather than repeated cross sections, i.e., one for each day as the crisis unfolds. We plan to exploit the panel nature of our data in a future draft.

- 25The standard deviations of rj, βjC−2−1 and βjMKT are 0.008, 0.051 and 0.043.

### 3.4 Spatial Implications and Employment

In this section we examine whether changes in predicted cases, as channeled through investors’ reactions to COVID-19, forecast changes in employment at the regional level.26 Job loss is a major concern of both workers and public oﬃcials. An ability to predict employment declines by industry and region is an important input into the develoment of economic and health policy.27

For each US county c, we construct the average change in market value from January 22 to April 10 as the employment-share weighted change in the market value of its constituent 4-digit NAICS industries (n) as

Enc Ec ∗ ∆Ln( MVn). (7)

∆Ln( MVc) ≡

n∈N

where Enc is the 2016 employment in county c in industry n, and ∆Ln(MVn) is the log change in market value of all ﬁrms in industry n attributable to COVID-19 exposure.28 As illustrated in Figure 10, counties vary substantially in their weighted average changes in market value. Notably, much of the “oil belt”, from Texas and Louisiana up through Oklahoma into Wyoming and North Dakota, and parts of Pennsylvania – in brown – exhibit the largest declines. By contrast, much of California and the East Coast – in blue – feature relatively lower declines. Interpreted through the lens of Table 3, these trends indicate that the coasts have disproportionately large employment in indutries containing labor-intensive ﬁrms.

Thus far, oﬃcial estimates of job loss during the pandemic are available only in terms of initial unemployment claims from the US Department of Labor, and only at the state level.29 Appendix Figure A.7 displays the relationship between state changes in market value between January 22 and April 10 (constructed in a manner analogous to counties above), and cumulative new jobless claims per worker.30 This ﬁgure shows that states whose employment is more concentrated in industries with milder losses in market value exhibit greater growth in jobless claims per worker.

As market value declines are larger in more labor-intensive industries (Figure A.5), this trend is consistent with the idea that the labor-intensive sectors favored by the market shed relatively more workers (vis a vis ﬁrms in capital-intensive sectors) in an eﬀort to cut costs as consumption contracts across the board (Baker et al., 2020), and revenues decline. Given the unprecedented collapse of global economic activity, capital-intensive ﬁrms’ property, plant and equipment is eﬀectively sunk. As a consequence, ﬁrms that retain leverage on such assets may fare better by continuing to employ

- 26As ﬁrm employment in COMPUSTAT is updated quarterly, we are at present unable to examine the link between ﬁrm exposure to COVID-19 and ﬁrm employment directly. An additional complication is that ﬁrm employment data in COMPUSTAT reﬂects worldwide, not just US employment. We will include this analysis as the data become available.
- 27We perform two checks on the representativeness of the publicly listed ﬁrms in our sample with respect to employment. First, in appendix Figure A.5, we show that employment among these ﬁrms, while obviously diﬀerent in levels, is highly correlated across industries with US employment in 2016. Second, we ﬁnd, in appendix Figure A.6, that 95 percent of all counties have at least 76 percent of their employment in industries appearing among publicly listed ﬁrms.
- 28Country business pattern employment for 2016 are the latest available from Eckert et al. (2020). We show in appendix Figures A.4 and A.4 that industries with greater capital intensity exhibit greater declines in market value. ∆Ln( MVn) = Ln j∈n MVj,t0(1+

rˆ)52

MVn,t0 is the market capitalization weighted average of return of all ﬁrms j in industry n.

- 29Initial jobless claims are available from the US Department of Labor website at https://oui.doleta.gov/ unemploy/claims_arch.asp. Current Employment Survey (CES) data available from the Bureau of Labor Statistics (BLS) is not yet available for March, but will be included in a future draft.
- 30That is, we sum the initial jobless claims from March 18 (before most of the COVID-19 labor market disruption began) to April 11, and divide by the initial number of employees in the state according to the 2016 CBP.

#### Figure 10: Employment Weighted Change in Market Value, by County

[Figure 10]

Source: Johns Hopkins Coronavirus Resource Center, Bloomberg, Yahoo Finance, Compustat, Eckert et al. (2020) and authors’ calculations. We omit counties (in grey) if we match less than 70% of their employment at the NAICS-4 level. This is under 5% of all counties.

workers, producing at a loss given the decline in demand, so long as they are able to cover short-run variable costs.

Figure 11: Jobless Claims per Worker vs. State-Average Change in Market Value

[Figure 11]

Source: Johns Hopkins Coronavirus Resource Center, Bloomberg, Yahoo Finance, Compustat, Eckert et al.

(2020), US Department of Labor and authors’ calculations.

We investigate this mechanism more formally using an OLS diﬀerence-in-diﬀerences (DID) regression,

Joblesssw Es,2016

= η0 + η1Post ∗ ∆Ln( MVs) + η2Post ∗ Xs + η3Γsw + ρw + ρs + sw, (8)

where the dependent variable is the ratio of jobless claims in state s in week w expressed in percentage terms, Xs are state labor market characteristics (deﬁned below), Γsw are week-varying state controls, and the last two terms are state and week ﬁxed eﬀects. We deﬁne the treatment period (Post) as the full weeks following the oﬃcial March 11 announcement by the WHO declaring

COVID-19 a global pandemic.31 We note that we interpret the DID term of interest in this regression as the translation of unanticipated news about the pandemic from ﬁrms to states.32 During the pre-period, average jobless claims per worker across states is 0.19 percent; after March 11, they jump to 4 percent. For ease of interpretation covariates have been standardized so the coeﬃcients may be interpreted as the eﬀect of increasing the covariate by one standard deviation. Standard errors are clustered at the state level.

Table 5: Jobless Claims and Market Valuation

(1) (2) (3) (4) (5) (6)

Joblesss,w Emps,2016

Joblesss,w Emps,2016

Joblesss,w Emps,2016

Joblesss,w Emps,2016

Joblesss,w Emps,2016

Joblesss,w Emps,2016

∆Ln( MV s) 0.3305∗ 0.4653∗∗ 0.3902∗∗ 0.3911∗∗ 0.4059∗∗ 0.3101∗ × Post (0.175) (0.180) (0.171) (0.174) (0.175) (0.176)

Teleworkables -0.3744∗ -0.4021∗∗ -0.4013∗∗ -0.4613∗ -0.4495∗ × Post (0.189) (0.180) (0.181) (0.231) (0.234)

I(Stay Orders,w) 0.9029∗∗∗ 0.9042∗∗∗ 0.8855∗∗∗ 0.9415∗∗∗

(0.325) (0.325) (0.319) (0.320) Ln(Employment2016) -0.0040 0.0104 0.0220

× Post (0.185) (0.191) (0.197) Workforce Matchs -0.1004 -0.0711 × Post (0.181) (0.178)

Constant 0.1910∗∗∗ 0.1910∗∗∗ 0.1910∗∗∗ 0.1910∗∗∗ 0.1910∗∗∗ 0.1910∗∗∗ (0.049) (0.047) (0.044) (0.044) (0.045) (0.045)

Reduced Exposure N N N N N Y State FE Y Y Y Y Y Y Week FE Y Y Y Y Y Y Observations 765 765 765 765 765 765

R2 0.834 0.840 0.847 0.847 0.847 0.844

Source: Johns Hopkins Coronavirus Resource Center, Bloomberg, Yahoo Finance, Henry J. Kaiser Family Foundation, (Eckert et al., 2020) and authors’ calculations. ∆Ln( MVs) is the employment weighted average change in industry market n value at the state level. Post is equal to 1 for full weeks after March 11. Standard errors are clustered at the state level. Independent variables are in terms of standard deviations.

Results are reported in Table 5. In column 1, we include only state and week ﬁxed eﬀects and the DID term of interest, ∆Ln( MVs) ∗ Post. The coeﬃcient estimate, indicates that a 1 standard deviation increase in market value is associated with 0.33 percentage point increase in jobless claims per worker per week in the post period, relative to the pre-period. This eﬀect is sizable, representing nearly 10 percent of the average post-period increase.

In column 2 we include the share of state employment amenable to teleworking from home developed by Dingel and Neiman (2020).33 The estimated coeﬃcient on this variable is intuitive: the more intensive a state is in work that can be done at home, the lower the initial jobless claims. Inclusion of this covariate raises the magnitude of the DID term of interest to 0.47.

The third column in Table 5 introduces a covariate capturing the staggered stay-at-home orders

- 31As illustrated in appendix Figure A.7, there is a substantial break in jobless growth following the WHO announcement, indicated by the red vertical line in the ﬁgure.
- 32That is, we do not view changes in market value per se as exogenous predictions of employment. Here, the DID term of interest captures exogenous information about the trajectory of the pandemic, mediated by investors.
- 33As with the dependent variable in this regression, we compute this measure as the employment-weighted average teleworking share across 4-digit NAICS industries.

imposed by states during the post period.34 Predictably, the coeﬃcient for this variable is large in magnitude and statistically signiﬁcant at conventional levels. Its sign indicates that the roll-out of social mobility restrictions coincides with increases in jobless claims per worker conditional on the share of work that can be done from home. In this speciﬁcation, the DID coeﬃcient of interest remains positive and statistically signiﬁcant, with a magnitude of 0.39 percentage points.

Columns 4 and 5 of Table 5 investigate whether the DID term of interest is sensitive to including two additional controls, for total employment in the state, interacted with Post, and the share of state workforce for which we observe a 4-digit NAICS industry. Neither covariate is statistically signiﬁcant at conventional levels, and the magnitude of the DID term of interest remains within the bounds established by previous columns.

Our baseline measure of state’s exposure to the economic eﬀects of COVID-19 is calculated through nearly all of the spring – spanning our pre- and post-period. As a consequence, one may have concerns that equity market reactions are themselves a function of states’ exposure to the rise in jobless claims. To address this, in the last column of Table 5 we restrict estimation of our measure of ∆Ln( MVss) to the that ends March 18, the date of the ﬁrst substantial increase in jobless claims. While the DID term of interest is estimated less precisely, this estimate is consistent with the estimates in the earlier columns of the table.

Overall, the ﬁndings in Table 5 provide a consistent message: investors bid down the stock prices of ﬁrms less the more they are able to shed costs, and states intensive in these ﬁrms see greater initial jobless claims. During a pandemic, equity market participants appear to love precisely what labor market participants loathe – the ease with which workers can be temporarily furloughed or permanently dismissed.

34Data collected from “State Data and Policy Actions to Address Coronavirus,” provided by the Henry J. Kaiser Family Foundation.

# 4 Application to SARS

In this section we demonstrate historical precedent for the link between US stock market returns and COVID-19 discussed above by reporting a similar link during the Severe Acute Respiratory Syndrome (SARS) outbreak in Honk Kong nearly 20 years earlier.

The ﬁrst SARS case was identiﬁed in Foshan, China in November 2002, but was not recognized as such until much later. According to WHO (2006), on February 10, 2003 a member of the WHO in China received an email asking:

“Am wondering if you would have information on the strange contagious disease (similar to pneumonia with invalidating eﬀect on lung) which has already left more than 100 people dead in ... Guangdong Province, in the space of 1 week. The outbreak is not allowed to be made known to the public via the media, but people are already aware of it (through hospital workers) and there is a ‘panic’ attitude.”

The WHO immediately began an investigation into SARS, and started releasing regular reports of suspected and conﬁrmed cases beginning March 17, 2003.35 The World Health Organization (WHO) declared SARS contained in July 2003, though cases continued to be reported until May 2004. Figure 12 plots the cumulative number of conﬁrmed SARS infections worldwide (left scale) and in Hong Kong (right scale). The two vertical lines in the ﬁgure note the days on which the WHO oﬃcially received the aforementioned email, and the ﬁrst day on which the WHO began reporting the number of infections on each weekday.

Figure 12: SARS Infections in Hong Kong and Worldwide During 2003

[Figure 12]

Source: World Health Organization and authors’ calculations. Figure displays the cumulative reported SARS infections in Hong Kong and the rest of the world from January 1, 2003 to July 11, 2003. The two vertical lines in the ﬁgure note the days on which the WHO oﬃcially received the aforementioned email, and the ﬁrst day on which the WHO began reporting the number of infections on each weekday.

Hong Kong and China accounted for the vast majority of cases worldwide.36 We focus our analysis on Hong Kong for two reasons related to data reliability. First, while China acknowledged having over 300 cases of “atypical pneumonia” in February, the Ministry of Health did not provide day-by-day counts until March 26. In fact, on March 17, the day before WHO began releasing daily situation reports, Chinese authorities informed the WHO that “[t]he outbreak in Guangdong

- 35Counts were released every weekday. These data can be downloaded from https://www.who.int/csr/sars/ country/en/. A timeline of WHO activities related to SARS events can be found at https://www.who.int/csr/ don/2003_07_04/en/.
- 36Reported cases for China are plotted in appendix Figure A.2.

is said to have tapered oﬀ.” The next day, cases were reported in 8 locations other than China – including Hong Kong. When China did begin reporting daily counts, on March 26, the ﬁrst count was 800 cases. This large initial level of infections accounts for the sharp jump in world counts displayed for that day in Figure 12. Lack of real-time infection updates in mainland China prior to this jump undermines reliable estimation of model parameters, thereby impeding accurate assessment of unanticipated changes in infections. Second, it is unclear how China’s restrictions on foreign ownership of companies’ “A shares” during this period aﬀects the extent to which such unanticipated changes will be reﬂected in Mainland ﬁrms’ equity value.

We estimate equations 1 and 2 by day for each country as discussed in Section 2. The daily parameter estimates for the logistic estimation, kt, ct and rt are displayed graphically in the left panel of Figure 13. The right panel displays analogous estimates for the exponential function. Gaps in either panel’s time series represent lack of convergence. As indicated in the ﬁgure, logistic parameters fail to converge for several days early in the outbreak, and then once again when the estimates have started to settle down in the beginning of May. The exponential model, by contrast, converges on every day in the sample period.

Figure 13: Parameter Estimates for SARS

[Figure 13]

Source: World Health Organization and authors’ calculations. The left panel plots the sequence of logistic parameters, kt, ct and rt, estimated using the information up to each day t on the cumulative reported cases for Hong Kong displayed in Figure 12. Right panel Figure plots the analogous sequence of exponential parameters, ait and rit, using the same data. Missing estimates indicate lack of convergence (see text). Circles represent estimates. Solid lines connect estimates.

In the left panel of Figure 14, we compare the predictions of the two models. In each case, parameter estimates from day t − 1 are used to predict the cumulative number of cases for day t. Shading represents 95 percent conﬁdence intervals. As indicated in the panel, predicted infections under the two models (left axis) are similar through the ﬁrst week in April, but diverge thereafter. Interestingly, this divergence coincides with a stabilization of the estimated inﬂection point of the logistic curve (right axis), which, as illustrated by the dashed grey line in the panel, hovers between April 5 and 7 from April 5 onward.37

We use the predictions of the logistic model for the remainder of the analysis. The right panel of Figure 14 compares the logistic model predictions for day t using information as of day t − 1, Ctt−1, versus day t−2, Ctt−2, as well as the log diﬀerence between these predictions, ∆ln( Ct−2,−1).38 We ﬁnd that ∆ln( Ct−2,−1) exhibits wide swings in value during the early stages of the outbreak, before settling down in late April. As illustrated in Figure 15, these swings have a noticeably negative correlation with aggregate stock market performance in Hong Kong, as identiﬁed via daily

37The inﬂection point is given by ln( ct)/ rt. 38We use the last available parameter estimates for days on which logistic parameters do not converge.

#### Figure 14: Daily Predictions ( Ctt−1) for SARS

[Figure 14]

Source:World Health Organization and authors’ calculations. Left panel displays predicted cumulative cases for each day t, Ctt−1, information as of day t − 1, based on parameter estimates reported in Figure 13. Shading spans 95 percent conﬁdence intervals. Dashed line (right scale) traces out the estimated of the logistic curve’s inﬂection point (ln( ct)/ rt). Right panel reports day t predicted cumulative cases under the logistic model using information as of day t − 1, Ctt−1, and day t − 2, Ctt−2, as well as the log diﬀerence between these predictions, ∆ln( Ct−2,−1). Missing estimates in left panel indicate lack of convergence (see text).

log changes in the Hang Seng Index.39

We explore this relationship formally in an OLS estimation of equation 4. Coeﬃcient estimates and robust standard errors are reported in Table 6. In the ﬁrst column, we ﬁnd a negative and statistically signiﬁcant relationship using the raw data displayed in Figure 15. In column 2, we account for weekends and holidays by dividing both the left- and right-hand side variables by the number of days over which the returns are calculated, so that the regression coeﬃcient represents a daily change in market value for a given log change in predicted cases. Here, too, the coeﬃcient estimate is negative and statistically signiﬁcant at conventional levels, and higher in absolute magnitude.

In column 3, we examine whether the explanatory power of ∆ln( Ct−1,−2) remains after controlling for a simple, local proxy of outbreak severity, the diﬀerence in cumulative reported infections between days t − 1 and t − 2, ∆ln(Ct−1,−0). As indicated in the table, the coeﬃcient of interest remains negative and statistically signiﬁcant at conventional levels, though of lower magnitude in absolute terms. The coeﬃcient for ∆ln(Ct−2,−1) is also negative and statistically signiﬁcant.

Finally, in column 4, we repeat the speciﬁcation for column 3 but include month ﬁxed eﬀects to account for potential secular movements in the market unrelated to SARS. Esimate are essentially unchanged.

Overall, the estimates in Table 6 suggest investors may have used simple epidemiological models to update their beliefs about the economic severity of the outbreak in Hong Kong, in real time. Across speciﬁcations, coeﬃcient estimates indicate an average decline of 8 to 11 percent in response to a doubling of predicted cumulative infections.

39Data for the Hong Seng index are downloaded from Yahoo Finance.

#### Figure 15: Changes in Predicted SARS Cases (∆ Ct−2,−1) vs Hang Seng Index Returns

[Figure 15]

Source: World Health Organization, Yahoo Finance and authors’ calculations. Figure displays the daily log change in the Hang Seng Index against the daily log change in predicted cases for day t based on information as of day t − 1 versus day t − 2,

∆ln( Ct−2,−1).

#### Table 6: Changes in Predicted SARS Cases vs Hang Seng Index Returns

(1) (2) (3) (4) ∆Ln(Close) ∆Ln(Close) ∆Ln(Close) ∆Ln(Close)

∆Ln( C−2,−1) -0.0752∗∗∗ -0.1095∗∗∗ -0.0891∗∗ -0.0923∗

(0.0241) (0.0396) (0.0427) (0.0537) ∆Ln(C−2,−1) -0.0445∗∗ -0.0483

(0.0200) (0.0294) Constant 0.0018 0.0010 0.0019∗ 0.0025

(0.0013) (0.0011) (0.0011) (0.0051)

Daily Adjustment N Y Y Y Month FE N N N Y Observations 70 70 70 70 R2 0.108 0.060 0.103 0.111

Source: World Health Organization,Yahoo Finance and authors’ calculations. ∆Ln(Closet) is the daily log change (i.e., day t − 1 to day t) closing values Hang Seng Index. ∆ln( Ct−2,−1) is the change in predicted cases for day t using information from days t−1 and t−2. ∆ln(Ct−2,−1) is the change in reported cases between days t−1 and t. Robust standard errors in parenthesis. Columns 2-4 divide all variables by the number of days since the last observation (i.e. over weekends). Column 4 includes month ﬁxed eﬀects.

# 5 Conclusion

This paper shows that day-to-day changes in the predictions of standard models of infectious disease forecast changes in aggregate stock returns in Hong Kong during the SARS outbreak and the United States during the COVID-19 pandemic. In future updates to this paper, we plan to extend the analysis to other countries and pandemics, and to investigate the link between individual ﬁrms’ returns and their exposure to public health crises via domestic and international input and output linkages as well as the demographics and occupations of their labor forces.

# References

Albuquerque, R. A., S. Yang, and C. Zhang (2020). Love in the time of covid-19: The resiliency of environmental and social stocks. Working Paper.

Atkeson, A. (2020, March). What will be the economic impact of covid-19 in the us? rough estimates of disease scenarios. Working Paper 26867, National Bureau of Economic Research.

Bai, H., K. Hou, H. Kung, E. X.N., and L. Zhang (2019). The CAPM Strikes Back? An Equilibrium Model with Disasters. Journal of Financial Economics 131(2), 269–298.

Baker, S., N. Bloom, S. Davis, and S. J. Terry (2020). Covid-induced economic uncertainty. NBER w26983.

Baker, S. R., N. Bloom, S. J. Davis, K. J. Kost, M. C. Sammon, and T. Viratyosin (2020, April). The unprecedented stock market impact of covid-19. Working Paper 26945, National Bureau of Economic Research.

Baker, S. R., R. Farrokhnia, S. Meyer, M. Pagel, and C. Yannelis (2020). How does household spending respond to an epidemic? consumption during the 2020 covid-19 pandemic. NBER Working Paper 26949.

Ball, R. and P. Brown (1968). An empirical evaluation of accounting income numbers. Journal of accounting research, 159–178.

Barro, R. J., J. F. Ursua, and J. Weng (2020, March). The coronavirus and the great inﬂuenza pandemic: Lessons from the “spanish ﬂu” for the coronavirus’s potential eﬀects on mortality and economic activity. Working Paper 26866, National Bureau of Economic Research.

Bartik, A. W., M. Bertrand, Z. Cullen, E. L. Glaeser, M. Luca, and C. T. Stanton (2020). How are small businesses adjusting to covid-19? early evidence from a survey. NBER w26989.

Bartik, T. J. (1991). Who Beneﬁts from State and Local Economic Development Policies? Upjohn Institute for employment Research.

Berger, D., K. Herkenhoﬀ, and S. Mongey (2020). A seir infectious disease model with testing and conditional quarantine. Working Paper.

Cajner, T., L. D. Crane, R. A. Decker, A. Hamins-Puertolas, and C. Kurz (2020). Tracking labor market developments during thecovid-19 pandemic: A preliminary assessment. Finance and Economics Discussion Series 2020-030.

Campbell, J. Y. and R. J. Shiller (1988). The dividend-price ratio and expectations of future dividends and discount factors. The Review of Financial Studies 1(3), 195–228.

Coibion, O., Y. Gorodnichenko, and M. Weber (2020). Labor markets during the covid-19 crisis: A preliminary view. NBER w27017.

Ding, W., R. Levine, C. Lin, and W. Xie (2020). Corporate immunity to the covid-19 pandemic. Working Paper.

Dingel, J. I. and B. Neiman (2020). How many jobs can be done at home? University of Chicao Mimeo.

Eckert, F., T. C. Fort, P. K. Schott, and N. J. Yang (2020). Imputing missing values in the us census bureau’s county business patterns. Technical report, National Bureau of Economic Research.

Fahlenbrach, R., K. Rageth, and R. M. Stultz (2020). How Valueable is Financial Flexibility When Revenue Stops? Evidence from the COVID-19 Crisis.

Fama, E. and J. D. MacBeth (1973). Risk, return, and equilibrium: Emprirical tests. Journal of Political Economy.

Fama, E. F., L. Fisher, M. C. Jensen, and R. Roll (1969). The Adjustment of Stock Prices to New Information. International Economic Review 10.

Fama, E. F. and K. R. French (1988). Dividend yields and expected stock returns. Journal of ﬁnancial economics 22(1), 3–25.

Gormsen, N. J. and R. S. Koijen (2020). Coronavirus: Impact on stock prices and growth expecta-

tions. University of Chicago, Becker Friedman Institute for Economics Working Paper (2020-22). Greenland, A., M. Ion, J. Lopresti, and P. K. Schott (2019). Using equity market reactions to infer

exposure to trade liberalization. Technical report, Working Paper. Guerrieri, V., G. Lorenzi, L. Straub, and I. Werning (2020). Macroeconomic Implications of COVID19: Can Negative Supply Shocks Cause Demand Shortages. NBER w26918. Humphries, J. E., C. Neilson, and G. Ulyssea (2020). The evolving impacts of covid-19 on small businesses since the cares act. working paper.

Kermack, W. O. and A. G. McKendrick (1927). A contribution to the mathematical theory of epidemics. Proceedings of the royal society of london. Series A, Containing papers of a mathematical and physical character 115(772), 700–721.

Kermack, W. O. and A. G. McKendrick (1937). Contributions to the mathematical theory of epidemics iv. analysis of experimental epidemics of the virus disease mouse ectromelia. Journal of Hygiene 37(2), 172–187.

Keynes, J. M. (1937). The general theory of employment. The quarterly journal of economics 51(2),

209–223. Knight, F. H. (1921). Risk, uncertainty and proﬁt. Library of Economics and Liberty. Li, R., S. Pei, B. Chen, Y. Song, T. Zhang, W. Yang, and J. Shaman (2020). Substantial undocumented infection facilitates the rapid dissemination of novel coronavirus (sars-cov2). Science. Piguillem, F. and L. Shi (2020). The optimal covid-19 quarantine and testing policies. Working

Paper. Ramelli, S. and A. F. Wagner (2020). Feverish stock price reactions to covid-19. Swiss Finance Institute Research Paper (20-12). Richards, F. J. (1959, 06). A Flexible Growth Function for Empirical Use. Journal of Experimental Botany 10(2), 290–301. Ross, R. (1911). The Prevention of Malaria. John Murray.

Ru, H., E. Yang, and K. Zou (2020). What do we learn from sars-cov-1 to sars-cov-2: Evidence from global stock markets. Working Paper.

- Sharpe, W. F. (1964a). Capital Asset Prices: A Theory of Market Equilibrium Under Conditions of Risk.
- Sharpe, W. F. (1964b). Capital Asset Prices: A Theory of Market Equilibrium Under Conditions of Risk.

WHO (2006). SARS: how a global epidemic was stopped. Manila: WHO Regional Oﬃce for the Western Paciﬁc.

#### Figure A.1: Actual COVID-19 Cases, By Country

[Figure 16]

Source: Johns Hopkins Coronavirus Resource Center and authors’ calculations. Figure displays the COVID-19 up to March 28.

#### Figure A.2: SARS Infections in China and Worldwide During 2003

[Figure 17]

Source: World Health Organization and authors’ calculations. Figure displays the cumulative reported SARS infections in China and the rest of the world from January 1, 2003 to July 11, 2003.

#### Figure A.3: Loss of Market Value and Initial Capital Intensity, by Industry

[Figure 18]

Source: Johns Hopkins Coronavirus Resource Center, Bloomberg, Yahoo Finance, Compustat and authors’ calculations. Veritcal axis is the cumulative change in market value from January 22 to April 10 due to COVID-19 across ﬁrms by fourdigit NAICS industry, based on the coeﬃcient in column 1 of Table 4. Horizontal axis is ﬁrms’ ﬁxed assets divided by their employment, also by four-digit NAICS sector.

#### Figure A.4: Loss of Market Value and Initial Capital Intensity (Unabridged)

[Figure 19]

Source: Johns Hopkins Coronavirus Resource Center, Bloomberg, Yahoo Finance and authors’ calculations. Figure reports the distribution of industry changes in market value implied by column 1 of Table 4 to industry capital to labor ratio.

#### Figure A.5: Employment in Compustat vs County Business Patterns

[Figure 20]

Source: Compustat, author’s calculations, and County Business Patterns database.

#### Figure A.6: County Employment Coverage

[Figure 21]

Source: Johns Hopkins Coronavirus Resource Center, Bloomberg, Yahoo Finance, County Business Patterns, Compustat, and authors’ calculations. Figure reports the percent of county employment listed in CBP for which we have a matching naics-4 digit measure of ∆Ln(MVn)

#### Figure A.7: State Jobless Claims per Worker

[Figure 22]

Source: US Department of Labor. Eckert et al. (2020) and authors’ calculations. Figure reports weekly initial jobless claims reported by the Department of Labor during 2020.

#### Figure A.8: Changes in Predicted SARS Cases vs HSI Index

[Figure 23]

Source: Johns Hopkins Coronavirus Resource Center, Yahoo Finance and authors’ calculations. Figure displays the daily log change in the Hang Seng Index against the log change in projected cases for day t based on day t − 1 and day t − 2 information.

