# file pymonet/box.py:26-35
# lines [26, 35]
# branches []

import pytest
from pymonet.box import Box

def test_box_map():
    # Setup: Create a Box with an initial value
    initial_value = 10
    box = Box(initial_value)

    # Define a mapper function to be used with Box.map
    def mapper(x):
        return x * 2

    # Exercise: Map the Box value using the mapper function
    mapped_box = box.map(mapper)

    # Verify: Check that the new Box contains the mapped value
    assert mapped_box.value == mapper(initial_value)

    # Cleanup: No cleanup required as no external state was modified
