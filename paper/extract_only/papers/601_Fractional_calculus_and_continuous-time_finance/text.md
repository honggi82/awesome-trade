arXiv:cond-mat/0001120v1[cond-mat.dis-nn]10Jan2000

Fractional calculus and continuous-time ﬁnance

Enrico Scalasa, Rudolf Gorenﬂob, and Francesco Mainardic

aDipartimento di Scienze e Tecnologie Avanzate, Universit`a del Piemonte Orientale, via Cavour 84, I–15100 Alessandria, Italy and INFN Sezione di Torino, via P.Giuria 1, I–10125 Torino, Italy bErstes Matematisches Institut, Freie Universitaet Berlin, Arnimallee 2-6, D–14195 Berlin, Germany cDipartimento di Fisica, Universita` di Bologna and INFN Sezione di Bologna, via Irnerio 46, I–40126 Bologna, Italy

[Figure 1]

Abstract

In this paper we present a rather general phenomenological theory of tick-by-tick dynamics in ﬁnancial markets. Many well-known aspects, such as the Le´vy scaling form, follow as particular cases of the theory. The theory fully takes into account the non-Markovian and non-local character of ﬁnancial time series. Predictions on the long-time behaviour of the waiting-time probability density are presented. Finally, a general scaling form is given, based on the solution of the fractional diﬀusion equation.

Key words: Stochastic processes; random walk; statistical ﬁnance; econophysics PACS: 02.50.Ey, 02.50.Wp, 89.90.+n Corresponding author: Enrico Scalas (scalas@unipmn.it), url: www.econophysics.org

[Figure 2]

- 1 Introduction

The importance of random walks in ﬁnance has been known since the seminal work of Bachelier [1] which was completed at the end of the XIXth century, nearly a hundred years ago. The ideas of Bachelier were further carried out by Mandelbrot [2], who introduced the concept of L´evy ﬂights and stable distributions [3] in ﬁnance, and by the MIT school of Samuelson [4].

Although it was well-known that the distribution of returns or of logarithmic returns approximately followed a stable law, there was a barrier to the appli-

Preprint submitted to Elsevier Preprint 6 December 1999

cation of these concepts in the ﬁnancial practice. Indeed, stable distributions have non-ﬁnite variance, and this leads to many mathematical diﬃculties (for a discussion on this point the reader is referred to chapter 3 of Merton’s book [4]). Therefore, in mainstream ﬁnance, both theoreticians and practitioners prefer to use the more tractable continuous Wiener process instead of discontinuous L´evy ﬂights. A way of overcoming these diﬃculties has been provided by empirical studies suggesting the use of truncated L´evy ﬂights, characterized by probability density distributions with ﬁnite moments [5–8].

In ﬁnancial markets, not only prices and returns can be considered as random variables, but also the waiting time between two transactions varies randomly. So far, a large part of the ﬁnancial practice is based on daily price changes. However, a company specialized in intra–day transactions and high–frequency data analysis, Olsen & Associates, has published various working papers related to the time behaviour of tick-by-tick data (see, for instance, on fractional time ref. [9] and on mean ﬁrst passage time ref. [10]).

The purpose of this paper is to present a rather general phenomenological theory of tick-by-tick dynamics in ﬁnancial markets. Many well-known aspects, such as the L´evy scaling form of ref. [6], follow as particular cases of the theory. The theory fully takes into account the non-Markovian and non-local character of ﬁnancial time series. Predictions on the long-time behaviour of the waitingtime probability density are presented. Finally, a more general scaling form is given, based on the solution of the fractional diﬀusion equation.

The paper is divided as follows. In Sec. 2, we discuss the relevance of continuoustime random walks in ﬁnance by explicitly performing a mapping from ﬁnancial data to random walks. In Sec. 3, we present the master equation and we show that it reduces to the fractional diﬀusion equation in the hydrodynamic limit (corresponding to a long jump-observation scale and long observation times) if some simple scaling assumptions on the jump and waiting-time probability densities hold true. Sec. 4 is devoted to the solutions of the fractional diﬀusion equation and their natural scaling properties. Finally, in Sec. 5, we point out the main conclusions and outline the direction for future work.

