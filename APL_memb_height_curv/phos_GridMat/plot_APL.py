#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 14:20:04 2018

@author: sarahmccomas
"""

import os
import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd 


a = pd.read_csv('ATPs1.APL.frame9.150x150.top_areas.dat', skiprows =3, delimiter = '\t')


'''
bottom_areas = []
top_areas = np.empty()
num_frames = 21
for x in xrange(1, num_frames+1):
    for filename in os.listdir('./'):
        if 'frame%s.150x150.top_areas' %str(x) in filename:
            top_areas.append(np.loadtxt(filename, skiprows =4))
'''