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


from matplotlib import pyplot as plt
import numpy as np
import scipy.special

import matplotlib_ as mpl_


plt.figure('fattoriale')
x = np.arange(1, 51)
y1 = scipy.special.factorial(x)
y2 = np.exp(x)
mpl_.curve(x, y1, logy=True, xlabel='$n$', ylabel='$n!$', xmin=0., ymin=1., ymax=1.0e60)
mpl_.curve(x, y2, color=mpl_.DARK_GRAY, ls='dotted')
plt.text(35.0, 1.0e12, '$f(x) = e^x$')

mpl_.save_all_figures()