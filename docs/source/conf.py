# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Takao"
copyright = "2023 Reupen Shah"
author = "Reupen Shah"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx_sitemap"]

templates_path = ["_templates"]
exclude_patterns = []

highlight_language = "python3"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "takao"
html_static_path = ["_static"]

sitemap_url_scheme = "{link}"
sitemap_filename = "pages.xml"
