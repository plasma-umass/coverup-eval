# file lib/ansible/module_utils/common/collections.py:28-29
# lines [29]
# branches []

import pytest
from ansible.module_utils.common.collections import ImmutableDict

def test_immutable_dict_hash():
    # Create an instance of ImmutableDict with some items
    data = {'key1': 'value1', 'key2': 'value2'}
    immutable_dict = ImmutableDict(data)
    
    # Calculate the hash
    dict_hash = hash(immutable_dict)
    
    # Verify that the hash is as expected
    expected_hash = hash(frozenset(data.items()))
    assert dict_hash == expected_hash

    # Clean up
    del immutable_dict
