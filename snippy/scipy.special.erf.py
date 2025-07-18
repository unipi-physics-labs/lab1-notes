import numpy as np
import scipy.special

for z0 in [1.0, 2.0, 3.0]:
    P = scipy.special.erf(z0 / np.sqrt(2.0))
    print(f'{z0} -> {P}')
