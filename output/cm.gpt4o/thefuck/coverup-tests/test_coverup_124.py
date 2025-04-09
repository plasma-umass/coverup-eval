# file thefuck/rules/git_rm_recursive.py:11-16
# lines [13, 14, 15, 16]
# branches []

import pytest
from thefuck.rules.git_rm_recursive import get_new_command
from thefuck.types import Command

def test_get_new_command_adds_recursive_flag():
    command = Command('git rm file.txt', ['git', 'rm', 'file.txt'])
    new_command = get_new_command(command)
    assert new_command == 'git rm -r file.txt'

@pytest.fixture
def mock_git_support(mocker):
    return mocker.patch('thefuck.rules.git_rm_recursive.git_support', lambda x: x)

def test_get_new_command_with_mocked_git_support(mock_git_support):
    command = Command('git rm file.txt', ['git', 'rm', 'file.txt'])
    new_command = get_new_command(command)
    assert new_command == 'git rm -r file.txt'