As a ﬁnal remark, let us stress that the theory of continuous-time random walks is well developed [11,12], and its relation to the fractional diﬀusion equation and fractional calculus [13] has been recently discussed by various authors [14–18]. However, as far as we know, these concepts have not yet been applied to ﬁnance in the form we present here.

- 2 Continuous-time random walk in ﬁnance

The price dynamics in ﬁnancial markets can be mapped onto a random walk whose properties are studied in continuous, rather than discrete, time [4]. Here, we shall perform this mapping, pioneered by Bachelier [1] and fully exploited by Samuelson and his school [4], in a rather general way.

As a matter of fact, there are various ways in which to embed a random walk in continuous time. Here, we shall base our approach on the so-called continuoustime random walk (henceforth abbreviated as CTRW) in which time intervals between successive steps are random variables, as discussed by Montroll and Weiss [11]

Let S(t) denote the price of an asset or the value of an index at time t. In a real market, prices are ﬁxed when demand and oﬀer meet and a transaction occurs. In this case, we say that a trade takes place. In ﬁnance, returns rather than prices are considered. For this reason, in the following we shall take into account the variable x(t) = logS(t), that is the logarithm of the price. Indeed, for a small price variation ∆S = S(ti+1)−S(ti), the return r = ∆S/S(ti) and the logarithmic return rlog = log[S(ti+1)/S(ti)] virtually coincide.

As we mentioned before, in ﬁnancial markets, not only prices can be modelled as random variables, but also waiting times between two consecutive transactions vary in a stochastic fashion. Therefore, the time series {x(ti)} is characterised by ϕ(ξ,τ), the joint probability density of jumps ξi = x(ti+1) − x(ti) and of waiting times τi = ti+1−ti. The joint density satisﬁes the normalization condition dξdτϕ(ξ,τ) = 1.

Montroll and Weiss [11] have shown that the Fourier-Laplace transform of p(x,t), the probability density function, pdf, of ﬁnding the value x of the price logarithm (which is the diﬀusing quantity in our case) at time t, is given by:

1 − ψ(s) s

1 1 − ϕ(κ,s)

p(κ,s) =

, (1)

[Figure 3]

[Figure 4]

where

p(κ,s) =

+∞ 0

dt

+∞ −∞

dxe−st + iκx p(x,t) , (2)

and ψ(τ) = dξ ϕ(ξ,τ) is the waiting time pdf.

Let us now consider the situation in which the waiting time and the size of the step are independent. In this case the joint density function, ϕ, can be factorized, namely written as the product of a “spatial” part and a temporal part: ϕ(ξ,τ) = λ(ξ)ψ(τ). Here λ(ξ) is the probability for a displacement ξ

in each single step (transition probability density). Now, the normalization condition for the transition pdf: dξλ(ξ) = 1 must be added to that for the probability density of the waiting time dτψ(τ) = 1.

As a consequence we get:

1 − ψ(s) s

1 1 − λ(κ) ψ(s)

p(κ,s) =

[Figure 5]

[Figure 6]

Ψ(s) 1 − λ(κ) ψ(s)

=

, (3)

[Figure 7]

where λ(κ) , the Fourier transform of the transition probability density, is usually called the structure function of the random walk and Ψ(s) = (1 − ψ˜(s))/s is the Laplace transform of

Ψ(t) =

∞ t

ψ(t′) dt′ = 1 −

t 0

ψ(t′) dt′ . (4)

Ψ(t) is the survival probability at the initial point position (t0 = 0) [15].

t

0 ψ(t′) dt′ represents the probability that at least one step is taken in the interval (0,t), hence Ψ(t) is the probability that the diﬀusing quantity does not change during the time interval of duration t after a jump [18].

