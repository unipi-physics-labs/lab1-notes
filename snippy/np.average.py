import numpy as np

x = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
w = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]
m = np.average(x, weights=w)
print(m)
