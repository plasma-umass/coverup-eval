# file lib/ansible/utils/vars.py:82-94
# lines [82, 87, 88, 91, 92, 93, 94]
# branches ['87->88', '87->91']

import pytest
from ansible.utils.vars import combine_vars
from ansible import constants as C

def test_combine_vars_merge_behavior(mocker):
    # Mock the DEFAULT_HASH_BEHAVIOUR to 'merge'
    mocker.patch.object(C, 'DEFAULT_HASH_BEHAVIOUR', 'merge')
    
    a = {'key1': 'value1', 'key2': 'value2'}
    b = {'key2': 'new_value2', 'key3': 'value3'}
    
    result = combine_vars(a, b)
    
    assert result == {'key1': 'value1', 'key2': 'new_value2', 'key3': 'value3'}

def test_combine_vars_replace_behavior(mocker):
    # Mock the DEFAULT_HASH_BEHAVIOUR to 'replace'
    mocker.patch.object(C, 'DEFAULT_HASH_BEHAVIOUR', 'replace')
    
    a = {'key1': 'value1', 'key2': 'value2'}
    b = {'key2': 'new_value2', 'key3': 'value3'}
    
    result = combine_vars(a, b)
    
    assert result == {'key1': 'value1', 'key2': 'new_value2', 'key3': 'value3'}

def test_combine_vars_explicit_merge():
    a = {'key1': 'value1', 'key2': 'value2'}
    b = {'key2': 'new_value2', 'key3': 'value3'}
    
    result = combine_vars(a, b, merge=True)
    
    assert result == {'key1': 'value1', 'key2': 'new_value2', 'key3': 'value3'}

def test_combine_vars_explicit_replace():
    a = {'key1': 'value1', 'key2': 'value2'}
    b = {'key2': 'new_value2', 'key3': 'value3'}
    
    result = combine_vars(a, b, merge=False)
    
    assert result == {'key1': 'value1', 'key2': 'new_value2', 'key3': 'value3'}
