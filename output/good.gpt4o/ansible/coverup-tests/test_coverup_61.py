# file lib/ansible/vars/clean.py:69-95
# lines [69, 72, 73, 75, 77, 78, 79, 81, 84, 85, 86, 87, 88, 90, 91, 93, 95]
# branches ['72->73', '72->75', '75->77', '75->81', '77->78', '77->95', '78->77', '78->79', '81->84', '81->93', '84->85', '84->95', '85->86', '85->90', '86->87', '86->90', '90->84', '90->91']

import pytest
from ansible.vars.clean import strip_internal_keys
from ansible.errors import AnsibleError
from collections.abc import MutableMapping, MutableSequence

def test_strip_internal_keys_dict():
    dirty = {
        '_ansible_internal': 'value',
        'valid_key': 'value',
        '_ansible_other': 'value'
    }
    expected = {
        'valid_key': 'value'
    }
    result = strip_internal_keys(dirty)
    assert result == expected

def test_strip_internal_keys_list():
    dirty = [
        {'_ansible_internal': 'value', 'valid_key': 'value'},
        {'_ansible_other': 'value', 'another_valid_key': 'value'}
    ]
    expected = [
        {'valid_key': 'value'},
        {'another_valid_key': 'value'}
    ]
    result = strip_internal_keys(dirty)
    assert result == expected

def test_strip_internal_keys_nested():
    dirty = {
        'level1': {
            '_ansible_internal': 'value',
            'level2': {
                '_ansible_other': 'value',
                'valid_key': 'value'
            }
        }
    }
    expected = {
        'level1': {
            'level2': {
                'valid_key': 'value'
            }
        }
    }
    result = strip_internal_keys(dirty)
    assert result == expected

def test_strip_internal_keys_exceptions():
    dirty = {
        '_ansible_internal': 'value',
        '_ansible_keep': 'value',
        'valid_key': 'value'
    }
    expected = {
        '_ansible_keep': 'value',
        'valid_key': 'value'
    }
    result = strip_internal_keys(dirty, exceptions=('_ansible_keep',))
    assert result == expected

def test_strip_internal_keys_invalid_type():
    with pytest.raises(AnsibleError, match="Cannot strip invalid keys from <class 'int'>"):
        strip_internal_keys(42)
