# file: pymonet/utils.py:117-137
# asked: {"lines": [117, 132, 133, 134, 135, 137], "branches": [[133, 0], [133, 134], [134, 133], [134, 135]]}
# gained: {"lines": [117, 132, 133, 134, 135, 137], "branches": [[133, 0], [133, 134], [134, 133], [134, 135]]}

import pytest
from pymonet.utils import cond

def test_cond():
    # Define some condition and execution functions
    def is_even(x):
        return x % 2 == 0

    def is_odd(x):
        return x % 2 != 0

    def even_action(x):
        return f"{x} is even"

    def odd_action(x):
        return f"{x} is odd"

    # Create a condition list
    condition_list = [
        (is_even, even_action),
        (is_odd, odd_action)
    ]

    # Get the conditional function
    conditional_function = cond(condition_list)

    # Test the conditional function
    assert conditional_function(2) == "2 is even"
    assert conditional_function(3) == "3 is odd"

    # Test with no matching condition
    def always_false(x):
        return False

    condition_list = [
        (always_false, even_action)
    ]

    conditional_function = cond(condition_list)
    assert conditional_function(2) is None

