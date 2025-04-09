# file thefuck/rules/git_commit_reset.py:4-6
# lines [4, 5, 6]
# branches []

import pytest
from thefuck.types import Command
from thefuck.rules.git_commit_reset import match
from unittest.mock import Mock

@pytest.fixture
def git_script_parts(mocker):
    mocker.patch('thefuck.rules.git_commit_reset.git_support', return_value=lambda x: x)

def test_match_commit_in_script_parts(git_script_parts):
    command = Command('git commit -m "Initial commit"', '')
    assert match(command)

def test_not_match_commit_in_script_parts(git_script_parts):
    command = Command('git status', '')
    assert not match(command)
