# file: typesystem/json_schema.py:358-361
# asked: {"lines": [358, 359, 360, 361], "branches": []}
# gained: {"lines": [358, 359, 360, 361], "branches": []}

import pytest
from typesystem.fields import NO_DEFAULT, Field, Union
from typesystem.schemas import SchemaDefinitions
from typesystem.json_schema import any_of_from_json_schema, from_json_schema

def test_any_of_from_json_schema_with_default():
    data = {
        "anyOf": [
            {"type": "string"},
            {"type": "number"}
        ],
        "default": "default_value"
    }
    definitions = SchemaDefinitions()
    field = any_of_from_json_schema(data, definitions)
    
    assert isinstance(field, Union)
    assert field.get_default_value() == "default_value"
    assert len(field.any_of) == 2
    assert isinstance(field.any_of[0], Field)
    assert isinstance(field.any_of[1], Field)

def test_any_of_from_json_schema_without_default():
    data = {
        "anyOf": [
            {"type": "string"},
            {"type": "number"}
        ]
    }
    definitions = SchemaDefinitions()
    field = any_of_from_json_schema(data, definitions)
    
    assert isinstance(field, Union)
    assert not field.has_default()
    assert len(field.any_of) == 2
    assert isinstance(field.any_of[0], Field)
    assert isinstance(field.any_of[1], Field)
