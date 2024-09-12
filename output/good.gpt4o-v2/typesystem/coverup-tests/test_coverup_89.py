# file: typesystem/json_schema.py:199-331
# asked: {"lines": [219, 220, 221, 222, 223, 224, 225, 226, 228, 251, 252, 253, 256, 261, 262, 264, 265, 284, 285, 286, 295, 296, 297, 303, 304, 306, 307, 314, 315, 331], "branches": [[218, 219], [249, 251], [251, 252], [251, 256], [259, 261], [261, 262], [261, 264], [279, 331], [281, 284], [290, 295], [301, 303], [303, 304], [303, 306], [311, 314]]}
# gained: {"lines": [219, 220, 221, 222, 223, 224, 225, 226, 228, 251, 252, 253, 256, 261, 262, 264, 265, 284, 285, 286, 295, 296, 297, 303, 306, 307, 314, 315, 331], "branches": [[218, 219], [249, 251], [251, 252], [251, 256], [259, 261], [261, 262], [261, 264], [279, 331], [281, 284], [290, 295], [301, 303], [303, 306], [311, 314]]}

import pytest
from typesystem.json_schema import from_json_schema_type
from typesystem.schemas import SchemaDefinitions
from typesystem.fields import Integer, Array, Object, String, Boolean, Float, NO_DEFAULT

def test_from_json_schema_type_integer():
    data = {
        "minimum": 1,
        "maximum": 10,
        "exclusiveMinimum": 2,
        "exclusiveMaximum": 9,
        "multipleOf": 2,
        "default": 5
    }
    field = from_json_schema_type(data, "integer", allow_null=True, definitions=SchemaDefinitions())
    assert isinstance(field, Integer)
    assert field.minimum == 1
    assert field.maximum == 10
    assert field.exclusive_minimum == 2
    assert field.exclusive_maximum == 9
    assert field.multiple_of == 2
    assert field.default == 5
    assert field.allow_null is True

def test_from_json_schema_type_array_items_list(mocker):
    mocker.patch('typesystem.json_schema.from_json_schema', side_effect=[Integer()])
    data = {
        "items": [{"type": "integer"}],
        "additionalItems": False,
        "minItems": 1,
        "maxItems": 5,
        "uniqueItems": True,
        "default": [1, 2, 3]
    }
    field = from_json_schema_type(data, "array", allow_null=False, definitions=SchemaDefinitions())
    assert isinstance(field, Array)
    assert isinstance(field.items[0], Integer)
    assert field.additional_items is False
    assert field.min_items == 1
    assert field.max_items == 5
    assert field.unique_items is True
    assert field.default == [1, 2, 3]
    assert field.allow_null is False

def test_from_json_schema_type_array_items_single(mocker):
    mocker.patch('typesystem.json_schema.from_json_schema', side_effect=[Integer(), String()])
    data = {
        "items": {"type": "integer"},
        "additionalItems": {"type": "string"},
        "minItems": 1,
        "maxItems": 5,
        "uniqueItems": True,
        "default": [1, 2, 3]
    }
    field = from_json_schema_type(data, "array", allow_null=False, definitions=SchemaDefinitions())
    assert isinstance(field, Array)
    assert isinstance(field.items, Integer)
    assert isinstance(field.additional_items, String)
    assert field.min_items == 1
    assert field.max_items == 5
    assert field.unique_items is True
    assert field.default == [1, 2, 3]
    assert field.allow_null is False

def test_from_json_schema_type_object_properties(mocker):
    mocker.patch('typesystem.json_schema.from_json_schema', side_effect=[Integer(), String(), Boolean(), String()])
    data = {
        "properties": {
            "age": {"type": "integer"}
        },
        "patternProperties": {
            "^S": {"type": "string"}
        },
        "additionalProperties": {"type": "boolean"},
        "propertyNames": {"type": "string"},
        "minProperties": 1,
        "maxProperties": 5,
        "required": ["age"],
        "default": {"age": 30}
    }
    field = from_json_schema_type(data, "object", allow_null=True, definitions=SchemaDefinitions())
    assert isinstance(field, Object)
    assert isinstance(field.properties["age"], Integer)
    assert isinstance(field.pattern_properties["^S"], String)
    assert isinstance(field.additional_properties, Boolean)
    assert isinstance(field.property_names, String)
    assert field.min_properties == 1
    assert field.max_properties == 5
    assert field.required == ["age"]
    assert field.default == {"age": 30}
    assert field.allow_null is True

def test_from_json_schema_type_invalid_type():
    data = {}
    with pytest.raises(AssertionError, match="Invalid argument type_string='invalid'"):
        from_json_schema_type(data, "invalid", allow_null=False, definitions=SchemaDefinitions())
