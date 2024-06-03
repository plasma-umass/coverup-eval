# file thefuck/rules/git_diff_no_index.py:14-16
# lines [14, 15, 16]
# branches []

import pytest
from thefuck.rules.git_diff_no_index import get_new_command
from thefuck.types import Command
from unittest.mock import patch

def test_get_new_command():
    command = Command('git diff file1 file2', '')
    new_command = get_new_command(command)
    assert new_command == 'git diff --no-index file1 file2'

@pytest.fixture(autouse=True)
def mock_git_support(mocker):
    mocker.patch('thefuck.rules.git_diff_no_index.git_support', lambda x: x)
