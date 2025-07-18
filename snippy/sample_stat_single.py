import numpy as np

def sample_stats(sample):
    n = len(sample)
    mean = stdev = 0.0
    for x in sample:
        mean = mean + x
        stdev = stdev + x**2.0
    mean /= n
    stdev = np.sqrt((stdev - n * mean**2.0) / (n - 1))
    return mean, stdev

x = [2.53, 2.58, 2.28, 2.41, 2.61, 2.87, 2.40, 2.38, 2.34]
y = np.array(x) + 1.0e9

print(sample_stats(x))
print(sample_stats(y))
