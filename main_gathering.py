import numpy as np
import matplotlib.pyplot as plt
import libconf
from class_gathering import gathering

"""
The script gathers all data in one file.
It returns the survival function with the corresponding time in hours with bin in minutes.
The imput times must be in hours.
The imput survival functions must go to zero.
"""

# Data configuration
with open ('./config_file.cfg') as cfg:
	config = libconf.load(cfg)

t_max =  config['t_max'] # Should be above the duration of the longest experiment (in minutes)
fileroot = config['fileroot'] # Data location without experiment name/number
extension = config['extension'] # File format and end of the name
exp_name = config['exp_name'] # String containing the names of the different experiments

# Object calling
gath = gathering(t_max)

# Arrays creation, legend (plot)
t_minute = np.arange(0, t_max, 1)
s_minute = np.copy(t_minute) * 0
legend = []

# Data gathering
for i in range(len(exp_name)):
	path_exp = fileroot + exp_name[i] + extension # Writes the path where the data are
	t_i, s_i = np.loadtxt(path_exp ,unpack=True) # Opens the data
	s_minute_i = gath.minute_bin(t_i, s_i) # Converts in minute bins
	s_minute += s_minute_i # Add up to previous data
	plt.plot(t_i, s_i/s_i[0], '.') # Plots the individual data
	legend.append('Data set ' + exp_name[i])

# Data saving
np.savetxt('./gathered_data.txt', np.transpose([t_minute/60, s_minute]))

# Survival function plotting, total number of films displaying
print('Total number of films: ', s_minute[0])
legend.append('All data')
plt.plot(t_minute/60, s_minute/s_minute[0], 'k-')
plt.xlabel('Time [hours]')
plt.ylabel('Normalized number of films')
plt.legend(legend)
plt.xlim([0, t_max/60])
plt.ylim([0, 1])
plt.show()
