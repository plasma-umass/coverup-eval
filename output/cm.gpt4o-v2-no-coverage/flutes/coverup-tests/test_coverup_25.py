# file: flutes/iterator.py:160-161
# asked: {"lines": [160, 161], "branches": []}
# gained: {"lines": [160, 161], "branches": []}

import pytest
from flutes.iterator import scanl

def test_scanl_no_initial():
    def add(x, y):
        return x + y

    result = list(scanl(add, [1, 2, 3, 4]))
    assert result == [1, 3, 6, 10]

def test_scanl_with_initial():
    def add(x, y):
        return x + y

    result = list(scanl(add, [1, 2, 3, 4], 10))
    assert result == [10, 11, 13, 16, 20]

def test_scanl_empty_iterable():
    def add(x, y):
        return x + y

    result = list(scanl(add, [], 0))
    assert result == [0]

def test_scanl_single_element():
    def add(x, y):
        return x + y

    result = list(scanl(add, [5]))
    assert result == [5]

def test_scanl_with_initial_single_element():
    def add(x, y):
        return x + y

    result = list(scanl(add, [5], 10))
    assert result == [10, 15]
