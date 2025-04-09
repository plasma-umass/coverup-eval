# file: typesystem/json_schema.py:352-355
# asked: {"lines": [353, 354, 355], "branches": []}
# gained: {"lines": [353, 354, 355], "branches": []}

import pytest
from typesystem.json_schema import all_of_from_json_schema, from_json_schema
from typesystem.schemas import SchemaDefinitions
from typesystem.fields import NO_DEFAULT, Field
from typesystem.composites import AllOf

def test_all_of_from_json_schema(monkeypatch):
    # Mock the from_json_schema function to return a simple Field instance
    def mock_from_json_schema(item, definitions):
        return Field()

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
    assert result.default == "default_value"

    # Clean up
    monkeypatch.undo()
