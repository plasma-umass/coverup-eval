# file: lib/ansible/plugins/callback/junit.py:289-290
# asked: {"lines": [289, 290], "branches": []}
# gained: {"lines": [289, 290], "branches": []}

import pytest
from unittest.mock import Mock
from ansible.plugins.callback.junit import CallbackModule

@pytest.fixture
def callback_module():
    return CallbackModule()

def test_v2_playbook_on_cleanup_task_start(callback_module, mocker):
    mock_task = Mock()
    mock_start_task = mocker.patch.object(callback_module, '_start_task')

    callback_module.v2_playbook_on_cleanup_task_start(mock_task)

    mock_start_task.assert_called_once_with(mock_task)
