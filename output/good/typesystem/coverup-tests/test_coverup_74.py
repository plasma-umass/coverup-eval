# file typesystem/base.py:187-188
# lines [187, 188]
# branches []

import pytest
from typesystem.base import BaseError
from typesystem import ValidationError

class MockBaseError(BaseError):
    def __init__(self, messages):
        self._messages = messages

class MockValidationError(ValidationError):
    def __init__(self, messages):
        self._messages = messages

def test_base_error_eq():
    error = MockBaseError({"field": "error_message"})
    validation_error = MockValidationError({"field": "error_message"})
    different_error = MockValidationError({"field": "different_message"})
    non_error = {"field": "error_message"}

    # Test equality with ValidationError with same messages
    assert error == validation_error

    # Test inequality with ValidationError with different messages
    assert not (error == different_error)

    # Test inequality with non-ValidationError
    assert not (error == non_error)

    # Clean up is not necessary as no external resources or state changes are involved
