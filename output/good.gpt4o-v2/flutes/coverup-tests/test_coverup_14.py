# file: flutes/iterator.py:160-161
# asked: {"lines": [160, 161], "branches": []}
# gained: {"lines": [160, 161], "branches": []}

import pytest
from flutes.iterator import scanl

def test_scanl_overload_without_initial():
    def add(x, y):
        return x + y

    iterable = [1, 2, 3, 4]
    result = list(scanl(add, iterable))
    assert result == [1, 3, 6, 10]

def test_scanl_overload_with_initial():
    def add(x, y):
        return x + y

    iterable = [1, 2, 3, 4]
    result = list(scanl(add, iterable, 0))
    assert result == [0, 1, 3, 6, 10]
