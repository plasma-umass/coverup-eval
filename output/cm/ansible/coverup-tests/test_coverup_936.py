# file lib/ansible/plugins/callback/junit.py:289-290
# lines [289, 290]
# branches []

# test_junit.py

import pytest
from ansible.plugins.callback import junit
from ansible.playbook.task import Task
from unittest.mock import MagicMock

@pytest.fixture
def junit_callback():
    callback = junit.CallbackModule()
    callback._start_task = MagicMock()
    return callback

def test_v2_playbook_on_cleanup_task_start(junit_callback):
    fake_task = Task()
    fake_task.name = "cleanup_task"

    junit_callback.v2_playbook_on_cleanup_task_start(fake_task)

    junit_callback._start_task.assert_called_once_with(fake_task)
