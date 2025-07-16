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

from matplotlib import pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

import matplotlib_ as mpl_

np.random.seed(100)


def f(x, q, m):
    """Straight line.
    """
    return m * x + q


n = 10
dy = 0.1
offset = 5
x = np.linspace(0.1 + offset, 0.9 + offset, n)
y = f(x, 1, 1) + np.random.normal(0, dy, size=n)
dy = np.full(y.shape, dy)
popt, pcov = curve_fit(f, x, y, None, dy)
q, m = popt
dq, dm = np.sqrt(pcov.diagonal())
r = pcov[1,0] / dq / dm

plt.figure('correlazione_inter_coeff')
mpl_.scatter(x, y, dy, xlabel='$x$~[u.a.]', ylabel='$y$~[u.a.]')
plt.axis([offset, 1 + offset, 0.5 + offset, 2.5 + offset])
_x = np.linspace(offset, 1 + offset, 100)
_y = f(_x, q, m)
plt.plot(_x, _y, color='black')
delta = 2.
_y = f(_x, q + delta * dq, m - delta * dm)
plt.plot(_x, _y, color='black', ls='dotted')
mpl_.annotation('$r_1$', (_x[15], _y[15]), (0.4 + offset, 2 + offset))
_y = f(_x, q - delta * dq, m + delta * dm)
plt.plot(_x, _y, color='black', ls='dotted')
mpl_.annotation('$r_2$', (_x[15], _y[15]), (0.4 + offset, 0.75 + offset))
x0 = 0.5 + offset
d1 = np.sqrt(x0**2. * dm**2. + dq**2.)
d2 = np.sqrt(x0**2. * dm**2. + dq**2. + 2 * r * x0 * dm * dq)
print(d1, d2)
mpl_.scatter(x0, f(x0, *popt), d1, color='gray')
mpl_.axtext(0.6, 0.3, f'$q = {q:.2f} \\pm {dq:.2f}$')
mpl_.axtext(0.6, 0.22, f'$m = {m:.2f} \\pm {dm:.2f}$')
mpl_.axtext(0.6, 0.14, f'$\\varrho_{{qm}} = {r:.3f}$')

mpl_.save_all_figures()
