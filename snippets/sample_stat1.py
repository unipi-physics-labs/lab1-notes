import numpy as np

def sample_statistics(values):
    n = len(values)
    # First loop to calculate the mean.
    mean = 0.0
    for x in values:
        mean = mean + x
    mean /= n
    # Second loop to calculate the variance.
    stdev = 0.0
    for x in values:
        stdev = stdev + (x - mean)**2.
    stdev = np.sqrt(stdev / (n - 1))
    return mean, stdev

# Quick test with normally-distributed random numbers.
np.random.seed(1)
values = np.random.normal(0.0, 1.0, size=10000)
print(sample_statistics(values))
