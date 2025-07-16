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

from matplotlib_ import *


plt.figure()
a = -np.sqrt(3)
b = -a
h = 1. / (b - a)
x = np.array([a, a, b, b])
y = np.array([0, h, h, 0])
plt.plot(x, y, ls='dotted', label='$x$')
plt.axis([-3.5, 3.5, 0., 0.5])
plt.xlabel('$x$')
plt.ylabel('$p(x)$')
x = np.linspace(0, 3, 100)
y = 1./(2.*np.sqrt(3*x))
x = np.append(x, 3)
y = np.append(y, 0)
y[0] = 0.
plt.plot(x, y, color='black', label='$x^2$')
plt.legend()
save_current_figure('quadrato_uniforme.pgf')


plt.figure()
x = np.linspace(-6, 6, 100)
y = scipy.stats.norm.pdf(x, 0., 1.)
plt.plot(x, y, ls='dotted', label='x')
plt.axis([-6., 6., 0., 0.5])
plt.xlabel('$x$')
plt.ylabel('$p(x)$')
x = np.linspace(0, 6, 100)
y = scipy.stats.chi2.pdf(x, 1)
y[0] = 0
plt.plot(x, y, color='black', label='$x^2$')
plt.legend()
save_current_figure('quadrato_gaussiana.pgf')


show_figures()
