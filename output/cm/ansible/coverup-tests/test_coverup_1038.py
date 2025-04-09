# file lib/ansible/module_utils/common/collections.py:19-20
# lines [19, 20]
# branches []

import pytest
from ansible.module_utils.common.collections import ImmutableDict

def test_ImmutableDict_getitem():
    # Setup: Create an ImmutableDict instance with some data
    data = {'key1': 'value1', 'key2': 'value2'}
    immutable_dict = ImmutableDict(data)

    # Exercise & Verify: Access existing keys
    assert immutable_dict['key1'] == 'value1'
    assert immutable_dict['key2'] == 'value2'

    # Verify: Accessing a non-existing key raises KeyError
    with pytest.raises(KeyError):
        _ = immutable_dict['nonexistent']

    # Cleanup: Nothing to clean up as no external resources are modified
