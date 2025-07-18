# Toy two-digit (0--99) linear congruential generator.
a = 11
c = 3
m = 73
x = 81

# Generate 10 numbers.
sequence = []
for i in range(10):
    x = (a * x + c) % m
    sequence.append(x)

print(sequence)
