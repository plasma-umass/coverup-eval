# file: typesystem/schemas.py:150-158
# asked: {"lines": [150, 151, 152, 154, 155, 156, 157, 158], "branches": []}
# gained: {"lines": [150, 151, 152, 154, 155, 156, 157, 158], "branches": []}

import pytest
from typesystem.schemas import Schema
from typesystem.base import ValidationError, ValidationResult

class MockSchema(Schema):
    @classmethod
    def validate(cls, value, *, strict=False):
        if value == "invalid":
            raise ValidationError(text="Invalid value")
        return value

def test_validate_or_error_valid():
    result = MockSchema.validate_or_error("valid")
    assert isinstance(result, ValidationResult)
    assert result.value == "valid"
    assert result.error is None

def test_validate_or_error_invalid():
    result = MockSchema.validate_or_error("invalid")
    assert isinstance(result, ValidationResult)
    assert result.value is None
    assert isinstance(result.error, ValidationError)
