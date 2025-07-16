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

import numpy as np

from matplotlib_ import *

FILE_PATH = os.path.join(STATNOTES_MACRO_DATA, 'raccolta_differenziata.csv')
TAG = 'raccolta differenziata dei rifiuti urbani per i comuni - percentuale'
BINNING = np.linspace(0, 100, 15)
X_LABEL = 'Frazione di raccolta differenziata [%]'
Y_LABEL = 'Numero di Comuni'

data = {}
for year in range(2000, 2013):
    data[year] = []

input_file = open(FILE_PATH, 'rb')
input_file.readline()
for line in input_file:
    line = line.decode('latin-1')
    vals = [item.strip('"') for item in line.split(',')]
    year = int(vals[1])
    place = vals[2]
    if vals[3] == TAG and place != 'Italia':
        try:
            perc = float(vals[4])
            data[year].append(perc)
        except:
            pass


plt.figure()
hist(data[2012], bins=BINNING, color='black')
hist(data[2002], bins=BINNING, color='gray')
setup_gca(xlabel=X_LABEL, ylabel=Y_LABEL)

show_figures()
