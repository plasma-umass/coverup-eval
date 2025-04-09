# file: lib/ansible/module_utils/common/collections.py:28-29
# asked: {"lines": [28, 29], "branches": []}
# gained: {"lines": [28, 29], "branches": []}

import pytest
from ansible.module_utils.common.collections import ImmutableDict

def test_immutable_dict_hash():
    # Create an instance of ImmutableDict
    immut_dict = ImmutableDict(a=1, b=2, c=3)
    
    # Calculate the hash
    dict_hash = hash(immut_dict)
    
    # Verify that the hash is as expected
    assert dict_hash == hash(frozenset(immut_dict.items()))

    # Verify that the hash is consistent
    assert dict_hash == hash(immut_dict)

    # Verify that two ImmutableDicts with the same items have the same hash
    immut_dict2 = ImmutableDict(a=1, b=2, c=3)
    assert hash(immut_dict) == hash(immut_dict2)

    # Verify that two ImmutableDicts with different items have different hashes
    immut_dict3 = ImmutableDict(a=1, b=2, c=4)
    assert hash(immut_dict) != hash(immut_dict3)
