# file pymonet/validation.py:146-155
# lines [153, 155]
# branches []

import pytest
from pymonet.validation import Validation
from pymonet.monad_try import Try

class MockValidation(Validation):
    def __init__(self, value, is_success):
        self.value = value
        self._is_success = is_success

    def is_success(self):
        return self._is_success

def test_to_try_success(mocker):
    mock_value = "test_value"
    mock_is_success = True
    validation_instance = MockValidation(mock_value, mock_is_success)
    
    mocker.patch('pymonet.validation.Validation.is_success', return_value=mock_is_success)
    
    result = validation_instance.to_try()
    
    assert isinstance(result, Try)
    assert result.is_success == mock_is_success
    assert result.value == mock_value

def test_to_try_failure(mocker):
    mock_value = "test_value"
    mock_is_success = False
    validation_instance = MockValidation(mock_value, mock_is_success)
    
    mocker.patch('pymonet.validation.Validation.is_success', return_value=mock_is_success)
    
    result = validation_instance.to_try()
    
    assert isinstance(result, Try)
    assert result.is_success == mock_is_success
    assert result.value == mock_value
