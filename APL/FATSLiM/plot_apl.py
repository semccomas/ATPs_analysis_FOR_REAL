###### -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata
import MDAnalysis as md

#input_name = 'test2_frame_000'
GRO_FILENAME = "ATPs.7.eq.gro"
frame_nums = 40

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
    dftot = dftot.dropna()
    dftot_lower = dftot.loc[dftot['leaflet'] == 'lower leaflet']
    dftot_lower = dftot_lower.drop(columns = 'leaflet')
    dftot_upper = dftot.loc[dftot['leaflet'] == 'upper leaflet']
    dftot_upper = dftot_upper.drop(columns = 'leaflet')
    
    
    lipid_univ = md.Universe('replica_%s/%s' %(rep, GRO_FILENAME))
    lipgroup_names = ['POPA', 'CDL2', 'POPC', 'POPE']
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



### all you have to do here is run the function for each replica. Then you'll combine then and get the means
# and stds betwen the two arrays 
replica_1 = parse_arrays('replica_1/rep1_frame_000', 1)
replica_2 = parse_arrays('replica_2/rep2_frame_000', 2)
replica_3 = parse_arrays('replica_3/rep3_frame_000', 3)

replica_all = pd.concat((replica_1, replica_2, replica_3))
by_row_index = replica_all.groupby(replica_all.index)
rep_means = by_row_index.mean()
rep_std = by_row_index.std()
lipgroup_names = ['POPA', 'CDL2', 'POPC', 'POPE']

f, ((ax1, ax2), (ax3, ax4), (ax5, ax6), (ax7, ax8)) = plt.subplots(4, 2, sharex='col', sharey='row')
axl = [(ax1, ax2), (ax3, ax4), (ax5, ax6), (ax7, ax8)]
x = np.linspace(0, 4000, frame_nums +1)/1000

colors = ['#E6BF26', '#6167B4', '#54ABA7', '#C73A29']
n = 0
for ax, lip in zip(axl, lipgroup_names):
    lower_df_M = rep_means.loc[:,'lower_%s_rep1' %lip]
    upper_df_M = rep_means.loc[:,'upper_%s_rep1' %lip]
    lower_df_S = rep_std.loc[:,'lower_%s_rep1' %lip]
    upper_df_S = rep_std.loc[:,'upper_%s_rep1' %lip]
    colorN = colors[n]
    #left side 
    ax[0].plot(x,lower_df_M, color = colorN)
    ax[0].fill_between(x, lower_df_M + lower_df_S, lower_df_M - lower_df_S, alpha = 0.4, color = colorN)
    ax[0].set_title('lower leaflet %s' %lip, fontsize = 9)
    ax[0].set_ylim(0.4,1)
    ax[0].set_xlim(0, 4)
    
    #right side
    ax[1].plot(x,upper_df_M, color = colorN)
    ax[1].fill_between(x, upper_df_M + upper_df_S, upper_df_M - upper_df_S, alpha = 0.4,color = colorN)
    ax[1].set_title('upper leaflet %s' %lip, fontsize = 9)
    ax[1].set_ylim(0.4,1) 
    ax[1].set_xlim(0, 4)
    n = n+ 1

txt = plt.gcf().text(0.5, 0, r'$Time (\mu s)$')
txt2 = plt.gcf().text(0, 0.6, 'Area per lipid',rotation=90)
plt.tight_layout()
#plt.show()
plt.savefig('APL_all.png', dpi = 2000, bbox_extra_artists=(txt2,txt,), bbox_inches='tight')
















'''


input_name = 'replica_1/rep1_frame_000'
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
    with open('replica_1/%s' %GRO_FILENAME) as fp:
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

'''
