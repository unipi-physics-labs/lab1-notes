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
from fit import exponential, fit_exponential


# Data from https://github.com/karlrupp/microprocessor-trend-data
year, transistors = mpl_.load_file('transistors.txt', unpack=True)
transistors *= 1000

x = []
y = []
for _y, _n in zip(year, transistors):
    if len(x) == 0 or _n > y[-1]:
        print(len(x), _y, _n)
        x.append(_y)
        y.append(_n)
x = np.array(x)
y = np.array(y)

def _label_chip(name, i, pos):
    """
    """
    mpl_.annotation(name, (x[i], y[i]), pos)


plt.figure('transistor')
plt.plot(x, y, 'o')
p0 = (1.e3, 3., 1970.)
popt, pcov = fit_exponential(x, y, p0=p0, sigma=0.01 * y)
xgrid = np.linspace(1970., 2020., 100)
plt.plot(xgrid, exponential(xgrid, *popt), ls='dashed', color='gray')
# These are taken from https://en.wikipedia.org/wiki/Transistor_count
_label_chip('Intel 4004', 0, (1980, 1.e6))
_label_chip('Intel 80286', 4, (1995, 1.e4))
_label_chip('Intel 80486', 6, (1999, 1.e9))
_label_chip('AMD K6-3', 10, (2010, 1.e5))
mpl_.setup_gca(xlabel='Anno', ylabel='Record di transistor per microprocessore',
    logy=True, xmin=1970, xmax=2020, grids=True, ymin=1.e3, yticks=np.logspace(3, 11, 9))

mpl_.save_all_figures()
