# file pymonet/either.py:200-209
# lines [207, 209]
# branches []

import pytest
from pymonet.either import Right

def test_right_to_validation(mocker):
    # Mock the Validation class from pymonet.validation
    Validation = mocker.patch('pymonet.validation.Validation')
    
    # Create a Right instance with a test value
    test_value = "test"
    right_instance = Right(test_value)
    
    # Call the to_validation method
    result = right_instance.to_validation()
    
    # Assert that Validation.success was called with the correct value
    Validation.success.assert_called_once_with(test_value)
    
    # Assert that the result is the return value of Validation.success
    assert result == Validation.success.return_value
