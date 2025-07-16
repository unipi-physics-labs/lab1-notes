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


FALSE_POSITIVE = 0.05

def prob(prior):
    """
    """
    return prior/(FALSE_POSITIVE*(1. - prior) + prior)


plt.figure()
x = np.logspace(-5, 0, 100)
y = prob(x)
plt.xscale('log')
plt.yscale('log')
plt.plot(x, y)
plt.xlabel('$P(B_c)$')
plt.ylabel('$P(B_c\,|\,R_c)$')
save_current_figure('rilevatore_banconote.pgf')

show_figures()
