#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 16:53:40 2018

@author: semccomas
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

individual_reps = 0

if individual_reps:
    tot = pd.read_csv('all_replicas_cutoff1.8.csv')
    
    
    cdl_oi = []
    cdl_io = []
    cdl_ii = []
    
    pa_oi = []
    pa_io = []
    pa_ii = []
    
    pe_oi = []
    pe_io = []
    pe_ii = []
    
    pc_oi = []
    pc_io = []
    pc_ii = []
    
    for name in list(tot):
        if 'CDL_OI' in name:
            cdl_oi.append(tot.loc[:,name].values)
        if 'CDL_IO' in name:
            cdl_io.append(tot.loc[:,name].values)
        if 'CDL_II' in name:   
            cdl_ii.append(tot.loc[:,name].values)
    
    
        if 'PC_OI' in name:
            pc_oi.append(tot.loc[:,name].values)
        if 'PC_IO' in name:
            pc_io.append(tot.loc[:,name].values)
        if 'PC_II' in name:   
            pc_ii.append(tot.loc[:,name].values)
    
    
        if 'PE_OI' in name:
            pe_oi.append(tot.loc[:,name].values)
        if 'PE_IO' in name:
            pe_io.append(tot.loc[:,name].values)
        if 'PE_II' in name:   
            pe_ii.append(tot.loc[:,name].values)
       
    
        if 'PA_OI' in name:
            pa_oi.append(tot.loc[:,name].values)
        if 'PA_IO' in name:
            pa_io.append(tot.loc[:,name].values)
        if 'PA_II' in name:   
            pa_ii.append(tot.loc[:,name].values)


    cdl_oi = np.array(cdl_oi)
    cdl_io = np.array(cdl_io)
    cdl_ii = np.array(cdl_ii)
    
    pc_oi = np.array(pc_oi)
    pc_io = np.array(pc_io)
    pc_ii = np.array(pc_ii)
    
    pa_oi = np.array(pa_oi)
    pa_io = np.array(pa_io)
    pa_ii = np.array(pa_ii)
    
    pe_oi = np.array(pe_oi)
    pe_io = np.array(pe_io)
    pe_ii = np.array(pe_ii)
    
    
    
    Mcdl_ii = np.mean(cdl_ii, axis = 0)
    Scdl_ii = np.std(cdl_ii, axis = 0)
    Mcdl_io = np.mean(cdl_io, axis = 0)
    Scdl_io = np.std(cdl_io, axis = 0)    
    Mcdl_oi = np.mean(cdl_oi, axis = 0)
    Scdl_oi = np.std(cdl_oi, axis = 0)
    
    Mpc_ii = np.mean(pc_ii, axis = 0)
    Spc_ii = np.std(pc_ii, axis =0)
    Mpc_io = np.mean(pc_io, axis = 0)
    Spc_io = np.std(pc_io, axis = 0)
    Mpc_oi = np.mean(pc_oi, axis = 0)
    Spc_oi = np.std(pc_oi, axis = 0)
    
    Mpa_ii = np.mean(pa_ii, axis = 0)
    Spa_ii = np.std(pa_ii, axis =0)
    Mpa_io = np.mean(pa_io, axis = 0)
    Spa_io = np.std(pa_io, axis = 0)
    Mpa_oi = np.mean(pa_oi, axis = 0)
    Spa_oi = np.std(pa_oi, axis = 0)

    Mpe_ii = np.mean(pe_ii, axis = 0)
    Spe_ii = np.std(pe_ii, axis =0)
    Mpe_io = np.mean(pe_io, axis = 0)
    Spe_io = np.std(pe_io, axis = 0)   
    Mpe_oi = np.mean(pe_oi, axis = 0)
    Spe_oi = np.std(pe_oi, axis = 0)

    
    
    
    


else:
    Mcdl = pd.read_csv('probs_CDL2.cutoff_1.8.means.csv', index_col = 0)
    Scdl = pd.read_csv('probs_CDL2.cutoff_1.8.stds.csv', index_col = 0)
    Mcdl_ii = Mcdl.loc['I_I',:]
    Scdl_ii = Scdl.loc['I_I',:]
    Mcdl_io = Mcdl.loc['I_O',:]
    Scdl_io = Scdl.loc['I_O',:]
    Mcdl_oi = Mcdl.loc['O_I',:]
    Scdl_oi = Scdl.loc['O_I',:]
    
    Mpe = pd.read_csv('probs_POPE.cutoff_1.8.means.csv', index_col = 0)
    Spe = pd.read_csv('probs_POPE.cutoff_1.8.stds.csv', index_col = 0)    
    Mpe_ii = Mpe.loc['I_I',:]
    Spe_ii = Spe.loc['I_I',:]
    Mpe_io = Mpe.loc['I_O',:]
    Spe_io = Spe.loc['I_O',:]
    Mpe_oi = Mpe.loc['O_I',:]
    Spe_oi = Spe.loc['O_I',:]
    
    Mpc = pd.read_csv('probs_POPC.cutoff_1.8.means.csv', index_col = 0)
    Spc = pd.read_csv('probs_POPC.cutoff_1.8.stds.csv', index_col = 0)    
    Mpc_ii = Mpc.loc['I_I',:]
    Spc_ii = Spc.loc['I_I',:]
    Mpc_io = Mpc.loc['I_O',:]
    Spc_io = Spc.loc['I_O',:]
    Mpc_oi = Mpc.loc['O_I',:]
    Spc_oi = Spc.loc['O_I',:]
    
    Mpa = pd.read_csv('probs_POPA.cutoff_1.8.means.csv', index_col = 0)
    Spa = pd.read_csv('probs_POPA.cutoff_1.8.stds.csv', index_col = 0)    
    Mpa_ii = Mpa.loc['I_I',:]
    Spa_ii = Spa.loc['I_I',:]
    Mpa_io = Mpa.loc['I_O',:]
    Spa_io = Spa.loc['I_O',:]
    Mpa_oi = Mpa.loc['O_I',:]
    Spa_oi = Spa.loc['O_I',:]
    



