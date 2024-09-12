# file: typesystem/json_schema.py:370-373
# asked: {"lines": [371, 372, 373], "branches": []}
# gained: {"lines": [371, 372, 373], "branches": []}

import pytest
from typesystem.json_schema import not_from_json_schema
from typesystem.composites import Not
from typesystem.fields import NO_DEFAULT, Field
from typesystem.schemas import SchemaDefinitions
from typesystem.json_schema import from_json_schema

def test_not_from_json_schema(monkeypatch):
    # Mock the from_json_schema function to return a specific Field instance
    class MockField(Field):
        pass

    def mock_from_json_schema(data, definitions):
        return MockField()

    monkeypatch.setattr('typesystem.json_schema.from_json_schema', mock_from_json_schema)

    data = {
        "not": {"type": "string"},
        "default": "default_value"
    }
    definitions = SchemaDefinitions()

    result = not_from_json_schema(data, definitions)

    assert isinstance(result, Not)
    assert isinstance(result.negated, MockField)
    assert result.default == "default_value"

def test_not_from_json_schema_no_default(monkeypatch):
    # Mock the from_json_schema function to return a specific Field instance
    class MockField(Field):
        pass

    def mock_from_json_schema(data, definitions):
        return MockField()

    monkeypatch.setattr('typesystem.json_schema.from_json_schema', mock_from_json_schema)

    data = {
        "not": {"type": "string"}
    }
    definitions = SchemaDefinitions()

    result = not_from_json_schema(data, definitions)

    assert isinstance(result, Not)
    assert isinstance(result.negated, MockField)
    assert not hasattr(result, 'default') or result.default is NO_DEFAULT
