# file: typesystem/json_schema.py:352-355
# asked: {"lines": [352, 353, 354, 355], "branches": []}
# gained: {"lines": [352, 353, 354, 355], "branches": []}

import pytest
from typesystem.json_schema import all_of_from_json_schema
from typesystem.composites import AllOf
from typesystem.fields import NO_DEFAULT, Field
from typesystem.schemas import SchemaDefinitions
from typesystem.json_schema import from_json_schema

class MockField(Field):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

def test_all_of_from_json_schema(monkeypatch):
    # Mock the from_json_schema function to return a MockField
    def mock_from_json_schema(item, definitions):
        return MockField()

    monkeypatch.setattr('typesystem.json_schema.from_json_schema', mock_from_json_schema)

    data = {
        "allOf": [
            {"type": "string"},
            {"type": "number"}
        ],
        "default": "default_value"
    }
    definitions = SchemaDefinitions()

    result = all_of_from_json_schema(data, definitions)

    assert isinstance(result, AllOf)
    assert len(result.all_of) == 2
    assert all(isinstance(field, MockField) for field in result.all_of)
    assert result.default == "default_value"

def test_all_of_from_json_schema_no_default(monkeypatch):
    # Mock the from_json_schema function to return a MockField
    def mock_from_json_schema(item, definitions):
        return MockField()

    monkeypatch.setattr('typesystem.json_schema.from_json_schema', mock_from_json_schema)

    data = {
        "allOf": [
            {"type": "string"},
            {"type": "number"}
        ]
    }
    definitions = SchemaDefinitions()

    result = all_of_from_json_schema(data, definitions)

    assert isinstance(result, AllOf)
    assert len(result.all_of) == 2
    assert all(isinstance(field, MockField) for field in result.all_of)
    assert not hasattr(result, 'default') or result.default is NO_DEFAULT
