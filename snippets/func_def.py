import numpy as np

def sum_err_prop(x, sigma_x, y, sigma_y):
    """Error propagation on the addition operation.
    """
    s_hat = x + y
    sigma_s = np.sqrt(sigma_x**2.0 + sigma_y**2.0)
    return s_hat, sigma_s

s_hat, sigma_s = sum_err_prop(1.0, 0.01, 2.0, 0.02)
print(f's = {s_hat:.3f} +/- {sigma_s:.3f}')
s_hat, sigma_s = sum_err_prop(1.0, 0.01, 14.0, 0.2)
print(f's = {s_hat:.2f} +/- {sigma_s:.2f}')
