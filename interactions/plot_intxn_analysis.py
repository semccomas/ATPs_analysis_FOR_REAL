#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 11:11:34 2018

@author: semccomas
"""
### this will be for protein and for lipids, pretty much two scripts but it's easier to keep it all together

import pandas as pd
import numpy as np


print 'Choose 1 for protein plotting, you can choose later if you want to write a pdb or not'
print 'Choose 0 for lipid plotting'
prompt = raw_input('0 or 1?' )
prot_plot = int(prompt)

print 'Now choose lipid for analysis, POPA, POPC, POPE, or CDL2'
prompt = raw_input('lipid? ')
lipname = str(prompt).upper()

if prot_plot:
    df = pd.read_csv('arrays_csv/%s.max.avg.long.protres_index.csv' %lipname, index_col = 0)
