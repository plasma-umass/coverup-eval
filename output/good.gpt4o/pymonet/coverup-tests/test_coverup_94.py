# file pymonet/either.py:113-118
# lines [113, 118]
# branches []

import pytest
from pymonet.either import Either

def test_left_is_left():
    class Left(Either):
        def __init__(self, value):
            self.value = value

        def is_left(self) -> bool:
            return True

    left_instance = Left(value="test_value")
    assert left_instance.is_left() == True
