# file: lib/ansible/plugins/callback/default.py:407-415
# asked: {"lines": [407, 408, 409, 410, 411, 412, 413, 414], "branches": []}
# gained: {"lines": [407, 408, 409, 410, 411, 412, 413, 414], "branches": []}

import pytest
from unittest.mock import Mock
from ansible.plugins.callback.default import CallbackModule
from ansible import constants as C

@pytest.fixture
def callback_module():
    return CallbackModule()

def test_v2_runner_on_async_poll(callback_module, mocker):
    # Mock the result object
    result = Mock()
    result._host.get_name.return_value = 'test_host'
    result._result = {
        'ansible_job_id': '12345',
        'started': '2023-10-01T12:00:00Z',
        'finished': '2023-10-01T12:05:00Z'
    }

    # Mock the display object
    mock_display = mocker.patch.object(callback_module, '_display')
    mock_display.display = Mock()

    # Call the method
    callback_module.v2_runner_on_async_poll(result)

    # Assert the display method was called with the correct parameters
    mock_display.display.assert_called_once_with(
        'ASYNC POLL on test_host: jid=12345 started=2023-10-01T12:00:00Z finished=2023-10-01T12:05:00Z',
        color=C.COLOR_DEBUG
    )
