# file sty/rendertype.py:36-46
# lines [36, 37, 45, 46]
# branches []

import pytest
from sty.rendertype import EightbitBg

def test_eightbitbg_initialization():
    num = 42
    eightbit_bg = EightbitBg(num)
    assert eightbit_bg.args == [num], "EightbitBg did not initialize with the correct arguments."
