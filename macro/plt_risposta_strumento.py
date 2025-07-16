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

from matplotlib import pyplot as plt
import numpy as np
from scipy.interpolate import InterpolatedUnivariateSpline

import matplotlib_ as mpl_

np.random.seed(666)


def err_zero(x):
    """
    """
    return x + 0.1

def err_scale(x):
    """
    """
    return x * 0.8

plt.figure('risposta_strumento')
x = np.linspace(0, 1, 10)
_n = 6
_x = np.linspace(0, 1, _n)
_y = _x + np.random.normal(0, 0.05, _n)
spl = InterpolatedUnivariateSpline(_x, _y)
plt.plot(x, x)
fmt = dict(color='gray', lw=0.75)
plt.plot(x, err_zero(x), **fmt)
plt.plot(x, err_scale(x), **fmt)
_x = np.linspace(0, 1, 100)
_y = spl(_x)
plt.plot(_x, _y, linestyle='dashed', **fmt)
mpl_.setup_gca(xmin=0., xmax=1., ymin=0., ymax=1., xlabel='Valore del misurando [u.a.]',
    ylabel='Lettura dello strumento [u.a.]')
mpl_.annotation('Errore di zero', (0.55, err_zero(0.55)), (0.2, 0.8))
mpl_.annotation('Errore di scala', (0.45, err_scale(0.45)), (0.7, 0.2))

mpl_.save_all_figures()
