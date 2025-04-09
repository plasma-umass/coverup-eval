# file: lib/ansible/plugins/action/copy.py:50-52
# asked: {"lines": [50, 52], "branches": []}
# gained: {"lines": [50, 52], "branches": []}

import pytest

from ansible.plugins.action.copy import _create_remote_copy_args

def test_create_remote_copy_args():
    # Test with keys 'content' and 'decrypt' present
    module_args = {
        'src': '/path/to/source',
        'dest': '/path/to/dest',
        'content': 'some content',
        'decrypt': True
    }
    expected_result = {
        'src': '/path/to/source',
        'dest': '/path/to/dest'
    }
    result = _create_remote_copy_args(module_args)
    assert result == expected_result

    # Test with no 'content' and 'decrypt' keys
    module_args = {
        'src': '/path/to/source',
        'dest': '/path/to/dest'
    }
    expected_result = {
        'src': '/path/to/source',
        'dest': '/path/to/dest'
    }
    result = _create_remote_copy_args(module_args)
    assert result == expected_result

    # Test with only 'content' key
    module_args = {
        'src': '/path/to/source',
        'content': 'some content'
    }
    expected_result = {
        'src': '/path/to/source'
    }
    result = _create_remote_copy_args(module_args)
    assert result == expected_result

    # Test with only 'decrypt' key
    module_args = {
        'src': '/path/to/source',
        'decrypt': True
    }
    expected_result = {
        'src': '/path/to/source'
    }
    result = _create_remote_copy_args(module_args)
    assert result == expected_result
