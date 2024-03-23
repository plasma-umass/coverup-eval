# file thefuck/rules/git_diff_no_index.py:5-11
# lines [5, 6, 7, 8, 9, 10, 11]
# branches []

import pytest
from thefuck.types import Command
from thefuck.rules.git_diff_no_index import match
from unittest.mock import Mock

@pytest.fixture
def git_diff_no_index(mocker):
    mocker.patch('thefuck.rules.git_diff_no_index.git_support', lambda x: x)

def test_match_with_diff_no_index(git_diff_no_index):
    command = Command('git diff --no-index file1 file2', '')
    assert not match(command)

def test_match_with_diff_two_files(git_diff_no_index):
    command = Command('git diff file1 file2', '')
    assert match(command)

def test_match_with_diff_one_file(git_diff_no_index):
    command = Command('git diff file1', '')
    assert not match(command)

def test_match_with_diff_more_than_two_files(git_diff_no_index):
    command = Command('git diff file1 file2 file3', '')
    assert not match(command)

def test_match_with_diff_and_options(git_diff_no_index):
    command = Command('git diff --option file1 file2', '')
    assert match(command)

def test_match_with_non_diff_command(git_diff_no_index):
    command = Command('git log file1 file2', '')
    assert not match(command)
