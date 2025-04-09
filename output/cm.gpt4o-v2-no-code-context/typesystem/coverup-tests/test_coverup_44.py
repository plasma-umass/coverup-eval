# file: typesystem/base.py:187-188
# asked: {"lines": [187, 188], "branches": []}
# gained: {"lines": [187, 188], "branches": []}

import pytest
from typesystem.base import BaseError, ValidationError

class MockValidationError(ValidationError):
    def __init__(self, messages):
        self._messages = messages

class MockBaseError(BaseError):
    def __init__(self, messages):
        self._messages = messages

def test_base_error_eq_with_validation_error():
    error1 = MockBaseError(["error1"])
    error2 = MockValidationError(["error1"])
    
    assert error1 == error2

def test_base_error_eq_with_non_validation_error():
    error1 = MockBaseError(["error1"])
    error2 = MockBaseError(["error1"])
    
    assert error1 != error2
