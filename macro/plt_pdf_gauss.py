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


import numpy as np
import scipy.stats

from matplotlib_ import *


def plot_gauss(mu, sigma):
    """
    """
    x = np.linspace(-6, 6, 100)
    y = scipy.stats.norm.pdf(x, mu, sigma)
    plt.plot(x, y)
    plt.axis([-6, 6, 0., 0.6])
    plt.xlabel('$x$')
    plt.ylabel('$N(x; %d, %d)$' % (mu, sigma))
    annotation('$\\mu$', (mu, 0.), (mu, 0.5), style='angle')
    annotation('$\\mu + \\sigma$', (mu + sigma, 0.), (mu + sigma, 0.45),
               style='angle')

for i, (mu, sigma) in enumerate([(0, 1), (0, 2)]):
    plt.figure()
    plot_gauss(mu, sigma)
    save_current_figure('pdf_gauss_%d.pgf' % (i + 1))

show_figures()
