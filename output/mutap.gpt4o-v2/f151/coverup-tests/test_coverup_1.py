# file: f151/__init__.py:1-3
# asked: {"lines": [1, 3], "branches": []}
# gained: {"lines": [1, 3], "branches": []}

import pytest
from f151 import double_the_difference

def test_double_the_difference():
    # Test with positive odd integers
    assert double_the_difference([1, 3, 5]) == 1**2 + 3**2 + 5**2
    
    # Test with a mix of positive odd and even integers
    assert double_the_difference([1, 2, 3, 4, 5]) == 1**2 + 3**2 + 5**2
    
    # Test with negative integers and zero
    assert double_the_difference([-1, -2, 0, 1, 2, 3]) == 1**2 + 3**2
    
    # Test with floating point numbers
    assert double_the_difference([1.0, 2.0, 3.0]) == 0
    
    # Test with a mix of integers and floating point numbers
    assert double_the_difference([1, 2, 3, 4.0, 5.0]) == 1**2 + 3**2

    # Test with an empty list
    assert double_the_difference([]) == 0
