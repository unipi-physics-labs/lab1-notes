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

EARTH_MASS = 5.972e24
MOON_MASS = 7.348e22
OCEAN_MASS = 1.35e21
AVERAGE_PERSON_WEIGHT = 60.
ITALY_POPULATION_WEIGHT = AVERAGE_PERSON_WEIGHT * 60.e6
EU_POPULATION_WEIGHT = AVERAGE_PERSON_WEIGHT * 450.e6
WORLD_POPULATION_WEIGHT = AVERAGE_PERSON_WEIGHT * 7.75e9
TARGET_YEAR = 2070
print(f'Italy population weight: {ITALY_POPULATION_WEIGHT:.3e}')
print(f'EU population weight: {EU_POPULATION_WEIGHT:.3e}')
print(f'World population weight: {WORLD_POPULATION_WEIGHT:.3e}')


# Data from https://ourworldindata.org/plastic-pollution
year, prod = mpl_.load_file('global_plastics_production.csv', unpack=True, delimiter=',', usecols=(2, 3))
sigma = 0.01 * prod
prod *= 1.e3

plt.figure('produzione_plastica')
plt.plot(year, prod)
fmt = dict(ls='dashed', color='gray')
popt, pcov = fit_exponential(year, prod, sigma, xmax=1970., p0=(1.e15, 3., 1950.))
print(f'Projection at year {TARGET_YEAR}: {exponential(TARGET_YEAR, *popt):.3e}')
plt.plot(year, exponential(year, *popt), **fmt)
popt, pcov = fit_exponential(year, prod, sigma, xmin=1970., p0=(1.e15, 3., 1950.))
print(f'Projection at year {TARGET_YEAR}: {exponential(TARGET_YEAR, *popt):.3e}')
plt.plot(year, exponential(year, *popt), **fmt)
#plt.axhline(ITALY_POPULATION_WEIGHT, **fmt)
#plt.text(1990, ITALY_POPULATION_WEIGHT, 'Peso della popolazione Italiana', ha='center')
#plt.axhline(EU_POPULATION_WEIGHT, **fmt)
#plt.text(1990, EU_POPULATION_WEIGHT, 'Peso della popolazione Europea', ha='center')
#plt.axhline(WORLD_POPULATION_WEIGHT, **fmt)
#plt.text(1990, WORLD_POPULATION_WEIGHT, 'Peso della popolazione mondiale', ha='center')
mpl_.setup_gca(logy=True, grids=True, xmin=1950., xmax=2015., ymin=1.e9, ymax=1.e12,
    xlabel='Anno', ylabel='Produzione annua globale di plastica [kg]',
    xticks=np.arange(1940, 2021, 10))

mpl_.save_all_figures()
