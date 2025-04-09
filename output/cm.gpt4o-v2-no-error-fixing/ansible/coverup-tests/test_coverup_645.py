# file: lib/ansible/plugins/action/copy.py:50-52
# asked: {"lines": [50, 52], "branches": []}
# gained: {"lines": [50, 52], "branches": []}

import pytest

def test_create_remote_copy_args():
    from ansible.plugins.action.copy import _create_remote_copy_args

    # Test case where 'content' and 'decrypt' keys are present
    module_args = {
        'src': '/path/to/source',
        'dest': '/path/to/dest',
        'content': 'some content',
        'decrypt': True,
        'other_key': 'other_value'
    }
    expected_result = {
        'src': '/path/to/source',
        'dest': '/path/to/dest',
        'other_key': 'other_value'
    }
    result = _create_remote_copy_args(module_args)
    assert result == expected_result

    # Test case where 'content' and 'decrypt' keys are not present
    module_args = {
        'src': '/path/to/source',
        'dest': '/path/to/dest',
        'other_key': 'other_value'
    }
    expected_result = {
        'src': '/path/to/source',
        'dest': '/path/to/dest',
        'other_key': 'other_value'
    }
    result = _create_remote_copy_args(module_args)
    assert result == expected_result

    # Test case where only 'content' key is present
    module_args = {
        'src': '/path/to/source',
        'dest': '/path/to/dest',
        'content': 'some content'
    }
    expected_result = {
        'src': '/path/to/source',
        'dest': '/path/to/dest'
    }
    result = _create_remote_copy_args(module_args)
    assert result == expected_result

    # Test case where only 'decrypt' key is present
    module_args = {
        'src': '/path/to/source',
        'dest': '/path/to/dest',
        'decrypt': True
    }
    expected_result = {
        'src': '/path/to/source',
        'dest': '/path/to/dest'
    }
    result = _create_remote_copy_args(module_args)
    assert result == expected_result
