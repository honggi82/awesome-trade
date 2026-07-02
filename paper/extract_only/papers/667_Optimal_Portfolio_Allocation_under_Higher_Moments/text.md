# NOTES D’ÉTUDES ET DE RECHERCHE

|OPTIMAL PORTFOLIO ALLOCATION UNDER HIGHER MOMENTS<br><br>Eric Jondeau and Michael Rockinger<br><br>Février 2004<br><br>NER # 108|
|---|

[Figure 1]

DIRECTION GÉNÉRALE DES ÉTUDES ET DES RELATIONS INTERNATIONALES

#### DIRECTION GÉNÉRALE DES ÉTUDES ET DES RELATIONS INTERNATIONALES

###### DIRECTION DES ÉTUDES ÉCONOMIQUES ET DE LA RECHERCHE

|OPTIMAL PORTFOLIO ALLOCATION UNDER HIGHER MOMENTS<br><br>Eric Jondeau and Michael Rockinger<br><br>Février 2004<br><br>NER # 108|
|---|

Les Notes d'Études et de Recherche reflètent les idées personnelles de leurs auteurs et n'expriment pas nécessairement la position de la Banque de France. Ce document est disponible sur le site internet de la Banque de France « www.banque-France.fr ».

The Working Paper Series reflect the opinions of the authors and do not necessarily express the views of the Banque de France. This document is available on the Banque de France Website “www.banqueFrance.fr”.

| |
|---|

| |
|---|

| |
|---|

[Figure 2]

Number of observations

Data Description of variables Period Frequency

- DS1 Returns for dollar-denominated MSCI stockmarket indices for the main geographical areas (North America, Europe, and Asia)

From 1/1976 to 12/2001

Weekly 1354

- DS2 Returns for stocks included in the S&P100 (Delta Air Lines, Gillette, and Southern)

From 1/1973 to 1/2003

Weekly 1568

- DS3 Returns for emerging stock-market indices (Hang Seng index for Hong Kong, KOSPI index for South Korea, and S.E.T. index for Thailand)

From 2/1975 to 6/2002

Monthly 336

###### Table 1: Description of data sets under investigation

North America Europe Asia Panel A: Univariate statistics

T=1355

Moments stat. s.e. stat. s.e. stat. s.e.

- Mean 0.251 (0.055) 0.246 (0.058) 0.195 (0.083) Std 2.094 (0.099) 2.031 (0.086) 2.595 (0.100) SK -0.660 (0.342) -0.604 (0.316) -0.038 (0.123) XKu 3.873 (2.137) 2.984 (1.819) 1.488 (0.292) Normality tests stat. p-val. stat. p-val. stat. p-val. JB 945.239 (0.000) 585.198 (0.000) 125.404 (0.000) Omnibus 258.956 (0.000) 181.404 (0.000) 89.080 (0.000)

- KS 1.529 a 1.759 a 1.710 a

Serial correlation

QW(4) 1.854 (0.763) 2.320 (0.677) 10.412 (0.034) LM(1) 104.460 (0.000) 135.093 (0.000) 20.620 (0.000) LK(1) 10.215 (0.000) 11.627 (0.000) 4.542 (0.000)

Panel B: Multivariate statistics

Correlation matrix stat. s.e. stat. s.e. stat. s.e. stat. s.e.

###### x1 x2 x3

x1 1 0.526 (0.036) 0.327 (0.035) x2 0.526 (0.036) 1 0.478 (0.025) x3 0.327 (0.035) 0.478 (0.025) 1

Co-skewness matrix

###### x12 x22 x32 x1x2

x1 -0.660 (0.342) -0.523 (0.329) -0.264 (0.128) x2 -0.585 (0.338) -0.604 (0.316) -0.231 (0.117) x3 -0.231 (0.207) -0.348 (0.168) -0.038 (0.123) -0.265 (0.189)

Co-kurtosis matrix

###### x13 x23 x33

x1 6.873 (2.137) 4.376 (2.008) 1.716 (0.482) x2 4.712 (2.164) 5.984 (1.819) 2.217 (0.393) x3 2.956 (1.326) 3.027 (0.957) 4.488 (0.292)

