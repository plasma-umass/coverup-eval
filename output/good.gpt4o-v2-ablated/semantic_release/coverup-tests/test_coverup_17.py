# file: semantic_release/hvcs.py:221-243
# asked: {"lines": [221, 222, 223, 235, 236, 237, 238, 240, 241, 242, 243], "branches": []}
# gained: {"lines": [221, 222, 223, 235, 236, 237, 238, 240, 241, 242, 243], "branches": []}

import pytest
from unittest.mock import patch, Mock
from requests import HTTPError
from semantic_release.hvcs import Github

@pytest.fixture
def mock_session_post(monkeypatch):
    mock_post = Mock()
    monkeypatch.setattr(Github, 'session', Mock(return_value=Mock(post=mock_post)))
    return mock_post

def test_edit_release_success(mock_session_post):
    mock_session_post.return_value = Mock(status_code=200)
    
    result = Github.edit_release('owner', 'repo', 1, 'changelog')
    
    mock_session_post.assert_called_once_with(
        'https://api.github.com/repos/owner/repo/releases/1',
        json={'body': 'changelog'}
    )
    assert result is True

def test_edit_release_failure(mock_session_post):
    mock_session_post.side_effect = HTTPError("Error")
    
    result = Github.edit_release('owner', 'repo', 1, 'changelog')
    
    mock_session_post.assert_called_once_with(
        'https://api.github.com/repos/owner/repo/releases/1',
        json={'body': 'changelog'}
    )
    assert result is False
