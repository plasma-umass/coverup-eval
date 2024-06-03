# file thefuck/rules/git_commit_reset.py:9-11
# lines [9, 10, 11]
# branches []

import pytest
from thefuck.rules.git_commit_reset import get_new_command
from thefuck.types import Command
from unittest.mock import patch

@pytest.fixture
def mock_git_support(mocker):
    return mocker.patch('thefuck.rules.git_commit_reset.git_support')

def test_get_new_command(mock_git_support):
    command = Command('git commit', '')
    new_command = get_new_command(command)
    assert new_command == 'git reset HEAD~'
