# file: typesystem/schemas.py:142-148
# asked: {"lines": [142, 143, 144, 146, 147, 148], "branches": []}
# gained: {"lines": [142, 143, 144, 146, 147, 148], "branches": []}

import pytest
from typesystem.schemas import Schema, SchemaMetaclass

class TestSchema(Schema):
    @classmethod
    def make_validator(cls, strict: bool = False):
        class Validator:
            def validate(self, value, strict: bool = False):
                return value
        return Validator()

    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        if isinstance(other, dict):
            return self.value == other
        return super().__eq__(other)

def test_schema_validate():
    value = {"key": "value"}
    result = TestSchema.validate(value, strict=True)
    assert isinstance(result, TestSchema)
    assert result.value == value
