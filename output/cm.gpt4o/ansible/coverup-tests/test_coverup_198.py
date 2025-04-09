# file lib/ansible/plugins/action/reboot.py:235-257
# lines [235, 236, 237, 240, 241, 242, 243, 244, 245, 246, 249, 250, 251, 252, 256, 257]
# branches ['240->241', '240->249', '256->exit', '256->257']

import pytest
from unittest.mock import MagicMock, patch
from ansible.plugins.action.reboot import ActionModule
from ansible.playbook.task import Task
from ansible.executor.task_queue_manager import TaskQueueManager

@pytest.fixture
def action_module():
    task = Task()
    task.args = {'connect_timeout': 10}
    connection = MagicMock()
    play_context = MagicMock()
    loader = MagicMock()
    templar = MagicMock()
    shared_loader_obj = MagicMock()
    return ActionModule(task, connection, play_context, loader, templar, shared_loader_obj)

def test_check_boot_time(action_module):
    action_module._task.action = 'reboot'
    action_module._connection.set_option = MagicMock()
    action_module._connection.reset = MagicMock()
    action_module.get_system_boot_time = MagicMock(return_value='')

    with patch('ansible.plugins.action.reboot.display') as mock_display:
        with pytest.raises(ValueError, match="boot time has not changed"):
            action_module.check_boot_time('linux', 'previous_boot_time')

        mock_display.vvv.assert_called_with("reboot: attempting to get system boot time")
        mock_display.debug.assert_called_with("reboot: setting connect_timeout to 10")
        action_module._connection.set_option.assert_called_with("connection_timeout", 10)
        action_module._connection.reset.assert_called_once()

def test_check_boot_time_no_connect_timeout(action_module):
    action_module._task.args = {}
    action_module._task.action = 'reboot'
    action_module.get_system_boot_time = MagicMock(return_value='new_boot_time')

    with patch('ansible.plugins.action.reboot.display') as mock_display:
        action_module.check_boot_time('linux', 'previous_boot_time')

        mock_display.vvv.assert_called_with("reboot: attempting to get system boot time")
        action_module.get_system_boot_time.assert_called_with('linux')

def test_check_boot_time_exception(action_module):
    action_module._task.action = 'reboot'
    action_module.get_system_boot_time = MagicMock(side_effect=Exception('error'))

    with patch('ansible.plugins.action.reboot.display') as mock_display:
        with pytest.raises(Exception, match='error'):
            action_module.check_boot_time('linux', 'previous_boot_time')

        mock_display.vvv.assert_called_with("reboot: attempting to get system boot time")
        action_module.get_system_boot_time.assert_called_with('linux')
