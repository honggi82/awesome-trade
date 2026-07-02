arXiv:cond-mat/0203596v1[cond-mat.stat-mech]28Mar2002

Waiting-times and returns in high-frequency ﬁnancial data: an empirical study

Marco Raberto a, Enrico Scalasb, Francesco Mainardi c,1

aDipartimento di Ingegneria Bioﬁsica ed Elettronica, Universit`a di Genova, via dell’Opera Pia 11a, I–16145 Genova, Italy bDipartimento di Scienze e Tecnologie Avanzate, Universit`a del Piemonte Orientale, via Cavour 84, I–15100 Alessandria, Italy cDipartimento di Fisica, Universit`a di Bologna and INFN Sezione di Bologna, via Irnerio 46, I–40126 Bologna, Italy

[Figure 1]

Abstract

In ﬁnancial markets, not only prices and returns can be considered as random variables, but also the waiting time between two transactions varies randomly. In the following, we analyse the statistical properties of General Electric stock prices, traded at NYSE, in October 1999. These properties are critically revised in the framework of theoretical predictions based on a continuous-time random walk model.

Key words: PACS: 02.50.-r, 02.50.Ey, 02.50.Wp, 89.90.+n Stochastic processes; Continuous-time random walk; Statistical ﬁnance; Econophysics; Autocorrelation function

[Figure 2]

1 Introduction

In ﬁnancial markets, waiting times between two consecutive transactions vary in a stochastic fashion. In 1973, [1] Peter Clark wrote: “Instead of indexing [time] by the integers 0,1,2,. . ., the [price] process could be indexed by a set of numbers t1, t2, t3, . . ., where these numbers are themselves a realization of a stochastic process (with positive increments, so that t1 < t2 < t3 < . . .).”

From this point of view the continuous time random walk (CTRW) model of Montroll and Weiss [2] (see also Refs. [3–5]) can provide a phenomenological description of tick-by-tick dynamics in ﬁnancial markets [6–8].

[Figure 3]

- 1 Corresponding author. E-mail: mainardi@bo.infn.it URL: www.fracalmo.org

Preprint submitted to Elsevier Preprint 21 July 2021

Actually in CTRWs, two random variables are used: jumps ξn = x(tn+1)−x(tn) and waiting times τn = tn+1 − tn. In the ﬁnancial interpretation of CTRWs, x represents a log-price and ξ a log-return [6–8] (see also [9]). The physicist can think of x as the position of a random walker performing discrete jumps in one dimension at randomly distributed instants. Based on [7] the evolution equation for p(x, t), the probability of occurrence of the log-price x at time t, or of ﬁnding the random walker at position x at time instant t, can be written, assuming the initial condition p(x, 0) = δ(x) (i.e. the walker is initially at the origin x = 0),

p(x, t) = δ(x) Ψ(t) +

t

0

+∞

ϕ(x − x′, t − t′) p(x′, t′) dx′ dt′ , (1.1)

−∞

where Ψ(t) is the survival probability and ϕ(ξ, τ), is the joint probability density of jumps ξn = x(tn+1)−x(tn) and of waiting times τn = tn+1−tn. Relevant quantities are the two (marginal) probability density functions (pdf’s) deﬁned

- as λ(ξ) := 0 ∞ ϕ(ξ, τ) dτ , ψ(τ) := −∞ +∞ ϕ(ξ, τ) dξ , and called jump pdf and waiting-time pdf, respectively. If one assumes that the jump pdf λ(ξ) is independent of the waiting-time pdf ψ(τ) , we have the so-called ”decoupling” which leads to the factorisation ϕ(ξ, τ) = λ(ξ) ψ(τ) .

The Eq. (1.1) is the most general master equation of the CTRW, usually derived in the Fourier-Laplace domain. The simpliﬁed form under the hypothesis of ”decoupling” is reported in [7].

The probability that a given inter-step interval is greater or equal to τ is Ψ(τ) , which is deﬁned in terms of ψ(τ) by

Ψ(τ) =

τ

∞

ψ(t′) dt′ = 1 −

0

τ

d dτ

ψ(t′) dt′ , ψ(τ) = −

[Figure 4]

Ψ(τ) . (1.2)

We note that 0 τ ψ(t′) dt′ represents the probability that at least one step is taken at some instant in the interval [0, τ), hence Ψ(τ) is the probability that the diﬀusing quantity x does not change value during the time interval of duration τ after a jump. We also note, recalling that t0 = 0 , that Ψ(t) is the survival probability until time instant t at the initial position x0 = 0 .

A relevant choice for the survival probability is given by the Mittag-Leﬄer function of order β (0 < β < 1), which leads to a time-fractional master equation as shown in [7] (see also [10,11]). For reader’s convenience hereafter we recall the main properties of this transcendental function useful for our purposes. From its deﬁnition valid for any β > 0 :

∞

Ψ(τ) = Eβ −(τ/τ0)β :=

n=0

(τ/τ0)βn Γ(β n + 1)

(−1)n

, β > 0 , (1.3)

[Figure 5]

one recognises that the Mittag-Leﬄer function generalises the simple exponential function (recovered for β = 1) and, if 0 < β < 1 , it interpolates on the positive real axis a stretched exponential and a power law according to

exp −(τ/τ0)β/Γ(1 + β) , τ/τ0 → 0+, (τ/τ0)−β/Γ(1 − β), τ/τ0 → ∞,

Eβ −(τ/τ0)β ∼

0 < β < 1. (1.4)

For more information on the Mittag-Leﬄer function see e.g. [12–14].

The purpose of this paper is to investigate some statistical properties of the random variables ξ and τ in ﬁnancial markets. This study is limited to a speciﬁc equity of a given market in a deﬁnite period. Therefore caution is necessary and our results cannot be arbitrarily generalized. In particular, the reader will learn about General Electric stock prices, traded at NYSE, in October 1999. This preliminary presentation is part of a broader project aimed

- at studying the behaviour of all Dow-Jones-Industrial-Average stocks during that month.

- 2 Empirical analysis

- In Fig. 1, a scatter plot is presented for waiting times τn as a function of the corresponding log-return ξn. By means of a contingency table analysis [15], we have studied the independence of the two stochastic variables. A direct inspection of Fig. 1 shows that for large values of log-returns waiting times tend to be shorter. This indicates a possible correlation. Actually, a hypothesis test has been performed on the empirical joint pdf ϕ(ξ, τ) . According to the contingency table presented in Tab. 1, the two random variables cannot be considered independent. The null hypothesis of independence can be rejected with a signiﬁcance level of 1%.
- In Fig. 2, an estimate of the autocorrelation function for the absolute value of log-returns is plotted. We have used the following estimator [16]

N−m−1

1 N − m

[Figure 6]

[Figure 7]

C(m) =

(|ξn+m| − |ξ|)(|ξn| − |ξ|), (2.1)

[Figure 8]

n=0

[Figure 9]

where N is the total number of points (N = 55559) and |ξ| = N1 n N=0−1 |ξn| . The inset shows the time series of the absolute values as a function of the tick

[Figure 10]

n.

Due to scale persistence, the autocorrelation function follows a power-law decay with a slope of −0.76. The autocorrelation is over the noise level (conventionally 3/√N) for a lag between 20 and 30 ticks, corresponding to an

[Figure 11]

[Figure 12]

[Figure 13]

[Figure 14]

[Figure 15]

[Figure 16]

[Figure 17]

τn

[Figure 18]

[Figure 19]

[Figure 20]

[Figure 21]

[Figure 22]

[Figure 23]

[Figure 24]

0 ÷ 10 10 ÷ 20 > 20 < −0.002 25 (38.9) 21 (10.1) 9 (6.0) −0.002 ÷ −0.001 516 (613.6) 230 (159.5) 122 (94.9)

[Figure 25]

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

ξn −0.001 ÷ 0 6641 (7114.3) 2085 (1849.1) 1338 (1100.6) 0 ÷ 0.001 31661 (31008.0) 7683 (8059.2) 4520 (4797.0) 0.001 ÷ 0.002 398 (464.4) 179 (120.7) 80 (71.9) > 0.002 34 (36.1) 10 (9.4) 7 (5.6)

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

Table 1 Contingency table between log-returns ξn and waiting times τn. Every cell contains the frequency observed within the values considered and (in brackets) the theoretical frequency which can be computed under the null hypothesis of independence between ξn and τn.

average time of 250s. Therefore, within that time scale, it is not safe to assume that the log-returns themselves, ξn, are independent variables. These are well-known stylised fact for tick-by-tick ﬁnancial time series, see e.g. [17–19].

- In Fig. 3, the autocorrelation function is shown for waiting-times τn. As above, the inset shows the time series itself. Waiting times between trades are inherently positive random variables. For the GE stock in October 1999, there is a marked seasonality of waiting times with a 1-day period (nearly 3, 000 trades). Inspection of the series shows that the trading activity is slower in the middle of the day. The seasonality is outlined by the periodic behaviour of the autocorrelation estimate, with periodicity above the conventional noise band.

In recent times, several eﬀorts have been devoted to ﬁnd a suitable measure of time, in order to discard similar seasonalities, see e.g. [20,21].

However, as shown in Fig. 4, the survival probability Ψ(τ) can be ﬁtted by a stretched exponential function: exp −(τ/τ0)β/Γ(1 + β) , with τ0 = 6.6s and β = 0.7. The reduced chi-square of the ﬁt is 0.71.

In a previous work on bond futures [7], according to theoretical considerations on the properties of continuous-time random walks, we suggested the Mittag-Leﬄer function with a power-law decay as a suitable ﬁt for the empirical survival probability. The above result does not contradict our previous ﬁndings. In fact, whereas for bonds futures we found waiting times greater than 10, 000s , here we have only waiting times smaller than 200s, and the Mittag-Leﬄer function is well approximated by the stretched exponential as τ is small enough, see Eq. (1.4).

- 3 Summary

A preliminary study of General Electric high-frequency stock prices has been performed. Some statistical properties of the log-return and waiting-time random variables have been presented. This study was inspired by previous theoretical and empirical work, based on the phenomenological CTRW model of ﬁnancial markets.

The main results are as follows: the two random variables cannot be considered independent from each other; the autocorrelation of log-returns absolute values exhibits a power-law decay and reaches the noise level after about 250 s; the autocorrelation of waiting times shows a 1-day periodicity, corresponding to the daily stock market activity.

References

- [1] P.K. Clark, A subordinated stochastic process model with ﬁnite variance for speculative prices, Econometrica 41 (1973) 135-156.
- [2] E.W. Montroll and G.H. Weiss, Random walks on lattices, II, J. Math. Phys. 6

(1965) 167–181.

- [3] E.W. Montroll and B.J. West, On an enriched collection of stochastic processes, in: E.W. Montroll and J. Leibowitz (Eds.), Fluctuation Phenomena, NorthHolland, Amsterdam, 1979, pp. 61-175.
- [4] E.W. Montroll and M.F. Shlesinger, On the wonderful world of random walks, in: J. Leibowitz and E.W. Montroll (Eds.), Nonequilibrium Phenomena II: from Stochastics to Hydrodynamics, North-Holland, Amsterdam, 1984, pp. 1-121.
- [5] G.H. Weiss, Aspects and Applications of Random Walks, North-Holland, Amsterdam, 1994.
- [6] E. Scalas, R. Gorenﬂo and F. Mainardi, Fractional calculus and continuous-time ﬁnance, Physica A 284 (2000) 376-384.
- [7] F. Mainardi, M. Raberto, R. Gorenﬂo, E. Scalas, Fractional calculus and continuous-time ﬁnance II: the waiting-time distribution, Physica A 287 (2000) 468-481.
- [8] R. Gorenﬂo, F. Mainardi, E. Scalas and M. Raberto Fractional calculus and continuous-time ﬁnance III: the diﬀusion limit, in: M. Kohlmann and S. Tang (Eds.), Mathematical Finance, Birkh¨auser, Basel, 2001, pp. 171-180.
- [9] M. Parkinson, Option Pricing: The American Put, Journal of Business, 50 (1977) 21-36.

- [10] R. Hilfer and L. Anton, Fractional master equations and fractal time random walks, Phys. Rev. E 51 (1995) R848–R851.
- [11] A.I. Saichev and G.M. Zaslavsky, Fractional kinetic equations: solutions and applications, Chaos 7 (1997) 753–764.
- [12] A. Erde´lyi, W. Magnus, F. Oberhettinger, F.G. Tricomi, Higher Transcendental Functions, Bateman Project, Vol. 3, McGraw-Hill, New York, 1955. [Ch. 18, pp. 206-227.]
- [13] R. Gorenﬂo and F. Mainardi, Fractional calculus, integral and diﬀerential equations of fractional order, in: A. Carpinteri and F. Mainardi (Eds.), Fractals and Fractional Calculus in Continuum Mechanics, Springer Verlag, Wien and New York, 1997, pp. 223–276. [down-loadable from: http://www.fracalmo.org]
- [14] F. Mainardi and R. Gorenﬂo, On Mittag-Leﬄer type functions in fractional evolution processes, J. Comput. & Appl. Mathematics 118 (2000) 283-299.
- [15] D.A. Berry and B.V. Linfgren, Statistics: Theory and Methods, Brooks/Cole Publishing, 1990.
- [16] S.L. Marple, Digital Spectral Analysis with Applications, Prentice-Hall, Englewood Cliﬀs, N.J., 1987.
- [17] R. Cont, Statistical properties of ﬁnancial time series, Lectures presented at the Symposium on Mathematical Finance, Fudan University, Shangai, 10-24 August

1999. These lectures are down-loadable from http://www.eleves.ens.fr:8080/home/cont/papers.html

- [18] R.N. Mantegna and H.E. Stanley, An Introduction to Econophysics: Correlations and Complexity in Finance, Cambridge University Press, Cambridge, UK, 2000.
- [19] P. Gopikrishnan, V. Plerou, Y. Liu, L. Amaral, X. Gabaix, H.E. Stanley, Scaling and correlation in ﬁnancial time series, Physica A 287 (2000) 362-373.
- [20] G. Lefol and L. Mercier, Time deformation: deﬁnition and comparisons, Journal of Computational Intelligence in Finance 6 (1998) 19-33.
- [21] M. Dacorogna, R. Genay, U.A. Mller, R.B. Olsen, O.V. Pictet, An Introduction to High-Frequency Finance, Academic Press, New-York, 2001.

200

180

160

140

120

τ{s}i

100

80

60

40

20

0

−0.015 −0.01 −0.005 0 0.005 0.01 0.015

ξi

- Fig. 1. Scatter plot of waiting times τn as a function of the corresponding log-returns ξn.

100 101 102

10−4

10−3

10−2

10−1

lag

autocorrelationofabsolutelogreturns

noise level

slope ∼ −0.76

1 10000 20000 30000 40000 50000

0

0.005

0.01

0.015

ticks

absolutelogreturns

- Fig. 2. Autocorrelation function for the absolute value of log-returns ξn. The inset shows the time series.

| |
|---|
| |
| |
| |
| |
| |
| |
| |
| |
| |
| |
| |

- 0

0.1

0.2

0.3

0.4

0.5

0.6

0.7

0.8

0.9

- 1

200

150

waitingtimes{s}

autocorrelationofwaitingtimes

100

50

0

1 10000 20000 30000 40000 50000

ticks

noise band

−0.1

0 2000 4000 6000 8000 10000

lag

- Fig. 3. Autocorrelation function for the waiting times τn. The inset shows the time series.

100 101 102

10−5

10−4

10−3

10−2

10−1

100

τ {s}

Ψτ()

|market data stretched exponential (τ0=6.6, β=0.7) standard exponential (τ0=6.6, β=1)<br><br>|
|---|

- Fig. 4. Survival probability. The stretched exponential (solid line) is compared with the standard exponential (dash-dotted line).

