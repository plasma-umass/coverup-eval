# file: typesystem/schemas.py:184-187
# asked: {"lines": [184, 185, 186, 187], "branches": [[185, 0], [185, 186], [186, 185], [186, 187]]}
# gained: {"lines": [184, 185, 186, 187], "branches": [[185, 0], [185, 186], [186, 185], [186, 187]]}

import typing
import pytest
from typesystem.schemas import Schema, SchemaMetaclass
from typesystem.fields import Field
from typesystem.base import ValidationError

class StringField(Field):
    def validate(self, value: typing.Any, *, strict: bool=False) -> typing.Any:
        if not isinstance(value, str):
            raise ValidationError("Must be a string")
        return value

class TestSchema:
    def test_schema_iter(self):
        class TestSchema(Schema):
            field1 = StringField()
            field2 = StringField()

        schema_instance = TestSchema(field1="value1", field2="value2")
        keys = list(iter(schema_instance))
        assert keys == ["field1", "field2"]

    def test_schema_iter_no_fields(self):
        class TestSchema(Schema):
            pass

        schema_instance = TestSchema()
        keys = list(iter(schema_instance))
        assert keys == []

    def test_schema_iter_missing_field(self):
        class TestSchema(Schema):
            field1 = StringField()

        schema_instance = TestSchema(field1="value1")
        del schema_instance.field1
        keys = list(iter(schema_instance))
        assert keys == []

    def test_schema_iter_with_inherited_fields(self):
        class BaseSchema(Schema):
            base_field = StringField()

        class ChildSchema(BaseSchema):
            child_field = StringField()

        schema_instance = ChildSchema(base_field="base_value", child_field="child_value")
        keys = list(iter(schema_instance))
        assert keys == ["base_field", "child_field"]
