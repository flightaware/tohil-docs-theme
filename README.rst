Tohil Docs Sphinx Theme
=========================

This is the theme for the Tohil documentation, heavily heavily based on
the theme for the Python documentation at https://github.com/python/python-docs-theme.

Note that when adopting this theme, you're also borrowing an element of the
trust and credibility established by the CPython core developers over the
years. That's fine, and you're welcome to do so for other Python community
projects if you so choose, but please keep in mind that in doing so you're also
choosing to accept some of the responsibility for maintaining that collective
trust.

To use the theme, install it into your docs build environment via ``pip`` 
(preferably in a virtual environment).


Configuration options
---------------------

To use this theme, add the following to ``conf.py``:

- ``html_theme = 'tohil_docs_theme'``

- ``html_sidebars``, defaults taken from http://www.sphinx-doc.org/en/stable/config.html#confval-html_sidebars

But really you probably want to start with this or the Python theme or whatever, and
change the theme.conf, etc.
