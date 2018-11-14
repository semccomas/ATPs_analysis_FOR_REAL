#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 10:16:58 2018

@author: sarahmccomas
"""


import tables as tb
import numpy as np
import pandas as pd 
import MDAnalysis as md
import matplotlib.pyplot as plt


##########################################
### User defined variables  ##############
#########################################
#input_tab = sys.argv[1]
#input_tab = 'POPA.6'
#lipid_choice = input_tab.split('.')[0]  #if lipid name is always first this will work!
#chain_n = 'A'
lipid_choice = 'POPA'
chain = 'A'
rep = 1
##########################################
### get system info ready ##############
#########################################

#def get_names_and_table(rep, lipid_focus):
system_p = md.Universe('../protein_selection.pdb')
system_l = md.Universe('../lipid_selection.pdb')
protein = system_p.select_atoms('name BB and segid %s' %chain)
protein = protein[np.where(protein.atoms.occupancies == 1)]
lipid = system_l.select_atoms('resname %s' %lipid_choice)
lipid = lipid[np.where(lipid.atoms.occupancies == 1)]   #take only the values that are 1 (ie not within 1 of prot)

protein_names = []
for resname, resid in zip(list(protein.residues.resnames), list(protein.residues.resids)):
    protein_names.append(resname + '_' + str(resid))

lipid_names = []
for lipid_id in list(lipid.residues.resids):
    lipid_names.append(lipid_choice + '_' + str(lipid_id))


  
h5 = tb.open_file('%s.%s.%s.table.h5' %(lipid_choice, chain, rep))
intxn_array = [] 
for i in xrange(0, len(protein_names)):
    intxn_array.append(h5.root.intxn_tab.intxn[i])
intxn_array = np.array(intxn_array)



lip_across_all_res = np.array(intxn_array, dtype = int)
lip_across_all_res = lip_across_all_res.max(axis = 0)
lip_df = pd.DataFrame(data = lip_across_all_res)#, index= lipid_names)
lip_df =lip_df.T


lip1 = lip_across_all_res.T
time = np.arange(len(lip1))
for i in np.arange(np.shape(lip1)[1]):
    plot = lip1[:,i]
    plot = plot * i
    plot = plot.astype(float)
    plot[ plot==0 ] = np.nan
    plt.scatter(time, plot, marker = '|', color = 'blue')
    
    
plt.savefig('%s.timeplot.png' %lipid_choice, dpi = 900)

