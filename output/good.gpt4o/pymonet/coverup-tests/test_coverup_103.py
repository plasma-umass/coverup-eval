# file pymonet/either.py:182-187
# lines [182, 187]
# branches []

import pytest
from pymonet.either import Right

class TestRight:
    def test_is_left(self):
        right_instance = Right("some_value")
        assert not right_instance.is_left()
