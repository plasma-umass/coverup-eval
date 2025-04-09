# file: flutes/iterator.py:200-201
# asked: {"lines": [200, 201], "branches": []}
# gained: {"lines": [200, 201], "branches": []}

import pytest
from flutes.iterator import scanr

def test_scanr():
    # Test case 1: Simple addition
    result = scanr(lambda x, y: x + y, [1, 2, 3, 4])
    assert result == [10, 9, 7, 4]

    # Test case 2: Multiplication
    result = scanr(lambda x, y: x * y, [1, 2, 3, 4])
    assert result == [24, 24, 12, 4]

    # Test case 3: Empty iterable with initial value
    result = scanr(lambda x, y: x + y, [], 0)
    assert result == [0]

    # Test case 4: Single element iterable
    result = scanr(lambda x, y: x + y, [5])
    assert result == [5]

    # Test case 5: Using initial value
    result = scanr(lambda x, y: x + y, [1, 2, 3, 4], 10)
    assert result == [20, 19, 17, 14, 10]

    # Test case 6: Using initial value with multiplication
    result = scanr(lambda x, y: x * y, [1, 2, 3, 4], 2)
    assert result == [48, 48, 24, 8, 2]
