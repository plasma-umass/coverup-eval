# file: f136/__init__.py:1-5
# asked: {"lines": [1, 3, 4, 5], "branches": []}
# gained: {"lines": [1, 3, 4, 5], "branches": []}

import pytest
from f136 import largest_smallest_integers

def test_largest_smallest_integers_all_positive():
    result = largest_smallest_integers([1, 2, 3, 4, 5])
    assert result == (None, 1)

def test_largest_smallest_integers_all_negative():
    result = largest_smallest_integers([-1, -2, -3, -4, -5])
    assert result == (-1, None)

def test_largest_smallest_integers_mixed():
    result = largest_smallest_integers([-10, -20, 30, 40])
    assert result == (-10, 30)

def test_largest_smallest_integers_empty():
    result = largest_smallest_integers([])
    assert result == (None, None)

def test_largest_smallest_integers_no_positive():
    result = largest_smallest_integers([-1, -2, -3, 0])
    assert result == (-1, None)

def test_largest_smallest_integers_no_negative():
    result = largest_smallest_integers([1, 2, 3, 0])
    assert result == (None, 1)