x1x22 x1x32 x2x32 x12x2 x1 4.449 (2.075) 2.645 (0.717) x2 1.960 (0.668) 2.516 (0.561) x3 2.404 (1.101) 2.540 (1.199)

###### Multivariate Normality test stat. s.e.

Omnibus 309.812 (0.000) Small 287.877 (0.000) Mardia 1229.963 (0.000)

- Table 2a: Statistics on weekly MSCI returns (DS1)

Delta Air Lines Gillette Southern

T=1568

- Panel A: Univariate statistics
- Panel B: Multivariate statistics

Moments stat. s.e. stat. s.e. stat. s.e.

Mean -0.021 (0.123) 0.175 (0.098) 0.097 (0.061) Std 5.032 (0.272) 4.188 (0.263) 2.776 (0.116) SK -0.888 (0.506) -1.347 (0.925) 0.197 (0.227) XKu 8.240 (4.234) 16.875 (10.519) 4.264 (0.904) Normality tests stat. p-val. stat. p-val. stat. p-val.

JB 4641.44 (0.000) 19077.67 (0.000) 1198.07 (0.000) Omnibus 801.032 (0.000) 1674.067 (0.000) 503.176 (0.000)

- KS 2.019 a 2.386 a 2.622 a

Serial correlation

QW(4) 4.554 (0.336) 5.574 (0.233) 4.425 (0.352) LM(1) 13.340 (0.000) 0.152 (0.697) 21.910 (0.000) LK(1) 3.645 (0.000) 0.391 (0.348) 4.685 (0.000)

Correlation matrix stat. s.e. stat. s.e. stat. s.e. stat. s.e.

###### x1 x2 x3

x1 1 0.147 (0.033) 0.283 (0.035) x2 0.282 (0.034) 1.000 0.234 (0.036) x3 0.147 (0.033) 0.234 (0.036) 1.000

Co-skewness matrix

###### x12 x22 x32 x1x2

x1 -0.888 (0.506) -0.472 (0.407) -0.130 (0.109) x2 -0.237 (0.167) -1.347 (0.925) -0.179 (0.200) x3 0.002 (0.100) -0.457 (0.446) 0.197 (0.227) -0.217 (0.185)

Co-kurtosis matrix

###### x13 x23 x33

x1 11.240 (4.234) 6.687 (4.788) 0.984 (0.587) x2 1.980 (0.809) 19.875 (10.519) 1.947 (0.946) x3 0.256 (0.644) 6.459 (5.054) 7.264 (0.904)

x1x22 x1x32 x2x32 x12x2 x1 3.320 (1.970) 1.696 (0.397) x2 1.361 (0.928) 3.673 (2.122) x3 2.721 (2.119) 1.231 (0.899)

###### Multivariate Normality test stat. s.e.

Omnibus 2900.84 (0.000) Small 2876.56 (0.000) Mardia 14997.99 (0.000)

- Table 2b: Statistics on weekly S&P100 stock returns (DS2)

Hong Kong South Korea Thailand

T=336

- Panel A: Univariate statistics
- Panel B: Multivariate statistics

Moments stat. s.e. stat. s.e. stat. s.e.

- Mean 1.078 (0.438) 0.737 (0.497) 0.898 (0.602) Std 8.698 (0.657) 7.861 (0.756) 9.834 (0.872) SK -0.684 (0.304) 0.052 (0.380) 0.339 (0.194) XKu 2.856 (1.066) 2.522 (1.159) 1.473 (0.391) Normality tests stat. p-val. stat. p-val. stat. p-val. JB 140.425 (0.000) 89.217 (0.000) 36.805 (0.000) Omnibus 44.593 (0.000) 58.333 (0.000) 22.465 (0.000) KS 1.300 a 1.126 a 1.214 a

Serial correlation

QW(4) 4.732 (0.316) 0.525 (0.971) 3.341 (0.503) LM(1) 3.449 (0.063) 32.935 (0.000) 36.903 (0.000) LK(1) 1.868 (0.031) 5.748 (0.000) 5.956 (0.000)

Correlation matrix stat. s.e. stat. s.e. stat. s.e. stat. s.e.

###### x1 x2 x3

x1 1 0.254 (0.064) 0.271 (0.067) x2 0.254 (0.064) 1 0.228 (0.060) x3 0.271 (0.067) 0.228 (0.060) 1

