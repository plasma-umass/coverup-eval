# file: lib/ansible/module_utils/common/dict_transformations.py:112-124
# asked: {"lines": [112, 116, 117, 118, 119, 120, 121, 123, 124], "branches": [[116, 117], [116, 118], [119, 120], [119, 124], [120, 121], [120, 123]]}
# gained: {"lines": [112, 116, 117, 118, 119, 120, 121, 123, 124], "branches": [[116, 117], [116, 118], [119, 120], [119, 124], [120, 121], [120, 123]]}

import pytest
from ansible.module_utils.common.dict_transformations import dict_merge

def test_dict_merge_with_non_dict():
    a = {'key1': 'value1'}
    b = ['not', 'a', 'dict']
    result = dict_merge(a, b)
    assert result == b

def test_dict_merge_with_empty_dict():
    a = {}
    b = {'key1': 'value1'}
    result = dict_merge(a, b)
    assert result == b

def test_dict_merge_with_nested_dicts():
    a = {'key1': {'subkey1': 'subvalue1'}}
    b = {'key1': {'subkey2': 'subvalue2'}}
    result = dict_merge(a, b)
    expected = {'key1': {'subkey1': 'subvalue1', 'subkey2': 'subvalue2'}}
    assert result == expected

def test_dict_merge_with_overlapping_keys():
    a = {'key1': 'value1'}
    b = {'key1': 'new_value1', 'key2': 'value2'}
    result = dict_merge(a, b)
    expected = {'key1': 'new_value1', 'key2': 'value2'}
    assert result == expected

def test_dict_merge_with_deepcopy():
    a = {'key1': {'subkey1': 'subvalue1'}}
    b = {'key1': {'subkey2': 'subvalue2'}}
    result = dict_merge(a, b)
    b['key1']['subkey2'] = 'modified_value'
    expected = {'key1': {'subkey1': 'subvalue1', 'subkey2': 'subvalue2'}}
    assert result == expected
