# file pymonet/either.py:81-82
# lines [81, 82]
# branches []

import pytest
from pymonet.either import Either

class Left(Either):
    def __init__(self, value):
        super().__init__(value)

    def is_right(self):
        return False

class Right(Either):
    def __init__(self, value):
        super().__init__(value)

    def is_right(self):
        return True

def test_either_is_right():
    left = Left(None)
    right = Right(None)

    assert not left.is_right(), "Left should return False for is_right"
    assert right.is_right(), "Right should return True for is_right"
