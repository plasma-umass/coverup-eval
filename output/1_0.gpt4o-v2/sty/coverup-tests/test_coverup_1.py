# file: sty/rendertype.py:49-61
# asked: {"lines": [49, 50, 60, 61], "branches": []}
# gained: {"lines": [49, 50, 60, 61], "branches": []}

import pytest
from sty.rendertype import RgbFg

def test_rgbfg_initialization():
    r, g, b = 100, 150, 200
    rgb_fg = RgbFg(r, g, b)
    assert rgb_fg.args == [r, g, b]
