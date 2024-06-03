# file typesystem/json_schema.py:346-349
# lines [347, 348, 349]
# branches []

import pytest
from typesystem.json_schema import const_from_json_schema, SchemaDefinitions, Const, NO_DEFAULT

def test_const_from_json_schema():
    data = {
        "const": "test_value",
        "default": "default_value"
    }
    definitions = SchemaDefinitions()
    
    field = const_from_json_schema(data, definitions)
    
    assert isinstance(field, Const)
    assert field.const == "test_value"
    assert field.default == "default_value"

def test_const_from_json_schema_no_default():
    data = {
        "const": "test_value"
    }
    definitions = SchemaDefinitions()
    
    field = const_from_json_schema(data, definitions)
    
    assert isinstance(field, Const)
    assert field.const == "test_value"
    assert not hasattr(field, 'default') or field.default == NO_DEFAULT
