import numpy as np
import scipy.stats

mu = 2.
k = np.linspace(0, 3, 4, dtype=int)
print(k)
print(scipy.stats.poisson(mu).pmf(k))
