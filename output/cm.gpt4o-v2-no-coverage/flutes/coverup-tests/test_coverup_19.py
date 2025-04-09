# file: flutes/iterator.py:164-165
# asked: {"lines": [164, 165], "branches": []}
# gained: {"lines": [164, 165], "branches": []}

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

def test_scanl_empty_iterable_with_initial():
    def add(x, y):
        return x + y

    result = list(scanl(add, [], 10))
    assert result == [10]
