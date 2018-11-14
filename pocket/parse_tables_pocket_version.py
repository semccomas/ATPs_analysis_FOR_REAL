#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 10:56:33 2018

@author: semccomas
"""

import numpy as np
import pandas as pd
import MDAnalysis as md
import matplotlib.pyplot as plt
import os 
import sys

prompt = raw_input('Cutoff distance 1.8 or 2.3? ' )
cutoff_dist = float(prompt)


def make_arr_df(xvg_f, lipname, repnum, use_system_lipnames):
    if use_system_lipnames:
        system = md.Universe('../input_files/files_rep%s/ATPs%s.system.pre_eq.pdb'%(repnum,repnum))
        lipnames = ['time']
        lip = system.select_atoms('resname %s' %lipname)
        for line in lip.residues.resids:
            lipnames.append(line)
   
    arr = np.loadtxt(xvg_f)

    
    arr_mask = np.where(arr<cutoff_dist, arr, 0)   #do initial masking
    if use_system_lipnames:
        arr_df = pd.DataFrame(arr_mask, columns = lipnames)
    else:
        arr_df = pd.DataFrame(arr_mask)
   
    ## nix the trapped guys and the guys who never show up
    arr_df.replace(0, np.nan, inplace=True)    #getting ready to drop all zeros, round 1
    arr_df = arr_df.dropna(axis = 1, how = 'all')
    trapped_guys = pd.isnull(arr_df).any(axis =0)    #find where there is NEVER a nan == always bound
    print 'trapped guys at %s removed' %(trapped_guys[trapped_guys!=True].index.tolist())  
    print
    arr_df = arr_df.loc[:,trapped_guys[trapped_guys].index]  #nix the trapped guys
    arr_df['time'] = np.arange(0,len(arr))    #nix time column, make index label
    arr_df = arr_df.set_index('time')       #set the name of time col
    
    
    
    
    ## masking round 2
    #arr_df = arr_df[arr_df < 1.4].dropna(axis = 1, how = 'all')
    

    return arr_df

lipname_list = ['POPA', 'POPC', 'POPE', 'CDL2']
lip_color = {'POPA':'blue', 'POPC':'green', 'POPE':'orange', 'CDL2':'red'}
fig = plt.figure()
use_system_lipnames = 0

print 'Calculate all lipids together(0) or write calculations per replica(1)?'
prompt = raw_input('0 or 1? ')
individual = int(prompt)


def do_all(num, lipname,individual):    
    total = []
    names_list = []   #to keep track of which array will belong to which replica/dimer
    ax = fig.add_subplot(2,2,num+1)
    for filename in os.listdir('./'):
        if filename.endswith(".xvg") and filename.startswith(lipname):
            print filename, ' running!'
            if individual:
                booldf = make_arr_df(filename, lipname, filename.split('_')[-1][0], use_system_lipnames)
                total.append(np.array(np.nan_to_num(booldf.values), dtype = bool))
                names_list.append(filename.strip('.xvg'))
            else:
                total.append(make_arr_df(filename, lipname, filename.split('_')[-1][0], use_system_lipnames))
                t = pd.concat(total, axis = 1)
                if not use_system_lipnames:
                    t.columns = np.arange(1,len(t.columns)+1)
                
                #this is just to make the plot prettier
                for col in t:
                    mask = t[col] > 0
                    t.loc[mask, col] = col
            
                ax.plot(t, color = lip_color[lipname])
                ax.set_title(lipname)
    
    if individual:
        return names_list, total
    
    if not individual:
        return names_list, t

#for num, lipname in enumerate(lipname_list):
#    do_all(num, lipname)   #num is the plot area
    
pc_names, popc_tab = do_all(1, 'POPC', individual)
pa_names, popa_tab = do_all(2, 'POPA', individual)
pe_names, pope_tab = do_all(3, 'POPE', individual)
cl_names, cdl2_tab = do_all(0, 'CDL2', individual)

plt.tight_layout()
plt.show()

def makenpz(lipname, names, tab):
    dct = {}
    for arr_name, arr in zip(names, tab):
        dct[arr_name] = arr
    np.savez('%s_cutoff_by_replicas.%s.npz' %(lipname, cutoff_dist), **dct)
    
if individual:
    makenpz('POPA', pa_names, popa_tab)
    makenpz('POPC', pc_names, popc_tab)
    makenpz('POPE', pe_names, pope_tab)
    makenpz('CDL2', cl_names, cdl2_tab)
    


#output for prob analysis
if not individual:
    popc_tab = popc_tab.fillna(0)
    popc_tab = np.array(popc_tab.values, dtype = bool)
    
    popa_tab = popa_tab.fillna(0)
    popa_tab = np.array(popa_tab.values, dtype = bool)
    
    pope_tab = pope_tab.fillna(0)
    pope_tab = np.array(pope_tab.values, dtype = bool)
    
    cdl2_tab = cdl2_tab.fillna(0)
    cdl2_tab = np.array(cdl2_tab.values, dtype = bool)

    np.savez('POPC_cutoff_combined.%s.npz' %cutoff_dist, popc_tab)
    np.savez('POPE_cutoff_combined.%s.npz' %cutoff_dist, pope_tab)
    np.savez('POPA_cutoff_combined.%s.npz' %cutoff_dist, popa_tab)
    np.savez('CDL2_cutoff_combined.%s.npz' %cutoff_dist, cdl2_tab)

