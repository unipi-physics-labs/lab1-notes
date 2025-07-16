#!/usr/bin/env python
#
# Copyright (C) 2015, Luca Baldini (luca.baldini@pi.infn.it).
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

# Set the numpy random seed to get reproducible results.
np.random.seed(100)


# Parameter definition for simluated data.
n = 16
xmin, xmax = 0.5, 9.5
sigma_y = np.full(n, 10.)
l0 = 2.5
m0 = 4.
q0 = 50.
N = 16

def quadratic_model(x, l, m, q):
    """Quadratico model.
    """
    return l * x**2. + m * x + q

def linear_model(x, m, q):
    """Linear model.
    """
    return m * x + q

def polinomial_model(x, *pars):
    """Polynomial model.
    """
    val = 0.0
    for i, par in enumerate(pars):
        exponent = len(pars) - i - 1.0
        val += par * (x**exponent)
    return val

# Generate the data points according to a quadratic model.
x = np.linspace(xmin, xmax, n)
y = quadratic_model(x,  l0, m0, q0) + np.random.normal(0.0, sigma_y, size=n)
xgrid = np.linspace(xmin, xmax, 100)


def _plot(dy, model, num_params):
    """Convenience function to plot the data and fit with a given model.
    """
    mpl_.scatter(x, y, dy, xlabel='$x$~[u.a.]', ylabel='$y$~[u.a.]', xmin=0.0, xmax=10.0)
    popt, pcov = curve_fit(model, x, y, p0=[1.] * num_params, sigma=dy)
    mpl_.curve(xgrid, model(xgrid, *popt))
    zeta = (y - model(x, *popt)) / dy
    chisq = (zeta**2.0).sum()
    dof = n - num_params
    mpl_.chisq_text(0.7, 0.15, chisq, dof)
    return zeta


plt.figure('chi2_test_ok')
zeta = _plot(sigma_y, quadratic_model, 3)
# Loop over the data points and label them with the contribution to the chisquare.
fmt = dict(ha='center', size=6)
for _x, _y, _dy, _z in zip(x, y, sigma_y, zeta):
    delta = 1.2 * _dy
    text = f'${_z**2.:.2f}$'
    if _z > 0:
        plt.text(_x, _y + delta, text, va='bottom', **fmt)
    else:
        plt.text(_x, _y - delta, text, va='top', **fmt)

plt.figure('chi2_test_modello_cattivo')
_plot(sigma_y, linear_model, 2)
mpl_.axtext(0.1, 0.85, 'Modello inadeguato')

plt.figure('chi2_test_errori_sottostimati')
_plot(0.4 * sigma_y, quadratic_model, 3)
mpl_.axtext(0.1, 0.85, 'Errori sottostimati')

plt.figure('chi2_test_errori_sovrastimati')
_plot(2.5 * sigma_y, quadratic_model, 3)
mpl_.axtext(0.1, 0.85, 'Errori sovrastimati')

plt.figure('chi2_test_overfitting')
_plot(sigma_y, polinomial_model, 5)
mpl_.axtext(0.1, 0.85, 'Overfitting?')

fig, ax1, ax2 = mpl_.residual_figure('chi2_test_residui')
mpl_.scatter(x, y, sigma_y, ylabel='$y$~[u.a.]', grids=True)
popt, pcov = curve_fit(quadratic_model, x, y, sigma=sigma_y)
mpl_.curve(xgrid, quadratic_model(xgrid, *popt))
plt.sca(ax2)
mpl_.scatter(x, y - quadratic_model(x, *popt), sigma_y, xlabel='$x$~[u.a.]',
    ylabel='Residui [u.a.]', ymin=-27.5, ymax=27.5, grids=True)

mpl_.save_all_figures()
