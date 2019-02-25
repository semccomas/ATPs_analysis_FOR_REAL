#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 11:25:04 2019

@author: sarahmccomas

This script is loosely based on intxn_analysis.py
"""

import numpy as np
import matplotlib.pyplot as plt

#short = np.array([0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0], dtype = bool)
#longs = np.array([0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0], dtype = bool)
                 #0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17   
#start at index 4, end at index 10 => event count is 7

def count_res(lip_name):
    short_lip = np.loadtxt('1.8_cutoff/%s.xvg' %lip_name)[:,1:] 
    long_lip = np.loadtxt('3.5_cutoff/%s.xvg' %lip_name)[:,1:]
    short_lip = short_lip < 1.8
    long_lip = long_lip < 3.5
    
    long_lip_drop_stuck = long_lip[:,~np.all(long_lip, axis=0)]
    #short_lip = short_lip[:,~np.all(long_lip, axis=0)]    #we have to drop in both short and long, all the guys that are only TRUE in long
    short_lip_drop_stuck = short_lip[:,~np.all(long_lip, axis=0)]
                   
    counts = []
    for short, longs in zip(short_lip_drop_stuck.T, long_lip_drop_stuck.T): #need to transpose because you have to read lipid by lipid 
        def dual_cutoff(start_read):
          #  print 'starting at index %s'  %start_read
            #this is saying, at what index does short continue from? Ex: say lipid exits longs at index
            ## 10, we need to tell short to continue from 10, and start the next trigger (start_where_long)
            ### but we need still the indexes to be in place(ie can't say short[10:] because then you lose your place
            #### when triggering longs). So we find where this continues from, and repeat, triggering longs
            ##### when we get the first true again from short. 
            ##
            ###### THEN, you start reading from longs, you do np.where to say how long is longs continuous, break
            ####### after that point and report back the # of frames continuous in long
            if np.any(np.where(short)[0] > start_read):
                start_where_short = np.where(np.where(short)[0] > start_read)[0][0]    
                start_where_long = np.where(short)[0][start_where_short]  #access list in array, and take first val
            #    print 'lipid found in 1.8 cutoff at time %s' %start_where_long
                events_indices = np.where(longs[start_where_long:])[0]  
                events_indices = np.append(events_indices,0) #array, starting at index start_where_long. If longs looks like [True, True, True, False, True], then
                ### events_indices will look like [0, 1, 2, 4], meaning lipid left after 3 frames, and residence time should stop at n = 3. We add a zero to the last frame
                ### so that if we are at the end of traj and longs looks like [True, True, True], then we will count all those 3 residence times at the end.
                for frame_num, event_index in enumerate(events_indices):
                    if event_index + 1 != events_indices[frame_num+1]:
            #                print frame_num + 1, '= length of binding'  #we print + 1 here because frame_num starts at 0, and we want to count that as a res time
                            break
                return frame_num + 1, start_where_long #we want to know residence time, and where to continue from
            
            else:
           #     print 'no more binding events found'
                return len(longs)+1, 0   #this will then be longer than longs, breaking the while loop below. It's important that it doesn't == longs because sometimes we end
                                         ### at the length of longs, and these should be accounted for (ie, things that stay bound)
        
            
        start_read = 0 #start at beginning of array
        while start_read < len(longs):  
            len_binding, start_where_short = dual_cutoff(start_read)
            start_read = len_binding + start_where_short   #continue from residence time + wherever you started from again
            if start_read <= len(longs) and len_binding < 795:  #nix all guys that are trapped
                counts.append(len_binding)
                print len_binding, '(binding len) + ', start_where_short, '(starting index) = ', start_read
                print len_binding, 'res time'
                if start_read < len(longs):
                    print 'running again from index %s' %start_read
                else:
                    print 'Finished bound at end of trajectory, index 802'
            else:
                 #print 'finished!'
                 #print
                 pass
        
        
        
    return counts
    
    
POPA_out = []
POPC_out = []
POPE_out = []
CDL2_out = []

lipids_list = [POPA_out, CDL2_out, POPC_out, POPE_out]
lipids = ['POPA', 'CDL2', 'POPC', 'POPE']
for lipid_list, lipid in zip(lipids_list, lipids):
    lipid_list.append(count_res('%s_A_1' %lipid))
    lipid_list.append(count_res('%s_A_2' %lipid))
    lipid_list.append(count_res('%s_A_3' %lipid))
    lipid_list.append(count_res('%s_B_1' %lipid))
    lipid_list.append(count_res('%s_B_2' %lipid))
    lipid_list.append(count_res('%s_B_3' %lipid))
    
    
POPA_out = np.hstack(POPA_out)
POPC_out = np.hstack(POPC_out)
POPE_out = np.hstack(POPE_out)
CDL2_out = np.hstack(CDL2_out)


'''
import scipy.stats as stats

density = stats.gaussian_kde(CDL2_out)
n, x, _ = plt.hist(CDL2_out, density = True)


density2 = stats.gaussian_kde(POPC_out)
n, x2, _ = plt.hist(POPC_out, density = True)

plt.clf()

plt.plot(x, density(x), label = 'pa')

plt.plot(x2, density2(x2), label = 'pc')
plt.legend()
#plt.hist(POPA_out, fill = False, color = 'red')
#plt.hist(POPC_out, fill = False, color = 'green')
#plt.hist(POPE_out, fill = False, color = 'yellow')
#plt.hist(CDL2_out, fill = False, color = 'purple')


plt.xlim(0, 800)
plt.ylim(0)
plt.show()
'''
#%%
#plt.scatter(np.zeros(len(POPA_out)) + 1, POPA_out, label = 'pa')
#plt.scatter(np.zeros(len(POPE_out)) + 2, POPE_out, label = 'pe')
#plt.scatter(np.zeros(len(POPC_out)) + 3, POPC_out, label = 'pc')
#plt.scatter(np.zeros(len(CDL2_out)) + 4, CDL2_out, label = 'cdl')

my_dict = {'POPC':POPC_out, 'POPA': POPA_out, 'CDL2':CDL2_out, 'POPE':POPE_out}
fig, ax = plt.subplots()
ax.boxplot(my_dict.values(), )
ax.set_xticklabels(my_dict.keys())
plt.ylim(0, 800)
#locs, labels = plt.yticks()
locs = np.array([0, 200, 400, 600, 800])
plt.yticks(locs, np.round(np.linspace(0, 2, 5), 2))
plt.ylabel(r'residence time ($\mu$s)')

plt.legend()

plt.savefig('3.5cutoff.png', dpi = 600)


