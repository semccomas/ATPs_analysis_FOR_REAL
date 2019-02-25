import os
import numpy as np
import matplotlib.pyplot as plt
import sys
#lip = 'POPE.'
#resid = 'ARG.25'

lip = sys.argv[1]
resid = sys.argv[2]


dist = np.loadtxt('../AN_replica_1/RDF/dimer_1/CDL.1.ARG.25.xvg')
dist = dist[:,0]
rdf_avg = []
for filename in os.listdir('./'):
#	if filename.endswith(resid):
#	if filename.startswith(lip):
	if resid in filename and filename.startswith(lip):
		rdf = np.loadtxt(filename)
		rdf = rdf[:7822]
		plt.plot(dist, rdf, label = filename.strip('.txt'))
		rdf_avg.append(rdf)


plt.legend()
plt.savefig(lip.strip('.') + '-' + resid + '.png')
plt.clf()


rdf_avg = np.asarray(rdf_avg)
rdf_avg = np.mean(rdf_avg, axis = 0)

#plt.plot(dist, rdf_avg)
#plt.show()

np.savetxt(lip.strip('.') + '-' + resid + '.avg.txt', rdf_avg)
