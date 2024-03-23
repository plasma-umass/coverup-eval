# file pymonet/maybe.py:24-33
# lines [24, 25, 33]
# branches []

import pytest
from pymonet.maybe import Maybe

def test_maybe_just():
    # Test the Maybe.just class method
    value = "test_value"
    maybe_just = Maybe.just(value)

    # Assert that maybe_just is an instance of Maybe
    assert isinstance(maybe_just, Maybe)

    # Assert that maybe_just is not empty
    assert not maybe_just.is_nothing

    # Assert that the value is stored correctly
    assert maybe_just.get_or_else(None) == value
