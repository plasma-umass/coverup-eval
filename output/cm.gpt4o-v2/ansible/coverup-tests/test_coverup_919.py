# file: lib/ansible/plugins/callback/default.py:222-223
# asked: {"lines": [222, 223], "branches": []}
# gained: {"lines": [222, 223], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.plugins.callback.default import CallbackModule

@pytest.fixture
def callback_module():
    return CallbackModule()

def test_v2_playbook_on_cleanup_task_start(callback_module):
    task = MagicMock()
    callback_module._task_start = MagicMock()

    callback_module.v2_playbook_on_cleanup_task_start(task)

    callback_module._task_start.assert_called_once_with(task, prefix='CLEANUP TASK')
