# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata
import MDAnalysis as md

input_name = 'test2_frame_000'
GRO_FILENAME = "4YB9.6.us.gro"
frame_nums = 20

def parse_arrays(input_name, rep):
    dftot = []
    for x in np.arange(0, frame_nums + 1):
        if x == 0:
            df = pd.read_csv('%s0%i.csv' %(input_name, x), usecols = ['resid', 'leaflet', 'Area per lipid'])
        elif x < 10: 
            df = pd.read_csv('%s0%i.csv' %(input_name, x), usecols = ['resid', 'Area per lipid'])
        else:
            df = pd.read_csv('%s%i.csv' %(input_name, x), usecols = ['resid', 'Area per lipid'])
        df = df.set_index('resid')
        if x == 0:
            df.columns = ['leaflet', 'APL_%i' %x]
        else:
            df.columns = ['APL_%i' %x]
        dftot.append(df)
    dftot = pd.concat(dftot, axis = 1)
    dftot_lower = dftot.loc[dftot['leaflet'] == 'lower leaflet'].drop(columns = 'leaflet')
    dftot_upper = dftot.loc[dftot['leaflet'] == 'upper leaflet'].drop(columns = 'leaflet')
    
    
    lipid_univ = md.Universe(GRO_FILENAME)
    lipgroup_names = ['POPC', 'POPE', 'CDL2', 'POPA']
    num_plot_rows = len(lipgroup_names)
    
    def make_lip_plot(lipid):
        selection = lipid_univ.select_atoms('resname %s' %lipid)
        lipid_arr_lower = []#np.zeros(np.shape(dftot_lower))
        lipid_arr_upper = []
        for line in selection.residues:       
            try:
                lipid_arr_lower.append(dftot_lower.loc[line.resid, :].values.tolist())
            except KeyError:
                pass
            
        ### yes you have to do this loop twice,I don't know how to fix it with the try and except 
        for line in selection.residues:       
            try:
                lipid_arr_upper.append(dftot_upper.loc[line.resid, :].values.tolist()) 
            except KeyError:
                pass                          
    
        
        lipid_arr_lower = np.array(lipid_arr_lower)
        lipid_arr_upper = np.array(lipid_arr_upper)
        
        return np.mean(lipid_arr_lower, axis = 0), np.mean(lipid_arr_upper, axis = 0)
    out_dataframes = []    
    for lipid in lipgroup_names:
        low, up = make_lip_plot(lipid)
        out_dataframes.append(pd.DataFrame(data = low, columns = ['lower_%s_rep%i' %(lipid, 1)]))        
        out_dataframes.append(pd.DataFrame(data = up, columns = ['upper_%s_rep%i' %(lipid, 1)]))
    out_dataframes = pd.concat(out_dataframes, axis = 1)
    return out_dataframes

f, ((ax1, ax2), (ax3, ax4), (ax5, ax6), (ax7, ax8), (ax9, ax10)) = plt.subplots(5, 2, sharex='col', sharey='row')
axl = [(ax1, ax2), (ax3, ax4), (ax5, ax6), (ax7, ax8), (ax9, ax10)]
x = np.linspace(0, 1000, frame_nums +1)

### all you have to do here is run the function for each replica. Then you'll combine then and get the means
# and stds betwen the two arrays 
replica_1 = parse_arrays('test2_frame_000', 1)
replica_2 = parse_arrays('test9_frame_000', 2)
replica_all = pd.concat((replica_1, replica_2))
by_row_index = replica_all.groupby(replica_all.index)
rep_means = by_row_index.mean()
rep_std = by_row_index.std()
lipgroup_names = ['POPC', 'POPE', 'CDL2', 'POPA']

