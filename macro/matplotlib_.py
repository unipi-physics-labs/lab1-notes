#!/usr/bin/env python
#
# Copyright (C) 2015--2021 Luca Baldini (luca.baldini@pi.infn.it).
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


"""matplotlib configuration module.

Note this underwent a major rwfactoring after version 4.3.0 of the book.
"""

import matplotlib
import numpy as np
import os
import sys

from matplotlib import pyplot as plt
from matplotlib.ticker import NullFormatter
from cycler import cycler

if sys.flags.interactive:
    plt.ion()


STATNOTES_MACRO = os.path.dirname(__file__)
STATNOTES_MACRO_DATA = os.path.join(STATNOTES_MACRO, 'data')
LATEX_FOLDER = os.path.join(STATNOTES_MACRO, os.pardir, 'latex')
FIGURE_FOLDER = os.path.join(LATEX_FOLDER, 'figures')
TABLE_FOLDER = os.path.join(LATEX_FOLDER, 'tables')
SNIPPETS_FOLDER = os.path.join(STATNOTES_MACRO, os.pardir, 'snippy')
SNIPPETS_DATA_FOLDER = os.path.join(SNIPPETS_FOLDER, 'data')

DEFAULT_FIG_WIDTH = 3.19
DEFAULT_FIG_HEIGHT = 2.65
MAX_FIG_HEIGHT = 9.
DEFAULT_FIG_SIZE = (DEFAULT_FIG_WIDTH, DEFAULT_FIG_HEIGHT)
DEFAULT_MARGINS = dict(bottom=0.16, top=0.96, left=0.195, right=0.95)
NORMAL_FONT_SIZE = 9
SMALL_FONT_SIZE = 8
SMALLER_FONT_SIZE = 7
QUOTE_LW = 0.75
QUOTE_TS = SMALLER_FONT_SIZE
DARK_GRAY = '0.32'
LIGHT_GRAY = '0.68'


def macro_file_path(file_name):
    """Return the full path to a file in the macro folder.
    """
    return os.path.join(STATNOTES_MACRO_DATA, file_name)

def load_file(file_name, **kwargs):
    """Load data from a text file.
    """
    return np.loadtxt(macro_file_path(file_name), **kwargs)

def setup_matplotlib():
    """Basic setup.
    """
    pgf_preamble = '\n'.join([
        r'\usepackage[nice]{nicefrac}',
        r'\usepackage{amsmath}',
        r'\usepackage[utf8]{inputenc}',
        '\DeclareUnicodeCharacter{2212}{\ensuremath{-}}'
        ])
    matplotlib.rc('pgf', texsystem='pdflatex', preamble=pgf_preamble)
    matplotlib.rc('figure', facecolor='white', figsize=DEFAULT_FIG_SIZE)
    matplotlib.rc('lines', linewidth=1.25, color='black', markersize=4.)
    matplotlib.rc('patch', linewidth=0.5, facecolor='black', edgecolor='eeeeee', antialiased=True)
    matplotlib.rc('text', hinting_factor=8, usetex=True)
    matplotlib.rc('mathtext', fontset='cm')
    matplotlib.rc('axes', xmargin=0., facecolor='white', edgecolor='black', grid=False, prop_cycle=cycler('color', 'kbgrcmy'))
    matplotlib.rc('grid', color=LIGHT_GRAY, linestyle='dashed', linewidth=0.25)
    matplotlib.rc('legend', fancybox=True, frameon=False, numpoints=1)
    matplotlib.rc('font', family='serif', serif=[], size=NORMAL_FONT_SIZE)
    matplotlib.rc('figure.subplot', **DEFAULT_MARGINS)


setup_matplotlib()


def setup_gca(xlabel=None, ylabel=None, xmin=None, xmax=None, ymin=None, ymax=None,
    logx=False, logy=False, grids=False, xticks=None, yticks=None, legend=False):
    """Setup the axes for the current plot.

    This is a convenience method that encapsulates some of the most common plot
    settings in a way that makes it easy to combine with other functions.
    All the plotting functions below accept keyword arguments to be passed to
    a setup_gca() call.
    """
    if logx is True:
        plt.xscale('log')
    if logy is True:
        plt.yscale('log')
    if xticks is not None:
        plt.gca().set_xticks(xticks)
    if yticks is not None:
        plt.gca().set_yticks(yticks)
    if xlabel is not None:
        plt.xlabel(xlabel)
    if ylabel is not None:
        plt.ylabel(ylabel)
    if xmin is None and xmax is None and ymin is None and ymax is None:
        pass
    else:
        plt.axis([xmin, xmax, ymin, ymax])
    if grids:
        plt.grid(which='both', dashes=[4., 4.])
    if legend:
        plt.legend()