According to Weiss [19], Ψ(t) can be viewed as the probability that the duration of a given interval between successive steps is strictly greater than t and is the peculiar function needed to specify the probability of the displacement at time t∗ + t in a CTRW, where t∗ is the instant of the last jump. The waiting-time pdf is related to Ψ(t) by the formula: ψ(t) = −dΨ(t)/dt.

Let us ﬁnally remark that, in general, the CTRW is a non-Markovian model [19], as at any time one has to know the value of the diﬀusing quantity as well as the time at which the last step took place in order to predict the further course of the walk. The non-Markovian property arises because the time of the previous step does vary and could be even t = 0, so that the complete history of the process must be taken into account at all times. The only Markovian version of the CTRW is the one in which the waiting time pdf, ψ(τ), is a negative exponential:

1 T

ψ(τ) =

exp(−τ/T),

[Figure 8]

where T is the average time between successive steps. Only for this form of the density, the probability that a step of the random walk will take place in (t, t + dt) is dt/T , as dt → 0 , independent of the time at which the immediately preceding step occurred. This is not true of any other form of ψ(τ) .

- 3 Master equations and fractional diﬀusion

The master equation governing the probability density proﬁle in a CTRW can be derived by inverting the Fourier-Laplace transform in eq. (3). Rewriting (3) as

p(κ,s) = Ψ(s) + ψ(s) λ(κ) p(κ,s) we obtain

p(x,t) = δx0Ψ(t) +

t 0

dt′ ψ(t − t′)

+∞ −∞

dx′ λ(x − x′) p(x′,t′) . (5)

This form of the master equation is quoted, e.g., in Klafter et al. [20] and Hilfer and Anton [15]. However, equivalent forms can be found in the literature. The following form shows the non-local and non-Markovian character of the CTRW [12,18]:

∂ ∂t

p(x,t) =

[Figure 9]

t 0

dt′ φ(t − t′) −p(x,t′) +

+∞ −∞

dx′ λ(x − x′) p(x′,t′) ; (6)

here, the kernel φ(t) is deﬁned through its Laplace transform

s ψ(s) 1 − ψ(s)

φ(s) =

.

[Figure 10]

The above equations allow to compute p(x,t) from the knowledge of the jump pdf λ(ξ) and of the waiting-time pdf ψ(τ). In principle, both these quantities are empirically accessible from high-frequency market data, even if, recently, within the physics community, emphasis has been given to the jump pdf [6].

The time-evolution equation for p(x,t) has a remarkable limit, if some scaling conditions on the structure function and on the waiting time pdf are veriﬁed.

Let us assume the following scaling behaviour in the hydrodynamic limit (longjump scale and long observation times):

λ(κ) ∼ 1 − |κ|α , κ → 0 , 0 < α ≤ 2 , (7) and

ψ(s) ∼ 1 − sβ , s → 0 , 0 < β ≤ 1 . (8)

The above approximations are consistent with the following explicit expressions for the Fourier and Laplace transforms:

λ(κ) = exp(−|κ|α) , 0 < α ≤ 2 , (9)

and

1 1 + sβ

ψ(s) =

, 0 < β ≤ 1 . (10)

[Figure 11]

We note that eq. (9) represents the characteristic function for the symmetric L´evy stable pdf of index α ; for 0 < α < 2 the pdf decays like |x|−(α+1) as |x| → ∞ , for α = 2 the Gaussian pdf is recovered.

From eq. (10), we observe that

1 − ψ(s) s

Ψ(s) =

[Figure 12]

sβ−1 1 + sβ

=

, 0 < β ≤ 1 , (11)

[Figure 13]

so that the survival probability turns out to be

Ψ(t) = Eβ(−tβ) , 0 < β ≤ 1 , (12) where

∞

tβn Γ(βn + 1)

(−1)n

Eβ(−tβ) =

[Figure 14]

n=0

is the Mittag-Leﬄer function of order β [21,22]. Thus the pdf for the waiting time is

d dt

ψ(t) = −

[Figure 15]

d dt

Ψ(t) = −

[Figure 16]

