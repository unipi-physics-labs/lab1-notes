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

import numpy as np
from scipy.stats import norm

from matplotlib_ import *


FILE_PATH = os.path.join(STATNOTES_MACRO_DATA, 'statura_leva_2.csv')
BINNING = np.linspace(145, 185, 9)
#Meno di 150,150-154,155-159,160-164,165-169,170-174,175-#179,180


input_file = open(FILE_PATH)
year = []
mean = []
for line in input_file:
    vals = [float(item) for item in line.split(',')]
    year.append(vals[0])
    mean.append(vals[2])


plt.figure()
y = vals[5:]
x = BINNING[:-1]
plt.bar(x, y, width=4, color='white', edgecolor='black')
plt.axis([145, 195, 0, 35])
annotation('$> 180$~cm', (182, y[-1]), (188, 30))
x = np.linspace(145, 200, 100)
y = 500*norm.pdf(x, vals[2], 7.5)
plt.plot(x, y, color='gray', ls='dotted')
plt.text(149, 30, 'Nati nel 1980')
plt.xlabel('Statura~[cm]')
plt.ylabel('Ripartizione percentuale~[\\%]')
save_current_figure('stature_leva_classi_1980.pgf')

plt.figure()
scatter_plot(year, mean, 0.02)
plt.axis([1970, 1982, 173.75, 174.75])
x = np.linspace(1970, 1982, 100)
y = 173.7 + 0.1*(x - 1970)
plt.plot(x, y, color='gray')
plt.xlabel('Anno di nascita')
plt.ylabel('Statura media~[cm]')
annotation('$\\sim 1$~mm all\'anno', (x[10], y[10]), (1976, 174.6))
save_current_figure('stature_leva_trend.pgf')

show_figures()