Co-skewness matrix

###### x12 x22 x32 x1x2

x1 -0.684 (0.304) 0.088 (0.157) -0.097 (0.095) x2 0.056 (0.166) 0.052 (0.380) 0.014 (0.079) x3 -0.184 (0.152) 0.017 (0.091) 0.339 (0.194) -0.008 (0.085)

Co-kurtosis matrix

###### x13 x23 x33

x1 5.856 (1.066) 0.776 (0.781) 0.855 (0.303) x2 1.469 (0.427) 5.522 (1.159) 0.495 (0.249) x3 1.826 (0.524) 0.298 (0.532) 4.473 (0.391)

x1x22 x1x32 x2x32 x12x2 x1 1.967 (0.360) 1.355 (0.247) x2 0.446 (0.170) 1.227 (0.161) x3 0.867 (0.243) 0.690 (0.196)

###### Multivariate Normality test stat. s.e.

Omnibus 151.654 (0.000) Small 151.643 (0.000) Mardia 307.998 (0.000)

- Table 2c: Statistics on monthly emerging stock-market returns (DS3)

- 1 0.607 0.393 0.000 - 0.249 1.822 -0.858 8.166 -
- 2 0.537 0.463 0.000 - 0.249 1.806 -0.863 8.184 5 0.489 0.498 0.013 - 0.248 1.794 -0.858 8.158 -

10 0.443 0.440 0.117 - 0.242 1.751 -0.824 8.076 15 0.421 0.418 0.161 - 0.240 1.744 -0.800 7.944 20 0.401 0.406 0.194 - 0.238 1.742 -0.778 7.802 -

###### Panel B: Taylor expansion up to order 2

- 1 0.608 0.392 0.000 0.002 0.249 1.822 -0.858 8.165 0.000
- 2 0.538 0.462 0.000 0.003 0.249 1.806 -0.863 8.185 0.000 5 0.495 0.502 0.003 0.020 0.248 1.800 -0.860 8.153 0.002

10 0.455 0.448 0.098 0.039 0.243 1.757 -0.833 8.120 0.002 15 0.441 0.430 0.129 0.064 0.242 1.749 -0.819 8.054 0.002 20 0.435 0.421 0.144 0.099 0.241 1.746 -0.810 8.011 0.002

###### Panel C: Taylor expansion up to order 3

- 1 0.607 0.393 0.000 0.000 0.249 1.822 -0.858 8.166 0.000
- 2 0.537 0.463 0.000 0.000 0.249 1.806 -0.863 8.184 0.000 5 0.491 0.498 0.011 0.004 0.248 1.795 -0.859 8.158 0.001

10 0.448 0.441 0.111 0.012 0.243 1.753 -0.827 8.093 0.001 15 0.433 0.420 0.148 0.027 0.241 1.745 -0.808 8.000 0.001 20 0.424 0.408 0.168 0.051 0.240 1.743 -0.796 7.932 0.001

###### Panel D: Taylor expansion up to order 4

- 1 0.607 0.393 0.000 0.000 0.249 1.822 -0.858 8.166 0.000
- 2 0.537 0.463 0.000 0.000 0.249 1.806 -0.863 8.184 0.000 5 0.490 0.498 0.013 0.000 0.248 1.794 -0.858 8.158 0.000

10 0.445 0.440 0.116 0.003 0.242 1.752 -0.825 8.081 0.000 15 0.426 0.419 0.156 0.011 0.240 1.744 -0.803 7.968 0.000 20 0.413 0.407 0.180 0.028 0.239 1.742 -0.788 7.874 0.000

###### Table 3a: Optimal allocation for weekly MSCI returns (DS1)

1 0.000 0.635 0.365 - 0.146 3.059 -1.271 19.121 2 0.000 0.434 0.567 - 0.131 2.666 -0.887 14.614 5 0.016 0.291 0.694 - 0.118 2.528 -0.488 10.814 -

10 0.081 0.187 0.733 - 0.102 2.466 -0.294 9.034 15 0.107 0.120 0.773 - 0.094 2.479 -0.155 7.971 20 0.126 0.067 0.808 - 0.087 2.513 -0.058 7.331 -

###### Panel B: Taylor expansion up to order 2

