# file: lib/ansible/module_utils/common/dict_transformations.py:55-76
# asked: {"lines": [55, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 73, 74, 76], "branches": [[63, 64], [63, 65], [66, 67], [66, 69], [67, 68], [67, 74], [69, 70], [69, 73], [70, 71], [70, 74]]}
# gained: {"lines": [55, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 73, 74, 76], "branches": [[63, 64], [63, 65], [66, 67], [66, 69], [67, 68], [67, 74], [69, 70], [69, 73], [70, 71], [70, 74]]}

import pytest
from ansible.module_utils.common.dict_transformations import snake_dict_to_camel_dict

def test_snake_dict_to_camel_dict_empty_dict():
    assert snake_dict_to_camel_dict({}) == {}

def test_snake_dict_to_camel_dict_simple_dict():
    snake_dict = {'simple_key': 'value'}
    camel_dict = {'simpleKey': 'value'}
    assert snake_dict_to_camel_dict(snake_dict) == camel_dict

def test_snake_dict_to_camel_dict_nested_dict():
    snake_dict = {'nested_key': {'inner_key': 'value'}}
    camel_dict = {'nestedKey': {'innerKey': 'value'}}
    assert snake_dict_to_camel_dict(snake_dict) == camel_dict

def test_snake_dict_to_camel_dict_list_in_dict():
    snake_dict = {'list_key': [{'inner_key': 'value'}]}
    camel_dict = {'listKey': [{'innerKey': 'value'}]}
    assert snake_dict_to_camel_dict(snake_dict) == camel_dict

def test_snake_dict_to_camel_dict_with_capitalize_first():
    snake_dict = {'simple_key': 'value'}
    camel_dict = {'SimpleKey': 'value'}
    assert snake_dict_to_camel_dict(snake_dict, capitalize_first=True) == camel_dict

def test_snake_dict_to_camel_dict_none():
    assert snake_dict_to_camel_dict(None) is None

def test_snake_dict_to_camel_dict_list():
    snake_list = [{'simple_key': 'value'}, {'another_key': 'another_value'}]
    camel_list = [{'simpleKey': 'value'}, {'anotherKey': 'another_value'}]
    assert snake_dict_to_camel_dict(snake_list) == camel_list

def test_snake_dict_to_camel_dict_mixed_types():
    snake_dict = {'key1': 'value1', 'key2': [{'inner_key': 'value2'}, 'string_value']}
    camel_dict = {'key1': 'value1', 'key2': [{'innerKey': 'value2'}, 'string_value']}
    assert snake_dict_to_camel_dict(snake_dict) == camel_dict
