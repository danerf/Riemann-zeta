# Riemann-zeta function

This code (Plot_Riemann_Zeta_Critical_Line.py) generates a plot (Z(t)_plot.png) comparing the modulus of the
Riemann zeta function (Sum of 1/n^s for n=0 to infinity) evaluated on the critical line (for complex numbers
s=1/2+it) to the Riemann-Siegel Z-function, which is one of the most powerful numerical methods for computing
the Riemann zeta function near and on the critical line. It is conjectured, by the famous Riemann Hypothesis,
that all of the non-trivial zeros of this function occur on the critical line. It turns out that mpmath has
built in functions pertaining to the Riemann zeta function, including zeta(), zetazeros(), and siegelz().

The plot Z(t)_plot.png exposes the Riemann-Siegel formula as a convenient way of studying the Riemann zeta
function near the critical line, notice how they overlap in the first quadrant meeting at the zeros.

