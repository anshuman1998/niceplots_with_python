%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np

import matplotlib as mpl
mpl.rcParams['xtick.major.size'] = 30
mpl.rcParams['xtick.major.width'] = 5
mpl.rcParams['xtick.minor.size'] = 20
mpl.rcParams['xtick.minor.width'] = 5
mpl.rcParams['ytick.major.size'] = 30
mpl.rcParams['ytick.major.width'] = 5
mpl.rcParams['ytick.minor.size'] = 20
mpl.rcParams['ytick.minor.width'] = 5
mpl.rcParams['xtick.direction'] = 'in'
mpl.rcParams['ytick.direction'] = 'in'

plt.rcParams.update({'font.size':80})
plt.rc('font',family='serif') #can comment out to keep the default sans serif font
plt.rc('xtick',labelsize=70)
plt.rc('ytick',labelsize=70)

fig = plt.figure(figsize=(30,18))
ax = fig.add_subplot(1,1,1)

ax.tick_params(right=True,top=True,which='both') #'both' makes minor ticks on both right #and top to appear apart from left and bottom

from matplotlib.ticker import FuncFormatter
formatter = FuncFormatter(lambda y, _: '{:.16g}'.format(y)) #Shows in decimals even for log scales
formatter_x = FuncFormatter(lambda y, _: '{:.1f}'.format(y)) #Shows up to 1 significant digit

'''
This is where the magic happens
'''

ax.set_yscale('log')
ax.set_xscale('log')
ax.set_xlim(left=,right=)
ax.set_ylim(bottom=,top=)
ax.yaxis.set_major_formatter(formatter)
ax.xaxis.set_major_formatter(formatter_x)
ax.set_ylabel(r"$Latex style titles$")
ax.set_xlabel(r"$\Phi$")
ax.legend(loc='upper left',ncol=1,fontsize=55) #control no. of columns and 
                                               #font size for legend
plt.savefig('xyz.pdf', dpi=200, format='pdf',bbox_inches="tight")
plt.show()
