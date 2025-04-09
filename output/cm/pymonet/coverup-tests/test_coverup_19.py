# file pymonet/either.py:22-35
# lines [22, 33, 34, 35]
# branches ['33->34', '33->35']

import pytest
from pymonet.either import Either, Left, Right

def test_either_case_left_branch():
    def error_handler(value):
        return f"Error: {value}"

    def success_handler(value):
        return f"Success: {value}"

    left_value = Left("Something went wrong")
    result = left_value.case(error_handler, success_handler)
    assert result == "Error: Something went wrong"

def test_either_case_right_branch():
    def error_handler(value):
        return f"Error: {value}"

    def success_handler(value):
        return f"Success: {value}"

    right_value = Right("All good")
    result = right_value.case(error_handler, success_handler)
    assert result == "Success: All good"
