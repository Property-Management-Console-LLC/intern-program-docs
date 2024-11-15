Contributing to Documentation
===========================

This guide explains how to work with our Sphinx documentation system, including setting up your environment, making changes, and submitting contributions.

Setting Up Your Environment
-------------------------

Prerequisites
~~~~~~~~~~~~

* Python 3.8 or higher
* pip (Python package installer)
* Git

Initial Setup
~~~~~~~~~~~~

1. Clone the repository::

    git clone <repository-url>
    cd <repository-name>

2. Create and activate a virtual environment::

    python -m venv venv
    
    # On Windows
    .\venv\Scripts\activate
    
    # On Unix or MacOS
    source venv/bin/activate

3. Install required packages::

    pip install -r docs/requirements.txt

Documentation Structure
---------------------

The documentation is organized as follows::

    docs/
    ├── source/
    │   ├── conf.py           # Sphinx configuration file
    │   ├── index.rst         # Documentation homepage
    │   ├── _static/          # Static files (images, CSS, etc.)
    │   └── _templates/       # Custom HTML templates
    ├── build/                # Built documentation
    └── requirements.txt      # Python dependencies

Making Changes
-------------

Creating or Editing Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Navigate to the ``docs/source`` directory
2. Documentation files are written in reStructuredText (.rst) format
3. Basic RST syntax examples:

.. code-block:: rst

    Section Header
    =============

    Subsection Header
    ----------------

    Regular paragraph text.

    * Bullet point
    * Another bullet point

    1. Numbered item
    2. Another numbered item

    .. code-block:: python

        def example():
            return "Hello, World!"

    .. note::
       This is a note callout box.

    .. warning::
       This is a warning callout box.

Building Documentation Locally
~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Navigate to the docs directory::

    cd docs

2. Build the HTML documentation::

    make html

3. View the built documentation:

   * Open ``docs/build/html/index.html`` in your web browser
   * For Windows: ``start build/html/index.html``
   * For Unix/MacOS: ``open build/html/index.html``

Live Preview (Optional)
~~~~~~~~~~~~~~~~~~~~~

For real-time preview while editing:

1. Install sphinx-autobuild::

    pip install sphinx-autobuild

2. Run auto-build server::

    sphinx-autobuild source build/html

3. Open http://localhost:8000 in your browser

Submitting Changes
----------------

1. Create a new feature branch::

    git checkout -b feature/update-docs

2. Make your changes and build the documentation locally to verify them

3. Check for broken links and syntax errors::

    make linkcheck
    make doctest

4. Commit your changes::

    git add .
    git commit -m "docs: describe your changes"

5. Push to your feature branch::

    git push origin feature/update-docs

6. Create a pull request:

   * Go to the repository on GitHub
   * Click "New Pull Request"
   * Select your feature branch
   * Add a description of your changes
   * Request review from documentation maintainers

Best Practices
------------

File Organization
~~~~~~~~~~~~~~~

* Keep related topics in the same directory
* Use clear, descriptive filenames
* Follow the existing directory structure

Writing Style
~~~~~~~~~~~

* Use clear, concise language
* Include examples where appropriate
* Keep paragraphs focused and brief
* Use active voice

Code Examples
~~~~~~~~~~~

* Always test code examples
* Include comments for complex code
* Show both input and expected output

Images and Diagrams
~~~~~~~~~~~~~~~~

* Use SVG format when possible
* Include alt text for accessibility
* Keep file sizes reasonable

Cross-referencing
~~~~~~~~~~~~~~~

* Use proper RST cross-references
* Ensure all links work
* Include references to related documentation

Getting Help
----------

If you need assistance:

1. Check the `Sphinx documentation <https://www.sphinx-doc.org/>`_
2. Review existing documentation for examples
3. Contact the documentation team
4. Open an issue for documentation-related questions

Common Issues and Solutions
------------------------

Build Errors
~~~~~~~~~~

1. Missing Dependencies::

    pip install -r docs/requirements.txt

2. Cache Issues::

    make clean
    make html

3. Image Problems:

   * Ensure images are in ``_static``
   * Use relative paths
   * Check file permissions

RST Syntax
~~~~~~~~~

1. Indentation Errors:

   * Use consistent indentation (3 or 4 spaces)
   * Check code block formatting

2. Table Formatting:

   * Use grid tables for complex content
   * Simple tables for basic data
   * Align columns properly

.. note::
   Remember to build and test the documentation locally before submitting changes to ensure everything renders correctly.

.. tip::
   Use the ``sphinx-build -W`` flag to treat warnings as errors during local development to catch potential issues early.