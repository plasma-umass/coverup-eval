# file: lib/ansible/vars/clean.py:69-95
# asked: {"lines": [], "branches": [[85, 90]]}
# gained: {"lines": [], "branches": [[85, 90]]}

import pytest
from ansible.errors import AnsibleError
from ansible.vars.clean import strip_internal_keys
from collections.abc import MutableMapping, MutableSequence
import six

def test_strip_internal_keys_with_internal_keys():
    dirty = {
        '_ansible_keep': 'value1',
        '_ansible_remove': 'value2',
        'normal_key': 'value3',
        'nested': {
            '_ansible_nested_remove': 'value4',
            'nested_key': 'value5'
        }
    }
    exceptions = ('_ansible_keep',)
    result = strip_internal_keys(dirty, exceptions)
    assert '_ansible_keep' in result
    assert '_ansible_remove' not in result
    assert 'normal_key' in result
    assert 'nested' in result
    assert '_ansible_nested_remove' not in result['nested']
    assert 'nested_key' in result['nested']

def test_strip_internal_keys_with_mutable_sequence():
    dirty = [
        {
            '_ansible_remove': 'value1',
            'normal_key': 'value2'
        },
        {
            '_ansible_remove': 'value3',
            'normal_key': 'value4'
        }
    ]
    result = strip_internal_keys(dirty)
    for element in result:
        assert '_ansible_remove' not in element
        assert 'normal_key' in element

def test_strip_internal_keys_with_invalid_type():
    with pytest.raises(AnsibleError, match="Cannot strip invalid keys from <class 'int'>"):
        strip_internal_keys(123)

def test_strip_internal_keys_with_non_string_keys():
    dirty = {
        1: 'value1',
        '_ansible_remove': 'value2',
        'normal_key': 'value3'
    }
    result = strip_internal_keys(dirty)
    assert 1 in result
    assert '_ansible_remove' not in result
    assert 'normal_key' in result