Eβ(−tβ) , 0 < β ≤ 1 , (13)

which is in agreement with the expression obtained in [15] in terms of the generalized Mittag-Leﬄer function in two parameters.

For 0 < β < 1 the Mittag-Leﬄer function Eβ(−tβ) is known to be, for t > 0, a completely monotonic function of t, decreasing from 1 (at t = 0) to 0 like t−β as t → ∞ [22]. As a consequence the pdf for the waiting time is strictly positive and monotonically decreasing to zero like t−(β+1) . For β = 1 the Mittag-Leﬄer function reduces to exp(−t) and we recover from eqs. (11 – 13) the Markovian CTRW.

If we insert eqs. (7) and (8) into eq. (1), we get the limiting relation: sβ p(κ,s) + |κ|α p(κ,s) = sβ−1 . (14)

Inverting eq. (14), we obtain the time-evolution equation for p(x,t) in the hydrodynamic limit. If 0 < β ≤ 1 and 0 < α ≤ 2, we have, for x ∈ R:

∂βp(x,t) ∂tβ

=

[Figure 17]

∂αp(x,t) ∂|x|α

+

[Figure 18]

t−β Γ(1 − β)

δ(x), (t > 0). (15)

[Figure 19]

In eq. (15), we have introduced the fractional derivatives ∂β/∂tβ and ∂α/∂|x|α deﬁned as the inverse Laplace and Fourier transforms of sβ and −|κ|α, respectively [13,17]. Fractional derivatives are non-local operators belonging to the larger class of pseudo-diﬀerential operators [23,24], which allow power-law eﬀects. In particular, the “time” operator in eq. (15) is the Riemann-Liouville fractional derivative of order β deﬁned as (if 0 < β < 1):

dβ dtβ

1 Γ(1 − β)

d dt

f(t) =

[Figure 20]

[Figure 21]

[Figure 22]

f(τ) (t − τ)β

t 0

dτ ,

[Figure 23]

whereas the “jump” operator is the Riesz fractional derivative of order α which, if 0 < α < 2 can be represented as [13]:

dα d|x|α

sin(απ/2) π

f(x) = Γ(1 + α)

[Figure 24]

[Figure 25]

f(x + ξ) − 2f(x) + f(x − ξ) ξ1+α

∞ 0

dξ .

[Figure 26]

Finally, let us mention that eq. (14) was derived by Weiss [19] and by Afanas’ev and co-workers [25]. Moreover, the above derivation of eq. (15) was implicit in a paper by Fogedby [14] and was explicitly presented by Compte [16] and by Saichev and Zaslavsky [17].

- 4 Le´vy ﬂights and scaling of solutions

We start this section with the analysis of a particular case of eq. (15), the limit β → 1, where we have (in the weak sense) [17]:

t−β Γ(1 − β)

lim

= δ(t),

[Figure 27]

β→1

and eq. (15) becomes equivalent to the following initial value problem:

∂p(x,t) ∂t

[Figure 28]

∂αp(x,t) ∂|x|α

=

, p(x, 0) = δ(x). (16)

[Figure 29]

The Cauchy problem (16) can be solved by Fourier-transforming both sides of the equation with respect to x. After integrating and inverse Fourier-transforming, one gets:

1 t1/α

Lα

p(x,t) =

[Figure 30]

x t1/α

[Figure 31]

, (17)

where Lα(u) is the L´evy standardized probability density function:

- 1

[Figure 32]

- 2π

Lα(u) =

+∞ −∞

e−iqu−|q|

α

dq. (18)

