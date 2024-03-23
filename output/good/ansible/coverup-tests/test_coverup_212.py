# file lib/ansible/plugins/action/reboot.py:259-280
# lines [259, 260, 261, 262, 263, 264, 265, 268, 269, 270, 271, 272, 274, 275, 276, 277, 278, 280]
# branches ['274->275', '274->280']

import pytest
from ansible.plugins.action import reboot
from ansible.utils.display import Display
from ansible.errors import AnsibleError
from ansible.module_utils._text import to_native

# Mock the Display class to prevent actual output during tests
@pytest.fixture
def mock_display(mocker):
    return mocker.patch.object(reboot, 'display', Display())

# Mock the ActionModule class to isolate the run_test_command method
@pytest.fixture
def action_module(mocker, mock_display):
    mocker.patch.multiple(reboot.ActionBase, __abstractmethods__=set())
    action_module = reboot.ActionModule(None, None, None, None, None, None)
    action_module._task = mocker.MagicMock()
    action_module._task.action = 'test_action'
    action_module._task.args = {}
    action_module._low_level_execute_command = mocker.MagicMock()
    action_module._connection = mocker.MagicMock()
    action_module._get_value_from_facts = mocker.MagicMock(return_value='echo "System is up!"')
    return action_module

def test_run_test_command_success(action_module):
    # Mock the command result to simulate a successful test command
    action_module._low_level_execute_command.return_value = {'rc': 0, 'stdout': 'success', 'stderr': ''}
    
    # Run the test command
    action_module.run_test_command(distribution={'name': 'TestOS', 'version': '1.0', 'family': 'TestFamily'})
    
    # Assert that the command was executed
    action_module._low_level_execute_command.assert_called_once()
    
    # Assert that no exception was raised
    assert action_module._connection.reset.call_count == 0

def test_run_test_command_failure(action_module):
    # Mock the command result to simulate a failed test command
    action_module._low_level_execute_command.return_value = {'rc': 1, 'stdout': '', 'stderr': 'error'}
    
    # Run the test command and expect a RuntimeError
    with pytest.raises(RuntimeError) as excinfo:
        action_module.run_test_command(distribution={'name': 'TestOS', 'version': '1.0', 'family': 'TestFamily'})
    
    # Assert that the exception message matches the expected output
    assert 'Test command failed: error ' in str(excinfo.value)

def test_run_test_command_exception_and_reset(action_module):
    # Mock the command execution to raise an exception
    action_module._low_level_execute_command.side_effect = AnsibleError('An error occurred')
    
    # Run the test command and expect an AnsibleError
    with pytest.raises(AnsibleError):
        action_module.run_test_command(distribution={'name': 'TestOS', 'version': '1.0', 'family': 'TestFamily'})
    
    # Assert that the connection reset was attempted
    action_module._connection.reset.assert_called_once()

def test_run_test_command_exception_without_reset(action_module):
    # Mock the command execution to raise an exception
    action_module._low_level_execute_command.side_effect = AnsibleError('An error occurred')
    # Remove the reset attribute to simulate an AttributeError
    del action_module._connection.reset
    
    # Run the test command and expect an AnsibleError
    with pytest.raises(AnsibleError):
        action_module.run_test_command(distribution={'name': 'TestOS', 'version': '1.0', 'family': 'TestFamily'})
    
    # Assert that no AttributeError was raised
    assert 'reset' not in dir(action_module._connection)
