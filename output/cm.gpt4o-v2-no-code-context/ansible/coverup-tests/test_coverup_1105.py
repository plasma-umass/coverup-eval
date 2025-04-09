# file: lib/ansible/module_utils/common/collections.py:40-41
# asked: {"lines": [41], "branches": []}
# gained: {"lines": [41], "branches": []}

import pytest
from ansible.module_utils.common.collections import ImmutableDict

def test_immutable_dict_repr():
    # Create an instance of ImmutableDict
    data = {'key1': 'value1', 'key2': 'value2'}
    immutable_dict = ImmutableDict(data)
    
    # Verify the __repr__ method
    expected_repr = "ImmutableDict({0})".format(repr(data))
    assert repr(immutable_dict) == expected_repr
