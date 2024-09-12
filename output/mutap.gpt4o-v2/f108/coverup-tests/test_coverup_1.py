# file: f108/__init__.py:1-10
# asked: {"lines": [1, 3, 4, 5, 6, 7, 8, 9, 10], "branches": [[5, 6], [5, 7]]}
# gained: {"lines": [1, 3, 4, 5, 6, 7, 8, 9, 10], "branches": [[5, 6], [5, 7]]}

import pytest
from f108 import count_nums

def test_count_nums_all_positive():
    arr = [123, 456, 789]
    assert count_nums(arr) == 3

def test_count_nums_mixed():
    arr = [123, -456, 789]
    assert count_nums(arr) == 3

def test_count_nums_all_negative():
    arr = [-123, -456, -789]
    assert count_nums(arr) == 3

def test_count_nums_zero():
    arr = [0, 0, 0]
    assert count_nums(arr) == 0

def test_count_nums_empty():
    arr = []
    assert count_nums(arr) == 0
