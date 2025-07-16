import numpy as np

x = [2.53, 2.58, 2.28, 2.41, 2.61, 2.87, 2.40, 2.38, 2.34]

mean = np.mean(x)
stdev = np.std(x, ddof=1)

print(mean, stdev)
