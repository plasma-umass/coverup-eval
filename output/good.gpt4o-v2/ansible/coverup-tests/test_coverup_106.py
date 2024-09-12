# file: lib/ansible/module_utils/common/dict_transformations.py:55-76
# asked: {"lines": [55, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 73, 74, 76], "branches": [[63, 64], [63, 65], [66, 67], [66, 69], [67, 68], [67, 74], [69, 70], [69, 73], [70, 71], [70, 74]]}
# gained: {"lines": [55, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 73, 74, 76], "branches": [[63, 64], [63, 65], [66, 67], [66, 69], [67, 68], [67, 74], [69, 70], [69, 73], [70, 71], [70, 74]]}

import pytest
from ansible.module_utils.common.dict_transformations import snake_dict_to_camel_dict

def test_snake_dict_to_camel_dict_with_none():
    result = snake_dict_to_camel_dict(None)
    assert result is None

def test_snake_dict_to_camel_dict_with_empty_dict():
    result = snake_dict_to_camel_dict({})
    assert result == {}

def test_snake_dict_to_camel_dict_with_empty_list():
    result = snake_dict_to_camel_dict([])
    assert result == []

def test_snake_dict_to_camel_dict_with_simple_dict():
    snake_dict = {'simple_key': 'value'}
    expected = {'simpleKey': 'value'}
    result = snake_dict_to_camel_dict(snake_dict)
    assert result == expected

def test_snake_dict_to_camel_dict_with_nested_dict():
    snake_dict = {'nested_key': {'inner_key': 'value'}}
    expected = {'nestedKey': {'innerKey': 'value'}}
    result = snake_dict_to_camel_dict(snake_dict)
    assert result == expected

def test_snake_dict_to_camel_dict_with_list_in_dict():
    snake_dict = {'list_key': [{'inner_key': 'value'}]}
    expected = {'listKey': [{'innerKey': 'value'}]}
    result = snake_dict_to_camel_dict(snake_dict)
    assert result == expected

def test_snake_dict_to_camel_dict_with_capitalize_first():
    snake_dict = {'simple_key': 'value'}
    expected = {'SimpleKey': 'value'}
    result = snake_dict_to_camel_dict(snake_dict, capitalize_first=True)
    assert result == expected

def test_snake_dict_to_camel_dict_with_mixed_types():
    snake_dict = {
        'outer_key': [
            {'inner_key': 'value'},
            'string_value',
            123,
            None,
            {'another_inner_key': ['list_item']}
        ]
    }
    expected = {
        'outerKey': [
            {'innerKey': 'value'},
            'string_value',
            123,
            None,
            {'anotherInnerKey': ['list_item']}
        ]
    }
    result = snake_dict_to_camel_dict(snake_dict)
    assert result == expected
