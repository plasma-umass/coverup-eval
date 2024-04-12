# file pymonet/lazy.py:117-126
# lines [117, 124, 126]
# branches []

import pytest
from pymonet.lazy import Lazy
from pymonet.either import Right

def test_lazy_to_either():
    # Setup: Create a Lazy instance with a lambda that returns a value
    lazy_value = Lazy(lambda: 42)

    # Exercise: Convert the Lazy instance to an Either
    either_result = lazy_value.to_either()

    # Verify: Check that the result is a Right instance with the correct value
    assert isinstance(either_result, Right)
    assert either_result.value == 42

    # Cleanup: No cleanup necessary as no external state was modified
