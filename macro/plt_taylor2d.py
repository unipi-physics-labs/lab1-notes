#!/usr/bin/env python
#
# Copyright (C) 2021, Luca Baldini (luca.baldini@pi.infn.it).
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


import numpy
# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

from matplotlib_ import *


def f(x, y):
    """
    """
    return 1. - (x - 0.5)**2. - (y - 0.5)**2.

x = numpy.linspace(0., 1., 100)
y = numpy.linspace(0., 1., 100)
x0, y0 = 0.4, 0.4
_x, _y = numpy.meshgrid(x, y)
z = f(_x, _y)

plt.figure('Taylor 2d')
ax = plt.axes(projection='3d')
ax.view_init(60, 215)
ax.plot_wireframe(_x, _y, z, color='black', rstride=20, cstride=20)
ax.plot_surface(_x, _y, z, alpha=0.2)
ax.scatter(x0, y0, f(x0, y0))

ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_zlabel('$f(x, y)$')


show_figures()
