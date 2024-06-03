# file pymonet/box.py:103-112
# lines [103, 110, 112]
# branches []

import pytest
from pymonet.box import Box
from pymonet.validation import Validation

def test_box_to_validation():
    # Create a Box instance with a sample value
    box = Box("test_value")
    
    # Convert the Box to a Validation
    validation = box.to_validation()
    
    # Assert that the Validation is successful and contains the correct value
    assert isinstance(validation, Validation)
    assert validation.is_success()
    assert validation.value == "test_value"
