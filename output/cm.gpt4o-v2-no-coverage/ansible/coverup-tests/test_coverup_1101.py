# file: lib/ansible/module_utils/common/dict_transformations.py:16-52
# asked: {"lines": [30, 32, 33, 34, 35, 36, 37, 39, 41, 43, 44, 45, 46, 47, 48, 50, 52], "branches": [[33, 34], [33, 41], [34, 35], [34, 36], [36, 37], [36, 39], [44, 45], [44, 52], [45, 46], [45, 47], [47, 48], [47, 50]]}
# gained: {"lines": [30, 32, 33, 34, 35, 36, 39, 41, 43, 44, 45, 46, 47, 48, 50, 52], "branches": [[33, 34], [33, 41], [34, 35], [34, 36], [36, 39], [44, 45], [44, 52], [45, 46], [45, 47], [47, 48], [47, 50]]}

import pytest
from ansible.module_utils.common.dict_transformations import camel_dict_to_snake_dict

def test_camel_dict_to_snake_dict_basic():
    camel_dict = {
        'CamelCaseKey': 'value',
        'AnotherCamelCase': {
            'NestedCamelCase': 'nested_value'
        }
    }
    expected_snake_dict = {
        'camel_case_key': 'value',
        'another_camel_case': {
            'nested_camel_case': 'nested_value'
        }
    }
    assert camel_dict_to_snake_dict(camel_dict) == expected_snake_dict

def test_camel_dict_to_snake_dict_with_list():
    camel_dict = {
        'CamelCaseKey': 'value',
        'ListCamelCase': [
            {'NestedCamelCase': 'nested_value'},
            'string_value',
            123
        ]
    }
    expected_snake_dict = {
        'camel_case_key': 'value',
        'list_camel_case': [
            {'nested_camel_case': 'nested_value'},
            'string_value',
            123
        ]
    }
    assert camel_dict_to_snake_dict(camel_dict) == expected_snake_dict

def test_camel_dict_to_snake_dict_reversible():
    camel_dict = {
        'HTTPEndpoint': 'value',
        'AnotherHTTPEndpoint': {
            'NestedHTTPEndpoint': 'nested_value'
        }
    }
    expected_snake_dict = {
        'h_t_t_p_endpoint': 'value',
        'another_h_t_t_p_endpoint': {
            'nested_h_t_t_p_endpoint': 'nested_value'
        }
    }
    assert camel_dict_to_snake_dict(camel_dict, reversible=True) == expected_snake_dict

def test_camel_dict_to_snake_dict_ignore_list():
    camel_dict = {
        'CamelCaseKey': 'value',
        'Tags': {
            'CaseSensitiveKey': 'sensitive_value'
        }
    }
    expected_snake_dict = {
        'camel_case_key': 'value',
        'tags': {
            'CaseSensitiveKey': 'sensitive_value'
        }
    }
    assert camel_dict_to_snake_dict(camel_dict, ignore_list=['Tags']) == expected_snake_dict
