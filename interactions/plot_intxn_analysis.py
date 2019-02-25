#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 11:11:34 2018

@author: semccomas
FOOD FOR THOUGHT:
this will be for protein and for lipids, pretty much two scripts but it's easier to keep it all together
For lipid focus:
    The number of lipids in lipids_focus dfs will be # lipids in system - # lipids that were trapped to begin with(occ = 1)
    each column has nothing to do with each other as the lipids location isn't consistent across replicas, obvious but easy to 
        forget sometimes
        
        

"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print 'Choose 0 for protein plotting, you can choose later if you want to write a pdb or not'
print 'Choose 1 for lipid plotting'
prompt = raw_input('0 or 1?' )
lipid_focus = int(prompt)   #want to be consistent with intxn analysis where lipid focus = 1 = print lipid stuff not protein stuff 

if not lipid_focus:
    print 'Now choose lipid for analysis, POPA, POPC, POPE, or CDL2 (only relevant for protein plotting, disregarded otherwise)'
    prompt = raw_input('lipid? ')
    lipname = str(prompt).upper()

if not lipid_focus:
    df = pd.read_csv('arrays_csv/%s.max.avg.long.protres_index.TWOGONEDELETEME.csv' %lipname, index_col = 0)









def parse_lip(lipname):
    df = pd.read_csv('arrays_csv/%s.max.avg.long.lipres_index.TWOGONEDELETEME.csv' %lipname, index_col = 0)
    arr = np.append(df['max_1'].values, df['max_3'].values)
    arr_nozero = arr[np.nonzero(arr)]
    arr_nozero = np.log2(arr_nozero)
    #arr = arr / len(arr)
    arr = arr_nozero / len(arr)
    return arr

if lipid_focus:
    popa = parse_lip('POPA')
    pope = parse_lip('POPE')
    fig,ax = plt.subplots()
   # plt.hist([popa, pope], label=['pa', 'pe'])
    #plt.legend()
    a = ax.boxplot([popa, pope], labels =['pa', 'pe'], whis = 1)

'''    
labelgroup = ['POPC', 'POPE', 'POPS', 'POPA', 'POSM']
data = [popc, pope, pops, popa, posm]

data_sort = [popc_sort, pope_sort, pops_sort, popa_sort, posm_sort]
a = ax.boxplot(data_sort)#, whis = 3)   #whis = 3 will extend whiskers 
ax.set_xticklabels(labelgroup)
ax.get_xaxis().tick_bottom()
ax.get_yaxis().tick_left()
ax.set_ylabel('# ns Tmax')
plt.title(system + ' ' + i_o)
plt.savefig(trajdir + 'boxplot.png')

'''