from math import factorial

def binomial(k, n, p):
    binom = factorial(n) / (factorial(k) * factorial(n - k))
    return binom * (p**k)*((1.0 - p)**(n - k))

for k in range(4):
    print(binomial(k, 4, 1.0 / 6.0))
