# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Servicio Webhook Odoo'
copyright = '2024, Soltein S.A.'
author = 'Soltein S.A.'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.todo', 'sphinx.ext.autodoc', 'sphinxcontrib.sass']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'venv']

language = 'es'

# build sass
import sass
css = sass.compile(
    dirname=('_sass', '_static/css'),
)

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

import sphinx_theme_pd
html_theme = 'sphinx_theme_pd'
html_theme_path = [sphinx_theme_pd.get_html_theme_path()]
html_static_path = ['_static']
html_logo = '_static/img/logosol.png'
html_style = 'css/soltein.css'
html_title = 'Soltein Webhook Odoo'


