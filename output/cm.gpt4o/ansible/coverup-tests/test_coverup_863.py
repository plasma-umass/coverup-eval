# file lib/ansible/plugins/callback/junit.py:289-290
# lines [289, 290]
# branches []

import pytest
from unittest.mock import MagicMock
from ansible.plugins.callback import CallbackBase
from ansible.plugins.callback.junit import CallbackModule

@pytest.fixture
def mock_task():
    return MagicMock()

@pytest.fixture
def callback_module():
    return CallbackModule()

def test_v2_playbook_on_cleanup_task_start(callback_module, mock_task):
    # Mock the _start_task method
    callback_module._start_task = MagicMock()

    # Call the method to be tested
    callback_module.v2_playbook_on_cleanup_task_start(mock_task)

    # Assert that _start_task was called with the correct argument
    callback_module._start_task.assert_called_once_with(mock_task)
