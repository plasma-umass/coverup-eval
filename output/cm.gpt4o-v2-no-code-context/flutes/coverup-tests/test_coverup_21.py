# file: flutes/iterator.py:204-205
# asked: {"lines": [204, 205], "branches": []}
# gained: {"lines": [204, 205], "branches": []}

import pytest
from typing import Callable, Iterable, List, TypeVar

# Define type variables
A = TypeVar('A')
B = TypeVar('B')

# Assuming the scanr function is defined somewhere in flutes/iterator.py
# and we are importing it here for testing purposes.
from flutes.iterator import scanr

def test_scanr_with_initial():
    def add(x: int, y: int) -> int:
        return x + y

    result = scanr(add, [1, 2, 3], 0)
    assert result == [6, 5, 3, 0]

def test_scanr_with_initial_empty_iterable():
    def add(x: int, y: int) -> int:
        return x + y

    result = scanr(add, [], 0)
    assert result == [0]

@pytest.fixture(autouse=True)
def cleanup():
    # Any necessary cleanup code can be added here
    yield
    # Cleanup actions after each test
