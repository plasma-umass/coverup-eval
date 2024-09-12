# file: lib/ansible/plugins/action/reboot.py:259-280
# asked: {"lines": [259, 260, 261, 262, 263, 264, 265, 268, 269, 270, 271, 272, 274, 275, 276, 277, 278, 280], "branches": [[274, 275], [274, 280]]}
# gained: {"lines": [259, 260, 261, 262, 263, 264, 265, 268, 269, 270, 271, 272, 274, 275, 276, 277, 278, 280], "branches": [[274, 275], [274, 280]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.plugins.action.reboot import ActionModule
from ansible.module_utils._text import to_native

@pytest.fixture
def action_module():
    task = MagicMock()
    task.args = {'test_command': 'echo test'}
    task.action = 'reboot'
    connection = MagicMock()
    connection.reset = MagicMock()
    play_context = MagicMock()
    loader = MagicMock()
    templar = MagicMock()
    shared_loader_obj = MagicMock()
    module = ActionModule(task, connection, play_context, loader, templar, shared_loader_obj)
    module.TEST_COMMANDS = {
        'test_distribution': 'echo test',
        'DEFAULT_TEST_COMMAND': 'echo default'
    }
    return module

def test_run_test_command_success(action_module):
    with patch.object(action_module, '_low_level_execute_command', return_value={'rc': 0, 'stdout': 'success', 'stderr': ''}):
        action_module.run_test_command({'name': 'test_distribution', 'version': '', 'family': ''})
        action_module._low_level_execute_command.assert_called_once_with('echo test', sudoable=action_module.DEFAULT_SUDOABLE)

def test_run_test_command_failure(action_module):
    with patch.object(action_module, '_low_level_execute_command', return_value={'rc': 1, 'stdout': 'failure', 'stderr': 'error'}):
        with pytest.raises(RuntimeError, match='Test command failed: error failure'):
            action_module.run_test_command({'name': 'test_distribution', 'version': '', 'family': ''})

def test_run_test_command_exception(action_module):
    with patch.object(action_module, '_low_level_execute_command', side_effect=Exception('test exception')):
        with pytest.raises(Exception, match='test exception'):
            action_module.run_test_command({'name': 'test_distribution', 'version': '', 'family': ''})
        action_module._connection.reset.assert_called_once()

def test_run_test_command_exception_no_reset(action_module):
    action_module._connection = None
    with patch.object(action_module, '_low_level_execute_command', side_effect=Exception('test exception')):
        with pytest.raises(Exception, match='test exception'):
            action_module.run_test_command({'name': 'test_distribution', 'version': '', 'family': ''})
