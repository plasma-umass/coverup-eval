# file pymonet/either.py:120-125
# lines [125]
# branches []

import pytest
from pymonet.either import Left

def test_left_is_right():
    left_instance = Left(value=None)
    assert not left_instance.is_right()
