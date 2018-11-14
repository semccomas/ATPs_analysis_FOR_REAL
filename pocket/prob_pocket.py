#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 13:59:26 2018

@author: semccomas
"""

import numpy as np
import matplotlib.pyplot as plt
import sys
import pandas as pd 

prompt = raw_input('Cutoff distance 1.8 or 2.3? ' )
cutoff = float(prompt)


prompt = raw_input('Run for all lipids(0) or individual replicas? (1) ' )
#run_calcs = 1   #if you just want to plot, change this to 0, if you need to run stuff, make 1
indiv_replicas = int(prompt)

if indiv_replicas:
    outname = 'by_replicas'
else:
    outname = 'combined'

indiv_names = ['_A_1', '_B_1', '_A_2', '_B_2', '_A_3', '_B_3']


def make_whole(dic_arr):   #this just combines all the saved arrays, same output format as before (# frames, #lipids)
    arr = []
    for line in dic_arr.iteritems():
        arr.append(line[1])
    arr = np.hstack(arr)
    arr = arr.T
    return arr

if indiv_replicas:
    pc_whole = np.load('POPC_cutoff_by_replicas.%s.npz' %cutoff)
    pe_whole = np.load('POPE_cutoff_by_replicas.%s.npz' %cutoff)
    pa_whole = np.load('POPA_cutoff_by_replicas.%s.npz' %cutoff)
    cl_whole = np.load('CDL2_cutoff_by_replicas.%s.npz' %cutoff)

if not indiv_replicas:
    pc = make_whole(np.load('POPC_cutoff_combined.%s.npz' %cutoff))
    pe = make_whole(np.load('POPE_cutoff_combined.%s.npz' %cutoff))
    pa = make_whole(np.load('POPA_cutoff_combined.%s.npz' %cutoff))
    cl = make_whole(np.load('CDL2_cutoff_combined.%s.npz' %cutoff))

def calc_probs(lipid_array, lipname):
    tot_p_oo = []
    tot_p_oi = []
    tot_p_io = []
    tot_p_ii = []
    
    std_p_oo = []
    std_p_oi = []
    std_p_io = []
    std_p_ii = []
    for tau in xrange(801):
        #print tau
        sys.stdout.write('\r')
        # the exact output you're looking for:
        sys.stdout.write('tau ' + str(tau) + '/801 done')
        sys.stdout.flush()
        p_oo = []
        p_oi = []
        p_io = []
        p_ii = []
        for resid in lipid_array:
            oo_l = []
            oi_l = []
            io_l = []
            ii_l = []
            for n, line in enumerate(resid):
                try:
                    if line:                  #this then IN
                        if resid[n] == resid[n+tau]:  #meaning II
                            oo_l.append(0)
                            oi_l.append(0)
                            io_l.append(0)
                            ii_l.append(1)
                        else:                 #meaning IO
                            oo_l.append(0)
                            oi_l.append(0)
                            io_l.append(1)
                            ii_l.append(0)
                    else:                     #this is then OUT
                        if resid[n] == resid[n+tau]:  #meaning OO 
                            oo_l.append(1)
                            oi_l.append(0)
                            io_l.append(0)
                            ii_l.append(0)
                        else:                 #meaning OI
                            oo_l.append(0)
                            oi_l.append(1)
                            io_l.append(0)
                            ii_l.append(0)                       
                except IndexError:
                    pass
        
            p_oo.append(np.sum(oo_l, dtype = float)/len(oo_l))
            p_oi.append(np.sum(oi_l, dtype = float)/len(oi_l))
            p_io.append(np.sum(io_l, dtype = float)/len(io_l))
            p_ii.append(np.sum(ii_l, dtype = float)/len(ii_l))
        
        tot_p_oo.append(np.mean(p_oo))
        tot_p_oi.append(np.mean(p_oi))
        tot_p_io.append(np.mean(p_io))
        tot_p_ii.append(np.mean(p_ii))
        
        std_p_oo.append(np.std(p_oo))
        std_p_oi.append(np.std(p_oi))
        std_p_io.append(np.std(p_io))
        std_p_ii.append(np.std(p_ii))
        
    Moutdf = pd.DataFrame(data=np.vstack((tot_p_oo, tot_p_oi, tot_p_io, tot_p_ii)), index=('O_O','O_I', 'I_O', 'I_I'))
    Soutdf = pd.DataFrame(data=np.vstack((std_p_oo, std_p_oi, std_p_io, std_p_ii)), index=('O_O','O_I', 'I_O', 'I_I'))

    if not indiv_replicas:
        Moutdf.to_csv('probs_%s.cutoff_combined.%s.means.csv' %(lipname, cutoff))
        Soutdf.to_csv('probs_%s.cutoff_combined.%s.stds.csv' %(lipname, cutoff))

    return tot_p_oo, tot_p_oi, tot_p_io, tot_p_ii

'''
def get_pandas_csv(lipname):
    df = pd.read_csv('probs_%s.cutoff_%s.csv' %(lipname, cutoff), index_col=0)
    oo = df.loc['O_O', :].tolist()
    oi = df.loc['O_I', :].tolist()
    io = df.loc['I_O', :].tolist()
    ii = df.loc['I_I', :].tolist()
    return oo, oi, io, ii


def plot_probs(outname):
    #fig = plt.figure()
    bot = 0
    top = 760
    f, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True)
    
    ax1.plot(np.arange(bot, top*5, 5), cdl_ii[bot:top], label = 'cdl ii')
    ax1.plot(np.arange(bot, top*5, 5), pe_ii[bot:top], label = 'pe ii')
    ax1.plot(np.arange(bot, top*5, 5), pc_ii[bot:top], label = 'pc ii')
    ax1.plot(np.arange(bot, top*5, 5), pa_ii[bot:top], label = 'pa ii')
    ax1.set_title('I to I')
    ax1.set_ylim(0, 0.1)
    
    
    ax2.plot(np.arange(bot, top*5, 5), cdl_oi[bot:top], label = 'cdl oi')
    ax2.plot(np.arange(bot, top*5, 5), pe_oi[bot:top], label = 'pe oi')
    ax2.plot(np.arange(bot, top*5, 5), pc_oi[bot:top], label = 'pc oi')
    ax2.plot(np.arange(bot, top*5, 5), pa_oi[bot:top], label = 'pa oi')
    ax2.set_title('O to I')
    ax2.set_ylabel('Probability')
    ax2.set_ylim(0, 0.1)
    
    
    ax3.plot(np.arange(bot, top*5, 5), cdl_io[bot:top], label = 'cdl io')
    ax3.plot(np.arange(bot, top*5, 5), pe_io[bot:top], label = 'pe io')
    ax3.plot(np.arange(bot, top*5, 5), pc_io[bot:top], label = 'pc io')
    ax3.plot(np.arange(bot, top*5, 5), pa_io[bot:top], label = 'pa io')
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
    #plt.show()
    plt.savefig(outname,bbox_extra_artists=(lgd,), bbox_inches='tight', dpi = 900)
'''

if not indiv_replicas:
    cdl_oo, cdl_oi, cdl_io, cdl_ii = calc_probs(cl, 'CDL2')
    print 'cdl done!'
    pa_oo, pa_oi, pa_io, pa_ii = calc_probs(pa, 'POPA')
    print 'pa done!'
    pe_oo, pe_oi, pe_io, pe_ii = calc_probs(pe, 'POPE')
    print 'pe done!'
    pc_oo, pc_oi, pc_io, pc_ii = calc_probs(pc, 'POPC')
    print 'pc done!'
    #plot_probs('probs_cutoff%s.png' %cutoff)
    
    '''
    if not run_calcs:
        cdl_oo, cdl_oi, cdl_io, cdl_ii = get_pandas_csv('CDL2')
        pa_oo, pa_oi, pa_io, pa_ii = get_pandas_csv('POPA')
        pe_oo, pe_oi, pe_io, pe_ii = get_pandas_csv('POPE')
        pc_oo, pc_oi, pc_io, pc_ii = get_pandas_csv('POPC')
        plot_probs('probs_cutoff%s.png' %cutoff)
   '''

if indiv_replicas:
    outdf = pd.DataFrame(np.zeros(801), columns = ['filler'])
    for val in indiv_names:
        for arr in pc_whole.iteritems():
            if val in arr[0]:
                pc = arr[1].T
        for arr in pa_whole.iteritems():
            if val in arr[0]:
                pa = arr[1].T
        for arr in pe_whole.iteritems():
            if val in arr[0]:
                pe = arr[1].T
        for arr in cl_whole.iteritems():
            if val in arr[0]:
                cl = arr[1].T
    
        cdl_oo, cdl_oi, cdl_io, cdl_ii = calc_probs(cl, 'CDL2')
        outdf['CDL_OO%s' %val] = pd.Series(cdl_oo, index = outdf.index)
        outdf['CDL_OI%s' %val] = pd.Series(cdl_oi, index = outdf.index)
        outdf['CDL_IO%s' %val] = pd.Series(cdl_io, index = outdf.index)
        outdf['CDL_II%s' %val] = pd.Series(cdl_ii, index = outdf.index)
        print 'cdl done!'
        pa_oo, pa_oi, pa_io, pa_ii = calc_probs(pa, 'POPA')
        outdf['PA_OO%s' %val] = pd.Series(pa_oo, index = outdf.index)
        outdf['PA_OI%s' %val] = pd.Series(pa_oi, index = outdf.index)
        outdf['PA_IO%s' %val] = pd.Series(pa_io, index = outdf.index)
        outdf['PA_II%s' %val] = pd.Series(pa_ii, index = outdf.index)
        print 'pa done!'
        pe_oo, pe_oi, pe_io, pe_ii = calc_probs(pe, 'POPE')
        outdf['PE_OO%s' %val] = pd.Series(pe_oo, index = outdf.index)
        outdf['PE_OI%s' %val] = pd.Series(pe_oi, index = outdf.index)
        outdf['PE_IO%s' %val] = pd.Series(pe_io, index = outdf.index)
        outdf['PE_II%s' %val] = pd.Series(pe_ii, index = outdf.index)
        print 'pe done!'
        pc_oo, pc_oi, pc_io, pc_ii = calc_probs(pc, 'POPC')
        outdf['PC_OO%s' %val] = pd.Series(pc_oo, index = outdf.index)
        outdf['PC_OI%s' %val] = pd.Series(pc_oi, index = outdf.index)
        outdf['PC_IO%s' %val] = pd.Series(pc_io, index = outdf.index)
        outdf['PC_II%s' %val] = pd.Series(pc_ii, index = outdf.index)
        print 'pc done!'
        #plot_probs('probs_cutoff%s.%s.png' %(val, cutoff))
    
    
    
    outdf.to_csv('probs_%s.cutoff_by_replica.csv' %cutoff)
    
    
    
    
    




