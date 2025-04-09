# file: typesystem/fields.py:53-60
# asked: {"lines": [53, 54, 56, 57, 58, 59, 60], "branches": []}
# gained: {"lines": [53, 54, 56, 57, 58, 59, 60], "branches": []}

import typing
import pytest
from typesystem.base import ValidationError, ValidationResult, Message, Position
from typesystem.fields import Field

class MockField(Field):
    def validate(self, value: typing.Any, *, strict: bool=False) -> typing.Any:
        if value == "raise_error":
            raise ValidationError(text="Validation error")
        return value

@pytest.fixture
def mock_field():
    return MockField()

def test_validate_or_error_success(mock_field):
    result = mock_field.validate_or_error("valid_value")
    assert result.value == "valid_value"
    assert result.error is None

def test_validate_or_error_failure(mock_field):
    result = mock_field.validate_or_error("raise_error")
    assert result.value is None
    assert isinstance(result.error, ValidationError)
    assert str(result.error) == "Validation error"

def test_validate_or_error_strict(mock_field):
    result = mock_field.validate_or_error("valid_value", strict=True)
    assert result.value == "valid_value"
    assert result.error is None
