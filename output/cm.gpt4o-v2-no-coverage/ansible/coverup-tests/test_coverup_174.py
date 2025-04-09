# file: lib/ansible/plugins/callback/default.py:78-99
# asked: {"lines": [78, 80, 81, 83, 84, 86, 87, 89, 90, 93, 94, 95, 96, 98, 99], "branches": [[83, 84], [83, 86], [89, 90], [89, 93], [93, 94], [93, 95], [98, 0], [98, 99]]}
# gained: {"lines": [78, 80, 81, 83, 84, 86, 87, 89, 90, 93, 94, 95, 96, 98, 99], "branches": [[83, 84], [89, 90], [89, 93], [93, 94], [98, 0], [98, 99]]}

import pytest
from unittest.mock import Mock, patch
from ansible.plugins.callback.default import CallbackModule
from ansible import constants as C

@pytest.fixture
def callback_module():
    return CallbackModule()

def test_v2_runner_on_failed(callback_module, mocker):
    result = Mock()
    result._result = {'exception': 'Test exception\nTraceback...'}
    result._task.action = 'test_action'
    result._task._uuid = '1234'
    result._task.loop = False
    result._task.get_path = Mock(return_value='/path/to/task')
    result._task.get_name = Mock(return_value='test_task')
    result._task.delegate_to = None
    result._host.get_name = Mock(return_value='localhost')
    
    callback_module._last_task_banner = '5678'
    callback_module._last_task_name = None
    callback_module._task_type_cache = {'1234': 'TASK'}
    callback_module._display = Mock()
    callback_module._display.verbosity = 1
    callback_module.display_failed_stderr = True
    callback_module.get_option = Mock(return_value=True)
    
    mocker.patch.object(callback_module, 'host_label', return_value='localhost')
    mocker.patch.object(callback_module, '_clean_results')
    mocker.patch.object(callback_module, '_print_task_banner')
    mocker.patch.object(callback_module, '_handle_exception')
    mocker.patch.object(callback_module, '_handle_warnings')
    mocker.patch.object(callback_module, '_process_items')
    mocker.patch.object(callback_module, '_print_task_path')
    mocker.patch.object(callback_module, '_dump_results', return_value='dumped_result')
    
    callback_module.v2_runner_on_failed(result, ignore_errors=True)
    
    callback_module.host_label.assert_called_once_with(result)
    callback_module._clean_results.assert_called_once_with(result._result, result._task.action)
    callback_module._print_task_banner.assert_called_once_with(result._task)
    callback_module._handle_exception.assert_called_once_with(result._result, use_stderr=True)
    callback_module._handle_warnings.assert_called_once_with(result._result)
    callback_module._print_task_path.assert_called_once_with(result._task)
    callback_module._dump_results.assert_called_once_with(result._result)
    callback_module._display.display.assert_any_call("fatal: [localhost]: FAILED! => dumped_result", color=C.COLOR_ERROR, stderr=True)
    callback_module._display.display.assert_any_call("...ignoring", color=C.COLOR_SKIP)

def test_v2_runner_on_failed_with_loop(callback_module, mocker):
    result = Mock()
    result._result = {'results': ['item1', 'item2']}
    result._task.action = 'test_action'
    result._task._uuid = '1234'
    result._task.loop = True
    result._task.get_path = Mock(return_value='/path/to/task')
    result._task.get_name = Mock(return_value='test_task')
    result._task.delegate_to = None
    result._host.get_name = Mock(return_value='localhost')
    
    callback_module._last_task_banner = '5678'
    callback_module._last_task_name = None
    callback_module._task_type_cache = {'1234': 'TASK'}
    callback_module._display = Mock()
    callback_module._display.verbosity = 1
    callback_module.display_failed_stderr = True
    callback_module.get_option = Mock(return_value=True)
    
    mocker.patch.object(callback_module, 'host_label', return_value='localhost')
    mocker.patch.object(callback_module, '_clean_results')
    mocker.patch.object(callback_module, '_print_task_banner')
    mocker.patch.object(callback_module, '_handle_exception')
    mocker.patch.object(callback_module, '_handle_warnings')
    mocker.patch.object(callback_module, '_process_items')
    mocker.patch.object(callback_module, '_print_task_path')
    mocker.patch.object(callback_module, '_dump_results', return_value='dumped_result')
    
    callback_module.v2_runner_on_failed(result, ignore_errors=False)
    
    callback_module.host_label.assert_called_once_with(result)
    callback_module._clean_results.assert_called_once_with(result._result, result._task.action)
    callback_module._print_task_banner.assert_called_once_with(result._task)
    callback_module._handle_exception.assert_called_once_with(result._result, use_stderr=True)
    callback_module._handle_warnings.assert_called_once_with(result._result)
    callback_module._process_items.assert_called_once_with(result)
    callback_module._dump_results.assert_not_called()
    callback_module._display.display.assert_not_called()
