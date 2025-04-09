# file flutes/iterator.py:204-205
# lines [204, 205]
# branches []

import pytest
from flutes.iterator import scanr
from typing import Callable, Iterable, List

def test_scanr():
    def func(x: int, y: int) -> int:
        return x + y

    iterable = [1, 2, 3]
    initial = 0

    result = scanr(func, iterable, initial)
    expected = [6, 5, 3, 0]

    assert result == expected, "The scanr function did not produce the expected output."

    # Clean up is not necessary here as we are not modifying any external state or resources.
