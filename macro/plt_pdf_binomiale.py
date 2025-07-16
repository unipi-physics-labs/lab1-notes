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


from matplotlib_ import *

import numpy as np

import scipy.stats


def plot_binomial(n, p):
    """
    """
    x = np.arange(0, n + 1)
    y = scipy.stats.binom.pmf(x, n, p)
    bar_plot(x, y, width=11./50)
    plt.axis([-0.5, 10.5, 0., 0.6])
    plt.xlabel('$k$')
    plt.ylabel('$\\mathcal{B}(k)$')
    mu = n*p
    sigma = np.sqrt(n*p*(1 - p))
    annotation('$\\mu$', (mu, 0.), (mu, 0.5), style='angle')
    annotation('$\\mu + \\sigma$', (mu + sigma, 0.), (mu + sigma, 0.42),
               style='angle')

for i, (n, p, l) in enumerate([(4, 1./6, '1/6'),
                               (4, 1./2, '1/2'),
                               (10, 1./6, '1/6'),
                               (10, 1./2, '1/2')]):
    plt.figure()
    plot_binomial(n, p)
    x = 7.75
    plt.text(x, 0.52, '$n = %d$' % n)
    plt.text(x, 0.47, '$p = %s$' % l)
    save_current_figure('pdf_binomiale_%d.pgf' % (i + 1))

show_figures()
