#!/usr/bin/env python
#
# Copyright (C) 2016, Luca Baldini (luca.baldini@pi.infn.it).
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
import scipy.special

from matplotlib_ import *


mu = 100


for k in range(80, 121, 5):
    p = scipy.stats.poisson(mu).pmf(k)
    g = scipy.stats.norm(mu, mu**0.5).pdf(k)
    delta = abs(p - g)/p
    text = '$%d$&$%.3e$&$%.3e$&$%.2e$\\\\' % (k, p, g, delta)
    text = text.replace('e-0', '\\times 10^{-')
    text = text.replace('-2$', '-2}$').replace('-3$', '-3}$').replace('-4$', '-4}$')

def draw(mu, kmin, kmax, fileName):
    """
    """
    fig = plt.figure()
    k = np.arange(kmin, kmax, 1)
    p = scipy.stats.poisson(mu).pmf(k)
    x = np.linspace(kmin, kmax, 100)
    g = scipy.stats.norm(mu, mu**0.5).pdf(x)
    bar_plot(k, p, width = 0.3)
    plt.plot(x, g)
    plt.axis([kmin, kmax, None, None])
    plt.xlabel('k')
    plt.text(0.75, 0.85, '$\mu = %d$' % mu, transform=plt.gca().transAxes)
    save_current_figure(fileName)
    return fig

draw(5, 0, 15, 'poisson_gauss1.pgf')
draw(100, 60, 140, 'poisson_gauss2.pgf')

# Answer to one of the examples.
mu = 1000
sigma = np.sqrt(mu)
kmin = 950
kmax = 1022
k = np.arange(kmin, kmax + 1, 1)
p = scipy.stats.poisson(mu).pmf(k).sum()
print(p)
zmin = (kmin - 0.5 - mu)/sigma
zmax = (kmax + 0.5 - mu)/sigma
pg = 0.5*scipy.special.erf((zmax) / np.sqrt(2.)) - 0.5*scipy.special.erf((zmin) / np.sqrt(2.))
print(zmin, zmax, pg)
print(p/pg)



show_figures()
