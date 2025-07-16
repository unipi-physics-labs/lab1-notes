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

import scipy.stats
#from scipy.special import erf

QUANTILES = [0.005, 0.01, 0.05, 0.10, 0.25, 0.5, 0.75, 0.90, 0.95, 0.99, 0.995, 0.999, 0.9999]

output_file_path = os.path.join(TABLE_FOLDER, 'chisq1.tex')
output_file = open(output_file_path, 'w')
print('Writing output file %s...' % output_file_path)
# Write the header.
output_file.write('$\\nu / p$')
for q in QUANTILES:
    output_file.write(' & $%s$' % ('%.4f' % q).rstrip('0'))
output_file.write(' \\\\\n\\hline\n\\hline\n')
# Now the actual content.
for n in range(1, 41):
    line = '$%d$' % n
    for q in QUANTILES:
        x = scipy.stats.chi2.ppf(q, n)
        if x < 0.1:
            line += (' & $%.0e$' % x).replace('e-0', '$e-$')
        elif x >= 10:
            line += ' & $%.1f$' % x
        else:
            line += ' & $%.2f$' % x
    line += ' \\\\'
    output_file.write('%s\n' % line)
output_file.close()
print('Done.')


table_figure()
x = numpy.linspace(0, 10, 100)
y = scipy.stats.chi2.pdf(x, 5)
plt.plot(x, y)
mask = (x >= 0)*(x <= 3.5)
plt.gca().fill_between(x[mask], 0, y[mask], facecolor='gray', alpha=0.5)
plt.ylabel('$\\wp(x)$')
plt.axis([0, 10, 0, 0.2])
plt.yticks([0, 0.1, 0.2])
save_current_figure('tab_chisq1.pgf')

show_figures()
