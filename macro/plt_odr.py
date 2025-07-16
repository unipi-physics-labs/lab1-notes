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
from matplotlib_ import *

np.random.seed(700)

n = 5
dx = 0.0001
dy = 0.12
x = np.linspace(0.2, 0.8, n) + np.random.normal(0, dx, size=n)
y = x + np.random.normal(0, dy, size=n)

plt.figure()
plt.plot([0, 1], [0, 1])
scatter_plot(x, y, color='black')
plt.xlabel('$x$~[u. a.]')
plt.ylabel('$y$~[u. a.]')
plt.axis([0, 1, 0, 1])
for _x, _y in zip(x, y):
    plt.plot([_x, _x], [_y, _x], ls='dotted', color='gray')
save_current_figure('chisq_delta_x.pgf')

plt.figure()
plt.plot([0, 1], [0, 1])
scatter_plot(x, y, color='black')
plt.xlabel('$x$~[u. a.]')
plt.ylabel('$y$~[u. a.]')
plt.axis([0, 1, 0, 1])
for _x, _y in zip(x, y):
    _d = 0.45*(_y - _x)
    plt.plot([_x, _x + _d], [_y, _x + _d], ls='dotted', color='gray')
save_current_figure('chisq_delta_xy.pgf')

show_figures()