1 0.000 0.647 0.354 0.023 0.147 3.088 -1.283 19.274 0.233 2 0.000 0.449 0.551 0.032 0.132 2.688 -0.929 15.070 0.129 5 0.013 0.325 0.661 0.069 0.121 2.548 -0.593 11.718 0.117

10 0.074 0.259 0.667 0.146 0.108 2.473 -0.509 10.716 0.140 15 0.093 0.238 0.669 0.235 0.104 2.459 -0.478 10.307 0.154 20 0.103 0.228 0.670 0.323 0.103 2.454 -0.463 10.103 0.149

###### Panel C: Taylor expansion up to order 3

1 0.000 0.636 0.364 0.003 0.147 3.063 -1.272 19.141 0.029 2 0.000 0.436 0.564 0.006 0.131 2.670 -0.894 14.695 0.022 5 0.013 0.302 0.685 0.022 0.119 2.536 -0.516 11.059 0.033

10 0.072 0.221 0.708 0.068 0.106 2.468 -0.381 9.719 0.052 15 0.089 0.185 0.726 0.130 0.101 2.461 -0.305 9.047 0.056 20 0.095 0.162 0.743 0.191 0.098 2.464 -0.249 8.622 0.043

###### Panel D: Taylor expansion up to order 4

1 0.000 0.635 0.365 0.000 0.146 3.059 -1.271 19.122 0.002 2 0.000 0.434 0.566 0.001 0.131 2.666 -0.888 14.625 0.003 5 0.016 0.294 0.691 0.007 0.118 2.530 -0.497 10.894 0.010

10 0.079 0.203 0.718 0.034 0.103 2.464 -0.341 9.376 0.024 15 0.102 0.160 0.738 0.079 0.097 2.461 -0.255 8.600 0.029 20 0.117 0.131 0.752 0.130 0.093 2.467 -0.200 8.136 0.021

###### Table 3b: Optimal allocation for monthly S&P100 stock returns (DS2)

1 1.000 0.000 0.000 - 0.416 8.106 -0.652 5.526 2 0.757 0.000 0.243 - 0.264 6.792 -0.441 4.802 5 0.532 0.024 0.445 - 0.112 6.114 -0.133 3.724 -

10 0.393 0.129 0.479 - -0.022 5.846 -0.070 3.139 15 0.334 0.170 0.497 - -0.077 5.815 -0.034 2.959 20 0.300 0.194 0.506 - -0.108 5.818 -0.015 2.883 -

###### Panel B: Taylor expansion up to order 2

1 1.000 0.000 0.000 0.000 0.416 8.106 -0.652 5.526 0.000 2 0.787 0.000 0.213 0.060 0.282 6.924 -0.478 4.933 0.516 5 0.580 0.026 0.394 0.101 0.141 6.196 -0.217 3.950 0.385

10 0.476 0.114 0.410 0.168 0.037 5.914 -0.179 3.460 0.328 15 0.448 0.138 0.414 0.229 0.009 5.864 -0.164 3.332 0.298 20 0.439 0.146 0.415 0.277 0.000 5.850 -0.158 3.291 0.276

###### Panel C: Taylor expansion up to order 3

1 1.000 0.000 0.000 0.000 0.416 8.106 -0.652 5.526 0.000 2 0.763 0.000 0.237 0.013 0.268 6.819 -0.449 4.831 0.107 5 0.554 0.006 0.440 0.044 0.134 6.182 -0.139 3.822 0.150

10 0.434 0.089 0.477 0.083 0.022 5.912 -0.081 3.305 0.122 15 0.393 0.101 0.505 0.136 -0.009 5.888 -0.038 3.171 0.099 20 0.376 0.087 0.537 0.213 -0.014 5.922 0.003 3.151 0.091

###### Panel D: Taylor expansion up to order 4

1 1.000 0.000 0.000 0.000 0.416 8.106 -0.652 5.526 0.000 2 0.758 0.000 0.242 0.001 0.264 6.794 -0.442 4.804 0.009 5 0.534 0.024 0.442 0.006 0.114 6.118 -0.138 3.736 0.019

