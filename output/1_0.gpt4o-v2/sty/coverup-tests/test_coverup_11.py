# file: sty/rendertype.py:23-33
# asked: {"lines": [23, 24, 32, 33], "branches": []}
# gained: {"lines": [23, 24, 32, 33], "branches": []}

import pytest
from sty.rendertype import EightbitFg

def test_eightbitfg_initialization():
    # Test initialization with a valid number
    num = 42
    fg = EightbitFg(num)
    assert fg.args == [num]

    # Test initialization with the boundary values
    fg_min = EightbitFg(0)
    assert fg_min.args == [0]

    fg_max = EightbitFg(255)
    assert fg_max.args == [255]
