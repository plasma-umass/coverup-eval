# file: flutes/iterator.py:200-201
# asked: {"lines": [200, 201], "branches": []}
# gained: {"lines": [200, 201], "branches": []}

import pytest
from flutes.iterator import scanr
from typing import Callable, Iterable, List

def test_scanr_overload():
    def add(x: int, y: int) -> int:
        return x + y

    iterable = [1, 2, 3, 4]
    result = scanr(add, iterable)
    assert isinstance(result, list)

