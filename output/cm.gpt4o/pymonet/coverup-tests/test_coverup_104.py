# file pymonet/either.py:120-125
# lines [120, 125]
# branches []

import pytest
from pymonet.either import Either

class Left(Either):
    def __init__(self, value):
        self.value = value

    def is_right(self) -> bool:
        """
        :returns: False
        :rtype: Boolean
        """
        return False

class TestLeft:
    def test_is_right(self):
        left_instance = Left(value=None)
        assert not left_instance.is_right()
