#!/usr/bin/env python
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


# One die...
x = np.linspace(1.0, 6.0, 6)
y = np.full(6, 1. / 6.0)
mu = 3.5
sigma = np.sqrt(35. / 12.)

plt.figure('pdf_un_dado')
mpl_.bar(x, y, show_labels=True, labels=['1/6'] * 6)
mpl_.setup_gca(xlabel='$x$', ylabel='$P(x)$', xmin=0.5, xmax=6.5, ymin=0.0, ymax=0.2)

plt.figure('pdf_un_dado_media_std')
mpl_.bar(x, y)
mpl_.setup_gca(xlabel='$x$', ylabel='$P(x)$', xmin=0.5, xmax=6.5, ymin=0.0, ymax=0.25)
mpl_.annotation('$\\mu$', (mu, 0.), (mu, 0.20), style='angle')
mpl_.annotation('$\\mu + \\sigma$', (mu + sigma, 0.), (mu + sigma, 0.20), style='angle')
mpl_.annotation('$\\mu - \\sigma$', (mu - sigma, 0.), (mu - sigma, 0.20), style='angle')


# Two dice.
x = np.linspace(2.0, 12.0, 11)
y = []
l = []
for _x in x:
    _n = 6 - abs(7 - _x)
    y.append(_n / 36.)
    l.append(f'{_n:.0f}/36')
mu = 7.0
sigma = np.sqrt(70. / 12.)


plt.figure('pdf_somma_due_dadi')
mpl_.bar(x, y, show_labels=True, labels=l)
mpl_.setup_gca(xlabel='$x$', ylabel='$P(x)$', xmin=1.25, xmax=12.75, ymin=0.0, ymax=0.2)

plt.figure('pdf_somma_due_dadi_media_std')
mpl_.bar(x, y)
mpl_.setup_gca(xlabel='$x$', ylabel='$P(x)$', xmin=1.25, xmax=12.75, ymin=0.0, ymax=0.25)
mpl_.annotation('$\\mu$', (mu, 0.), (mu, 0.2), style='angle')
mpl_.annotation('$\\mu + \\sigma$', (mu + sigma, 0.), (mu + sigma, 0.2), style='angle')
mpl_.annotation('$\\mu - \\sigma$', (mu - sigma, 0.), (mu - sigma, 0.2), style='angle')

mpl_.save_all_figures()
