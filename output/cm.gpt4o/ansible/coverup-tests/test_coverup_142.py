# file lib/ansible/module_utils/common/dict_transformations.py:55-76
# lines [55, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 73, 74, 76]
# branches ['63->64', '63->65', '66->67', '66->69', '67->68', '67->74', '69->70', '69->73', '70->71', '70->74']

import pytest
from ansible.module_utils.common.dict_transformations import snake_dict_to_camel_dict

def _snake_to_camel(snake_str, capitalize_first=False):
    components = snake_str.split('_')
    if capitalize_first:
        components[0] = components[0].capitalize()
    return components[0] + ''.join(x.capitalize() or '_' for x in components[1:])

def test_snake_dict_to_camel_dict_dict():
    snake_dict = {
        'first_key': 'value1',
        'second_key': {
            'nested_key': 'value2'
        },
        'third_key': [
            {'list_key': 'value3'}
        ]
    }
    expected_camel_dict = {
        'firstKey': 'value1',
        'secondKey': {
            'nestedKey': 'value2'
        },
        'thirdKey': [
            {'listKey': 'value3'}
        ]
    }
    result = snake_dict_to_camel_dict(snake_dict)
    assert result == expected_camel_dict

def test_snake_dict_to_camel_dict_list():
    snake_list = [
        {'first_key': 'value1'},
        {'second_key': 'value2'}
    ]
    expected_camel_list = [
        {'firstKey': 'value1'},
        {'secondKey': 'value2'}
    ]
    result = snake_dict_to_camel_dict(snake_list)
    assert result == expected_camel_list

def test_snake_dict_to_camel_dict_none():
    result = snake_dict_to_camel_dict(None)
    assert result is None

def test_snake_dict_to_camel_dict_capitalize_first():
    snake_dict = {
        'first_key': 'value1',
        'second_key': {
            'nested_key': 'value2'
        }
    }
    expected_camel_dict = {
        'FirstKey': 'value1',
        'SecondKey': {
            'NestedKey': 'value2'
        }
    }
    result = snake_dict_to_camel_dict(snake_dict, capitalize_first=True)
    assert result == expected_camel_dict
