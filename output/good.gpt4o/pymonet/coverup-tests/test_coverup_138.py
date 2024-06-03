# file pymonet/either.py:138-147
# lines [145, 147]
# branches []

import pytest
from pymonet.either import Left

def test_left_to_validation(mocker):
    # Mock the Validation class from pymonet.validation
    ValidationMock = mocker.patch('pymonet.validation.Validation')
    
    # Create an instance of Left with a sample value
    left_instance = Left("error_value")
    
    # Call the to_validation method
    result = left_instance.to_validation()
    
    # Assert that Validation.fail was called with the correct argument
    ValidationMock.fail.assert_called_once_with(["error_value"])
    
    # Assert that the result is the return value of Validation.fail
    assert result == ValidationMock.fail.return_value
