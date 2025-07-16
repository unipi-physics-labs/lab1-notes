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

import numpy as np
from scipy.optimize import curve_fit

def exponential(x, norm, scale, origin=0.):
    """Simple exponential fitting model.
    """
    return norm * np.exp((x - origin) / scale)


def power_law(x, norm, index):
    """Power-law fitting model.
    """
    return norm * x**index


def _filter_data(x, y, sigma=None, xmin=None, xmax=None):
    """Filter data to fit in sub-ranges.
    """
    if xmin is not None:
        mask = x >= xmin
        x, y = x[mask], y[mask]
        if sigma is not None:
            sigma = sigma[mask]
    if xmax is not None:
        mask = x <= xmax
        x, y = x[mask], y[mask]
        if sigma is not None:
            sigma = sigma[mask]
    return x, y, sigma


def fit_exponential(x, y, sigma=None, xmin=None, xmax=None, **kwargs):
    """Small wrapper around scipy.optimize.curve_fit() for an exponential fit.
    """
    x, y, sigma = _filter_data(x, y, sigma, xmin, xmax)
    popt, pcov = curve_fit(exponential, x, y, sigma=sigma, **kwargs)
    norm, scale, *_ = popt
    sigma_norm, sigma_scale, *_ = np.sqrt(pcov.diagonal())
    t2 = scale * np.log(2.)
    print('Exponential best-fit parameters')
    print(f'Normalization = {norm:.3e}, scale = {scale:.3f} +/- {sigma_scale:.3f}, doubling time = {t2:.3f}')
    return popt, pcov


def fit_power_law(x, y, sigma=None, xmin=None, xmax=None, **kwargs):
    """Small wrapper around scipy.optimize.curve_fit() for an exponential fit.
    """
    x, y, sigma = _filter_data(x, y, sigma, xmin, xmax)
    popt, pcov = curve_fit(power_law, x, y, sigma=sigma, **kwargs)
    norm, index = popt
    sigma_norm, sigma_index = np.sqrt(pcov.diagonal())
    print('Power-law best-fit parameters')
    print(f'Normalization = {norm:.3e} +/- {sigma_norm:.3e}, index = {index:.3f} +/- {sigma_index:.3f}')
    return popt, pcov
