# file typesystem/schemas.py:142-148
# lines [142, 143, 144, 146, 147, 148]
# branches []

import pytest
from unittest import mock
from typesystem.schemas import Schema, SchemaMetaclass

class TestSchema(Schema):
    def __init__(self, value):
        self.value = value

    @classmethod
    def make_validator(cls, strict=False):
        class Validator:
            def validate(self, value, strict=False):
                return value
        return Validator()

def test_schema_validate():
    value = {"key": "value"}
    strict = True

    with mock.patch.object(TestSchema, 'make_validator', wraps=TestSchema.make_validator) as mock_make_validator:
        schema_instance = TestSchema.validate(value, strict=strict)
        mock_make_validator.assert_called_once_with(strict=strict)
        assert isinstance(schema_instance, TestSchema)
        assert schema_instance.value == value
