# file lib/ansible/plugins/callback/junit.py:286-287
# lines [286, 287]
# branches []

import pytest
from unittest.mock import Mock, patch
from ansible.plugins.callback import CallbackBase
from ansible.plugins.callback.junit import CallbackModule

@pytest.fixture
def mock_task():
    return Mock()

@pytest.fixture
def callback_module():
    return CallbackModule()

def test_v2_playbook_on_task_start(callback_module, mock_task):
    with patch.object(callback_module, '_start_task') as mock_start_task:
        callback_module.v2_playbook_on_task_start(mock_task, is_conditional=False)
        mock_start_task.assert_called_once_with(mock_task)
