# file thefuck/rules/lein_not_task.py:14-19
# lines [14, 15, 16, 17, 18, 19]
# branches []

import pytest
from thefuck.types import Command
from thefuck.rules.lein_not_task import get_new_command
from thefuck.rules.lein_not_task import match
from unittest.mock import Mock

@pytest.fixture
def lein_not_task_output():
    return """'foo' is not a task. See 'lein help'.
    Did you mean this?
        do"""

@pytest.fixture
def lein_not_task_command(lein_not_task_output):
    return Command('lein foo', lein_not_task_output)

def test_get_new_command(mocker, lein_not_task_command):
    mock_get_all_matched_commands = mocker.patch('thefuck.rules.lein_not_task.get_all_matched_commands', return_value=['do'])
    mock_replace_command = mocker.patch('thefuck.rules.lein_not_task.replace_command', return_value='lein do')

    new_command = get_new_command(lein_not_task_command)

    assert new_command == 'lein do'
    mock_get_all_matched_commands.assert_called_once_with(lein_not_task_command.output, 'Did you mean this?')
    mock_replace_command.assert_called_once_with(lein_not_task_command, 'foo', ['do'])

def test_match(mocker, lein_not_task_output):
    mocker.patch('thefuck.rules.lein_not_task.get_all_matched_commands', return_value=['do'])
    command = Command('lein foo', lein_not_task_output)
    assert match(command)
