# file pymonet/validation.py:45-52
# lines [45, 52]
# branches []

import pytest
from pymonet.validation import Validation

class MockValidation(Validation):
    def __init__(self, errors):
        self.errors = errors

@pytest.fixture
def mock_validation_empty():
    return MockValidation(errors=[])

@pytest.fixture
def mock_validation_with_errors():
    return MockValidation(errors=['error1', 'error2'])

def test_is_success_with_empty_errors(mock_validation_empty):
    assert mock_validation_empty.is_success() is True

def test_is_success_with_errors(mock_validation_with_errors):
    assert mock_validation_with_errors.is_success() is False
