# file typesystem/json_schema.py:199-331
# lines [252, 253, 262, 304]
# branches ['251->252', '261->262', '303->304']

import pytest
from typesystem.fields import (
    Array, Boolean, Float, Integer, Object, String
)
from typesystem.json_schema import from_json_schema_type, SchemaDefinitions

@pytest.fixture
def schema_definitions():
    return SchemaDefinitions()

@pytest.fixture
def json_schema_data():
    return {
        "type": "object",
        "properties": {
            "name": {"type": "string"},
            "age": {"type": "integer"},
            "is_active": {"type": "boolean"},
        },
        "additionalProperties": False,
        "items": [{"type": "string"}, {"type": "integer"}],
        "additionalItems": False,
    }

def test_from_json_schema_type_array_items_and_additional_items(json_schema_data, schema_definitions):
    # Test the 'array' type with 'items' as a list and 'additionalItems' as a boolean
    array_field = from_json_schema_type(
        data=json_schema_data,
        type_string="array",
        allow_null=True,
        definitions=schema_definitions
    )
    assert isinstance(array_field, Array)
    assert isinstance(array_field.items[0], String)
    assert isinstance(array_field.items[1], Integer)
    assert array_field.additional_items is False

def test_from_json_schema_type_object_additional_properties(json_schema_data, schema_definitions):
    # Test the 'object' type with 'additionalProperties' as a boolean
    object_field = from_json_schema_type(
        data=json_schema_data,
        type_string="object",
        allow_null=True,
        definitions=schema_definitions
    )
    assert isinstance(object_field, Object)
    assert object_field.additional_properties is False
