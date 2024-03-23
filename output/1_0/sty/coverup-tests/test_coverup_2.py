# file sty/rendertype.py:64-76
# lines [64, 65, 75, 76]
# branches []

import pytest
from sty.rendertype import RgbBg

def test_rgb_bg_initialization():
    r, g, b = 10, 20, 30
    rgb_bg = RgbBg(r, g, b)
    assert rgb_bg.args == [r, g, b], "RgbBg did not initialize with the correct arguments"
