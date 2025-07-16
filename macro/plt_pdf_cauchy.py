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



_x = np.linspace(-6, 6, 100)
_c = 1. / (np.pi*(1 + _x**2))
_g = scipy.stats.norm.pdf(_x, 0, 1)
plt.plot(_x, _c)
plt.plot(_x, _g, color='black', ls='dotted')
plt.axis([-5, 5, 0., 0.5])
plt.xlabel('$x$')
plt.ylabel('$c(x; 0, 1)$')
annotation('$x_0$', (0, 0.), (0, 0.46), style='angle')
annotation('$x_0 + \\gamma$', (1, 0.), (1, 0.42), style='angle')
save_current_figure('pdf_cauchy.pgf')

show_figures()
