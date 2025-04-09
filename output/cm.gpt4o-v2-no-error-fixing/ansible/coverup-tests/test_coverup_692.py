# file: lib/ansible/module_utils/common/collections.py:19-20
# asked: {"lines": [19, 20], "branches": []}
# gained: {"lines": [19, 20], "branches": []}

import pytest
from ansible.module_utils.common.collections import ImmutableDict

def test_immutable_dict_getitem():
    # Create an instance of ImmutableDict with some initial data
    data = {'key1': 'value1', 'key2': 'value2'}
    immutable_dict = ImmutableDict(data)
    
    # Test __getitem__ method
    assert immutable_dict['key1'] == 'value1'
    assert immutable_dict['key2'] == 'value2'
    
    # Test for a key that does not exist to ensure KeyError is raised
    with pytest.raises(KeyError):
        _ = immutable_dict['key3']
