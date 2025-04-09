# file: lib/ansible/plugins/callback/default.py:407-415
# asked: {"lines": [407, 408, 409, 410, 411, 412, 413, 414], "branches": []}
# gained: {"lines": [407, 408, 409, 410, 411, 412, 413, 414], "branches": []}

import pytest
from unittest.mock import Mock, patch
from ansible.plugins.callback.default import CallbackModule
from ansible.utils.display import Display
import ansible.constants as C

@pytest.fixture
def callback_module():
    return CallbackModule()

@pytest.fixture
def mock_result():
    mock = Mock()
    mock._host.get_name.return_value = 'test_host'
    mock._result.get.side_effect = lambda key: {
        'ansible_job_id': '12345',
        'started': '2023-10-01T12:00:00Z',
        'finished': '2023-10-01T12:05:00Z'
    }.get(key)
    return mock

def test_v2_runner_on_async_poll(callback_module, mock_result, monkeypatch):
    mock_display = Mock(spec=Display)
    monkeypatch.setattr(callback_module, '_display', mock_display)

    callback_module.v2_runner_on_async_poll(mock_result)

    mock_result._host.get_name.assert_called_once()
    mock_result._result.get.assert_any_call('ansible_job_id')
    mock_result._result.get.assert_any_call('started')
    mock_result._result.get.assert_any_call('finished')
    mock_display.display.assert_called_once_with(
        'ASYNC POLL on test_host: jid=12345 started=2023-10-01T12:00:00Z finished=2023-10-01T12:05:00Z',
        color=C.COLOR_DEBUG
    )
