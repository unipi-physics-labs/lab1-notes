#!/usr/bin/env python
#
# Copyright (C) 2021, Luca Baldini (luca.baldini@pi.infn.it).
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU GengReral Public License as published by
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


import argparse
import os
import re
import subprocess

from helpers import LATEX_FILES, logger

ALLOWED_REPETITIONS = 'via'
ALLOWED_REPERITION_PATTERS = ('\\', '_', '&')

def check_repetitions(file_path):
    """
    """
    logger.info(f'Running wackamole on {file_path}...')
    with open(file_path, 'r') as input_file:
        tex = input_file.read()
    # Replace endlines with spaces
    tex = tex.replace(r'\n', ' ')
    words = tex.split()
    for i, word in enumerate(words[:-1]):
        # Have we a candidate repetition?
        if words[i + 1] == word:
            if word in ALLOWED_REPETITIONS:
                continue
            if sum([pattern in word for pattern in ALLOWED_REPERITION_PATTERS]):
                continue
            logger.warning(f'Possible repetition of {word}')



if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='PROG')
    parser.add_argument('infiles', nargs='*')
    args = parser.parse_args()
    if len(args.infiles) == 0:
        args.infiles = LATEX_FILES
    for file_path in args.infiles:
        check_repetitions(file_path)