Taking the limit β → 1 in eq. (15) corresponds to considering independent time increments. Continuous-time random walks whose pdf p(x,t) is given by eq. (17) are called symmetric L´evy ﬂights or better symmetric α-stable L´evy processes [3,26]. In 1963, analysing the scaling properties of ﬁnancial timeseries, Mandelbrot [2] found that the empirical pdf p(x,t) could be well ﬁtted by the L´evy density function (17) with α = 1.7. As we mentioned in the introduction, the main diﬃculty in dealing with the L´evy distribution is that its moments diverge. For 0 < α < 2, the only bounded ﬁnite moments have index γ satisfying −1 < γ < α. For this reason, the results of Mandelbrot were well-known but not much used in mainstream quantitative ﬁnance [4]. The recent empirical analysis of Mantegna and Stanley [6] suggests that truncated L´evy ﬂights should be used instead, as good models for ﬁnancial price dynamics [5]. Koponen [7] introduced a class of truncated L´evy ﬂights, which was successively generalized by Boyarchenko and Levendorskii [8]. However, all these studies somehow neglected the waiting-time pdf.

In the general case, the Cauchy problem of eq. (15) can be solved by the same technique used above. There is, however, a mathematical subtlety. In order to give a meaning to the Cauchy problem, the Riemann-Liouville operator must be replaced by the Caputo fractional derivative of order β [22,27]:

dβ dtβ

1 Γ(1 − β)

d dt

f(t) =

[Figure 33]

[Figure 34]

[Figure 35]

t−β Γ(1 − β)

f(τ) (t − τ)β

t 0

dτ −

f(0) .

[Figure 36]

[Figure 37]

Now, the solution is:

1 tβ/α

Wα,β

p(x,t) =

[Figure 38]

x tβ/α

[Figure 39]

, (19)

and Wα,β(u) is the following scaling function:

- 1

[Figure 40]

- 2π

+∞

e−iquEβ(−|q|α)dq, (20) where Eβ the Mittag-Leﬄer function of order β and argument z = −|q|α Further empirical studies on high-frequency ﬁnancial data may reveal the scaling form (20), if the waiting-time pdf satisﬁes the asymptotics (8).

Wα,β(u) =

−∞

- 5 Conclusions and outlook

In this paper, we argued that the continuous-time random walk (CTRW) is a good phenomenological model for high-frequency price dynamics in ﬁnancial markets, as, in general, this dynamics is non-Markovian and/or non-local.

CTRW naturally leads to the so-called fractional diﬀusion equation in the hydrodynamic limit if some scaling properties of the waiting time pdf ψ(τ) and of the jump pdf λ(ξ) hold true in that limit. This point needs a further discussion. Indeed, the scaling regime of eqs. (8) and (7) breaks down for very large jumps. For this reason, truncated L´evy ﬂights have been introduced [5– 8]. Preliminary investigations [28] on high frequency ﬁnancial data show that a similar problem is present for the waiting time pdf. Nevertheless, we can view the fractional diﬀusion equation (15) as a model for approximating the true behaviour of returns in ﬁnancial markets.

In the region where the dynamics is well approximated by eq. (15), we expect the following scaling for the waiting-time pdf (see the discussion in Sec. 3):

ψ(τ) ∼ τ−µ, (21)

where µ = β + 1 varies in the range 1 < µ < 2. Consequently, the more complex scaling form (20) should hold true.

Empirical analyses on market high-frequency data will be necessary in order to verify these predictions. In any case, we expect that the concepts of CTRW and of fractional calculus will be of help in practical applications such as option pricing, as they provide an intuitive background for dealing with nonMarkovian and non-local random processes.

In this paper, the mathematical apparatus has been kept to a minimum, the interested reader will ﬁnd full mathematical details in a forthcoming paper [29].

Acknowledgements

This work was partially supported by the Italian INFM and INFN, and by the Research Commission of the Free University in Berlin. R. G. is grateful to the Italian ”Istituto Nazionale di Alta Matematica” for supporting his visit in Italy. E. S. wishes to thank CERN for its wonderful library open 24 hours a day: an ideal place to study in a quiet atmosphere after shifts at the colliders. Discussions on high-frequency ﬁnancial data with Marco Raberto inspired this work.

References

- [1] L.J.B. Bachelier: Theorie de la Speculation, Gauthier-Villars, Paris, 1900, Reprinted in 1995, Editions Jaques Gabay, Paris, 1995.

