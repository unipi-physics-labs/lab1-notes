#!/usr/bin/env python
#
# Copyright (C) 2021, Luca Baldini (luca.baldini@pi.infn.it).
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
import scipy.special
import scipy.stats
import scipy.interpolate

import matplotlib_ as mpl_


dof_max = 50
dof = np.linspace(1, dof_max, 101)
dof_grid = np.geomspace(1, dof_max, 500)
dof0 = 14.5
qm = scipy.stats.norm().cdf(-1.)
qp = scipy.stats.norm().cdf(1.)


def norm_chi2_ppf(q, dof):
    """Return the chisquare ppf normalized to the degrees of freedom.
    """
    return scipy.stats.chi2(dof).ppf(q) / dof


mpl_.huge_figure('chi2_quantiles')
# Loop over the quantiles and plot the ppf.
text_kwargs = dict(va='center', ha='center', backgroundcolor='white')
for q in (0.001, 0.01, 0.05, qm, 0.25, 0.75, qp, 0.95, 0.99, 0.999):
    spline = scipy.interpolate.InterpolatedUnivariateSpline(dof, norm_chi2_ppf(q, dof), k=3)
    plt.plot(dof_grid, spline(dof_grid), color='black')
    plt.text(dof0, norm_chi2_ppf(q, dof0), '$%.3f$' % q, **text_kwargs)

# Plot the lines corresponding to the Gaussian approximations at +/- 1 sigma.
delta = np.sqrt(2. * dof_grid) / dof_grid
kwargs = dict(ls='dashed', color='gray')
plt.plot(dof_grid, 1. + delta, **kwargs)
plt.plot(dof_grid, 1. - delta, **kwargs)

# Setup the plots.
mpl_.setup_gca(grids=True, xmin=1.0, xmax=dof_max, ymin=0.0, ymax=3.0, logx=True)
labels = [''] * dof_max
for i in range(10):
    labels[i] = i + 1
for i in range(19, dof_max, 10):
    labels[i] = i + 1
plt.xticks(np.linspace(1., dof_max, dof_max), labels)
plt.yticks(np.linspace(0., 3., 31))
plt.xlabel(r'$\nu$')
plt.ylabel(r'Quantili normalizzati della distribuzione del $\chi^2$')
plt.tight_layout()

mpl_.save_all_figures()
