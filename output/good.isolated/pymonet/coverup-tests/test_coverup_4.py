# file pymonet/utils.py:81-96
# lines [81, 92, 93, 94, 95]
# branches []

import pytest
from pymonet.utils import compose

def test_compose():
    # Define some simple functions for composition
    def add_one(x):
        return x + 1

    def multiply_by_two(x):
        return x * 2

    # Compose the functions and apply to the initial value
    result = compose(5, add_one, multiply_by_two)

    # Check the result is as expected (5 * 2) + 1 = 11
    assert result == 11

    # Test with no functions, should return the initial value
    result_no_functions = compose(5)
    assert result_no_functions == 5

    # Test with a single function, should apply it to the value
    result_single_function = compose(5, add_one)
    assert result_single_function == 6

    # Test with multiple functions
    result_multiple_functions = compose(5, add_one, multiply_by_two, add_one)
    assert result_multiple_functions == 13  # ((5 + 1) * 2) + 1

# No top-level code is included as per instructions.
