# file lib/ansible/module_utils/common/dict_transformations.py:112-124
# lines [112, 116, 117, 118, 119, 120, 121, 123, 124]
# branches ['116->117', '116->118', '119->120', '119->124', '120->121', '120->123']

import pytest
from copy import deepcopy
from ansible.module_utils.common.dict_transformations import dict_merge

def test_dict_merge():
    # Test merging where 'b' is not a dict
    assert dict_merge({'key1': 'value1'}, 'notadict') == 'notadict'

    # Test merging where 'b' is a dict
    a = {'key1': 'value1', 'nested': {'key2': 'value2'}}
    b = {'key3': 'value3', 'nested': {'key2': 'newvalue2'}}
    expected = {
        'key1': 'value1',
        'key3': 'value3',
        'nested': {'key2': 'newvalue2'}
    }
    assert dict_merge(a, b) == expected

    # Test merging where 'a' and 'b' have overlapping keys
    a = {'key1': 'value1', 'nested': {'key2': 'value2'}}
    b = {'key1': 'newvalue1', 'nested': {'key3': 'value3'}}
    expected = {
        'key1': 'newvalue1',
        'nested': {'key2': 'value2', 'key3': 'value3'}
    }
    assert dict_merge(a, b) == expected

    # Test merging where 'a' and 'b' have deeply nested overlapping keys
    a = {'nested': {'inner': {'key': 'value'}}}
    b = {'nested': {'inner': {'key': 'newvalue'}, 'inner2': 'value2'}}
    expected = {
        'nested': {
            'inner': {'key': 'newvalue'},
            'inner2': 'value2'
        }
    }
    assert dict_merge(a, b) == expected

    # Test merging with empty dicts
    assert dict_merge({}, {}) == {}
    assert dict_merge({'key': 'value'}, {}) == {'key': 'value'}
    assert dict_merge({}, {'key': 'value'}) == {'key': 'value'}

    # Test that the original dictionaries are not modified
    original_a = deepcopy(a)
    original_b = deepcopy(b)
    dict_merge(a, b)
    assert a == original_a
    assert b == original_b
