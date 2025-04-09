# file pymonet/validation.py:74-83
# lines [74, 83]
# branches []

import pytest
from pymonet.validation import Validation

class TestValidation:
    def test_bind(self, mocker):
        # Create a mock function to use as the folder
        mock_folder = mocker.Mock(return_value="new_value")
        
        # Create an instance of Validation with a value and errors
        validation_instance = Validation(value="initial_value", errors=None)
        
        # Call the bind method with the mock function
        result = validation_instance.bind(mock_folder)
        
        # Assert that the folder function was called with the correct value
        mock_folder.assert_called_once_with("initial_value")
        
        # Assert that the result is the expected new value
        assert result == "new_value"
