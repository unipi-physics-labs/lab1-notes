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


import os
import time
import os
import sys
import subprocess
import zipfile
import glob
import shutil

""" Rudimental release manager.
"""

TAG_MODES = ['major', 'minor', 'patch']

STATNOTES_BIN = os.path.abspath(os.path.dirname(__file__))
STATNOTES_ROOT = os.path.abspath(os.path.join(STATNOTES_BIN, os.pardir))
STATNOTES_LATEX = os.path.join(STATNOTES_ROOT, 'latex')
STATNOTES_PDF = os.path.join(STATNOTES_ROOT, 'pdf')
TAG_FILE_PATH = os.path.join(STATNOTES_LATEX, 'version.tex')



def cmd(cmd, verbose=False, dry_run=False):
    """ Exec a command.

    This uses subprocess internally and returns the subprocess status code
    (if the dry_run option is true the function will just print the command out
    through the logger and returns happily).
    """
    print('About to execute "%s"...' % cmd)
    if dry_run:
        print('Just kidding (dry run).')
        return 0
    err = subprocess.PIPE
    out = subprocess.PIPE
    process = subprocess.Popen(cmd, stdout=out, stderr=err, shell=True)
    errorCode = process.wait()
    if verbose:
        output = process.stdout.read().strip(b'\n')
        for line in output.split(b'\n'):
            print(line)
    if not errorCode:
        print('Command executed with status code %d.' % errorCode)
    else:
        print('Command returned status code %d.' % errorCode)
    errorMessages = process.stderr.read().strip(b'\n')
    if errorMessages:
        print('stderr not empty, error/warning message(s) following...')
        print(errorMessages)
    return errorCode


def cp(src, dest):
    """ Copy a file in another location.
    """
    print('Copying %s to %s...' % (src, dest))
    shutil.copy(src, dest)

def read_tag():
    """ Read the tag and build date straight from the appropriate file.
    """
    return open(TAG_FILE_PATH).readline().strip('\n')

def update_version_file(mode, dry_run=False):
    """ Update the __tag__.py module with the new tag and build date.
    """
    prev_tag = read_tag()
    print('Previous tag was %s...' % prev_tag)
    version, release, patch = [int(item) for item in prev_tag.split('.')]
    if mode == 'major':
        version += 1
        release = 0
        patch = 0
    elif mode == 'minor':
        release += 1
        patch = 0
    elif mode == 'patch':
        patch += 1
    else:
        abort('Unknown release mode %s.' % mode)
    next_tag = '%s.%s.%s' % (version, release, patch)
    print('Writing new tag (%s) to %s...' % (next_tag, TAG_FILE_PATH))
    if not dry_run:
        outputFile = open(TAG_FILE_PATH, 'w')
        outputFile.writelines('%s\n' % next_tag)
        outputFile.close()
    print('Done.')
    return next_tag

def compile_latex():
    """ Recompile the damned thing.
    """
    os.system('cd %s; make' % STATNOTES_LATEX)

def release(mode, dry_run=False):
    """ Tag the package and create a release.
    """
    cmd('git pull', verbose=True, dry_run=dry_run)
    cmd('git status', verbose=True, dry_run=dry_run)
    tag = update_version_file(mode, dry_run)
    compile_latex()
    src = os.path.join(STATNOTES_LATEX, 'statnotes.pdf')
    dest = os.path.join(STATNOTES_PDF, 'statnotes_%s.pdf' % tag)
    pwd = os.getcwd()
    cp(src, dest)
    dest = dest.replace(pwd, '').rstrip('/')
    #cmd('git add %s' % dest)
    #cmd('git commit -m "Initial import" %s' % dest)
    dest = os.path.join(STATNOTES_PDF, 'statnotes_head.pdf')
    cp(src, dest)
    dest = dest.replace(pwd, '').rstrip('/')
    cmd('git commit -m "Initial import" %s' % dest)    
    msg = 'Prepare for tag %s.' % tag
    cmd('git commit -a -m "%s"' % msg, verbose=True, dry_run=dry_run)
    cmd('git push', verbose=True, dry_run=dry_run)
    msg = 'tagging version %s' % tag
    cmd('git tag -a %s -m "%s"' % (tag, msg), verbose=True, dry_run=dry_run)
    cmd('git push --tags', verbose=True, dry_run=dry_run)
    cmd('git status', verbose=True, dry_run=dry_run)
    return tag



if __name__ == '__main__':
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option('-t', dest='tagmode', type=str, default=None,
                      help='The release tag mode %s.' % TAG_MODES)
    parser.add_option('-n', action='store_true', dest='dryrun',
                      help='Dry run (i.e. do not actually do anything).')
    (opts, args) = parser.parse_args()
    if opts.tagmode not in TAG_MODES:
        parser.error('Invalid tag mode %s (allowed: %s)' %\
                     (opts.tagmode, TAG_MODES))
    release(opts.tagmode, opts.dryrun)




