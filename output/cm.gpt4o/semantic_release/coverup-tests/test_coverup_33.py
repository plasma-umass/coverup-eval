# file semantic_release/hvcs.py:245-272
# lines [245, 246, 247, 259, 260, 261, 263, 264, 265, 266, 267, 268, 270, 272]
# branches ['263->264', '263->272', '266->267', '266->270']

import pytest
from unittest.mock import patch, MagicMock
from semantic_release.hvcs import Github

@pytest.fixture
def mock_logger(mocker):
    return mocker.patch('semantic_release.hvcs.logger')

@pytest.fixture
def mock_github(mocker):
    return mocker.patch('semantic_release.hvcs.Github')

def test_post_release_changelog_create_success(mock_github, mock_logger):
    mock_github.create_release.return_value = True

    result = Github.post_release_changelog('owner', 'repo', '1.0.0', 'changelog')

    assert result is True
    mock_logger.debug.assert_called_with('Attempting to create release for v1.0.0')
    mock_github.create_release.assert_called_once_with('owner', 'repo', 'v1.0.0', 'changelog')

def test_post_release_changelog_create_failure_update_success(mock_github, mock_logger):
    mock_github.create_release.return_value = False
    mock_github.get_release.return_value = 'release_id'
    mock_github.edit_release.return_value = True

    result = Github.post_release_changelog('owner', 'repo', '1.0.0', 'changelog')

    assert result is True
    mock_logger.debug.assert_any_call('Attempting to create release for v1.0.0')
    mock_logger.debug.assert_any_call('Unsuccessful, looking for an existing release to update')
    mock_logger.debug.assert_any_call('Updating release release_id')
    mock_github.create_release.assert_called_once_with('owner', 'repo', 'v1.0.0', 'changelog')
    mock_github.get_release.assert_called_once_with('owner', 'repo', 'v1.0.0')
    mock_github.edit_release.assert_called_once_with('owner', 'repo', 'release_id', 'changelog')

def test_post_release_changelog_create_failure_update_failure(mock_github, mock_logger):
    mock_github.create_release.return_value = False
    mock_github.get_release.return_value = None

    result = Github.post_release_changelog('owner', 'repo', '1.0.0', 'changelog')

    assert result is False
    mock_logger.debug.assert_any_call('Attempting to create release for v1.0.0')
    mock_logger.debug.assert_any_call('Unsuccessful, looking for an existing release to update')
    mock_logger.debug.assert_any_call('Existing release not found')
    mock_github.create_release.assert_called_once_with('owner', 'repo', 'v1.0.0', 'changelog')
    mock_github.get_release.assert_called_once_with('owner', 'repo', 'v1.0.0')
