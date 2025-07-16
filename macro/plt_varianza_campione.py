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

from matplotlib_ import *

np.random.seed(666)

SAMPLE_SIZE = 8
NUM_TRIALS = 100000
BINNING = np.linspace(0, 3, 50)

def sample_variance(x):
    """
    """
    m = sum(x) / float(SAMPLE_SIZE)
    return sum((x - m)**2) / float(SAMPLE_SIZE)

vals = []
for i in range(NUM_TRIALS):
    x = np.random.normal(0, 1, size=SAMPLE_SIZE)
    s = sample_variance(x)
    vals.append(s)
vals_biased = np.array(vals)
vals_unbiased = vals_biased*SAMPLE_SIZE/(SAMPLE_SIZE - 1.)

plt.figure()
hist(vals_biased, bins=BINNING, label='$s_n^2$')
hist(vals_unbiased, bins=BINNING, color='gray', label='$s_{n-1}^2$')
plt.axis([None, None, 0, 8500])
plt.xlabel('Varianza campione')
plt.legend()
plt.text(0.25, 7500, '$n = %d$' % SAMPLE_SIZE)
plt.text(0.25, 6700, '$\sigma^2 = 1$')
line(1, 0, 1, 8500)
save_current_figure('bias_varianza_campione.pgf')

print (abs(vals_biased - 1.) < abs(vals_unbiased - 1.).sum())
print (abs(vals_biased - 1.) >= abs(vals_unbiased - 1.).sum())

show_figures()
