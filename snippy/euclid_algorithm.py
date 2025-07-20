n = 49
m = 21
r = n % m
while r != 0:
    m = n
    n = r
    r = n % m

print(n)
