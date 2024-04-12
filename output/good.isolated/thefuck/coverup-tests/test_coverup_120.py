# file thefuck/rules/git_diff_no_index.py:14-16
# lines [16]
# branches []

import pytest
from thefuck.types import Command
from thefuck.rules.git_diff_no_index import get_new_command
from thefuck.specific.git import git_support

@pytest.fixture
def mock_git_support(mocker):
    mocker.patch('thefuck.specific.git.git_support', lambda x: x)

def test_get_new_command_with_diff(mock_git_support):
    command = Command('git diff file1 file2', '')
    new_command = get_new_command(command)
    assert new_command == 'git diff --no-index file1 file2'
