import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Sample input data for the plot and the fit---use your data points and errors :-)
x = np.array([0.5, 1.1, 1.7, 2.3, 2.9, 3.5, 4.1, 4.7, 5.3, 5.9, 6.5, 7.1, 7.7, 8.3, 8.9, 9.5])
y = np.array([35, 61, 76, 70, 92, 100, 111, 113, 140, 163, 177, 209, 223, 264, 290, 312])
sigma = np.full(y.shape, 10.0)

# Definition of the model for fitting the data.
def model(x, a, b, c):
    """Simple quadratic fitting model.
    """
    return a + b * x + c * x**2.

# Perform the fit...
popt, pcov = curve_fit(model, x, y, sigma=sigma)
# ...and calculate the residuals with respect to the best-fit model.
res = y - model(x, *popt)

# Create the main figure...
fig = plt.figure('Un grafico dei residui')
# ...and make space for the two plots. Note that `gridspec_kw` and `hspace`
# control the arrangements of the two sub-panels within the figure, see
# https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html
ax1, ax2 = fig.subplots(2, 1, sharex=True, gridspec_kw=dict(height_ratios=[2, 1], hspace=0.05))

# Main plot: the scatter plot of x vs. y, on the top panel.
ax1.errorbar(x, y, sigma, fmt='o', label='Dati')
# Plot the best-fit model on a dense grid.
xgrid = np.linspace(0.0, 10.0, 100)
ax1.plot(xgrid, model(xgrid, *popt), label='Modello di best-fit')
# Setup the axes, grids and legend.
ax1.set_ylabel('y [a. u.]')
ax1.grid(color='lightgray', ls='dashed')
ax1.legend()

# And now the residual plot, on the bottom panel.
ax2.errorbar(x, res, sigma, fmt='o')
# This will draw a horizontal line at y=0, which is the equivalent of the best-fit
# model in the residual representation.
ax2.plot(xgrid, np.full(xgrid.shape, 0.0))
# Setup the axes, grids and legend.
ax2.set_xlabel('x [a. u.]')
ax2.set_ylabel('Residuals [a. u.]')
ax2.grid(color='lightgray', ls='dashed')

# The final touch to main canvas :-)
plt.xlim(0.0, 10.0)
fig.align_ylabels((ax1, ax2))

plt.show()
