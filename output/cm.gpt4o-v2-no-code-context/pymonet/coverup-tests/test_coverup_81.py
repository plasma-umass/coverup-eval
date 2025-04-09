# file: pymonet/validation.py:124-133
# asked: {"lines": [124, 131, 133], "branches": []}
# gained: {"lines": [124, 131, 133], "branches": []}

import pytest
from pymonet.validation import Validation
from pymonet.box import Box

class TestValidation:
    def test_to_box(self):
        # Create a Validation instance with a value and errors
        validation_instance = Validation(value="test_value", errors=[])
        
        # Call the to_box method
        box_instance = validation_instance.to_box()
        
        # Assert that the returned instance is a Box and contains the correct value
        assert isinstance(box_instance, Box)
        assert box_instance.value == "test_value"
