# file: lib/ansible/plugins/action/copy.py:50-52
# asked: {"lines": [50, 52], "branches": []}
# gained: {"lines": [50, 52], "branches": []}

import pytest

from ansible.plugins.action.copy import _create_remote_copy_args

def test_create_remote_copy_args_removes_keys():
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

def test_create_remote_copy_args_no_keys_to_remove():
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

def test_create_remote_copy_args_empty_input():
    module_args = {}
    expected_result = {}
    result = _create_remote_copy_args(module_args)
    assert result == expected_result

def test_create_remote_copy_args_only_keys_to_remove():
    module_args = {
        'content': 'some content',
        'decrypt': True
    }
    expected_result = {}
    result = _create_remote_copy_args(module_args)
    assert result == expected_result
