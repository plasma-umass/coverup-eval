# file lib/ansible/plugins/callback/default.py:247-261
# lines [247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261]
# branches ['248->249', '248->256', '249->exit', '249->250', '250->249', '250->251', '252->249', '252->253', '253->254', '253->255', '256->exit', '256->257', '258->exit', '258->259', '259->260', '259->261']

import pytest
from ansible.plugins.callback import default
from ansible.executor.task_result import TaskResult
from unittest.mock import MagicMock, patch

@pytest.fixture
def callback_module():
    callback = default.CallbackModule()
    callback._display = MagicMock()
    callback._last_task_banner = None
    callback._print_task_banner = MagicMock()
    callback._get_diff = MagicMock(return_value="diff")
    return callback

@pytest.fixture
def task_result():
    mock_task = MagicMock()
    mock_task.loop = None
    mock_task._uuid = "unique_id"
    mock_host = MagicMock()
    mock_host.name = "localhost"
    return TaskResult(mock_task, mock_host, {})

def test_v2_on_file_diff_with_diff_and_changed(callback_module, task_result):
    task_result._result = {'diff': 'fake_diff', 'changed': True}
    callback_module.v2_on_file_diff(task_result)
    callback_module._display.display.assert_called_once_with("diff")
    callback_module._print_task_banner.assert_called_once_with(task_result._task)

def test_v2_on_file_diff_with_diff_and_not_changed(callback_module, task_result):
    task_result._result = {'diff': 'fake_diff', 'changed': False}
    callback_module.v2_on_file_diff(task_result)
    callback_module._display.display.assert_not_called()
    callback_module._print_task_banner.assert_not_called()

def test_v2_on_file_diff_with_no_diff(callback_module, task_result):
    task_result._result = {'diff': None, 'changed': True}
    callback_module.v2_on_file_diff(task_result)
    callback_module._display.display.assert_not_called()
    callback_module._print_task_banner.assert_not_called()

def test_v2_on_file_diff_with_loop_and_diff(callback_module, task_result):
    task_result._task.loop = True
    task_result._result = {
        'results': [
            {'diff': 'fake_diff', 'changed': True},
            {'diff': 'fake_diff', 'changed': False},
            {'diff': None, 'changed': True}
        ]
    }
    callback_module.v2_on_file_diff(task_result)
    assert callback_module._display.display.call_count == 1
    callback_module._print_task_banner.assert_called_once_with(task_result._task)

def test_v2_on_file_diff_with_loop_and_no_diff(callback_module, task_result):
    task_result._task.loop = True
    task_result._result = {
        'results': [
            {'diff': None, 'changed': True},
            {'diff': None, 'changed': False}
        ]
    }
    callback_module.v2_on_file_diff(task_result)
    callback_module._display.display.assert_not_called()
    callback_module._print_task_banner.assert_not_called()
