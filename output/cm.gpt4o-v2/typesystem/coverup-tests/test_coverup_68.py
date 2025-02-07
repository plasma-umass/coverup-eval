# file: typesystem/json_schema.py:358-361
# asked: {"lines": [358, 359, 360, 361], "branches": []}
# gained: {"lines": [358, 359, 360, 361], "branches": []}

import pytest
from typesystem.fields import NO_DEFAULT, Union, Field
from typesystem.schemas import SchemaDefinitions
from typesystem.json_schema import any_of_from_json_schema, from_json_schema

class MockField(Field):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.allow_null = False

def test_any_of_from_json_schema(monkeypatch):
    # Mock the from_json_schema function to return a simple Field for testing
    def mock_from_json_schema(item, definitions):
        return MockField()
    
    monkeypatch.setattr('typesystem.json_schema.from_json_schema', mock_from_json_schema)
    
    data = {
        "anyOf": [
            {"type": "string"},
            {"type": "number"}
        ],
        "default": "default_value"
    }
    definitions = SchemaDefinitions()
    
    result = any_of_from_json_schema(data, definitions)
    
    assert isinstance(result, Union)
    assert len(result.any_of) == 2
    assert isinstance(result.any_of[0], MockField)
    assert isinstance(result.any_of[1], MockField)
    assert result.default == "default_value"

    # Clean up monkeypatch
    monkeypatch.undo()
