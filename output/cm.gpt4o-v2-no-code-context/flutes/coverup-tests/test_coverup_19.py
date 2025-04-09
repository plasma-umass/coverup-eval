# file: flutes/iterator.py:164-165
# asked: {"lines": [164, 165], "branches": []}
# gained: {"lines": [164, 165], "branches": []}

import pytest
from typing import Callable, Iterable, Iterator, TypeVar

# Define type variables
A = TypeVar('A')
B = TypeVar('B')

# Assuming the scanl function is defined somewhere in flutes/iterator.py
from flutes.iterator import scanl

def test_scanl_with_initial():
    def add(x, y):
        return x + y

    iterable = [1, 2, 3, 4]
    initial = 0
    result = list(scanl(add, iterable, initial))
    
    assert result == [0, 1, 3, 6, 10]

def test_scanl_without_initial():
    def add(x, y):
        return x + y

    iterable = [1, 2, 3, 4]
    result = list(scanl(add, iterable))
    
    assert result == [1, 3, 6, 10]

@pytest.fixture(autouse=True)
def cleanup():
    yield
    # Add any necessary cleanup code here
