#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 14:08:03 2019

@author: semccomas
"""

import numpy as np

short_lip = np.loadtxt('1.8_cutoff/POPE_A_3.xvg')[:,1:] 
long_lip = np.loadtxt('3.5_cutoff/POPE_A_3.xvg')[:,1:]

short_add = np.full_like(short_lip[0], 1.8)
long_add = np.full_like(long_lip[0], 3.5)
#short_lip = np.vstack((short_lip, short_add))
#long_lip = np.vstack((long_lip, long_add))
short_lip = short_lip < 1.8
long_lip = long_lip < 3.5
               
counts = []
    for short, longs in zip(short_lip.T, long_lip.T): #need to transpose because you have to read lipid by lipid 
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
                         #   print frame_num + 1, '= length of binding'  #we print + 1 here because frame_num starts at 0, and we want to count that as a res time
                            break
                return frame_num + 1, start_where_long #we want to know residence time, and where to continue from
            
            else:
                print 'no more binding events found'
                return len(longs)+1, 0   #this will then be as long as longs, breaking the while loop below
        
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
                 print 'finished!'
                 print
                 pass
    
    
    print counts