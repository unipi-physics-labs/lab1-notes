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

names = ['Mercurio', 'Venere', 'Terra', 'Marte', 'Giove', 'Saturno', 'Urano', 'Nettuno']
semiaxes = [0.3870993, 0.723336, 1.000003, 1.52371, 5.2029, 9.537, 19.189, 30.0699]
periods = [0.2408467, 0.61519726, 1.0000174, 1.8808158, 11.862615, 29.447498, 84.016846, 164.79132]

def _plot(xmin, xmax, ymin, ymax, start_planet=0, loglog=False):
    """Plot the data.
    """
    mpl_.errorbar(semiaxes, periods)
    mpl_.setup_gca(xmin=xmin, xmax=xmax, ymin=ymin, ymax=ymax, xlabel='Semiasse maggiore dell\'orbita [U.A.]',
        ylabel='Periodo di rivoluzione [anni]', grids=True, logx=loglog, logy=loglog)
    for i, (n, s, p) in enumerate(zip(names, semiaxes, periods)):
        if i >= start_planet:
            if loglog:
                y = 1.15 * p
            else:
                y = p + 4.
            plt.text(s, y, n, size=8, ha='center', va='bottom')

plt.figure('sistema_solare_lin')
_plot(0., 35, 0., 200., start_planet=4)

plt.figure('sistema_solare_log')
_plot(0.1, 100., 0.1, 1000., loglog=True)
x = np.geomspace(0.1, 100., 100)
y = x**1.5
plt.plot(x, y, color=mpl_.LIGHT_GRAY, lw=mpl_.QUOTE_LW)

mpl_.save_all_figures()
