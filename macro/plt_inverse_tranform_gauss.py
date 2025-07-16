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

from matplotlib_ import *

import numpy as np
import scipy.special


XMIN = 0.
XMAX = 1.
YMIN = -3.5
YMAX = 3.5

ppf = scipy.special.ndtri

fig, axs, axhx, axhy = scatter_hist_figure(inverse=True)
x = np.linspace(0, 1, 1000)
y = ppf(x)
plt.sca(axs)
plt.plot(x, y)
plt.axis([XMIN, XMAX, YMIN, YMAX])
for _x in np.linspace(0, 1, 20):
    _y = ppf(_x)
    line(_x, YMIN, _x, _y, lw=0.75, color='gray')
    line(_x, _y, XMIN, _y, lw=0.75, color='gray')


x = np.random.uniform(size=50000)
y = ppf(x)
plt.sca(axhx)
histogram(x, ylabel='', bins=100)
plt.axis([XMIN, XMAX, None, None])
plt.sca(axhy)
histogram(y, ylabel='', bins=100, orientation='horizontal')
plt.axis([None, None, YMIN, YMAX])

show_figures()
