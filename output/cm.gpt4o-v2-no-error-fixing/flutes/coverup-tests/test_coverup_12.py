# file: flutes/iterator.py:164-165
# asked: {"lines": [164, 165], "branches": []}
# gained: {"lines": [164, 165], "branches": []}

import pytest
from typing import Callable, Iterable, Iterator
from flutes.iterator import scanl

def test_scanl_with_initial():
    def add(x: int, y: int) -> int:
        return x + y

    iterable = [1, 2, 3]
    initial = 0
    result = list(scanl(add, iterable, initial))
    assert result == [0, 1, 3, 6]

def test_scanl_without_initial():
    def add(x: int, y: int) -> int:
        return x + y

    iterable = [1, 2, 3]
    result = list(scanl(add, iterable))
    assert result == [1, 3, 6]
