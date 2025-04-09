# file: lib/ansible/plugins/callback/junit.py:289-290
# asked: {"lines": [290], "branches": []}
# gained: {"lines": [290], "branches": []}

import pytest
from unittest.mock import Mock
from ansible.plugins.callback import CallbackBase
from ansible.plugins.callback.junit import CallbackModule, TaskData

@pytest.fixture
def mock_task():
    task = Mock()
    task._uuid = "1234-uuid"
    task.get_name.return_value = "test_task"
    task.get_path.return_value = "/path/to/task"
    task.action = "test_action"
    task.no_log = False
    task.args = {"arg1": "value1", "arg2": "value2"}
    return task

@pytest.fixture
def callback_module():
    module = CallbackModule()
    module._task_data = {}
    module._play_name = "test_play"
    module._hide_task_arguments = 'false'
    return module

def test_v2_playbook_on_cleanup_task_start(callback_module, mock_task):
    callback_module.v2_playbook_on_cleanup_task_start(mock_task)
    
    assert mock_task._uuid in callback_module._task_data
    task_data = callback_module._task_data[mock_task._uuid]
    assert task_data.name == "test_task arg1=value1, arg2=value2"
    assert task_data.path == "/path/to/task"
    assert task_data.play == "test_play"
    assert task_data.action == "test_action"
