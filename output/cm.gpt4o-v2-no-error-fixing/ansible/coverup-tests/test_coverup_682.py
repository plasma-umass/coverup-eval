# file: lib/ansible/module_utils/common/collections.py:22-23
# asked: {"lines": [22, 23], "branches": []}
# gained: {"lines": [22, 23], "branches": []}

import pytest
from ansible.module_utils.common.collections import ImmutableDict

def test_immutable_dict_iter():
    data = {'key1': 'value1', 'key2': 'value2'}
    immut_dict = ImmutableDict(data)
    
    iterator = iter(immut_dict)
    keys = list(iterator)
    
    assert keys == list(data.keys())
