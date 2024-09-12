# file: pymonet/box.py:26-35
# asked: {"lines": [26, 35], "branches": []}
# gained: {"lines": [26, 35], "branches": []}

import pytest
from pymonet.box import Box

def test_box_map():
    # Create a Box with an initial value
    box = Box(5)
    
    # Define a mapper function
    def mapper(x):
        return x * 2
    
    # Apply the map function
    new_box = box.map(mapper)
    
    # Assert the new box has the mapped value
    assert new_box.value == 10

    # Clean up
    del box
    del new_box
