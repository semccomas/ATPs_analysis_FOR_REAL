#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 14:24:47 2018

@author: semccomas
"""

import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
#for f in os.listdir('./'):
#    if f.endswith('dat'):
#        print f


def pandas_df(num, top_or_bottom):
    fname = 'ATPs1.APL.frame%i.150x150.%s_areas.dat' %(num, top_or_bottom)
    df = pd.read_csv(fname, skiprows = 3, delimiter = '\t')
    df.columns = ['protein', '%i.z' %num, '%i.A' %num]
    df = df.set_index('protein')
    df = df.drop('%i.z' %num, axis = 1)
    return df                
    
for x in np.arange(1,22):
   # ft = 'ATPs1.APL.frame%i.150x150.top_areas.dat' %x
   # fb = 'ATPs1.APL.frame%i.150x150.bottom_areas.dat' %x
   
    if x == 1:
        t = pandas_df(x, 'top')
        b = pandas_df(x, 'bottom')
        df = t.append(b, verify_integrity = True)
    else:
        t = pandas_df(x, 'top')
        b = pandas_df(x, 'bottom')
        df_0 = t.append(b, verify_integrity = True)

        df = pd.concat([df, df_0], axis = 1)

num= 577
#
#for num in xrange(530,8548):
for num in xrange(530,540):
    plt.plot(np.arange(1, 21),df.loc[num,'2.A':])
plt.xlim(0)
plt.ylim(0, 120)
plt.title(str(df.loc[num, :].name))
plt.show()
    #if num % 10 == 0:
     #   raw_input()
        