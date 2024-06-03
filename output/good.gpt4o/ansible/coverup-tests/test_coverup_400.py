# file lib/ansible/utils/collection_loader/_collection_finder.py:1014-1021
# lines [1014, 1015, 1016, 1017, 1018, 1019, 1021]
# branches ['1016->1017', '1016->1021', '1018->1016', '1018->1019']

import pytest

from ansible.utils.collection_loader._collection_finder import _nested_dict_get

def test_nested_dict_get(mocker):
    # Test case where the key_list is found in the dictionary
    root_dict = {'a': {'b': {'c': 'value'}}}
    key_list = ['a', 'b', 'c']
    assert _nested_dict_get(root_dict, key_list) == 'value'

    # Test case where the key_list is not found in the dictionary
    key_list = ['a', 'b', 'd']
    assert _nested_dict_get(root_dict, key_list) is None

    # Test case where the key_list is partially found in the dictionary
    key_list = ['a', 'x']
    assert _nested_dict_get(root_dict, key_list) is None

    # Test case where the key_list is empty
    key_list = []
    assert _nested_dict_get(root_dict, key_list) == root_dict

    # Test case where the root_dict is empty
    root_dict = {}
    key_list = ['a']
    assert _nested_dict_get(root_dict, key_list) is None
