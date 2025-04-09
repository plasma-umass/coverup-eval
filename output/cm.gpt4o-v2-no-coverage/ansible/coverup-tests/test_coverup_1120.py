# file: lib/ansible/plugins/action/reboot.py:259-280
# asked: {"lines": [260, 261, 262, 263, 264, 265, 268, 269, 270, 271, 272, 274, 275, 276, 277, 278, 280], "branches": [[274, 275], [274, 280]]}
# gained: {"lines": [260, 261, 262, 263, 264, 265, 268, 269, 270, 271, 272, 274, 275, 276, 277, 278, 280], "branches": [[274, 275], [274, 280]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.plugins.action.reboot import ActionModule
from ansible.module_utils._text import to_native

@pytest.fixture
def action_module():
    task = MagicMock()
    task.args = {'test_command': 'echo test'}
    connection = MagicMock()
    play_context = MagicMock()
    loader = MagicMock()
    templar = MagicMock()
    shared_loader_obj = MagicMock()
    return ActionModule(task, connection, play_context, loader, templar, shared_loader_obj)

def test_run_test_command_success(action_module):
    action_module._low_level_execute_command = MagicMock(return_value={'rc': 0, 'stdout': 'output', 'stderr': 'error'})
    action_module._task.action = 'reboot'
    action_module.run_test_command({'name': 'test', 'version': '1.0', 'family': 'test_family'})
    action_module._low_level_execute_command.assert_called_once_with('echo test', sudoable=True)

def test_run_test_command_failure(action_module):
    action_module._low_level_execute_command = MagicMock(return_value={'rc': 1, 'stdout': 'output', 'stderr': 'error'})
    action_module._task.action = 'reboot'
    with pytest.raises(RuntimeError, match='Test command failed: error output'):
        action_module.run_test_command({'name': 'test', 'version': '1.0', 'family': 'test_family'})

def test_run_test_command_exception(action_module):
    action_module._low_level_execute_command = MagicMock(side_effect=Exception('test exception'))
    action_module._connection.reset = MagicMock()
    action_module._task.action = 'reboot'
    with pytest.raises(Exception, match='test exception'):
        action_module.run_test_command({'name': 'test', 'version': '1.0', 'family': 'test_family'})
    action_module._connection.reset.assert_called_once()

def test_run_test_command_exception_no_reset(action_module):
    action_module._low_level_execute_command = MagicMock(side_effect=Exception('test exception'))
    del action_module._connection.reset
    action_module._task.action = 'reboot'
    with pytest.raises(Exception, match='test exception'):
        action_module.run_test_command({'name': 'test', 'version': '1.0', 'family': 'test_family'})
