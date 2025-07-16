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

w = mpl_.load_file('cfsb.csv')

plt.figure('cfsb')
mpl_.hist(w, bins=np.linspace(19.5, 21.5, 50))
mpl_.setup_gca(xlabel='Contenuto della confezione [oz]', ylabel='Occorrenze')
mpl_.annotation('Contenuto nominale', (20.0, 0.0), (20.0, 720.0), style='angle')

mpl_.save_all_figures()
