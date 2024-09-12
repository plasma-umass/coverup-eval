# file: f123/__init__.py:1-16
# asked: {"lines": [1, 3, 4, 6, 7, 8, 9, 11, 13, 14, 16], "branches": [[3, 4], [3, 6], [7, 8], [7, 16], [8, 9], [8, 11], [13, 7], [13, 14]]}
# gained: {"lines": [1, 3, 4, 6, 7, 8, 9, 11, 13, 14, 16], "branches": [[3, 4], [3, 6], [7, 8], [7, 16], [8, 9], [8, 11], [13, 7], [13, 14]]}

import pytest
from f123 import get_odd_collatz

def test_get_odd_collatz_even():
    result = get_odd_collatz(6)
    assert result == [1, 3, 5]

def test_get_odd_collatz_odd():
    result = get_odd_collatz(7)
    assert result == [1, 5, 7, 11, 13, 17]

def test_get_odd_collatz_one():
    result = get_odd_collatz(1)
    assert result == [1]
