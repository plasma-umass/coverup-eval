# file lib/ansible/plugins/callback/minimal.py:76-78
# lines [77, 78]
# branches ['77->exit', '77->78']

import pytest
from ansible.plugins.callback import minimal
from ansible.executor.task_result import TaskResult
from unittest.mock import MagicMock

@pytest.fixture
def minimal_callback():
    return minimal.CallbackModule()

@pytest.fixture
def task_result():
    mock_result = TaskResult(
        host='localhost',
        task=MagicMock(),
        return_data={
            'diff': 'some diff'
        }
    )
    return mock_result

def test_v2_on_file_diff_with_diff(minimal_callback, task_result, mocker):
    display_mock = mocker.patch.object(minimal_callback._display, 'display')
    minimal_callback.v2_on_file_diff(task_result)
    display_mock.assert_called_once_with(minimal_callback._get_diff('some diff'))

def test_v2_on_file_diff_without_diff(minimal_callback, task_result, mocker):
    task_result._result['diff'] = None
    display_mock = mocker.patch.object(minimal_callback._display, 'display')
    minimal_callback.v2_on_file_diff(task_result)
    display_mock.assert_not_called()
