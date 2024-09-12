# file: sty/renderfunc.py:25-26
# asked: {"lines": [25, 26], "branches": []}
# gained: {"lines": [25, 26], "branches": []}

import pytest
from sty.renderfunc import rgb_bg

def test_rgb_bg():
    result = rgb_bg(255, 0, 0)
    assert result == "\x1b[48;2;255;0;0m"

    result = rgb_bg(0, 255, 0)
    assert result == "\x1b[48;2;0;255;0m"

    result = rgb_bg(0, 0, 255)
    assert result == "\x1b[48;2;0;0;255m"

    result = rgb_bg(123, 45, 67)
    assert result == "\x1b[48;2;123;45;67m"
