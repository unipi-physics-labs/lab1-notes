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

"""Helper functions.
"""

import logging
import os
import shutil
import sys


STATNOTES_TOOLS = os.path.abspath(os.path.dirname(__file__))
STATNOTES_ROOT = os.path.abspath(os.path.join(STATNOTES_TOOLS, os.pardir))
STATNOTES_LATEX = os.path.join(STATNOTES_ROOT, 'latex')
STATNOTES_LATEX_MISC = os.path.join(STATNOTES_LATEX, 'misc')
STATNOTES_LATEX_CHAPTERS = os.path.join(STATNOTES_LATEX, 'chapters')
STATNOTES_MACRO = os.path.join(STATNOTES_ROOT, 'macro')
STATNOTES_SNIPPETS = os.path.join(STATNOTES_ROOT, 'snippy')
STATNOTES_SPELLING = os.path.join(STATNOTES_ROOT, 'spelling')


MISC_LATEX_FILES = [os.path.join(STATNOTES_LATEX_MISC, file_name) for file_name in [
    'colophon.tex',
    'prefazione.tex'
    ]]

CHAPTER_LATEX_FILES = [os.path.join(STATNOTES_LATEX_CHAPTERS, file_name) for file_name in [
    'cambiamenti_variabile.tex',
    'campioni.tex',
    'complementi.tex',
    'distribuzioni.tex',
    'fit.tex',
    'introduzione.tex',
    'monte_carlo.tex',
    'numpy.tex',
    'primi_passi.tex',
    'probabilita.tex',
    'rappresentazione_dati.tex',
    'relazione.tex',
    'scipy.tex',
    'sistema_binario.tex',
    'strumenti.tex',
    'verosimiglianza.tex'
    ]]

LATEX_FILES = MISC_LATEX_FILES + CHAPTER_LATEX_FILES


class TerminalColors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def _color(text, color):
    """Process a piece of tect to be printed out in color.
    """
    return '%s%s%s' % (color, text, TerminalColors.ENDC)

def _red(text):
    """Process a piece of text to be printed out in red.
    """
    return _color(text, TerminalColors.RED)

def _yellow(text):
    """Process a piece of text to be printed out in yellow.
    """
    return _color(text, TerminalColors.YELLOW)

def _green(text):
    """Process a piece of text to be printed out in green.
    """
    return _color(text, TerminalColors.GREEN)


logger = logging.getLogger('statnotes')
logger.setLevel(logging.DEBUG)


class TerminalFormatter(logging.Formatter):

    """Logging terminal formatter class.
    """

    def format(self, record):
        """Overloaded format method.
        """
        text = ('>>> %s' % record.msg)
        if len(record.args) > 0:
            text = text % record.args
        if record.levelno >= logging.ERROR:
            text = _red(text)
        elif record.levelno == logging.WARNING:
            text = _yellow(text)
        return text


""" Configure the main terminal logger.
"""
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(TerminalFormatter())
logger.addHandler(console_handler)


def abort(message = ''):
    """Abort the execution (via a sys.exit) with a message.

    Use this with care, and opt for custom exceptions whenever possible.
    """
    if message != '':
        message = '%s. Abort.' % message
    else:
        message = 'Abort.'
    sys.exit(message)


def copy_file(src : str, dest : str):
    """Copy a file.
    """
    logger.info(f'Copying {src} -> {dest}...')
    shutil.copyfile(src, dest)


def backup_file(file_path: str, suffix : str = 'backup'):
    """Create a backup for a file.
    """
    dest = f'{file_path}.{suffix}'
    copy_file(file_path, dest)
    return dest


def remove_file(file_path: str):
    """Remove a file.
    """
    logger.info(f'Removing {file_path}...')
    os.remove(file_path)
