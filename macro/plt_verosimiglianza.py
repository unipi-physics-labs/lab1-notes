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
import scipy.stats
import scipy.special

from matplotlib_ import *


mu = k = 3.

plt.figure()
x = np.arange(0, 10)
y = scipy.stats.poisson.pmf(x, mu)
bar_plot(x, y, width=21./50)
plt.axis([-0.5, 10.5, 0., 0.3])
plt.xlabel('$k$')
plt.ylabel('$\\mathcal{P}(k; \\mu = %d)$' % mu)
save_current_figure('esempio_likelihood_poisson1.pgf')

plt.figure()
x = np.linspace(0, 10, 100)
y = (x**k) * np.exp(-x) / scipy.special.factorial(k)
plt.axis([0., 10., 0., 0.3])
plt.xlabel('$\\mu$')
plt.ylabel('$\\mathcal{L}(\\mu; k = %d)$' % k)
plt.plot(x, y)
save_current_figure('esempio_likelihood_poisson2.pgf')

show_figures()
