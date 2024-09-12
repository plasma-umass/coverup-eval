# file: f009/__init__.py:4-17
# asked: {"lines": [4, 6, 7, 9, 10, 11, 13, 15, 17], "branches": [[9, 10], [9, 17], [10, 11], [10, 13]]}
# gained: {"lines": [4, 6, 7, 9, 10, 11, 13, 15, 17], "branches": [[9, 10], [9, 17], [10, 11], [10, 13]]}

import pytest
from f009 import rolling_max

def test_rolling_max_all_positive():
    numbers = [1, 2, 3, 2, 5, 4]
    expected = [1, 2, 3, 3, 5, 5]
    assert rolling_max(numbers) == expected

def test_rolling_max_with_negatives():
    numbers = [-1, -2, -3, -2, -1, 0]
    expected = [-1, -1, -1, -1, -1, 0]
    assert rolling_max(numbers) == expected

def test_rolling_max_all_same():
    numbers = [2, 2, 2, 2, 2]
    expected = [2, 2, 2, 2, 2]
    assert rolling_max(numbers) == expected

def test_rolling_max_empty():
    numbers = []
    expected = []
    assert rolling_max(numbers) == expected

def test_rolling_max_single_element():
    numbers = [5]
    expected = [5]
    assert rolling_max(numbers) == expected
