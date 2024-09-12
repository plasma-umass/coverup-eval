# file: f045/__init__.py:1-3
# asked: {"lines": [1, 3], "branches": []}
# gained: {"lines": [1, 3], "branches": []}

import pytest
from f045 import triangle_area

def test_triangle_area():
    # Test with positive integers
    assert triangle_area(3, 6) == 9.0
    
    # Test with zero
    assert triangle_area(0, 5) == 0.0
    assert triangle_area(5, 0) == 0.0
    
    # Test with floating point numbers
    assert triangle_area(2.5, 4.0) == 5.0
    
    # Test with negative numbers
    assert triangle_area(-3, 6) == -9.0
    assert triangle_area(3, -6) == -9.0
    assert triangle_area(-3, -6) == 9.0
