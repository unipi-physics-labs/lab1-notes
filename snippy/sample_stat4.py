import numpy as np

def sample_statistics(values):
    # Using native numpy functions.
    mean = values.mean()
    stdev = values.std(ddof=1)
    return mean, stdev

# Quick test with normally-distributed random numbers.
np.random.seed(1)
values = np.random.normal(0.0, 1.0, size=10000)
print(sample_statistics(values))
# And now add 1,000,000 to all the values in the sample.
values = values + 1.0e9
print(sample_statistics(values))
