# file: f003/__init__.py:4-13
# asked: {"lines": [4, 6, 8, 9, 10, 11, 13], "branches": [[8, 9], [8, 13], [10, 8], [10, 11]]}
# gained: {"lines": [4, 6, 8, 9, 10, 11, 13], "branches": [[8, 9], [8, 13], [10, 8], [10, 11]]}

import pytest
from f003 import below_zero

def test_below_zero_all_positive():
    assert below_zero([1, 2, 3, 4, 5]) == False

def test_below_zero_goes_negative():
    assert below_zero([1, -2, 3, -4, 5]) == True

def test_below_zero_stays_zero():
    assert below_zero([0, 0, 0, 0]) == False

def test_below_zero_immediately_negative():
    assert below_zero([-1, 2, 3, 4, 5]) == True

def test_below_zero_negative_then_positive():
    assert below_zero([-1, 1, -1, 1]) == True
