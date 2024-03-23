# file sty/rendertype.py:23-33
# lines [23, 24, 32, 33]
# branches []

import pytest
from sty.rendertype import EightbitFg

def test_eightbit_fg_initialization():
    # Test initialization of EightbitFg
    num = 42
    eightbit_fg = EightbitFg(num)
    assert eightbit_fg.args == [num], "EightbitFg did not initialize with the correct arguments"
