# file: flutes/iterator.py:160-161
# asked: {"lines": [160, 161], "branches": []}
# gained: {"lines": [160, 161], "branches": []}

import pytest
from typing import Callable, Iterable, Iterator
from flutes.iterator import scanl

def test_scanl_overload():
    def add(x: int, y: int) -> int:
        return x + y

    iterable = [1, 2, 3, 4]
    result = scanl(add, iterable)
    assert isinstance(result, Iterator)

    # Ensure the result is as expected
    result_list = list(result)
    assert result_list == [1, 3, 6, 10]

