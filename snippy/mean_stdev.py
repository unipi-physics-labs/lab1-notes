import numpy as np

# Input data.
T = [2.12, 2.22, 2.16, 2.10, 2.15]
# Calculation of basic metrics.
n = len(T)
mean = np.mean(T)
stdevm = np.std(T, ddof=1) / np.sqrt(n)
max_err = (max(T) - min(T)) / 2.0
# Print out stuff...
print(f'n = {n}')
print(f'mean = {mean:.2f}')
print(f'sigma = {stdevm:.2f}')
print(f'max_err = {max_err:.2f}')
