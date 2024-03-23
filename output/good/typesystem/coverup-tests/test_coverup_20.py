# file typesystem/fields.py:53-60
# lines [53, 54, 56, 57, 58, 59, 60]
# branches []

import pytest
from typesystem.fields import Field, ValidationError, ValidationResult

class DummyField(Field):
    def validate(self, value, strict=False):
        if strict and value != "strict_value":
            raise ValidationError(text="Strict mode requires 'strict_value'.")
        return value

@pytest.fixture
def dummy_field():
    return DummyField()

def test_validate_or_error_without_error(dummy_field):
    result = dummy_field.validate_or_error("any_value")
    assert result.value == "any_value"
    assert result.error is None

def test_validate_or_error_with_error(dummy_field):
    result = dummy_field.validate_or_error("wrong_value", strict=True)
    assert result.value is None
    assert isinstance(result.error, ValidationError)
    assert str(result.error) == "Strict mode requires 'strict_value'."

def test_validate_or_error_with_strict_value(dummy_field):
    result = dummy_field.validate_or_error("strict_value", strict=True)
    assert result.value == "strict_value"
    assert result.error is None
