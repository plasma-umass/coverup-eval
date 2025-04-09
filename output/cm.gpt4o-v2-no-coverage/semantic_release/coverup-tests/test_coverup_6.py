# file: semantic_release/hvcs.py:221-243
# asked: {"lines": [221, 222, 223, 235, 236, 237, 238, 240, 241, 242, 243], "branches": []}
# gained: {"lines": [221, 222, 223, 235, 236, 237, 238, 240, 241, 242, 243], "branches": []}

import pytest
from requests import HTTPError
from unittest.mock import patch, MagicMock
from semantic_release.hvcs import Github

@pytest.fixture
def mock_logger(mocker):
    return mocker.patch('semantic_release.hvcs.logger')

@pytest.fixture
def mock_session(mocker):
    return mocker.patch('semantic_release.hvcs.Github.session')

def test_edit_release_success(mock_session, mock_logger):
    mock_post = MagicMock()
    mock_session.return_value.post = mock_post

    result = Github.edit_release('owner', 'repo', 1, 'changelog')

    mock_post.assert_called_once_with(
        'https://api.github.com/repos/owner/repo/releases/1',
        json={'body': 'changelog'}
    )
    assert result is True
    mock_logger.warning.assert_not_called()

def test_edit_release_failure(mock_session, mock_logger):
    mock_post = MagicMock()
    mock_post.side_effect = HTTPError("Error")
    mock_session.return_value.post = mock_post

    result = Github.edit_release('owner', 'repo', 1, 'changelog')

    mock_post.assert_called_once_with(
        'https://api.github.com/repos/owner/repo/releases/1',
        json={'body': 'changelog'}
    )
    assert result is False
    mock_logger.warning.assert_called_once_with('Edit release on Github has failed: Error')