def hist(data, bins=None, **kwargs):
    """Convenience function wrapping the plt.hist() function.
    """
    kwargs.setdefault('histtype', 'step')
    kwargs.setdefault('lw', 0.75)
    plt.hist(data, bins, **kwargs)

def errorbar(x, y, yerr=None, xerr=None, **kwargs):
    """Convenience function wrapping the plt.errorbar() function.
    """
    kwargs.setdefault('color', 'black')
    kwargs.setdefault('capsize', 3)
    kwargs.setdefault('fmt', 'o')
    plt.errorbar(x, y, yerr, xerr, **kwargs)

def bar(left, height, show_labels=False, labels=None, **kwargs):
    """Convenience function wrapping the plt.bar() function.
    """
    kwargs.setdefault('width', (max(left) - min(left)) / 50.)
    kwargs.setdefault('color', 'gray')
    kwargs.setdefault('edgecolor', 'black')
    kwargs.setdefault('align', 'center')
    plt.bar(left, height, **kwargs)
    if not show_labels:
        return
    delta = max(height) - min(height)
    offset = delta * 0.025
    if labels is None:
        labels = height
    fmt = dict(size=SMALL_FONT_SIZE, ha='center', va='bottom')
    for x, y, text in zip(left, height, labels):
        plt.text(x, y + offset, f'{text}', **fmt)

def axtext(x, y, text, **kwargs):
    """Draw text in axes coordinates.
    """
    plt.text(x, y, text, transform=plt.gca().transAxes, **kwargs)

def chisq_text(x, y, chisq, dof, **kwargs):
    """Draw a text label at a specied position specialized to hold the chisquare
    from a fit.

    The x and y coordinates are expressed in canvas relative coordinates, i.e.,
    fractions of the axis span.
    """
    kwargs.setdefault('ha', 'center')
    kwargs.setdefault('va', 'center')
    text = f'$\chi^2 = {chisq:.1f} / {dof}~\\mathrm{{dof}}$'
    axtext(x, y, text, **kwargs)

def marker(x, y, **kwargs):
    """Draw a marker.
    """
    kwargs.setdefault('color', 'black')
    kwargs.setdefault('markersize', 3)
    plt.plot([x], [y], 'o', **kwargs)

def horizontal_quote(y, x1, x2, text=None, color='gray', ls='dashed', lw=QUOTE_LW,
        markers=True, text_align='bottom', text_size=QUOTE_TS, text_offset=0.02):
    """Draw a horizontal ruler with a piece of text attached to it.
    """
    line(x1, y, x2, y, color=color, linestyle=ls, linewidth=lw)
    if markers:
        marker(x1, y, color=color)
        marker(x2, y, color=color)
    if text is None:
        return
    ymin, ymax = plt.gca().get_ylim()
    if plt.gca().get_xscale() == 'log':
        xt = (x1 * x2)**0.5
    else:
        xt = 0.5*(x1 + x2)
    if text_align == 'top':
        text_offset *= -1.
    if plt.gca().get_yscale() == 'log':
        yt = y * (ymax / ymin)**text_offset
    else:
        yt = y + text_offset * (ymax - ymin)
    plt.text(xt, yt, text, color=color, size=text_size, va=text_align, ha='center')

def vertical_quote(x, y1, y2, text=None, color='gray', ls='dashed', lw=QUOTE_LW,
    markers=True, text_align='left', text_size=QUOTE_TS, text_offset=0.02):
    """Draw a vertical ruler with a piece of text attached to it.
    """
    line(x, y1, x, y2, color=color, linestyle=ls, linewidth=lw)
    if markers:
        marker(x, y1, color=color)
        marker(x, y2, color=color)
    if text is None:
        return
    xmin, xmax = plt.gca().get_xlim()
    if text_align == 'right':
        text_offset *= -1.
    if plt.gca().get_xscale() == 'log':
        xt = x * (xmax / xmin)**text_offset
    else:
        xt = x + text_offset * (xmax - xmin)
    if plt.gca().get_yscale() == 'log':
        yt = (y1 * y2)**0.5
    else:
        yt = 0.5 * (y1 + y2)
    plt.text(xt, yt, text, color=color, size=text_size, rotation=90, va='center', ha=text_align)

