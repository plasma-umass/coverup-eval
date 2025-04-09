# file: semantic_release/hvcs.py:221-243
# asked: {"lines": [221, 222, 223, 235, 236, 237, 238, 240, 241, 242, 243], "branches": []}
# gained: {"lines": [221, 222, 223, 235, 236, 237, 238, 240, 241, 242, 243], "branches": []}

import pytest
from requests import HTTPError
from unittest.mock import patch, MagicMock
from semantic_release.hvcs import Github

@pytest.fixture
def mock_github_session(monkeypatch):
    mock_session = MagicMock()
    monkeypatch.setattr(Github, 'session', MagicMock(return_value=mock_session))
    return mock_session

@pytest.fixture
def mock_github_api_url(monkeypatch):
    monkeypatch.setattr(Github, 'api_url', MagicMock(return_value='https://api.github.com'))

def test_edit_release_success(mock_github_session, mock_github_api_url):
    mock_github_session.post.return_value.raise_for_status = MagicMock()
    
    result = Github.edit_release('owner', 'repo', 1, 'changelog')
    
    mock_github_session.post.assert_called_once_with(
        'https://api.github.com/repos/owner/repo/releases/1',
        json={'body': 'changelog'}
    )
    assert result is True

def test_edit_release_failure(mock_github_session, mock_github_api_url, caplog):
    mock_github_session.post.side_effect = HTTPError("Error")
    
    result = Github.edit_release('owner', 'repo', 1, 'changelog')
    
    mock_github_session.post.assert_called_once_with(
        'https://api.github.com/repos/owner/repo/releases/1',
        json={'body': 'changelog'}
    )
    assert result is False
    assert "Edit release on Github has failed: Error" in caplog.text
