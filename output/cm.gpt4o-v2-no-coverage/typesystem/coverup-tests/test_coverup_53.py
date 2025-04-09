# file: typesystem/json_schema.py:346-349
# asked: {"lines": [346, 347, 348, 349], "branches": []}
# gained: {"lines": [346, 347, 348, 349], "branches": []}

import pytest
from typesystem.fields import NO_DEFAULT, Const
from typesystem.schemas import SchemaDefinitions
from typesystem.json_schema import const_from_json_schema

def test_const_from_json_schema_with_default():
    data = {"const": "value", "default": "default_value"}
    definitions = SchemaDefinitions()
    field = const_from_json_schema(data, definitions)
    
    assert isinstance(field, Const)
    assert field.const == "value"
    assert field.default == "default_value"

def test_const_from_json_schema_without_default():
    data = {"const": "value"}
    definitions = SchemaDefinitions()
    field = const_from_json_schema(data, definitions)
    
    assert isinstance(field, Const)
    assert field.const == "value"
    assert not hasattr(field, 'default') or field.default is NO_DEFAULT