bot = 0
top = 760
f, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True)

ax1.plot(np.arange(bot, top*5, 5), Mcdl_ii[bot:top], label = 'cdl ii', color = 'blue')
ax1.fill_between(np.arange(bot, top*5, 5), (Mcdl_ii + Scdl_ii)[bot:top], (Mcdl_ii - Scdl_ii)[bot:top], alpha = 0.5, color ='blue')

ax1.plot(np.arange(bot, top*5, 5), Mpe_ii[bot:top], label = 'pe ii', color = 'orange')
ax1.fill_between(np.arange(bot, top*5, 5), (Mpe_ii + Spe_ii)[bot:top], (Mpe_ii - Spe_ii)[bot:top], alpha = 0.5, color ='orange')

ax1.plot(np.arange(bot, top*5, 5), Mpc_ii[bot:top], label = 'pc ii', color = 'green')
ax1.fill_between(np.arange(bot, top*5, 5), (Mpc_ii + Spc_ii)[bot:top], (Mpc_ii - Spc_ii)[bot:top], alpha = 0.5, color ='green')

ax1.plot(np.arange(bot, top*5, 5), Mpa_ii[bot:top], label = 'pa ii', color = 'red')
ax1.fill_between(np.arange(bot, top*5, 5), (Mpa_ii + Spa_ii)[bot:top], (Mpa_ii - Spa_ii)[bot:top], alpha = 0.5, color ='red')

ax1.set_title('I to I')
ax1.set_ylim(0, 0.1)



ax2.plot(np.arange(bot, top*5, 5), Mcdl_oi[bot:top], label = 'cdl oi', color = 'blue')
ax2.fill_between(np.arange(bot, top*5, 5), (Mcdl_oi + Scdl_oi)[bot:top], (Mcdl_oi - Scdl_oi)[bot:top], alpha = 0.5, color ='blue')

ax2.plot(np.arange(bot, top*5, 5), Mpe_oi[bot:top], label = 'pe oi', color = 'orange')
ax2.fill_between(np.arange(bot, top*5, 5), (Mpe_oi + Spe_oi)[bot:top], (Mpe_oi - Spe_oi)[bot:top], alpha = 0.5, color ='orange')

ax2.plot(np.arange(bot, top*5, 5), Mpc_oi[bot:top], label = 'pc oi', color = 'green')
ax2.fill_between(np.arange(bot, top*5, 5), (Mpc_oi + Spc_oi)[bot:top], (Mpc_oi - Spc_oi)[bot:top], alpha = 0.5, color ='green')

ax2.plot(np.arange(bot, top*5, 5), Mpa_oi[bot:top], label = 'pa oi', color = 'red')
ax2.fill_between(np.arange(bot, top*5, 5), (Mpa_oi + Spa_oi)[bot:top], (Mpa_oi - Spa_oi)[bot:top], alpha = 0.5, color ='red')

ax2.set_title('O to I')
ax2.set_ylabel('Probability')
ax2.set_ylim(0, 0.1)


ax3.plot(np.arange(bot, top*5, 5), Mcdl_io[bot:top], label = 'cdl io', color = 'blue')
ax3.fill_between(np.arange(bot, top*5, 5), (Mcdl_io + Scdl_io)[bot:top], (Mcdl_io - Scdl_io)[bot:top], alpha = 0.5, color ='blue')

ax3.plot(np.arange(bot, top*5, 5), Mpe_io[bot:top], label = 'pe io', color = 'orange')
ax3.fill_between(np.arange(bot, top*5, 5), (Mpe_io + Spe_io)[bot:top], (Mpe_io - Spe_io)[bot:top], alpha = 0.5, color ='orange')

ax3.plot(np.arange(bot, top*5, 5), Mpc_io[bot:top], label = 'pc io', color = 'green')
ax3.fill_between(np.arange(bot, top*5, 5), (Mpc_io + Spc_io)[bot:top], (Mpc_io - Spc_io)[bot:top], alpha = 0.5, color ='green')

ax3.plot(np.arange(bot, top*5, 5), Mpa_io[bot:top], label = 'pa io', color = 'red')
ax3.fill_between(np.arange(bot, top*5, 5), (Mpa_io + Spa_io)[bot:top], (Mpa_io - Spa_io)[bot:top], alpha = 0.5, color ='red')

ax3.set_title('I to O')
ax3.set_ylim(0, 0.1)

ratio = 0.1
for ax in [ax1, ax2, ax3]:
    xmin, xmax = ax.get_xlim()
    ymin, ymax = ax.get_ylim()
    ax.set_aspect(abs((xmax-xmin)/(ymax-ymin))*ratio, adjustable='box-forced')

plt.xlim(bot,top*5 -1)
plt.xlabel('Tau size in num. ns')
plt.tight_layout()
lgd = plt.legend(loc='upper right', bbox_to_anchor=(-0.1, 0.5))
plt.show()




