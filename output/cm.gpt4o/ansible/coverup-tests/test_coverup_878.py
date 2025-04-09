# file lib/ansible/plugins/callback/default.py:222-223
# lines [222, 223]
# branches []

import pytest
from unittest.mock import MagicMock
from ansible.plugins.callback.default import CallbackModule

@pytest.fixture
def callback_module():
    return CallbackModule()

def test_v2_playbook_on_cleanup_task_start(callback_module, mocker):
    task = MagicMock()
    mock_task_start = mocker.patch.object(callback_module, '_task_start')

    callback_module.v2_playbook_on_cleanup_task_start(task)

    mock_task_start.assert_called_once_with(task, prefix='CLEANUP TASK')
