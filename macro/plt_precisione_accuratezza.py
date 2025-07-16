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
import scipy.stats

import matplotlib_ as mpl_

def _plot(mu, sigma, label1, label2, xmin=-6., xmax=6.):
    x = np.linspace(xmin, xmax, 250)
    y = scipy.stats.norm.pdf(x, mu, sigma)
    plt.plot(x, y)
    ymax = 2. / np.sqrt(2. * np.pi) / sigma
    mpl_.setup_gca(xticks=[], yticks=[], ymin=0., ymax=ymax)
    mpl_.annotation('misurando', (0, 0.), (0, 0.7 * ymax), style='angle')
    mpl_.axtext(0.08, 0.90, label1)
    mpl_.axtext(0.08, 0.82, label2)
    plt.tight_layout()

plt.figure('precisione_accuratezza_1')
_plot(0.0, 0.2, 'Buona accuratezza', 'Buona precisione')

plt.figure('precisione_accuratezza_2')
_plot(0.0, 1.2, 'Buona accuratezza', 'Scarsa precisione')

plt.figure('precisione_accuratezza_3')
_plot(2.5, 0.2, 'Scarsa accuratezza', 'Buona precisione')

plt.figure('precisione_accuratezza_4')
_plot(2.5, 1.2, 'Scarsa accuratezza', 'Scarsa precisione')

plt.figure('errore_stat_sys')
n = np.linspace(0, 200, 100)
stat_err = 1. / np.sqrt(n)
sys_err = np.full(n.shape, 0.2)
tot_err = np.sqrt(stat_err**2. + sys_err**2.)
plt.plot(n, stat_err, ls='dashed', color='black', label='Incertezza statistica')
plt.plot(n, sys_err, ls='dotted', color='black', label='Incertezza sistematica')
plt.plot(n, tot_err, color='black', label='Incertezza totale')
mpl_.setup_gca(xticks=[], yticks=[], xlabel='Numero di misure', ylabel='Incertezza', legend=True)

mpl_.save_all_figures()
