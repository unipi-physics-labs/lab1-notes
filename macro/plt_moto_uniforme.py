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

import os

from matplotlib import pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

import matplotlib_ as mpl_

np.random.seed(666)

tmin = 1.
tmax = 9.
x0 = 12.0
v0 = 7.5
dx = 2.5

def position(t):
    """Return the position at a given time.
    """
    return x0 + v0 * t

def generate(num_points=9):
    """Generate a series of measured points---note the errors are uniform.
    """
    t = np.linspace(tmin, tmax, num_points)
    x = position(t) + np.random.uniform(-dx, dx, size=num_points)
    return t, x

def write_table(x, y, dy, file_name):
    """This should be moved to a helper function.
    """
    file_path = os.path.join(mpl_.TABLE_FOLDER, file_name)
    f = open(file_path, 'w')
    for _x, _y in zip(x, y):
        f.write('$%.3f$ & $%.1f \\pm %.1f$ \\\\\n' % (_x, _y, dy))
    f.close()

def _plot():
    """Plot the data.
    """
    mpl_.errorbar(t, x, dx)
    mpl_.setup_gca(xmin=tmin - 1., xmax=tmax + 1., ymin=0., ymax=90., xlabel='Tempo [s]',
        ylabel='Posizione [cm]', grids=True)

t, x = generate()
tgrid = np.linspace(tmin - 1., tmax + 1., 100)
write_table(t, x, dx, 'moto_uniforme_dati.tex')

def line(x, m, q):
    """Linear fit model.
    """
    return m * x + q

plt.figure('moto_uniforme_dati')
_plot()

plt.figure('moto_uniforme_fit')
_plot()
popt, pcov = curve_fit(line, t, x)
plt.plot(tgrid, line(tgrid, *popt))

mpl_.save_all_figures()
