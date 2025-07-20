import numpy as np
from scipy.special import erf

def Phi(z):
    """ Gaussian cumulative function.
    """
    return 0.5 + 0.5 * erf(z / np.sqrt(2.0))

def integrate_gauss(x1, x2, mu=0.0, sigma=1.0):
    """Integrate a generic gaussian between x1 and x2.
    """
    z1 = (x1 - mu) / sigma
    z2 = (x2 - mu) / sigma
    return Phi(z2) - Phi(z1)

print(integrate_gauss(-1.0, 1.0))
print(integrate_gauss(22.0, 24.0, 20.0, 4.0))
