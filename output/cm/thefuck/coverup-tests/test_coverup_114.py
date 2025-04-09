# file thefuck/rules/git_add_force.py:11-13
# lines [11, 12, 13]
# branches []

import pytest
from thefuck.types import Command
from thefuck.rules.git_add_force import get_new_command
from thefuck.specific.git import git_support

@pytest.fixture
def git_add_command():
    return Command('git add file.txt', '')

@pytest.fixture
def git_commit_command():
    return Command('git commit -m "message"', '')

def test_get_new_command_with_git_add(mocker, git_add_command):
    mocker.patch('thefuck.specific.git.git_support', return_value=True)
    new_command = get_new_command(git_add_command)
    assert new_command == 'git add --force file.txt'

def test_get_new_command_with_non_git_add(mocker, git_commit_command):
    mocker.patch('thefuck.specific.git.git_support', return_value=False)
    new_command = get_new_command(git_commit_command)
    assert new_command == git_commit_command.script
