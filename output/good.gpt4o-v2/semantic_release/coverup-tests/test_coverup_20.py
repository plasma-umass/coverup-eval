# file: semantic_release/hvcs.py:221-243
# asked: {"lines": [221, 222, 223, 235, 236, 237, 238, 240, 241, 242, 243], "branches": []}
# gained: {"lines": [221, 222, 223, 235, 236, 237, 238, 240, 241, 242, 243], "branches": []}

import pytest
from requests import HTTPError
from unittest.mock import patch, MagicMock
from semantic_release.hvcs import Github

@pytest.fixture
def mock_session_post(monkeypatch):
    mock_post = MagicMock()
    monkeypatch.setattr(Github, 'session', lambda: MagicMock(post=mock_post))
    return mock_post

def test_edit_release_success(mock_session_post):
    mock_session_post.return_value = MagicMock(status_code=200)
    result = Github.edit_release('owner', 'repo', 1, 'changelog')
    assert result is True
    mock_session_post.assert_called_once_with(
        'https://api.github.com/repos/owner/repo/releases/1',
        json={'body': 'changelog'}
    )

def test_edit_release_failure(mock_session_post):
    mock_session_post.side_effect = HTTPError("Error")
    with patch('semantic_release.hvcs.logger') as mock_logger:
        result = Github.edit_release('owner', 'repo', 1, 'changelog')
        assert result is False
        mock_logger.warning.assert_called_once_with("Edit release on Github has failed: Error")
