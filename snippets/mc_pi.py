import random
random.seed(1)

# Initialize the counters.
n_q = 1000000
n_c = 0
# Extract a number of random points...
for i in range(n_q):
    x = random.uniform(0.0, 1.0)
    y = random.uniform(0.0, 1.0)
    #  ...and check if they lie in the circle.
    if (x**2.0 + y**2.0 <= 1.0):
        n_c = n_c + 1
# Estimate pi and print it.
pi = 4.0 * n_c / n_q
print(pi)
