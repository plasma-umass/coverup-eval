# file: typesystem/schemas.py:150-158
# asked: {"lines": [150, 151, 152, 154, 155, 156, 157, 158], "branches": []}
# gained: {"lines": [150, 151, 152, 154, 155, 156, 157, 158], "branches": []}

import pytest
from typesystem.schemas import Schema, ValidationError, ValidationResult

class TestSchema:
    def test_validate_or_error_success(self, monkeypatch):
        class MockSchema(Schema):
            @classmethod
            def validate(cls, value, strict=False):
                return value

        result = MockSchema.validate_or_error("test_value")
        assert result.value == "test_value"
        assert result.error is None

    def test_validate_or_error_failure(self, monkeypatch):
        class MockSchema(Schema):
            @classmethod
            def validate(cls, value, strict=False):
                raise ValidationError(text="Validation failed")

        result = MockSchema.validate_or_error("test_value")
        assert result.value is None
        assert isinstance(result.error, ValidationError)
        assert str(result.error) == "Validation failed"
