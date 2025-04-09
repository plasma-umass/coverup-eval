# file: lib/ansible/module_utils/common/collections.py:40-41
# asked: {"lines": [40, 41], "branches": []}
# gained: {"lines": [40, 41], "branches": []}

import pytest
from ansible.module_utils.common.collections import ImmutableDict

def test_immutable_dict_repr():
    data = {'key1': 'value1', 'key2': 'value2'}
    immut_dict = ImmutableDict(data)
    expected_repr = f"ImmutableDict({repr(data)})"
    assert repr(immut_dict) == expected_repr

