# file: pymonet/utils.py:117-137
# asked: {"lines": [117, 132, 133, 134, 135, 137], "branches": [[133, 0], [133, 134], [134, 133], [134, 135]]}
# gained: {"lines": [117, 132, 133, 134, 135, 137], "branches": [[133, 0], [133, 134], [134, 133], [134, 135]]}

import pytest
from pymonet.utils import cond

def test_cond():
    # Define some sample condition and execution functions
    def is_even(x):
        return x % 2 == 0

    def is_odd(x):
        return x % 2 != 0

    def return_even(x):
        return f"{x} is even"

    def return_odd(x):
        return f"{x} is odd"

    # Create a condition list
    condition_list = [
        (is_even, return_even),
        (is_odd, return_odd)
    ]

    # Get the result function from cond
    result_func = cond(condition_list)

    # Test the result function
    assert result_func(2) == "2 is even"
    assert result_func(3) == "3 is odd"

    # Test with no matching condition
    def always_false(x):
        return False

    condition_list_no_match = [
        (always_false, return_even)
    ]

    result_func_no_match = cond(condition_list_no_match)
    assert result_func_no_match(2) is None

