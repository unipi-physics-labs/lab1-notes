# Real (i.e., usable) linear congruential generator.
a = 6364136223846793005
c = 1442695040888963407
m = 2**64
x = 1

# Generate 10 number between 0 and 1.
for i in range(10):
    x = (a * x + c) % m
    u = float(x) / (m - 1)
    print(u)
