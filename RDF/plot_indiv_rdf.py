#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 15:11:31 2018

@author: semccomas
"""


import numpy as np
import matplotlib.pyplot as plt 
from scipy.ndimage.filters import gaussian_filter
import sys
import os
#a = np.loadtxt('new_xvg/RDF.1.7.xvg')
#a = np.loadtxt(sys.argv[1])
c = 0
for x in xrange(1,430): #os.listdir('headgroup_xvg/'):
    for t in xrange(1,4):
        f = 'RDF.%i.%i.xvg' %(t, x)
        c = c + 1
        a = np.loadtxt('headgroup_xvg/%s' %f)
        #gaus = int(raw_input('Gaussian filtering? (1 yes 0 no)'))
        gaus = 1
        cdl = a[:,1]
        pe = a[:,2]
        pc = a[:,3]
        pa = a[:,4]
        
        sig = 20
        if gaus:
            cdl = gaussian_filter(cdl, sigma=sig, mode = 'mirror')
            pe = gaussian_filter(pe, sigma=sig, mode = 'mirror')
            pc = gaussian_filter(pc, sigma=sig, mode = 'mirror')
            pa = gaussian_filter(pa, sigma=sig, mode = 'mirror')
        
        plt.plot(cdl, label = 'CDL2', color = 'blue')
        plt.plot(pa, label = 'POPA', color = 'red')
        plt.plot(pc, label = 'POPC', color = 'green')
        plt.plot(pe, label = 'POPE', color = 'yellow')
        plt.legend()
        plt.title(f)
        plt.savefig('test/%s.png' %f)
        plt.clf()
    #    if c %9 == 0:   #ask to keep going every 5 plots
           # raw_input() 