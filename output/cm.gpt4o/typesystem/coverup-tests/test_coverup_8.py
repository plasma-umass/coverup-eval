# file typesystem/json_schema.py:174-196
# lines [174, 179, 180, 181, 183, 185, 186, 188, 189, 191, 192, 193, 194, 196]
# branches ['180->181', '180->183', '185->186', '185->188', '188->189', '188->191', '192->193', '192->196']

import pytest
from typesystem.json_schema import get_valid_types

def test_get_valid_types():
    # Test with empty dictionary
    data = {}
    type_strings, allow_null = get_valid_types(data)
    assert type_strings == {"boolean", "object", "array", "number", "string"}
    assert allow_null is True

    # Test with type as a single string
    data = {"type": "string"}
    type_strings, allow_null = get_valid_types(data)
    assert type_strings == {"string"}
    assert allow_null is False

    # Test with type as a list of strings
    data = {"type": ["string", "number"]}
    type_strings, allow_null = get_valid_types(data)
    assert type_strings == {"string", "number"}
    assert allow_null is False

    # Test with type including "null"
    data = {"type": ["string", "null"]}
    type_strings, allow_null = get_valid_types(data)
    assert type_strings == {"string"}
    assert allow_null is True

    # Test with type including "number" and "integer"
    data = {"type": ["number", "integer"]}
    type_strings, allow_null = get_valid_types(data)
    assert type_strings == {"number"}
    assert allow_null is False

    # Test with type as an empty list
    data = {"type": []}
    type_strings, allow_null = get_valid_types(data)
    assert type_strings == {"boolean", "object", "array", "number", "string"}
    assert allow_null is True

    # Test with type as a list containing only "null"
    data = {"type": ["null"]}
    type_strings, allow_null = get_valid_types(data)
    assert type_strings == set()
    assert allow_null is True
