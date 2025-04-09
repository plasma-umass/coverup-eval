# file: lib/ansible/plugins/callback/default.py:222-223
# asked: {"lines": [222, 223], "branches": []}
# gained: {"lines": [222, 223], "branches": []}

import pytest
from ansible.plugins.callback.default import CallbackModule
from ansible.plugins.callback import CallbackBase
from unittest.mock import Mock

@pytest.fixture
def callback_module():
    return CallbackModule()

def test_v2_playbook_on_cleanup_task_start(callback_module, mocker):
    task = Mock()
    mock_task_start = mocker.patch.object(callback_module, '_task_start')

    callback_module.v2_playbook_on_cleanup_task_start(task)

    mock_task_start.assert_called_once_with(task, prefix='CLEANUP TASK')
