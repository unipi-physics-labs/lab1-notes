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
from scipy import odr

from matplotlib_ import *


np.random.seed(100)



def f1(x, m, q):
    """
    """
    return m*x + q

def f2(p, x):
    """
    """
    return p[0]*x + p[1]


d = 10.
n = 10
pmin = 0.13
pmax = 0.45
dp = 0.005
dq = 0.005
p = np.linspace(pmin, pmax, n) + np.random.normal(0, dp, size=n)
q = 1. / (d - 1./np.linspace(pmin, pmax, n)) + np.random.normal(0, dq, size=10)

x = 1. / p
dx = dp / (p**2)
y = 1. / q
dy = dq / (q**2)

output_file = open(os.path.join(SNIPPETS_DATA_FOLDER, 'lens.dat'), 'w')
for i in range(n):
    output_file.write('%.5f\t%.5f\t%.5f\t%.5f\n' % (x[i], dx[i], y[i], dy[i]))
output_file.close()

# Vanilla least square.
popt1, pcov1 = curve_fit(f1, x, y, None, dy)
chisq1 = (((y - f1(x, *popt1)) / dy)**2).sum()
print(popt1, np.sqrt(pcov1.diagonal()), chisq1)

# Orthogonal distance regression.
model = odr.Model(f2)
data = odr.RealData(x, y, sx=dx, sy=dy)
alg = odr.ODR(data, model, beta0=(1, 1))
out = alg.run()
popt2, pcov2, chisq2 = out.beta, out.cov_beta, out.sum_square
print(popt2, np.sqrt(pcov2.diagonal()), chisq2)

# Improved least squares
popt3, pcov3 = curve_fit(f1, x, y, None, np.sqrt(dy**2 + (popt1[0]*dx)**2))
print(popt3, np.sqrt(pcov3.diagonal()))


_x = np.linspace(0, 10, 100)
_y1 = f1(_x, *popt1)
_y2 = f2(popt2, _x)


plt.figure()
scatter_plot(x, y, dy, dx, xlabel='$1/p$~[m$^{-1}$]', ylabel='$1/q$~[m$^{-1}$]')
plt.plot(_x, _y1, color='black', label='Minimi quadrati')
plt.axis([0, 10, 0, 10])
plt.text(0.6, 0.85, '$\\chi^2/\\nu = %.1f/%d$' % (chisq1, n - 2),
         transform=plt.gca().transAxes)
save_current_figure('fit_generale_ls.pgf')

plt.figure()
scatter_plot(x, y, dy, dx, xlabel='$1/p$~[m$^{-1}$]', ylabel='$1/q$~[m$^{-1}$]')
plt.plot(_x, _y2, color='black', label='ODR')
plt.plot(_x, _y1, color='black', ls='dotted', label='Minimi quadrati')
plt.axis([0, 10, 0, 10])
plt.text(0.15, 0.15, '$\\chi^2/\\nu = %.2f/%d$' % (chisq2, n - 2),
         transform=plt.gca().transAxes)
plt.legend()
save_current_figure('fit_generale_odr.pgf')

show_figures()
