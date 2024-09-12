# file: sty/renderfunc.py:21-22
# asked: {"lines": [21, 22], "branches": []}
# gained: {"lines": [21, 22], "branches": []}

import pytest
from sty.renderfunc import rgb_fg

def test_rgb_fg():
    # Test with a set of RGB values
    result = rgb_fg(255, 0, 0)
    assert result == "\x1b[38;2;255;0;0m"
    
    result = rgb_fg(0, 255, 0)
    assert result == "\x1b[38;2;0;255;0m"
    
    result = rgb_fg(0, 0, 255)
    assert result == "\x1b[38;2;0;0;255m"
    
    result = rgb_fg(123, 45, 67)
    assert result == "\x1b[38;2;123;45;67m"
    
    result = rgb_fg(0, 0, 0)
    assert result == "\x1b[38;2;0;0;0m"
    
    result = rgb_fg(255, 255, 255)
    assert result == "\x1b[38;2;255;255;255m"