- [2] B. Mandelbrot, Journal of Business 36 (1963) 394.
- [3] P. Le´vy, The´orie de l’Addition des Variables Ale´atoires, Gauthier–Villars, Paris, 1937.
- [4] R.C. Merton, Continuous Time Finance, Blackwell, Cambridge, MA, 1990.
- [5] R.N. Mantegna, H.E. Stanley, Phys. Rev. Lett. 73 (1994) 2946.
- [6] R.N Mantegna and H.E. Stanley, Nature 376 (1995) 46.
- [7] I. Koponen, Phys. Rev. E 52 (1995) 1197.
- [8] S.I. Boyarchenko and S.Z. Levendorskii, 1999 preprint, downloadable from: http://l3www.cern.ch/homepages/susinnog/Library/biblioindex.html.
- [9] U.A. Mu¨ller, M.M. Dacorogna, R.D. Dave´, O.V. Pictet, R. B. Olsen and J.R. Ward, 1993, Olsen, internal document UAM.1993-08-16, downloadable from http://www.olsen.ch/library/research/oa working.html.

[Figure 41]

- [10] G. Zumbach, 1998, Olsen, internal document GOZ.1998-01-15, downloadable from http://www.olsen.ch/library/research/oa working.html.

[Figure 42]

- [11] E.W. Montroll and G.H. Weiss, J. Math. Phys. 6 (1965) 167.
- [12] E.W. Montroll and M.F. Shlesinger, On the wonderful world of random walks, in: J. Lebowitz and E.W. Montroll (Eds.), Nonequilibrium Phenomena II: from Stochastics to Hydrodynamics, North-Holland, Amsterdam, 1984, pp. 1–122.
- [13] S.G. Samko, A.A. Kilbas, O.I. Marichev, Fractional Integrals and Derivatives. Theory and Applications, Gordon and Breach Science Publishers, 1993.
- [14] H.C. Fogedby, Phys. Rev. E 50 (1994) 1657.
- [15] R. Hilfer and L. Anton, Phys. Rev. E 51 (1995) R848.
- [16] A. Compte, Phys. Rev. E 53 (1996) 4191.
- [17] A.I. Saichev and G.M. Zaslavsky, Chaos 7 (1997) 753.
- [18] R. Balescu, Statistical Dynamics: Matter out of Equilibrium, Imperial College Press - World Scientiﬁc, London, 1994.
- [19] G.H. Weiss, Aspects and Applications of the Random Walk, North-Holland, Amsterdam, 1994.
- [20] J. Klafter, A. Blumen and M.F. Shlesinger, Phys. Rev. A 35 (1987) 3081.
- [21] A. Erde´lyi (Ed.), Higher Transcendental Functions, Bateman Project, Vol. 3, McGraw-Hill, New York, 1955.
- [22] R. Gorenﬂo and F. Mainardi, Fractional calculus, integral and diﬀerential equations of fractional order, in Fractals and fractional calculus in continuum mechanics, A. Carpinteri and F. Mainardi (Eds.), Springer, Wien and New York, 1997, pp. 223–276.

- [23] L. H¨o rmander, The Analysis of Linear Partial Diﬀerential Operators III. Pseudo-Diﬀerential Operators, Springer, Berlin, 1985.
- [24] N. Jacob, Pseudo-Diﬀerential Operators and Markov Processes, Akademie Verlag, Berlin, 1996.
- [25] V.V. Afanas’ev, R.Z. Sagdeev, and G.M. Zaslavsky, Chaos 1 (1991) 143.
- [26] A. Janicki, A. Weron, Simulation and Chaotic Behavior of α–Stable Stochastic Processes, Marcel Dekker, New York, 1994.
- [27] I. Podlubny, Fractional Diﬀerential Equations, Academic Press, San Diego, 1999.
- [28] E. Scalas, M. Raberto, F. Mainardi, and R. Gorenﬂo, in preparation.
- [29] R. Gorenﬂo, F. Mainardi, and E. Scalas, in preparation.

