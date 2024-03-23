# file pymonet/either.py:106-111
# lines [106, 111]
# branches []

import pytest
from pymonet.either import Left

def test_left_ap_returns_copy_of_self():
    left_value = "error"
    left = Left(left_value)

    # Apply a function wrapped in a Left
    result = left.ap(Left(lambda x: x.upper()))

    assert isinstance(result, Left), "The result should be an instance of Left"
    assert result.value == left_value, "The value should be unchanged"
    assert result is not left, "The result should be a copy, not the same instance"
