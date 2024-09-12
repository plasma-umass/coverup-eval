# file: lib/ansible/vars/clean.py:69-95
# asked: {"lines": [69, 72, 73, 75, 77, 78, 79, 81, 84, 85, 86, 87, 88, 90, 91, 93, 95], "branches": [[72, 73], [72, 75], [75, 77], [75, 81], [77, 78], [77, 95], [78, 77], [78, 79], [81, 84], [81, 93], [84, 85], [84, 95], [85, 86], [85, 90], [86, 87], [86, 90], [90, 84], [90, 91]]}
# gained: {"lines": [69, 72, 73, 75, 77, 78, 79, 81, 84, 85, 86, 87, 88, 90, 91, 93, 95], "branches": [[72, 73], [72, 75], [75, 77], [75, 81], [77, 78], [77, 95], [78, 79], [81, 84], [81, 93], [84, 85], [84, 95], [85, 86], [86, 87], [86, 90], [90, 84], [90, 91]]}

import pytest
from ansible.errors import AnsibleError
from collections.abc import MutableMapping, MutableSequence
import six

# Assuming the function strip_internal_keys is imported from ansible/vars/clean.py
from ansible.vars.clean import strip_internal_keys

def test_strip_internal_keys_dict():
    dirty = {
        '_ansible_keep': 'keep',
        '_ansible_remove': 'remove',
        'normal_key': 'value'
    }
    expected = {
        '_ansible_keep': 'keep',
        'normal_key': 'value'
    }
    result = strip_internal_keys(dirty, exceptions=('_ansible_keep',))
    assert result == expected

def test_strip_internal_keys_list():
    dirty = [
        {'_ansible_keep': 'keep', '_ansible_remove': 'remove', 'normal_key': 'value'},
        {'_ansible_remove': 'remove', 'normal_key': 'value'}
    ]
    expected = [
        {'_ansible_keep': 'keep', 'normal_key': 'value'},
        {'normal_key': 'value'}
    ]
    result = strip_internal_keys(dirty, exceptions=('_ansible_keep',))
    assert result == expected

def test_strip_internal_keys_nested():
    dirty = {
        'level1': {
            '_ansible_keep': 'keep',
            '_ansible_remove': 'remove',
            'level2': {
                '_ansible_remove': 'remove',
                'normal_key': 'value'
            }
        }
    }
    expected = {
        'level1': {
            '_ansible_keep': 'keep',
            'level2': {
                'normal_key': 'value'
            }
        }
    }
    result = strip_internal_keys(dirty, exceptions=('_ansible_keep',))
    assert result == expected

def test_strip_internal_keys_invalid_type():
    with pytest.raises(AnsibleError, match="Cannot strip invalid keys from <class 'int'>"):
        strip_internal_keys(123)

def test_strip_internal_keys_no_exceptions():
    dirty = {
        '_ansible_remove': 'remove',
        'normal_key': 'value'
    }
    expected = {
        'normal_key': 'value'
    }
    result = strip_internal_keys(dirty)
    assert result == expected

def test_strip_internal_keys_empty_dict():
    dirty = {}
    expected = {}
    result = strip_internal_keys(dirty)
    assert result == expected

def test_strip_internal_keys_empty_list():
    dirty = []
    expected = []
    result = strip_internal_keys(dirty)
    assert result == expected
