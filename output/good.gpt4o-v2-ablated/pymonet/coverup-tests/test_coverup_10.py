# file: pymonet/validation.py:16-19
# asked: {"lines": [16, 17, 18, 19], "branches": [[17, 18], [17, 19]]}
# gained: {"lines": [16, 17, 18, 19], "branches": [[17, 18], [17, 19]]}

import pytest
from pymonet.validation import Validation

class MockValidationSuccess(Validation):
    def __init__(self, value):
        self.value = value

    def is_success(self):
        return True

class MockValidationFail(Validation):
    def __init__(self, value, errors):
        self.value = value
        self.errors = errors

    def is_success(self):
        return False

def test_validation_str_success():
    validation = MockValidationSuccess("test_value")
    result = str(validation)
    assert result == 'Validation.success[test_value]'

def test_validation_str_fail():
    validation = MockValidationFail("test_value", "test_error")
    result = str(validation)
    assert result == 'Validation.fail[test_value, test_error]'
