#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 18:33:16 2018

@author: semccomas
"""

import tables as tb
import numpy as np
import pandas as pd 
import MDAnalysis as md
from sklearn.preprocessing import MinMaxScaler
import sys
import matplotlib.pyplot as plt

##########################################sss
### User defined variables  ##############
#########################################
'''
HELLO!!! You need to change input file names before running this script
You also need to change chain naming
You also need to consider how to represent the dimer, maybe just do one monomer?

system_p and system_l in get_names
table in get_names
pdb file in ending

'''

lipid_choice = sys.argv[1]
long_time = 60   #300ns = 60 frames

##########################################
### get system info ready ##############
#########################################


print 'This script is meant to be run on one lipid type at a time, across all replicates'
print 'Will save a pdb file coloring score per residue'
print 'Will output a numpy array in lipid_arrays that is for per lipid statistics'
print 'Running for lipid name %s' %lipid_choice
print 'Long time = %s ns' %(str(long_time * 5))
print 

def get_names_and_table(rep, chain_n, lipid_focus):
    system_p = md.Universe('../input_files/files_rep%s/protein_selection.pdb' %rep)
    system_l = md.Universe('../input_files/files_rep%s/lipid_selection.pdb' %rep)
    protein = system_p.select_atoms('name BB and segid %s' %chain_n)
    protein = protein[np.where(protein.atoms.occupancies == 1)]
    lipid = system_l.select_atoms('resname %s' %lipid_choice)
    lipid = lipid[np.where(lipid.atoms.occupancies == 1)]   #take only the values that are 1 (ie not within 1 of prot)
    
    protein_names = []
    for resname, atomid in zip(list(protein.residues.resnames), list(protein.ids)):
        protein_names.append(str(atomid) + '_' + resname)
    
    lipid_names = []
    for lipid_id in list(lipid.residues.resids):
        lipid_names.append(str(lipid_id) + '_' + lipid_choice)
    
    
      
    h5 = tb.open_file('tables/%s.%s.%s.table.h5' %(lipid_choice, chain_n, rep))
    intxn_array = [] 
    for i in xrange(0, len(protein_names)):
        intxn_array.append(h5.root.intxn_tab.intxn[i])
    intxn_array = np.array(intxn_array)
       
    


    '''
    count continuous events - you input an array that is now reading as one chunk
    per residue, and in each chunk a row is a lipid, and each column is a 5ns frame
    (at least for ATP synthase)
    
    you then read each chunk and initialize a list for each chunk(residue)
    then you read each chunk line by line (lipid by lipid) to see across each row
    the continuous counts in the line. All the counts in the row will correspond to 
    how many continuous 1's you had (meaning the lipid is there in that trajectory frame)
    
    then you append each of these values to the residue chunk, and when the whole
    chunk is finished, you put into total_counts
    
    
    Therefore, in total_counts you have a 2d array, each row is per residue
    Each value in the array corresponds to that residue of the row and that lipid of the column
    (total_counts[0] might be like ([], [], [1 2 1], [1 8 1], []), meaning that for resid 0, 
    there were 0 hits across all frames for lipid[0] or lipid[1], but lipid[2] and 3 had
    some longer events, as well as short events (1 frame))
    
    RAW_total_counts is just a way to keep track of the counts as we do various calculations to them
    (finding the max, avg, # long... just to see where it all comes from, we WONT use this in the end!!)
    OTHER ARRAYS:
        max_len = take maximum durating of binding in resid vs lip across all time frames
        num_long_binding = count how many times a longer binding event occurs (defined at top with lipid name) 
        
    *1 - np.extract(continuous_counts > long_time, continuous_counts) takes the values in the array that 
    are true to this statements, and sees how many there are (so if cont_c = [10, 10, 1, 3] and long == 2,
    then you get back [10, 10, 3] and take the length of this!)
    
    '''
    RAW_total_counts = []
    max_len = []
    num_long_binding = []
    avg_binding = []
    
    for resid in intxn_array:
        per_resid_intxns = []
        per_resid_max_len = []
        per_resid_long_bind = []
        per_resid_avg_bind = []
        for lipname in resid:
            continuous_counts = np.diff(np.where(np.concatenate(([lipname[0]], lipname[:-1] != lipname[1:], [True])))[0])[::2]
            per_resid_intxns.append(str(continuous_counts))
            if continuous_counts.size > 0:
                per_resid_max_len.append(np.max(continuous_counts))
                per_resid_long_bind.append(len(np.extract(continuous_counts > long_time, continuous_counts))) ## see *1 for exp
                per_resid_avg_bind.append(np.mean(continuous_counts))
            else:
                per_resid_max_len.append(0)
                per_resid_long_bind.append(0)
                per_resid_avg_bind.append(0)
    
        per_resid_intxns = np.array(per_resid_intxns)
        per_resid_max_len = np.array(per_resid_max_len)
        per_resid_long_bind = np.array(per_resid_long_bind)
        per_resid_avg_bind = np.array(per_resid_avg_bind)
    
        RAW_total_counts.append(per_resid_intxns)
        max_len.append(per_resid_max_len)
        num_long_binding.append(per_resid_long_bind)
        avg_binding.append(per_resid_avg_bind)
    

#### here we transpose because I actually want columns named after resids, the indices I care less about    
    if lipid_focus:
        RAW_total_counts= np.array(RAW_total_counts)
        max_len = np.array(max_len)  #same shape, # resids by # lipids, containing max length of continuous_count across all frames
        num_long_binding = np.array(num_long_binding)
        avg_binding = np.array(avg_binding)
        column_name = lipid_names
        index_name = protein_names

    else:    
        RAW_total_counts= np.transpose(np.array(RAW_total_counts))
        max_len = np.transpose(np.array(max_len))  #same shape, # resids by # lipids, containing max length of continuous_count across all frames
        num_long_binding = np.array(num_long_binding)
        num_long_binding = np.transpose(num_long_binding)
        avg_binding = np.transpose(np.array(avg_binding))
        column_name = protein_names
        index_name = lipid_names
    
    RAW_total_counts = pd.DataFrame(data= RAW_total_counts, columns = column_name, index = index_name)
    max_len = pd.DataFrame(data= max_len, columns = column_name, index = index_name)
    num_long_binding = pd.DataFrame(data= num_long_binding, columns = column_name, index = index_name)
    avg_binding = pd.DataFrame(data= avg_binding, columns = column_name, index = index_name)
    avg_binding.replace(0, np.nan, inplace = True)
    
    return RAW_total_counts, max_len, num_long_binding, avg_binding



#############################################
###### parse tables and score  ############
#############################################

lipid_focus = int(raw_input('Protein(0) or lipid(1) plotting? '))
print 'making pdb colors...'
raw1a, max1a, long1a, avg1a = get_names_and_table(1, 'A', lipid_focus)
print '1A done!'
raw1b, max1b, long1b, avg1b = get_names_and_table(1, 'B', lipid_focus)
print '1B done!'
#raw2a, max2a, long2a, avg2a = get_names_and_table(2, 'A', lipid_focus)
print '2A done ignored!'
#raw2b, max2b, long2b, avg2b = get_names_and_table(2, 'B', lipid_focus)
print '2B done ignored!'
raw3a, max3a, long3a, avg3a = get_names_and_table(3, 'A', lipid_focus)
print '3A done!'
raw3b, max3b, long3b, avg3b = get_names_and_table(3, 'B', lipid_focus)
print '3B done!'


#raw3, max3, long3, avg3 = get_names_and_table(9, lipid_focus)
'''
def combine_dataframes(d1a, d1b, d2a, d2b, d3a, d3b, maxv, colname):
    if maxv:
        d1 = pd.concat([d1a.max(), d1b.max()]).groupby(level=0).max()  #this is more for the lipid arrays but it won't really affect the protein so much, take the max when adding the two arrays
        d2 = pd.concat([d2a.max(), d2b.max()]).groupby(level=0).max()
        d3 = pd.concat([d3a.max(), d3b.max()]).groupby(level=0).max()
    else:
        d1 = pd.concat([d1a.mean(), d1b.mean()]).groupby(level=0).mean()
        d2 = pd.concat([d2a.mean(), d2b.mean()]).groupby(level=0).mean()
        d3 = pd.concat([d3a.mean(), d3b.mean()]).groupby(level=0).mean()
        
    d_tot = pd.concat([d1,d2,d3], axis = 1)
    d_tot = d_tot.fillna(value = 0)
    d_tot = d_tot.rename(index=str, columns={0:'%s_1' %colname, 1:'%s_2' %colname, 2:'%s_3' %colname})
    d_tot['mean_%s' %colname] = d_tot[['%s_1'%colname, '%s_2'%colname, '%s_3'%colname]].mean(axis = 1)
    d_tot['std_%s' %colname] = d_tot[['%s_1'%colname, '%s_2'%colname, '%s_3'%colname]].std(axis = 1)
    d_tot['max_%s' %colname] = d_tot[['%s_1'%colname, '%s_2'%colname, '%s_3'%colname]].max(axis = 1)
    return d_tot

max_tot = combine_dataframes(max1a, max1b, max2a, max2b, max3a, max3b, 1, 'max')
avg_tot = combine_dataframes(avg1a, avg1b, avg2a, avg2b, avg3a, avg3b, 0, 'avg')
long_tot = combine_dataframes(long1a, long1b, long2a, long2b, long3a, long3b, 1, 'long')
df = pd.concat([max_tot, avg_tot, long_tot], axis = 1)
 
if not lipid_focus:    
    df.to_csv('arrays_csv/%s.max.avg.long.protres_index.csv' %lipid_choice)
if lipid_focus:
    df.to_csv('arrays_csv/%s.max.avg.long.lipres_index.csv' %lipid_choice)
 '''   
    
    
def combine_dataframesIGNTWO(d1a, d1b, d3a, d3b, maxv, colname):
    if maxv:
        d1 = pd.concat([d1a.max(), d1b.max()]).groupby(level=0).max()  #this is more for the lipid arrays but it won't really affect the protein so much, take the max when adding the two arrays
        #d2 = pd.concat([d2a.max(), d2b.max()]).groupby(level=0).max()
        d3 = pd.concat([d3a.max(), d3b.max()]).groupby(level=0).max()
    else:
        d1 = pd.concat([d1a.mean(), d1b.mean()]).groupby(level=0).mean()
       # d2 = pd.concat([d2a.mean(), d2b.mean()]).groupby(level=0).mean()
        d3 = pd.concat([d3a.mean(), d3b.mean()]).groupby(level=0).mean()
        
    d_tot = pd.concat([d1,d3], axis = 1)
    d_tot = d_tot.fillna(value = 0)
    d_tot = d_tot.rename(index=str, columns={0:'%s_1' %colname, 1:'%s_3' %colname})
    d_tot['mean_%s' %colname] = d_tot[['%s_1'%colname, '%s_3'%colname]].mean(axis = 1)
    d_tot['std_%s' %colname] = d_tot[['%s_1'%colname, '%s_3'%colname]].std(axis = 1)
    d_tot['max_%s' %colname] = d_tot[['%s_1'%colname, '%s_3'%colname]].max(axis = 1)
    return d_tot   
    
    
max_tot = combine_dataframesIGNTWO(max1a, max1b, max3a, max3b, 1, 'max')
avg_tot = combine_dataframesIGNTWO(avg1a, avg1b, avg3a, avg3b, 0, 'avg')
long_tot = combine_dataframesIGNTWO(long1a, long1b, long3a, long3b, 1, 'long')
df = pd.concat([max_tot, avg_tot, long_tot], axis = 1)
 
if not lipid_focus:    
    df.to_csv('arrays_csv/%s.max.avg.long.protres_index.TWOGONEDELETEME.csv' %lipid_choice)
if lipid_focus:
    df.to_csv('arrays_csv/%s.max.avg.long.lipres_index.TWOGONEDELETEME.csv' %lipid_choice)
      
    
    
    
    
    
    
    
    
    
    '''
    max_tot = pd.concat([max1a, max1b, max2a, max2b, max3a, max3b])
    raw_vals = max_tot
    max_tot = max_tot.max()
    long_tot = pd.concat([long1a, long1b, long2a, long2b, long3a, long3b])
    long_tot = long_tot.max()
    avg_tot = pd.concat([avg1a.mean(), avg1b.mean(), avg2a.mean(), avg2b.mean(), avg3a.mean(), avg3b.mean()], axis = 1)
    avg_tot = avg_tot.mean(axis = 1)
    
    df = pd.concat([avg_tot, long_tot, max_tot], axis = 1)
    df = df.rename(index=str, columns={0: "avg_tot", 1: "long_tot", 2:"max_tot"})
    #df.replace(0, np.nan, inplace = True)
    df['score'] = 0
    df_b = df
    #############################################
    ###### plotting and looking at arrays #######
    #############################################
   
    We open a pdb, take all residues for protein from it
    sort the df by them, the ones that aren't in the df already (ex those not included in membrane)
    will get a NaN but everyone should have some attribute attached to them
    
    Then, write out the score per residue, using this function above 
    Using funct, we can also do it for the atomistic model if we want
    
    
    template_prot = md.Universe('../AN_replica_1/ATPs1.0ns.chainref.pdb') #choosing whatever pdb
    prot = template_prot.select_atoms('name BB')
    prot_for_writing = template_prot.select_atoms('name BB SC1 SC2 SC3 SC4')
    protein_names = []
    for resname, atomid in zip(list(prot.residues.resnames), list(prot.ids)):
        protein_names.append(str(atomid) + '_' + resname)
    df = df.reindex(protein_names)  
    df = df.fillna(value = 0)
    scal = MinMaxScaler()
    df['score_max'] = scal.fit_transform(df['max_tot'])
    df['score_long'] = scal.fit_transform(df['long_tot'])
    df['score_avg'] = scal.fit_transform(df['avg_tot']) 
    df['score'] = df['score_max'] + df['score_long'] + df['score_avg']
    score = np.array(df["score"].tolist()) * 100
   
    
    score_per_resid = []
    c = -1
    for atom_g in prot_for_writing:
        if atom_g.name == 'BB':
            c = c + 1 
        score_per_resid.append(score[c])
        
        
    prot_for_writing.write("%s_prot_score.pdb" %lipid_choice)  #save protein only pdb
    u = md.Universe('%s_prot_score.pdb' %lipid_choice)   #open again to fix beta column
    u.atoms.tempfactors = score_per_resid
    u.atoms.write('%s_prot_score.pdb' %lipid_choice)
    
    df.hist(bins=30)
    plt.savefig('images_graphs/histogram.%s.png' %lipid_choice)
    df.to_csv('arrays_csv/%s.df.byprotres.csv' %lipid_choice)

'''








##########################################
### plot lipid stuff ##############
#########################################

"""
My idea for this is that we will be running the protein focused calcs and have to change
the lipid type each time, so this will save for each lipid type. It should
be combining all relevant lipid types into one array (=> 3 arrays per lipid type)
and then we will read this into lipid_boxplots.py


