import scipy.stats

mu = 0.0
sigma = 1.0
z = scipy.stats.norm(mu, sigma)
print(z.pdf(0.0))
for z0 in [1.0, 2.0, 3.0]:
    P = z.cdf(z0) - z.cdf(-z0)
    print(f'{z0} -> {P}')
