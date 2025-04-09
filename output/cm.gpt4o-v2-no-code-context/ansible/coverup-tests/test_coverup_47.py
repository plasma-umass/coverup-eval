# file: lib/ansible/plugins/action/reboot.py:352-403
# asked: {"lines": [352, 353, 354, 356, 358, 360, 361, 362, 363, 364, 365, 368, 369, 370, 371, 373, 374, 375, 376, 377, 378, 379, 380, 382, 383, 387, 388, 389, 390, 391, 392, 394, 395, 397, 398, 399, 400, 401, 403], "branches": [[373, 374], [373, 387]]}
# gained: {"lines": [352, 353, 354, 356, 358, 360, 361, 362, 363, 364, 365, 368, 369, 373, 374, 375, 376, 377, 378, 379, 380, 382, 383, 387, 388, 389, 390, 391, 392, 394, 395, 397, 398, 399, 400, 401, 403], "branches": [[373, 374]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.plugins.action.reboot import ActionModule, TimedOutException

@pytest.fixture
def action_module():
    task = MagicMock()
    task.args = {
        'reboot_timeout': 10
    }
    connection = MagicMock()
    play_context = MagicMock()
    loader = MagicMock()
    templar = MagicMock()
    shared_loader_obj = MagicMock()
    return ActionModule(task, connection, play_context, loader, templar, shared_loader_obj)

def test_validate_reboot_success(action_module):
    action_module._task.action = 'reboot'
    action_module._connection.get_option = MagicMock(return_value=5)
    action_module._connection.set_option = MagicMock()
    action_module._connection.reset = MagicMock()
    action_module.check_boot_time = MagicMock(return_value=True)
    action_module.run_test_command = MagicMock(return_value=True)
    action_module.do_until_success_or_timeout = MagicMock()

    result = action_module.validate_reboot('linux', original_connection_timeout=10)

    assert result['rebooted'] is True
    assert result['changed'] is True
    action_module._connection.set_option.assert_called_with("connection_timeout", 10)
    action_module._connection.reset.assert_called_once()

def test_validate_reboot_timeout_exception(action_module):
    action_module._task.action = 'reboot'
    action_module._connection.get_option = MagicMock(return_value=5)
    action_module._connection.set_option = MagicMock()
    action_module._connection.reset = MagicMock()
    action_module.check_boot_time = MagicMock(return_value=True)
    action_module.run_test_command = MagicMock(return_value=True)
    action_module.do_until_success_or_timeout = MagicMock(side_effect=TimedOutException('timeout'))

    result = action_module.validate_reboot('linux', original_connection_timeout=10)

    assert result['failed'] is True
    assert result['rebooted'] is True
    assert 'timeout' in result['msg']

def test_validate_reboot_connection_timeout_reset_failure(action_module):
    action_module._task.action = 'reboot'
    action_module._connection.get_option = MagicMock(return_value=5)
    action_module._connection.set_option = MagicMock(side_effect=AttributeError('error'))
    action_module._connection.reset = MagicMock()
    action_module.check_boot_time = MagicMock(return_value=True)
    action_module.run_test_command = MagicMock(return_value=True)
    action_module.do_until_success_or_timeout = MagicMock()

    result = action_module.validate_reboot('linux', original_connection_timeout=10)

    assert result['rebooted'] is True
    assert result['changed'] is True
    action_module._connection.set_option.assert_called_with("connection_timeout", 10)
    action_module._connection.reset.assert_not_called()
