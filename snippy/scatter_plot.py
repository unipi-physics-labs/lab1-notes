import numpy as np
from matplotlib import pyplot as plt

# Set matplotlib in interactive mode, so that plots are
# displayed on the screen as they are created.
plt.ion()

# Definition of the data points.
t = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
s = [20.5, 28.7, 35.4, 43.1, 51.8, 54.6, 64.1, 69.7, 77.5]
sigma_s = [2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5]
# Make the actual plot.
plt.errorbar(t, s, sigma_s, fmt='o')
# Setup the axes labels.
plt.xlabel('Tempo [s]')
plt.ylabel('Posizione [cm]')
# Adjust the axis ranges (None means autoscale).
plt.axis([0.0, 10.0, 0.0, None])
