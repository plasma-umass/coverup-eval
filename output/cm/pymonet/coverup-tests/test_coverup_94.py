# file pymonet/either.py:37-46
# lines [37, 46]
# branches []

import pytest
from pymonet.either import Either, Left, Right

def test_either_ap_with_right():
    right_function = Right(lambda x: x + 1)
    right_value = Right(1)
    
    result = right_function.ap(right_value)
    
    assert isinstance(result, Right)
    assert result.value == 2

def test_either_ap_with_left():
    left_value = Left("Error")
    right_function = Right(lambda x: x + 1)
    
    result = left_value.ap(right_function)
    
    assert isinstance(result, Left)
    assert result.value == "Error"
