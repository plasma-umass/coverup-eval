# file: lib/ansible/plugins/callback/junit.py:292-293
# asked: {"lines": [292, 293], "branches": []}
# gained: {"lines": [292, 293], "branches": []}

import pytest
from ansible.plugins.callback import CallbackBase
from ansible.plugins.callback.junit import CallbackModule

class MockTask:
    def __init__(self, name):
        self.name = name

@pytest.fixture
def callback_module():
    return CallbackModule()

def test_v2_playbook_on_handler_task_start(callback_module, mocker):
    mock_task = MockTask(name="test_task")
    mock_start_task = mocker.patch.object(callback_module, '_start_task')

    callback_module.v2_playbook_on_handler_task_start(mock_task)

    mock_start_task.assert_called_once_with(mock_task)
