# file: lib/ansible/module_utils/common/collections.py:22-23
# asked: {"lines": [22, 23], "branches": []}
# gained: {"lines": [22, 23], "branches": []}

import pytest
from ansible.module_utils.common.collections import ImmutableDict

def test_immutable_dict_iter():
    data = {'key1': 'value1', 'key2': 'value2'}
    immut_dict = ImmutableDict(data)
    
    # Collect all keys using the __iter__ method
    keys = list(iter(immut_dict))
    
    # Assert that the keys match the original dictionary's keys
    assert keys == list(data.keys())
