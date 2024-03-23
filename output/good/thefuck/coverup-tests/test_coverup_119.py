# file thefuck/rules/git_commit_reset.py:9-11
# lines [11]
# branches []

import pytest
from thefuck.types import Command
from thefuck.rules.git_commit_reset import get_new_command
from thefuck.specific.git import git_support

@pytest.fixture
def mock_git_support(mocker):
    mocker.patch('thefuck.specific.git.git_support', lambda x: x)

def test_git_commit_reset(mock_git_support):
    command = Command('git commit -m "test"', '')
    new_command = get_new_command(command)
    assert new_command == 'git reset HEAD~'
