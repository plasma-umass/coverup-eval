# file lib/ansible/module_utils/common/dict_transformations.py:112-124
# lines [112, 116, 117, 118, 119, 120, 121, 123, 124]
# branches ['116->117', '116->118', '119->120', '119->124', '120->121', '120->123']

import pytest
from copy import deepcopy
from ansible.module_utils.common.dict_transformations import dict_merge

def test_dict_merge(mocker):
    # Test case 1: Merging two dictionaries with nested dictionaries
    a = {'key1': {'subkey1': 'value1'}, 'key2': 'value2'}
    b = {'key1': {'subkey2': 'value3'}, 'key3': 'value4'}
    expected_result = {'key1': {'subkey1': 'value1', 'subkey2': 'value3'}, 'key2': 'value2', 'key3': 'value4'}
    result = dict_merge(a, b)
    assert result == expected_result

    # Test case 2: Merging when b is not a dictionary
    a = {'key1': 'value1'}
    b = 'not_a_dict'
    result = dict_merge(a, b)
    assert result == 'not_a_dict'

    # Test case 3: Merging when a key in b is not a dictionary
    a = {'key1': {'subkey1': 'value1'}}
    b = {'key1': 'value2'}
    expected_result = {'key1': 'value2'}
    result = dict_merge(a, b)
    assert result == expected_result

    # Test case 4: Merging when a key in a is not a dictionary
    a = {'key1': 'value1'}
    b = {'key1': {'subkey1': 'value2'}}
    expected_result = {'key1': {'subkey1': 'value2'}}
    result = dict_merge(a, b)
    assert result == expected_result

    # Test case 5: Merging empty dictionaries
    a = {}
    b = {}
    expected_result = {}
    result = dict_merge(a, b)
    assert result == expected_result

    # Test case 6: Merging with one empty dictionary
    a = {'key1': 'value1'}
    b = {}
    expected_result = {'key1': 'value1'}
    result = dict_merge(a, b)
    assert result == expected_result

    a = {}
    b = {'key1': 'value1'}
    expected_result = {'key1': 'value1'}
    result = dict_merge(a, b)
    assert result == expected_result
