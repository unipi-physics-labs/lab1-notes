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

import matplotlib.pyplot as plt

import matplotlib_ as mpl_


plt.figure('carta_bilogaritmica')
plt.loglog([], [])
mpl_.setup_gca(xmin=1.0, xmax=100.0, ymin=1.0, ymax=100.0, grids=True)

plt.figure('carta_semilogaritmica')
plt.semilogy([], [])
mpl_.setup_gca(xmin=0.0, xmax=1.0, ymin=1, ymax=100.0, grids=True)

mpl_.save_all_figures()
