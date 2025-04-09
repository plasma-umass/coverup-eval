# file: lib/ansible/module_utils/common/collections.py:25-26
# asked: {"lines": [25, 26], "branches": []}
# gained: {"lines": [25, 26], "branches": []}

import pytest
from ansible.module_utils.common.collections import ImmutableDict

def test_immutable_dict_len():
    data = {'a': 1, 'b': 2, 'c': 3}
    immut_dict = ImmutableDict(data)
    
    assert len(immut_dict) == 3

    # Clean up
    del immut_dict
