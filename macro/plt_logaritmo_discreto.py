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

m = 71
p = 11
k = range(0, m)
y = [p**_k % m for _k in k]

plt.figure()
plt.plot(k, y, color='gray', ls='dotted')
plt.plot(k, y, 'o')
plt.axis([0, m + 2, 0, m + 2])
plt.xlabel('$k$')
plt.ylabel('$p^k~\\mathrm{mod}~m$')

save_current_figure('logaritmo_discreto.pgf')

show_figures()
