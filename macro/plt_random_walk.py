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

np.random.seed(666)


def generate(num_steps, step_size=1):
    """
    """
    x = np.random.choice([-step_size, step_size], size=num_steps)
    return np.cumsum(x)


plt.figure()
n = 500
for i in range(15):
    x = generate(n)
    plt.plot(x, color='gray', lw=1)
dy = 2.5*n**0.5
plt.axis([None, None, -dy, dy])
plt.xlabel('$n$')
plt.ylabel('$x_n$')
x = np.linspace(0, n, n)
y = x**0.5
plt.plot(x, y, color='black')
plt.plot(x, -y, color='black')
plt.plot(x, 2*y, color='black', ls='dotted')
plt.plot(x, -2*y, color='black', ls='dotted')
save_current_figure('random_walk.pgf')

show_figures()
