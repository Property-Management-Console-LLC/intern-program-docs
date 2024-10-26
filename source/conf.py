# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
project = 'Intern Program Documentation'
copyright = '2024, Property Management Console'
author = 'Property Management Console'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
extensions = ['sphinx_rtd_theme']
templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# GitHub Pages configuration
# Remove the baseurl as it's not correct for GitHub Pages
# html_baseurl = 'https://github.com/Property-Management-Console-LLC/intern-program-docs/docs'  # Remove this line
html_use_static_path = True

# GitHub context for proper resource paths
html_context = {
    'display_github': True,
    'github_user': 'Property-Management-Console-LLC',
    'github_repo': 'intern-program-docs',
    'github_version': 'main/docs/',
}

# Custom CSS files
html_css_files = [
    'custom.css',
]

# Make sure URLs are relative
html_theme_options = {
    'canonical_url': '',
    'analytics_id': '',
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'style_nav_header_background': '#2980B9',
    # Toc options
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}

# Important for GitHub Pages
master_doc = 'index'