# file thefuck/rules/cp_create_destination.py:14-15
# lines [14, 15]
# branches []

import pytest
from unittest.mock import Mock
from thefuck.rules.cp_create_destination import get_new_command
from thefuck.shells import shell

def test_get_new_command(mocker):
    # Mock the command object
    command = Mock()
    command.script = "cp file.txt /nonexistent/directory/"
    command.script_parts = ["cp", "file.txt", "/nonexistent/directory/"]

    # Mock the shell.and_ method
    mocker.patch('thefuck.shells.shell.and_', return_value="mkdir -p /nonexistent/directory/ && cp file.txt /nonexistent/directory/")

    # Call the function
    new_command = get_new_command(command)

    # Assert the expected new command
    assert new_command == "mkdir -p /nonexistent/directory/ && cp file.txt /nonexistent/directory/"

    # Clean up
    mocker.stopall()
