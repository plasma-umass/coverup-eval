# file pymonet/either.py:113-118
# lines [118]
# branches []

import pytest
from pymonet.either import Either

def test_left_is_left():
    class Left(Either):
        def __init__(self, value):
            self.value = value

        def is_left(self) -> bool:
            return True

    left_instance = Left(value=None)
    assert left_instance.is_left() == True

    # Ensure that the actual Left class from pymonet.either is tested
    from pymonet.either import Left as PymonetLeft
    pymonet_left_instance = PymonetLeft(value=None)
    assert pymonet_left_instance.is_left() == True
