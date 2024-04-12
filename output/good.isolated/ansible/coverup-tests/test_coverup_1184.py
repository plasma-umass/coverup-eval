# file lib/ansible/plugins/action/reboot.py:235-257
# lines [236, 237, 240, 241, 242, 243, 244, 245, 246, 249, 250, 251, 252, 256, 257]
# branches ['240->241', '240->249', '256->exit', '256->257']

import pytest
from ansible.plugins.action.reboot import ActionModule
from ansible.utils.display import Display

# Mock the Display class to prevent actual output during tests
@pytest.fixture
def mock_display(mocker):
    return mocker.patch.object(Display, 'vvv')

@pytest.fixture
def mock_debug(mocker):
    return mocker.patch.object(Display, 'debug')

@pytest.fixture
def mock_warning(mocker):
    return mocker.patch.object(Display, 'warning')

@pytest.fixture
def mock_connection(mocker):
    connection_mock = mocker.MagicMock()
    connection_mock.set_option.side_effect = AttributeError
    return connection_mock

@pytest.fixture
def mock_action_module(mocker, mock_connection):
    action_module = ActionModule(None, None, None, None, None, None)
    mocker.patch.object(action_module, '_connection', mock_connection)
    mocker.patch.object(action_module, '_task', mocker.MagicMock(args={'connect_timeout': 10}))
    mocker.patch.object(action_module, 'get_system_boot_time', return_value='')
    return action_module

def test_check_boot_time_exception(mock_action_module, mock_display, mock_debug, mock_warning):
    with pytest.raises(ValueError) as excinfo:
        mock_action_module.check_boot_time('distribution', 'previous_boot_time')
    assert "boot time has not changed" in str(excinfo.value)
    mock_display.assert_called_once()
    mock_debug.assert_called_once()
    mock_warning.assert_called_once()
