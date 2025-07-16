# Copyright (C) 2022, Luca Baldini (luca.baldini@pi.infn.it).
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


import os
import glob as glob

import numpy as np
import matplotlib.pyplot as plt

from wordcloud import WordCloud


SIZE = (1000, 1000)
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
FILE_LIST = glob.glob(os.path.join(ROOT_DIR, 'latex', 'chapters', '*.tex'))

BLACK_LIST = ['begin', 'end', 'align', 'eqref', 'emph', 'label', 'foreign',
    'subsection', 'nicefrac', 'section', 'expect', 'example', 'examplebox',
    'pgffigone',
    'abbiamo', 'allora', 'possiamo', 'questo', 'quello', 'questa', 'sezione',
    'nostro', 'nostra', 'dunque']

print('Reading input files...')
text = ''.join(open(file_path, 'r').read() for file_path in FILE_LIST)
print('Done.')

# Generate the mask.
width, height = SIZE
radius = round(min(width, height) * 0.45)
x, y = np.ogrid[:width, :height]
mask = (x - width // 2) ** 2 + (y - height // 2) ** 2 > radius ** 2
mask = 255 * mask.astype(int)

# Generate the actual cloud.
wc = WordCloud(width=500, height=500, background_color="white", mask=mask,
    min_word_length=6, stopwords=BLACK_LIST)
wc.generate(text)

# Show the figure.
plt.axis("off")
plt.tight_layout()
plt.imshow(wc, interpolation="bilinear")
plt.show()
