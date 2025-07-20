n = 49
m = 21

def gcd(n, m):
    """Calculate the greatest common divisor.
    """
    r = n % m
    while r != 0:
        m = n
        n = r
        r = n % m
    return n

print(gcd(49, 21))
