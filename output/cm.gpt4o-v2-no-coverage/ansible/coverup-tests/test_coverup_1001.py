# file: lib/ansible/module_utils/common/collections.py:19-20
# asked: {"lines": [19, 20], "branches": []}
# gained: {"lines": [19, 20], "branches": []}

import pytest
from ansible.module_utils.common.collections import ImmutableDict

def test_immutable_dict_getitem():
    # Create an instance of ImmutableDict
    immut_dict = ImmutableDict(a=1, b=2, c=3)
    
    # Test __getitem__ method
    assert immut_dict['a'] == 1
    assert immut_dict['b'] == 2
    assert immut_dict['c'] == 3
    
    # Test for a key that does not exist
    with pytest.raises(KeyError):
        _ = immut_dict['d']
