# file thefuck/rules/lein_not_task.py:14-19
# lines [14, 15, 16, 17, 18, 19]
# branches []

import pytest
from thefuck.rules.lein_not_task import get_new_command
from thefuck.types import Command
from thefuck.specific.sudo import sudo_support
from unittest.mock import patch

@pytest.fixture
def mock_get_all_matched_commands(mocker):
    return mocker.patch('thefuck.rules.lein_not_task.get_all_matched_commands')

@pytest.fixture
def mock_replace_command(mocker):
    return mocker.patch('thefuck.rules.lein_not_task.replace_command')

def test_get_new_command(mock_get_all_matched_commands, mock_replace_command):
    command = Command('lein some-task', "'some-task' is not a task. Did you mean this?\nother-task")
    mock_get_all_matched_commands.return_value = ['other-task']
    mock_replace_command.return_value = 'lein other-task'

    result = get_new_command(command)

    mock_get_all_matched_commands.assert_called_once_with(command.output, 'Did you mean this?')
    mock_replace_command.assert_called_once_with(command, 'some-task', ['other-task'])
    assert result == 'lein other-task'
