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

import matplotlib_ as mpl_
from fit import exponential, fit_exponential

TARGET_YEAR = 2070
# https://en.wikipedia.org/wiki/Solar_constant
SOLAR_IRRADIANCE = 1.73e17 # W
SOLAR_ANNUAL_PRODUCTION = SOLAR_IRRADIANCE * 24. * 365.25
AN_602_BLAST = 50. * 4.184e15 / 3600

print(f'Solar annual production: {SOLAR_ANNUAL_PRODUCTION:.3e} Wh')
print(f'AN 602 blast: {AN_602_BLAST:.3e} Wh')

# Data from https://ourworldindata.org/energy-production-consumption
data = mpl_.load_file('global_energy_substitution.csv', delimiter=',', usecols=range(2, 13))
year = data[:,0]
consumption = data[:,1:].sum(axis=1)
consumption *= 1.e12 # TW h
sigma = 0.01 * consumption

plt.figure('consumo_energia')
plt.plot(year, consumption)
fmt = dict(ls='dashed', color='gray')
popt, pcov = fit_exponential(year, consumption, sigma, xmax=1900., p0=(1.e15, 100., 1800.))
print(f'Projection at year {TARGET_YEAR}: {exponential(TARGET_YEAR, *popt):.3e}')
plt.plot(year, exponential(year, *popt), **fmt)
popt, pcov = fit_exponential(year, consumption, sigma, xmin=1930., p0=(1.e15, 100., 1800.))
print(f'Projection at year {TARGET_YEAR}: {exponential(TARGET_YEAR, *popt):.3e}')
plt.plot(year, exponential(year, *popt), **fmt)
mpl_.setup_gca(logy=True, grids=True, ymin=5.e15, xlabel='Anno',
    ylabel='Consumo globale annuo di energia [Wh]')

mpl_.save_all_figures()
