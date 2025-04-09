# file pymonet/either.py:182-187
# lines [182, 187]
# branches []

import pytest
from pymonet.either import Right

def test_right_is_left():
    right_instance = Right(42)
    assert right_instance.is_left() is False
