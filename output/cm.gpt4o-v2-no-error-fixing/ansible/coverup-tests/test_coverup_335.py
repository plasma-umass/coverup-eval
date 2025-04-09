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
    result._result.get.side_effect = lambda key: {
        'ansible_job_id': '12345',
        'started': 1,
        'finished': 0
    }.get(key)

    # Mock the display object
    mock_display = Mock()
    callback_module._display = mock_display

    # Call the method
    callback_module.v2_runner_on_async_poll(result)

    # Assertions
    result._host.get_name.assert_called_once()
    result._result.get.assert_any_call('ansible_job_id')
    result._result.get.assert_any_call('started')
    result._result.get.assert_any_call('finished')
    mock_display.display.assert_called_once_with(
        'ASYNC POLL on test_host: jid=12345 started=1 finished=0',
        color=C.COLOR_DEBUG
    )
