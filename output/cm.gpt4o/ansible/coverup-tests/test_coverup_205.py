# file lib/ansible/plugins/action/reboot.py:259-280
# lines [259, 260, 261, 262, 263, 264, 265, 268, 269, 270, 271, 272, 274, 275, 276, 277, 278, 280]
# branches ['274->275', '274->280']

import pytest
from unittest.mock import MagicMock, patch
from ansible.plugins.action.reboot import ActionModule
from ansible.errors import AnsibleError

@pytest.fixture
def action_module():
    task = MagicMock()
    task.args = {'test_command': 'echo "test"'}
    task.action = 'reboot'
    connection = MagicMock()
    connection.reset = MagicMock()
    play_context = MagicMock()
    loader = MagicMock()
    templar = MagicMock()
    shared_loader_obj = MagicMock()
    return ActionModule(task, connection, play_context, loader, templar, shared_loader_obj)

def test_run_test_command_success(action_module):
    action_module._low_level_execute_command = MagicMock(return_value={'rc': 0, 'stderr': '', 'stdout': 'success'})
    action_module._get_value_from_facts = MagicMock(return_value='echo "test"')
    action_module._task.args = {'test_command': 'echo "test"'}

    action_module.run_test_command('dummy_distribution')

    action_module._low_level_execute_command.assert_called_once_with('echo "test"', sudoable=action_module.DEFAULT_SUDOABLE)

def test_run_test_command_failure(action_module):
    action_module._low_level_execute_command = MagicMock(return_value={'rc': 1, 'stderr': 'error', 'stdout': 'failure'})
    action_module._get_value_from_facts = MagicMock(return_value='echo "test"')
    action_module._task.args = {'test_command': 'echo "test"'}

    with pytest.raises(RuntimeError, match='Test command failed: error failure'):
        action_module.run_test_command('dummy_distribution')

    action_module._low_level_execute_command.assert_called_once_with('echo "test"', sudoable=action_module.DEFAULT_SUDOABLE)

def test_run_test_command_exception(action_module):
    action_module._low_level_execute_command = MagicMock(side_effect=Exception('command error'))
    action_module._get_value_from_facts = MagicMock(return_value='echo "test"')
    action_module._task.args = {'test_command': 'echo "test"'}

    with pytest.raises(Exception, match='command error'):
        action_module.run_test_command('dummy_distribution')

    action_module._low_level_execute_command.assert_called_once_with('echo "test"', sudoable=action_module.DEFAULT_SUDOABLE)
    action_module._connection.reset.assert_called_once()
