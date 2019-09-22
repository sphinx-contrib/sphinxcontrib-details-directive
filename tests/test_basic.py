"""
    test_basic
    ~~~~~~~~~~

    :copyright: Copyright 2017-2019 by Takeshi KOMIYA
    :license: Apache License 2.0, see LICENSE for details.
"""

import pytest


@pytest.mark.sphinx('html')
def test_html_build(app, status, warning):
    app.build()
    content = (app.outdir / 'index.html').text()
    assert '<details><summary>caption</summary><p>blah blah blah</p>\n</details>' in content


@pytest.mark.sphinx('latex')
def test_latex_build(app, status, warning):
    app.build()
    content = (app.outdir / 'python.tex').text()
    assert '\n\ncaption\n\nblah blah blah\n\n' in content
