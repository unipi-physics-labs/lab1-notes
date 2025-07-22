# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information



project = 'lab1-notes'
copyright = '2025, Luca Baldini'
author = 'Luca Baldini'
with open('../version.tex') as version_file:
    release = version_file.read().strip()
language = 'it'

def _asset_url(name, label):
    return f'https://github.com/unipi-physics-labs/lab1-notes/releases/download/{release}/{name}-{release}.pdf'

rst_prolog = f"""
.. |version| replace:: {release}
.. |statnotes_url| replace:: {_asset_url('statnotes', 'Statistica')}
"""

print(rst_prolog)

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
