# file pymonet/validation.py:98-109
# lines [98, 105, 107, 108, 109]
# branches ['107->108', '107->109']

import pytest
from pymonet.validation import Validation
from pymonet.either import Left, Right

class SuccessValidation(Validation):
    def __init__(self):
        self._value = 'success value'

    def is_success(self):
        return True

    @property
    def value(self):
        return self._value

class FailureValidation(Validation):
    def __init__(self):
        self._errors = ['error1', 'error2']

    def is_success(self):
        return False

    @property
    def errors(self):
        return self._errors

def test_validation_to_either_success():
    validation = SuccessValidation()
    result = validation.to_either()
    assert isinstance(result, Right)
    assert result.value == 'success value'

def test_validation_to_either_failure():
    validation = FailureValidation()
    result = validation.to_either()
    assert isinstance(result, Left)
    assert result.value == ['error1', 'error2']
