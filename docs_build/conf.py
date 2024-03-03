# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'bad examples'
copyright = '2024, Matt Dumont'
author = 'Matt Dumont'
release = 'v2.1.0'


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

# Auto API settings
autoapi_dirs = ['../src/komanawa/']  # The directory to process
autoapi_keep_files = True  # Keep the generated files (for debugging)
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# TODO commenting out any one of the following settings will cause the error to go away
extensions.extend([
    'sphinx.ext.viewcode', # note this setting is required for error!
])
extensions.append('autoapi.extension') # Note this setting is required for error!

autoapi_python_class_content = 'both' # Note this setting is required for error!
autoapi_options = ['inherited-members'] # Note this setting is required for error!
autoapi_python_use_implicit_namespaces = True # NOTE this setting is required for error!

