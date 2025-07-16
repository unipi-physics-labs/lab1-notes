import numpy as np

def weighted_average(y, sigma_y):
    """Implementation of the weighted average using numpy.
    """
    w = 1.0 / sigma_y**2.0
    q_hat = np.average(y, weights=w)
    sigma_q = np.sqrt(1.0 / np.sum(w))
    return q_hat, sigma_q

n = np.array([1.325, 1.36, 1.32, 1.338, 1.335])
sigma_n = np.array([0.012, 0.05, 0.01, 0.005, 0.006])
q_hat, sigma_q = weighted_average(n, sigma_n)
print(f'q = {q_hat:.4f} +/- {sigma_q:.4f}')
