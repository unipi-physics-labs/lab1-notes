import numpy as np

def sample_stats(sample):
    n = mean = stdev = 0.0
    for x in sample:
        n = n + 1
        delta = x - mean
        mean = mean + delta / n
        stdev = stdev + delta * (x - mean)
    stdev = np.sqrt(stdev / (n - 1))
    return mean, stdev

x = [2.53, 2.58, 2.28, 2.41, 2.61, 2.87, 2.40, 2.38, 2.34]
y = np.array(x) + 1.0e9

print(sample_stats(x))
print(sample_stats(y))
