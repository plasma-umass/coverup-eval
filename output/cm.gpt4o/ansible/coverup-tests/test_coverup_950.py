# file lib/ansible/module_utils/common/collections.py:43-53
# lines [43, 53]
# branches []

import pytest
from ansible.module_utils.common.collections import ImmutableDict

def test_immutable_dict_union():
    original_dict = ImmutableDict({'key1': 'value1', 'key2': 'value2'})
    overriding_mapping = {'key2': 'new_value2', 'key3': 'value3'}
    
    new_dict = original_dict.union(overriding_mapping)
    
    assert new_dict['key1'] == 'value1'
    assert new_dict['key2'] == 'new_value2'
    assert new_dict['key3'] == 'value3'
    assert 'key1' in new_dict
    assert 'key2' in new_dict
    assert 'key3' in new_dict
    assert len(new_dict) == 3
