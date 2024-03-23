# file typesystem/json_schema.py:199-331
# lines [199, 206, 207, 208, 209, 210, 211, 212, 213, 214, 216, 218, 219, 220, 221, 222, 223, 224, 225, 226, 228, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 241, 243, 244, 245, 247, 248, 249, 250, 251, 252, 253, 256, 258, 259, 260, 261, 262, 264, 265, 268, 269, 270, 271, 272, 273, 274, 275, 277, 279, 280, 281, 282, 284, 285, 286, 289, 290, 291, 292, 295, 296, 297, 300, 301, 302, 303, 304, 306, 307, 310, 311, 312, 314, 315, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 329, 331]
# branches ['206->207', '206->218', '218->219', '218->230', '230->231', '230->243', '243->244', '243->247', '247->248', '247->279', '249->250', '249->251', '251->252', '251->256', '259->260', '259->261', '261->262', '261->264', '279->280', '279->331', '281->282', '281->284', '290->291', '290->295', '301->302', '301->303', '303->304', '303->306', '311->312', '311->314']

import pytest
from typesystem.fields import (
    Boolean,
    Float,
    Integer,
    String,
    Array,
    Object,
    Field
)
from typesystem.json_schema import from_json_schema_type, SchemaDefinitions

NO_DEFAULT = object()

@pytest.fixture
def schema_definitions():
    return SchemaDefinitions()

@pytest.mark.parametrize(
    "type_string,expected_type",
    [
        ("number", Float),
        ("integer", Integer),
        ("string", String),
        ("boolean", Boolean),
        ("array", Array),
        ("object", Object),
    ],
)
def test_from_json_schema_type(type_string, expected_type, schema_definitions):
    data = {
        "minimum": 1,
        "maximum": 10,
        "exclusiveMinimum": 1,
        "exclusiveMaximum": 10,
        "multipleOf": 2,
        "minLength": 3,
        "maxLength": 5,
        "format": "email",
        "pattern": ".*",
        "minItems": 1,
        "maxItems": 5,
        "uniqueItems": True,
        "minProperties": 1,
        "maxProperties": 5,
        "required": ["id"],
        "default": "default_value",
        "properties": {"id": {"type": "integer"}},
        "patternProperties": {"^S": {"type": "string"}},
        "additionalProperties": {"type": "number"},
        "propertyNames": {"type": "string"},
        "items": {"type": "string"},
        "additionalItems": {"type": "boolean"},
    }
    field = from_json_schema_type(data, type_string, allow_null=True, definitions=schema_definitions)
    assert isinstance(field, expected_type)
    assert field.allow_null is True
    if type_string == "number":
        assert field.minimum == 1
        assert field.maximum == 10
        assert field.exclusive_minimum == 1
        assert field.exclusive_maximum == 10
        assert field.multiple_of == 2
    elif type_string == "integer":
        assert field.minimum == 1
        assert field.maximum == 10
        assert field.exclusive_minimum == 1
        assert field.exclusive_maximum == 10
        assert field.multiple_of == 2
    elif type_string == "string":
        assert field.min_length == 3
        assert field.max_length == 5
        assert field.format == "email"
        assert field.pattern == ".*"
    elif type_string == "boolean":
        pass
    elif type_string == "array":
        assert field.min_items == 1
        assert field.max_items == 5
        assert field.unique_items is True
        assert isinstance(field.items, Field)
        assert isinstance(field.additional_items, Field)
    elif type_string == "object":
        assert field.min_properties == 1
        assert field.max_properties == 5
        assert field.required == ["id"]
        assert isinstance(field.properties, dict)
        assert isinstance(field.pattern_properties, dict)
        assert isinstance(field.additional_properties, Field)
        assert isinstance(field.property_names, Field)

def test_from_json_schema_type_invalid_type(schema_definitions):
    with pytest.raises(AssertionError) as exc_info:
        from_json_schema_type({}, "invalid_type", allow_null=True, definitions=schema_definitions)
    assert "Invalid argument type_string='invalid_type'" in str(exc_info.value)
