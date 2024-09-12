# file: f032/__init__.py:4-6
# asked: {"lines": [4, 6], "branches": []}
# gained: {"lines": [4, 6], "branches": []}

import pytest
from f032 import poly

def test_poly():
    # Test with a simple polynomial, e.g., 2 + 3x + 4x^2 at x=2
    result = poly([2, 3, 4], 2)
    assert result == 2 + 3*2 + 4*2**2

    # Test with a zero polynomial
    result = poly([0, 0, 0], 2)
    assert result == 0

    # Test with a single coefficient
    result = poly([5], 2)
    assert result == 5

    # Test with negative coefficients
    result = poly([-1, -2, -3], 2)
    assert result == -1 + (-2)*2 + (-3)*2**2

    # Test with x=0
    result = poly([1, 2, 3], 0)
    assert result == 1

    # Test with an empty list
    result = poly([], 2)
    assert result == 0
