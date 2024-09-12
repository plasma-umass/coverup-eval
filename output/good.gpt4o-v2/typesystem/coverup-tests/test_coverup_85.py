# file: typesystem/schemas.py:189-190
# asked: {"lines": [190], "branches": []}
# gained: {"lines": [190], "branches": []}

import pytest
import typing
from typesystem.schemas import Schema, SchemaMetaclass
from typesystem.fields import Field, ValidationError

class StringField(Field):
    def validate(self, value: typing.Any, *, strict: bool=False) -> typing.Any:
        if not isinstance(value, str):
            raise ValidationError("Must be a string.")
        return value

class TestSchema(Schema):
    field1 = StringField()
    field2 = StringField()

def test_schema_len():
    schema_instance = TestSchema(field1="value1", field2="value2")
    assert len(schema_instance) == 2

    # Test with one field not set
    schema_instance = TestSchema(field1="value1")
    assert len(schema_instance) == 1

    # Test with no fields set
    schema_instance = TestSchema()
    assert len(schema_instance) == 0
