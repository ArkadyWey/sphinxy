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
    'sphinx.ext.napoleon', 
    'sphinx.ext.githubpages', 
    "sphinx_multiversion",]
# 'autodoc' helps sphinx read docstrings as documentation 
# 'napoleon' helps sphinx read docstrings that aren't in .rst format as documentation.
# 'githubpages' automatically adds a  .nojekyll file at html so that pages doesn't use jekyll (static site generator) sicne we are using sphinx
# 'sphinx_multiversion' to use sphinx-multiversion package to version the documentation.

autoclass_content = "both"
# add the option to display documentation both from a class docstring and its __init__ methods’s

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo" #'alabaster'
html_static_path = ['_static']
html_favicon = "_static/favicon.ico"

# Ask sphinx to use template html file to add sidebar
templates_path = [
    "_templates",
]

# Use defaults for the rest of the sidebar options from furo
html_sidebars = {
    "**": [
        "sidebar/brand.html",
        "sidebar/search.html",
        "sidebar/scroll-start.html",
        "sidebar/navigation.html",
        "sidebar/versioning.html",
        "sidebar/scroll-end.html",
    ],
}

# -- Sphinx Multiversion --------------------------------------------------
# https://holzhaus.github.io/sphinx-multiversion/master/configuration.html#
smv_tag_whitelist = r'^v\d+\.\d+\.\d+$'
smv_branch_whitelist = r'^.*$'
smv_remote_whitelist = r'^.*$'

