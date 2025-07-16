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
from scipy.optimize import curve_fit

from matplotlib_ import *


FILE_PATH = os.path.join(STATNOTES_MACRO_DATA, 'pendolo_smorzato.txt')
T_MIN = 40.
T_MAX = 80.
RESAMPLE = 1
RESIDUALS = False
PARS = (60., 4.39, 4.71, 0.025, 440.)


def f(t, amplitude, omega, phi, lambda_, offset):
    """Definition of the fit function
    """
    return amplitude * np.sin(omega * t + phi) * np.exp(-lambda_ * t) + offset


t, x = np.loadtxt(FILE_PATH, unpack=True)
mask = (t >= T_MIN)*(t <= T_MAX)
t = t[mask]
x = x[mask]
if RESAMPLE > 1:
    t = t[::RESAMPLE]
    x = x[::RESAMPLE]
t -= t.min()

popt, pcov = curve_fit(f, t, x, PARS)
amplitude, omega, phi, lambda_, offset = popt
print(popt)
print(np.sqrt(pcov.diagonal()))

if RESIDUALS:
    fig, frame1, frame2 = large_residual_figure()
    plt.sca(frame1)
else:
    fig = large_figure()
scatter_plot(t, x, xlabel='$t$~[s]', ylabel='y~[u. a.]')
_t = np.linspace(t.min(), t.max(), 1000)
_x = f(_t, *popt)
plt.plot(_t, _x, color='black')
plt.axis([None, None, 360, 520])
for i, _x in enumerate(np.arange(1.5*np.pi - phi, 40, 2*np.pi/omega)):
    _y = f(_x, *popt) + 10
    plt.text(_x, _y, '%d' % (i + 1), size=8, ha='center', va='bottom')

def hline(y, tmin=0, tmax=T_MAX - T_MIN):
    """
    """
    line(tmin, y, tmax, y, color='gray')

hline(440)
hline(500, 0, 3)
hline(500, 7)
hline(380)

if RESIDUALS:
    plt.sca(frame2)
    scatter_plot(t, x - f(t, *popt), xlabel='$t$~[s]')
    plt.axis([None, None, -3, 3])


save_current_figure('fit_pendolo_smorzato.pgf')

show_figures()
