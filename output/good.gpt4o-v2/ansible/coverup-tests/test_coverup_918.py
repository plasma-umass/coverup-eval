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
    mock_task_start = mocker.patch.object(callback_module, '_task_start')

    callback_module.v2_playbook_on_task_start(task, is_conditional=False)

    mock_task_start.assert_called_once_with(task, prefix='TASK')
