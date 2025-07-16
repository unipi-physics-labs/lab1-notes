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
from fit import power_law, fit_power_law


def _load_data(min_sales=20.):
    """
    """
    file_path = mpl_.macro_file_path('riaa.txt')
    with open(file_path) as input_file:
        lines = input_file.readlines()
    data = {}
    for line in lines:
        if line.startswith('\t') and line.endswith('\n'):
            line = line.strip('\n\t')
            line = line.replace('B*WITCHED', 'BWITCHED')
            line = line.replace('THE A*TEENS', 'THE ATEENS')
            artist = line.split('*')[0].strip()
            try:
                units = float(line.split('*')[1])
                if units < min_sales:
                    break
                data[artist] = units
            except ValueError:
                print(line)
                input()
    return data


data = _load_data()
print(data)
print(f'Total number of artits: {len(data)}')
artists = list(data.keys())
sales = np.array(list(data.values()))

n = 10
print(f'Sales for the first {n}: {sales[:n].sum()}')
print(f'Total sales: {sales.sum()}')
print(f'f_10: {sales[:n].sum() / sales.sum()}')

def _label_artist(artist, pos):
    """
    """
    rank = artists.index(artist) + 1
    sale = data[artist]
    label = f'{artist.title()}'
    mpl_.annotation(label, (rank, sale), pos)

plt.figure('riaa')
rank = np.arange(len(sales)) + 1
plt.plot(rank, sales, 'o')
popt, pcov = fit_power_law(rank, sales, sigma=np.sqrt(sales))
norm, index = popt
N_10 = norm / (index + 1) * (10.5**(index + 1) - 0.5**(index + 1))
N_tot = norm / (index + 1) * (130.5**(index + 1) - 0.5**(index + 1))
print(N_10, N_tot, N_10 / N_tot)

grid = np.linspace(0.75, 150, 100)
plt.plot(grid, power_law(grid, *popt), ls='dashed', color='gray')
_label_artist('THE BEATLES', (3, 13))
_label_artist('EAGLES', (4, 23))
_label_artist('LED ZEPPELIN', (40, 200))
_label_artist('PINK FLOYD', (50, 150))
_label_artist('QUEEN', (100, 110))
_label_artist('THE BEACH BOYS', (20, 15))
mpl_.setup_gca(logx=True, logy=True, grids=True, ymin=10., xlabel='Posizione in classifica',
    ylabel='Dischi venduti [milioni di copie]')

mpl_.save_all_figures()
