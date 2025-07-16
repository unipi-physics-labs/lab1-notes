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

offset = 0.25
exponent = 4.

def f(x):
    """Function.
    """
    return offset + x**exponent

def der(x):
    """Derivative.
    """
    return exponent*(x**(exponent - 1))

def tangent(x):
    """Tangent line.
    """
    return f(x0) + der(x0) * (x - x0)

fmt = dict(color='gray')

plt.figure('linearizzazione_errore_max')
x0 = 0.8
dx = 0.075
x = np.linspace(0., 1., 100)
plt.plot(x, f(x))
mpl_.setup_gca(xmin=0., xmax=1., ymin=0., ymax=1., xlabel='$x$', ylabel='$f(x)$')
y0 = f(x0)
mpl_.marker(x0, y0)
plt.plot(x, tangent(x), lw=mpl_.QUOTE_LW, **fmt)
mpl_.vertical_quote(x0, 0, y0, markers=False, **fmt)
mpl_.vertical_quote(x0 + dx, 0, tangent(x0 + dx), markers=False, **fmt)
mpl_.vertical_quote(x0 - dx, 0, tangent(x0 - dx), markers=False, **fmt)
mpl_.horizontal_quote(y0, 0, x0, markers=False, **fmt)
mpl_.horizontal_quote(tangent(x0 + dx), 0, x0 + dx, markers=False, **fmt)
mpl_.horizontal_quote(tangent(x0 - dx), 0, x0 - dx, markers=False, **fmt)
mpl_.marker(x0 + dx, tangent(x0 + dx), **fmt)
mpl_.marker(x0 - dx, tangent(x0 - dx), **fmt)
mpl_.horizontal_quote(0.25, x0, x0 + dx, '$\\Delta x$', **fmt)
mpl_.vertical_quote(0.25, f(x0), tangent(x0 + dx), '$\\Delta f$', **fmt)
mpl_.annotation('$P = (\\hat{x}, f(\\hat{x}))$', (x0, y0), (0.4, 0.9), **fmt)

plt.figure('sviluppo_taylor_lineare')
x0 = 0.75
dx = 0.15
x = np.linspace(0., 1., 100)
plt.plot(x, f(x))
mpl_.setup_gca(xmin=0.5, xmax=1., ymin=0.2, ymax=1.15, xlabel='$x$', ylabel='$f(x)$')
y0 = f(x0)
mpl_.marker(x0, y0, **fmt)
mpl_.annotation('$P = (x_0, f(x_0))$', (x0, y0), (0.6, 0.9), **fmt)
mpl_.horizontal_quote(f(x0), x0, x0 + dx, '$(x - x_0)$', text_align='top', **fmt)
text = '$\\left| \\frac{df}{dx}(x_0) \\right| (x - x_0)$'
mpl_.vertical_quote(x0 + dx, f(x0), tangent(x0 + dx), text, text_offset=0.05, **fmt)
plt.plot(x, tangent(x), lw=mpl_.QUOTE_LW, **fmt)

mpl_.save_all_figures()
