# file lib/ansible/plugins/callback/junit.py:292-293
# lines [293]
# branches []

# test_junit.py

import pytest
from ansible.plugins.callback import junit
from ansible.playbook.task import Task
from unittest.mock import MagicMock

@pytest.fixture
def junit_callback():
    junit_plugin = junit.CallbackModule()
    junit_plugin._start_task = MagicMock()
    return junit_plugin

def test_v2_playbook_on_handler_task_start(junit_callback):
    fake_task = Task()
    fake_task.action = 'fake_action'

    junit_callback.v2_playbook_on_handler_task_start(fake_task)

    junit_callback._start_task.assert_called_once_with(fake_task)
