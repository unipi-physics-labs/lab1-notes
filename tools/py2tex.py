#!/usr/bin/env python
#
# Copyright (C) 2012--2025, Luca Baldini (luca.baldini@pi.infn.it).
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

"""Small script to pygmentize Python scripts and generate the corresponding
LaTeX output.
"""

import argparse
import pathlib
import subprocess
import sys

from loguru import logger

# Configure the logger.
logger.remove()
logger.add(sink=sys.stderr, colorize=True, format='>>> <level>{message}</level>')


STATNOTES_GITHUB_URL = 'https://github.com/unipi-physics-labs/statnotes/tree/main'

STATNOTES_ROOT = pathlib.Path(__file__).resolve().parent.parent
STATNOTES_PY = STATNOTES_ROOT / 'snippy'
STATNOTES_TEX = STATNOTES_ROOT / 'sniptex'
_OUTPUT_LATEX_SUBSTITUTIONS = {
    '😀' : r'\smiley',
    '' : '',
    '\\' : r'\textbackslash{}'
}
_NO_OUTPUT_SCRIPTS = []
_ENCODING = 'utf-8'


def pygmentize(snippet_path: str = STATNOTES_PY, random_seed: int = 1):
    """Run pygments on a python script and generate the corresponding LaTeX output.
    """
    # pylint: disable=use-dict-literal, too-many-locals
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
    if snippet_path.is_file() and snippet_path.suffix != '.py':
        raise RuntimeError(f'{snippet_path} is not a python file')

    # Now we are good to go with a single, good Python file!
    file_path = snippet_path.resolve()
    logger.info(f'Pygmentizing {file_path}...')
    # Pygmentize the script.
    cmd = f'pygmentize -f latex -O full -l python {file_path}'
    kwargs = dict(stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    with subprocess.Popen(cmd, **kwargs) as process:
        snippet_tex = process.stdout.read().decode()
    # Note at this point the LaTeX source is complete document with a long preamble,
    # and all we really care is whatever lies in the Verbatim block.
    snippet_tex = snippet_tex.split(r'\begin{Verbatim}[commandchars=\\\{\}]')[1]
    snippet_tex = snippet_tex.split(r'\end{Verbatim}')[0]

    # If necessary, run the script to capture the output and append it to the tex.
    if file_path.name not in _NO_OUTPUT_SCRIPTS:
        # Note the logic is quite convoluted, here, as one of the things we want to
        # achieve is to ensure that the output is reproducible, when random numbers
        # are involved, and that is less than trivial to achieve, as spawning a
        # subprocess implies that the snippets are running in a different Python
        # interpreter, and we don't want to explicitly set the seeds in the snippets,
        # as that would encourage bad practices. A (quite frankly, hacky) solution
        # is to do python -c "exec(open('file.py').read())" instead of the more
        # natural python file.py, so that we can prepend arbitrary code to the
        # script at runtime.
        cmd_string = f'exec(open(\'{file_path}\').read())'
        if 'random' in snippet_tex:
            # If the script uses random, we set the seed to ensure reproducibility.
            logger.debug(f'Setting the random seed to {random_seed}...')
            cmd_string = f'import numpy as np; np.random.seed({random_seed}); {cmd_string}'
        cmd = f'python -c "{cmd_string}"'
        # Note in this case we run the process in the parent folder of the target
        # script, in case the latter has relative paths to data files.
        with subprocess.Popen(cmd, cwd=file_path.parent, **kwargs) as process:
            errors = process.stderr.read().decode()
            if errors:
                logger.error(errors)
            snippet_output = process.stdout.read().decode()

            # Replace the bits that, for any reason, cannot be rendered in LaTeX
            for key, value in _OUTPUT_LATEX_SUBSTITUTIONS.items():
                if key in snippet_output:
                    logger.debug(f'Replacing {key} with {value}...')
                    snippet_output = snippet_output.replace(key, value)

        if len(snippet_output):
            logger.debug(f'Command output:\n{snippet_output}')
            snippet_tex = f'{snippet_tex}\n[Output]\n{snippet_output}'


    # Complete the information with the url to the snippet on github.
    url = f'{STATNOTES_GITHUB_URL}{str(file_path).replace(str(STATNOTES_ROOT), "")}'
    file_name = file_path.name.replace('_', r'\_')
    title = f'https://github.com/.../{file_name}'
    label = r'\makebox{\href{%s}{%s}}' % (url, title)

    # We are ready to write the output file.
    full_text = r'\begin{Verbatim}[label=%s,commandchars=\\\{\}]' % label
    full_text = f'{full_text}{snippet_tex}'
    full_text = '%s\\end{Verbatim}\n' % full_text
    output_file_path = STATNOTES_TEX / f'{file_path.stem}.tex'
    with open(output_file_path, 'w', encoding=_ENCODING) as output_file:
        output_file.write(full_text)
    logger.info('Done!')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('target')
    args = parser.parse_args()
    pygmentize(args.target)
