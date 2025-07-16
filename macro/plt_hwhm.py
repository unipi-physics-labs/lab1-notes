#!/usr/bin/env python
#
# Copyright (C) 2016, Luca Baldini (luca.baldini@pi.infn.it).
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
from scipy.interpolate import InterpolatedUnivariateSpline

import matplotlib_ as mpl_


def prob(x):
    """
    """
    return x*(1 - x)/(1 + x)


plt.figure('hwhm')
x = np.linspace(0, 1, 100)
y = prob(x)
# Lazy...
spl = InterpolatedUnivariateSpline(x, y)
y /= spl.integral(0., 1.)
ymax = max(y)
xa = 0.105
xb = 0.805
mpl_.curve(x, y, xlabel='$x$', ylabel='$p(x)$', ymin=0.)
mpl_.horizontal_quote(0.5*ymax, xa, xb, '\\textsc{FWHM}')
mpl_.vertical_quote(xa, 0, 0.5*ymax, '$x_a$')
mpl_.vertical_quote(xb, 0, 0.5*ymax, '$x_b$')
mpl_.horizontal_quote(0.35 * ymax, xa, 0.5 * (xa + xb), '\\textsc{HWHM}')

mpl_.save_all_figures()