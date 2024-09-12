# file: typesystem/json_schema.py:364-367
# asked: {"lines": [364, 365, 366, 367], "branches": []}
# gained: {"lines": [364, 365, 366, 367], "branches": []}

import pytest
from typesystem.json_schema import one_of_from_json_schema, from_json_schema
from typesystem.schemas import SchemaDefinitions
from typesystem.fields import NO_DEFAULT, Field
from typesystem.composites import OneOf

def test_one_of_from_json_schema(monkeypatch):
    # Mocking from_json_schema to return a simple Field instance
    def mock_from_json_schema(item, definitions):
        return Field()

    monkeypatch.setattr('typesystem.json_schema.from_json_schema', mock_from_json_schema)

    data = {
        "oneOf": [
            {"type": "string"},
            {"type": "number"}
        ],
        "default": "default_value"
    }
    definitions = SchemaDefinitions()

    result = one_of_from_json_schema(data, definitions)

    assert isinstance(result, OneOf)
    assert len(result.one_of) == 2
    assert result.default == "default_value"

def test_one_of_from_json_schema_no_default(monkeypatch):
    # Mocking from_json_schema to return a simple Field instance
    def mock_from_json_schema(item, definitions):
        return Field()

    monkeypatch.setattr('typesystem.json_schema.from_json_schema', mock_from_json_schema)

    data = {
        "oneOf": [
            {"type": "string"},
            {"type": "number"}
        ]
    }
    definitions = SchemaDefinitions()

    result = one_of_from_json_schema(data, definitions)

    assert isinstance(result, OneOf)
    assert len(result.one_of) == 2
    assert not hasattr(result, 'default')
