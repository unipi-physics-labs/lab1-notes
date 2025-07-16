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

from matplotlib_ import *


def plot_uniform(a, b, annotate=True):
    """
    """
    h = 1. / (b - a)
    x = np.array([a, a, b, b])
    y = np.array([0, h, h, 0])
    plt.plot(x, y)
    plt.axis([-0.1, 1.1, 0., 1.5])
    plt.xlabel('$x$')
    if annotate:
        plt.ylabel('$u(x; %d, %d)$' % (a, b))
        mu = 0.5*(a + b)
        sigma = (b - a)/np.sqrt(12)
        annotation('$\\mu$', (mu, 0.), (mu, 1.3), style='angle')
        annotation('$\\mu + \\sigma$', (mu + sigma, 0.), (mu + sigma, 1.3), style='angle')
    else:
        plt.ylabel('$p(x)$')

plt.figure()
plot_uniform(0, 1)
save_current_figure('pdf_uniforme.pgf')

plt.figure()
plot_uniform(0, 1, False)
x1 = 0.22
x2 = 0.35
plt.gca().fill_between(np.array([x1, x2]), 0, 1, facecolor='gray', alpha=0.5)
line(x1, 0, x1, 1, linewidth=0.75)
line(x2, 0, x2, 1, linewidth=0.75)
plt.text(x1, 1.05, '$x_1$', horizontalalignment='center')
plt.text(x2, 1.05, '$x_2$', horizontalalignment='center')
annotation('$P(x_1 \leq x \leq x_2) = \int_{x_1}^{x_2} p(x)dx$',
           (0.5*(x1 + x2), 1), (0.72, 1.25), color='black')
save_current_figure('pdf_esempio_uniforme.pgf')

plt.figure()
mu = 0.5
sigma = (1. / 12.)**0.5
plot_uniform(0, 1, False)
annotation('$\\mu$', (mu, 0.), (mu, 1.3), style='angle')
annotation('$\\mu + \\sigma$', (mu + sigma, 0.), (mu + sigma, 1.3), style='angle')
annotation('$\\mu - \\sigma$', (mu - sigma, 0.), (mu - sigma, 1.3), style='angle')
save_current_figure('pdf_uniforme_mean_std.pgf')

show_figures()
