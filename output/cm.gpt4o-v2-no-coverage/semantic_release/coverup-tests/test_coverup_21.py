# file: semantic_release/hvcs.py:168-196
# asked: {"lines": [168, 169, 170, 182, 183, 184, 185, 186, 187, 188, 189, 190, 193, 194, 195, 196], "branches": []}
# gained: {"lines": [168, 169, 170, 182, 183, 184, 185, 186, 187, 188, 189, 190, 193, 194, 195, 196], "branches": []}

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

def test_create_release_success(mock_session, mock_logger):
    mock_post = MagicMock()
    mock_session.return_value.post = mock_post

    result = Github.create_release('owner', 'repo', 'v1.0.0', 'Changelog content')

    mock_post.assert_called_once_with(
        'https://api.github.com/repos/owner/repo/releases',
        json={
            'tag_name': 'v1.0.0',
            'name': 'v1.0.0',
            'body': 'Changelog content',
            'draft': False,
            'prerelease': False,
        }
    )
    assert result is True

def test_create_release_failure(mock_session, mock_logger):
    mock_post = MagicMock()
    mock_post.side_effect = HTTPError("Error")
    mock_session.return_value.post = mock_post

    result = Github.create_release('owner', 'repo', 'v1.0.0', 'Changelog content')

    mock_post.assert_called_once_with(
        'https://api.github.com/repos/owner/repo/releases',
        json={
            'tag_name': 'v1.0.0',
            'name': 'v1.0.0',
            'body': 'Changelog content',
            'draft': False,
            'prerelease': False,
        }
    )
    mock_logger.warning.assert_called_once_with('Release creation on Github has failed: Error')
    assert result is False
