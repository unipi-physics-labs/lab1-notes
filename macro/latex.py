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


"""Simple facility to write out LaTeX objects such as tables.
"""

import os

from matplotlib_ import TABLE_FOLDER


__OUTPUT_FILE = None


def open_table_file(file_name):
    """
    """
    global __OUTPUT_FILE
    file_path = os.path.join(TABLE_FOLDER, file_name)
    print('Opening output file %s...' % file_path)
    __OUTPUT_FILE = open(file_path, 'w')
    return __OUTPUT_FILE

def close_current_file():
    """
    """
    __OUTPUT_FILE.close()
    print('Current file closed.')

def format_number(val, precision=5, threshold=0.01):
    """
    """
    if isinstance(val, str):
        return val
    fmt = '%%.%df' % precision
    if val == 0:
        return '0'
    if abs(val) < threshold:
        val = '%e' % val
        mant, exp = str(val).split('e')
        mant = fmt % float(mant)
        exp = int(exp)
        return '%s \\times 10^{%d}' % (mant, exp)
    else:
        return fmt % val

def write_table_row(data, fmt=None):
    """
    """
    if fmt is None:
        fmt = '%s'
    if isinstance(fmt, str):
        fmt = [fmt]*len(data)
    line = ''
    for i, val in enumerate(data):
        line += '$%s$ & ' % (fmt[i] % val)
    line = line.strip('& ')
    line += '\\\\\n'
    __OUTPUT_FILE.write(line)
