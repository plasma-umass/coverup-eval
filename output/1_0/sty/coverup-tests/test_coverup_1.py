# file sty/rendertype.py:10-20
# lines [10, 11, 19, 20]
# branches []

import pytest
from sty.rendertype import Sgr

def test_sgr_initialization():
    sgr_num = 1
    sgr_instance = Sgr(sgr_num)
    assert sgr_instance.args == [sgr_num], "SGR instance args should contain the provided SGR number"
