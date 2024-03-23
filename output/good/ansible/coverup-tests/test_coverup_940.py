# file lib/ansible/plugins/callback/default.py:167-168
# lines [167, 168]
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
def task():
    fake_task = MagicMock(spec=Task)
    fake_task.get_name.return_value = "fake_task"
    return fake_task

def test_v2_playbook_on_task_start(callback_module, task, mocker):
    mocker.patch.object(callback_module, '_task_start')
    is_conditional = False

    callback_module.v2_playbook_on_task_start(task, is_conditional)

    callback_module._task_start.assert_called_once_with(task, prefix='TASK')
