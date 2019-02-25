import numpy as np
import matplotlib.pyplot as plt
import os

shortgraph = 4000
avgcdl = []
avgpe = []
avgpc = []
avgpa = []

dist = np.loadtxt('../AN_replica_1/RDF/dimer_1/CDL.1.ARG.25.xvg')
dist = dist[:,0]
dist = dist[:shortgraph]

for filename in os.listdir('./'):
    if filename.endswith('.avg.txt'):
        rdf = np.loadtxt(filename)
        if 'CDL' in filename:
            plt.plot(rdf, label = filename, color = '#009A8F')
	    avgcdl.append(rdf)
        if 'POPE' in filename:
            plt.plot(rdf, label = filename, color = '#1820AE')
	    avgpe.append(rdf)
        if 'POPC' in filename:
            plt.plot(rdf, label = filename, color = '#FB6D00')
	    avgpc.append(rdf)
        if 'POPA' in filename:
            plt.plot(rdf, label = filename, color = '#FBB900')
	    avgpa.append(rdf)
plt.legend()
#plt.show()

plt.clf()

fig,ax = plt.subplots()
def plot_avgs2(avg, lab, col):
	avg = np.mean(avg, axis = 0)
	avg = avg[:shortgraph]
	ax.plot(dist, avg, label = lab, color = col, alpha =0.5)
	return avg

cdl2 = plot_avgs2(avgcdl, 'CDL', '#009A8F')
pe2 = plot_avgs2(avgpe, 'POPE', '#1820AE')
pc2 = plot_avgs2(avgpc, 'POPC', '#FB6D00')
pa2 = plot_avgs2(avgpa, 'POPA', '#FBB900')


def find_min(rdf):
    density = rdf
        
    maxpt = int(np.argwhere(density == max(density)))  #where does first RDF peak start
    step = maxpt                                        
    upcount = 0                                         # same for smooth below, use this to make sure you found a 'global' min
    ## and not just a little bump. sigma is 10 for this reason too
    smooth = 5
    for line in density[maxpt:]:
        if density[step] >= density[step + 1]:   # if current density is larger than the following, we are still on peak
#            print density[step] - density[step + 1], step, 'going down'
            pass
        else:
#            print density[step] - density[step + 1], step, 'going up'
            upcount = upcount + 1               #as above, for smoothing
            final = step - smooth
            if upcount >= smooth:
                break                           #when reached cutoff, stop and report initial base
        step = step + 1
    return final
    
mincdl2 = find_min(cdl2)
minpe = find_min(pe2)
minpc = find_min(pc2)
minpa =  find_min(pa2)


ax.scatter(dist[mincdl2], cdl2[mincdl2], color = '#009A8F')
ax.scatter(dist[minpe], pe2[minpe], color = '#1820AE')
ax.scatter(dist[minpc], pc2[minpc], color = '#FB6D00')
ax.scatter(dist[minpa], pa2[minpa], color = '#FBB900')

textstr = '\n'.join((
'CDL min '+ str(dist[mincdl2]),
'PE min ' + str(dist[minpe]),
'PC min ' + str(dist[minpc]),
'PA min ' + str(dist[minpa])))

props = dict(boxstyle='square', facecolor = 'white', alpha = 0.5)
ax.text(0.75,0.4,textstr, fontsize=10, transform = ax.transAxes, verticalalignment='top', bbox= props)

plt.legend()
plt.xlabel('Distance from residue')
plt.ylabel('g(r)')
plt.title('RDF - system lipids vs select residues')
#plt.show()
plt.savefig('AVG_ALL_RDFS.png', dpi = 800)
