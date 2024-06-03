# file pymonet/either.py:175-180
# lines [175, 180]
# branches []

import pytest
from pymonet.either import Either

def test_right_is_right():
    class Right(Either):
        def is_right(self) -> bool:
            """
            :returns: True
            :rtype: Boolean
            """
            return True

    right_instance = Right("test_value")
    assert right_instance.is_right() == True
