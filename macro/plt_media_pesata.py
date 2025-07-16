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


from matplotlib_ import *

import numpy as np

n = np.array([1.325, 1.36, 1.32, 1.338, 1.335])
dn = np.array([0.012, 0.05, 0.01, 0.005, 0.006])

nmin = 1.22
nmax = 1.45

plt.figure()
_x = np.arange(1, len(n) + 1)
scatter_plot(_x, n, dn)
_xmin = 0
_xmax = len(n) + 1
plt.axis([_xmin, _xmax, None, None])
w = 1./dn**2.
m = (n*w).sum()/w.sum()
dm = np.sqrt(1./w.sum())
plt.plot([_xmin, _xmax], [m, m], color='black')
line(_xmin, m + dm, _xmax, m + dm)
line(_xmin, m - dm, _xmax, m - dm)
plt.xlabel('Gruppo')
plt.ylabel('$n$')
plt.xticks(_x, ['A', 'B', 'C', 'D', 'E'])
save_current_figure('media_pesata.pgf')


plt.figure()
_x = []
_y = []
for _n in np.linspace(nmin, nmax, 100):
    _chi2 = (((n - _n)/dn)**2).sum()
    _x.append(_n)
    _y.append(_chi2)
plt.plot(_x, _y)
plt.axis([nmin, nmax, 0, None])
plt.xlabel('$n$')
plt.ylabel('$\chi^2(n)$')
save_current_figure('media_pesata_chisq.pgf')

show_figures()
