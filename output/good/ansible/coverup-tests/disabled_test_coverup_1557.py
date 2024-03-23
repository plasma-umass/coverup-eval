# file lib/ansible/plugins/action/reboot.py:235-257
# lines [236, 237, 240, 241, 242, 243, 244, 245, 246, 249, 250, 251, 252, 256, 257]
# branches ['240->241', '240->249', '256->exit', '256->257']

import pytest
from ansible.plugins.action.reboot import ActionModule
from ansible.utils.display import Display

@pytest.fixture
def mock_display(mocker):
    return mocker.patch.object(Display, 'vvv')

@pytest.fixture
def mock_connection(mocker):
    mock_conn = mocker.MagicMock()
    mock_conn.set_option = mocker.MagicMock()
    mock_conn.reset = mocker.MagicMock()
    return mock_conn

@pytest.fixture
def action_module(mocker, mock_connection):
    module = ActionModule(None, None, None, None, None, None)
    module._task = mocker.MagicMock()
    module._task.action = 'test_action'
    module._task.args = {'connect_timeout': 10}
    module._connection = mock_connection
    return module

def test_check_boot_time_exception(mocker, action_module, mock_display):
    mocker.patch.object(action_module, 'get_system_boot_time', side_effect=Exception("Test Exception"))
    with pytest.raises(Exception) as excinfo:
        action_module.check_boot_time('distribution', 'previous_boot_time')
    assert str(excinfo.value) == "Test Exception"
    mock_display.assert_called_once()

def test_check_boot_time_no_change(mocker, action_module, mock_display):
    mocker.patch.object(action_module, 'get_system_boot_time', return_value='previous_boot_time')
    with pytest.raises(ValueError) as excinfo:
        action_module.check_boot_time('distribution', 'previous_boot_time')
    assert str(excinfo.value) == "boot time has not changed"
    mock_display.assert_called_once()

def test_check_boot_time_changed(mocker, action_module, mock_display):
    mocker.patch.object(action_module, 'get_system_boot_time', return_value='new_boot_time')
    result = action_module.check_boot_time('distribution', 'previous_boot_time')
    assert result is None
    mock_display.assert_called_once()
