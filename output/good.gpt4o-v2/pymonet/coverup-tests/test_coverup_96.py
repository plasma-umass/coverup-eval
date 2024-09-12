# file: pymonet/validation.py:124-133
# asked: {"lines": [124, 131, 133], "branches": []}
# gained: {"lines": [124, 131, 133], "branches": []}

import pytest
from pymonet.validation import Validation
from pymonet.box import Box

def test_validation_to_box():
    # Arrange
    validation_instance = Validation("test_value", [])
    
    # Act
    box_instance = validation_instance.to_box()
    
    # Assert
    assert isinstance(box_instance, Box)
    assert box_instance.value == "test_value"
