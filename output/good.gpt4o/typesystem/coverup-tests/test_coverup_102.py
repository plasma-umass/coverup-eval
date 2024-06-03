# file typesystem/json_schema.py:199-331
# lines [252, 253, 261, 262, 264, 265, 295, 296, 297, 303, 304, 306, 307, 314, 315]
# branches ['251->252', '259->261', '261->262', '261->264', '290->295', '301->303', '303->304', '303->306', '311->314']

import pytest
from typesystem.json_schema import from_json_schema_type, SchemaDefinitions, Field, Float, Integer, String, Boolean, Array, Object

def test_from_json_schema_type_array_items_list(mocker):
    data = {
        "type": "array",
        "items": [{"type": "string"}, {"type": "integer"}],
        "additionalItems": False,
        "minItems": 1,
        "maxItems": 5,
        "uniqueItems": True,
        "default": []
    }
    definitions = SchemaDefinitions()
    field = from_json_schema_type(data, "array", allow_null=True, definitions=definitions)
    assert isinstance(field, Array)
    assert isinstance(field.items[0], String)
    assert isinstance(field.items[1], Integer)
    assert field.additional_items == False
    assert field.min_items == 1
    assert field.max_items == 5
    assert field.unique_items == True
    assert field.default == []

def test_from_json_schema_type_array_additional_items_schema(mocker):
    data = {
        "type": "array",
        "items": {"type": "string"},
        "additionalItems": {"type": "integer"},
        "minItems": 1,
        "maxItems": 5,
        "uniqueItems": True,
        "default": []
    }
    definitions = SchemaDefinitions()
    field = from_json_schema_type(data, "array", allow_null=True, definitions=definitions)
    assert isinstance(field, Array)
    assert isinstance(field.items, String)
    assert isinstance(field.additional_items, Integer)
    assert field.min_items == 1
    assert field.max_items == 5
    assert field.unique_items == True
    assert field.default == []

def test_from_json_schema_type_object_pattern_properties(mocker):
    data = {
        "type": "object",
        "properties": {"name": {"type": "string"}},
        "patternProperties": {"^S_": {"type": "string"}},
        "additionalProperties": False,
        "propertyNames": {"type": "string"},
        "minProperties": 1,
        "maxProperties": 5,
        "required": ["name"],
        "default": {}
    }
    definitions = SchemaDefinitions()
    field = from_json_schema_type(data, "object", allow_null=True, definitions=definitions)
    assert isinstance(field, Object)
    assert isinstance(field.properties["name"], String)
    assert isinstance(field.pattern_properties["^S_"], String)
    assert field.additional_properties == False
    assert isinstance(field.property_names, String)
    assert field.min_properties == 1
    assert field.max_properties == 5
    assert field.required == ["name"]
    assert field.default == {}

def test_from_json_schema_type_object_additional_properties_schema(mocker):
    data = {
        "type": "object",
        "properties": {"name": {"type": "string"}},
        "additionalProperties": {"type": "string"},
        "propertyNames": {"type": "string"},
        "minProperties": 1,
        "maxProperties": 5,
        "required": ["name"],
        "default": {}
    }
    definitions = SchemaDefinitions()
    field = from_json_schema_type(data, "object", allow_null=True, definitions=definitions)
    assert isinstance(field, Object)
    assert isinstance(field.properties["name"], String)
    assert isinstance(field.additional_properties, String)
    assert isinstance(field.property_names, String)
    assert field.min_properties == 1
    assert field.max_properties == 5
    assert field.required == ["name"]
    assert field.default == {}
