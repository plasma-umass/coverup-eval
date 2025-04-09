# file: lib/ansible/plugins/callback/junit.py:292-293
# asked: {"lines": [293], "branches": []}
# gained: {"lines": [293], "branches": []}

import pytest
from unittest.mock import Mock
from ansible.plugins.callback import CallbackBase
from ansible.plugins.callback.junit import CallbackModule

@pytest.fixture
def callback_module():
    return CallbackModule()

def test_v2_playbook_on_handler_task_start(callback_module):
    task = Mock()
    task._uuid = "1234"
    task.get_name.return_value = "test_task"
    task.get_path.return_value = "/path/to/task"
    task.action = "test_action"
    task.no_log = False
    task.args = {"arg1": "value1", "arg2": "value2"}

    callback_module.v2_playbook_on_handler_task_start(task)

    assert "1234" in callback_module._task_data
    task_data = callback_module._task_data["1234"]
    assert task_data.uuid == "1234"
    assert task_data.name == "test_task arg1=value1, arg2=value2"
    assert task_data.path == "/path/to/task"
    assert task_data.play == callback_module._play_name
    assert task_data.action == "test_action"
