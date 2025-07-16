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
import scipy.stats

import matplotlib_ as mpl_



# Prussian cavalry.
n = 200
mu = 122. / 200
ok = np.array([109, 65, 22, 3, 1])

x = np.arange(0, 5)
_prob = scipy.stats.poisson.pmf(x, mu)
_prob[4] = _prob[4] + (1. - _prob.sum())
ek = n * _prob
print(x)
print(_prob, _prob.sum())
print(ek, ek.sum())
print(ok, ok.sum())

chisq = ((ok - ek)**2. / ek).sum()
dof = 3
p_value = scipy.stats.chi2.cdf(chisq, dof)
print(f'Chisquare/ndof: {chisq:.2f}/{dof:d}')
print(f'p-value: {p_value:3e}')

plt.figure('esempio_poisson_cavalleria')
mpl_.bar(x - 0.1, ok, color='black', label='$o_k$')
mpl_.bar(x + 0.1, ek, color='gray', label='Poisson')
mpl_.setup_gca(xmin=-0.5, xmax=4.0, legend=True)


# Bombs on London.
N = 576
n = 537
p = 1. / N
mu = n * p
ok = np.array([229, 211, 93, 35, 7, 1])

x = np.arange(0, 6)
_probb = scipy.stats.binom.pmf(x, n, p)
_probb[5] = _probb[5] + (1. - _probb.sum())
yb = N * _probb
_probp = scipy.stats.poisson.pmf(x, mu)
_probp[5] = _probp[5] + (1. - _probp.sum())
yp = N * _probp
print(x)
print(_probb, _probb.sum())
print(_probp, _probp.sum())
print(yp, yp.sum())
print(ok, ok.sum())

chisq = ((ok - yp)**2. / yp).sum()
dof = 4
p_value = scipy.stats.chi2.cdf(chisq, dof)
print('Chisquare/ndof: {chisq:.2f}/{dof:d}')
print('p-value: {p_value:3e}')

plt.figure('esempio_poisson_bombe')
mpl_.bar(x - 0.2, ok, color='black', label='$o_k$')
mpl_.bar(x, yp, color='white', label='Binomiale')
mpl_.bar(x + 0.2, yp, color='gray', label='Poisson')
mpl_.setup_gca(xmin=-0.5, xmax=5.5, legend=True)

mpl_.save_all_figures()
