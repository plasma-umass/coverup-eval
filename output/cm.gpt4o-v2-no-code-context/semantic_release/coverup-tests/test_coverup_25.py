# file: semantic_release/hvcs.py:245-272
# asked: {"lines": [245, 246, 247, 259, 260, 261, 263, 264, 265, 266, 267, 268, 270, 272], "branches": [[263, 264], [263, 272], [266, 267], [266, 270]]}
# gained: {"lines": [245, 246, 247, 259, 260, 261, 263, 264, 265, 266, 267, 268, 270, 272], "branches": [[263, 264], [263, 272], [266, 267], [266, 270]]}

import pytest
from unittest.mock import patch, MagicMock
from semantic_release.hvcs import Github

@pytest.fixture
def mock_logger(mocker):
    return mocker.patch('semantic_release.hvcs.logger')

@pytest.fixture
def mock_create_release(mocker):
    return mocker.patch('semantic_release.hvcs.Github.create_release')

@pytest.fixture
def mock_get_release(mocker):
    return mocker.patch('semantic_release.hvcs.Github.get_release')

@pytest.fixture
def mock_edit_release(mocker):
    return mocker.patch('semantic_release.hvcs.Github.edit_release')

def test_post_release_changelog_success(mock_logger, mock_create_release):
    mock_create_release.return_value = True
    result = Github.post_release_changelog('owner', 'repo', '1.0.0', 'changelog')
    assert result is True
    mock_logger.debug.assert_called_with('Attempting to create release for v1.0.0')

def test_post_release_changelog_create_fails_no_existing_release(mock_logger, mock_create_release, mock_get_release):
    mock_create_release.return_value = False
    mock_get_release.return_value = None
    result = Github.post_release_changelog('owner', 'repo', '1.0.0', 'changelog')
    assert result is False
    mock_logger.debug.assert_any_call('Unsuccessful, looking for an existing release to update')
    mock_logger.debug.assert_any_call('Existing release not found')

def test_post_release_changelog_create_fails_existing_release_update_success(mock_logger, mock_create_release, mock_get_release, mock_edit_release):
    mock_create_release.return_value = False
    mock_get_release.return_value = 'release_id'
    mock_edit_release.return_value = True
    result = Github.post_release_changelog('owner', 'repo', '1.0.0', 'changelog')
    assert result is True
    mock_logger.debug.assert_any_call('Unsuccessful, looking for an existing release to update')
    mock_logger.debug.assert_any_call('Updating release release_id')

def test_post_release_changelog_create_fails_existing_release_update_fails(mock_logger, mock_create_release, mock_get_release, mock_edit_release):
    mock_create_release.return_value = False
    mock_get_release.return_value = 'release_id'
    mock_edit_release.return_value = False
    result = Github.post_release_changelog('owner', 'repo', '1.0.0', 'changelog')
    assert result is False
    mock_logger.debug.assert_any_call('Unsuccessful, looking for an existing release to update')
    mock_logger.debug.assert_any_call('Updating release release_id')
