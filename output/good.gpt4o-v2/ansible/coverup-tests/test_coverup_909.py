# file: lib/ansible/plugins/callback/junit.py:286-287
# asked: {"lines": [286, 287], "branches": []}
# gained: {"lines": [286, 287], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.plugins.callback import CallbackBase
from ansible.plugins.callback.junit import CallbackModule

@pytest.fixture
def callback_module():
    return CallbackModule()

def test_v2_playbook_on_task_start(callback_module, mocker):
    task = MagicMock()
    task._uuid = "test-uuid"
    task.get_name.return_value = "test-task"
    task.get_path.return_value = "/path/to/task"
    task.action = "test-action"
    task.args = {"arg1": "value1"}
    task.no_log = False

    mocker.patch.object(callback_module, '_start_task')

    callback_module.v2_playbook_on_task_start(task, is_conditional=False)

    callback_module._start_task.assert_called_once_with(task)

def test_start_task(callback_module):
    task = MagicMock()
    task._uuid = "test-uuid"
    task.get_name.return_value = "test-task"
    task.get_path.return_value = "/path/to/task"
    task.action = "test-action"
    task.args = {"arg1": "value1"}
    task.no_log = False

    callback_module._task_data = {}
    callback_module._play_name = "test-play"
    callback_module._hide_task_arguments = 'false'

    callback_module._start_task(task)

    assert task._uuid in callback_module._task_data
    task_data = callback_module._task_data[task._uuid]
    assert task_data.name == "test-task arg1=value1"
    assert task_data.path == "/path/to/task"
    assert task_data.play == "test-play"
    assert task_data.action == "test-action"
