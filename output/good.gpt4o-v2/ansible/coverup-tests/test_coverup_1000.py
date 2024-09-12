# file: lib/ansible/module_utils/common/collections.py:28-29
# asked: {"lines": [28, 29], "branches": []}
# gained: {"lines": [28, 29], "branches": []}

import pytest
from ansible.module_utils.common.collections import ImmutableDict

def test_immutable_dict_hash():
    # Create an instance of ImmutableDict
    immutable_dict = ImmutableDict(a=1, b=2, c=3)
    
    # Calculate the hash
    dict_hash = hash(immutable_dict)
    
    # Verify the hash is as expected
    expected_hash = hash(frozenset(immutable_dict.items()))
    assert dict_hash == expected_hash

    # Clean up
    del immutable_dict
