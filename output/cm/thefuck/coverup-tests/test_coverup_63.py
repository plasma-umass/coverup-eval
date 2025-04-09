# file thefuck/rules/git_rm_recursive.py:4-8
# lines [4, 5, 6, 7, 8]
# branches []

import pytest
from thefuck.types import Command
from thefuck.rules.git_rm_recursive import match

@pytest.fixture
def git_rm_error():
    return "fatal: not removing 'some_file' recursively without -r"

def test_match(mocker, git_rm_error):
    mocker.patch('thefuck.rules.git_rm_recursive.git_support', lambda x: x)
    command = Command('git rm some_file', git_rm_error)
    assert match(command)

def test_not_match(mocker):
    mocker.patch('thefuck.rules.git_rm_recursive.git_support', lambda x: x)
    command = Command('git rm -r some_file', "fatal: pathspec 'some_file' did not match any files")
    assert not match(command)

    command = Command('git rm some_file', 'some unrelated error')
    assert not match(command)

    command = Command('rm some_file', "fatal: not removing 'some_file' recursively without -r")
    assert not match(command)
