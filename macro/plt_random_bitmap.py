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

import random

import numpy as np

from matplotlib_ import *



NUM_PX_SIDE = 128


class msqg:

    """Simple implementation of a MSQG.
    """

    def __init__(self, m, b = 10, seed = 1):
        assert m % 2 == 0
        self._m = m
        self._b = b
        self._x = seed
        self._c1 = self._b**(self._m/2)
        self._c2 = self._b**self._m
        self._norm = float(self._c2)

    def __iter__(self):
        return self

    def next(self):
        self._x = self._x**2/self._c1 % self._c2
        return self._x/self._norm


class lcg:

    """Simple implementation of a LCG.
    """

    def __init__(self, a, c, m, seed = 1):
        self._a = a
        self._c = c
        self._m = m
        self._x = seed
        self._norm = float(self._m)

    def __iter__(self):
        return self

    def next(self):
        self._x = (self._a*self._x + self._c) % self._m
        return self._x/self._norm


class randu(lcg):

    """The infamous RANDU RNG, see http://en.wikipedia.org/wiki/RANDU
    """

    def __init__(self, seed = 1):
        lcg.__init__(self, 65539, 0, 2**31, seed)


r2 = lcg(2**7 + 1, 0, 2**35, 1)
r3 = lcg(23, 0, 1000, 1)

m1 = np.zeros((NUM_PX_SIDE, NUM_PX_SIDE))
m2 = np.zeros((NUM_PX_SIDE, NUM_PX_SIDE))
m3 = np.zeros((NUM_PX_SIDE, NUM_PX_SIDE))

for i in range(NUM_PX_SIDE):
    for j in range(NUM_PX_SIDE):
        m1[i, j] = random.randint(0, 1)
        m2[i, j] = int(r2.next() > 0.5)
        m3[i, j] = int(r3.next() > 0.5)


img = plt.matshow(m1, cmap=plt.cm.gray)
#img.set_rasterized(False)
#plt.gcf().set_rasterized(False)
#plt.gca().set_rasterized(False)
save_current_figure('random_bitmap_std.pgf')

plt.matshow(m2, cmap=plt.cm.gray)
save_current_figure('random_bitmap_1.pgf')

plt.matshow(m3, cmap=plt.cm.gray)
save_current_figure('random_bitmap_2.pgf')

show_figures()
