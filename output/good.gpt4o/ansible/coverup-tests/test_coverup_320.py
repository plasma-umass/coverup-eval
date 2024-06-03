# file lib/ansible/plugins/callback/default.py:290-304
# lines [290, 291, 292, 294, 295, 296, 298, 299, 300, 301, 302, 303]
# branches ['291->292', '291->294']

import pytest
from unittest.mock import MagicMock, patch
from ansible.plugins.callback.default import CallbackModule
from ansible.plugins.callback import CallbackBase
from ansible.executor.task_result import TaskResult
from ansible.playbook.task import Task
from ansible.utils.color import C

@pytest.fixture
def callback_module():
    return CallbackModule()

@pytest.fixture
def mock_result():
    task = Task()
    task._uuid = "1234-uuid"
    task.action = "test_action"
    result = TaskResult(
        host="localhost",
        task=task,
        return_data={"failed": True, "msg": "Test failure", "item": "test_item"}
    )
    result._task = task
    return result

def test_v2_runner_item_on_failed(callback_module, mock_result, mocker):
    mocker.patch.object(callback_module, '_print_task_banner')
    mocker.patch.object(callback_module, 'host_label', return_value="localhost")
    mocker.patch.object(callback_module, '_clean_results')
    mocker.patch.object(callback_module, '_handle_exception')
    mocker.patch.object(callback_module, '_handle_warnings')
    mocker.patch.object(callback_module, '_get_item_label', return_value="test_item")
    mocker.patch.object(callback_module, '_dump_results', return_value="{'failed': True, 'msg': 'Test failure', 'item': 'test_item'}")
    mocker.patch.object(callback_module._display, 'display')

    callback_module._last_task_banner = "different-uuid"
    callback_module.display_failed_stderr = True

    callback_module.v2_runner_item_on_failed(mock_result)

    callback_module._print_task_banner.assert_called_once_with(mock_result._task)
    callback_module._clean_results.assert_called_once_with(mock_result._result, mock_result._task.action)
    callback_module._handle_exception.assert_called_once_with(mock_result._result, use_stderr=True)
    callback_module._handle_warnings.assert_called_once_with(mock_result._result)
    callback_module._display.display.assert_called_once_with(
        "failed: [localhost] (item=test_item) => {'failed': True, 'msg': 'Test failure', 'item': 'test_item'}",
        color=C.COLOR_ERROR,
        stderr=True
    )
