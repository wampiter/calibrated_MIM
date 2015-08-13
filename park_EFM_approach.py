import numpy as np
import scipy.integrate as integrate

dcdz = 1.45 #aF/nm/V
filename = '150804151737Spectroscopy001_2.txt'
data = np.genfromtxt(filename, skip_header = 3)
size = data[:,0].size/2
z = data[0:size,2]*1000.0 #in nm
p #uncalibrated MIM-Im data
efm = data[0:size,6]*dcdz #EFM data in aF/nm
efm_int = -integrate.cumtrapz(efm, x = z)

plt.clf()
efmline, = plt.plot(z[0:1023] - 8245, efm_int, label = "Integrated EFM")
mimline, = plt.plot(z - 8245, mim_fit*3.35 + 5, label = "MIM-Im (scaled)")
plt.legend(handles=[efmline, mimline])