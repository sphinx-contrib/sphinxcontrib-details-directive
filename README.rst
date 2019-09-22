===============================
sphinxcontrib-details-directive
===============================

``details`` directive for Sphinx

It enables ``details`` directive as an element to represent ``<details>`` element in HTML output.
It will be converted into mere paragraphs in other output formats.

## Install

Install the package via pip
```
$ pip install sphinxcontrib-details-directive
```

And append `sphinxcontrib.details.directive` to extensions list in your conf.py.
```
extensions = ['sphinxcontrib.details.directive]
```

## Directive

**details**

  ``details`` directive create a ``<details>`` block containing following contents::

    .. details:: summary of the detail block

       description of the details block.
       blah blah blah

   It will be rendered with ``<details>`` tag in HTML output.  On the other hand, for
   other output formats, it will be rendered as mere paragraphs.

   ``:open:`` flag is allowed to indicate the details block is opened by default.
