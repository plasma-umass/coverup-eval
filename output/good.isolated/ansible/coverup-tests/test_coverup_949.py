# file lib/ansible/plugins/callback/default.py:222-223
# lines [222, 223]
# branches []

# test_default_callback.py

import pytest
from ansible.plugins.callback.default import CallbackModule
from ansible.playbook.task import Task
from unittest.mock import MagicMock

@pytest.fixture
def callback_module():
    return CallbackModule()

@pytest.fixture
def mock_task():
    task = MagicMock(spec=Task)
    task.get_name.return_value = "cleanup_task"
    return task

def test_v2_playbook_on_cleanup_task_start(callback_module, mock_task, mocker):
    mocker.patch.object(callback_module, '_task_start')
    callback_module.v2_playbook_on_cleanup_task_start(mock_task)
    callback_module._task_start.assert_called_once_with(mock_task, prefix='CLEANUP TASK')
