import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

import matplotlib_ as mpl_


# Sample input data for the plot and the fit.
x = np.array([0.5, 1.1, 1.7, 2.3, 2.9, 3.5, 4.1, 4.7, 5.3, 5.9, 6.5, 7.1, 7.7, 8.3, 8.9, 9.5])
y = np.array([35, 61, 76, 70, 92, 100, 111, 113, 140, 163, 177, 209, 223, 264, 290, 312])
sigma = np.full(y.shape, 10.0)

# Definition of the model for fitting the data.
def model(x, a, b, c):
    return a + b * x + c * x**2.

# Perform the fit and calculate the residuals with respect to the best-fit model.
popt, pcov = curve_fit(model, x, y, sigma=sigma)
res = y - model(x, *popt)

# Create the main figure and make space for the two plots.
fig = plt.figure('Grafico dei residui')
ax1, ax2 = fig.subplots(2, 1, sharex=True, gridspec_kw=dict(height_ratios=[2, 1], hspace=0.05))

# Main plot: the scatter plot of x vs. y, on the top panel.
ax1.errorbar(x, y, sigma, fmt='o', label='Dati')
xgrid = np.linspace(0.0, 10.0, 100)
ax1.plot(xgrid, model(xgrid, *popt), label='Modello di best-fit', color='k')
ax1.set_ylabel('y [a. u.]')
ax1.grid(color='lightgray', ls='dashed')
ax1.legend()

# Residual plot, on the bottom panel.
ax2.errorbar(x, res, sigma, fmt='o')
ax2.plot(xgrid, np.full(xgrid.shape, 0.0), color='k')
ax2.set_xlabel('x [a. u.]')
ax2.set_ylabel('Residui [a. u.]')
ax2.grid(color='lightgray', ls='dashed')

# The final touch to main canvas :-)
plt.xlim(0.0, 10.0)
fig.align_ylabels((ax1, ax2))

mpl_.save_all_figures()