10 0.402 0.128 0.470 0.019 -0.015 5.847 -0.083 3.168 0.025 15 0.353 0.167 0.480 0.038 -0.064 5.808 -0.056 3.001 0.022 20 0.329 0.187 0.484 0.057 -0.088 5.801 -0.043 2.934 0.012

###### Table 3c: Optimal allocation for monthly emerging stock-market returns (DS3)

### Notes d'Études et de Recherche

- 1. C. Huang and H. Pagès, “Optimal Consumption and Portfolio Policies with an Infinite Horizon: Existence and Convergence,” May 1990.
- 2. C. Bordes, « Variabilité de la vitesse et volatilité de la croissance monétaire : le cas français », février 1989.
- 3. C. Bordes, M. Driscoll and A. Sauviat, “Interpreting the Money-Output Correlation: MoneyReal or Real-Real?,” May 1989.
- 4. C. Bordes, D. Goyeau et A. Sauviat, « Taux d'intérêt, marge et rentabilité bancaires : le cas des pays de l'OCDE », mai 1989.
- 5. B. Bensaid, S. Federbusch et R. Gary-Bobo, « Sur quelques propriétés stratégiques de l’intéressement des salariés dans l'industrie », juin 1989.
- 6. O. De Bandt, « L'identification des chocs monétaires et financiers en France : une étude empirique », juin 1990.
- 7. M. Boutillier et S. Dérangère, « Le taux de crédit accordé aux entreprises françaises : coûts opératoires des banques et prime de risque de défaut », juin 1990.
- 8. M. Boutillier and B. Cabrillac, “Foreign Exchange Markets: Efficiency and Hierarchy,” October 1990.
- 9. O. De Bandt et P. Jacquinot, « Les choix de financement des entreprises en France : une modélisation économétrique », octobre 1990 (English version also available on request).
- 10. B. Bensaid and R. Gary-Bobo, “On Renegotiation of Profit-Sharing Contracts in Industry,” July 1989 (English version of NER n° 5).
- 11. P. G. Garella and Y. Richelle, “Cartel Formation and the Selection of Firms,” December 1990.
- 12. H. Pagès and H. He, “Consumption and Portfolio Decisions with Labor Income and Borrowing Constraints,” August 1990.
- 13. P. Sicsic, « Le franc Poincaré a-t-il été délibérément sous-évalué ? », octobre 1991.
- 14. B. Bensaid and R. Gary-Bobo, “On the Commitment Value of Contracts under Renegotiation Constraints,” January 1990 revised November 1990.
- 15. B. Bensaid, J.-P. Lesne, H. Pagès and J. Scheinkman, “Derivative Asset Pricing with Transaction Costs,” May 1991 revised November 1991.
- 16. C. Monticelli and M.-O. Strauss-Kahn, “European Integration and the Demand for Broad Money,” December 1991.
- 17. J. Henry and M. Phelipot, “The High and Low-Risk Asset Demand of French Households: A Multivariate Analysis,” November 1991 revised June 1992.
- 18. B. Bensaid and P. Garella, “Financing Takeovers under Asymetric Information,” September 1992.

