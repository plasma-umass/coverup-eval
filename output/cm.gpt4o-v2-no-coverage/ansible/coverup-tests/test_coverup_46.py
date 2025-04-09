# file: lib/ansible/plugins/action/reboot.py:352-403
# asked: {"lines": [352, 353, 354, 356, 358, 360, 361, 362, 363, 364, 365, 368, 369, 370, 371, 373, 374, 375, 376, 377, 378, 379, 380, 382, 383, 387, 388, 389, 390, 391, 392, 394, 395, 397, 398, 399, 400, 401, 403], "branches": [[373, 374], [373, 387]]}
# gained: {"lines": [352, 353, 354, 356, 358, 360, 361, 362, 363, 364, 365, 368, 369, 370, 371, 373, 374, 375, 376, 377, 378, 379, 380, 382, 383, 387, 388, 389, 390, 391, 392, 394, 395, 397, 398, 399, 400, 401, 403], "branches": [[373, 374]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.errors import AnsibleError
from ansible.plugins.action.reboot import ActionModule, TimedOutException

@pytest.fixture
def action_module():
    task = MagicMock()
    task.args = {
        'reboot_timeout': 600
    }
    connection = MagicMock()
    play_context = MagicMock()
    loader = MagicMock()
    templar = MagicMock()
    shared_loader_obj = MagicMock()
    return ActionModule(task, connection, play_context, loader, templar, shared_loader_obj)

def test_validate_reboot_success(action_module):
    action_module._task.args['reboot_timeout'] = 600
    action_module._connection.get_option = MagicMock(return_value=20)
    action_module._connection.set_option = MagicMock()
    action_module._connection.reset = MagicMock()
    action_module.do_until_success_or_timeout = MagicMock()
    
    result = action_module.validate_reboot('linux', original_connection_timeout=10)
    
    assert result['rebooted'] is True
    assert result['changed'] is True
    action_module._connection.set_option.assert_called_with("connection_timeout", 10)
    action_module._connection.reset.assert_called_once()

def test_validate_reboot_timeout(action_module):
    action_module._task.args['reboot_timeout'] = 600
    action_module.do_until_success_or_timeout = MagicMock(side_effect=TimedOutException('Timeout'))
    
    result = action_module.validate_reboot('linux', original_connection_timeout=10)
    
    assert result['failed'] is True
    assert result['rebooted'] is True
    assert 'Timeout' in result['msg']

def test_validate_reboot_connection_timeout_key_error(action_module):
    action_module._task.args['reboot_timeout'] = 600
    action_module._connection.get_option = MagicMock(side_effect=KeyError)
    action_module.do_until_success_or_timeout = MagicMock()
    
    result = action_module.validate_reboot('linux', original_connection_timeout=10)
    
    assert result['rebooted'] is True
    assert result['changed'] is True

def test_validate_reboot_connection_timeout_ansible_error(action_module):
    action_module._task.args['reboot_timeout'] = 600
    action_module._connection.get_option = MagicMock(return_value=20)
    action_module._connection.set_option = MagicMock(side_effect=AnsibleError('Error'))
    action_module._connection.reset = MagicMock()
    action_module.do_until_success_or_timeout = MagicMock()
    
    result = action_module.validate_reboot('linux', original_connection_timeout=10)
    
    assert result['rebooted'] is True
    assert result['changed'] is True
    action_module._connection.set_option.assert_called_with("connection_timeout", 10)
    action_module._connection.reset.assert_not_called()