def annotation(text, pos, text_pos, color=DARK_GRAY, text_size=QUOTE_TS,
               style='angle,angleA=0,angleB=90,rad=10'):
    """Annotate the current figure.
    """
    arrowprops = dict(arrowstyle="->", color=color, connectionstyle=style)
    plt.gca().annotate(text, xy=pos, xycoords='data', xytext=text_pos, textcoords='data',
        size=text_size, va='center', ha='center', color=color, arrowprops=arrowprops)





def residual_figure(figure_name=None, vscale=1.25, hspace=0.075):
    """Create a figure for a residual plot.
    """
    fig_kw = dict(num=figure_name, figsize=(DEFAULT_FIG_WIDTH, DEFAULT_FIG_HEIGHT * vscale))
    gridspec_kw = dict(height_ratios=[1.0, 1.5 * (vscale - 1.0)], hspace=hspace)
    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, gridspec_kw=gridspec_kw, **fig_kw)
    fig.align_ylabels()
    plt.sca(ax1)
    return fig, ax1, ax2

def large_figure(figure_name=None):
    """Create a large figure, i.e., twice as wide
    """
    fig = plt.figure(figure_name, figsize=(2.0 * DEFAULT_FIG_WIDTH, DEFAULT_FIG_HEIGHT))
    left = 0.5 * DEFAULT_MARGINS['left']
    right = 1.0 - 0.5 * (1.0 - DEFAULT_MARGINS['right'])
    top = DEFAULT_MARGINS['top']
    bottom = DEFAULT_MARGINS['bottom']
    plt.subplots_adjust(left=left, right=right, top=top, bottom=bottom)
    return fig

def huge_figure(figure_name=None):
    """Create a huge figure, i.e., taking up a full page.
    """
    fig = plt.figure(figure_name, figsize=(2.0 * DEFAULT_FIG_WIDTH, MAX_FIG_HEIGHT))
    left = 0.5 * DEFAULT_MARGINS['left']
    right = 1.0 - 0.5 * (1.0 - DEFAULT_MARGINS['right'])
    top = 1.0 - 0.5 * (1.0 - DEFAULT_MARGINS['top'])
    bottom = 0.5 * DEFAULT_MARGINS['bottom']
    plt.subplots_adjust(left=left, right=right, top=top, bottom=bottom)
    return fig






def curve(x, y, color='black', ls='solid', label=None, **kwargs):
    """Convenience function wrapping the plt.plot() function.

    Note this is calling setup_gca(**kwargs) at the end of the function body.
    """
    plt.plot(x, y, color='black', ls=ls, label=label)
    setup_gca(**kwargs)

def scatter(x, y, yerr=None, xerr=None, color='black', label=None, fillstyle='full', **kwargs):
    """Convenience function wrapping the plt.errorbar() function.

    Note this is calling setup_gca(**kwargs) at the end of the function body.
    """
    plt.errorbar(x, y, yerr, xerr, fmt='o', color=color, capsize=3, label=label,
        fillstyle=fillstyle)
    setup_gca(**kwargs)


def histogram(data, bins=None, orientation='vertical', **kwargs):
    """Create a histogram.

    Note this is calling setup_gca(**kwargs) at the end of the function body.
    """
    kwargs.setdefault('ylabel', 'Occorrenze')
    plt.hist(data, bins=bins, orientation=orientation, histtype='step', linewidth=0.75)
    setup_gca(**kwargs)


def line(x1, y1, x2, y2, **kwargs):
    """Draw a line.
    """
    line = plt.Line2D([x1, x2], [y1, y2], dashes=[3, 3], **kwargs)
    plt.gca().add_line(line)
    return line


def large_residual_figure(vscale=1.25):
    """Create a figure for a residual plot.
    """
    fig = plt.figure(figsize=(2*DEFAULT_FIG_WIDTH, DEFAULT_FIG_HEIGHT*vscale))
    left = 0.5*DEFAULT_MARGINS['left']
    right = 1 - 0.5*(1 - DEFAULT_MARGINS['right'])
    bot = DEFAULT_MARGINS['bottom']/vscale
    width = right - left
    mid = 0.2
    top = (1 - (1 - DEFAULT_MARGINS['top'])/vscale - mid - bot)
    frame1 = fig.add_axes((left, mid + bot, width, top))
    frame1.set_xticklabels([])
    frame2 = fig.add_axes((left, bot, width, mid))
    return fig, frame1, frame2

