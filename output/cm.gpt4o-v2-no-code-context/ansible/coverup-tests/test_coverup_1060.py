# file: lib/ansible/plugins/action/reboot.py:352-403
# asked: {"lines": [370, 371], "branches": [[373, 387]]}
# gained: {"lines": [370, 371], "branches": []}

import pytest
from unittest.mock import MagicMock, patch
from ansible.plugins.action.reboot import ActionModule, TimedOutException
from ansible.errors import AnsibleError

@pytest.fixture
def action_module():
    task = MagicMock()
    task.args = {'reboot_timeout': 10}
    connection = MagicMock()
    connection.get_option = MagicMock(side_effect=KeyError)
    play_context = MagicMock()
    loader = MagicMock()
    templar = MagicMock()
    shared_loader_obj = MagicMock()
    return ActionModule(task, connection, play_context, loader, templar, shared_loader_obj)

def test_validate_reboot_keyerror(action_module):
    action_module._connection.get_option = MagicMock(side_effect=KeyError)
    action_module.do_until_success_or_timeout = MagicMock()
    action_module.check_boot_time = MagicMock()
    action_module.run_test_command = MagicMock()

    result = action_module.validate_reboot(distribution='test_distribution')

    assert result['rebooted'] is True
    assert result['changed'] is True
    action_module._connection.get_option.assert_called_once_with('connection_timeout')
    action_module.do_until_success_or_timeout.assert_any_call(
        action=action_module.check_boot_time,
        action_desc="last boot time check",
        reboot_timeout=10,
        distribution='test_distribution',
        action_kwargs=None
    )
    action_module.do_until_success_or_timeout.assert_any_call(
        action=action_module.run_test_command,
        action_desc="post-reboot test command",
        reboot_timeout=10,
        distribution='test_distribution',
        action_kwargs=None
    )

def test_validate_reboot_connection_timeout_reset(action_module):
    action_module._connection.get_option = MagicMock(return_value=20)
    action_module.do_until_success_or_timeout = MagicMock()
    action_module.check_boot_time = MagicMock()
    action_module.run_test_command = MagicMock()

    result = action_module.validate_reboot(distribution='test_distribution', original_connection_timeout=10)

    assert result['rebooted'] is True
    assert result['changed'] is True
    action_module._connection.get_option.assert_called_once_with('connection_timeout')
    action_module._connection.set_option.assert_called_once_with('connection_timeout', 10)
    action_module._connection.reset.assert_called_once()
    action_module.do_until_success_or_timeout.assert_any_call(
        action=action_module.check_boot_time,
        action_desc="last boot time check",
        reboot_timeout=10,
        distribution='test_distribution',
        action_kwargs=None
    )
    action_module.do_until_success_or_timeout.assert_any_call(
        action=action_module.run_test_command,
        action_desc="post-reboot test command",
        reboot_timeout=10,
        distribution='test_distribution',
        action_kwargs=None
    )

def test_validate_reboot_connection_timeout_reset_failure(action_module):
    action_module._connection.get_option = MagicMock(return_value=20)
    action_module._connection.set_option = MagicMock(side_effect=AnsibleError("Test Error"))
    action_module.do_until_success_or_timeout = MagicMock()
    action_module.check_boot_time = MagicMock()
    action_module.run_test_command = MagicMock()

    result = action_module.validate_reboot(distribution='test_distribution', original_connection_timeout=10)

    assert result['rebooted'] is True
    assert result['changed'] is True
    action_module._connection.get_option.assert_called_once_with('connection_timeout')
    action_module._connection.set_option.assert_called_once_with('connection_timeout', 10)
    action_module._connection.reset.assert_not_called()
    action_module.do_until_success_or_timeout.assert_any_call(
        action=action_module.check_boot_time,
        action_desc="last boot time check",
        reboot_timeout=10,
        distribution='test_distribution',
        action_kwargs=None
    )
    action_module.do_until_success_or_timeout.assert_any_call(
        action=action_module.run_test_command,
        action_desc="post-reboot test command",
        reboot_timeout=10,
        distribution='test_distribution',
        action_kwargs=None
    )
