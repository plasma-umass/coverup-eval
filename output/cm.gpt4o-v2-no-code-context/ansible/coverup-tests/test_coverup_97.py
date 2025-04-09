# file: lib/ansible/module_utils/common/dict_transformations.py:55-76
# asked: {"lines": [55, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 73, 74, 76], "branches": [[63, 64], [63, 65], [66, 67], [66, 69], [67, 68], [67, 74], [69, 70], [69, 73], [70, 71], [70, 74]]}
# gained: {"lines": [55, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 73, 74, 76], "branches": [[63, 64], [63, 65], [66, 67], [66, 69], [67, 68], [67, 74], [69, 70], [69, 73], [70, 71], [70, 74]]}

import pytest
from ansible.module_utils.common.dict_transformations import snake_dict_to_camel_dict

def test_snake_dict_to_camel_dict_empty_dict():
    result = snake_dict_to_camel_dict({})
    assert result == {}

def test_snake_dict_to_camel_dict_none():
    result = snake_dict_to_camel_dict(None)
    assert result is None

def test_snake_dict_to_camel_dict_simple_dict():
    snake_dict = {'simple_key': 'value'}
    result = snake_dict_to_camel_dict(snake_dict)
    assert result == {'simpleKey': 'value'}

def test_snake_dict_to_camel_dict_nested_dict():
    snake_dict = {'nested_key': {'inner_key': 'value'}}
    result = snake_dict_to_camel_dict(snake_dict)
    assert result == {'nestedKey': {'innerKey': 'value'}}

def test_snake_dict_to_camel_dict_list_in_dict():
    snake_dict = {'list_key': [{'inner_key': 'value'}]}
    result = snake_dict_to_camel_dict(snake_dict)
    assert result == {'listKey': [{'innerKey': 'value'}]}

def test_snake_dict_to_camel_dict_capitalize_first():
    snake_dict = {'simple_key': 'value'}
    result = snake_dict_to_camel_dict(snake_dict, capitalize_first=True)
    assert result == {'SimpleKey': 'value'}

def test_snake_dict_to_camel_dict_complex():
    snake_dict = {
        'outer_key': {
            'inner_key': [
                {'list_key_1': 'value1'},
                {'list_key_2': 'value2'}
            ]
        }
    }
    result = snake_dict_to_camel_dict(snake_dict)
    assert result == {
        'outerKey': {
            'innerKey': [
                {'listKey1': 'value1'},
                {'listKey2': 'value2'}
            ]
        }
    }
