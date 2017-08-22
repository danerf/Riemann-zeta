
# coding: utf-8

# In[1]:

import numpy as np
import matplotlib.pyplot as plt
#The next library contains the zeta(), zetazero(), and siegelz() functions
from mpmath import *
mp.dps = 25; mp.pretty = True

def graph_zeta(real, image_name):
    A,B,C = [], [], []

    fig = plt.figure()
    ax = fig.add_subplot(111)

    for i in np.arange(0.1, 60.0, 0.1):
        function = zeta(real + 1j*i)
        function1 = siegelz(i)
        A.append(abs(function))
        B.append(function1)
        C.append(i)

    ax.grid(True)
    ax.plot(C,A, label='modulus of Riemann zeta function along critical line, s = 1/2 + it', lw=0.8)
    ax.plot(C,B, label='Riemann-Siegel Z-function, Z(t)', lw=0.8)
    ax.set_title("Riemann Zeta function - re(s)=1/2")
    ax.set_ylabel("Z(t)")
    ax.set_xlabel("t")

    #Include legend
    leg = ax.legend(shadow=True)
    #Edit font size of legend to make it fit into chart
    for t in leg.get_texts():
        t.set_fontsize('small')
    #Edit the line width in the legend
    for l in leg.get_lines():
        l.set_linewidth(2.0)
    #Plot the zeroes of zeta
    for i in xrange(1, 13):
        zero = zetazero(i)
        ax.plot(zero.imag, [0.0], "ro")
    
    #save plot and print that it was saved 
    ax.set_ylim(-7, 7)
    plt.savefig(image_name)
    print "Successfully plotted %s !" % image_name
    plt.close()


graph_zeta(0.5, "Z(t)_Plot.png")


# In[ ]:



