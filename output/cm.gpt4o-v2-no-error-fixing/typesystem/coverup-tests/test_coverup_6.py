# file: typesystem/json_schema.py:174-196
# asked: {"lines": [174, 179, 180, 181, 183, 185, 186, 188, 189, 191, 192, 193, 194, 196], "branches": [[180, 181], [180, 183], [185, 186], [185, 188], [188, 189], [188, 191], [192, 193], [192, 196]]}
# gained: {"lines": [174, 179, 180, 181, 183, 185, 186, 188, 189, 191, 192, 193, 194, 196], "branches": [[180, 181], [180, 183], [185, 186], [185, 188], [188, 189], [188, 191], [192, 193], [192, 196]]}

import pytest
from typesystem.json_schema import get_valid_types

def test_get_valid_types_with_empty_dict():
    data = {}
    expected_types = {'null', 'boolean', 'object', 'array', 'number', 'string'}
    expected_allow_null = True
    type_strings, allow_null = get_valid_types(data)
    assert type_strings == expected_types - {'null'}
    assert allow_null == expected_allow_null

def test_get_valid_types_with_string_type():
    data = {'type': 'string'}
    expected_types = {'string'}
    expected_allow_null = False
    type_strings, allow_null = get_valid_types(data)
    assert type_strings == expected_types
    assert allow_null == expected_allow_null

def test_get_valid_types_with_list_type():
    data = {'type': ['string', 'number']}
    expected_types = {'string', 'number'}
    expected_allow_null = False
    type_strings, allow_null = get_valid_types(data)
    assert type_strings == expected_types
    assert allow_null == expected_allow_null

def test_get_valid_types_with_null_in_type():
    data = {'type': ['null', 'string']}
    expected_types = {'string'}
    expected_allow_null = True
    type_strings, allow_null = get_valid_types(data)
    assert type_strings == expected_types
    assert allow_null == expected_allow_null

def test_get_valid_types_with_number_and_integer():
    data = {'type': ['number', 'integer']}
    expected_types = {'number'}
    expected_allow_null = False
    type_strings, allow_null = get_valid_types(data)
    assert type_strings == expected_types
    assert allow_null == expected_allow_null
