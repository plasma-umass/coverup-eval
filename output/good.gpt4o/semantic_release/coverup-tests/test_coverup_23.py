# file semantic_release/hvcs.py:221-243
# lines [221, 222, 223, 235, 236, 237, 238, 240, 241, 242, 243]
# branches []

import pytest
from unittest.mock import patch, Mock
from requests.exceptions import HTTPError
from semantic_release.hvcs import Github

@pytest.fixture
def mock_github_session(mocker):
    mock_session = mocker.patch('semantic_release.hvcs.Github.session')
    return mock_session

@pytest.fixture
def mock_logger(mocker):
    return mocker.patch('semantic_release.hvcs.logger')

def test_edit_release_success(mock_github_session):
    mock_post = Mock()
    mock_github_session.return_value.post = mock_post

    result = Github.edit_release('owner', 'repo', 1, 'changelog')

    mock_post.assert_called_once_with(
        'https://api.github.com/repos/owner/repo/releases/1',
        json={'body': 'changelog'}
    )
    assert result is True

def test_edit_release_failure(mock_github_session, mock_logger):
    mock_post = Mock()
    mock_post.side_effect = HTTPError("Error")
    mock_github_session.return_value.post = mock_post

    result = Github.edit_release('owner', 'repo', 1, 'changelog')

    mock_post.assert_called_once_with(
        'https://api.github.com/repos/owner/repo/releases/1',
        json={'body': 'changelog'}
    )
    mock_logger.warning.assert_called_once_with("Edit release on Github has failed: Error")
    assert result is False
