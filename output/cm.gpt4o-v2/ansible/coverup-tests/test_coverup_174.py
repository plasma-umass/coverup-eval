# file: lib/ansible/plugins/action/reboot.py:235-257
# asked: {"lines": [235, 236, 237, 240, 241, 242, 243, 244, 245, 246, 249, 250, 251, 252, 256, 257], "branches": [[240, 241], [240, 249], [256, 0], [256, 257]]}
# gained: {"lines": [235, 236, 237, 240, 241, 242, 243, 244, 245, 246, 249, 250, 251, 252, 256, 257], "branches": [[240, 241], [240, 249], [256, 0], [256, 257]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.plugins.action.reboot import ActionModule
from ansible.errors import AnsibleError

@pytest.fixture
def action_module():
    task = MagicMock()
    task.args = {
        'connect_timeout': 10,
        'boot_time_command': 'uptime -s'
    }
    connection = MagicMock()
    connection.set_option = MagicMock()
    connection.reset = MagicMock()
    play_context = MagicMock()
    loader = MagicMock()
    templar = MagicMock()
    shared_loader_obj = MagicMock()
    return ActionModule(task, connection, play_context, loader, templar, shared_loader_obj)

def test_check_boot_time_with_connect_timeout(action_module):
    action_module.get_system_boot_time = MagicMock(return_value="2023-10-01 12:00:00")
    action_module._task.args['connect_timeout'] = 5

    action_module.check_boot_time('Linux', '2023-10-01 11:00:00')

    action_module._connection.set_option.assert_called_with("connection_timeout", 5)
    action_module._connection.reset.assert_called_once()

def test_check_boot_time_without_connect_timeout(action_module):
    action_module.get_system_boot_time = MagicMock(return_value="2023-10-01 12:00:00")
    action_module._task.args.pop('connect_timeout', None)

    action_module.check_boot_time('Linux', '2023-10-01 11:00:00')

    action_module._connection.set_option.assert_not_called()
    action_module._connection.reset.assert_not_called()

def test_check_boot_time_connection_timeout_not_overridden(action_module):
    action_module.get_system_boot_time = MagicMock(return_value="2023-10-01 12:00:00")
    action_module._connection.set_option.side_effect = AttributeError

    with patch('ansible.plugins.action.reboot.display.warning') as mock_warning:
        action_module.check_boot_time('Linux', '2023-10-01 11:00:00')
        mock_warning.assert_called_once_with("Connection plugin does not allow the connection timeout to be overridden")

def test_check_boot_time_boot_time_not_changed(action_module):
    action_module.get_system_boot_time = MagicMock(return_value="2023-10-01 11:00:00")

    with pytest.raises(ValueError, match="boot time has not changed"):
        action_module.check_boot_time('Linux', '2023-10-01 11:00:00')

def test_check_boot_time_boot_time_empty(action_module):
    action_module.get_system_boot_time = MagicMock(return_value="")

    with pytest.raises(ValueError, match="boot time has not changed"):
        action_module.check_boot_time('Linux', '2023-10-01 11:00:00')

def test_check_boot_time_exception_raised(action_module):
    action_module.get_system_boot_time = MagicMock(side_effect=Exception("Some error"))

    with pytest.raises(Exception, match="Some error"):
        action_module.check_boot_time('Linux', '2023-10-01 11:00:00')
