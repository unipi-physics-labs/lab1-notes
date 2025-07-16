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

np.random.seed(80)


# Setup.
T_hat = 1.25
sigma_T = 0.02

def _data_set(n):
    """Generate a data set.
    """
    T = np.random.normal(T_hat, sigma_T, max(n))
    m = []
    sigma_m = []
    delta_m = []
    for _n in n:
        data = T[:_n]
        m.append(np.mean(data))
        sigma_m.append(np.std(data, ddof=1) / np.sqrt(_n))
        delta_m.append(0.5 * (data.max() - data.min()))
    return m, sigma_m, delta_m

plt.figure('errore_asintotico')
n = np.arange(10, 160, 10, dtype=int)
# Plot two different realizations.
m, sigma_m, delta_m = _data_set(n)
mpl_.errorbar(n, sigma_m, label='Realizzazione 1')
m, sigma_m, delta_m = _data_set(n)
mpl_.errorbar(n, sigma_m, label='Realizzazione 2', fillstyle='none')
# Plot the 1./sqrt(n) line.
x = np.linspace(n.min(), n.max() + 5, 250)
y = sigma_T / np.sqrt(x)
plt.plot(x, y, ls='dashed', label='$\\propto 1/\\sqrt{n}$')
mpl_.setup_gca(xmin=0.0, xmax=n.max() + 5., ymin=0.0, xlabel='Numero totale di misure',
    ylabel='$\\sigma_T$ [s]', legend=True, grids=True)

mpl_.save_all_figures()
