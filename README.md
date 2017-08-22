# Riemann-zeta function

The Plot_Riemann_Zeta_Critical_Line.py generates a plot Z(t)_plot.png comparing the modulus of the
Riemann zeta function (Sum of 1/n^s for n=0 to infinity) evaluated on the critical line (for complex numbers
s=1/2+it) to the Riemann-Siegel Z-function, which is one of the most powerful numerical methods for computing
the Riemann zeta function near and on the critical line. 

It is conjectured, by the famous Riemann Hypothesis, that all of the non-trivial zeros of this function occur on the critical line. It turns out that mpmath has built in functions pertaining to the Riemann zeta function, including zeta(), zetazeros(), and siegelz().

The plot Z(t)_plot.png exposes the Riemann-Siegel formula as a convenient way of studying the Riemann zeta
function near the critical line, notice how they overlap in the first quadrant meeting at the zeros.

The code Siegel_Graph_Loop.py generates a list of plots starting at a given input, it plots the Riemann zeta function along an 
array of input values (by default the input values are from -0.5 to 1.5) converging to the Riemann zeta function evaluated at 0.5 (which is the same as the plot Z(t)_plot.png). It further demonstrates that the Riemann-Siegel formula is a good approximationg AROUND THE CRITICAL LINE. This can clearly be seen in the video called Output.mp4.

The video was created using ffmpeg which you can install on ubuntu using the command "sudo apt install ffmpeg". The command line which was used to create the video is in the text file called "Make_mp4_from_png_files_ubuntu.txt"

