# file pymonet/either.py:175-180
# lines [175, 180]
# branches []

import pytest
from pymonet.either import Right

def test_right_is_right():
    right_instance = Right(42)
    assert right_instance.is_right() is True
