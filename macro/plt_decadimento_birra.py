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

# Data from https://www.tf.uni-kiel.de/matwis/amat/elmat_en/articles/beer_decay/beer_article.pdf
t = np.array([0., 15., 30., 45., 60., 75., 90., 105., 120., 150., 180., 210., 240., 300., 360.])
h = np.array([14., 11.8, 10.5, 9.3, 8.5, 7.7, 7.1, 6.5, 6., 5.3, 4.4, 3.5, 2.9, 1.3, 0.7])
sigma_h = np.array([0.01, 0.3, 0.3, 0.5, 0.6, 0.6, 0.7, 0.8, 0.8, 1.1, 1.2, 0.9, 1.1, 0.7, 0.5])
tgrid = np.linspace(0., 400., 100)

plt.figure('decadimento_birra')
plt.errorbar(t, h, sigma_h, fmt='o')
popt, pcov = fit_exponential(t, h, sigma_h, p0=(15., -100.))
plt.plot(tgrid, exponential(tgrid, *popt), ls='dashed', color='gray')
mpl_.setup_gca(logy=True, grids=True, ymin=0.5, xlabel='Tempo [s]', ylabel='Altezza della schiuma [cm]')
