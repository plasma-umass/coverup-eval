# file lib/ansible/plugins/callback/junit.py:301-302
# lines [302]
# branches []

import pytest
from unittest.mock import MagicMock
from ansible.plugins.callback.junit import CallbackModule

@pytest.fixture
def callback_module():
    return CallbackModule()

def test_v2_runner_on_ok(callback_module, mocker):
    result = MagicMock()
    mock_finish_task = mocker.patch.object(callback_module, '_finish_task')

    callback_module.v2_runner_on_ok(result)

    mock_finish_task.assert_called_once_with('ok', result)
