# file: f131/__init__.py:1-13
# asked: {"lines": [1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13], "branches": [[5, 6], [5, 10], [7, 5], [7, 8], [10, 11], [10, 13]]}
# gained: {"lines": [1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13], "branches": [[5, 6], [5, 10], [7, 5], [7, 8], [10, 11], [10, 13]]}

import pytest
from f131 import digits

def test_digits_all_even():
    assert digits(2468) == 0

def test_digits_mixed():
    assert digits(1234) == 3  # 1 * 3

def test_digits_all_odd():
    assert digits(135) == 15  # 1 * 3 * 5

def test_digits_no_digits():
    assert digits(0) == 0

def test_digits_single_odd():
    assert digits(7) == 7

def test_digits_single_even():
    assert digits(4) == 0
