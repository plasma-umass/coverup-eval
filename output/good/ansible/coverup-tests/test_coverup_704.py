# file lib/ansible/cli/arguments/option_helpers.py:155-158
# lines [155, 156, 157, 158]
# branches []

import os
import pytest
from ansible.cli.arguments.option_helpers import _gitinfo
from unittest.mock import patch, MagicMock

# Test function to cover the _gitinfo function
def test_gitinfo(mocker):
    # Mock the _git_repo_info function
    mock_git_repo_info = mocker.patch('ansible.cli.arguments.option_helpers._git_repo_info')
    mock_git_repo_info.return_value = {'git_branch': 'main', 'git_commit': 'abc123'}

    # Mock os.path.dirname to return a specific directory
    mocker.patch('os.path.dirname', return_value='/path/to/ansible/cli/arguments/option_helpers.py')

    # Mock os.path.join to ensure it returns the expected path
    mocker.patch('os.path.join', return_value='/path/to/ansible/.git')

    # Mock os.path.normpath to ensure it returns the expected path
    mocker.patch('os.path.normpath', return_value='/path/to/ansible')

    # Call the function under test
    git_info = _gitinfo()

    # Assert that the _git_repo_info function was called with the correct path
    mock_git_repo_info.assert_called_once_with('/path/to/ansible/.git')

    # Assert that the function returns the expected result
    assert git_info == {'git_branch': 'main', 'git_commit': 'abc123'}

    # Cleanup is handled by the mocker fixture, which undoes all patches after the test
