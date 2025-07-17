import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit

plt.ion()

def fit_model(x, m, q):
    return m * x + q

t = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
s = [20.5, 28.7, 35.4, 43.1, 51.8, 54.6, 64.1, 69.7, 77.5]
sigma_s = np.full(len(s), 2.5)
plt.errorbar(t, s, sigma_s, fmt='o')
plt.xlabel('Tempo [s]')
plt.ylabel('Posizione [cm]')
plt.axis([0.0, 10.0, 0.0, None])

# Perform the actual fit and get the best-fit parameters.
popt, pcov = curve_fit(fit_model, t, s, sigma=sigma_s)
m_hat, q_hat = popt
sigma_m, sigma_q = np.sqrt(pcov.diagonal())
# Note the string formatting for the significant digits.
print(f'm = {m_hat:.2f} +- {sigma_m:.2f}')
print(f'q = {q_hat:.2f} +- {sigma_q:.2f}')
# Overlay the best-fit model.
x = np.linspace(0.0, 10.0, 100)
plt.plot(x, fit_model(x, m_hat, q_hat))
