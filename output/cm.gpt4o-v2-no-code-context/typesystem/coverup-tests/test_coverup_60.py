# file: typesystem/json_schema.py:340-343
# asked: {"lines": [341, 342, 343], "branches": []}
# gained: {"lines": [341, 342, 343], "branches": []}

import pytest
from typesystem.json_schema import enum_from_json_schema, SchemaDefinitions, Choice, NO_DEFAULT

def test_enum_from_json_schema_with_default():
    data = {
        "enum": ["value1", "value2", "value3"],
        "default": "value1"
    }
    definitions = SchemaDefinitions()
    field = enum_from_json_schema(data, definitions)
    
    assert isinstance(field, Choice)
    assert field.choices == [("value1", "value1"), ("value2", "value2"), ("value3", "value3")]
    assert field.default == "value1"

def test_enum_from_json_schema_without_default():
    data = {
        "enum": ["value1", "value2", "value3"]
    }
    definitions = SchemaDefinitions()
    field = enum_from_json_schema(data, definitions)
    
    assert isinstance(field, Choice)
    assert field.choices == [("value1", "value1"), ("value2", "value2"), ("value3", "value3")]
    assert not hasattr(field, 'default') or field.default == NO_DEFAULT
