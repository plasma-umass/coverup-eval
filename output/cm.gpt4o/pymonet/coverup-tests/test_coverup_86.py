# file pymonet/box.py:48-57
# lines [48, 57]
# branches []

import pytest
from pymonet.box import Box

class TestBox:
    def test_ap(self):
        # Create a Box containing a value
        box_with_value = Box(1)
        
        # Create a Box containing a function
        box_with_function = Box(lambda x: x + 1)
        
        # Apply the function inside box_with_function to box_with_value
        result_box = box_with_function.ap(box_with_value)
        
        # Assert that the result is a Box containing the expected value
        assert result_box.value == 2
