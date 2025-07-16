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

import matplotlib_ as mpl_

tstart = 10.
tstop = 50.

t, T1, T2 = mpl_.load_file('temperatura_newton.txt', unpack=True)
mask = (t >= tstart) * (t <= tstop)
t = t[mask]
T1 = T1[mask]
T2 = T2[mask]

t -= tstart
T1 -= 2.3

def fit_function(t):
    """Hard-coded fit function.
    """
    return 20. * np.exp(-0.105 * t)

def _plot(**kwargs):
    """Plot the data.
    """
    mpl_.errorbar(t, T1)
    mpl_.setup_gca(xlabel='Tempo [s]', ylabel='Temperatura [$^\\circ$C]', xmin=0.,
        xmax=40., grids=True, **kwargs)

plt.figure('temperatura_newton_lin')
_plot(ymin=0., ymax=25.)

plt.figure('temperatura_newton_log')
_plot(ymin=0.1, ymax=100., logy=True)
plt.plot(t, fit_function(t), color='gray', zorder=10)

mpl_.save_all_figures()
