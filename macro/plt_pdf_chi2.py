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


from matplotlib_ import *

import numpy as np
import scipy.stats


def plot_chi2(n):
    """
    """
    xmin = max(0, n - 4. * np.sqrt(2. * n))
    xmax = n + 4. * np.sqrt(2. * n)
    x = np.linspace(xmin, xmax, 100)
    y = scipy.stats.chi2.pdf(x, n)
    plt.plot(x, y)
    ymax = 0.5
    if n > 2 and n < 10:
        ymax = 0.25
    if n >= 10:
        ymax = 0.1
    plt.axis([xmin, xmax, 0, ymax])
    plt.xlabel('$x$')
    plt.ylabel('$\\wp(x; %d)$' % n)
    plt.text(0.75, 0.85, '$n = %d$' % n, transform=plt.gca().transAxes)

for n in [1, 2, 3, 5, 10, 50]:
    plt.figure()
    plot_chi2(n)
    save_current_figure('pdf_chi2_%d.pgf' % n)

show_figures()
