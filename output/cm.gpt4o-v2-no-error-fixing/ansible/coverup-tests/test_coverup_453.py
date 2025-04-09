# file: lib/ansible/cli/arguments/option_helpers.py:155-158
# asked: {"lines": [155, 156, 157, 158], "branches": []}
# gained: {"lines": [155, 156, 157, 158], "branches": []}

import os
import pytest
from unittest import mock

# Mock _git_repo_info to avoid dependency on actual git repository
def mock_git_repo_info(repo_path):
    return "mocked git info"

# Import the function to be tested
from ansible.cli.arguments.option_helpers import _gitinfo

@pytest.fixture
def mock_git_repo(monkeypatch):
    # Mock the _git_repo_info function
    monkeypatch.setattr("ansible.cli.arguments.option_helpers._git_repo_info", mock_git_repo_info)

    # Create a temporary directory structure
    with mock.patch("os.path.normpath") as normpath_mock, \
         mock.patch("os.path.join") as join_mock, \
         mock.patch("os.path.dirname") as dirname_mock:
        
        normpath_mock.side_effect = lambda x: x
        join_mock.side_effect = lambda *args: "/".join(args)
        dirname_mock.return_value = "test_dir"

        yield

def test_gitinfo(mock_git_repo):
    result = _gitinfo()
    assert result == "mocked git info"
