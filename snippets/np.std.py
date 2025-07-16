import numpy as np

x = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
m = np.std(x)
print(m)
m = np.std(x, ddof=1)
print(m)
