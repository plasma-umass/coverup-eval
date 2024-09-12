# file: f068/__init__.py:1-6
# asked: {"lines": [1, 3, 4, 5, 6], "branches": [[3, 3], [3, 4], [5, 5], [5, 6]]}
# gained: {"lines": [1, 3, 4, 5, 6], "branches": [[3, 3], [3, 4], [5, 5], [5, 6]]}

import pytest
from f068 import pluck

def test_pluck_empty_array():
    assert pluck([]) == []

def test_pluck_no_evens():
    assert pluck([1, 3, 5]) == []

def test_pluck_with_evens():
    assert pluck([1, 2, 3, 4, 5]) == [2, 1]

def test_pluck_all_evens():
    assert pluck([2, 4, 6, 8]) == [2, 0]

def test_pluck_single_even():
    assert pluck([1, 2, 3]) == [2, 1]
