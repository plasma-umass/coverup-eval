# file semantic_release/hvcs.py:168-196
# lines [168, 169, 170, 182, 183, 184, 185, 186, 187, 188, 189, 190, 193, 194, 195, 196]
# branches []

import pytest
from unittest.mock import patch, MagicMock
from requests.exceptions import HTTPError
from semantic_release.hvcs import Github

@pytest.fixture
def mock_github_session(mocker):
    mock_session = mocker.patch('semantic_release.hvcs.Github.session', autospec=True)
    return mock_session

def test_github_create_release_success(mock_github_session):
    mock_post = mock_github_session.return_value.post
    mock_post.return_value.status_code = 201

    result = Github.create_release('owner', 'repo', 'v1.0.0', 'Initial release')

    mock_post.assert_called_once_with(
        'https://api.github.com/repos/owner/repo/releases',
        json={
            'tag_name': 'v1.0.0',
            'name': 'v1.0.0',
            'body': 'Initial release',
            'draft': False,
            'prerelease': False,
        }
    )
    assert result is True

def test_github_create_release_failure(mock_github_session):
    mock_post = mock_github_session.return_value.post
    mock_post.side_effect = HTTPError("Error creating release")

    result = Github.create_release('owner', 'repo', 'v1.0.0', 'Initial release')

    mock_post.assert_called_once_with(
        'https://api.github.com/repos/owner/repo/releases',
        json={
            'tag_name': 'v1.0.0',
            'name': 'v1.0.0',
            'body': 'Initial release',
            'draft': False,
            'prerelease': False,
        }
    )
    assert result is False
