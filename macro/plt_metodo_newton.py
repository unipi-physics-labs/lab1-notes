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
from latex import *

def f(x):
    """
    """
    return np.cos(x) - x

def der(x):
    """
    """
    return -np.sin(x) - 1

def nextx(x):
    """
    """
    return x - f(x)/der(x)

def radix():
    """
    """
    return np.log(-C/OFFSET)/LAMBDA

X_MIN = -2
X_MAX = 10
X_0 = 9.


plt.figure()
x = np.linspace(X_MIN, X_MAX, 100)
plt.plot(x, f(x))
plt.plot(x, np.zeros(len(x)), color='black', ls='dotted')
plt.xlabel('$x$')
plt.ylabel('$f(x) = \cos x - x$')

x1 = nextx(X_0)
x2 = nextx(x1)
yt = 0.5
marker(X_0, 0)
plt.text(X_0, yt, '$x_0$', ha='center', va='bottom')
line(X_0, 0, X_0, f(X_0), color=DARK_GRAY)
marker(X_0, f(X_0))
line(X_0, f(X_0), x1, 0, color=DARK_GRAY)
marker(x1, 0)
plt.text(x1, yt, '$x_1$', ha='center', va='bottom')
line(x1, 0, x1, f(x1), color=DARK_GRAY)
marker(x1, f(x1))
line(x1, f(x1), x2, 0, color=DARK_GRAY)
marker(x2, 0)
plt.text(x2, yt, '$x_2$', ha='center', va='bottom')
line(x2, 0, x2, f(x2), color=DARK_GRAY)
marker(x2, f(x2))
save_current_figure('metodo_newton.pgf')

open_table_file('metodo_newton.tex')
x = X_0
prevx = None
for i in range(7):
    if prevx is None:
        delta = '-'
    else:
        delta = x - prevx
    data = [i, x, format_number(delta)]
    write_table_row(data)
    prevx = x
    x = nextx(x)
close_current_file()

show_figures()
