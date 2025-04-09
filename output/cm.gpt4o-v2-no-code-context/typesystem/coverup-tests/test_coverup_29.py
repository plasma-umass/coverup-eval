# file: typesystem/fields.py:53-60
# asked: {"lines": [53, 54, 56, 57, 58, 59, 60], "branches": []}
# gained: {"lines": [53, 54, 56, 57, 58, 59, 60], "branches": []}

import pytest
from typesystem.fields import Field, ValidationError, ValidationResult

class MockValidationError(ValidationError):
    def __init__(self, message):
        self.message = message

class MockField(Field):
    def validate(self, value, strict=False):
        if value == "invalid":
            raise MockValidationError("Invalid value")
        return value

def test_validate_or_error_valid_value():
    field = MockField()
    result = field.validate_or_error("valid")
    assert result.value == "valid"
    assert result.error is None

def test_validate_or_error_invalid_value():
    field = MockField()
    result = field.validate_or_error("invalid")
    assert result.value is None
    assert isinstance(result.error, MockValidationError)
    assert str(result.error.message) == "Invalid value"
