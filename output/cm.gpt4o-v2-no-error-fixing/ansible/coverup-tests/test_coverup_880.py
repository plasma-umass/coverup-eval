# file: lib/ansible/plugins/action/reboot.py:235-257
# asked: {"lines": [236, 237, 240, 241, 242, 243, 244, 245, 246, 249, 250, 251, 252, 256, 257], "branches": [[240, 241], [240, 249], [256, 0], [256, 257]]}
# gained: {"lines": [236, 237, 240, 241, 242, 243, 244, 245, 246, 249, 250, 251, 252, 256, 257], "branches": [[240, 241], [240, 249], [256, 0], [256, 257]]}

import pytest
from unittest.mock import Mock, patch
from ansible.plugins.action.reboot import ActionModule

@pytest.fixture
def action_module():
    task = Mock()
    task.args = {
        'connect_timeout': 10
    }
    connection = Mock()
    play_context = Mock()
    loader = Mock()
    templar = Mock()
    shared_loader_obj = Mock()
    return ActionModule(task, connection, play_context, loader, templar, shared_loader_obj)

def test_check_boot_time_with_connect_timeout(action_module):
    action_module._task.args['connect_timeout'] = 10
    action_module._connection.set_option = Mock()
    action_module._connection.reset = Mock()
    action_module.get_system_boot_time = Mock(return_value="boot_time")

    action_module.check_boot_time('distribution', 'previous_boot_time')

    action_module._connection.set_option.assert_called_once_with("connection_timeout", 10)
    action_module._connection.reset.assert_called_once()

def test_check_boot_time_without_connect_timeout(action_module):
    action_module._task.args['connect_timeout'] = None
    action_module.get_system_boot_time = Mock(return_value="boot_time")

    action_module.check_boot_time('distribution', 'previous_boot_time')

    action_module._connection.set_option.assert_not_called()
    action_module._connection.reset.assert_not_called()

def test_check_boot_time_connection_timeout_not_overridden(action_module):
    action_module._task.args['connect_timeout'] = 10
    action_module._connection.set_option = Mock(side_effect=AttributeError)
    action_module._connection.reset = Mock()
    action_module.get_system_boot_time = Mock(return_value="boot_time")

    with patch('ansible.plugins.action.reboot.display.warning') as mock_warning:
        action_module.check_boot_time('distribution', 'previous_boot_time')
        mock_warning.assert_called_once_with("Connection plugin does not allow the connection timeout to be overridden")

def test_check_boot_time_exception_raised(action_module):
    action_module.get_system_boot_time = Mock(side_effect=Exception("error"))

    with pytest.raises(Exception, match="error"):
        action_module.check_boot_time('distribution', 'previous_boot_time')

def test_check_boot_time_value_error_raised(action_module):
    action_module.get_system_boot_time = Mock(return_value="previous_boot_time")

    with pytest.raises(ValueError, match="boot time has not changed"):
        action_module.check_boot_time('distribution', 'previous_boot_time')

def test_check_boot_time_empty_boot_time(action_module):
    action_module.get_system_boot_time = Mock(return_value="")

    with pytest.raises(ValueError, match="boot time has not changed"):
        action_module.check_boot_time('distribution', 'previous_boot_time')
