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

EVEREST_ALT = 8.85
BALLOON_ALT = 30.
ISS_ALT = 408.

# Data from https://ccmc.gsfc.nasa.gov/modelweb/models/nrlmsise00.php
height, density, temperature = mpl_.load_file('atmosfera_pisa.txt', unpack=True)
sigma = 0.01 * density

plt.figure('atmosfera_densita')
plt.plot(height, density)
popt, pcov = fit_exponential(height, density, sigma, xmax=100., p0=(1.e-3, -5.))
plt.plot(height, exponential(height, *popt), ls='dashed', color='gray')
mpl_.annotation(f'ISS ({ISS_ALT:.0f} km)', (ISS_ALT, 1.e-15), (300., 1.e-12))
mpl_.setup_gca(xlabel='Altitudine [km]', ylabel='Densità atmosferica [g cm$^{-3}$]',
    xmax=450., ymin=1.e-16, ymax=2.e-3, logy=True, grids=True, yticks=np.logspace(-16., -2., 15))
# Setup the zoom.
axins = plt.gca().inset_axes([0.5, 0.5, 0.47, 0.47])
x1, x2, y1, y2 = 0., 45., 1.e-6, 2.e-3
axins.set_xlim(x1, x2)
axins.set_ylim(y1, y2)
axins.plot(height, density)
axins.set_yscale('log')
axins.grid(which='both')
plt.gca().indicate_inset_zoom(axins, edgecolor='black', alpha=1.)

plt.figure('atmosfera_temperatura')
plt.plot(height, temperature)
mpl_.setup_gca(xlabel='Altitudine [km]', ylabel='Tempreratura atmosferica [$^\\circ$K]',
    xmax=450., grids=True)

mpl_.save_all_figures()
