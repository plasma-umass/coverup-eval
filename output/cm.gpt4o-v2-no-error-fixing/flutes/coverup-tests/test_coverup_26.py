# file: flutes/iterator.py:204-205
# asked: {"lines": [204, 205], "branches": []}
# gained: {"lines": [204, 205], "branches": []}

import pytest
from flutes.iterator import scanr
from typing import List

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
