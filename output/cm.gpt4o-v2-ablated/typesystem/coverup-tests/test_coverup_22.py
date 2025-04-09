# file: typesystem/json_schema.py:199-331
# asked: {"lines": [206, 207, 208, 209, 210, 211, 212, 213, 214, 216, 218, 219, 220, 221, 222, 223, 224, 225, 226, 228, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 241, 243, 244, 245, 247, 248, 249, 250, 251, 252, 253, 256, 258, 259, 260, 261, 262, 264, 265, 268, 269, 270, 271, 272, 273, 274, 275, 277, 279, 280, 281, 282, 284, 285, 286, 289, 290, 291, 292, 295, 296, 297, 300, 301, 302, 303, 304, 306, 307, 310, 311, 312, 314, 315, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 329, 331], "branches": [[206, 207], [206, 218], [218, 219], [218, 230], [230, 231], [230, 243], [243, 244], [243, 247], [247, 248], [247, 279], [249, 250], [249, 251], [251, 252], [251, 256], [259, 260], [259, 261], [261, 262], [261, 264], [279, 280], [279, 331], [281, 282], [281, 284], [290, 291], [290, 295], [301, 302], [301, 303], [303, 304], [303, 306], [311, 312], [311, 314]]}
# gained: {"lines": [206, 207, 208, 209, 210, 211, 212, 213, 214, 216, 218, 219, 220, 221, 222, 223, 224, 225, 226, 228, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 241, 243, 244, 245, 247, 248, 249, 251, 256, 258, 259, 260, 268, 269, 270, 271, 272, 273, 274, 275, 277, 279, 280, 281, 284, 285, 286, 289, 290, 295, 296, 297, 300, 301, 303, 304, 310, 311, 314, 315, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 329, 331], "branches": [[206, 207], [206, 218], [218, 219], [218, 230], [230, 231], [230, 243], [243, 244], [243, 247], [247, 248], [247, 279], [249, 251], [251, 256], [259, 260], [279, 280], [279, 331], [281, 284], [290, 295], [301, 303], [303, 304], [311, 314]]}

import pytest
from typesystem.json_schema import from_json_schema_type, SchemaDefinitions
from typesystem.fields import Float, Integer, String, Boolean, Array, Object, Field, NO_DEFAULT

def test_from_json_schema_type_number():
    data = {
        "minimum": 1,
        "maximum": 10,
        "exclusiveMinimum": 2,
        "exclusiveMaximum": 9,
        "multipleOf": 2,
        "default": 5
    }
    field = from_json_schema_type(data, "number", allow_null=True, definitions=SchemaDefinitions())
    assert isinstance(field, Float)
    assert field.minimum == 1
    assert field.maximum == 10
    assert field.exclusive_minimum == 2
    assert field.exclusive_maximum == 9
    assert field.multiple_of == 2
    assert field.default == 5
    assert field.allow_null is True

def test_from_json_schema_type_integer():
    data = {
        "minimum": 1,
        "maximum": 10,
        "exclusiveMinimum": 2,
        "exclusiveMaximum": 9,
        "multipleOf": 2,
        "default": 5
    }
    field = from_json_schema_type(data, "integer", allow_null=False, definitions=SchemaDefinitions())
    assert isinstance(field, Integer)
    assert field.minimum == 1
    assert field.maximum == 10
    assert field.exclusive_minimum == 2
    assert field.exclusive_maximum == 9
    assert field.multiple_of == 2
    assert field.default == 5
    assert field.allow_null is False

def test_from_json_schema_type_string():
    data = {
        "minLength": 2,
        "maxLength": 10,
        "format": "email",
        "pattern": "^[a-z]+$",
        "default": "test"
    }
    field = from_json_schema_type(data, "string", allow_null=True, definitions=SchemaDefinitions())
    assert isinstance(field, String)
    assert field.min_length == 2
    assert field.max_length == 10
    assert field.format == "email"
    assert field.pattern == "^[a-z]+$"
    assert field.default == "test"
    assert field.allow_null is True
    assert field.allow_blank is False

def test_from_json_schema_type_boolean():
    data = {
        "default": True
    }
    field = from_json_schema_type(data, "boolean", allow_null=False, definitions=SchemaDefinitions())
    assert isinstance(field, Boolean)
    assert field.default is True
    assert field.allow_null is False

def test_from_json_schema_type_array():
    data = {
        "items": {"type": "string"},
        "minItems": 1,
        "maxItems": 5,
        "uniqueItems": True,
        "default": ["a", "b"]
    }
    field = from_json_schema_type(data, "array", allow_null=True, definitions=SchemaDefinitions())
    assert isinstance(field, Array)
    assert field.min_items == 1
    assert field.max_items == 5
    assert field.unique_items is True
    assert field.default == ["a", "b"]
    assert field.allow_null is True
    assert isinstance(field.items, String)

def test_from_json_schema_type_object():
    data = {
        "properties": {
            "name": {"type": "string"},
            "age": {"type": "integer"}
        },
        "patternProperties": {
            "^S_": {"type": "string"}
        },
        "additionalProperties": False,
        "propertyNames": {"type": "string"},
        "minProperties": 1,
        "maxProperties": 3,
        "required": ["name"],
        "default": {"name": "John", "age": 30}
    }
    field = from_json_schema_type(data, "object", allow_null=False, definitions=SchemaDefinitions())
    assert isinstance(field, Object)
    assert field.min_properties == 1
    assert field.max_properties == 3
    assert field.required == ["name"]
    assert field.default == {"name": "John", "age": 30}
    assert field.allow_null is False
    assert isinstance(field.properties["name"], String)
    assert isinstance(field.properties["age"], Integer)
    assert isinstance(field.pattern_properties["^S_"], String)
    assert field.additional_properties is False
    assert isinstance(field.property_names, String)

def test_from_json_schema_type_invalid():
    with pytest.raises(AssertionError, match="Invalid argument type_string='invalid'"):
        from_json_schema_type({}, "invalid", allow_null=False, definitions=SchemaDefinitions())
