# file: typesystem/json_schema.py:199-331
# asked: {"lines": [219, 220, 221, 222, 223, 224, 225, 226, 228, 247, 248, 249, 250, 251, 252, 253, 256, 258, 259, 260, 261, 262, 264, 265, 268, 269, 270, 271, 272, 273, 274, 275, 277, 279, 280, 281, 282, 284, 285, 286, 289, 290, 291, 292, 295, 296, 297, 300, 301, 302, 303, 304, 306, 307, 310, 311, 312, 314, 315, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 329, 331], "branches": [[218, 219], [243, 247], [247, 248], [247, 279], [249, 250], [249, 251], [251, 252], [251, 256], [259, 260], [259, 261], [261, 262], [261, 264], [279, 280], [279, 331], [281, 282], [281, 284], [290, 291], [290, 295], [301, 302], [301, 303], [303, 304], [303, 306], [311, 312], [311, 314]]}
# gained: {"lines": [219, 220, 221, 222, 223, 224, 225, 226, 228, 247, 248, 249, 251, 256, 258, 259, 261, 262, 268, 269, 270, 271, 272, 273, 274, 275, 277, 279, 280, 281, 284, 285, 286, 289, 290, 295, 296, 297, 300, 301, 303, 306, 307, 310, 311, 314, 315, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 329, 331], "branches": [[218, 219], [243, 247], [247, 248], [247, 279], [249, 251], [251, 256], [259, 261], [261, 262], [279, 280], [279, 331], [281, 284], [290, 295], [301, 303], [303, 306], [311, 314]]}

import pytest
from typesystem.json_schema import from_json_schema_type
from typesystem.schemas import SchemaDefinitions
from typesystem.fields import Integer, Array, Object, Field, NO_DEFAULT

def test_from_json_schema_type_integer():
    data = {
        "minimum": 1,
        "maximum": 10,
        "exclusiveMinimum": 2,
        "exclusiveMaximum": 9,
        "multipleOf": 2,
        "default": 4
    }
    field = from_json_schema_type(data, "integer", allow_null=True, definitions=SchemaDefinitions())
    assert isinstance(field, Integer)
    assert field.minimum == 1
    assert field.maximum == 10
    assert field.exclusive_minimum == 2
    assert field.exclusive_maximum == 9
    assert field.multiple_of == 2
    assert field.default == 4
    assert field.allow_null is True

def test_from_json_schema_type_array():
    data = {
        "items": {"type": "integer"},
        "additionalItems": False,
        "minItems": 1,
        "maxItems": 5,
        "uniqueItems": True,
        "default": [1, 2, 3]
    }
    definitions = SchemaDefinitions()
    field = from_json_schema_type(data, "array", allow_null=False, definitions=definitions)
    assert isinstance(field, Array)
    assert isinstance(field.items, Integer)
    assert field.additional_items is False
    assert field.min_items == 1
    assert field.max_items == 5
    assert field.unique_items is True
    assert field.default == [1, 2, 3]
    assert field.allow_null is False

def test_from_json_schema_type_object():
    data = {
        "properties": {
            "name": {"type": "string"},
            "age": {"type": "integer"}
        },
        "patternProperties": {
            "^S": {"type": "string"}
        },
        "additionalProperties": {"type": "boolean"},
        "propertyNames": {"type": "string"},
        "minProperties": 1,
        "maxProperties": 3,
        "required": ["name"],
        "default": {"name": "John", "age": 30}
    }
    definitions = SchemaDefinitions()
    field = from_json_schema_type(data, "object", allow_null=True, definitions=definitions)
    assert isinstance(field, Object)
    assert isinstance(field.properties["name"], Field)
    assert isinstance(field.properties["age"], Integer)
    assert isinstance(field.pattern_properties["^S"], Field)
    assert isinstance(field.additional_properties, Field)
    assert isinstance(field.property_names, Field)
    assert field.min_properties == 1
    assert field.max_properties == 3
    assert field.required == ["name"]
    assert field.default == {"name": "John", "age": 30}
    assert field.allow_null is True

def test_from_json_schema_type_invalid():
    data = {}
    with pytest.raises(AssertionError, match="Invalid argument type_string='invalid'"):
        from_json_schema_type(data, "invalid", allow_null=False, definitions=SchemaDefinitions())
