#!/usr/bin/env python
#
# Copyright (C) 2017--2021, Luca Baldini (luca.baldini@pi.infn.it).
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

# Basic settings.
xmin, xmax = 16.2, 17.8
ymin, ymax = 260.0, 290.0
xticks = [16.5, 17.0, 17.5]
yticks = [260.0, 270.0, 280.0, 290.0]
hticks = [0.0, 5.0, 10.0, 15.0]
num_bins = 19

# Load the input data.
l, m, d = mpl_.load_file('chiodini.txt', unpack=True)
# Convert to mg and mm
l *= 10.
m *= 1000.

# Calculate the basic stats.
r = np.corrcoef(l, m)[1,0]
ml = np.mean(l)
sl = np.sqrt(l.var(ddof=1))
mm = np.mean(m)
sm = np.sqrt(m.var(ddof=1))
n = len(l)
print(f'm = {mm:.2f} +\- {sm / np.sqrt(n):.2f} mg')
print(f'l = {ml:.3f} +\- {sl / np.sqrt(n):.3f} mg')
# Estimate the density
lambda_ = mm / ml
sigma_lambda = np.sqrt((mm**2.0 * sl**2.0 + ml**2.0 * sm**2)/(ml**4.)) / np.sqrt(n)
print('lambda = %.4f +\- %.4f g/m' % (lambda_, sigma_lambda))

plt.figure('chiodini_lambda')
x = m / l
mx = x.mean()
sx = np.sqrt(x.var(ddof=1))
print(f'x = {mx:.3f} +\- {sx / np.sqrt(n):.3f} g m^-1')
mpl_.histogram(x, bins=num_bins, xlabel='$\lambda$~[g~m$^{-1}$]', xmin=15.7, xmax=16.7, ymax=15.0)
mpl_.axtext(0.07, 0.875, f'$m = {mx:.3f}$~g~m$^{{-1}}$')
mpl_.axtext(0.07, 0.8, f'$s_{{n-1}} = {sx:.3f}$~g~m$^{{-1}}$')

xfmt = dict(xmin=xmin, xmax=xmax, xticks=xticks)
yfmt = dict(ymin=ymin, ymax=ymax, yticks=yticks)

plt.figure('chiodini_scatter')
mpl_.scatter(l, m, xlabel='$l$~[mm]', ylabel='$m$~[mg]', **xfmt, **yfmt)
mpl_.axtext(0.1, 0.85, f'$r = {r:.2f}$')

fig, axs, axhx, axhy = mpl_.scatter_hist_figure('chiodini_scatter_hist')
plt.sca(axs)
mpl_.scatter(l, m, xlabel='$l$~[mm]', ylabel='$m$~[mg]', **xfmt, **yfmt)
mpl_.axtext(0.1, 0.85, f'$r = {r:.2f}$')
mpl_.line(xmin, mm, xmax, mm)
mpl_.line(ml, ymin, ml, ymax)
plt.sca(axhx)
mpl_.histogram(l, bins=num_bins, ylabel='', yticks=hticks, **xfmt)
mpl_.axtext(0.07, 0.85, f'$m = {ml:.3}f$~mm')
mpl_.axtext(0.07, 0.75, f'$s_{{n-1}} = {sl:.3f}$~mm')
mpl_.line(ml, 0.0, ml, 15.0)
plt.sca(axhy)
mpl_.histogram(m, bins=num_bins, ylabel='', orientation='horizontal', xmin=0.0,
    xmax=15.0, xticks=hticks, **yfmt)
mpl_.axtext(0.85, 0.58, f'$m = {mm:.2f}$~mg', rotation=-90.0)
mpl_.axtext(0.765, 0.58, f'$s_{{n-1}} = {sm:.2f}$~mg', rotation=-90.0)
mpl_.line(0, mm, 15, mm)

mpl_.save_all_figures()
