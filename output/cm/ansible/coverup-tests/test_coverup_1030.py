# file lib/ansible/module_utils/common/collections.py:22-23
# lines [22, 23]
# branches []

import pytest
from ansible.module_utils.common.collections import ImmutableDict

def test_immutable_dict_iteration():
    # Setup the ImmutableDict with some data
    data = {'a': 1, 'b': 2, 'c': 3}
    immutable_dict = ImmutableDict(data)

    # Test __iter__ method
    keys = list(iter(immutable_dict))
    assert keys == list(data.keys()), "The keys from iteration do not match the original data keys"

    # Cleanup is not necessary as ImmutableDict does not modify any external state
