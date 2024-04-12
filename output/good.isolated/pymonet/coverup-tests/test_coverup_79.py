# file pymonet/either.py:8-13
# lines [8, 9]
# branches []

import pytest
from pymonet.either import Either, Left, Right

def test_either_left_and_right():
    left_value = Left('error')
    right_value = Right(10)

    assert isinstance(left_value, Either)
    assert isinstance(right_value, Either)
    assert left_value.is_left() is True
    assert right_value.is_left() is False
    assert left_value.is_right() is False
    assert right_value.is_right() is True
