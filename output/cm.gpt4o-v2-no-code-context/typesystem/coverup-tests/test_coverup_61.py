# file: typesystem/json_schema.py:174-196
# asked: {"lines": [183, 186, 189, 193, 194], "branches": [[180, 183], [185, 186], [188, 189], [192, 193]]}
# gained: {"lines": [183, 186, 189, 193, 194], "branches": [[180, 183], [185, 186], [188, 189], [192, 193]]}

import pytest
from typesystem.json_schema import get_valid_types

def test_get_valid_types_with_empty_type():
    data = {"type": []}
    type_strings, allow_null = get_valid_types(data)
    assert type_strings == {"boolean", "object", "array", "number", "string"}
    assert allow_null is True

def test_get_valid_types_with_number_and_integer():
    data = {"type": ["number", "integer"]}
    type_strings, allow_null = get_valid_types(data)
    assert type_strings == {"number"}
    assert allow_null is False

def test_get_valid_types_with_null():
    data = {"type": ["null", "string"]}
    type_strings, allow_null = get_valid_types(data)
    assert type_strings == {"string"}
    assert allow_null is True

def test_get_valid_types_with_string_type():
    data = {"type": "string"}
    type_strings, allow_null = get_valid_types(data)
    assert type_strings == {"string"}
    assert allow_null is False

def test_get_valid_types_with_no_type():
    data = {}
    type_strings, allow_null = get_valid_types(data)
    assert type_strings == {"boolean", "object", "array", "number", "string"}
    assert allow_null is True
