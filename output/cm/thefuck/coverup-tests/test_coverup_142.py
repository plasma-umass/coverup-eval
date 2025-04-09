# file thefuck/rules/no_such_file.py:21-30
# lines [22, 23, 25, 26, 27, 29, 30]
# branches ['22->exit', '22->23', '25->22', '25->26']

import pytest
from thefuck.types import Command
from thefuck.rules.no_such_file import get_new_command
from thefuck.shells import shell
import re

patterns = [r"No such file or directory: '([^']+)'",
            r"No such file or directory: ([^\s]+)"]

@pytest.fixture
def no_such_file_error(mocker):
    return mocker.Mock(return_value="No such file or directory: '/nonexistent/path/to/file.txt'")

@pytest.fixture
def command(no_such_file_error):
    return Command('ls /nonexistent/path/to/file.txt', no_such_file_error())

def test_get_new_command_creates_directory_from_output(command, mocker):
    mocker.patch('thefuck.rules.no_such_file.patterns', patterns)
    mocker.patch('thefuck.shells.shell', shell)
    new_command = get_new_command(command)
    assert new_command == "mkdir -p /nonexistent/path/to && ls /nonexistent/path/to/file.txt"
