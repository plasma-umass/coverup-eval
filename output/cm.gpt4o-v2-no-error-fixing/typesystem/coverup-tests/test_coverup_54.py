# file: typesystem/schemas.py:189-190
# asked: {"lines": [190], "branches": []}
# gained: {"lines": [190], "branches": []}

import pytest
from typesystem.schemas import Schema, SchemaMetaclass
from typesystem.fields import Field

class TestField(Field):
    def validate_or_error(self, value):
        return value, None

    def has_default(self):
        return False

    def get_default_value(self):
        return None

class TestSchema(Schema, metaclass=SchemaMetaclass):
    field1 = TestField()
    field2 = TestField()

def test_schema_len():
    schema = TestSchema(field1="value1", field2="value2")
    assert len(schema) == 2

    schema = TestSchema(field1="value1")
    assert len(schema) == 1

    schema = TestSchema()
    assert len(schema) == 0
