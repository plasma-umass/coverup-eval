# file thefuck/rules/git_diff_no_index.py:5-11
# lines [5, 6, 7, 8, 9, 10, 11]
# branches []

import pytest
from thefuck.rules.git_diff_no_index import match
from thefuck.types import Command

@pytest.fixture
def mock_git_support(mocker):
    return mocker.patch('thefuck.rules.git_diff_no_index.git_support', lambda x: x)

def test_match_no_index(mock_git_support):
    command = Command('git diff file1 file2', ['git', 'diff', 'file1', 'file2'])
    assert match(command) is True

def test_match_with_no_index(mock_git_support):
    command = Command('git diff --no-index file1 file2', ['git', 'diff', '--no-index', 'file1', 'file2'])
    assert match(command) is False

def test_match_not_diff(mock_git_support):
    command = Command('git status', ['git', 'status'])
    assert match(command) is False

def test_match_insufficient_files(mock_git_support):
    command = Command('git diff file1', ['git', 'diff', 'file1'])
    assert match(command) is False
