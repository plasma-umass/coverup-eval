# file: lib/ansible/module_utils/common/collections.py:55-65
# asked: {"lines": [55, 63, 64, 65], "branches": []}
# gained: {"lines": [55, 63, 64, 65], "branches": []}

import pytest
from ansible.module_utils.common.collections import ImmutableDict

def test_immutable_dict_difference():
    original_dict = ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    subtractive_iterable = ['b', 'c']
    
    new_dict = original_dict.difference(subtractive_iterable)
    
    assert 'a' in new_dict
    assert 'b' not in new_dict
    assert 'c' not in new_dict
    assert new_dict['a'] == 1

def test_immutable_dict_difference_no_keys_removed():
    original_dict = ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    subtractive_iterable = ['d', 'e']
    
    new_dict = original_dict.difference(subtractive_iterable)
    
    assert 'a' in new_dict
    assert 'b' in new_dict
    assert 'c' in new_dict
    assert new_dict['a'] == 1
    assert new_dict['b'] == 2
    assert new_dict['c'] == 3

def test_immutable_dict_difference_all_keys_removed():
    original_dict = ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    subtractive_iterable = ['a', 'b', 'c']
    
    new_dict = original_dict.difference(subtractive_iterable)
    
    assert 'a' not in new_dict
    assert 'b' not in new_dict
    assert 'c' not in new_dict
    assert len(new_dict) == 0
