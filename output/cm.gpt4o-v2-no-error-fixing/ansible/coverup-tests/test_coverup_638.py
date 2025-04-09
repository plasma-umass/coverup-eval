# file: lib/ansible/plugins/callback/junit.py:283-284
# asked: {"lines": [283, 284], "branches": []}
# gained: {"lines": [283, 284], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.plugins.callback import CallbackBase
from ansible.plugins.callback.junit import CallbackModule

@pytest.fixture
def callback_module():
    return CallbackModule()

def test_v2_runner_on_no_hosts(callback_module, mocker):
    task_mock = MagicMock()
    task_mock._uuid = "test-uuid"
    task_mock.get_name.return_value = "test-task"
    task_mock.get_path.return_value = "/path/to/task"
    task_mock.action = "test-action"
    task_mock.no_log = False
    task_mock.args = {"arg1": "value1"}

    mocker.patch.object(callback_module, '_start_task')
    callback_module.v2_runner_on_no_hosts(task_mock)
    
    callback_module._start_task.assert_called_once_with(task_mock)
