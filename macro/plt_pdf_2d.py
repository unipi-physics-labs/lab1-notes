#!/usr/bin/env python
#
# Copyright (C) 2020, Luca Baldini (luca.baldini@pi.infn.it).
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


def plot_pdf_2d(x, y, z):
    """
    """
    ax = plt.axes(projection='3d')
    ax.view_init(60, 215)
    ax.plot_wireframe(x, y, z, color='black', rstride=15, cstride=15)
    ax.set_xlabel('$x_1$')
    ax.set_ylabel('$x_2$')
    ax.set_zlabel('$p(x_1, x_2)$')


x = numpy.linspace(0., 1., 100)
y = numpy.linspace(0., 1., 100)
_x, _y = numpy.meshgrid(x, y)

plt.figure('Indipendendti')
z = 4. * _x * _y
plot_pdf_2d(_x, _y, z)
save_current_figure('pdf_2d_indipendenti.pgf')

plt.figure('Indipendenti 1d')
for y in [0.25, 0.5, 0.75, 1.]:
    plt.plot(x, 4. * x * y, color='black')
    x0 = 0.75
    y0 = 4. * x0 * y
    plt.text(x0, y0, '$x_2=%.2f$' % y, ha='center', va='center', backgroundcolor='white')
plt.axis([0., 1., 0., 4.])
plt.xlabel('$x_1$')
plt.ylabel('$p(x_1, x_2~\\mathrm{fissato})$')
save_current_figure('pdf_2d_indipendenti_1d.pgf')


plt.figure('Dipendenti')
z = 1.5 * (_x**2. + _y**2.)
plot_pdf_2d(_x, _y, z)
save_current_figure('pdf_2d_dipendenti.pgf')

plt.figure('Dipendenti 1d')
for y in [0.25, 0.5, 0.75, 1.]:
    plt.plot(x, 1.5 * (x**2. + y**2.), color='black')
    x0 = 0.3
    y0 = 1.5 * (x0**2. + y**2.) + 0.05
    if y == 0.25:
        y0 -= 0.1
    plt.text(x0, y0, '$x_2=%.2f$' % y, ha='center', va='center', backgroundcolor='white')
plt.axis([0., 1., 0., 3.])
plt.xlabel('$x_1$')
plt.ylabel('$p(x_1, x_2~\\mathrm{fissato})$')
save_current_figure('pdf_2d_dipendenti_1d.pgf')



show_figures()
