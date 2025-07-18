# Middle-square random number generator with m = 4.
# Define the seed and print it out.
x = 3333
sequence = [x]
# Generate 10 numbers---note 10^{m/2} = 100 and 10^m = 10000.
for n in range(10):
    x = (x**2 // 100) % 10000
    sequence.append(x)
# Print the sequence.
print(sequence)
