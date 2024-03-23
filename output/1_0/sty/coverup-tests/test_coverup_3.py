# file sty/renderfunc.py:9-10
# lines [9, 10]
# branches []

import pytest

from sty.renderfunc import sgr

def test_sgr():
    assert sgr(0) == "\033[0m", "SGR reset code should be correct"
    assert sgr(1) == "\033[1m", "SGR bold code should be correct"
    assert sgr(30) == "\033[30m", "SGR black foreground code should be correct"
