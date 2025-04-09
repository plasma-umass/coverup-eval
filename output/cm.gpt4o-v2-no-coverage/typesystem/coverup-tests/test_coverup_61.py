# file: typesystem/schemas.py:189-190
# asked: {"lines": [189, 190], "branches": []}
# gained: {"lines": [189, 190], "branches": []}

import pytest
from typesystem.schemas import Schema, SchemaMetaclass
from typesystem.fields import Field

class TestSchema:
    def test_len_with_no_fields(self):
        class EmptySchema(Schema):
            pass

        schema = EmptySchema()
        assert len(schema) == 0

    def test_len_with_fields(self):
        class MySchema(Schema):
            field1 = Field()
            field2 = Field()

        schema = MySchema()
        assert len(schema) == 0

        schema.field1 = "value1"
        assert len(schema) == 1

        schema.field2 = "value2"
        assert len(schema) == 2

    def test_len_with_inherited_fields(self):
        class BaseSchema(Schema):
            field1 = Field()

        class ChildSchema(BaseSchema):
            field2 = Field()

        schema = ChildSchema()
        assert len(schema) == 0

        schema.field1 = "value1"
        assert len(schema) == 1

        schema.field2 = "value2"
        assert len(schema) == 2
