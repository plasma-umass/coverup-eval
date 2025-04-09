# file pymonet/validation.py:16-19
# lines [16, 17, 18, 19]
# branches ['17->18', '17->19']

import pytest
from pymonet.validation import Validation

class MockValidation(Validation):
    def __init__(self, value, errors=None):
        self.value = value
        self.errors = errors

    def is_success(self):
        return self.errors is None

def test_validation_str_success():
    validation = MockValidation(value="test_value")
    result = str(validation)
    assert result == 'Validation.success[test_value]'

def test_validation_str_fail():
    validation = MockValidation(value="test_value", errors="test_error")
    result = str(validation)
    assert result == 'Validation.fail[test_value, test_error]'
