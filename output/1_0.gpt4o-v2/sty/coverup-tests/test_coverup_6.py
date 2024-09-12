# file: sty/rendertype.py:64-76
# asked: {"lines": [64, 65, 75, 76], "branches": []}
# gained: {"lines": [64, 65, 75, 76], "branches": []}

import pytest
from sty.rendertype import RgbBg

def test_rgbbg_initialization():
    r, g, b = 10, 20, 30
    rgb_bg = RgbBg(r, g, b)
    assert rgb_bg.args == [r, g, b]
