# file pymonet/validation.py:98-109
# lines [98, 105, 107, 108, 109]
# branches ['107->108', '107->109']

import pytest
from pymonet.validation import Validation
from pymonet.either import Left, Right

class MockValidation(Validation):
    def __init__(self, success, value=None, errors=None):
        self._success = success
        self.value = value
        self.errors = errors

    def is_success(self):
        return self._success

def test_validation_to_either_success():
    validation = MockValidation(success=True, value="valid_value")
    result = validation.to_either()
    assert isinstance(result, Right)
    assert result.value == "valid_value"

def test_validation_to_either_failure():
    validation = MockValidation(success=False, errors=["error1", "error2"])
    result = validation.to_either()
    assert isinstance(result, Left)
    assert result.value == ["error1", "error2"]
