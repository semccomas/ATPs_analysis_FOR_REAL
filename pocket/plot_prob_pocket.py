#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 14:55:49 2018

@author: sarahmccomas
"""
import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd 

### this is the same as prob_pocket but you can tinker with the plot and not wait for the code to run

bot = 0
top = 760

a = pd.read_csv('probs_CDL2.cutoff_1.8.csv')


'''
fig = plt.figure()
f, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True)

ax1.plot(cdl_ii[bot:top], label = 'cdl ii')
ax1.plot(pe_ii[bot:top], label = 'pe ii')
ax1.plot(pc_ii[bot:top], label = 'pc ii')
ax1.plot(pa_ii[bot:top], label = 'pa ii')
ax1.set_title('I to I')


ax2.plot(cdl_oi[bot:top], label = 'cdl oi')
ax2.plot(pe_oi[bot:top], label = 'pe oi')
ax2.plot(pc_oi[bot:top], label = 'pc oi')
ax2.plot(pa_oi[bot:top], label = 'pa oi')
ax2.set_title('O to I')


ax3.plot(cdl_io[bot:top], label = 'cdl io')
ax3.plot(pe_io[bot:top], label = 'pe io')
ax3.plot(pc_io[bot:top], label = 'pc io')
ax3.plot(pa_io[bot:top], label = 'pa io')
ax3.set_title('I to O')

ratio = 0.1
for ax in [ax1, ax2, ax3]:
    xmin, xmax = ax.get_xlim()
    ymin, ymax = ax.get_ylim()
    print((xmax-xmin)/(ymax-ymin))
    ax.set_aspect(abs((xmax-xmin)/(ymax-ymin))*ratio, adjustable='box-forced')

plt.xlim(bot,top-1)

plt.tight_layout()
plt.legend(loc='upper right', bbox_to_anchor=(-0.1, 0.5)
)
#plt.show()
plt.savefig('probs_cutoff%s.png' %cutoff, dpi = 900)

'''