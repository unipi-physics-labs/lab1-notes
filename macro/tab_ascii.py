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

NUM_ROWS = 16
NUM_COLS = 128 // NUM_ROWS
NUM_CHARS = NUM_ROWS * NUM_COLS
SPEC = 'll@{\\hskip 20pt}' * (NUM_ROWS // 2)
HEADER = '  \\texttt{\n' +\
('    \\begin{tabular*}{\\textwidth}{%s}\n' % SPEC) + \
'    \\hline\n'
FOOTER = '    \\hline\n' \
'  \end{tabular*}\n' \
'  }\n'

SPECIAL_CHAR_DICT = {
    0  : '\\NUL (NUL)',
    1  : '\\SOH (SOH)',
    2  : '\\STX (STX)',
    3  : '\\ETX (ETX)',
    4  : '\\EOT (EOT)',
    5  : '\\ENQ (ENQ)',
    6  : '\\ACK (ACK)',
    7  : '\\BEL (BEL)',
    8  : '\\BS  BSs)',
    9  : '~ (TAB)',
    10 : '\\LF (LF)',
    11 : '\\VT (VT)',
    12 : '~  (NP)',
    13 : '\\CR (CR)',
    14 : '\\SO (SO)',
    15 : '\\SI (SI)',
    16 : '\\DLE (DLE)',
    17 : '\\DCa (DC1)',
    18 : '\\DCb (DC2)',
    19 : '\\DCc (DC3)',
    20 : '\\DCd (DC4)',
    21 : '\\NAK (NAK)',
    22 : '\\SYN (SYN)',
    23 : '\\ETB (ETB)',
    24 : '\\CAN (CAN)',
    25 : '\\EM (EM)',
    26 : '~ (EOF)',
    27 : '\\ESC (ESC)',
    28 : '\\FS (FS)',
    29 : '\\GS (GS)',
    30 : '\\RS (RS)',
    31 : '\\US (US)',
    32 : '\\textvisiblespace',
    35 : '\\#',
    36 : '\\$',
    37 : '\\%',
    38 : '\\&',
    39 : '\\textquotesingle',
    39 : '\\textquoteright',
    92 : '\\char`\\\\',
    94 : '\\^{}',
    95 : '\\char`\\_',
    123: '\\char`\\{',
    125: '\\char`\\}',
    126: '\\~{}',
    127: '\\DEL (DEL)'
}


output_file_path = os.path.join(TABLE_FOLDER, 'ascii_table.tex')
output_file = open(output_file_path, 'w')
print('Writing output file %s...' % output_file_path)

output_file.write(HEADER)
for row in range(NUM_ROWS):
    line = ''
    for col in range(NUM_COLS):
        i = row + col * NUM_ROWS
        ch = SPECIAL_CHAR_DICT.get(i, chr(i))
        line = f'{line} {i} & {ch} & '
    line = line[:-2]
    output_file.write(f'   {line}\\\\\n')
    print(line)

output_file.write(FOOTER)
print('Closing output file.')
output_file.close()
