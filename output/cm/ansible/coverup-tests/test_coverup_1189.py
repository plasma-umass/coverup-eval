# file lib/ansible/plugins/action/wait_for_connection.py:45-61
# lines [46, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 61]
# branches ['49->50', '49->61', '52->53', '52->54', '57->58', '57->59']

import pytest
from datetime import datetime, timedelta
from ansible.plugins.action.wait_for_connection import ActionModule
from ansible.utils.display import Display

# Define a custom exception to simulate the TimedOutException from the actual module
class TimedOutException(Exception):
    pass

@pytest.fixture
def action_module(mocker):
    mocker.patch.object(Display, 'debug')
    task = mocker.MagicMock()
    connection = mocker.MagicMock()
    play_context = mocker.MagicMock()
    loader = mocker.MagicMock()
    templar = mocker.MagicMock()
    shared_loader_obj = mocker.MagicMock()
    return ActionModule(task, connection, play_context, loader, templar, shared_loader_obj)

def test_do_until_success_or_timeout(mocker, action_module):
    mocker.patch('time.sleep', return_value=None)
    what_mock = mocker.Mock(side_effect=[Exception("temporary failure"), None])
    mocker.patch.object(action_module, '_display', Display())

    # Test that the loop retries until success
    action_module.do_until_success_or_timeout(what_mock, timeout=5, connect_timeout=1, what_desc="connection")
    what_mock.assert_called()
    assert what_mock.call_count == 2

    # Test that the loop raises TimedOutException after timeout
    what_mock = mocker.Mock(side_effect=Exception("permanent failure"))
    with pytest.raises(TimedOutException):
        action_module.do_until_success_or_timeout(what_mock, timeout=1, connect_timeout=1, what_desc="connection")
    assert what_mock.call_count > 1

# Patch the TimedOutException in the module with our custom exception for testing
@pytest.fixture(autouse=True)
def patch_exceptions(mocker):
    mocker.patch('ansible.plugins.action.wait_for_connection.TimedOutException', new=TimedOutException)
