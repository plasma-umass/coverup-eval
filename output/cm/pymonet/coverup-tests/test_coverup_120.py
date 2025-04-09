# file pymonet/either.py:138-147
# lines [145, 147]
# branches []

import pytest
from pymonet.either import Left

def test_left_to_validation(mocker):
    # Mock the import to ensure it's called without affecting other tests
    validation_mock = mocker.patch('pymonet.validation.Validation')
    
    # Create a Left instance
    left_value = 'error'
    left = Left(left_value)
    
    # Call the to_validation method
    result = left.to_validation()
    
    # Assert that the Validation.fail method was called with the correct value
    validation_mock.fail.assert_called_once_with([left_value])
    
    # Assert that the result is the return value from the Validation.fail call
    assert result == validation_mock.fail.return_value
