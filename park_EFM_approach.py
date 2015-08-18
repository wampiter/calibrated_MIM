import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt

dcdz = 2.66 #aF/nm/V
filename = '150814Spectroscopy002_3.txt'
data = np.genfromtxt(filename, skip_header = 3)
size = data[:,0].size/2
z = data[0:size,2]*1000.0 #in nm
mim = data[0:size,4] #uncalibrated MIM-Im data
efm = data[0:size,6]*dcdz #EFM data in aF/nm
efm_int = -integrate.cumtrapz(efm, x = z)

plt.clf()
efmline, = plt.plot(z[0:1023] - 8245 -49, efm_int, label = "Integrated EFM")
mimline, = plt.plot(z - 8245 -49, (mim-1.67)*620, label = "MIM-Im (scaled)")
plt.legend(handles=[efmline, mimline])
plt.xlabel("z (nm)")
plt.ylabel("C (aF)")