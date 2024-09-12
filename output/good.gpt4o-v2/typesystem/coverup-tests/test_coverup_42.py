# file: typesystem/schemas.py:192-201
# asked: {"lines": [192, 193, 194, 195, 197, 198, 200, 201], "branches": []}
# gained: {"lines": [192, 193, 194, 195, 197, 198, 200, 201], "branches": []}

import pytest
import typing
from typesystem.schemas import Schema, SchemaMetaclass
from typesystem.fields import Field

class MockField(Field):
    def validate(self, value: typing.Any, *, strict: bool=False) -> typing.Any:
        return value

    def validate_or_error(self, value: typing.Any, *, strict: bool=False) -> typing.Any:
        return value, None

class TestSchema(Schema):
    field1 = MockField(default="default1")
    field2 = MockField(default="default2")

def test_schema_repr():
    schema_instance = TestSchema(field1="value1", field2="value2")
    expected_repr = "TestSchema(field1='value1', field2='value2')"
    assert repr(schema_instance) == expected_repr

def test_schema_repr_with_sparse(monkeypatch):
    schema_instance = TestSchema(field1="value1", field2="value2")
    
    def mock_is_sparse(self):
        return True
    
    monkeypatch.setattr(TestSchema, 'is_sparse', property(mock_is_sparse))
    
    expected_repr = "TestSchema(field1='value1', field2='value2') [sparse]"
    assert repr(schema_instance) == expected_repr
