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


plt.figure()
plt.plot([], [])
plt.axis([0, 1, 0, 1])
plt.xlabel('$x_1$')
plt.ylabel('$x_2$')
for x in [0.5, 1, 1.5]:
    plt.plot([0, x], [x, 0], color='black')
    pad = 0.03
    plt.text(0.5*x - pad, 0.5*x - pad, '$x_1 + x_2 = %.1f$' % x,
             ha='center', va='center', rotation=-41)
save_current_figure('somma_pdf_uniforme.pgf')

plt.figure()
x = np.linspace(0, 2, 100)
y = 1 - abs(x - 1)
plt.plot(x, y)
plt.xlabel('$x = x_1 + x_2$')
plt.ylabel('$p(x)$')
plt.axis([0, 2, 0, 1.2])
save_current_figure('pdf_somma_pdf_uniforme.pgf')

show_figures()
