# file: lib/ansible/utils/collection_loader/_collection_finder.py:1014-1021
# asked: {"lines": [1014, 1015, 1016, 1017, 1018, 1019, 1021], "branches": [[1016, 1017], [1016, 1021], [1018, 1016], [1018, 1019]]}
# gained: {"lines": [1014, 1015, 1016, 1017, 1018, 1019, 1021], "branches": [[1016, 1017], [1016, 1021], [1018, 1016], [1018, 1019]]}

import pytest

from ansible.utils.collection_loader._collection_finder import _nested_dict_get

def test_nested_dict_get_existing_path():
    root_dict = {'a': {'b': {'c': 'value'}}}
    key_list = ['a', 'b', 'c']
    result = _nested_dict_get(root_dict, key_list)
    assert result == 'value'

def test_nested_dict_get_non_existing_path():
    root_dict = {'a': {'b': {'c': 'value'}}}
    key_list = ['a', 'x', 'c']
    result = _nested_dict_get(root_dict, key_list)
    assert result is None

def test_nested_dict_get_partial_path():
    root_dict = {'a': {'b': {'c': 'value'}}}
    key_list = ['a', 'b']
    result = _nested_dict_get(root_dict, key_list)
    assert result == {'c': 'value'}

def test_nested_dict_get_empty_key_list():
    root_dict = {'a': {'b': {'c': 'value'}}}
    key_list = []
    result = _nested_dict_get(root_dict, key_list)
    assert result == root_dict

def test_nested_dict_get_empty_dict():
    root_dict = {}
    key_list = ['a', 'b', 'c']
    result = _nested_dict_get(root_dict, key_list)
    assert result is None
