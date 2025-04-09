# file: lib/ansible/plugins/action/copy.py:45-47
# asked: {"lines": [45, 47], "branches": []}
# gained: {"lines": [45, 47], "branches": []}

import pytest
from ansible.plugins.action.copy import _create_remote_file_args, REAL_FILE_ARGS

def test_create_remote_file_args():
    module_args = {
        'src': 'source_file',
        'dest': 'destination_file',
        'state': 'present',
        'path': '/some/path',
        '_original_basename': 'basename',
        'recurse': True,
        'force': False,
        '_diff_peek': True,
        'unrelated_key': 'should_be_removed'
    }

    expected_args = {
        'src': 'source_file',
        'state': 'present',
        'path': '/some/path',
        '_original_basename': 'basename',
        'recurse': True,
        'force': False,
        '_diff_peek': True
    }

    result = _create_remote_file_args(module_args)
    assert result == expected_args
    assert 'unrelated_key' not in result
