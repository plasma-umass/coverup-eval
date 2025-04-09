# file: lib/ansible/module_utils/common/collections.py:55-65
# asked: {"lines": [55, 63, 64, 65], "branches": []}
# gained: {"lines": [55, 63, 64, 65], "branches": []}

import pytest
from ansible.module_utils.common.collections import ImmutableDict

def test_difference():
    original = ImmutableDict(a=1, b=2, c=3)
    subtractive = ['b', 'c']
    result = original.difference(subtractive)
    
    assert isinstance(result, ImmutableDict)
    assert 'a' in result
    assert 'b' not in result
    assert 'c' not in result
    assert result['a'] == 1

def test_difference_no_keys_removed():
    original = ImmutableDict(a=1, b=2, c=3)
    subtractive = ['d', 'e']
    result = original.difference(subtractive)
    
    assert isinstance(result, ImmutableDict)
    assert 'a' in result
    assert 'b' in result
    assert 'c' in result
    assert result['a'] == 1
    assert result['b'] == 2
    assert result['c'] == 3

def test_difference_all_keys_removed():
    original = ImmutableDict(a=1, b=2, c=3)
    subtractive = ['a', 'b', 'c']
    result = original.difference(subtractive)
    
    assert isinstance(result, ImmutableDict)
    assert len(result) == 0
