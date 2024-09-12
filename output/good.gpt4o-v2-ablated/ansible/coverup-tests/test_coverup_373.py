# file: lib/ansible/plugins/callback/default.py:225-226
# asked: {"lines": [225, 226], "branches": []}
# gained: {"lines": [225, 226], "branches": []}

import pytest
from ansible.plugins.callback.default import CallbackModule
from ansible.plugins.callback import CallbackBase
from unittest.mock import Mock

@pytest.fixture
def callback_module():
    return CallbackModule()

def test_v2_playbook_on_handler_task_start(callback_module, mocker):
    mock_task = Mock()
    mock_task.name = "test_task"
    
    mock_task_start = mocker.patch.object(callback_module, '_task_start')
    
    callback_module.v2_playbook_on_handler_task_start(mock_task)
    
    mock_task_start.assert_called_once_with(mock_task, prefix='RUNNING HANDLER')
