import numpy as np

def lls(x, y, sigma_y):
    w = 1.0 / sigma_y**2.0
    Sx0 = np.sum(w)
    Sx1 = np.sum(w * x)
    Sx2 = np.sum(w * x**2.0)
    Sxy0 = np.sum(w * y)
    Sxy1 = np.sum(w * x * y)
    D = Sx0 * Sx2 - Sx1**2.0
    q_hat = (Sxy0 * Sx2 - Sxy1 * Sx1) / D
    sigma_q = np.sqrt(Sx2 / D)
    m_hat = (Sxy1 * Sx0 - Sxy0 * Sx1) / D
    sigma_m = np.sqrt(Sx0 / D)
    return q_hat, sigma_q, m_hat, sigma_m

x = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
y = np.array([10.42, 10.96, 14.50, 16.58, 19.41])
sigma_y = np.full(y.shape, 0.50)
q_hat, sigma_q, m_hat, sigma_m = lls(x, y, sigma_y)
print(f'q = {q_hat:.2f} +/- {sigma_q:.2f}')
print(f'm = {m_hat:.2f} +/- {sigma_m:.2f}')
