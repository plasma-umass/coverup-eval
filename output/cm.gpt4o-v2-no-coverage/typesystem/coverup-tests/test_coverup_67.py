# file: typesystem/json_schema.py:364-367
# asked: {"lines": [364, 365, 366, 367], "branches": []}
# gained: {"lines": [364, 365, 366, 367], "branches": []}

import pytest
from typesystem.composites import OneOf
from typesystem.fields import NO_DEFAULT, Field
from typesystem.schemas import SchemaDefinitions
from typesystem.json_schema import one_of_from_json_schema
from typesystem.json_schema import from_json_schema

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
    assert isinstance(result.one_of[0], Field)
    assert isinstance(result.one_of[1], Field)
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
    assert isinstance(result.one_of[0], Field)
    assert isinstance(result.one_of[1], Field)
    assert result.default is NO_DEFAULT if hasattr(result, 'default') else True
