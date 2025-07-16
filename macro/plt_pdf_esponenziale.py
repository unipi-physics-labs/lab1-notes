#!/usr/bin/env python
#
# Copyright (C) 2015--2016, Luca Baldini (luca.baldini@pi.infn.it).
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


def plot_exp(_lambda):
    """
    """
    x = np.linspace(0, 5, 100)
    y = _lambda*np.exp(-x * _lambda)
    x = np.append(0., x)
    y = np.append(0., y)
    plt.plot(x, y)
    plt.axis([-0.25, 5, 0., 2.5])
    plt.xlabel('$x$')
    plt.ylabel('$\\varepsilon(x; %d)$' % (_lambda))
    mu = sigma = 1. / _lambda
    annotation('$\\mu$', (mu, 0.), (mu, 1.3), style='angle')
    annotation('$\\mu + \\sigma$', (mu + sigma, 0.), (mu + sigma, 1.), style='angle')
    plt.text(0.75, 0.85, '$\lambda = %.1f$' % _lambda,
             transform=plt.gca().transAxes)

for i, _lambda in enumerate([1., 2.]):
    plt.figure()
    plot_exp(_lambda)
    save_current_figure('pdf_esponenziale_%d.pgf' % (i + 1))

# Cumulative distribution and percent point function for a given value of lambda
_lambda = 1
x = np.linspace(0., 5.*_lambda, 100)
q = np.linspace(0., 1., 100)
cdf = 1 - np.exp(-_lambda*x)
ppf = -np.log(1 - q) / _lambda

plt.figure()
plt.plot(x, cdf)
plt.xlabel('$x$')
plt.ylabel('$F(x)$')
plt.text(0.1, 0.85, '$\lambda = %.1f$' % _lambda, transform=plt.gca().transAxes)
save_current_figure('cdf_esponenziale.pgf')

plt.figure()
plt.plot(q, ppf)
plt.xlabel('$q$')
plt.ylabel('$F^{-1}(q)$')
plt.text(0.1, 0.85, '$\lambda = %.1f$' % _lambda, transform=plt.gca().transAxes)
save_current_figure('ppf_esponenziale.pgf')


show_figures()
