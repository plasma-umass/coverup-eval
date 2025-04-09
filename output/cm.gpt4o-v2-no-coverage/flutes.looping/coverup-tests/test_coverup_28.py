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

    # Test case 3: Empty iterable
    result = scanr(lambda x, y: x + y, [], 0)
    assert result == [0]

    # Test case 4: Single element iterable
    result = scanr(lambda x, y: x + y, [42])
    assert result == [42]

    # Test case 5: With initial value
    result = scanr(lambda x, y: x + y, [1, 2, 3, 4], 5)
    assert result == [15, 14, 12, 9, 5]

    # Test case 6: With initial value and multiplication
    result = scanr(lambda x, y: x * y, [1, 2, 3, 4], 2)
    assert result == [48, 48, 24, 8, 2]
