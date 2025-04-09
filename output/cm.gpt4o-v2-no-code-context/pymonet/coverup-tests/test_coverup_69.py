# file: pymonet/box.py:26-35
# asked: {"lines": [26, 35], "branches": []}
# gained: {"lines": [26, 35], "branches": []}

import pytest
from pymonet.box import Box

def test_box_map():
    # Create a Box instance with an initial value
    box = Box(10)
    
    # Define a mapper function
    def mapper(x):
        return x * 2
    
    # Use the map method
    new_box = box.map(mapper)
    
    # Assert the new box has the correct mapped value
    assert new_box.value == 20

    # Clean up
    del box
    del new_box
    del mapper