- 19. A. de Palma and M. Uctum, “Financial Intermediation under Financial Integration and Deregulation,” September 1992.
- 20. A. de Palma, L. Leruth and P. Régibeau, “Partial Compatibility with Network Externalities and Double Purchase,” August 1992.
- 21. A. Frachot, D. Janci and V. Lacoste, “Factor Analysis of the Term Structure: a Probabilistic Approach,” November 1992.
- 22. P. Sicsic et B. Villeneuve, « L'afflux d'or en France de 1928 à 1934 », janvier 1993.
- 23. M. Jeanblanc-Picqué and R. Avesani, “Impulse Control Method and Exchange Rate,” September 1993.
- 24. A. Frachot and J.-P. Lesne, “Expectations Hypothesis and Stochastic Volatilities,” July 1993 revised September 1993.
- 25. B. Bensaid and A. de Palma, “Spatial Multiproduct Oligopoly,” February 1993 revised October 1994.
- 26. A. de Palma and R. Gary-Bobo, “Credit Contraction in a Model of the Banking Industry,” October 1994.
- 27. P. Jacquinot et F. Mihoubi, « Dynamique et hétérogénéité de l'emploi en déséquilibre », septembre 1995.
- 28. G. Salmat, « Le retournement conjoncturel de 1992 et 1993 en France : une modélisation VAR », octobre 1994.
- 29. J. Henry and J. Weidmann, “Asymmetry in the EMS Revisited: Evidence from the Causality Analysis of Daily Eurorates,” February 1994 revised October 1994.
- 30. O. De Bandt, “Competition Among Financial Intermediaries and the Risk of Contagious Failures,” September 1994 revised January 1995.
- 31. B. Bensaid et A. de Palma, « Politique monétaire et concurrence bancaire », janvier 1994 révisé en septembre 1995.
- 32. F. Rosenwald, « Coût du crédit et montant des prêts : une interprétation en terme de canal large du crédit », septembre 1995.
- 33. G. Cette et S. Mahfouz, « Le partage primaire du revenu : constat descriptif sur longue période », décembre 1995.
- 34. H. Pagès, “Is there a Premium for Currencies Correlated with Volatility? Some Evidence from Risk Reversals,” January 1996.
- 35. E. Jondeau and R. Ricart, “The Expectations Theory: Tests on French, German and American Euro-rates,” June 1996.
- 36. B. Bensaid et O. De Bandt, « Les stratégies “stop-loss” : théorie et application au Contrat Notionnel du Matif », juin 1996.
- 37. C. Martin et F. Rosenwald, « Le marché des certificats de dépôts. Écarts de taux à l'émission : l'influence de la relation émetteurs-souscripteurs initiaux », avril 1996.

- 38. Banque de France - CEPREMAP - Direction de la Prévision - Erasme - INSEE - OFCE, « Structures et propriétés de cinq modèles macroéconomiques français », juin 1996.
- 39. F. Rosenwald, « L'influence des montants émis sur le taux des certificats de dépôts », octobre 1996.
- 40. L. Baumel, « Les crédits mis en place par les banques AFB de 1978 à 1992 : une évaluation des montants et des durées initiales », novembre 1996.
- 41. G. Cette et E. Kremp, « Le passage à une assiette valeur ajoutée pour les cotisations sociales : Une caractérisation des entreprises non financières “gagnantes” et “perdantes” », novembre 1996.
- 42. S. Avouyi-Dovi, E. Jondeau et C. Lai Tong, « Effets “volume”, volatilité et transmissions internationales sur les marchés boursiers dans le G5 », avril 1997.
- 43. E. Jondeau et R. Ricart, « Le contenu en information de la pente des taux : Application au cas des titres publics français », juin 1997.
- 44. B. Bensaid et M. Boutillier, « Le contrat notionnel : efficience et efficacité », juillet 1997.
- 45. E. Jondeau et R. Ricart, « La théorie des anticipations de la structure par terme : test à partir des titres publics français », septembre 1997.
- 46. E. Jondeau, « Représentation VAR et test de la théorie des anticipations de la structure par terme », septembre 1997.
- 47. E. Jondeau et M. Rockinger, « Estimation et interprétation des densités neutres au risque : Une comparaison de méthodes », octobre 1997.
- 48. L. Baumel et P. Sevestre, « La relation entre le taux de crédits et le coût des ressources bancaires. Modélisation et estimation sur données individuelles de banques », octobre 1997.
- 49. P. Sevestre, “On the Use of Banks Balance Sheet Data in Loan Market Studies : A Note,” October 1997.
- 50. P.-C. Hautcoeur and P. Sicsic, “Threat of a Capital Levy, Expected Devaluation and Interest Rates in France during the Interwar Period,” January 1998.
- 51. P. Jacquinot, « L’inflation sous-jacente à partir d’une approche structurelle des VAR : une application à la France, à l’Allemagne et au Royaume-Uni », janvier 1998.
- 52. C. Bruneau et O. De Bandt, « La modélisation VAR structurel : application à la politique monétaire en France », janvier 1998.
- 53. C. Bruneau and E. Jondeau, “Long-Run Causality, with an Application to International Links between Long-Term Interest Rates,” June 1998.
- 54. S. Coutant, E. Jondeau and M. Rockinger, “Reading Interest Rate and Bond Futures Options’ Smiles: How PIBOR and Notional Operators Appreciated the 1997 French Snap Election,” June 1998.
- 55. E. Jondeau et F. Sédillot, « La prévision des taux longs français et allemands à partir d’un modèle à anticipations rationnelles », juin 1998.

