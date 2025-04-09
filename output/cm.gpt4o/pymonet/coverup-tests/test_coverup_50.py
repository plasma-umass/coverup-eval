# file pymonet/utils.py:49-51
# lines [49, 50, 51]
# branches []

import pytest
from pymonet.utils import eq

def test_eq():
    # Test when both values are equal
    assert eq(5, 5) == True
    assert eq("test", "test") == True
    assert eq([1, 2, 3], [1, 2, 3]) == True

    # Test when values are not equal
    assert eq(5, 6) == False
    assert eq("test", "TEST") == False
    assert eq([1, 2, 3], [3, 2, 1]) == False

    # Test with different types
    assert eq(5, "5") == False
    assert eq(5, 5.0) == True  # int and float comparison

    # Test with curried function
    eq_5 = eq(5)
    assert eq_5(5) == True
    assert eq_5(6) == False
