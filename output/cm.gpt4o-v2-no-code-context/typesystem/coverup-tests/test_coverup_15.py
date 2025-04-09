# file: typesystem/json_schema.py:199-331
# asked: {"lines": [199, 206, 207, 208, 209, 210, 211, 212, 213, 214, 216, 218, 219, 220, 221, 222, 223, 224, 225, 226, 228, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 241, 243, 244, 245, 247, 248, 249, 250, 251, 252, 253, 256, 258, 259, 260, 261, 262, 264, 265, 268, 269, 270, 271, 272, 273, 274, 275, 277, 279, 280, 281, 282, 284, 285, 286, 289, 290, 291, 292, 295, 296, 297, 300, 301, 302, 303, 304, 306, 307, 310, 311, 312, 314, 315, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 329, 331], "branches": [[206, 207], [206, 218], [218, 219], [218, 230], [230, 231], [230, 243], [243, 244], [243, 247], [247, 248], [247, 279], [249, 250], [249, 251], [251, 252], [251, 256], [259, 260], [259, 261], [261, 262], [261, 264], [279, 280], [279, 331], [281, 282], [281, 284], [290, 291], [290, 295], [301, 302], [301, 303], [303, 304], [303, 306], [311, 312], [311, 314]]}
# gained: {"lines": [199, 206, 207, 208, 209, 210, 211, 212, 213, 214, 216, 218, 219, 220, 221, 222, 223, 224, 225, 226, 228, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 241, 243, 244, 245, 247, 248, 249, 251, 256, 258, 259, 261, 262, 268, 269, 270, 271, 272, 273, 274, 275, 277, 279, 280, 281, 284, 285, 286, 289, 290, 295, 296, 297, 300, 301, 303, 304, 310, 311, 314, 315, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 329, 331], "branches": [[206, 207], [206, 218], [218, 219], [218, 230], [230, 231], [230, 243], [243, 244], [243, 247], [247, 248], [247, 279], [249, 251], [251, 256], [259, 261], [261, 262], [279, 280], [279, 331], [281, 284], [290, 295], [301, 303], [303, 304], [311, 314]]}

import pytest
from typesystem.json_schema import from_json_schema_type, SchemaDefinitions, Field, Float, Integer, String, Boolean, Array, Object, NO_DEFAULT

def test_from_json_schema_type_number():
    data = {
        "minimum": 0,
        "maximum": 10,
        "exclusiveMinimum": 1,
        "exclusiveMaximum": 9,
        "multipleOf": 2,
        "default": 5
    }
    result = from_json_schema_type(data, "number", allow_null=True, definitions=SchemaDefinitions())
    assert isinstance(result, Float)
    assert result.minimum == 0
    assert result.maximum == 10
    assert result.exclusive_minimum == 1
    assert result.exclusive_maximum == 9
    assert result.multiple_of == 2
    assert result.default == 5
    assert result.allow_null is True

def test_from_json_schema_type_integer():
    data = {
        "minimum": 0,
        "maximum": 10,
        "exclusiveMinimum": 1,
        "exclusiveMaximum": 9,
        "multipleOf": 2,
        "default": 5
    }
    result = from_json_schema_type(data, "integer", allow_null=True, definitions=SchemaDefinitions())
    assert isinstance(result, Integer)
    assert result.minimum == 0
    assert result.maximum == 10
    assert result.exclusive_minimum == 1
    assert result.exclusive_maximum == 9
    assert result.multiple_of == 2
    assert result.default == 5
    assert result.allow_null is True

def test_from_json_schema_type_string():
    data = {
        "minLength": 2,
        "maxLength": 10,
        "format": "email",
        "pattern": "^[a-z]+$",
        "default": "test"
    }
    result = from_json_schema_type(data, "string", allow_null=True, definitions=SchemaDefinitions())
    assert isinstance(result, String)
    assert result.min_length == 2
    assert result.max_length == 10
    assert result.format == "email"
    assert result.pattern == "^[a-z]+$"
    assert result.default == "test"
    assert result.allow_null is True
    assert result.allow_blank is False

def test_from_json_schema_type_boolean():
    data = {
        "default": True
    }
    result = from_json_schema_type(data, "boolean", allow_null=True, definitions=SchemaDefinitions())
    assert isinstance(result, Boolean)
    assert result.default is True
    assert result.allow_null is True

def test_from_json_schema_type_array():
    data = {
        "items": {"type": "string"},
        "additionalItems": False,
        "minItems": 1,
        "maxItems": 5,
        "uniqueItems": True,
        "default": ["test"]
    }
    result = from_json_schema_type(data, "array", allow_null=True, definitions=SchemaDefinitions())
    assert isinstance(result, Array)
    assert isinstance(result.items, String)
    assert result.additional_items is False
    assert result.min_items == 1
    assert result.max_items == 5
    assert result.unique_items is True
    assert result.default == ["test"]
    assert result.allow_null is True

def test_from_json_schema_type_object():
    data = {
        "properties": {
            "name": {"type": "string"}
        },
        "patternProperties": {
            "^S_": {"type": "string"}
        },
        "additionalProperties": False,
        "propertyNames": {"type": "string"},
        "minProperties": 1,
        "maxProperties": 5,
        "required": ["name"],
        "default": {"name": "test"}
    }
    result = from_json_schema_type(data, "object", allow_null=True, definitions=SchemaDefinitions())
    assert isinstance(result, Object)
    assert isinstance(result.properties["name"], String)
    assert isinstance(result.pattern_properties["^S_"], String)
    assert result.additional_properties is False
    assert isinstance(result.property_names, String)
    assert result.min_properties == 1
    assert result.max_properties == 5
    assert result.required == ["name"]
    assert result.default == {"name": "test"}
    assert result.allow_null is True

def test_from_json_schema_type_invalid():
    data = {}
    with pytest.raises(AssertionError, match="Invalid argument type_string='invalid'"):
        from_json_schema_type(data, "invalid", allow_null=True, definitions=SchemaDefinitions())
