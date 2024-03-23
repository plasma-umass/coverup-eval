# file pymonet/validation.py:54-61
# lines [54, 61]
# branches []

import pytest
from pymonet.validation import Validation

class MockValidation(Validation):
    def __init__(self, errors):
        self.errors = errors

@pytest.fixture
def mock_validation_empty():
    return MockValidation([])

@pytest.fixture
def mock_validation_with_errors():
    return MockValidation(['error1', 'error2'])

def test_is_fail_with_empty_errors(mock_validation_empty):
    assert not mock_validation_empty.is_fail()

def test_is_fail_with_non_empty_errors(mock_validation_with_errors):
    assert mock_validation_with_errors.is_fail()
