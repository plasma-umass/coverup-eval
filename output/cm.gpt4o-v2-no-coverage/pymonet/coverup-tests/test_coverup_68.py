# file: pymonet/validation.py:124-133
# asked: {"lines": [124, 131, 133], "branches": []}
# gained: {"lines": [124, 131, 133], "branches": []}

import pytest
from pymonet.validation import Validation
from pymonet.box import Box

def test_validation_to_box():
    # Create a Validation instance with a value
    validation = Validation("test_value", [])
    
    # Convert the Validation instance to a Box
    box = validation.to_box()
    
    # Assert that the Box contains the correct value
    assert isinstance(box, Box)
    assert box.value == "test_value"
