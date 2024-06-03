# file lib/ansible/plugins/callback/default.py:263-288
# lines [263, 265, 266, 267, 268, 269, 270, 272, 273, 275, 276, 278, 279, 281, 282, 284, 285, 286, 287, 288]
# branches ['266->267', '266->268', '268->269', '268->275', '269->270', '269->272', '275->276', '275->278', '278->279', '278->281', '286->287', '286->288']

import pytest
from unittest.mock import MagicMock, patch
from ansible.plugins.callback.default import CallbackModule
from ansible.executor.task_result import TaskResult
from ansible.playbook.task_include import TaskInclude
from ansible.playbook.task import Task
from ansible import constants as C

@pytest.fixture
def callback_module():
    return CallbackModule()

@pytest.fixture
def mock_result():
    result = MagicMock(spec=TaskResult)
    result._task = MagicMock(spec=Task)
    result._result = {}
    result._host = MagicMock()
    return result

def test_v2_runner_item_on_ok_changed(callback_module, mock_result):
    mock_result._result = {'changed': True}
    mock_result._task._uuid = 'test-uuid'
    callback_module._last_task_banner = None
    callback_module._print_task_banner = MagicMock()
    callback_module._clean_results = MagicMock()
    callback_module._run_is_verbose = MagicMock(return_value=False)
    callback_module._display = MagicMock()
    callback_module.host_label = MagicMock(return_value='test-host')
    callback_module._get_item_label = MagicMock(return_value='test-item')

    callback_module.v2_runner_item_on_ok(mock_result)

    callback_module._print_task_banner.assert_called_once_with(mock_result._task)
    callback_module._clean_results.assert_called_once_with(mock_result._result, mock_result._task.action)
    callback_module._display.display.assert_called_once_with('changed: [test-host] => (item=test-item)', color=C.COLOR_CHANGED)

def test_v2_runner_item_on_ok_ok(callback_module, mock_result):
    mock_result._result = {'changed': False}
    mock_result._task._uuid = 'test-uuid'
    callback_module._last_task_banner = None
    callback_module._print_task_banner = MagicMock()
    callback_module._clean_results = MagicMock()
    callback_module._run_is_verbose = MagicMock(return_value=False)
    callback_module._display = MagicMock()
    callback_module.host_label = MagicMock(return_value='test-host')
    callback_module._get_item_label = MagicMock(return_value='test-item')
    callback_module.display_ok_hosts = True

    callback_module.v2_runner_item_on_ok(mock_result)

    callback_module._print_task_banner.assert_called_once_with(mock_result._task)
    callback_module._clean_results.assert_called_once_with(mock_result._result, mock_result._task.action)
    callback_module._display.display.assert_called_once_with('ok: [test-host] => (item=test-item)', color=C.COLOR_OK)

def test_v2_runner_item_on_ok_task_include(callback_module, mock_result):
    mock_result._task = MagicMock(spec=TaskInclude)
    callback_module._print_task_banner = MagicMock()

    callback_module.v2_runner_item_on_ok(mock_result)

    callback_module._print_task_banner.assert_not_called()
