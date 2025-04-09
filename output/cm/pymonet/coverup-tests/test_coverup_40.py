# file pymonet/box.py:92-101
# lines [92, 99, 101]
# branches []

import pytest
from pymonet.box import Box
from pymonet.monad_try import Try

def test_box_to_try():
    # Create a Box instance with a value
    box = Box(42)

    # Convert the Box to a Try
    result = box.to_try()

    # Assert that the result is a Try instance
    assert isinstance(result, Try)

    # Assert that the Try is successful and contains the correct value
    assert result.is_success is True
    assert result.value == 42

# Clean up is not necessary in this case as no external state is modified
