#!/usr/bin/env python
#
# Copyright (C) 2017--2021, Luca Baldini (luca.baldini@pi.infn.it).
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


# Years
years = [1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009]
# Number people who drowned by falling into a swimming-pool
deaths = [109, 102, 102, 98, 85, 95, 96, 98, 123, 94, 102]
#Number of films Nicolas Cage appeared in
movies = [2, 2, 2, 3, 1, 1, 2, 3, 4, 1, 4]
# Age of Miss America
age = [24, 24, 24, 21, 22, 21, 24, 22, 20, 19, 22]
# Murders by steam, hot vapours and hot objects
murders = [7, 7, 7, 3, 4, 3, 8, 4, 2, 3, 2]

plt.figure('nicolas_cage')
mpl_.scatter(movies, deaths, xlabel='Numero di film con Nicolas Cage', xmin=0.0, xmax=5.0,
    ylabel='Numero di affogamenti in piscina', ymin=80.0, ymax=130.0)
for x, y, l in zip(movies, deaths, years):
    if l == 2008:
        y -= 1
    plt.text(x + 0.12, y, f'{l}', size=mpl_.SMALLER_FONT_SIZE)
r = np.corrcoef(movies, deaths)[1, 0]
mpl_.axtext(0.1, 0.85, f'$r = {r:.2f}$')

plt.figure('miss_america')
mpl_.scatter(age, murders, xlabel='Et\`a di miss America', xmin=18.0, xmax=25.0,
    ylabel='Numero di omicidi "caldi"', ymin=1.0, ymax=9.0)
for x, y, l in zip(age, murders, years):
    if l in (1999, 2003, 2004):
        y -= 0.25
    if l == 2001:
        y += 0.25
    plt.text(x + 0.15, y, f'{l}', size=mpl_.SMALLER_FONT_SIZE)
r = np.corrcoef(age, murders)[1,0]
mpl_.axtext(0.1, 0.85, f'$r = {r:.2f}$')

mpl_.save_all_figures()