for ax, lip in zip(axl, lipgroup_names):
    lower_df_M = rep_means.loc[:,'lower_%s_rep1' %lip]
    upper_df_M = rep_means.loc[:,'upper_%s_rep1' %lip]
    lower_df_S = rep_std.loc[:,'lower_%s_rep1' %lip]
    upper_df_S = rep_std.loc[:,'upper_%s_rep1' %lip]
    
    #left side 
    ax[0].plot(x,lower_df_M)
    ax[0].fill_between(x, lower_df_M + lower_df_S, lower_df_M - lower_df_S, alpha = 0.4)
    ax[0].set_title('lower %s' %lip)
    ax[0].set_ylim(0,1)
    
    #right side
    ax[1].plot(x,upper_df_M)
    ax[1].fill_between(x, upper_df_M + upper_df_S, upper_df_M - upper_df_S, alpha = 0.4)
    ax[1].set_title('upper %s' %lip)
    ax[1].set_ylim(0,1)    

plt.tight_layout()
plt.show()

'''
for ax, lipid in zip(axl, lipgroup_names):
    lipid_arr_lower, lipid_arr_upper = make_lip_plot(lipid)
    lipid_arr_L_mean = np.mean(lipid_arr_lower, axis = 0)
    lipid_arr_U_mean = np.mean(lipid_arr_upper, axis = 0)
    ax[0].plot(x,lipid_arr_L_mean)
    ax[0].set_title('lower %s' %lipid)
    ax[0].set_ylim(0,1)
    ax[1].plot(x,lipid_arr_U_mean)
    ax[1].set_title('upper %s' %lipid)
    ax[1].set_ylim(0,1)

#ax4.set_ylabel('test')
#ax10.set_xlabel('test2')    
plt.tight_layout()
plt.show()
       




locn = 500
print dftot.iloc[locn,:].name, 'resid'
#plt.plot(dftot.iloc[locn,:])        

a  = dftot.iloc[2:50,:].values
plt.plot(np.mean(a, axis = 0))
plt.ylim(0, 1)
plt.show()   
'''    










plot3d = 0#int(raw_input('Plot 3d image? 1 = yes, 0 = no'))
if plot3d:
    ###############################################
    ### From FATSLiM                      #########
    ###############################################

    frame_choice = int(raw_input('Choose a frame to plot (between 1 and %i)' %frame_nums))
    if frame_choice < 10:
        CSV_FILENAME =  '%s0%i.csv' %(input_name, frame_choice)
    else:
        CSV_FILENAME = '%s%i.csv' %(input_name, frame_choice)
    
    PNG_FILENAME = 'contour_APL.frame%i.png' %frame_choice
    # Get Box vectors
    last_line = ""
    with open(GRO_FILENAME) as fp:
        for line in fp:
            line = line.strip()
    
            if len(line) == 0:
                continue
    
            last_line = line
    
    box_x, box_y = [float(val) for val in line.split()[:2]]
    
    # Get values
    membrane_property = "Area per lipid"
    x_values = []
    y_values = []
    z_values = []
    property_values = []
    with open(CSV_FILENAME) as fp:
        for lino, line in enumerate(fp):
            if lino == 0:
                membrane_property = line.split(",")[-1].strip()
    
            else:
                line = line.strip()
    
                if len(line) == 0:
                    continue
    
                resid, leaflet, x, y, z, value = line.split(",")
    
                x_values.append(float(x))
                y_values.append(float(y))
                property_values.append(float(value))
    
    # Building data from plotting
    grid_x, grid_y = np.mgrid[0:box_x:50j, 0:box_y:50j]
    points = np.stack((np.array(x_values).T, np.array(y_values).T), axis=-1)
    values = np.array(property_values)
    grid = griddata(points, values, (grid_x, grid_y), method='cubic')
    
    # Plot map
    plt.xlim(0,10)
    plt.contourf(grid_x, grid_y, grid)
    #plt.contourf(grid_x, grid_y, grid, vmin = 0, vmax = 2)
    #plt.clim(0, 2)
    cbar = plt.colorbar()
    
    plt.title(membrane_property)
    plt.xlabel("Box X (nm)")
    plt.ylabel("Box Y (nm)")
    
    plt.savefig(PNG_FILENAME)