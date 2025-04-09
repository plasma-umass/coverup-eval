# file pymonet/validation.py:146-155
# lines [146, 153, 155]
# branches []

import pytest
from pymonet.validation import Validation
from pymonet.monad_try import Try

@pytest.fixture
def mock_try(mocker):
    return mocker.patch('pymonet.monad_try.Try', autospec=True)

def test_validation_to_try_success(mock_try):
    # Create a Validation instance with no errors (success)
    validation = Validation('test_value', [])

    # Call the to_try method
    result = validation.to_try()

    # Assertions to check if Try was called correctly
    mock_try.assert_called_once_with('test_value', is_success=True)

def test_validation_to_try_failure(mock_try):
    # Create a Validation instance with errors (failure)
    validation = Validation('test_value', ['error'])

    # Call the to_try method
    result = validation.to_try()

    # Assertions to check if Try was called correctly
    mock_try.assert_called_once_with('test_value', is_success=False)
