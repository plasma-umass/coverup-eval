# file pymonet/either.py:175-180
# lines [180]
# branches []

import pytest
from pymonet.either import Right

def test_right_is_right():
    right_instance = Right("test_value")
    assert right_instance.is_right() == True
