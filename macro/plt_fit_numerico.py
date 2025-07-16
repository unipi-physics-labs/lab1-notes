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
from scipy.optimize import curve_fit

import matplotlib_ as mpl_

np.random.seed(100)


n = 20
omega = 1.2
xmin, xmax = 1., 19.
sigma_y = 0.05


def f(x, omega):
    """Fit function.
    """
    return np.sin(omega * x)

x = np.linspace(xmin, xmax, n)
y = np.sin(omega * x) + np.random.normal(0, sigma_y, size=n)
sigma_y = np.full(y.shape, sigma_y)

popt, pcov = curve_fit(f, x, y, sigma=sigma_y)
omega = popt[0]
domega = np.sqrt(pcov[0, 0])
print(omega, domega)

chisq = (((y - f(x, *popt)) / sigma_y)**2.).sum()
print(chisq)

fig, frame1, frame2 = mpl_.residual_figure('fit_numerico_seno')
mpl_.scatter(x, y, sigma_y, ylabel='$y$~[m]', grids=True)
_x = np.linspace(0., 20., 100)
mpl_.curve(_x, f(_x, omega), ymin=-1.25, ymax=1.25)
plt.sca(frame2)
mpl_.scatter(x, y - f(x, *popt), sigma_y, xlabel='$t$~[s]', ymin=-0.2, ymax=0.2,
    yticks=[-0.2, -0.1, 0, 0.1, 0.2], grids=True, ylabel='Residui [m]')

plt.figure('fit_numerico_seno_chisq')
_x = []
_y = []
for _omega in np.linspace(0, 10, 500):
    _chi2 = (((y - f(x, _omega)) / sigma_y)**2.).sum()
    _x.append(_omega)
    _y.append(_chi2)
mpl_.curve(_x, _y, xlabel='$\omega$', ylabel='$\chi^2(\omega)$', ymin=10, logy=True, grids=True)

fig, frame1, frame2 = mpl_.residual_figure('fit_numerico_errato')
popt, pcov = curve_fit(f, x, y, 3.2, sigma_y)
omega = popt
domega = np.sqrt(pcov)
print(omega, domega)
chisq = (((y - f(x, *popt)) / sigma_y)**2.).sum()
print(chisq)
mpl_.scatter(x, y, sigma_y, ylabel='$y$~[m]', grids=True)
_x = np.linspace(0, 20, 300)
mpl_.curve(_x, f(_x, omega), ymin=-1.25, ymax=1.25)
plt.sca(frame2)
mpl_.scatter(x, y - f(x, *popt), sigma_y, xlabel='$t$~[s]', grids=True,
    ymin=-1.5, ymax=1.5, yticks=[-1., 0., 1.])

mpl_.save_all_figures()