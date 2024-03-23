# file typesystem/json_schema.py:346-349
# lines [346, 347, 348, 349]
# branches []

import pytest
from typesystem.fields import Const
from typesystem.schemas import SchemaDefinitions

# Assuming the existence of the `const_from_json_schema` function in the module `typesystem.json_schema`
from typesystem.json_schema import const_from_json_schema

def test_const_from_json_schema_with_default():
    data = {"const": 42, "default": 42}
    definitions = SchemaDefinitions()
    field = const_from_json_schema(data, definitions)
    assert isinstance(field, Const)
    assert field.default == 42
    assert field.const == 42

def test_const_from_json_schema_without_default():
    data = {"const": "test"}
    definitions = SchemaDefinitions()
    field = const_from_json_schema(data, definitions)
    assert isinstance(field, Const)
    assert not hasattr(field, 'default')  # Assuming that 'default' attribute is not set when not provided
    assert field.const == "test"
