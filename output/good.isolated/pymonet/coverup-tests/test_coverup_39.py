# file pymonet/utils.py:49-51
# lines [49, 50, 51]
# branches []

import pytest
from pymonet.utils import eq

def test_eq_function():
    # Test the eq function with integers
    assert eq(1)(1) == True, "Should return True for equal integers"
    assert eq(1)(2) == False, "Should return False for different integers"

    # Test the eq function with strings
    assert eq("test")("test") == True, "Should return True for equal strings"
    assert eq("test")("fail") == False, "Should return False for different strings"

    # Test the eq function with different types
    assert eq(1)("1") == False, "Should return False for different types"
