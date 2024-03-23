# file lib/ansible/plugins/callback/junit.py:301-302
# lines [301, 302]
# branches []

import pytest
from ansible.plugins.callback.junit import CallbackModule
from ansible.executor.task_result import TaskResult
from unittest.mock import MagicMock

# Define a fixture for the callback module
@pytest.fixture
def junit_callback():
    return CallbackModule()

# Define a fixture for the task result
@pytest.fixture
def task_result():
    host = MagicMock()
    host.name = 'localhost'
    fake_result = {
        'changed': False,
        'failed': False,
        'ansible_facts': {}
    }
    return TaskResult(host=host, task=MagicMock(), return_data=fake_result)

# Define the test function for v2_runner_on_ok
def test_v2_runner_on_ok(junit_callback, task_result, mocker):
    mocker.patch.object(junit_callback, '_finish_task')
    junit_callback.v2_runner_on_ok(task_result)
    junit_callback._finish_task.assert_called_once_with('ok', task_result)
