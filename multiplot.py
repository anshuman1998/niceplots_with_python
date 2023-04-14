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
plt.rc('font',family='sans serif') #can comment out to keep the default sans serif font
plt.rc('xtick',labelsize=60)
plt.rc('ytick',labelsize=60)

from matplotlib.ticker import FuncFormatter
formatter = FuncFormatter(lambda y, _: '{:.1f}'.format(y)) #Shows in decimals even for log scales

from matplotlib import gridspec
from matplotlib.offsetbox import AnchoredText
fig = plt.figure(figsize=(30,36))
gs = gridspec.GridSpec(ncols=1, nrows=3, figure=fig,height_ratios=[1,1,1])
ax0 = plt.subplot(gs[0])
ax1 = plt.subplot(gs[1],sharex=ax0)
ax2 = plt.subplot(gs[2],sharex=ax0,sharey=ax1)
ax0.tick_params(right=True,top=True,which='both')
ax1.tick_params(right=True,top=True,which='both')
ax2.tick_params(right=True,top=True,which='both')
ax.set_facecolor('white') #background colour

#An example set of commmands for 3 plots stacked in a column, with a shared x and y axis label.

ax0.plot(x,y,lw=10,c='#228833',ls="--")
ax0.set(xlabel=None)
#ax0.set_yscale("log")
ax0.legend(loc="upper right",fontsize=43,framealpha=1.0,ncol=1)
plt.setp(ax0.get_xticklabels(), visible=False)
#ax0.set_ylim(top=,bottom=)


ax1.plot(x,y,lw=10,c='#228833',ls="--")
ax1.set(xlabel=None,ylabel=None)
plt.setp(ax1.get_xticklabels(), visible=False)
ax1.legend(loc="upper right",fontsize=43,framealpha=1.0,ncol=2)
#ax1.set_ylim(top=,bottom=)
#ax1.set_yscale("log")


ax2.plot(x,y,lw=10,c='#228833')
ax2.set(xlabel=r"$Latex style$",ylabel=None)
#ax2.set_ylim(top=,bottom=)
#ax2.set_yscale("log")
ax2.minorticks_off()

plt.subplots_adjust(hspace=.0) #To remove spacing between the 3 plots


#And the y-axis label:
fig.text(0.01, 0.38, r"label", va='center', rotation='vertical')

#plt.savefig('figs/multiplot.png',format='png',dpi=400,bbox_inches='tight')
plt.savefig('figs/multiplot.pdf',format='pdf',dpi=400,bbox_inches='tight')
