#!/usr/bin/env python
#
# Copyright (C) 2016--2021 Luca Baldini (luca.baldini@pi.infn.it).
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


import glob
import os
import sys

from matplotlib import pyplot as plt
import numpy as np
import scipy.stats

import matplotlib_ as mpl_


true_period = 1.76 # 1.75 nominal, 10 ms longer according to the system time.


def _load_file(file_name):
    """Load a single file, containing 10 (1 period) + 10 (10 periods) measurements,
    one per line, and return two arrays.
    """
    data = mpl_.load_file(file_name)
    assert len(data) == 20
    return data[:10], data[10:] / 10.

def _load_data():
    """Load all the data.
    """
    data1 = np.array([], dtype = 'd')
    data10 = np.array([], dtype = 'd')
    for i in range(1, 94):
        _d1, _d10 = _load_file(f'pendolo_{i}.txt')
        data1 = np.append(data1, _d1)
        data10 = np.append(data10, _d10)
    return data1, data10

data1, data10 = _load_data()

m1 = np.average(data1)
s1 = np.std(data1, ddof=1)
print(f'1 period: {data1.min():.3f}--{data1.max():.3f}, mean {m1:.3f}, stdev {s1:.3f}')
m10 = np.average(data10)
s10 = np.std(data10, ddof=1)
print(f'10 period: {data10.min():.3f}--{data10.max():.3f}, mean {m10:.3f}, stdev {s10:.3f}')

plt.figure('periodo_pendolo1')
mpl_.hist(data1, bins=np.linspace(1.5, 2., 50))
mpl_.setup_gca(xmin=1.5, xmax=2., xlabel='Periodo misurato~[s]', ylabel='Occorrenze')
mpl_.axtext(0.075, 0.85, '1~periodo')
mpl_.annotation('misurando', (true_period, 0.), (true_period, 70.), style='angle')

plt.figure('periodo_pendolo10')
mpl_.hist(data10, bins=np.linspace(1.5, 2., 50))
mpl_.setup_gca(xmin=1.5, xmax=2., ymax=550., xlabel='Periodo misurato~[s]', ylabel='Occorrenze')
mpl_.axtext(0.075, 0.85, '10~periodi')
mpl_.annotation('misurando', (true_period, 0.), (true_period, 500.), style='angle')
mpl_.annotation('$9$ periodi?', (1.584, 10), (1.584, 100))

mpl_.save_all_figures()
