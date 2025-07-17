#!/usr/bin/env python
#
# Copyright (C) 2025, Luca Baldini (luca.baldini@pi.infn.it).
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
import pathlib
import subprocess

from loguru import logger


STATNOTES_GITHUB_URL = 'https://github.com/unipi-physics-labs/statnotes/tree/main'

STATNOTES_ROOT = pathlib.Path(__file__).resolve().parent.parent
STATNOTES_TEXCODE = STATNOTES_ROOT / 'texcode'
STATNOTES_SNIPPETS = STATNOTES_ROOT / 'snippets'


NO_OUTPUT_SCRIPTS = []


def pygmentize(snippet_path: str = STATNOTES_SNIPPETS, label: bool = True):
    """Run pygments on a python script and generate the corresponding LaTeX output.
    """
    # First thing first, if the path to the snippet(s) is not a pathlib.Path
    # instance, we turn it into one.
    if not isinstance(snippet_path, pathlib.Path):
        snippet_path = pathlib.Path(snippet_path)
    # If the target path does not exist, we raise an exception.
    if not snippet_path.exists():
        raise RuntimeError(f'Target path {snippet_path} does not exist')
    # If the target path is a folder, then we pygmentize all the Python files within
    # the folder calling the function recursively.
    if snippet_path.is_dir():
        logger.info(f'Pygmentizing folder {snippet_path}...')
        for _path in snippet_path.iterdir():
            if _path.is_file() and _path.suffix == '.py':
                pygmentize(_path)
        return
    elif snippet_path.is_file() and snippet_path.suffix != '.py':
        raise RuntimeError(f'{snippet_path} is not a python file')

    # Now we are good to go with a single, good Python file!
    file_path = snippet_path.resolve()
    logger.info(f'Pygmentizing {file_path}...')
    # Pygmentize the script.
    cmd = f'pygmentize -f latex -O full -l python {file_path}'
    kwargs = dict(stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    snippet_tex = subprocess.Popen(cmd, **kwargs).stdout.read().decode()
    # Note at this point the LaTeX source is complete document with a long preamble,
    # and all we really care is whatever lies in the Verbatim block.
    snippet_tex = snippet_tex.split(r'\begin{Verbatim}[commandchars=\\\{\}]')[1]
    snippet_tex = snippet_tex.split(r'\end{Verbatim}')[0]

    # If necessary, run the script to capture the output and append it to the tex.
    if file_path.name not in NO_OUTPUT_SCRIPTS:
        cmd = f'python {file_path}'
        # Note in this case we run the process in the parent folder of the target
        # script, in case the latter has relative paths to data files.
        process = subprocess.Popen(cmd, cwd=file_path.parent, **kwargs)
        errors = process.stderr.read().decode()
        if errors:
            logger.error(errors)
        snippet_output = process.stdout.read().decode()
        if len(snippet_output):
            logger.debug(f'Command output:\n{snippet_output}')
            snippet_tex = f'{snippet_tex}\n[Output]\n{snippet_output}'

    # Complete the information with the url to the snippet on github.
    url = f'{STATNOTES_GITHUB_URL}{str(file_path).replace(str(STATNOTES_ROOT), "")}'
    title = f'https://github.com/.../{file_path.name}'
    label = r'\makebox{\href{%s}{%s}}' % (url, title)

    # We are ready to write the output file.
    full_text = r'\begin{Verbatim}[label=%s,commandchars=\\\{\}]' % label
    full_text = f'{full_text}{snippet_tex}'
    full_text = '%s\end{Verbatim}\n' % full_text
    output_file_path = STATNOTES_TEXCODE / f'{file_path.stem}.tex'
    with open(output_file_path, 'w') as output_file:
        output_file.write(full_text)
    logger.info('Done!')


if __name__ == '__main__':
    from optparse import OptionParser
    parser = OptionParser(usage = 'usage: %prog files')
    (opts, args) = parser.parse_args()
    if len(args) == 0:
        import glob
        args = glob.glob(os.path.join(STATNOTES_SNIPPETS, '*.py'))
    for file_path in args:
        pygmentize(file_path)
