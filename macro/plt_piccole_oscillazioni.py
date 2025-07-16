#!/usr/bin/env python
#
# Copyright (C) 2015-2021, Luca Baldini (luca.baldini@pi.infn.it).
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

def period_expansion(x):
    """Return the Taylor expansion of the pendulum period up to the 6-th order.
    """
    x = np.radians(x)
    v0 = np.full(x.shape, 1.)
    v2 = v0 + 1. / 16. * x**2.
    v4 = v2 + 11. / 3172. * x**4.
    v6 = v4 + 173. / 737280. * x**6
    return v0, v2, v4, v6

plt.figure('piccole_oscillazioni')
x = np.linspace(0, 90, 100)
y0, y2, y4, y6 = period_expansion(x)
fmt = dict(ls='dashed', color='gray', lw=0.75)
plt.plot(x, y0, **fmt)
plt.plot(x, y2, **fmt)
plt.plot(x, y4, **fmt)
plt.plot(x, y6, color='black')
mpl_.setup_gca(xmin=0., xmax=98.5, ymin=0.99, ymax=1.20, xlabel='$\\theta_0$ [$^\circ$]',
    ylabel='$T(\\theta_0)/T_0$', grids=True)
plt.text(45, 1.01, 'piccole oscillazioni')
_x = x[-1] + 1.5
fmt = dict(ha='left', va='center')
plt.text(_x, y0[-1], '1', **fmt)
plt.text(_x, y2[-1], '$\\theta_0^2$', **fmt)
plt.text(_x, y4[-1], '$\\theta_0^4$', **fmt)

plt.figure('piccole_oscillazioni_log')
x = np.geomspace(0.1, 90., 100)
y0, y2, y4, y6 = period_expansion(x)
plt.plot(x, y6 - y0, color='black')
mpl_.setup_gca(xlabel='$\\theta_0$ [$^\circ$]', ylabel='$\\delta(\\theta_0)$', logx=True,
    logy=True, grids=True)

mpl_.save_all_figures()
