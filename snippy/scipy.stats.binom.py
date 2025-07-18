import numpy as np
import scipy.stats

n = 4
p = 0.1
k = np.linspace(0, n, n + 1, dtype=int)
print(k)
print(scipy.stats.binom(n, p).pmf(k))
