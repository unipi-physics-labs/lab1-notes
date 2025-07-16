# Define m and p, and initialize an empty list.
m = 11
p = 7
sequence = []
# Calculate k^p mod m for all positive k < m.
# Note ** is the power and % the modulo operator.
for k in range(m):
    sequence.append(k**p % m)
# Print the sequence.
print(sequence)
