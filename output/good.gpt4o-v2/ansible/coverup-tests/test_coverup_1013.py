# file: lib/ansible/module_utils/common/collections.py:43-53
# asked: {"lines": [43, 53], "branches": []}
# gained: {"lines": [43, 53], "branches": []}

import pytest
from ansible.module_utils.common.collections import ImmutableDict

def test_union_with_overriding_mapping():
    original = ImmutableDict(a=1, b=2)
    overriding = {'b': 3, 'c': 4}
    result = original.union(overriding)
    
    assert isinstance(result, ImmutableDict)
    assert result['a'] == 1
    assert result['b'] == 3
    assert result['c'] == 4

def test_union_with_empty_overriding_mapping():
    original = ImmutableDict(a=1, b=2)
    overriding = {}
    result = original.union(overriding)
    
    assert isinstance(result, ImmutableDict)
    assert result['a'] == 1
    assert result['b'] == 2
    assert 'c' not in result

def test_union_with_new_keys():
    original = ImmutableDict(a=1, b=2)
    overriding = {'c': 3, 'd': 4}
    result = original.union(overriding)
    
    assert isinstance(result, ImmutableDict)
    assert result['a'] == 1
    assert result['b'] == 2
    assert result['c'] == 3
    assert result['d'] == 4
