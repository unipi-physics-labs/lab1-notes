#!/usr/bin/env python
#
# Copyright (C) 2021, Luca Baldini (luca.baldini@pi.infn.it).
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


def catenary(x, a, c, x0):
    """Catenary definition.
    """
    return c + a * np.cosh((x - x0) / a)

def catenary_derivative(x, a, c, x0):
    """Catenary derivative.
    """
    return np.sinh((x - x0) / a)

# Read the data from file---mind we reverse the y coordinate.
x, y = mpl_.load_file('catenary.csv', unpack=True, delimiter=',')
y = y.max() - y

# Fit the data with a catenary: first pass...
sigma = 1.
p0 = (100.0, 0.0, 2300.0)
popt, pcov = curve_fit(catenary, x, y, p0=p0)
# ... and second pass with the effective errors.
sigma_eff = sigma * np.sqrt(1. + catenary_derivative(x, *popt)**2.0)
popt, pcov = curve_fit(catenary, x, y, p0=popt, sigma=sigma_eff)
chisq = (((y - catenary(x, *popt)) / sigma_eff)**2.0).sum()
dof = len(y) - 3

fig, ax1, ax2 = mpl_.residual_figure('fit_catenaria')
mpl_.scatter(x, y, ylabel='$y$ [pixel]', grids=True)
mpl_.curve(x, catenary(x, *popt))
mpl_.chisq_text(0.5, 0.75, chisq, dof)
plt.sca(ax2)
axfmt = dict(xlabel='$x$ [pixel]', ylabel='Residui [pixel]', grids=True, ymin=-29.0, ymax=29.0)
mpl_.scatter(x, y - catenary(x, *popt), sigma_eff, **axfmt)

mpl_.save_all_figures()
