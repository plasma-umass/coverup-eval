# file: typesystem/json_schema.py:174-196
# asked: {"lines": [183, 186, 189, 193, 194], "branches": [[180, 183], [185, 186], [188, 189], [192, 193]]}
# gained: {"lines": [183, 186, 189, 193, 194], "branches": [[180, 183], [185, 186], [188, 189], [192, 193]]}

import pytest
from typesystem.json_schema import get_valid_types

def test_get_valid_types_with_empty_dict():
    data = {}
    expected_types = {"null", "boolean", "object", "array", "number", "string"}
    expected_allow_null = True
    result = get_valid_types(data)
    assert result == (expected_types - {"null"}, expected_allow_null)

def test_get_valid_types_with_type_string():
    data = {"type": "string"}
    expected_types = {"string"}
    expected_allow_null = False
    result = get_valid_types(data)
    assert result == (expected_types, expected_allow_null)

def test_get_valid_types_with_type_list():
    data = {"type": ["string", "number"]}
    expected_types = {"string", "number"}
    expected_allow_null = False
    result = get_valid_types(data)
    assert result == (expected_types, expected_allow_null)

def test_get_valid_types_with_type_list_including_null():
    data = {"type": ["string", "null"]}
    expected_types = {"string"}
    expected_allow_null = True
    result = get_valid_types(data)
    assert result == (expected_types, expected_allow_null)

def test_get_valid_types_with_type_list_including_integer():
    data = {"type": ["integer", "number"]}
    expected_types = {"number"}
    expected_allow_null = False
    result = get_valid_types(data)
    assert result == (expected_types, expected_allow_null)

def test_get_valid_types_with_type_list_including_null_and_integer():
    data = {"type": ["integer", "number", "null"]}
    expected_types = {"number"}
    expected_allow_null = True
    result = get_valid_types(data)
    assert result == (expected_types, expected_allow_null)
