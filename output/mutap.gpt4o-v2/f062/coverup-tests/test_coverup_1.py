# file: f062/__init__.py:1-3
# asked: {"lines": [1, 3], "branches": []}
# gained: {"lines": [1, 3], "branches": []}

import pytest
from f062 import derivative

def test_derivative():
    # Test with a list of integers
    xs = [1, 2, 3, 4]
    result = derivative(xs)
    assert result == [2, 6, 12]

    # Test with a list of zeros
    xs = [0, 0, 0, 0]
    result = derivative(xs)
    assert result == [0, 0, 0]

    # Test with an empty list
    xs = []
    result = derivative(xs)
    assert result == []

    # Test with a list of one element
    xs = [5]
    result = derivative(xs)
    assert result == []

    # Test with negative numbers
    xs = [-1, -2, -3, -4]
    result = derivative(xs)
    assert result == [-2, -6, -12]

    # Test with mixed positive and negative numbers
    xs = [1, -2, 3, -4]
    result = derivative(xs)
    assert result == [-2, 6, -12]
