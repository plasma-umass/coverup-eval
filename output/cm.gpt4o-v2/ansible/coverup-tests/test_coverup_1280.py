# file: lib/ansible/vars/clean.py:69-95
# asked: {"lines": [], "branches": [[78, 77], [85, 90]]}
# gained: {"lines": [], "branches": [[85, 90]]}

import pytest
from ansible.errors import AnsibleError
from ansible.module_utils.common._collections_compat import MutableMapping, MutableSequence
from ansible.module_utils.six import string_types
from ansible.vars.clean import strip_internal_keys

def test_strip_internal_keys_with_nested_structures():
    data = {
        '_ansible_keep': 'value1',
        '_ansible_remove': 'value2',
        'nested_dict': {
            '_ansible_nested_keep': 'nested_value1',
            '_ansible_nested_remove': 'nested_value2',
        },
        'nested_list': [
            {
                '_ansible_list_keep': 'list_value1',
                '_ansible_list_remove': 'list_value2',
            }
        ]
    }
    exceptions = ('_ansible_keep', '_ansible_nested_keep', '_ansible_list_keep')
    result = strip_internal_keys(data, exceptions=exceptions)
    
    assert '_ansible_keep' in result
    assert '_ansible_remove' not in result
    assert '_ansible_nested_keep' in result['nested_dict']
    assert '_ansible_nested_remove' not in result['nested_dict']
    assert '_ansible_list_keep' in result['nested_list'][0]
    assert '_ansible_list_remove' not in result['nested_list'][0]

def test_strip_internal_keys_with_invalid_type():
    with pytest.raises(AnsibleError, match="Cannot strip invalid keys from <class 'int'>"):
        strip_internal_keys(123)

def test_strip_internal_keys_with_string_key():
    data = {
        '_ansible_keep': 'value1',
        '_ansible_remove': 'value2',
        'normal_key': 'value3'
    }
    exceptions = ('_ansible_keep',)
    result = strip_internal_keys(data, exceptions=exceptions)
    
    assert '_ansible_keep' in result
    assert '_ansible_remove' not in result
    assert 'normal_key' in result

def test_strip_internal_keys_with_mutable_sequence():
    data = [
        {
            '_ansible_keep': 'value1',
            '_ansible_remove': 'value2',
        },
        {
            'nested_list': [
                {
                    '_ansible_list_keep': 'list_value1',
                    '_ansible_list_remove': 'list_value2',
                }
            ]
        }
    ]
    exceptions = ('_ansible_keep', '_ansible_list_keep')
    result = strip_internal_keys(data, exceptions=exceptions)
    
    assert '_ansible_keep' in result[0]
    assert '_ansible_remove' not in result[0]
    assert '_ansible_list_keep' in result[1]['nested_list'][0]
    assert '_ansible_list_remove' not in result[1]['nested_list'][0]

def test_strip_internal_keys_with_non_string_key():
    data = {
        '_ansible_keep': 'value1',
        '_ansible_remove': 'value2',
        123: 'numeric_key'
    }
    exceptions = ('_ansible_keep',)
    result = strip_internal_keys(data, exceptions=exceptions)
    
    assert '_ansible_keep' in result
    assert '_ansible_remove' not in result
    assert 123 in result
