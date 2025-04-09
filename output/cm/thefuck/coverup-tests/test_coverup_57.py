# file thefuck/rules/git_add_force.py:5-8
# lines [5, 6, 7, 8]
# branches []

import pytest
from thefuck.types import Command
from thefuck.rules.git_add_force import match
from unittest.mock import Mock

@pytest.fixture
def git_add_command():
    return Command('git add file.txt', 'The following paths are ignored by one of your .gitignore files:\nfile.txt\nUse -f if you really want to add them.')

@pytest.fixture
def git_add_command_without_error():
    return Command('git add file.txt', '')

def test_match_with_error_message(git_add_command):
    assert match(git_add_command)

def test_match_without_error_message(git_add_command_without_error):
    assert not match(git_add_command_without_error)
