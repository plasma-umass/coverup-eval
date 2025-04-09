# file lib/ansible/plugins/action/reboot.py:352-403
# lines [353, 354, 356, 358, 360, 361, 362, 363, 364, 365, 368, 369, 370, 371, 373, 374, 375, 376, 377, 378, 379, 380, 382, 383, 387, 388, 389, 390, 391, 392, 394, 395, 397, 398, 399, 400, 401, 403]
# branches ['373->374', '373->387']

import pytest
from unittest.mock import MagicMock, patch
from ansible.plugins.action.reboot import ActionModule, TimedOutException
from ansible.playbook.task import Task
from ansible.executor.task_queue_manager import TaskQueueManager

@pytest.fixture
def action_module():
    task = Task()
    task.action = 'reboot'
    task.args = {'reboot_timeout': 5}
    connection = MagicMock()
    connection.get_option = MagicMock(side_effect=KeyError)
    play_context = MagicMock()
    loader = MagicMock()
    templar = MagicMock()
    shared_loader_obj = MagicMock()
    return ActionModule(task, connection, play_context, loader, templar, shared_loader_obj)

def test_validate_reboot_success(action_module):
    action_module._task.args['reboot_timeout'] = 5
    action_module._connection.get_option = MagicMock(return_value=10)
    action_module._connection.set_option = MagicMock()
    action_module._connection.reset = MagicMock()
    action_module.check_boot_time = MagicMock()
    action_module.run_test_command = MagicMock()

    with patch('ansible.plugins.action.reboot.display') as mock_display:
        result = action_module.validate_reboot('test_distribution', original_connection_timeout=5)

    assert result['rebooted'] is True
    assert result['changed'] is True
    mock_display.vvv.assert_called_with('reboot: validating reboot')
    mock_display.debug.assert_any_call('reboot: setting connect_timeout back to original value of 5')

def test_validate_reboot_timeout(action_module):
    action_module._task.args['reboot_timeout'] = 5
    action_module.check_boot_time = MagicMock(side_effect=TimedOutException('timeout'))
    action_module.run_test_command = MagicMock()

    with patch('ansible.plugins.action.reboot.display') as mock_display:
        result = action_module.validate_reboot('test_distribution')

    assert result['failed'] is True
    assert result['rebooted'] is True
    assert 'timeout' in result['msg']
    mock_display.vvv.assert_called_with('reboot: validating reboot')
