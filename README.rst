===============================
sphinxcontrib-details-directive
===============================

``details`` directive for Sphinx

It enables ``details`` directive as an element to represent ``<details>``
element in HTML output. LaTeX output is via the ``sphinxdetails``
environment and ``\sphinxdetailssummary`` macro. In other output formats, the
directive contents are rendered as plain paragraphs.

Install
=======

Install the package via pip::

  $ pip install sphinxcontrib-details-directive

And append ``sphinxcontrib.details.directive`` to extensions list in your conf.py::

  extensions = ['sphinxcontrib.details.directive]

Directive
=========

**details**
  The ``details`` directive creates a ``<details>`` block containing following contents::

    .. details:: summary of the detail block

       description of the details block.
       blah blah blah

  It will be rendered with a ``<details>`` tag in HTML output. In LaTeX output,
  the contents of the directive will be wrapped in a ``sphinxdetails``
  environment. The summary, if present, will be rendered as the argument to a
  ``\sphinxdetailssummary`` macro. Customisation can be achieved by defining the
  environment and/or macro in the preamble. The default is simply to output the
  contents of the summary and directive. Outputting the summary and contents
  without further formatting is also the behaviour for all other output formats.

  ``:open:`` flag is allowed to indicate the details block is opened by default.
