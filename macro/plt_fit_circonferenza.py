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

import matplotlib_ as mpl_

np.random.seed(666)


def generate_points(N, sigma):
    """Generate a series of random points uniformly on a circle.
    """
    # Extract the data points.
    phi = np.linspace(0., 2. * np.pi, N)
    x = np.sin(phi)
    y = np.cos(phi)
    # Add the measurement errors.
    x += np.random.normal(0., sigma, N)
    y += np.random.normal(0., sigma, N)
    return x, y

def fit_circle(x, y, sigma):
    """Fit a series of data points to a circle.
    """
    N = len(x)
    # Refer coordinates to the mean values of x and y.
    x_m = np.mean(x)
    y_m = np.mean(y)
    u = x - x_m
    v = y - y_m
    # Calculate all the necessary sums.
    s_u = sum(u)
    s_uu = sum(u**2.)
    s_uuu = sum(u**3.)
    s_v = sum(v)
    s_vv = sum(v**2.)
    s_vvv = sum(v**3.)
    s_uv = sum(u * v)
    s_uuv = sum(u * u * v)
    s_uvv = sum(u * v * v)
    D = 2. * (s_uu * s_vv - s_uv**2.)
    # Calculate the best-fit values.
    u_c = (s_vv * (s_uuu + s_uvv) - s_uv * (s_vvv + s_uuv)) / D
    v_c = (s_uu * (s_vvv + s_uuv) - s_uv * (s_uuu + s_uvv)) / D
    x_c = u_c + x_m
    y_c = v_c + y_m
    r = np.sqrt(u_c**2. + v_c**2. + (s_uu + s_vv) / N)
    # Calculate the errors---mind this is only rigorously valid
    # if the data points are equi-spaced on the circumference.
    sigma_xy = sigma * np.sqrt(2. / N)
    sigma_r = sigma * np.sqrt(1. / N)
    return  x_c, y_c, r, sigma_xy, sigma_r

# Uncertainty on x and y, assumed to be the same for all the
# data points, in both coordinates.
sigma = 0.05
x, y = generate_points(25, sigma)
x_c, y_c, r, sigma_xy, sigma_r = fit_circle(x, y, sigma)

plt.figure('fit_circonferenza')
mpl_.scatter(x, y, sigma, sigma, xlabel='x [u.a.]', ylabel='y [u.a.]')
circle = plt.Circle((x_c, y_c), r, color='black', fill=False)
plt.gca().add_artist(circle)
plt.axis([-1.15, 1.15, -1.15, 1.15])
plt.gca().set_aspect('equal')

mpl_.save_all_figures()