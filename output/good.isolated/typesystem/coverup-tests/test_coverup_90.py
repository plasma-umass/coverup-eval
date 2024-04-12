# file typesystem/json_schema.py:340-343
# lines [341, 342, 343]
# branches []

import pytest
from typesystem.fields import Choice, NO_DEFAULT
from typesystem.schemas import SchemaDefinitions

# Assuming the typesystem.json_schema module and enum_from_json_schema function exist
from typesystem.json_schema import enum_from_json_schema

def test_enum_from_json_schema_with_default():
    # Setup
    data = {
        "enum": ["a", "b", "c"],
        "default": "b"
    }
    definitions = SchemaDefinitions()

    # Exercise
    result = enum_from_json_schema(data, definitions)

    # Verify
    assert isinstance(result, Choice)
    assert result.choices == [("a", "a"), ("b", "b"), ("c", "c")]
    assert result.default == "b"

def test_enum_from_json_schema_without_default():
    # Setup
    data = {
        "enum": ["x", "y", "z"]
    }
    definitions = SchemaDefinitions()

    # Exercise
    result = enum_from_json_schema(data, definitions)

    # Verify
    assert isinstance(result, Choice)
    assert result.choices == [("x", "x"), ("y", "y"), ("z", "z")]
    assert getattr(result, 'default', NO_DEFAULT) == NO_DEFAULT

# No cleanup is necessary as the test does not modify any external state
