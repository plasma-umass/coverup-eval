# file lib/ansible/module_utils/common/collections.py:40-41
# lines [40, 41]
# branches []

import pytest
from ansible.module_utils.common.collections import ImmutableDict

def test_immutable_dict_repr():
    # Create an instance of ImmutableDict
    data = {'key1': 'value1', 'key2': 'value2'}
    immutable_dict = ImmutableDict(data)
    
    # Check the __repr__ method
    expected_repr = "ImmutableDict({'key1': 'value1', 'key2': 'value2'})"
    assert repr(immutable_dict) == expected_repr

    # Clean up (not strictly necessary here, but good practice)
    del immutable_dict
