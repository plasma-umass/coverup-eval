# file: lib/ansible/module_utils/common/collections.py:25-26
# asked: {"lines": [25, 26], "branches": []}
# gained: {"lines": [25, 26], "branches": []}

import pytest
from ansible.module_utils.common.collections import ImmutableDict

def test_immutable_dict_len():
    data = {'key1': 'value1', 'key2': 'value2'}
    immutable_dict = ImmutableDict(data)
    
    assert len(immutable_dict) == 2

    # Clean up
    del immutable_dict
