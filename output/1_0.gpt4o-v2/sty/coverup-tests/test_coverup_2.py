# file: sty/rendertype.py:10-20
# asked: {"lines": [10, 11, 19, 20], "branches": []}
# gained: {"lines": [10, 11, 19, 20], "branches": []}

import pytest
from sty.rendertype import Sgr

def test_sgr_initialization():
    num = 5
    sgr = Sgr(num)
    assert sgr.args == [num]
