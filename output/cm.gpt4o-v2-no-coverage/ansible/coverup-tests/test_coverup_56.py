# file: lib/ansible/vars/clean.py:69-95
# asked: {"lines": [69, 72, 73, 75, 77, 78, 79, 81, 84, 85, 86, 87, 88, 90, 91, 93, 95], "branches": [[72, 73], [72, 75], [75, 77], [75, 81], [77, 78], [77, 95], [78, 77], [78, 79], [81, 84], [81, 93], [84, 85], [84, 95], [85, 86], [85, 90], [86, 87], [86, 90], [90, 84], [90, 91]]}
# gained: {"lines": [69, 72, 73, 75, 77, 78, 79, 81, 84, 85, 86, 87, 88, 90, 91, 93, 95], "branches": [[72, 73], [72, 75], [75, 77], [75, 81], [77, 78], [77, 95], [78, 79], [81, 84], [81, 93], [84, 85], [84, 95], [85, 86], [86, 87], [86, 90], [90, 84], [90, 91]]}

import pytest
from ansible.errors import AnsibleError
from ansible.module_utils.common._collections_compat import MutableMapping, MutableSequence
from ansible.module_utils.six import string_types
from ansible.vars.clean import strip_internal_keys

def test_strip_internal_keys_with_dict():
    dirty = {
        '_ansible_keep': 'value1',
        '_ansible_remove': 'value2',
        'normal_key': 'value3'
    }
    exceptions = ('_ansible_keep',)
    result = strip_internal_keys(dirty, exceptions)
    assert '_ansible_keep' in result
    assert '_ansible_remove' not in result
    assert 'normal_key' in result

def test_strip_internal_keys_with_list():
    dirty = [
        {'_ansible_keep': 'value1', '_ansible_remove': 'value2'},
        {'normal_key': 'value3'}
    ]
    exceptions = ('_ansible_keep',)
    result = strip_internal_keys(dirty, exceptions)
    assert '_ansible_keep' in result[0]
    assert '_ansible_remove' not in result[0]
    assert 'normal_key' in result[1]

def test_strip_internal_keys_with_invalid_type():
    with pytest.raises(AnsibleError, match="Cannot strip invalid keys from <class 'int'>"):
        strip_internal_keys(123)

def test_strip_internal_keys_with_nested_structures():
    dirty = {
        'level1': {
            '_ansible_keep': 'value1',
            '_ansible_remove': 'value2',
            'level2': [
                {'_ansible_keep': 'value3', '_ansible_remove': 'value4'},
                {'normal_key': 'value5'}
            ]
        }
    }
    exceptions = ('_ansible_keep',)
    result = strip_internal_keys(dirty, exceptions)
    assert '_ansible_keep' in result['level1']
    assert '_ansible_remove' not in result['level1']
    assert '_ansible_keep' in result['level1']['level2'][0]
    assert '_ansible_remove' not in result['level1']['level2'][0]
    assert 'normal_key' in result['level1']['level2'][1]
