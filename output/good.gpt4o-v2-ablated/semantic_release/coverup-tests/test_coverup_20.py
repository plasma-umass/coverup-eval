# file: semantic_release/hvcs.py:168-196
# asked: {"lines": [168, 169, 170, 182, 183, 184, 185, 186, 187, 188, 189, 190, 193, 194, 195, 196], "branches": []}
# gained: {"lines": [168, 169, 170, 182, 183, 184, 185, 186, 187, 188, 189, 190, 193, 194, 195, 196], "branches": []}

import pytest
from unittest.mock import patch, MagicMock
from requests.exceptions import HTTPError

from semantic_release.hvcs import Github

@pytest.fixture
def mock_github_session(monkeypatch):
    mock_session = MagicMock()
    monkeypatch.setattr(Github, 'session', lambda: mock_session)
    return mock_session

@pytest.fixture
def mock_github_api_url(monkeypatch):
    monkeypatch.setattr(Github, 'api_url', lambda: 'https://api.github.com')
    return 'https://api.github.com'

def test_create_release_success(mock_github_session, mock_github_api_url):
    mock_github_session.post.return_value = MagicMock(status_code=201)
    
    result = Github.create_release('owner', 'repo', 'v1.0.0', 'Changelog content')
    
    mock_github_session.post.assert_called_once_with(
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

def test_create_release_failure(mock_github_session, mock_github_api_url):
    mock_github_session.post.side_effect = HTTPError("Error creating release")
    
    result = Github.create_release('owner', 'repo', 'v1.0.0', 'Changelog content')
    
    mock_github_session.post.assert_called_once_with(
        'https://api.github.com/repos/owner/repo/releases',
        json={
            'tag_name': 'v1.0.0',
            'name': 'v1.0.0',
            'body': 'Changelog content',
            'draft': False,
            'prerelease': False,
        }
    )
    assert result is False
