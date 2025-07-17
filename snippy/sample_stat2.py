import numpy as np

def sample_statistics(values):
    n = len(values)
    # Calculate mean and standard deviation in one loop.
    mean = stdev = 0.0
    for x in values:
        mean = mean + x
        stdev = stdev + x**2.0
    mean /= n
    stdev = np.sqrt((stdev - n * mean**2.0) / (n - 1))
    return mean, stdev

# Quick test with normally-distributed random numbers.
np.random.seed(1)
values = np.random.normal(0.0, 1.0, size=10000)
print(sample_statistics(values))
# And now add 1,000,000.0 to all the values in the sample.
values = values + 1.0e9
print(sample_statistics(values))
