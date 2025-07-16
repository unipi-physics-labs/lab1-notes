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

import numpy as np

from matplotlib_ import *


plt.figure()
x = np.geomspace(1.e-9, 1., 100)
d = 5000.
for i, c in enumerate((1.e3, 1.e6, 1.e9)):
    y = x * c / (2. * d)
    plt.plot(x, y, color='black')
    x0 = 10.**(-5. - 1.5 * i)
    y0 = x0 * c / (2. * d)
    exp = int(np.log10(c))
    plt.text(x0, y0 * 3.5, f'$c = 10^{exp}$ m/s', rotation=36)

c = 299792458
y = x * c / (2. * d)
plt.plot(x, y, color='gray', ls='dashed')

plt.xscale('log')
plt.yscale('log')
plt.xlabel('$\\sigma_\\tau$ [s]')
plt.ylabel('$\\sigma_c / \\hat{c}$')
plt.axis([x.min(), x.max(), None, 1.])
plt.grid(which='both')
save_current_figure('misura_c.pgf')

show_figures()