lipid_focus = 1
print 'saving per lipid interactions...'
raw1, max1, long1, avg1 = get_names_and_table(4, lipid_focus)
raw2, max2, long2, avg2 = get_names_and_table(6, lipid_focus)
raw3, max3, long3, avg3 = get_names_and_table(9, lipid_focus)

if lipid_focus:
    max_lips = []
    max_lips.append(list(max1.max()))
    max_lips.append(list(max2.max()))
    max_lips.append(list(max3.max()))
    max_lips = np.concatenate(max_lips).ravel()
    np.save('lipid_arrays/%s.max_per_lipid.npy' %lipid_choice, max_lips)

    long_lips = []
    long_lips.append(list(long1.max()))
    long_lips.append(list(long2.max()))
    long_lips.append(list(long3.max()))
    long_lips = np.concatenate(long_lips).ravel()
    np.save('lipid_arrays/%s.long_intxn_per_lipid.npy' %lipid_choice, long_lips)
    
    avg_lips = []
    avg_lips.append(list(avg1.mean()))
    avg_lips.append(list(avg2.mean()))
    avg_lips.append(list(avg3.mean()))
    avg_lips = np.concatenate(avg_lips).ravel()
    np.save('lipid_arrays/%s.avg_intxn_per_lipid.npy' %lipid_choice, avg_lips)
    
    
"""
    
    
    
    
    
    