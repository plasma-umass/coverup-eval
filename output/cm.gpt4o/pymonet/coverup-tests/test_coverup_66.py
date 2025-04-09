# file pymonet/box.py:26-35
# lines [26, 35]
# branches []

import pytest
from pymonet.box import Box

def test_box_map():
    # Create a Box instance with an initial value
    box = Box(10)
    
    # Define a mapper function
    def mapper(x):
        return x * 2
    
    # Apply the map function
    new_box = box.map(mapper)
    
    # Assert that the new box has the correct mapped value
    assert new_box.value == 20

    # Clean up (if necessary, though in this case, there's nothing to clean up)
