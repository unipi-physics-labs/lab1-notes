import numpy as np
from scipy.optimize import curve_fit

def fit_model(x, m):
    return m * x

x = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
y = np.array([0.112, 0.202, 0.299, 0.393, 0.512])
sigma_y = np.array([0.01, 0.01, 0.01, 0.01, 0.010])

# Case 1: no errors, absolute_sigma = False
popt, pcov = curve_fit(fit_model, x, y)
m_hat, sigma_m = popt[0], np.sqrt(pcov.diagonal()[0])
print(f'm = {m_hat:.4f} +/- {sigma_m:.4f}')
# Case 2: errors, absolute_sigma = False
popt, pcov = curve_fit(fit_model, x, y, sigma=sigma_y)
m_hat, sigma_m = popt[0], np.sqrt(pcov.diagonal()[0])
print(f'm = {m_hat:.4f} +/- {sigma_m:.4f}')
# Case 3: no errors, absolute_sigma = True
popt, pcov = curve_fit(fit_model, x, y, absolute_sigma=True)
m_hat, sigma_m = popt[0], np.sqrt(pcov.diagonal()[0])
print(f'm = {m_hat:.4f} +/- {sigma_m:.4f}')
# Case 4: errors, absolute_sigma = True
popt, pcov = curve_fit(fit_model, x, y, sigma=sigma_y,
                       absolute_sigma=True)
m_hat, sigma_m = popt[0], np.sqrt(pcov.diagonal()[0])
print(f'm = {m_hat:.4f} +/- {sigma_m:.4f}')
