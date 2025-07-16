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

import matplotlib_ as mpl_


scores = {
    18: 1,
    22: 3,
    23: 13,
    24: 9,
    25: 3,
    26: 7,
    27: 15,
    28: 22,
    30: 12
    }

print(f'Number of students: {sum(scores.values())}')

plt.figure('voti_appello_esame')
mpl_.bar(scores.keys(), scores.values(), show_labels=True)
mpl_.setup_gca(xlabel='Voto [trentesimi]', ylabel='Occorrenze', xmin=17.0, xmax=31.0,
    xticks=range(18, 31), ymax=25.0)

mpl_.save_all_figures()
