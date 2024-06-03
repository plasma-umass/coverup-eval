# file thefuck/rules/dirty_unzip.py:40-42
# lines [40, 41, 42]
# branches []

import pytest
from thefuck.rules.dirty_unzip import get_new_command
from thefuck.types import Command
import shlex as shell

def _zip_file(command):
    return command.script.split()[-1]

@pytest.fixture
def mock_command():
    return Command(script='unzip dirty.zip', output='')

def test_get_new_command(mock_command):
    new_command = get_new_command(mock_command)
    expected_command = 'unzip dirty.zip -d {}'.format(shell.quote('dirty'))
    assert new_command == expected_command
