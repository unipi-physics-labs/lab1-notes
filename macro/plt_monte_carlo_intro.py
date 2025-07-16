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

from numpy import random
random.seed(666)

NUM_POINTS = 500


circle = plt.Circle((0.5, 0.5), 0.5, color='black', fill=False)

w = DEFAULT_FIG_WIDTH
h = DEFAULT_FIG_WIDTH - DEFAULT_MARGINS['left'] - DEFAULT_MARGINS['right'] +\
    DEFAULT_MARGINS['top'] + DEFAULT_MARGINS['bottom']

plt.figure(figsize=(w, h))
plt.gca().add_artist(circle)
plt.axis([0, 1, 0, 1])
plt.xlabel('x [u.a.]')
plt.ylabel('y [u.a.]')
x = random.uniform(size=NUM_POINTS)
y = random.uniform(size=NUM_POINTS)
plt.plot(x, y, 'o')
nc = (x**2 + y**2 <= 1).sum()
print(nc, NUM_POINTS, 4.*nc/NUM_POINTS)

save_current_figure('monte_carlo_pi.pgf')

show_figures()
