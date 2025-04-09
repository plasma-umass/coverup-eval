# file typesystem/schemas.py:92-94
# lines [92, 93]
# branches []

import pytest
from typesystem.schemas import Schema, SchemaMetaclass
from typesystem.fields import Field
from collections.abc import Mapping

def test_schema_class():
    class TestField(Field):
        def validate(self, value, *, context=None):
            return value

    class TestSchema(Schema):
        @classmethod
        def get_fields(cls):
            return {
                "name": TestField(),
                "age": TestField()
            }

    schema_instance = TestSchema()

    # Check if schema_instance is an instance of Mapping
    assert isinstance(schema_instance, Mapping)

    # Check if fields are correctly set
    fields = schema_instance.get_fields()
    assert "name" in fields
    assert "age" in fields

    # Check if fields are instances of Field
    assert isinstance(fields["name"], Field)
    assert isinstance(fields["age"], Field)

    # Check if metaclass is SchemaMetaclass
    assert isinstance(TestSchema, SchemaMetaclass)
