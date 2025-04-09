# file pymonet/utils.py:9-22
# lines [9, 15, 16, 18, 19, 20, 21, 22]
# branches ['15->16', '15->18', '19->20', '19->21']

import pytest
from pymonet.utils import curry

def test_curry_full_coverage():
    # Test case where args_count is None
    def add(a, b, c):
        return a + b + c

    curried_add = curry(add)
    assert curried_add(1)(2)(3) == 6
    assert curried_add(1, 2)(3) == 6
    assert curried_add(1)(2, 3) == 6
    assert curried_add(1, 2, 3) == 6

    # Test case where args_count is provided
    def multiply(a, b):
        return a * b

    curried_multiply = curry(multiply, 2)
    assert curried_multiply(2)(3) == 6
    assert curried_multiply(2, 3) == 6

    # Test case with different args_count
    def subtract(a, b, c, d):
        return a - b - c - d

    curried_subtract = curry(subtract, 4)
    assert curried_subtract(10)(1)(2)(3) == 4
    assert curried_subtract(10, 1)(2, 3) == 4
    assert curried_subtract(10, 1, 2)(3) == 4
    assert curried_subtract(10, 1, 2, 3) == 4

    # Test case with no arguments
    def no_args():
        return "no args"

    curried_no_args = curry(no_args)
    assert curried_no_args() == "no args"

    # Test case with single argument
    def single_arg(a):
        return a * 2

    curried_single_arg = curry(single_arg)
    assert curried_single_arg(5) == 10

