# file: lib/ansible/plugins/callback/default.py:167-168
# asked: {"lines": [167, 168], "branches": []}
# gained: {"lines": [167, 168], "branches": []}

import pytest
from unittest.mock import Mock
from ansible.plugins.callback.default import CallbackModule

@pytest.fixture
def callback_module():
    return CallbackModule()

def test_v2_playbook_on_task_start(callback_module, mocker):
    task = Mock()
    task.get_name.return_value = "Test Task"
    task._uuid = "1234-uuid"
    
    mocker.patch.object(callback_module, '_task_start')
    mocker.patch.object(callback_module, '_play', create=True)
    callback_module._play.strategy = 'linear'
    
    callback_module.v2_playbook_on_task_start(task, is_conditional=False)
    
    callback_module._task_start.assert_called_once_with(task, prefix='TASK')
