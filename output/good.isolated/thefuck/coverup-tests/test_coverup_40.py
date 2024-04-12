# file thefuck/rules/git_rm_recursive.py:11-16
# lines [11, 12, 13, 14, 15, 16]
# branches []

import pytest
from thefuck.types import Command
from thefuck.rules.git_rm_recursive import get_new_command
from thefuck.specific.git import git_support

@pytest.fixture
def git_rm_command(mocker):
    mocker.patch('thefuck.specific.git.git_support', lambda x: x)
    return Command('git rm some-file', '')

def test_get_new_command_with_rm(git_rm_command):
    new_command = get_new_command(git_rm_command)
    assert new_command == 'git rm -r some-file'
