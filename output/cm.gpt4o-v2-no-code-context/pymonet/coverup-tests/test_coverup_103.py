# file: pymonet/box.py:48-57
# asked: {"lines": [48, 57], "branches": []}
# gained: {"lines": [48, 57], "branches": []}

import pytest
from pymonet.box import Box

class TestBox:
    def test_ap_with_function_inside_box(self):
        # Arrange
        box_with_function = Box(lambda x: x + 1)
        box_with_value = Box(1)
        
        # Act
        result = box_with_function.ap(box_with_value)
        
        # Assert
        assert result.value == 2

    def test_ap_with_different_function_inside_box(self):
        # Arrange
        box_with_function = Box(lambda x: x * 2)
        box_with_value = Box(3)
        
        # Act
        result = box_with_function.ap(box_with_value)
        
        # Assert
        assert result.value == 6
