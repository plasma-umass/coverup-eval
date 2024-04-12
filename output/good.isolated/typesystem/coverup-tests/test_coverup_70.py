# file typesystem/json_schema.py:358-361
# lines [358, 359, 360, 361]
# branches []

import pytest
from typesystem.fields import Field, Union
from typesystem.schemas import SchemaDefinitions
from typesystem.json_schema import from_json_schema

@pytest.fixture
def schema_definitions():
    return SchemaDefinitions()

@pytest.fixture
def json_schema_data():
    return {
        "anyOf": [
            {"type": "string"},
            {"type": "number"}
        ]
    }

def test_any_of_from_json_schema(json_schema_data, schema_definitions):
    field = from_json_schema({"anyOf": json_schema_data["anyOf"]}, definitions=schema_definitions)
    assert isinstance(field, Union)
    assert len(field.any_of) == 2
    assert isinstance(field.any_of[0], Field)
    assert isinstance(field.any_of[1], Field)

def test_any_of_from_json_schema_with_default(json_schema_data, schema_definitions):
    json_schema_data_with_default = json_schema_data.copy()
    json_schema_data_with_default["default"] = "default_value"
    field = from_json_schema({"anyOf": json_schema_data_with_default["anyOf"], "default": "default_value"}, definitions=schema_definitions)
    assert field.default == "default_value"
