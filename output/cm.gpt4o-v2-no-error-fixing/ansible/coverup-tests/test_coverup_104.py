# file: lib/ansible/plugins/action/reboot.py:259-280
# asked: {"lines": [259, 260, 261, 262, 263, 264, 265, 268, 269, 270, 271, 272, 274, 275, 276, 277, 278, 280], "branches": [[274, 275], [274, 280]]}
# gained: {"lines": [259, 260, 261, 262, 263, 264, 265, 268, 269, 270, 271, 272, 274, 275, 276, 277, 278, 280], "branches": [[274, 275], [274, 280]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.plugins.action.reboot import ActionModule
from ansible.module_utils._text import to_native

@pytest.fixture
def action_module():
    return ActionModule(task=MagicMock(), connection=MagicMock(), play_context=MagicMock(), loader=MagicMock(), templar=MagicMock(), shared_loader_obj=MagicMock())

def test_run_test_command_success(action_module):
    action_module._task.args = {'test_command': 'echo success'}
    action_module._low_level_execute_command = MagicMock(return_value={'rc': 0, 'stdout': 'success', 'stderr': ''})
    action_module.DEFAULT_SUDOABLE = True

    with patch('ansible.plugins.action.reboot.display.vvv'), patch('ansible.plugins.action.reboot.display.debug'):
        action_module.run_test_command(distribution={'name': 'Ubuntu', 'version': '20.04', 'family': 'Debian'})

    action_module._low_level_execute_command.assert_called_once_with('echo success', sudoable=True)

def test_run_test_command_failure(action_module):
    action_module._task.args = {'test_command': 'echo fail'}
    action_module._low_level_execute_command = MagicMock(return_value={'rc': 1, 'stdout': 'fail', 'stderr': 'error'})
    action_module.DEFAULT_SUDOABLE = True

    with patch('ansible.plugins.action.reboot.display.vvv'), patch('ansible.plugins.action.reboot.display.debug'):
        with pytest.raises(RuntimeError, match='Test command failed: error fail'):
            action_module.run_test_command(distribution={'name': 'Ubuntu', 'version': '20.04', 'family': 'Debian'})

    action_module._low_level_execute_command.assert_called_once_with('echo fail', sudoable=True)

def test_run_test_command_exception(action_module):
    action_module._task.args = {'test_command': 'echo exception'}
    action_module._low_level_execute_command = MagicMock(side_effect=Exception('command error'))
    action_module._connection.reset = MagicMock()
    action_module.DEFAULT_SUDOABLE = True

    with patch('ansible.plugins.action.reboot.display.vvv'), patch('ansible.plugins.action.reboot.display.debug'):
        with pytest.raises(Exception, match='command error'):
            action_module.run_test_command(distribution={'name': 'Ubuntu', 'version': '20.04', 'family': 'Debian'})

    action_module._low_level_execute_command.assert_called_once_with('echo exception', sudoable=True)
    action_module._connection.reset.assert_called_once()

def test_run_test_command_exception_no_reset(action_module):
    action_module._task.args = {'test_command': 'echo exception'}
    action_module._low_level_execute_command = MagicMock(side_effect=Exception('command error'))
    del action_module._connection.reset
    action_module.DEFAULT_SUDOABLE = True

    with patch('ansible.plugins.action.reboot.display.vvv'), patch('ansible.plugins.action.reboot.display.debug'):
        with pytest.raises(Exception, match='command error'):
            action_module.run_test_command(distribution={'name': 'Ubuntu', 'version': '20.04', 'family': 'Debian'})

    action_module._low_level_execute_command.assert_called_once_with('echo exception', sudoable=True)
