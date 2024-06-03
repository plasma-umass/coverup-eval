# file pymonet/validation.py:111-122
# lines [118, 120, 121, 122]
# branches ['120->121', '120->122']

import pytest
from pymonet.validation import Validation
from pymonet.maybe import Maybe

class MockValidationSuccess(Validation):
    def __init__(self):
        self.value = "success_value"
        self.errors = []

    def is_success(self):
        return True

class MockValidationFailure(Validation):
    def __init__(self):
        self.value = None
        self.errors = ["error"]

    def is_success(self):
        return False

def test_validation_to_maybe_success():
    validation = MockValidationSuccess()
    maybe = validation.to_maybe()
    assert maybe == Maybe.just("success_value")

def test_validation_to_maybe_failure():
    validation = MockValidationFailure()
    maybe = validation.to_maybe()
    assert maybe == Maybe.nothing()
