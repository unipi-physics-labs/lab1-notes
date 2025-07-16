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

import matplotlib_ as mpl_

np.random.seed(666)


n = 10000

def throw():
    """Throw the die.
    """
    x = np.arange(1., n + 1.)
    p = np.random.choice([0., 0., 1., 0., 0., 0.], size=n)
    return x, np.cumsum(p) / x

plt.figure('frequenza_dado')
for i in range(10):
    x, y = throw()
    mpl_.curve(x, y)
mpl_.setup_gca(logx=True, xlabel='$N$', ylabel='$\\frac{n}{N}$', grids=True)
mpl_.line(1., 1. / 6, n, 1. / 6)
plt.text(n / 6., 0.25, '$\\frac{n}{N} = \\frac{1}{6}$')

mpl_.save_all_figures()