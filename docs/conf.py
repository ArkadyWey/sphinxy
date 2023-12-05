# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Sphinxy'
copyright = '2023, Arkady Wey'
author = 'Arkady Wey'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon']
# 'autodoc' helps sphinx read docstrings as documentation 
# 'napoleon' helps sphinx read docstrings that aren't in .rst format as documentation.

autoclass_content = "both"
# add the option to display documentation both from a class docstring and its __init__ methods’s

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo" #'alabaster'
html_static_path = ['_static']
