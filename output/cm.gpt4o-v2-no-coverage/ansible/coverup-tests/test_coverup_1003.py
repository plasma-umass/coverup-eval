# file: lib/ansible/module_utils/common/collections.py:28-29
# asked: {"lines": [28, 29], "branches": []}
# gained: {"lines": [28, 29], "branches": []}

import pytest
from ansible.module_utils.common.collections import ImmutableDict

def test_immutable_dict_hash():
    # Create an instance of ImmutableDict
    d = ImmutableDict(a=1, b=2, c=3)
    
    # Calculate the hash
    d_hash = hash(d)
    
    # Verify the hash is as expected
    expected_hash = hash(frozenset(d.items()))
    assert d_hash == expected_hash

    # Verify that the hash remains consistent
    assert d_hash == hash(d)
