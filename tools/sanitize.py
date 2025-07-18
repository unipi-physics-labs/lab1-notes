#!/usr/bin/env python
#
# Copyright (C) 2021--2025, Luca Baldini (luca.baldini@pi.infn.it).
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

"""Small script to sanitize LaTeX files in order to make them more interoperable
with spell-checking in Italian.
"""

import argparse
import pathlib
import sys

from loguru import logger

# Configure the logger.
logger.remove()
logger.add(sink=sys.stderr, colorize=True, format='>>> <level>{message}</level>')


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

_ENCODING = 'utf-8'


def sanitize(file_path: str):
    """Format a single LaTeX file.

    This is a basic preprocessing of the LaTeX source file intended to ensure
    consistency across the codebase and make life easier with the spell-checker
    while rigorously preserving the compiled output.
    """
    # First thing first, if the path to the snippet(s) is not a pathlib.Path
    # instance, we turn it into one.
    if not isinstance(file_path, pathlib.Path):
        file_path = pathlib.Path(file_path)
    # If the target path does not exist, we raise an exception.
    if not file_path.exists():
        raise RuntimeError(f'Target path {file_path} does not exist')
    # If the target path is a folder, then we sanitize all the tex files within
    # the folder calling the function recursively.
    if file_path.is_dir():
        logger.info(f'Sanitizing folder {file_path}...')
        for _path in file_path.iterdir():
            if _path.is_file() and _path.suffix == '.tex':
                sanitize(_path)
        return
    if file_path.is_file() and file_path.suffix != '.tex':
        raise RuntimeError(f'{file_path} is not a tex file')

    logger.info(f'Formatting {file_path}...')
    # Open the input file and read the content.
    with open(file_path, 'r', encoding=_ENCODING) as input_file:
        original_text = input_file.read()
    # Format the text.
    formatted_text = original_text
    for key, value in _FMT_SWAP_DICT.items():
        formatted_text = formatted_text.replace(key, value)
    if formatted_text == original_text:
        logger.debug('Nothing to do.')
        return
    # Write the output file.
    logger.info(f'Writing formatted text to {file_path}...')
    with open(file_path, 'w', encoding=_ENCODING) as output_file:
        output_file.write(formatted_text)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('target')
    args = parser.parse_args()
    sanitize(args.target)
