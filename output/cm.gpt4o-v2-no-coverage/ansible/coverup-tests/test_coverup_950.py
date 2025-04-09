# file: lib/ansible/plugins/callback/junit.py:304-305
# asked: {"lines": [304, 305], "branches": []}
# gained: {"lines": [304, 305], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.plugins.callback.junit import CallbackModule

@pytest.fixture
def callback_module():
    return CallbackModule()

def test_v2_runner_on_skipped(callback_module, mocker):
    result = MagicMock()
    mock_finish_task = mocker.patch.object(callback_module, '_finish_task')

    callback_module.v2_runner_on_skipped(result)

    mock_finish_task.assert_called_once_with('skipped', result)
