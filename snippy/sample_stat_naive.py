import numpy as np

def sample_stats(sample):
    n = len(sample)
    mean = 0.0
    stdev = 0.0
    for x in sample:
        mean = mean + x
    mean /= n
    for x in sample:
        stdev = stdev + (x - mean)**2.
    stdev = np.sqrt(stdev / (n - 1))
    return mean, stdev

x = [2.53, 2.58, 2.28, 2.41, 2.61, 2.87, 2.40, 2.38, 2.34]
print(sample_stats(x))
