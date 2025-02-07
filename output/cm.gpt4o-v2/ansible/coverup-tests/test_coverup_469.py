# file: lib/ansible/module_utils/common/collections.py:31-38
# asked: {"lines": [31, 32, 33, 34, 35, 36, 38], "branches": [[33, 34], [33, 38]]}
# gained: {"lines": [31, 32, 33, 34, 35, 36, 38], "branches": [[33, 34], [33, 38]]}

import pytest
from ansible.module_utils.common.collections import ImmutableDict

def test_immutable_dict_eq_with_equal_hash():
    dict1 = ImmutableDict(a=1, b=2)
    dict2 = ImmutableDict(a=1, b=2)
    
    assert dict1 == dict2

def test_immutable_dict_eq_with_unequal_hash():
    dict1 = ImmutableDict(a=1, b=2)
    dict2 = ImmutableDict(a=2, b=3)
    
    assert dict1 != dict2

def test_immutable_dict_eq_with_type_error():
    dict1 = ImmutableDict(a=1, b=2)
    not_a_dict = [("a", 1), ("b", 2)]
    
    assert dict1 != not_a_dict
