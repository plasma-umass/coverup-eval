# file lib/ansible/plugins/callback/junit.py:304-305
# lines [304, 305]
# branches []

# test_junit.py

import pytest
from ansible.plugins.callback import junit
from ansible.executor.task_result import TaskResult
from unittest.mock import MagicMock

@pytest.fixture
def callback_module():
    junit_plugin = junit.CallbackModule()
    junit_plugin._finish_task = MagicMock()
    return junit_plugin

def test_v2_runner_on_skipped(callback_module):
    fake_result = TaskResult(host='localhost', task=MagicMock(), return_data={})
    
    callback_module.v2_runner_on_skipped(fake_result)
    
    callback_module._finish_task.assert_called_once_with('skipped', fake_result)
