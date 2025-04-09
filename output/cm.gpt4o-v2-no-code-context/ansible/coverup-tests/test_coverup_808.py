# file: lib/ansible/plugins/action/copy.py:50-52
# asked: {"lines": [50, 52], "branches": []}
# gained: {"lines": [50, 52], "branches": []}

import pytest

def test_create_remote_copy_args():
    from ansible.plugins.action.copy import _create_remote_copy_args

    # Test case where 'content' and 'decrypt' keys are present
    module_args = {
        'src': '/path/to/source',
        'dest': '/path/to/destination',
        'content': 'some content',
        'decrypt': True,
        'mode': '0644'
    }
    expected_result = {
        'src': '/path/to/source',
        'dest': '/path/to/destination',
        'mode': '0644'
    }
    result = _create_remote_copy_args(module_args)
    assert result == expected_result

    # Test case where 'content' and 'decrypt' keys are not present
    module_args = {
        'src': '/path/to/source',
        'dest': '/path/to/destination',
        'mode': '0644'
    }
    expected_result = {
        'src': '/path/to/source',
        'dest': '/path/to/destination',
        'mode': '0644'
    }
    result = _create_remote_copy_args(module_args)
    assert result == expected_result

    # Test case where only 'content' key is present
    module_args = {
        'src': '/path/to/source',
        'dest': '/path/to/destination',
        'content': 'some content',
        'mode': '0644'
    }
    expected_result = {
        'src': '/path/to/source',
        'dest': '/path/to/destination',
        'mode': '0644'
    }
    result = _create_remote_copy_args(module_args)
    assert result == expected_result

    # Test case where only 'decrypt' key is present
    module_args = {
        'src': '/path/to/source',
        'dest': '/path/to/destination',
        'decrypt': True,
        'mode': '0644'
    }
    expected_result = {
        'src': '/path/to/source',
        'dest': '/path/to/destination',
        'mode': '0644'
    }
    result = _create_remote_copy_args(module_args)
    assert result == expected_result
