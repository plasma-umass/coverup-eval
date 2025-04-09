# file lib/ansible/plugins/callback/tree.py:39-86
# lines [39, 40, 44, 45, 46, 47, 49, 52, 54, 56, 58, 60, 63, 64, 65, 66, 67, 69, 70, 71, 72, 73, 74, 76, 77, 79, 80, 82, 83, 85, 86]
# branches ['54->56', '54->58']

import pytest
import os
from unittest.mock import MagicMock, patch
from ansible.plugins.callback.tree import CallbackModule
from ansible.utils.display import Display
from ansible.parsing.ajson import AnsibleJSONEncoder
from ansible.module_utils._text import to_bytes, to_text
from ansible.utils.path import makedirs_safe, unfrackpath

@pytest.fixture
def callback_module():
    cb = CallbackModule()
    cb._display = Display()
    cb.get_option = MagicMock(return_value='/tmp/test_tree')
    cb._load_name = 'tree'
    return cb

@pytest.fixture
def result():
    mock_result = MagicMock()
    mock_result._host.get_name.return_value = 'test_host'
    mock_result._result = {'key': 'value'}
    return mock_result

def test_set_options_with_tree_dir(callback_module, mocker):
    mocker.patch('ansible.plugins.callback.tree.TREE_DIR', '/tmp/tree_dir')
    mocker.patch('ansible.plugins.callback.tree.unfrackpath', return_value='/tmp/tree_dir')
    callback_module.set_options()
    assert callback_module.tree == '/tmp/tree_dir'

def test_set_options_without_tree_dir(callback_module, mocker):
    mocker.patch('ansible.plugins.callback.tree.TREE_DIR', None)
    callback_module.set_options()
    assert callback_module.tree == '/tmp/test_tree'

def test_write_tree_file_success(callback_module, mocker):
    mocker.patch('ansible.plugins.callback.tree.makedirs_safe')
    mocker.patch('builtins.open', mocker.mock_open())
    callback_module.tree = '/tmp/test_tree'
    callback_module.write_tree_file('test_host', 'test_buffer')
    open.assert_called_once_with(to_bytes('/tmp/test_tree/test_host'), 'wb+')

def test_write_tree_file_fail_makedirs(callback_module, mocker):
    mocker.patch('ansible.plugins.callback.tree.makedirs_safe', side_effect=OSError('Permission denied'))
    callback_module.tree = '/tmp/test_tree'
    with patch.object(callback_module._display, 'warning') as mock_warning:
        callback_module.write_tree_file('test_host', 'test_buffer')
        mock_warning.assert_any_call("Unable to access or create the configured directory (/tmp/test_tree): Permission denied")

def test_write_tree_file_fail_open(callback_module, mocker):
    mocker.patch('ansible.plugins.callback.tree.makedirs_safe')
    mocker.patch('builtins.open', side_effect=OSError('Permission denied'))
    callback_module.tree = '/tmp/test_tree'
    with patch.object(callback_module._display, 'warning') as mock_warning:
        callback_module.write_tree_file('test_host', 'test_buffer')
        mock_warning.assert_any_call("Unable to write to test_host's file: Permission denied")

def test_result_to_tree(callback_module, result, mocker):
    mocker.patch.object(callback_module, 'write_tree_file')
    mocker.patch.object(callback_module, '_dump_results', return_value='{"key": "value"}')
    callback_module.result_to_tree(result)
    callback_module.write_tree_file.assert_called_once_with('test_host', '{"key": "value"}')

def test_v2_runner_on_ok(callback_module, result, mocker):
    mocker.patch.object(callback_module, 'result_to_tree')
    callback_module.v2_runner_on_ok(result)
    callback_module.result_to_tree.assert_called_once_with(result)

def test_v2_runner_on_failed(callback_module, result, mocker):
    mocker.patch.object(callback_module, 'result_to_tree')
    callback_module.v2_runner_on_failed(result)
    callback_module.result_to_tree.assert_called_once_with(result)

def test_v2_runner_on_unreachable(callback_module, result, mocker):
    mocker.patch.object(callback_module, 'result_to_tree')
    callback_module.v2_runner_on_unreachable(result)
    callback_module.result_to_tree.assert_called_once_with(result)
