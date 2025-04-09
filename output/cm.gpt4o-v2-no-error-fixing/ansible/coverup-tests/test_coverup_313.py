# file: lib/ansible/module_utils/common/collections.py:31-38
# asked: {"lines": [31, 32, 33, 34, 35, 36, 38], "branches": [[33, 34], [33, 38]]}
# gained: {"lines": [31, 32, 33, 34, 35, 36, 38], "branches": [[33, 34], [33, 38]]}

import pytest
from ansible.module_utils.common.collections import ImmutableDict

def test_immutable_dict_eq_with_same_hash(mocker):
    dict1 = ImmutableDict(a=1, b=2)
    dict2 = ImmutableDict(a=1, b=2)
    
    mocker.patch.object(dict2, '__hash__', return_value=dict1.__hash__())
    
    assert dict1 == dict2

def test_immutable_dict_eq_with_different_hash(mocker):
    dict1 = ImmutableDict(a=1, b=2)
    dict2 = ImmutableDict(a=1, b=3)
    
    mocker.patch.object(dict2, '__hash__', return_value=dict1.__hash__() + 1)
    
    assert dict1 != dict2

def test_immutable_dict_eq_with_type_error(mocker):
    dict1 = ImmutableDict(a=1, b=2)
    dict2 = "not_a_dict"
    
    mocker.patch.object(dict1, '__hash__', side_effect=TypeError)
    
    assert dict1 != dict2
