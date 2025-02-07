# file: lib/ansible/plugins/action/copy.py:45-47
# asked: {"lines": [45, 47], "branches": []}
# gained: {"lines": [45, 47], "branches": []}

import pytest
from ansible.plugins.action.copy import _create_remote_file_args
from ansible.module_utils.basic import FILE_COMMON_ARGUMENTS

REAL_FILE_ARGS = frozenset(FILE_COMMON_ARGUMENTS.keys()).union(('state', 'path', '_original_basename', 'recurse', 'force', '_diff_peek', 'src'))

def test_create_remote_file_args():
    module_args = {
        'state': 'present',
        'path': '/tmp/testfile',
        '_original_basename': 'testfile',
        'recurse': True,
        'force': True,
        '_diff_peek': False,
        'src': '/tmp/sourcefile',
        'irrelevant_key': 'irrelevant_value'
    }
    
    expected_args = {
        'state': 'present',
        'path': '/tmp/testfile',
        '_original_basename': 'testfile',
        'recurse': True,
        'force': True,
        '_diff_peek': False,
        'src': '/tmp/sourcefile'
    }
    
    result = _create_remote_file_args(module_args)
    assert result == expected_args
    assert 'irrelevant_key' not in result
