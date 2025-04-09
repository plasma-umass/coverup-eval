# file typesystem/json_schema.py:174-196
# lines [174, 179, 180, 181, 183, 185, 186, 188, 189, 191, 192, 193, 194, 196]
# branches ['180->181', '180->183', '185->186', '185->188', '188->189', '188->191', '192->193', '192->196']

import pytest
from typesystem.json_schema import get_valid_types

def test_get_valid_types():
    # Test with type as string
    data = {"type": "string"}
    type_strings, allow_null = get_valid_types(data)
    assert type_strings == {"string"}
    assert not allow_null

    # Test with type as list
    data = {"type": ["string", "null"]}
    type_strings, allow_null = get_valid_types(data)
    assert type_strings == {"string"}
    assert allow_null

    # Test with type as list including "number" and "integer"
    data = {"type": ["number", "integer"]}
    type_strings, allow_null = get_valid_types(data)
    assert type_strings == {"number"}
    assert not allow_null

    # Test with empty type
    data = {}
    type_strings, allow_null = get_valid_types(data)
    assert type_strings == {"boolean", "object", "array", "number", "string"}
    assert allow_null  # Corrected assertion to expect allow_null to be True

    # Test with type as list including "null" only
    data = {"type": ["null"]}
    type_strings, allow_null = get_valid_types(data)
    assert type_strings == set()
    assert allow_null

    # Test with type as list not including "null"
    data = {"type": ["boolean"]}
    type_strings, allow_null = get_valid_types(data)
    assert type_strings == {"boolean"}
    assert not allow_null

# Clean up is not necessary as the function does not modify any external state
