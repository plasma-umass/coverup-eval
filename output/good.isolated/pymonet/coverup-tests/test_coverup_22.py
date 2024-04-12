# file pymonet/utils.py:99-114
# lines [99, 110, 111, 112, 113]
# branches []

import pytest
from pymonet.utils import pipe

def test_pipe_with_multiple_functions():
    # Define functions to be used in the pipe
    def add_two(x):
        return x + 2

    def multiply_by_three(x):
        return x * 3

    def subtract_five(x):
        return x - 5

    # Initial value to be piped through the functions
    initial_value = 5

    # Expected result after applying all functions: (((5 + 2) * 3) - 5) = 16
    expected_result = 16

    # Apply the pipe function with the defined functions
    result = pipe(initial_value, add_two, multiply_by_three, subtract_five)

    # Assert that the result is as expected
    assert result == expected_result

def test_pipe_with_no_functions():
    # Initial value to be piped through the functions
    initial_value = 10

    # Expected result after applying no functions should be the initial value itself
    expected_result = initial_value

    # Apply the pipe function with no functions
    result = pipe(initial_value)

    # Assert that the result is as expected
    assert result == expected_result
