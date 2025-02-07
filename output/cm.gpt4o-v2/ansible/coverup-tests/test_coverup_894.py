# file: lib/ansible/plugins/action/copy.py:50-52
# asked: {"lines": [50, 52], "branches": []}
# gained: {"lines": [50, 52], "branches": []}

import pytest
from ansible.plugins.action.copy import _create_remote_copy_args

def test_create_remote_copy_args():
    module_args = {
        'src': '/path/to/source',
        'dest': '/path/to/dest',
        'content': 'some content',
        'decrypt': True,
        'other_arg': 'value'
    }
    
    expected_result = {
        'src': '/path/to/source',
        'dest': '/path/to/dest',
        'other_arg': 'value'
    }
    
    result = _create_remote_copy_args(module_args)
    assert result == expected_result
