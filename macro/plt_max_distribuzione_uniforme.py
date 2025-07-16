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


from matplotlib_ import *

import math


plt.figure()
plt.plot([], [])
plt.axis([0, 1, 0, 1])
plt.xlabel('$x_1$')
plt.ylabel('$x_2$')
plt.plot([0, 1], [0, 1], ls='dotted', color='black')
for x in [0.25, 0.5, 0.75]:
    plt.plot([0, x, x], [x, x, 0], color='black')
    pad = 0.05
    plt.text(x, x + pad, '$\\max(x_1, x_2) = %.2f$' % x,
             ha='center', va='center')
save_current_figure('max_pdf_uniforme.pgf')

plt.figure()
plt.plot([0, 1, 1], [0, 2, 0])
plt.xlabel('$x = \\max(x_1, x_2)$')
plt.ylabel('$p(x)$')
plt.axis([0, 1.2, 0, 2.5])
save_current_figure('pdf_max_pdf_uniforme.pgf')

plt.figure()
plt.plot([0, 1, 1], [0, 2, 0])
plt.xlabel('$x = \\max(x_1, x_2)$')
plt.ylabel('$p(x)$')
plt.axis([0, 1.2, 0, 2.5])
mu = 2./3.
median = 1./math.sqrt(2)
mode = 1.
annotation('$\\mu$', (mu, 0.), (mu, 1.9), style='angle')
annotation('$\\mu_{1/2}$', (median, 0.), (median, 2.25), style='angle')
annotation('moda', (mode, 0.), (mode, 2.25), style='angle')
save_current_figure('pdf_max_pdf_uniforme_media.pgf')

plt.figure()
plt.plot([0, 1, 1], [0, 2, 0])
plt.xlabel('$x = \\max(x_1, x_2)$')
plt.ylabel('$p(x)$')
plt.axis([0, 1.2, 0, 2.5])
sigma = 1./math.sqrt(18)
hwhm = 0.25
annotation('$\\mu$', (mu, 0.), (mu, 2.2), style='angle')
annotation('$\\mu + \\sigma$', (mu + sigma, 0.), (mu + sigma, 2.2),
           style='angle')
plt.plot([0, 2], [1, 1], ls='dotted', color='black')
horizontal_quote(0.8, 0.5, 1, '\\textsc{FWHM}')
horizontal_quote(0.6, 0.75, 1, '\\textsc{HWHM}')
save_current_figure('pdf_max_pdf_uniforme_stdev.pgf')

show_figures()
