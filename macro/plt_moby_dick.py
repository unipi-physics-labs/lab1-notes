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

import collections

from matplotlib import pyplot as plt
import numpy as np

import matplotlib_ as mpl_
from fit import power_law, fit_power_law


file_path = mpl_.macro_file_path('moby_dick.txt')
with open(file_path) as input_file:
    text = input_file.read()

for char in (',', '.', ';', ':', '-', '\n', '"', "'"):
    text = text.replace(char, '')

words = text.lower().split()
print(len(words))
counter = collections.Counter(words)
data = counter.most_common()
words = [item[0] for item in data]
counts = [item[1] for item in data]

print(len(words))
print(data[:500])

def _label_word(word, pos):
    """
    """
    rank = words.index(word) + 1
    n = counts[rank - 1]
    mpl_.annotation(word, (rank, n), pos)


n = 5000
x = np.arange(n) + 1
y = np.array([item[1] for item in data[:n]])
plt.figure('moby_dick')
plt.plot(x, y, 'o')
popt, pcov = fit_power_law(x, y, sigma=np.sqrt(y))
norm, index = popt
xmax = norm**(-1./index)
print(f'Estimate of the number of distinct words: {xmax}')
print(norm / (index + 1) * (xmax**(index + 1) - 0.5**(index + 1)))

plt.plot(x, power_law(x, *popt), ls='dashed', color='gray')
_label_word('the', (3, 1.e2))
_label_word('of', (5, 1.e3))
_label_word('and', (10, 1.e4))
_label_word('whales', (500, 5))
_label_word('captain', (1000, 1.e3))
_label_word('life', (2000, 3.e2))
_label_word('blood', (2000, 1.e2))
mpl_.setup_gca(logx=True, logy=True, grids=True, xmin=0.75,
    xlabel='Rango', ylabel='Numero di occorrenze')

mpl_.save_all_figures()
