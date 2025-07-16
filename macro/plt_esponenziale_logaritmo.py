#!/usr/bin/env python
#
# Copyright (C) 2015--2021, Luca Baldini (luca.baldini@pi.infn.it).
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

import matplotlib_ as mpl_


plt.figure('esponenziale_logaritmo')
x = np.linspace(0.01, 10.0, 100)
exp = np.exp(x)
log = np.log(x)
plt.plot(x, exp)
mpl_.setup_gca(xmin=0.0, xmax=10.0, ymin=-5.0, ymax=20., xlabel='$x$', ylabel='$f(x)$', grids=True)
plt.plot(x, log, color='black')
plt.plot(x, x, color='black', ls='dotted')
plt.text(3.3, 15, '$f(x) = e^x$')
plt.text(7.0, 0, '$f(x) = \\ln x$')
plt.text(5.25, 8, '$f(x) = x$')

mpl_.save_all_figures()
