# file: typesystem/schemas.py:184-187
# asked: {"lines": [184, 185, 186, 187], "branches": [[185, 0], [185, 186], [186, 185], [186, 187]]}
# gained: {"lines": [184, 185, 186, 187], "branches": [[185, 0], [185, 186], [186, 185], [186, 187]]}

import pytest
import typing
from typesystem.schemas import Schema, SchemaMetaclass
from typesystem.fields import Field

class MockField(Field):
    def validate(self, value: typing.Any, *, strict: bool=False) -> typing.Any:
        return value

class TestSchema(Schema):
    field1 = MockField()
    field2 = MockField()

def test_schema_iter():
    schema = TestSchema(field1="value1", field2="value2")
    keys = list(iter(schema))
    assert "field1" in keys
    assert "field2" in keys

def test_schema_iter_with_missing_field():
    schema = TestSchema(field1="value1")
    keys = list(iter(schema))
    assert "field1" in keys
    assert "field2" not in keys
