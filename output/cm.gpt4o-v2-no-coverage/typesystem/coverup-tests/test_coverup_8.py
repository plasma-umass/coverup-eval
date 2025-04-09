# file: typesystem/json_schema.py:199-331
# asked: {"lines": [199, 206, 207, 208, 209, 210, 211, 212, 213, 214, 216, 218, 219, 220, 221, 222, 223, 224, 225, 226, 228, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 241, 243, 244, 245, 247, 248, 249, 250, 251, 252, 253, 256, 258, 259, 260, 261, 262, 264, 265, 268, 269, 270, 271, 272, 273, 274, 275, 277, 279, 280, 281, 282, 284, 285, 286, 289, 290, 291, 292, 295, 296, 297, 300, 301, 302, 303, 304, 306, 307, 310, 311, 312, 314, 315, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 329, 331], "branches": [[206, 207], [206, 218], [218, 219], [218, 230], [230, 231], [230, 243], [243, 244], [243, 247], [247, 248], [247, 279], [249, 250], [249, 251], [251, 252], [251, 256], [259, 260], [259, 261], [261, 262], [261, 264], [279, 280], [279, 331], [281, 282], [281, 284], [290, 291], [290, 295], [301, 302], [301, 303], [303, 304], [303, 306], [311, 312], [311, 314]]}
# gained: {"lines": [199, 206, 207, 208, 209, 210, 211, 212, 213, 214, 216, 218, 219, 220, 221, 222, 223, 224, 225, 226, 228, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 241, 243, 244, 245, 247, 248, 249, 251, 256, 258, 259, 260, 268, 269, 270, 271, 272, 273, 274, 275, 277, 279, 280, 281, 284, 285, 286, 289, 290, 291, 292, 300, 301, 302, 310, 311, 312, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 329, 331], "branches": [[206, 207], [206, 218], [218, 219], [218, 230], [230, 231], [230, 243], [243, 244], [243, 247], [247, 248], [247, 279], [249, 251], [251, 256], [259, 260], [279, 280], [279, 331], [281, 284], [290, 291], [301, 302], [311, 312]]}

import pytest
from typesystem.fields import NO_DEFAULT, Array, Boolean, Float, Integer, Object, String
from typesystem.schemas import SchemaDefinitions
from typesystem.json_schema import from_json_schema_type

@pytest.mark.parametrize("data, type_string, allow_null, expected_type", [
    ({"minimum": 0, "maximum": 10}, "number", True, Float),
    ({"minimum": 0, "maximum": 10}, "integer", False, Integer),
    ({"minLength": 5, "maxLength": 10}, "string", True, String),
    ({}, "boolean", False, Boolean),
    ({"items": {"type": "string"}}, "array", True, Array),
    ({"properties": {"name": {"type": "string"}}}, "object", False, Object),
])
def test_from_json_schema_type(data, type_string, allow_null, expected_type):
    definitions = SchemaDefinitions()
    field = from_json_schema_type(data, type_string, allow_null, definitions)
    assert isinstance(field, expected_type)
    assert field.allow_null == allow_null

def test_from_json_schema_type_invalid_type():
    definitions = SchemaDefinitions()
    with pytest.raises(AssertionError, match="Invalid argument type_string='invalid'"):
        from_json_schema_type({}, "invalid", False, definitions)
