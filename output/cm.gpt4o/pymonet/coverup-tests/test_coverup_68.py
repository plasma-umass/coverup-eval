# file pymonet/validation.py:124-133
# lines [124, 131, 133]
# branches []

import pytest
from pymonet.validation import Validation
from pymonet.box import Box

class TestValidation:
    def test_to_box(self, mocker):
        # Create an instance of Validation with required arguments
        validation_instance = Validation(value='test_value', errors=None)
        
        # Call the to_box method
        result = validation_instance.to_box()
        
        # Assert that the result is a Box instance with the correct value
        assert isinstance(result, Box)
        assert result.value == 'test_value'
