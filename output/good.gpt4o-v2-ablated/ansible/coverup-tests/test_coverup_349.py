# file: lib/ansible/plugins/callback/junit.py:286-287
# asked: {"lines": [286, 287], "branches": []}
# gained: {"lines": [286, 287], "branches": []}

import pytest
from ansible.plugins.callback import CallbackBase
from ansible.plugins.callback.junit import CallbackModule

class MockTask:
    def __init__(self, name):
        self.name = name

@pytest.fixture
def callback_module():
    return CallbackModule()

def test_v2_playbook_on_task_start(callback_module, mocker):
    mock_task = MockTask(name="test_task")
    mock_start_task = mocker.patch.object(callback_module, '_start_task')

    callback_module.v2_playbook_on_task_start(mock_task, is_conditional=False)

    mock_start_task.assert_called_once_with(mock_task)
