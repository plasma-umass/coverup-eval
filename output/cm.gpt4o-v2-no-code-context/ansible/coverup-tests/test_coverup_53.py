# file: lib/ansible/vars/clean.py:69-95
# asked: {"lines": [69, 72, 73, 75, 77, 78, 79, 81, 84, 85, 86, 87, 88, 90, 91, 93, 95], "branches": [[72, 73], [72, 75], [75, 77], [75, 81], [77, 78], [77, 95], [78, 77], [78, 79], [81, 84], [81, 93], [84, 85], [84, 95], [85, 86], [85, 90], [86, 87], [86, 90], [90, 84], [90, 91]]}
# gained: {"lines": [69, 72, 73, 75, 77, 78, 79, 81, 84, 85, 86, 87, 88, 90, 91, 93, 95], "branches": [[72, 73], [72, 75], [75, 77], [75, 81], [77, 78], [77, 95], [78, 79], [81, 84], [81, 93], [84, 85], [84, 95], [85, 86], [86, 87], [86, 90], [90, 84], [90, 91]]}

import pytest
from ansible.errors import AnsibleError
from ansible.vars.clean import strip_internal_keys
from collections.abc import MutableMapping, MutableSequence

def test_strip_internal_keys_with_none_exceptions():
    dirty = {
        '_ansible_keep': 'keep this',
        '_ansible_remove': 'remove this',
        'normal_key': 'keep this too'
    }
    result = strip_internal_keys(dirty)
    assert '_ansible_remove' not in result
    assert '_ansible_keep' not in result
    assert 'normal_key' in result

def test_strip_internal_keys_with_exceptions():
    dirty = {
        '_ansible_keep': 'keep this',
        '_ansible_remove': 'remove this',
        'normal_key': 'keep this too'
    }
    result = strip_internal_keys(dirty, exceptions=('_ansible_keep',))
    assert '_ansible_remove' not in result
    assert '_ansible_keep' in result
    assert 'normal_key' in result

def test_strip_internal_keys_with_mutable_sequence():
    dirty = [
        {'_ansible_remove': 'remove this', 'normal_key': 'keep this'},
        {'_ansible_keep': 'keep this', '_ansible_remove': 'remove this'}
    ]
    result = strip_internal_keys(dirty)
    assert '_ansible_remove' not in result[0]
    assert 'normal_key' in result[0]
    assert '_ansible_remove' not in result[1]
    assert '_ansible_keep' not in result[1]

def test_strip_internal_keys_with_invalid_type():
    with pytest.raises(AnsibleError, match="Cannot strip invalid keys from <class 'int'>"):
        strip_internal_keys(123)

def test_strip_internal_keys_nested_structure():
    dirty = {
        'level1': {
            '_ansible_remove': 'remove this',
            'level2': {
                '_ansible_keep': 'keep this',
                '_ansible_remove': 'remove this'
            }
        }
    }
    result = strip_internal_keys(dirty, exceptions=('_ansible_keep',))
    assert '_ansible_remove' not in result['level1']
    assert '_ansible_keep' in result['level1']['level2']
    assert '_ansible_remove' not in result['level1']['level2']
