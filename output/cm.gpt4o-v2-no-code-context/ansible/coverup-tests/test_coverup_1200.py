# file: lib/ansible/plugins/action/reboot.py:352-403
# asked: {"lines": [], "branches": [[373, 387]]}
# gained: {"lines": [], "branches": [[373, 387]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.plugins.action.reboot import ActionModule
from ansible.playbook.task import Task
from ansible.executor.task_queue_manager import TaskQueueManager

@pytest.fixture
def action_module():
    task = Task()
    task.args = {
        'reboot_timeout': 30
    }
    connection = MagicMock()
    connection.get_option = MagicMock(side_effect=lambda x: 10 if x == 'connection_timeout' else None)
    play_context = MagicMock()
    loader = MagicMock()
    templar = MagicMock()
    shared_loader_obj = MagicMock()
    return ActionModule(task, connection, play_context, loader, templar, shared_loader_obj)

def test_validate_reboot_with_different_connection_timeout(action_module):
    action_module._task.args['reboot_timeout'] = 30
    action_module._connection.get_option = MagicMock(return_value=20)
    action_module._connection.set_option = MagicMock()
    action_module._connection.reset = MagicMock()

    with patch.object(action_module, 'do_until_success_or_timeout') as mock_do_until:
        mock_do_until.side_effect = [None, None]
        result = action_module.validate_reboot('some_distribution', original_connection_timeout=10)

    assert result['rebooted'] is True
    assert result['changed'] is True
    action_module._connection.set_option.assert_called_with("connection_timeout", 10)
    action_module._connection.reset.assert_called_once()

def test_validate_reboot_with_same_connection_timeout(action_module):
    action_module._task.args['reboot_timeout'] = 30
    action_module._connection.get_option = MagicMock(return_value=10)

    with patch.object(action_module, 'do_until_success_or_timeout') as mock_do_until:
        mock_do_until.side_effect = [None, None]
        result = action_module.validate_reboot('some_distribution', original_connection_timeout=10)

    assert result['rebooted'] is True
    assert result['changed'] is True
    action_module._connection.set_option.assert_not_called()
    action_module._connection.reset.assert_not_called()

def test_validate_reboot_connection_timeout_reset_failure(action_module):
    action_module._task.args['reboot_timeout'] = 30
    action_module._connection.get_option = MagicMock(return_value=20)
    action_module._connection.set_option = MagicMock(side_effect=AttributeError("Mocked error"))
    action_module._connection.reset = MagicMock()

    with patch.object(action_module, 'do_until_success_or_timeout') as mock_do_until:
        mock_do_until.side_effect = [None, None]
        result = action_module.validate_reboot('some_distribution', original_connection_timeout=10)

    assert result['rebooted'] is True
    assert result['changed'] is True
    action_module._connection.set_option.assert_called_with("connection_timeout", 10)
    action_module._connection.reset.assert_not_called()
