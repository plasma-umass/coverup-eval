# file: semantic_release/hvcs.py:168-196
# asked: {"lines": [168, 169, 170, 182, 183, 184, 185, 186, 187, 188, 189, 190, 193, 194, 195, 196], "branches": []}
# gained: {"lines": [168, 169, 170, 182, 183, 184, 185, 186, 187, 188, 189, 190, 193, 194, 195, 196], "branches": []}

import pytest
from unittest.mock import patch, MagicMock
from requests import HTTPError
from semantic_release.hvcs import Github

@pytest.fixture
def mock_session_post(monkeypatch):
    mock_post = MagicMock()
    monkeypatch.setattr(Github, 'session', lambda: MagicMock(post=mock_post))
    return mock_post

def test_create_release_success(mock_session_post):
    mock_session_post.return_value.status_code = 201

    result = Github.create_release('owner', 'repo', 'v1.0.0', 'Changelog content')

    mock_session_post.assert_called_once_with(
        'https://api.github.com/repos/owner/repo/releases',
        json={
            'tag_name': 'v1.0.0',
            'name': 'v1.0.0',
            'body': 'Changelog content',
            'draft': False,
            'prerelease': False
        }
    )
    assert result is True

def test_create_release_failure(mock_session_post):
    mock_session_post.side_effect = HTTPError("Error message")

    result = Github.create_release('owner', 'repo', 'v1.0.0', 'Changelog content')

    mock_session_post.assert_called_once_with(
        'https://api.github.com/repos/owner/repo/releases',
        json={
            'tag_name': 'v1.0.0',
            'name': 'v1.0.0',
            'body': 'Changelog content',
            'draft': False,
            'prerelease': False
        }
    )
    assert result is False
