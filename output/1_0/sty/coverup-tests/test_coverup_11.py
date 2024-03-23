# file sty/renderfunc.py:25-26
# lines [25, 26]
# branches []

import pytest
from sty.renderfunc import rgb_bg

def test_rgb_bg():
    # Test with valid RGB values
    assert rgb_bg(255, 255, 255) == "\x1b[48;2;255;255;255m", "Should return the correct escape code for white background"
    assert rgb_bg(0, 0, 0) == "\x1b[48;2;0;0;0m", "Should return the correct escape code for black background"
    assert rgb_bg(128, 64, 32) == "\x1b[48;2;128;64;32m", "Should return the correct escape code for a brown background"
