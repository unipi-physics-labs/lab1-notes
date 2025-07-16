#!/usr/bin/env python
#
# Copyright (C) 2016, Luca Baldini (luca.baldini@pi.infn.it).
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


import glob
import os
import subprocess

STATNOTES_BITBUCKET_URL = 'https://bitbucket.org/lbaldini/statnotes/src/master/'
STATNOTES_BIN = os.path.abspath(os.path.dirname(__file__))
STATNOTES_ROOT = os.path.abspath(os.path.join(STATNOTES_BIN, os.pardir))
STATNOTES_TEXCODE = os.path.join(STATNOTES_ROOT, 'latex', 'texcode')
STATNOTES_SNIPPETS = os.path.join(STATNOTES_ROOT, 'snippets')


NO_OUTPUT_SCRIPTS = []


def pygmentize(file_path, label = True):
    """Run pygments on a python script and generate the corresponding
    LaTeX output.

    This is achieved through something along the lines of:
    pygmentize -f latex -O full -l python -o factorial_1.tex factorial_1.py
    """
    if os.path.isdir(file_path):
        print('Pygmentizing folder %s...' % file_path)
        for scriptPath in glob.glob(os.path.join(file_path, '*.py')):
            pygmentize(scriptPath)
        return
    if not file_path.endswith('.py'):
        print('%s does not look like a python file, skipping...'% file_path)
        return
    print('Running pygments...')
    cmd = 'pygmentize -f latex -O full -l python %s' % file_path
    process = subprocess.Popen(cmd, stdout = subprocess.PIPE,
                               stderr = subprocess.PIPE, shell = True)
    # At this point we have the full pygmentized output available and we
    # do have to extract the relevant part.
    file_path = os.path.abspath(file_path)
    file_name = os.path.basename(file_path)
    output_file_path = os.path.join(STATNOTES_TEXCODE,
                                  file_name.replace('.py', '.tex'))
    print('Generating output file %s...' % output_file_path)
    output_file = open(output_file_path, 'w')
    doWrite = False
    for line in process.stdout.readlines():
        line = line.decode()
        if line.startswith('\\begin{Verbatim}'):
            if label:
                text = os.path.basename(file_path).replace('_', '\_')
                folder = os.path.dirname(file_path).replace(STATNOTES_ROOT, '')
                folder = folder.strip('\/')
                #title = os.path.join(folder, text)
                title = text
                url = os.path.join(STATNOTES_BITBUCKET_URL, folder, text)
                text = '\\makebox{\\href{%s}{https://bitbucket.org/.../%s}}' %\
                       (url, title)
                line = line.replace('[', '[label=%s,' % text)
            doWrite = True
        elif line.startswith('\\end{Verbatim}'):
            doWrite = False
        if doWrite:
            output_file.write(line)
    if os.path.basename(file_path) not in NO_OUTPUT_SCRIPTS:
        os.chdir(os.path.dirname(file_path))
        cmd = 'python %s' % file_path
        process = subprocess.Popen(cmd, stdout = subprocess.PIPE,
                                   stderr = subprocess.PIPE, shell = True)
        error = process.stderr.read()
        if error:
            print(error)
        output = process.stdout.read().decode()
        if len(output):
            print('Adding command output...')
            text = '\n[Output]\n%s' % output
            output_file.write(text)
        os.chdir(STATNOTES_ROOT)
    output_file.write('\\end{Verbatim}')
    output_file.close()
    print('Done, closing output file.')



if __name__ == '__main__':
    from optparse import OptionParser
    parser = OptionParser(usage = 'usage: %prog files')
    (opts, args) = parser.parse_args()
    if len(args) == 0:
        import glob
        args = glob.glob(os.path.join(STATNOTES_SNIPPETS, '*.py'))
    for file_path in args:
        pygmentize(file_path)
