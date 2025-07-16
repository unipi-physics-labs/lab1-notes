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

from helpers import STATNOTES_SPELLING, LATEX_FILES, logger


STATNOTES_WORD_LIST = os.path.join(STATNOTES_SPELLING, 'statnotes_word_list.txt')



def _expand_re(base, *args):
    """Expand a generic re pattern.
    """
    return [base % arg for arg in args]

def _expand_re_optional(base):
    """Expand a re pattern in the {.*} and [.*]{.*} form, i.e., to allow for
    optional args.
    """
    return [r'%s{.*}' % base, r'%s%s{.*}' % (base, RE_OPT_ARG)]

def _expand_multiline():
    """
    """
    pass



# re pattern matching a LaTeX optional argument, i.e., [.*]
RE_OPT_ARG = '\[.*\]'

# Patterns related to the \label \ref LaTeX mechanism. This is somewhat more
# complicated than just \label{.*} because we want to make sure the reference
# names are consistent, and that equations are always referred to with \eqref.
RE_REF_PATTERNS =\
    _expand_re(r'\\label{%s:}', 'eq', 'exp', 'fig', 'sec', 'snip', 'tab') +\
    _expand_re(r'\\ref{%s:}', 'exp', 'fig', 'sec', 'snip', 'tab') +\
    [r'\\eqref{eq:.*}']

# pgffigs commands come in different declinations and with and without
# optional arguments.
RE_PGFFIG_PATTERNS =\
    _expand_re_optional(r'\\pgffig(.*)')

# Filtering out simple commands of the form \cmd{.*}, all in one line.
RE_CMD_PATTERNS =\
    _expand_re(r'\\%s{.*}', 'cite', 'code', 'href', 'input', 'npcmd', 'npfunc',
        'npmodule', 'pyfunc', 'pymodule', 'scipycmd', 'scipyfunc', 'scipymodule')

# Snippets.
RE_SNIP_PATTERNS =\
    _expand_re_optional(r'\\snip')

# Match the beginning of all the environments where we can pass optional arguments,
# such as \begin{figure}[htb] or required arguments, such as \begin{tabular}{ccc}
RE_BEGINENV_PATTERNS =\
    _expand_re(r'\\begin{%%s}%s' % RE_OPT_ARG, 'array', 'examplebox', 'figure', 'snippet', 'table') +\
    _expand_re(r'\\begin{%s}{.*}', 'tabular')

# Math stuff.
RE_MATH_PATTERNS = [r'\$.*\$']



RE_PATTERNS = RE_REF_PATTERNS + RE_PGFFIG_PATTERNS + RE_CMD_PATTERNS +\
    RE_SNIP_PATTERNS + RE_BEGINENV_PATTERNS + RE_MATH_PATTERNS + [
    r'\\foreign{.*}',
    r'(\\begin{Verbatim}.*\n)(.+)((?:\n.+)+)(\n\\end{Verbatim})',
    r'(\\begin{quotation}.*\n)(.+)((?:\n.+)+)(\n\\end{quotation})',
    r'\[.*pt\]',
    r'(\\begin{align})(.+)((?:\n.+)+)(\n\\end{align})', # This is too greedy
    r'\\foreign{(.+)((?:\n.+)+)}', # This is too greedy
]



def run_aspell(file_path, dict_='it', verbose=True):
    """Run aspell on a single file and print out the mis-spelled words.
    """
    logger.info(f'Running aspell on {file_path}...')
    with open(file_path, 'r') as input_file:
        tex = input_file.read()
    # Filtering the tex source to accommodate specific patterns.
    tex = tex.replace(r'\-', '')
    for pattern in RE_PATTERNS:
        if verbose:
            logger.info(f'Matching {pattern}...')
            for match in re.findall(pattern, tex):
                logger.info(f'{match}')
        tex = re.sub(pattern, '', tex)
    # Run aspell...
    cmd = ['aspell', '-t', '-d', dict_, '--list', '--add-wordlists', STATNOTES_WORD_LIST]
    output = subprocess.check_output(cmd, input=tex, text=True)
    word_list = list(set(output.split('\n')))
    word_list.sort()
    for word in word_list:
        if len(word) > 0:
            logger.warning(word)



class Dictionary:

    """
    https://superuser.com/questions/137957

    For some languages, e.g. Italian, expanding is not enough and you will have
    to do some more processing to get a list of plain words.

    This is the command I use to get a list of words in Italian (note that it
    will take some time to perform):

    aspell -d it dump master | aspell -l it expand | sed "s/\w*'//g;s/ \+/\n/g" |
    awk '{ print tolower($0) }' | uniq > wordlist.txt
    """

    def __init__(self, file_path):
        """
        """
        self.word_set = self.load_word_list(file_path)

    @staticmethod
    def load_word_list(file_path):
        """
        """
        logging.info(f'Loading word list from {file_path}...')
        with open(file_path, 'r') as input_file:
            word_list = [word.strip('\n') for word in input_file.readlines()]
        logging.info(f'Done, {len(word_list)} word(s) found.')
        return set(word_list)

    def contains(self, word):
        """
        """
        return word in self.word_set



if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='PROG')
    parser.add_argument('infiles', nargs='*')
    parser.add_argument('--dict', '-d', type=str, default='it',
        help='the built-in dictionary to be used')
    parser.add_argument('--verbose', '-v', action='store_true', default=False,
        help='print out re matching debug information')
    args = parser.parse_args()
    if len(args.infiles) == 0:
        args.infiles = LATEX_FILES
    for file_path in args.infiles:
        run_aspell(file_path, args.dict, args.verbose)
