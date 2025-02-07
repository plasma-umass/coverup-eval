# file: lib/ansible/plugins/action/reboot.py:352-403
# asked: {"lines": [], "branches": [[373, 387]]}
# gained: {"lines": [], "branches": [[373, 387]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.plugins.action.reboot import ActionModule
from ansible.errors import AnsibleError, AnsibleConnectionFailure
from ansible.module_utils._text import to_text

@pytest.fixture
def action_module():
    task = MagicMock()
    task.args = {
        'reboot_timeout': 30
    }
    connection = MagicMock()
    connection.get_option = MagicMock(return_value=10)
    play_context = MagicMock()
    loader = MagicMock()
    templar = MagicMock()
    shared_loader_obj = MagicMock()
    return ActionModule(task, connection, play_context, loader, templar, shared_loader_obj)

def test_validate_reboot_resets_connection_timeout(action_module):
    action_module._task.args['reboot_timeout'] = 5
    action_module._connection.get_option = MagicMock(side_effect=[20, 10])
    action_module._connection.set_option = MagicMock()
    action_module._connection.reset = MagicMock()
    action_module.check_boot_time = MagicMock()
    action_module.run_test_command = MagicMock()

    result = action_module.validate_reboot('dummy_distribution', original_connection_timeout=10)

    action_module._connection.set_option.assert_called_with('connection_timeout', 10)
    action_module._connection.reset.assert_called_once()
    assert result['rebooted'] is True
    assert result['changed'] is True

def test_validate_reboot_handles_reset_failure(action_module):
    action_module._task.args['reboot_timeout'] = 5
    action_module._connection.get_option = MagicMock(side_effect=[20, 10])
    action_module._connection.set_option = MagicMock(side_effect=AnsibleError("Failed to set option"))
    action_module._connection.reset = MagicMock()
    action_module.check_boot_time = MagicMock()
    action_module.run_test_command = MagicMock()

    result = action_module.validate_reboot('dummy_distribution', original_connection_timeout=10)

    action_module._connection.set_option.assert_called_with('connection_timeout', 10)
    action_module._connection.reset.assert_not_called()
    assert result['rebooted'] is True
    assert result['changed'] is True

def test_validate_reboot_executes_post_reboot_command(action_module):
    action_module._task.args['reboot_timeout'] = 5
    action_module._connection.get_option = MagicMock(return_value=10)
    action_module._connection.set_option = MagicMock()
    action_module._connection.reset = MagicMock()
    action_module.check_boot_time = MagicMock()
    action_module.run_test_command = MagicMock()

    result = action_module.validate_reboot('dummy_distribution', original_connection_timeout=10)

    action_module.run_test_command.assert_called_once()
    assert result['rebooted'] is True
    assert result['changed'] is True
