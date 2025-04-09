# file: lib/ansible/utils/collection_loader/_collection_finder.py:1014-1021
# asked: {"lines": [1014, 1015, 1016, 1017, 1018, 1019, 1021], "branches": [[1016, 1017], [1016, 1021], [1018, 1016], [1018, 1019]]}
# gained: {"lines": [1014, 1015, 1016, 1017, 1018, 1019, 1021], "branches": [[1016, 1017], [1016, 1021], [1018, 1016], [1018, 1019]]}

import pytest

def test_nested_dict_get():
    from ansible.utils.collection_loader._collection_finder import _nested_dict_get

    # Test case where all keys are found
    root_dict = {'a': {'b': {'c': 'value'}}}
    key_list = ['a', 'b', 'c']
    assert _nested_dict_get(root_dict, key_list) == 'value'

    # Test case where a key is not found
    key_list = ['a', 'b', 'd']
    assert _nested_dict_get(root_dict, key_list) is None

    # Test case where intermediate key is not found
    key_list = ['a', 'x', 'c']
    assert _nested_dict_get(root_dict, key_list) is None

    # Test case where root_dict is empty
    root_dict = {}
    key_list = ['a', 'b', 'c']
    assert _nested_dict_get(root_dict, key_list) is None

    # Test case where key_list is empty
    root_dict = {'a': {'b': {'c': 'value'}}}
    key_list = []
    assert _nested_dict_get(root_dict, key_list) == root_dict
