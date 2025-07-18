import numpy as np
from scipy.optimize import curve_fit

def fit_model(x, omega):
    return np.sin(omega * x)

# Definition of the input data set.
np.random.seed(100)
n = 20
sigma_y = 0.05
omega = 1.2
x = np.linspace(1.0, 19.0, n)
y = fit_model(x, omega) + np.random.normal(0.0, sigma_y, n)
# Need to turn sigma_y into an array to be used in the fit.
sigma_y = np.full(y.shape, sigma_y)
# Perform the fit and calculate the chisquare.
popt, pcov = curve_fit(fit_model, x, y, sigma=sigma_y)
chisq = (((y - fit_model(x, *popt)) / sigma_y)**2).sum()
# Print the fit output.
print(f'omega = {popt[0]:.4f} +/- {np.sqrt(pcov[0, 0]):.4f}')
print(f'Chisquare = {chisq:.1f}')
