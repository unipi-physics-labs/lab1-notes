import scipy.special

n = 100
k = 40
print(scipy.special.comb(n, k))
print(scipy.special.comb(n, k, exact=True))
