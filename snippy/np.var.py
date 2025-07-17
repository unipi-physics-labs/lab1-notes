import numpy as np

x = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
m = np.var(x)
print(m)
m = np.var(x, ddof=1)
print(m)
