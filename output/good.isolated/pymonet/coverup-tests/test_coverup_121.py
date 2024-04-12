# file pymonet/either.py:189-198
# lines [196, 198]
# branches []

import pytest
from pymonet.either import Right
from pymonet.maybe import Maybe

def test_right_to_maybe():
    # Setup: Create a Right instance with a value
    right_value = Right(10)

    # Exercise: Convert Right to Maybe
    maybe_value = right_value.to_maybe()

    # Verify: Check if the Maybe contains the correct value
    assert isinstance(maybe_value, Maybe)
    assert maybe_value.get_or_else(None) == 10

    # Cleanup: No cleanup required as no external state was modified
