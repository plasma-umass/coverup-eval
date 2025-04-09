# file: lib/ansible/plugins/callback/junit.py:286-287
# asked: {"lines": [286, 287], "branches": []}
# gained: {"lines": [286, 287], "branches": []}

import pytest
from unittest.mock import Mock
from ansible.plugins.callback.junit import CallbackModule

@pytest.fixture
def callback_module():
    module = CallbackModule()
    module._task_data = {}
    module._play_name = "test_play"
    module._hide_task_arguments = 'false'
    return module

def test_v2_playbook_on_task_start(callback_module):
    task = Mock()
    task._uuid = "1234"
    task.get_name.return_value = "test_task"
    task.get_path.return_value = "/path/to/task"
    task.action = "test_action"
    task.no_log = False
    task.args = {"arg1": "value1", "arg2": "value2"}

    callback_module.v2_playbook_on_task_start(task, is_conditional=False)

    assert "1234" in callback_module._task_data
    task_data = callback_module._task_data["1234"]
    assert task_data.uuid == "1234"
    assert task_data.name == "test_task arg1=value1, arg2=value2"
    assert task_data.path == "/path/to/task"
    assert task_data.play == "test_play"
    assert task_data.action == "test_action"

def test_v2_playbook_on_task_start_existing_task(callback_module):
    task = Mock()
    task._uuid = "1234"
    callback_module._task_data["1234"] = "existing_task_data"

    callback_module.v2_playbook_on_task_start(task, is_conditional=False)

    assert callback_module._task_data["1234"] == "existing_task_data"
