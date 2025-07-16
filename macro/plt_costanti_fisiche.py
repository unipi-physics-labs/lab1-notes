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

from collections import Counter

import matplotlib.pyplot as plt
import numpy as np
import scipy
import scipy.constants
from scipy.interpolate import InterpolatedUnivariateSpline

import matplotlib_ as mpl_


def first_digit(val):
    """
    """
    return int(f'{val:e}'.strip('-')[0])


values = np.array([const[0] for const in scipy.constants.physical_constants.values()])
num_constants = len(values)
digits = [first_digit(val) for val in values]
counter = Counter(digits)
digits = np.array(list(counter.keys()))
counts = np.array(list(counter.values()))
d = np.arange(1, 10)
benford = np.log10(d + 1.) - np.log10(d)
print(d, benford)
spline = InterpolatedUnivariateSpline(d, benford * num_constants)
frac = counts / num_constants
print(f'{num_constants} physical constants parsed...')
print(f'scipy version: {scipy.__version__}')

min_ = abs(values).min()
max_ = values.max()
for name, val in scipy.constants.physical_constants.items():
    if val[0] in (min_, max_):
        print(name, val)


plt.figure('legge_di_benford')
mpl_.bar(digits, counts)
x = np.linspace(0., 10., 100)
plt.plot(x, spline(x), ls='dashed', color='gray')
mpl_.setup_gca(xmin=0., xmax=10., ymax=180., xlabel='Prima cifra', ylabel='Occorrenze',
    xticks=np.arange(1, 10))
fmt = dict(ha='center', size=mpl_.SMALLER_FONT_SIZE)
offset_dict = {4: 7.5, 6: 7.5, 8: 7.5}
for digit, cnts, percent in zip(digits, counts, frac * 100.):
    offset = offset_dict.get(digit, 0.)
    plt.text(digit, cnts + 12 + offset, f'{cnts}', **fmt)
    plt.text(digit, cnts + 2 + offset, f'({percent:.1f}\%)', **fmt)

mpl_.save_all_figures()
