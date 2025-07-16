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

energy, _, _, flux, sigma_fluxp, sigma_fluxn = mpl_.load_file('ams_protons.txt', unpack=True)

plt.figure('protoni_ams')
plt.errorbar(energy, flux, (sigma_fluxp, sigma_fluxn), fmt='o')
popt, pcov = fit_power_law(energy, flux, sigma=sigma_fluxn, xmin=10.)
plt.plot(energy, power_law(energy, *popt), ls='dashed', color='gray')
mpl_.setup_gca(logx=True, logy=True, grids=True, xmin=8., xmax=2000, ymin=2.e-5, ymax=1.e2,
    xlabel='Energia [GeV]', ylabel='Flusso [m$^{-2}$ s$^{-1}$ sr$^{-1}$ GeV$^{-1}$]')
mpl_.save_all_figures()