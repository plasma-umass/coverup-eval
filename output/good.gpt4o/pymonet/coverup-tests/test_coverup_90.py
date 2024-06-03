# file pymonet/either.py:85-87
# lines [85, 86]
# branches []

import pytest
from pymonet.either import Either

def test_left_class():
    class Left(Either):
        """Not successfully Either"""
        def __init__(self, value):
            self.value = value

    left_instance = Left("test_value")
    assert isinstance(left_instance, Either)
    assert isinstance(left_instance, Left)
    assert left_instance.value == "test_value"
