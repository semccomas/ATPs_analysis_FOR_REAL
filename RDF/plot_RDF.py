#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 13:47:37 2018

@author: semccomas
"""

import numpy as np
import matplotlib.pyplot as plt
import os
import sys
from scipy.ndimage.filters import gaussian_filter

outdir = 'headgroup_xvg'
prompt = 0#int(raw_input('calculate arrays (answer 1 for yes)? TAKES SOME TIME!!! (answer 0 for no)' ))
if prompt:
    cdl = np.zeros((438, 3, 7822))
    pe = np.zeros((438, 3, 7822))
    pc = np.zeros((438, 3, 7822))
    pa = np.zeros((438, 3, 7822))
    c = 0
    for f in os.listdir('%s/' %outdir):
        c = c + 1
        fname = f.split('.')
        sys.stdout.write('\r')
        sys.stdout.write('%i/3233 done' %c)
        sys.stdout.flush()
        rep_position = int(fname[1]) - 1 ## to index on array
        res_position = int(fname[2]) - 1 ## same here, index on axis 0
        if rep_position == 2: #if we are looking at replica 3, as you see is this -1 
            arr = np.loadtxt('%s/%s' %(outdir, f))[:-4]
        else:
            arr = np.loadtxt('%s/%s' %(outdir, f))
        cdl[res_position][rep_position] = arr[:,1]  #cdl comes first in selection for RDF (see lipid_selection.dat)
        pe[res_position][rep_position] = arr[:,2]
        pc[res_position][rep_position] = arr[:,3]
        pa[res_position][rep_position] = arr[:,4]
    
    
    np.save('%s/CDL2_RDF_all.npy' %outdir, cdl)
    np.save('%s/POPE_RDF_all.npy' %outdir, pe)
    np.save('%s/POPC_RDF_all.npy' %outdir, pc)
    np.save('%s/POPA_RDF_all.npy' %outdir, pa)
    

if not prompt:
    cdl = np.load('%s/CDL2_RDF_all.npy'%outdir)
    pe = np.load('%s/POPE_RDF_all.npy'%outdir)
    pc = np.load('%s/POPC_RDF_all.npy'%outdir)
    pa = np.load('%s/POPA_RDF_all.npy' %outdir)
    

prompt = 1#int(raw_input('Average all reps?(1 = yes / 0 = no, plot separately)'))   #### YES average all reps
#std_dev = int(raw_input('Plot standard deviation? (1 = yes, 0 = no)'))
gaus = 1#int(raw_input('Gaussian filter? (1) or no (0)?'))
meancdl = np.mean(cdl, axis = 0)   
meanpe = np.mean(pe, axis = 0)    
meanpc = np.mean(pc, axis = 0)    
meanpa = np.mean(pa, axis = 0)



def plot_rep(rep_name, rep_index, ax):  #we don't actually use this plot when averaging all together but just leave for now
    if gaus:
        sig = 5
        meancdl_g = gaussian_filter(meancdl[rep_index], sigma=sig, mode = 'mirror') 
        meanpe_g = gaussian_filter(meanpe[rep_index], sigma=sig, mode = 'mirror')
        meanpc_g = gaussian_filter(meanpc[rep_index], sigma=sig, mode = 'mirror')
        meanpa_g = gaussian_filter(meanpa[rep_index], sigma=sig, mode = 'mirror')
        ax.plot(meancdl_g, color = 'blue', label = 'CDL2')
        ax.plot(meanpe_g, color = 'orange', label = 'POPE')
        ax.plot(meanpc_g, color = 'green', label = 'POPC')
        ax.plot(meanpa_g, color = 'red', label = 'POPA')
        return meancdl_g, meanpe_g, meanpc_g, meanpa_g


    if not gaus:
        ax.plot(meancdl[rep_index], color = 'blue', label = 'CDL2')
        ax.plot(meanpe[rep_index], color = 'orange', label = 'POPE')
        ax.plot(meanpc[rep_index], color = 'green', label = 'POPC')
        ax.plot(meanpa[rep_index], color = 'red', label = 'POPA')
        return meancdl, meanpe, meanpc, meanpa

    ax.set_xlim(0,2500)
    ax.set_ylim(0)
    ax.set_title('Replica %i for %s' %(rep_name, outdir))
    
    
#    if rep_index == 2:
#        lgd = ax.legend(loc='upper right', bbox_to_anchor=(-0.1, 0.5))

f, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True)
CL1, PE1, PC1, PA1 = plot_rep(1, 0, ax1)
CL2, PE2, PC2, PA2 = plot_rep(2, 1, ax2)
CL3, PE3, PC3, PA3 = plot_rep(3, 2, ax3)

if not prompt:
    plt.tight_layout()
    plt.savefig('%s/RDF_plot_per_rep.png' %outdir, dpi = 800)
    #plt.show()


dist = np.loadtxt('headgroup_xvg/RDF.1.1.xvg')[:,0]

def combine_arrs(arr1, arr2, arr3):
    tot = np.vstack((arr1, arr2, arr3))
    std = np.std(tot, axis = 0)
    mean = np.mean(tot, axis = 0)
    
    return std, mean
    
if prompt:  #if average all reps
    plt.clf()
    stdcdl, meancdl = combine_arrs(CL1,CL2,CL3)
    stdpe, meanpe = combine_arrs(PE1,PE2,PE3)
    stdpc, meanpc = combine_arrs(PC1,PC2,PC3)
    stdpa, meanpa = combine_arrs(PA1,PA2,PA3)


    plt.plot(dist,meanpa, label = 'POPA', color = '#E6BF26')
    plt.plot(dist,meancdl, label = 'CDL2', color = '#6167B4')
    plt.plot(dist,meanpc, label = 'POPC', color = '#54ABA7')
    plt.plot(dist,meanpe, label = 'POPE', color = '#C73A29')#CD4B3B
    
    plt.fill_between(dist, meanpa + stdpa, meanpa - stdpa, color = '#E6BF26', alpha = 0.4)
    plt.fill_between(dist, meancdl + stdcdl, meancdl - stdcdl, color = '#6167B4', alpha = 0.4)
    plt.fill_between(dist, meanpc + stdpc, meanpc - stdpc, color = '#54ABA7', alpha = 0.4)
    plt.fill_between(dist, meanpe + stdpe, meanpe - stdpe, color = '#C73A29', alpha = 0.4)
    

    #plt.title('Radial Distribution Function')
    plt.legend()
    plt.xlim(0, 5)
    plt.ylim(0)
    plt.xlabel('distance (nm)')
    plt.ylabel('g(r)')
    #plt.show()
    plt.savefig('RDF_head_avg_zoom.png', dpi = 2000)

#plt.savefig('probs_plot.cutoff.%s.by_replica.NOstd.png' %cutoff, bbox_extra_artists=(lgd,txt,), bbox_inches='tight', dpi = 900)



#np.arange(len(stdpe))















    