def scatter_hist_figure(figure_name=None, hscale=1.6, vscale=1.6, sep=0.001, inverse=False):
    """
    """
    width = DEFAULT_FIG_WIDTH * hscale
    height = DEFAULT_FIG_HEIGHT * vscale
    fig = plt.figure(figure_name, figsize=(width, height))
    # Calculate the dimensions.
    left = DEFAULT_MARGINS['left']/hscale
    rightm = (1 - DEFAULT_MARGINS['right'])/hscale
    width = 1./hscale - rightm - left
    bot = DEFAULT_MARGINS['bottom']/vscale
    topm = (1 - DEFAULT_MARGINS['top'])/vscale
    height = 1./vscale - topm - bot
    lefth = left + width + rightm + sep
    righth = 1 - rightm
    widthh = righth - lefth
    both = bot + height + topm + sep
    toph = 1 - topm
    heighth = toph - both
    # Create the actual panels.
    if not inverse:
        axs = plt.axes([left, bot, width, height])
        axhx = plt.axes([left, both, width, heighth])
        axhy = plt.axes([lefth, bot, widthh, height])
        # No labels.
        axhx.xaxis.set_major_formatter(NullFormatter())
        axhy.yaxis.set_major_formatter(NullFormatter())
    else:
        dx = rightm + sep
        dy = topm + sep
        axs = plt.axes([left + widthh + dx, bot + heighth + dy, width, height])
        axhx = plt.axes([left + widthh + dx, bot, width, heighth])
        axhy = plt.axes([left, bot + heighth + dy, widthh, height])
        # No labels.
        axs.xaxis.set_major_formatter(NullFormatter())
        axs.yaxis.set_major_formatter(NullFormatter())
    return fig, axs, axhx, axhy

def save_gcf():
    """Save the current matplotlib figure.
    """
    file_name = plt.gcf().get_label().lower().replace(' ', '_')
    if file_name == '':
        return
    file_name = f'{file_name}.pgf'
    file_path = os.path.join(FIGURE_FOLDER, file_name)
    print(f'Saving current figure to {file_path}...')
    try:
        plt.savefig(file_path, transparent=False)
    except IOError as e:
        logger.error(e)

def save_all_figures():
    """Save all the figures in memory to a given output folder.
    """
    for figid in plt.get_fignums():
        plt.figure(figid)
        save_gcf()























def property(key):
    """Return a given matplotlib configuration property.
    """
    return matplotlib.rcParams[key]

def save_current_figure(file_name, **kwargs):
    """Save the current figure to file.
    """
    file_path = os.path.join(FIGURE_FOLDER, file_name)
    print('Saving current figure to %s...' % file_path)
    plt.savefig(file_path, **kwargs)


def scatter_plot(x, y, dy=None, dx=None, xlabel=None, ylabel=None, logx=False,
                 logy=False, **kwargs):
    """Create a scatter plot.
    """
    plot = plt.errorbar(x, y, xerr=dx, yerr=dy, fmt='o', **kwargs)
    if xlabel:
        plt.xlabel(xlabel)
    if ylabel:
        plt.ylabel(ylabel)
    if logx:
        plt.xscale('log')
    if logy:
        plt.yscale('log')
    return plot

def bar_plot(left, height, width=None, xlabel=None, ylabel=None,
             show_values=False, bar_labels=None, **kwargs):
    """Create a bar plot.
    """
    if width is None:
        width = (max(left) - min(left))/50.
    if 'color' not in kwargs.keys():
        kwargs['color'] = 'gray'
    if 'edgecolor' not in kwargs.keys():
        kwargs['edgecolor'] = 'black'
    plot = plt.bar(left, height, width, align='center', **kwargs)
    if xlabel:
        plt.xlabel(xlabel)
    if ylabel:
        plt.ylabel(ylabel)
    if show_values:
        offset = 0.025*(max(height) - min(height))
        if bar_labels is None:
            bar_labels = height
        for _l, _h, _t in zip(left, height, bar_labels):
            plt.text(_l - 0.5*width, _h + offset, '%s' % _t,
                     size=SMALL_FONT_SIZE, horizontalalignment='center',
                     verticalalignment='bottom')
    return plot





def table_figure():
    """
    """
    fig = plt.figure(figsize=(2.25, 1.85))
    plt.subplots_adjust(left=0.18, bottom=0.18)
    return fig

def show_figures():
    """Remove me!
    """
    if sys.flags.interactive:
        plt.show()