- 56. E. Jondeau and M. Rockinger, “Estimating Gram-Charlier Expansions with Positivity Constraints,” January 1999.
- 57. S. Avouyi-Dovi and E. Jondeau, “Interest Rate Transmission and Volatility Transmission along the Yield Curve,” January 1999.
- 58. S. Avouyi-Dovi et E. Jondeau, « La modélisation de la volitilité des bourses asiatiques », janvier 1999.
- 59. E. Jondeau, « La mesure du ratio rendement-risque à partir du marché des euro-devises », janvier 1999.
- 60. C. Bruneau and O. De Bandt, “Fiscal Policy in the Transition to Monetary Union: A Structural VAR Model,” January 1999.
- 61. E. Jondeau and R. Ricart, “The Information Content of the French and German Government Bond Yield Curves: Why Such Differences?,” February 1999.
- 62. J.-B. Chatelain et P. Sevestre, « Coûts et bénéfices du passage d’une faible inflation à la stabilité des prix », février 1999.
- 63. D. Irac et P. Jacquinot, « L’investissement en France depuis le début des années 1980 », avril 1999.
- 64. F. Mihoubi, « Le partage de la valeur ajoutée en France et en Allemagne », mars 1999.
- 65. S. Avouyi-Dovi and E. Jondeau, “Modelling the French Swap Spread,” April 1999.
- 66. E. Jondeau and M. Rockinger, “The Tail Behavior of Stock Returns: Emerging Versus Mature Markets,” June 1999.
- 67. F. Sédillot, « La pente des taux contient-elle de l’information sur l’activité économique future ? », juin 1999.
- 68. E. Jondeau, H. Le Bihan et F. Sédillot, « Modélisation et prévision des indices de prix sectoriels », septembre 1999.
- 69. H. Le Bihan and F. Sédillot, “Implementing and Interpreting Indicators of Core Inflation: The French Case,” September 1999.
- 70. R. Lacroix, “Testing for Zeros in the Spectrum of an Univariate Stationary Process: Part I,” December 1999.
- 71. R. Lacroix, “Testing for Zeros in the Spectrum of an Univariate Stationary Process: Part II,” December 1999.
- 72. R. Lacroix, “Testing the Null Hypothesis of Stationarity in Fractionally Integrated Models,” December 1999.
- 73. F. Chesnay and E. Jondeau, “Does correlation between stock returns really increase during turbulent period?,” April 2000.
- 74. O. Burkart and V. Coudert, “Leading Indicators of Currency Crises in Emerging Economies,” May 2000.
- 75. D. Irac, “Estimation of a Time Varying NAIRU for France,” July 2000.

- 76. E. Jondeau and H. Le Bihan, “Evaluating Monetary Policy Rules in Estimated ForwardLooking Models: A Comparison of US and German Monetary Policies,” October 2000.
- 77. E. Jondeau and M. Rockinger, “Conditional Volatility, Skewness, ans Kurtosis: Existence and Persistence,” November 2000.
- 78. P. Jacquinot et F. Mihoubi, « Modèle à Anticipations Rationnelles de la COnjoncture Simulée : MARCOS », novembre 2000.
- 79. M. Rockinger and E. Jondeau, “Entropy Densities: With an Application to Autoregressive Conditional Skewness and Kurtosis,” January 2001.
- 80. B. Amable and J.-B. Chatelain, “Can Financial Infrastructures Foster Economic Development? ,” January 2001.
- 81. J.-B. Chatelain and J.-C. Teurlai, “Pitfalls in Investment Euler Equations,” January 2001.
- 82. M. Rockinger and E. Jondeau, “Conditional Dependency of Financial Series: An Application of Copulas,” February 2001.
- 83. C. Florens, E. Jondeau and H. Le Bihan, “Assessing GMM Estimates of the Federal Reserve Reaction Function,” March 2001.
- 84. J.-B. Chatelain, “Mark-up and Capital Structure of the Firm facing Uncertainty,” June 2001.
- 85. B Amable, J.-B. Chatelain and O. De Bandt, “Optimal capacity in the Banking Sector and Economic Growth,” June 2001.
- 86. E. Jondeau and H. Le Bihan, “Testing for a Forward-Looking Phillips Curve. Additional Evidence from European and US Data,” December 2001.
- 87. G. Cette, J. Mairesse et Y. Kocoglu, « Croissance économique et diffusion des TIC : le cas de la France sur longue période (1980-2000) », décembre 2001.
- 88. D. Irac and F. Sédillot, “Short Run Assessment of French Economic activity Using OPTIM,” January 2002.
- 89. M. Baghli, C. Bouthevillain, O. de Bandt, H. Fraisse, H. Le Bihan et Ph. Rousseaux, « PIB potentiel et écart de PIB : quelques évaluations pour la France », juillet 2002.
- 90. E. Jondeau and M. Rockinger, “Asset Allocation in Transition Economies,” October 2002.
- 91. H. Pagès and J.A.C Santos, “Optimal Supervisory Policies and Depositor-Preferences Laws,” October 2002.
- 92. C. Loupias, F. Savignac and P. Sevestre, “Is There a Bank Lending Channel in France ? Evidence from Bank Panel Data,” November 2002.
- 93. M. Ehrmann, L. Gambacorta, J. Martínez-Pagés, P. Sevestre and A. Worms, “Financial systems and The Role in Monetary Policy transmission in the Euro Area,” November 2002.
- 94. S. Avouyi-Dovi, D. Guégan et S. Ladoucette, « Une mesure de la persistance dans les indices boursiers », décembre 2002.

