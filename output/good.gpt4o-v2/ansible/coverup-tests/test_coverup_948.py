# file: lib/ansible/plugins/callback/junit.py:283-284
# asked: {"lines": [283, 284], "branches": []}
# gained: {"lines": [283, 284], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.plugins.callback.junit import CallbackModule

@pytest.fixture
def callback_module():
    return CallbackModule()

def test_v2_runner_on_no_hosts(callback_module, mocker):
    task = MagicMock()
    mock_start_task = mocker.patch.object(callback_module, '_start_task')

    callback_module.v2_runner_on_no_hosts(task)

    mock_start_task.assert_called_once_with(task)
