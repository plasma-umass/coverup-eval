# file: lib/ansible/plugins/callback/default.py:78-99
# asked: {"lines": [], "branches": [[83, 86], [93, 95]]}
# gained: {"lines": [], "branches": [[83, 86]]}

import pytest
from unittest.mock import Mock, patch, ANY
from ansible.plugins.callback.default import CallbackModule

@pytest.fixture
def callback_module():
    module = CallbackModule()
    module.display_failed_stderr = True
    return module

@pytest.fixture
def result():
    mock_result = Mock()
    mock_result._task = Mock()
    mock_result._task._uuid = 'some-uuid'
    mock_result._task.action = 'some-action'
    mock_result._task.loop = False
    mock_result._result = {}
    return mock_result

def test_v2_runner_on_failed_with_new_task(callback_module, result, mocker):
    result._task._uuid = 'new-uuid'
    callback_module._last_task_banner = 'old-uuid'
    callback_module._display = Mock()
    callback_module._display.verbosity = 1
    mocker.patch.object(callback_module, 'host_label', return_value='host_label')
    mocker.patch.object(callback_module, '_clean_results')
    mocker.patch.object(callback_module, '_print_task_banner')
    mocker.patch.object(callback_module, '_handle_exception')
    mocker.patch.object(callback_module, '_handle_warnings')
    mocker.patch.object(callback_module, 'get_option', return_value=True)
    mocker.patch.object(callback_module, '_dump_results', return_value='dumped_results')
    
    callback_module.v2_runner_on_failed(result)
    
    callback_module._print_task_banner.assert_called_once_with(result._task)
    callback_module._handle_exception.assert_called_once_with(result._result, use_stderr=callback_module.display_failed_stderr)
    callback_module._handle_warnings.assert_called_once_with(result._result)
    callback_module._display.display.assert_called_with("fatal: [host_label]: FAILED! => dumped_results", color=ANY, stderr=callback_module.display_failed_stderr)

def test_v2_runner_on_failed_with_task_path(callback_module, result, mocker):
    callback_module._last_task_banner = result._task._uuid
    callback_module._display = Mock()
    callback_module._display.verbosity = 1
    mocker.patch.object(callback_module, 'host_label', return_value='host_label')
    mocker.patch.object(callback_module, '_clean_results')
    mocker.patch.object(callback_module, '_handle_exception')
    mocker.patch.object(callback_module, '_handle_warnings')
    mocker.patch.object(callback_module, 'get_option', return_value=True)
    mocker.patch.object(callback_module, '_dump_results', return_value='dumped_results')
    mocker.patch.object(callback_module, '_print_task_path')
    
    callback_module.v2_runner_on_failed(result)
    
    callback_module._print_task_path.assert_called_once_with(result._task)
    callback_module._display.display.assert_called_with("fatal: [host_label]: FAILED! => dumped_results", color=ANY, stderr=callback_module.display_failed_stderr)
