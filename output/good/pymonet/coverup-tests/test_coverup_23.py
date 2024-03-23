# file pymonet/validation.py:16-19
# lines [16, 17, 18, 19]
# branches ['17->18', '17->19']

import pytest
from pymonet.validation import Validation

class SuccessValidation(Validation):
    def __init__(self, value):
        self._value = value

    def is_success(self):
        return True

    @property
    def value(self):
        return self._value

class FailValidation(Validation):
    def __init__(self, value, errors):
        self._value = value
        self._errors = errors

    def is_success(self):
        return False

    @property
    def value(self):
        return self._value

    @property
    def errors(self):
        return self._errors

def test_validation_str_success():
    success_validation = SuccessValidation("success_value")
    assert str(success_validation) == "Validation.success[success_value]"

def test_validation_str_fail():
    fail_validation = FailValidation("fail_value", ["error1", "error2"])
    assert str(fail_validation) == "Validation.fail[fail_value, ['error1', 'error2']]"