- 95. S. Avouyi-Dovi, D. Guégan et S. Ladoucette, “What is the Best Approach to Measure the Interdependence between Different Markets? ,” December 2002.
- 96. J.-B. Chatelain and A. Tiomo, “Investment, the Cost of Capital and Monetray Policy in the Nineties in France: A Panel Data Investigation,” December 2002.
- 97. J.-B. Chatelain, A. Generale, I. Hernando, U. von Kalckreuth and P. Vermeulen, “Firm Investment and Monetary Policy Transmission in the Euro Area,” December 2002.
- 98. J.-S. Mésonnier, « Banque centrale, taux de l’escompte et politique monétaire chez Henry Thornton (1760-1815) », décembre 2002.
- 99. M. Baghli, G. Cette et A. Sylvain, « Les déterminants du taux de marge en France et quelques autres grands pays industrialisés : Analyse empirique sur la période 1970-2000 », janvier 2003.
- 100. G. Cette and C. Pfister, “The Challenges of the “New Economy” for Monetary Policy,” January 2003.
- 101. C. Bruneau, O. De Bandt, A. Flageollet and E. Michaux, “Forecasting Inflation using Economic Indicators: the Case of France,” May 2003.
- 102. C. Bruneau, O. De Bandt and A. Flageollet, “Forecasting Inflation in the Euro Area,” May 2003.
- 103. E. Jondeau and H. Le Bihan, “ML vs GMM Estimates of Hybrid Macroeconomic Models (With an Application to the “New Phillips Curve”),” September 2003.
- 104. J. Matheron and T.-P. Maury, “Evaluating the Fit of Sticky Price Models,” January 2004.
- 105. S. Moyen and J.-G. Sahuc, “Incorporating Labour Market Frictions into an Optimising-Based Monetary Policy Model,” January 2004.
- 106. M. Baghli, V. Brunhes-Lesage, O. De Bandt, H. Fraisse et J.-P. Villetelle, « MASCOTTE : Modèle d’Analyse et de préviSion de la COnjoncture TrimesTriellE », Février 2004.

- 107. E. Jondeau and M. Rockinger, “The bank Bias: Segmentation of French Fund Families,” February 2004.
- 108. E. Jondeau and M. Rockinger, “Optimal Portfolio Allocation Under Higher Moments,” February 2004.

Pour tous commentaires ou demandes sur les Notes d'Études et de Recherche, contacter la bibliothèque du Centre de recherche à l'adresse suivante :

For any comment or enquiries on the Notes d'Études et de Recherche, contact the library of the Centre de recherche at the following address :

BANQUE DE FRANCE 41-1391 - Centre de recherche 75049 Paris Cedex 01 tél : (0)1 42 92 49 55 fax : (0)1 42 92 62 92 email : thierry.demoulin@banque-france.fr

