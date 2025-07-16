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

# Define some data points.
x = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
y = np.array([0.112, 0.202, 0.299, 0.393, 0.512])
dy = np.full(y.shape, 0.01)

def f(x, m):
    """Fit model.
    """
    return m * x

# Fit with a straight line.
popt, pcov = curve_fit(f, x, y)

axfmt = dict(xlabel='$x$ [a. u.]', ylabel='$y$ [a. u.]')

plt.figure('absolute_sigma')
mpl_.scatter(x, y, dy, **axfmt)
mpl_.curve(x, f(x, *popt))

plt.figure('absolute_sigma_noerr')
mpl_.scatter(x, y, 1., **axfmt)
mpl_.curve(x, f(x, *popt))

mpl_.save_all_figures()
