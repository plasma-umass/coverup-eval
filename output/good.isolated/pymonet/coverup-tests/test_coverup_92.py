# file pymonet/either.py:153-162
# lines [153, 162]
# branches []

import pytest
from pymonet.either import Right

def test_right_map():
    # Setup: Create a Right instance with an initial value
    right_instance = Right(10)

    # Exercise: Map the Right instance using a lambda that increments the value
    mapped_instance = right_instance.map(lambda x: x + 1)

    # Verify: Check that the result is still a Right instance and the value is incremented
    assert isinstance(mapped_instance, Right)
    assert mapped_instance.value == 11

    # Cleanup: No cleanup required as no external state was modified
