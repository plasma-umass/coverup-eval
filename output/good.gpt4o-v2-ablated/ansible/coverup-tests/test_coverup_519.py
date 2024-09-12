# file: lib/ansible/plugins/callback/junit.py:304-305
# asked: {"lines": [305], "branches": []}
# gained: {"lines": [305], "branches": []}

import pytest
from ansible.plugins.callback import CallbackBase
from ansible.plugins.callback.junit import CallbackModule

class MockResult:
    def __init__(self, task_name):
        self.task_name = task_name

@pytest.fixture
def callback_module():
    return CallbackModule()

def test_v2_runner_on_skipped(callback_module, mocker):
    mock_result = MockResult('test_task')
    mock_finish_task = mocker.patch.object(callback_module, '_finish_task')

    callback_module.v2_runner_on_skipped(mock_result)

    mock_finish_task.assert_called_once_with('skipped', mock_result)
