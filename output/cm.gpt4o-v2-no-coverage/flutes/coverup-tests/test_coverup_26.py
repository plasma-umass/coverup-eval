# file: flutes/iterator.py:204-205
# asked: {"lines": [204, 205], "branches": []}
# gained: {"lines": [204, 205], "branches": []}

import pytest
from typing import Callable, Iterable, List
from flutes.iterator import scanr

def test_scanr_with_initial():
    def add(x: int, y: int) -> int:
        return x + y

    result = scanr(add, [1, 2, 3], 0)
    assert result == [6, 5, 3, 0]

def test_scanr_without_initial():
    def add(x: int, y: int) -> int:
        return x + y

    result = scanr(add, [1, 2, 3])
    assert result == [6, 5, 3]

def test_scanr_empty_iterable_with_initial():
    def add(x: int, y: int) -> int:
        return x + y

    result = scanr(add, [], 0)
    assert result == [0]

def test_scanr_empty_iterable_without_initial():
    def add(x: int, y: int) -> int:
        return x + y

    with pytest.raises(RuntimeError):
        scanr(add, [])

def test_scanr_single_element_with_initial():
    def add(x: int, y: int) -> int:
        return x + y

    result = scanr(add, [1], 0)
    assert result == [1, 0]

def test_scanr_single_element_without_initial():
    def add(x: int, y: int) -> int:
        return x + y

    result = scanr(add, [1])
    assert result == [1]
