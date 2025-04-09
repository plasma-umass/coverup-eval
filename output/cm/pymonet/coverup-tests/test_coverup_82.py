# file pymonet/either.py:85-87
# lines [85, 86]
# branches []

import pytest
from pymonet.either import Left, Either

def test_left_is_instance_of_either():
    left_value = Left('error')
    assert isinstance(left_value, Either), "Left should be an instance of Either"
