import random
random.seed(1)

# Setup the simulation.
pos = 0.0
step = 1.0
path = [pos]
# Loop through the Galton box.
for i in range(10):
    r = random.uniform(0.0, 1.0)
    if r <= 0.5:
        pos = pos - step
    else:
        pos = pos + step
    path.append(pos)
# Print the actual path.
print(path)
