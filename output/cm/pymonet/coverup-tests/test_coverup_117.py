# file pymonet/validation.py:124-133
# lines [131, 133]
# branches []

import pytest
from pymonet.validation import Validation

def test_validation_to_box():
    # Create a Validation instance with some value and empty errors
    validation_instance = Validation('test_value', [])

    # Call the to_box method to transform Validation to Box
    box_instance = validation_instance.to_box()

    # Assert that the returned instance is of type Box
    from pymonet.box import Box
    assert isinstance(box_instance, Box)

    # Assert that the value inside the Box is the same as the one in Validation
    assert box_instance.value == 'test_value'
