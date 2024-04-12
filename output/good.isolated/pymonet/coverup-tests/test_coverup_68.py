# file pymonet/box.py:37-46
# lines [37, 46]
# branches []

import pytest
from pymonet.box import Box

def test_box_bind():
    # Setup: Create a Box with an initial value
    box = Box(10)

    # Define a mapper function to be used with bind
    def mapper(x):
        return x * 2

    # Exercise: Use bind to apply the mapper to the Box's value
    result = box.bind(mapper)

    # Verify: Check that the result is as expected
    assert result == 20

    # Cleanup: No cleanup necessary as no external state was modified
