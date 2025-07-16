#!/usr/bin/env python
#
# Copyright (C) 2015--2021, Luca Baldini (luca.baldini@pi.infn.it).
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

from matplotlib import pyplot as plt
import numpy as np

import matplotlib_ as mpl_
from fit import exponential, fit_exponential


x_hat = 100.
sigma_x = 4.
y_hat = 50.
sigma_y = 3.
n = 1000000

sigma_A = np.sqrt(4. * (y_hat**2. * sigma_x**2. + x_hat**2. * sigma_y**2.) / (x_hat + y_hat)**4.)
print(sigma_A)

x = np.random.normal(x_hat, sigma_x, size=n)
y = np.random.normal(y_hat, sigma_y, size=n)
A = (x - y) / (x + y)
print(np.mean(A))
print(np.std(A, ddof=1))
