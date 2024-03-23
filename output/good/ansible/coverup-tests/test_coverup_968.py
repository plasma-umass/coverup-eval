# file lib/ansible/plugins/callback/default.py:225-226
# lines [225, 226]
# branches []

# test_default_callback.py
import pytest
from ansible.plugins.callback.default import CallbackModule
from ansible.executor.task_result import TaskResult
from unittest.mock import MagicMock

@pytest.fixture
def callback_module(mocker):
    mocker.patch('ansible.plugins.callback.CallbackBase._dump_results', return_value='')
    return CallbackModule()

def test_v2_playbook_on_handler_task_start(callback_module, mocker):
    fake_task = MagicMock()
    fake_task.get_name.return_value = "fake_task_name"
    mocker.patch.object(callback_module, '_task_start', return_value=None)
    callback_module.v2_playbook_on_handler_task_start(fake_task)
    callback_module._task_start.assert_called_once_with(fake_task, prefix='RUNNING HANDLER')
