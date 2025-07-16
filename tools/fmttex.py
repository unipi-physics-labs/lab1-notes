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

from helpers import logger, copy_file, backup_file, remove_file, LATEX_FILES


# Dictionary containing all the patterns to be replaces, e.g., letters with accents
# spelled out in the TeX fashion.
_FMT_SWAP_DICT = {
    r'\`a': 'à',
    r'\`e': 'è',
    r'\`i': 'ì',
    r'\`o': 'ò',
    r'\`u': 'ù',
    r'\'e': 'é'
    }


def format_file(file_path : str, cleanup : bool=True):
    """Format a single LaTeX file.

    This is a basic preprocessing of the LaTeX source file intended to ensure
    consistency across the codebase and make life easier with the spell-checker
    while rigorously preserving the compiled output.
    """
    assert file_path.endswith('.tex')
    logger.info(f'Formatting {file_path}...')
    with open(file_path, 'r') as input_file:
        original_text = input_file.read()
    formatted_text = original_text
    for key, value in _FMT_SWAP_DICT.items():
        formatted_text = formatted_text.replace(key, value)
    if formatted_text == original_text:
        logger.info('Nothing to do.')
        return
    backup_path = backup_file(file_path)
    logger.info(f'Writing formatted text to {file_path}...')
    with open(file_path, 'w') as output_file:
        output_file.write(formatted_text)
    if cleanup:
        remove_file(backup_path)



if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='PROG')
    parser.add_argument('infiles', nargs='*')
    args = parser.parse_args()
    if len(args.infiles) == 0:
        args.infiles = LATEX_FILES
    for file_path in args.infiles:
        format_file(file_path)
