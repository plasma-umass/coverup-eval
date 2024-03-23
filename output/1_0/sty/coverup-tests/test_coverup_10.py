# file sty/renderfunc.py:21-22
# lines [21, 22]
# branches []

import pytest
from sty.renderfunc import rgb_fg

def test_rgb_fg():
    # Test for correct ANSI escape sequence for RGB foreground
    assert rgb_fg(255, 0, 0) == "\x1b[38;2;255;0;0m", "Should return red color"
    assert rgb_fg(0, 255, 0) == "\x1b[38;2;0;255;0m", "Should return green color"
    assert rgb_fg(0, 0, 255) == "\x1b[38;2;0;0;255m", "Should return blue color"
    assert rgb_fg(0, 0, 0) == "\x1b[38;2;0;0;0m", "Should return black color"
    assert rgb_fg(255, 255, 255) == "\x1b[38;2;255;255;255m", "Should return white color"
