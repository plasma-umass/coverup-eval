# file lib/ansible/plugins/action/reboot.py:352-403
# lines [370, 371, 380, 382, 383]
# branches ['373->387']

import pytest
from unittest.mock import MagicMock, patch
from ansible.plugins.action.reboot import ActionModule, TimedOutException
from ansible.playbook.task import Task
from ansible.executor.task_queue_manager import TaskQueueManager

@pytest.fixture
def action_module():
    task = Task()
    task.args = {
        'reboot_timeout': 10
    }
    connection = MagicMock()
    connection.get_option = MagicMock(side_effect=KeyError)
    play_context = MagicMock()
    loader = MagicMock()
    templar = MagicMock()
    shared_loader_obj = MagicMock()
    return ActionModule(task, connection, play_context, loader, templar, shared_loader_obj)

def test_validate_reboot_keyerror(action_module):
    action_module._task.args['reboot_timeout'] = 10
    action_module._connection.get_option = MagicMock(side_effect=KeyError)
    action_module.do_until_success_or_timeout = MagicMock()
    action_module.do_until_success_or_timeout.side_effect = [None, None]

    result = action_module.validate_reboot('dummy_distribution')

    assert result['rebooted'] is True
    assert result['changed'] is True

def test_validate_reboot_connection_timeout_reset(action_module):
    action_module._task.args['reboot_timeout'] = 10
    action_module._connection.get_option = MagicMock(return_value=5)
    action_module.do_until_success_or_timeout = MagicMock()
    action_module.do_until_success_or_timeout.side_effect = [None, None]
    action_module._connection.set_option = MagicMock()
    action_module._connection.reset = MagicMock()

    result = action_module.validate_reboot('dummy_distribution', original_connection_timeout=10)

    assert result['rebooted'] is True
    assert result['changed'] is True
    action_module._connection.set_option.assert_called_with("connection_timeout", 10)
    action_module._connection.reset.assert_called_once()

def test_validate_reboot_connection_timeout_reset_exception(action_module):
    action_module._task.args['reboot_timeout'] = 10
    action_module._connection.get_option = MagicMock(return_value=5)
    action_module.do_until_success_or_timeout = MagicMock()
    action_module.do_until_success_or_timeout.side_effect = [None, None]
    action_module._connection.set_option = MagicMock(side_effect=AttributeError("Test exception"))
    action_module._connection.reset = MagicMock()

    result = action_module.validate_reboot('dummy_distribution', original_connection_timeout=10)

    assert result['rebooted'] is True
    assert result['changed'] is True
    action_module._connection.set_option.assert_called_with("connection_timeout", 10)
    action_module._connection.reset.assert_not_called()
