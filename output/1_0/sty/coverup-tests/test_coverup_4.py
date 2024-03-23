# file sty/rendertype.py:49-61
# lines [49, 50, 60, 61]
# branches []

import pytest
from sty.rendertype import RgbFg

def test_rgb_fg_initialization():
    # Test initialization of RgbFg
    red = 100
    green = 150
    blue = 200
    rgb_fg = RgbFg(red, green, blue)
    
    # Assert that the arguments are stored correctly
    assert rgb_fg.args == [red, green, blue]
