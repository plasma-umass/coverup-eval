# file lib/ansible/plugins/callback/junit.py:295-299
# lines [295, 296, 297, 299]
# branches ['296->297', '296->299']

import pytest
from ansible.plugins.callback.junit import CallbackModule
from ansible.executor.task_result import TaskResult
from unittest.mock import MagicMock

# Define a fixture for the CallbackModule
@pytest.fixture
def junit_callback():
    return CallbackModule()

# Define a fixture for the TaskResult
@pytest.fixture
def task_result():
    host = MagicMock()
    return TaskResult(host=host, task=MagicMock(), return_data={})

# Test to cover the branch where ignore_errors is True and _fail_on_ignore is not 'true'
def test_v2_runner_on_failed_ignore_errors(junit_callback, task_result, mocker):
    mocker.patch.object(junit_callback, '_finish_task')
    junit_callback._fail_on_ignore = 'false'
    junit_callback.v2_runner_on_failed(task_result, ignore_errors=True)
    junit_callback._finish_task.assert_called_once_with('ok', task_result)

# Test to cover the branch where ignore_errors is False
def test_v2_runner_on_failed_no_ignore_errors(junit_callback, task_result, mocker):
    mocker.patch.object(junit_callback, '_finish_task')
    junit_callback.v2_runner_on_failed(task_result, ignore_errors=False)
    junit_callback._finish_task.assert_called_once_with('failed', task_result)

# Test to cover the branch where ignore_errors is True and _fail_on_ignore is 'true'
def test_v2_runner_on_failed_ignore_errors_fail_on_ignore(junit_callback, task_result, mocker):
    mocker.patch.object(junit_callback, '_finish_task')
    junit_callback._fail_on_ignore = 'true'
    junit_callback.v2_runner_on_failed(task_result, ignore_errors=True)
    junit_callback._finish_task.assert_called_once_with('failed', task_result)
