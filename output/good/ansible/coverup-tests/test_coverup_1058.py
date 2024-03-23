# file lib/ansible/module_utils/common/collections.py:40-41
# lines [40, 41]
# branches []

import pytest
from ansible.module_utils.common.collections import ImmutableDict

def test_immutable_dict_repr():
    # Create an ImmutableDict with a simple dictionary to test the __repr__ method
    immutable_dict = ImmutableDict({'key': 'value'})
    
    # Call __repr__ and assert it returns the expected string
    repr_string = repr(immutable_dict)
    assert repr_string == "ImmutableDict({'key': 'value'})"
    
    # Cleanup: No cleanup necessary as we are not affecting any global state
