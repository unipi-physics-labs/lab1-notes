#!/usr/bin/env python
#
# Copyright (C) 2017, Luca Baldini (luca.baldini@pi.infn.it).
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

np.random.seed(666)


def uniform(n=1000000, num_vars=1, num_bins=81):
    """
    """
    mean = 0.
    var = num_vars/12.
    stdev = np.sqrt(var)
    x = np.zeros(n)
    for i in range(num_vars):
        x += np.random.uniform(-0.5, 0.5, size=n)
    plt.figure()
    if num_vars == 1:
        xmin = -1
        xmax = 1
    else:
        xmin = mean - 4*stdev
        xmax = mean + 4*stdev
    histogram(x, xlabel='$x$', bins=np.linspace(xmin, xmax, num_bins))
    _x = np.linspace(xmin, xmax, 100)
    _y = n*(xmax - xmin)/num_bins*scipy.stats.norm(mean, stdev).pdf(_x)
    plt.plot(_x, _y, color='gray', ls='dotted')
    plt.text(0.75, 0.85, '$n = %d$' % num_vars, transform=plt.gca().transAxes)
    save_current_figure('tcl_uniforme_%d.pgf' % num_vars)
    return plt

def exponential(n=1000000, num_vars=1, num_bins=81):
    """
    """
    mean = 1.*num_vars
    var = 1*num_vars
    stdev = np.sqrt(var)
    x = np.zeros(n)
    for i in range(num_vars):
        x += np.random.exponential(1., size=n)
    plt.figure()
    xmin = max(0., mean - 4*stdev)
    xmax = mean + 4*stdev
    histogram(x, xlabel='$x$', bins=np.linspace(xmin, xmax, num_bins))
    _x = np.linspace(xmin, xmax, 100)
    _y = n*(xmax - xmin)/num_bins*scipy.stats.norm(mean, stdev).pdf(_x)
    plt.plot(_x, _y, color='gray', ls='dotted')
    plt.text(0.75, 0.85, '$n = %d$' % num_vars, transform=plt.gca().transAxes)
    save_current_figure('tcl_esponenziale_%d.pgf' % num_vars)
    return plt

def cauchy(n=1000000, num_vars=1, num_bins=81):
    """
    """
    mean = 0
    stdev = 1*num_vars
    x = np.zeros(n)
    for i in range(num_vars):
        x += np.random.standard_cauchy(size=n)
    plt.figure()
    xmin = mean - 4*stdev
    xmax = mean + 4*stdev
    histogram(x, xlabel='$x$', bins=np.linspace(xmin, xmax, num_bins))
    _x = np.linspace(xmin, xmax, 100)
    _y = n*(xmax - xmin)/num_bins*scipy.stats.norm(mean, np.sqrt(stdev)).pdf(_x)
    plt.plot(_x, _y, color='gray', ls='dotted')
    plt.axis([xmin, xmax, None, 60000])
    plt.text(0.75, 0.85, '$n = %d$' % num_vars, transform=plt.gca().transAxes)
    save_current_figure('tcl_cauchy_%d.pgf' % num_vars)
    return plt


for m in [1, 2, 3, 5, 10, 100]:
    uniform(num_vars=m)
    exponential(num_vars=m)
    cauchy(num_vars=m)


show_figures()
