# file: flutes/math.py:6-8
# asked: {"lines": [6, 8], "branches": []}
# gained: {"lines": [6, 8], "branches": []}

import pytest
from flutes.math import ceil_div

def test_ceil_div_positive():
    assert ceil_div(10, 3) == 4

def test_ceil_div_negative():
    assert ceil_div(-10, 3) == -3

def test_ceil_div_zero_division():
    with pytest.raises(ZeroDivisionError):
        ceil_div(10, 0)

def test_ceil_div_exact_division():
    assert ceil_div(9, 3) == 3
