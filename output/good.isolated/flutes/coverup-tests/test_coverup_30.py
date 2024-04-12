# file flutes/iterator.py:200-201
# lines [200, 201]
# branches []

import pytest
from flutes.iterator import scanr
from typing import List, Callable

# Adjusting the test to handle the case where an empty iterable is passed to scanr
# and ensuring that an initial value is provided to avoid StopIteration.

def test_scanr():
    # Define a simple binary function for testing
    def add(x: int, y: int) -> int:
        return x + y

    # Test with a non-empty list
    result = scanr(add, [1, 2, 3, 4], 0)
    assert result == [10, 9, 7, 4, 0], "The scanr function did not produce the expected cumulative sums"

    # Test with an empty list and an initial value
    result = scanr(add, [], 0)
    assert result == [0], "The scanr function should return a list with the initial value for an empty input"

    # Test with a single-element list
    result = scanr(add, [42], 0)
    assert result == [42, 0], "The scanr function should return the single element followed by the initial value"

# Note: The actual test function to improve coverage would depend on the missing lines/branches
# in the real implementation of scanr. The above test is a generic example and may not target
# the specific missing coverage in the actual code.
