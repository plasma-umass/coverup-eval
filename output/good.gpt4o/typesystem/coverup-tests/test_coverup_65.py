# file typesystem/json_schema.py:340-343
# lines [340, 341, 342, 343]
# branches []

import pytest
from typesystem.json_schema import enum_from_json_schema
from typesystem import SchemaDefinitions, Choice, Field

def test_enum_from_json_schema():
    NO_DEFAULT = object()  # Define NO_DEFAULT locally for the test

    data = {
        "enum": ["red", "green", "blue"],
        "default": "green"
    }
    definitions = SchemaDefinitions()
    
    field = enum_from_json_schema(data, definitions)
    
    assert isinstance(field, Choice)
    assert field.choices == [("red", "red"), ("green", "green"), ("blue", "blue")]
    assert field.default == "green"

    # Test without default value
    data_no_default = {
        "enum": ["red", "green", "blue"]
    }
    
    field_no_default = enum_from_json_schema(data_no_default, definitions)
    
    assert isinstance(field_no_default, Choice)
    assert field_no_default.choices == [("red", "red"), ("green", "green"), ("blue", "blue")]
    assert not hasattr(field_no_default, 'default') or field_no_default.default is NO_DEFAULT
