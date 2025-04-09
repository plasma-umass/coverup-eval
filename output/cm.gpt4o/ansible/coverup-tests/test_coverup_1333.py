# file lib/ansible/plugins/action/copy.py:45-47
# lines [47]
# branches []

import pytest
from ansible.plugins.action.copy import _create_remote_file_args

REAL_FILE_ARGS = {'src', 'dest', 'mode', 'owner', 'group'}

def test_create_remote_file_args(mocker):
    module_args = {
        'src': '/path/to/source',
        'dest': '/path/to/dest',
        'mode': '0644',
        'owner': 'user',
        'group': 'group',
        'extra_arg': 'should_be_removed'
    }
    
    expected_result = {
        'src': '/path/to/source',
        'dest': '/path/to/dest',
        'mode': '0644',
        'owner': 'user',
        'group': 'group'
    }
    
    # Mocking REAL_FILE_ARGS to ensure it is used in the function
    mocker.patch('ansible.plugins.action.copy.REAL_FILE_ARGS', REAL_FILE_ARGS)
    
    result = _create_remote_file_args(module_args)
    
    assert result == expected_result
    assert 'extra_arg' not in result
