# file: typesystem/json_schema.py:340-343
# asked: {"lines": [340, 341, 342, 343], "branches": []}
# gained: {"lines": [340, 341, 342, 343], "branches": []}

import pytest
from typesystem.fields import NO_DEFAULT, Choice
from typesystem.schemas import SchemaDefinitions
from typesystem.json_schema import enum_from_json_schema

def test_enum_from_json_schema():
    data = {
        "enum": ["red", "green", "blue"],
        "default": "green"
    }
    definitions = SchemaDefinitions()
    field = enum_from_json_schema(data, definitions)
    
    assert isinstance(field, Choice)
    assert field.choices == [("red", "red"), ("green", "green"), ("blue", "blue")]
    assert field.default == "green"

def test_enum_from_json_schema_no_default():
    data = {
        "enum": ["red", "green", "blue"]
    }
    definitions = SchemaDefinitions()
    field = enum_from_json_schema(data, definitions)
    
    assert isinstance(field, Choice)
    assert field.choices == [("red", "red"), ("green", "green"), ("blue", "blue")]
    assert not hasattr(field, 'default')
