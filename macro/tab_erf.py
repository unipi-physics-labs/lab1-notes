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


from matplotlib_ import *
from scipy.stats import norm
from scipy.special import erf

SQRT2 = numpy.sqrt(2.)


output_file_path = os.path.join(TABLE_FOLDER, 'erf1.tex')
output_file = open(output_file_path, 'w')
print('Writing output file %s...' % output_file_path)
# Write the header.
output_file.write('$z$')
for i in range(9, -1, -1):
    output_file.write(' & $%d$' % i)
output_file.write(' \\\\\n\\hline\n\\hline\n')
# Now the actual content.
for x in numpy.arange(-3.9, 0.1, 0.1):
    line = '$%.1f$' % x
    if not line.startswith('$-'):
        line = '$-%.1f$' % x
    for dx in numpy.linspace(-0.09, 0, 10):
        line += ' & $%.5f$' % (0.5 + 0.5*erf((x + dx)/SQRT2))
    line += ' \\\\'
    output_file.write('%s\n' % line)
output_file.close()
print('Done.')


table_figure()
x = numpy.linspace(-4, 4, 100)
y = norm.pdf(x, 0., 1)
plt.plot(x, y)
mask = (x >= -10)*(x <= -1.5)
plt.gca().fill_between(x[mask], 0, y[mask], facecolor='gray', alpha=0.5)
plt.xlabel('$z$')
plt.ylabel('$N(z)$')
plt.axis([-4, 4, 0, 0.5])
save_current_figure('tab_erf1.pgf')

output_file_path = os.path.join(TABLE_FOLDER, 'erf2.tex')
output_file = open(output_file_path, 'w')
print('Writing output file %s...' % output_file_path)
# Write the header.
output_file.write('$z$')
for i in range(10):
    output_file.write(' & $%d$' % i)
output_file.write(' \\\\\n\\hline\n\\hline\n')
# Now the actual content.
for x in numpy.arange(0, 4, 0.1):
    line = '$%.1f$' % x
    for dx in numpy.linspace(0, 0.09, 10):
        line += ' & $%.5f$' % (0.5 + 0.5*erf((x + dx)/SQRT2))
    line += ' \\\\'
    output_file.write('%s\n' % line)
output_file.close()
print('Done.')


table_figure()
x = numpy.linspace(-4, 4, 100)
y = norm.pdf(x, 0., 1)
plt.plot(x, y)
mask = (x >= -10)*(x <= 1.5)
plt.gca().fill_between(x[mask], 0, y[mask], facecolor='gray', alpha=0.5)
plt.xlabel('$z$')
plt.ylabel('$N(z)$')
plt.axis([-4, 4, 0, 0.5])
save_current_figure('tab_erf2.pgf')


output_file_path = os.path.join(TABLE_FOLDER, 'erf3.tex')
output_file = open(output_file_path, 'w')
print('Writing output file %s...' % output_file_path)
# Write the header.
output_file.write('$z$')
for i in range(10):
    output_file.write(' & $%d$' % i)
output_file.write(' \\\\\n\\hline\n\\hline\n')
# Now the actual content.
for x in numpy.arange(0, 4, 0.1):
    line = '$%.1f$' % x
    for dx in numpy.linspace(0, 0.09, 10):
        line += ' & $%.5f$' % (0.5*erf((x + dx)/SQRT2))
    line += ' \\\\'
    output_file.write('%s\n' % line)
output_file.close()
print('Done.')


table_figure()
x = numpy.linspace(-4, 4, 100)
y = norm.pdf(x, 0., 1)
plt.plot(x, y)
mask = (x >= 0)*(x <= 1.5)
plt.gca().fill_between(x[mask], 0, y[mask], facecolor='gray', alpha=0.5)
plt.xlabel('$z$')
plt.ylabel('$N(z)$')
plt.axis([-4, 4, 0, 0.5])
save_current_figure('tab_erf3.pgf')


output_file_path = os.path.join(TABLE_FOLDER, 'erf4.tex')
output_file = open(output_file_path, 'w')
print('Writing output file %s...' % output_file_path)
# Write the header.
output_file.write('$z$')
for i in range(10):
    output_file.write(' & $%d$' % i)
output_file.write(' \\\\\n\\hline\n\\hline\n')
# Now the actual content.
for x in numpy.arange(0, 4, 0.1):
    line = '$%.1f$' % x
    for dx in numpy.linspace(0, 0.09, 10):
        line += ' & $%.5f$' % (erf((x + dx)/SQRT2))
    line += ' \\\\'
    output_file.write('%s\n' % line)
output_file.close()
print('Done.')


table_figure()
x = numpy.linspace(-4, 4, 100)
y = norm.pdf(x, 0., 1)
plt.plot(x, y)
mask = (x >= -1.5)*(x <= 1.5)
plt.gca().fill_between(x[mask], 0, y[mask], facecolor='gray', alpha=0.5)
plt.xlabel('$z$')
plt.ylabel('$N(z)$')
plt.axis([-4, 4, 0, 0.5])
save_current_figure('tab_erf4.pgf')


output_file_path = os.path.join(TABLE_FOLDER, 'erf5.tex')
output_file = open(output_file_path, 'w')
print('Writing output file %s...' % output_file_path)
# Write the header.
output_file.write('$z$')
for i in range(10):
    output_file.write(' & $%d$' % i)
output_file.write(' \\\\\n\\hline\n\\hline\n')
# Now the actual content.
for x in numpy.arange(4, 8, 0.1):
    line = '$%.1f$' % x
    for dx in numpy.linspace(0, 0.09, 10):
        line += ' & $%.2e$' % (0.5 - 0.5*erf((x + dx)/SQRT2))
    line = line.replace('e-', '$e-$')
    line += ' \\\\'
    output_file.write('%s\n' % line)
output_file.close()
print('Done.')


table_figure()
x = numpy.linspace(-4, 4, 100)
y = norm.pdf(x, 0., 1)
plt.plot(x, y)
mask = (x >= 1.5)*(x <= 4)
plt.gca().fill_between(x[mask], 0, y[mask], facecolor='gray', alpha=0.5)
plt.xlabel('$z$')
plt.ylabel('$N(z)$')
plt.axis([-4, 4, 0, 0.5])
save_current_figure('tab_erf5.pgf')


show_figures()
