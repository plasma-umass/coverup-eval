# file lib/ansible/module_utils/common/collections.py:28-29
# lines [28, 29]
# branches []

import pytest
from ansible.module_utils.common.collections import ImmutableDict

def test_immutable_dict_hash():
    # Create an instance of ImmutableDict
    immutable_dict = ImmutableDict({'a': 1, 'b': 2})

    # Calculate the hash of the ImmutableDict instance
    hash_value = hash(immutable_dict)

    # Create a frozenset of the items and calculate its hash
    expected_hash = hash(frozenset(immutable_dict.items()))

    # Assert that the hash of the ImmutableDict instance is equal to the expected hash
    assert hash_value == expected_hash

    # Cleanup is not necessary as ImmutableDict does not modify any external state
