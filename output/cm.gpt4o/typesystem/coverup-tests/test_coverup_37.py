# file typesystem/fields.py:53-60
# lines [53, 54, 56, 57, 58, 59, 60]
# branches []

import pytest
from typesystem.fields import Field, ValidationError, ValidationResult

class MockValidationError(ValidationError):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

class MockField(Field):
    def validate(self, value, strict=False):
        if strict and not isinstance(value, int):
            raise MockValidationError("Value must be an integer in strict mode.")
        if not value:
            raise MockValidationError("Value cannot be empty.")
        return value

def test_validate_or_error_success():
    field = MockField()
    result = field.validate_or_error(10)
    assert result.value == 10
    assert result.error is None

def test_validate_or_error_strict_mode_failure():
    field = MockField()
    result = field.validate_or_error("string", strict=True)
    assert result.value is None
    assert isinstance(result.error, MockValidationError)
    assert str(result.error) == "Value must be an integer in strict mode."

def test_validate_or_error_empty_value_failure():
    field = MockField()
    result = field.validate_or_error("")
    assert result.value is None
    assert isinstance(result.error, MockValidationError)
    assert str(result.error) == "Value cannot be empty."
