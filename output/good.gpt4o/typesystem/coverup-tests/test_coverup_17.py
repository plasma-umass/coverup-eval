# file typesystem/schemas.py:150-158
# lines [150, 151, 152, 154, 155, 156, 157, 158]
# branches []

import pytest
from typesystem.schemas import Schema, ValidationError, ValidationResult

class MockValidationError(ValidationError):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

class MockSchema(Schema):
    @classmethod
    def validate(cls, value, strict=False):
        if value == "invalid":
            raise MockValidationError("Invalid value")
        return value

def test_validate_or_error_success():
    result = MockSchema.validate_or_error("valid")
    assert isinstance(result, ValidationResult)
    assert result.value == "valid"
    assert result.error is None

def test_validate_or_error_failure():
    result = MockSchema.validate_or_error("invalid")
    assert isinstance(result, ValidationResult)
    assert result.value is None
    assert isinstance(result.error, MockValidationError)
    assert str(result.error) == "Invalid value"
