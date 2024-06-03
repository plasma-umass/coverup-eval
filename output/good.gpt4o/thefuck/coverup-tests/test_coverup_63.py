# file thefuck/rules/git_add_force.py:11-13
# lines [11, 12, 13]
# branches []

import pytest
from thefuck.rules.git_add_force import get_new_command
from thefuck.types import Command
from unittest.mock import patch

@pytest.fixture
def mock_git_support(mocker):
    return mocker.patch('thefuck.rules.git_add_force.git_support', lambda x: x)

def test_get_new_command(mock_git_support):
    command = Command('git add file.txt', 'error: some error message')
    new_command = get_new_command(command)
    assert new_command == 'git add --force file.txt'
