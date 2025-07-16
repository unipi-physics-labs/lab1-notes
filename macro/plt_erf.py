#!/usr/bin/env python
#
# Copyright (C) 2016--2021, Luca Baldini (luca.baldini@pi.infn.it).
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


from matplotlib import pyplot as plt
import numpy as np
import scipy.special
import scipy.stats

import matplotlib_ as mpl_


zmax = 3.0
zmin = -zmax

plt.figure('cdf_gauss')
x = np.linspace(zmin, zmax, 100)
y = 0.5 * (1.0 + scipy.special.erf(x / np.sqrt(2.)))
mpl_.curve(x, y, xlabel='$z$', ylabel='$F(z)$', xmin=-5.0, xmax=5.0, ymin=0.0, ymax=1.0)

plt.figure('erf')
x = np.linspace(0.0, zmax, 100)
mpl_.curve(x, scipy.special.erf(x), xlabel='$x$', ylabel='erf$(x)$', xmin=0.0, xmax=zmax, ymin=0.0, ymax=1.0)


def _plot_interval(num_sigma, y0, lw=0.75):
    """Convenicence function to plot gaussian intervals.
    """
    cont = 2. * scipy.stats.norm().cdf(num_sigma) - 1.
    mpl_.horizontal_quote(y0, -num_sigma, num_sigma, f'{100. * cont:.2f}\%')
    mpl_.line(-num_sigma, 0.0, -num_sigma, y0, color=mpl_.DARK_GRAY, linewidth=lw)
    mpl_.line(num_sigma, 0.0, num_sigma, y0, color=mpl_.DARK_GRAY, linewidth=lw)


plt.figure('regola_68_95_99')
x = np.linspace(-5.0, 5.0, 100)
y = scipy.stats.norm.pdf(x)
mpl_.curve(x, y, xlabel='$z$', ylabel='$N(z)$', xmin=-5.0, xmax=5.0, ymin=0.0, ymax=0.75)
_plot_interval(1., 0.45)
_plot_interval(2., 0.55)
_plot_interval(3., 0.65)

mpl_.huge_figure('erf_tail')
x = np.linspace(0., 8.1, 200)
Phi = lambda x: 1. - scipy.stats.norm().cdf(x)
mpl_.curve(x, Phi(x), xmin=0.0, xmax=8.1, ymin=1e-16, ymax=1., logy=True, xlabel='$z$',
    ylabel='$1 - \Phi(z)$', grids=True, yticks=np.geomspace(1.0e-16, 1.0, 17))
for _z in np.linspace(1., 8., 8):
    _y = Phi(_z)
    plt.plot(_z, _y, 'o', color='black')
    a, b = ('%.2e' % _y).split('e-')
    b = int(b)
    if _z < 7:
        ha = 'left'
        _z += 0.1
    else:
        ha = 'right'
        _z -= 0.1
    plt.text(_z, _y, r'${%s} \times 10^{-%s}$' % (a, b), ha=ha, va='center')
plt.tight_layout()

mpl_.save_all_figures()
