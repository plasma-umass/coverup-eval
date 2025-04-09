# file thefuck/rules/sudo_command_from_user_path.py:5-8
# lines [5, 6, 7, 8]
# branches ['7->exit', '7->8']

import pytest
from thefuck.types import Command
from thefuck.rules.sudo_command_from_user_path import _get_command_name
import re

@pytest.fixture
def mock_command(mocker):
    return mocker.Mock(spec=Command)

def test_get_command_name_with_sudo_not_found(mock_command):
    mock_command.output = "sudo: example: command not found"
    assert _get_command_name(mock_command) == "example"

def test_get_command_name_without_sudo_not_found(mock_command):
    mock_command.output = "example: command not found"
    assert _get_command_name(mock_command) is None
