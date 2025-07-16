#!/usr/bin/env python
#
# Copyright (C) 2015--2021 Luca Baldini (luca.baldini@pi.infn.it).
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

# Values measured with the caliper.
true_l1 = 5.412
true_l2 = 4.323
num_bins = 40
label = 'misurando (calibro cinquantesimale)'

l1, l2 = mpl_.load_file('interpolazione_metro.txt', unpack=True)

plt.figure('interpolazione_metro_1')
mpl_.hist(l1, bins=np.linspace(5.2, 5.7, num_bins))
mpl_.setup_gca(xmin=5.2, xmax=5.7, ymin=0., ymax=13., xlabel='$l$~[cm]', ylabel='Occorrenze')
mpl_.annotation(label, (true_l1, 0.), (true_l1, 11.), style='angle')

plt.figure('interpolazione_metro_2')
mpl_.hist(l2, bins=np.linspace(4.1, 4.6, num_bins))
mpl_.setup_gca(xmin=4.1, xmax=4.6, ymin=0., ymax=13., xlabel='$l$~[cm]', ylabel='Occorrenze')
mpl_.annotation(label, (true_l2, 0.), (true_l2, 11.), style='angle')
fmt = dict(color=mpl_.LIGHT_GRAY, lw=0.75, ls='dashed')
plt.axvline(4.3, **fmt)
plt.axvline(4.4, **fmt)

mpl_.save_all_figures()
