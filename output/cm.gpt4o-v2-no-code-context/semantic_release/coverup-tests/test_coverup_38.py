# file: semantic_release/hvcs.py:274-314
# asked: {"lines": [274, 275, 276, 277, 291, 293, 294, 295, 297, 298, 299, 300, 301, 302, 304, 307, 308, 311, 312, 313, 314], "branches": [[294, 295], [294, 297]]}
# gained: {"lines": [274, 275, 276, 277, 291, 293, 294, 295, 297, 298, 299, 300, 301, 302, 304, 307, 308, 311, 312, 313, 314], "branches": [[294, 295], [294, 297]]}

import pytest
import os
import mimetypes
from unittest.mock import patch, mock_open, MagicMock
from requests.exceptions import HTTPError
from semantic_release.hvcs import Github

@pytest.fixture
def mock_github_session_post(monkeypatch):
    mock_post = MagicMock()
    monkeypatch.setattr(Github, 'session', lambda: MagicMock(post=mock_post))
    return mock_post

def test_upload_asset_success(mock_github_session_post, monkeypatch):
    owner = "test_owner"
    repo = "test_repo"
    release_id = 1
    file = "test_file.txt"
    label = "test_label"
    
    # Mock the file opening and reading
    m = mock_open(read_data="file content")
    monkeypatch.setattr("builtins.open", m)
    
    # Mock the response
    mock_response = MagicMock()
    mock_response.url = "http://example.com"
    mock_response.status_code = 200
    mock_github_session_post.return_value = mock_response
    
    result = Github.upload_asset(owner, repo, release_id, file, label)
    
    assert result is True
    mock_github_session_post.assert_called_once()
    m.assert_called_once_with(file, "rb")

def test_upload_asset_no_content_type(mock_github_session_post, monkeypatch):
    owner = "test_owner"
    repo = "test_repo"
    release_id = 1
    file = "test_file.unknown"
    label = "test_label"
    
    # Mock the file opening and reading
    m = mock_open(read_data="file content")
    monkeypatch.setattr("builtins.open", m)
    
    # Mock the response
    mock_response = MagicMock()
    mock_response.url = "http://example.com"
    mock_response.status_code = 200
    mock_github_session_post.return_value = mock_response
    
    # Ensure mimetypes returns None
    monkeypatch.setattr(mimetypes, 'guess_type', lambda *args, **kwargs: (None, None))
    
    result = Github.upload_asset(owner, repo, release_id, file, label)
    
    assert result is True
    mock_github_session_post.assert_called_once()
    m.assert_called_once_with(file, "rb")

def test_upload_asset_failure(mock_github_session_post, monkeypatch):
    owner = "test_owner"
    repo = "test_repo"
    release_id = 1
    file = "test_file.txt"
    label = "test_label"
    
    # Mock the file opening and reading
    m = mock_open(read_data="file content")
    monkeypatch.setattr("builtins.open", m)
    
    # Mock the response to raise HTTPError
    mock_github_session_post.side_effect = HTTPError("HTTP Error")
    
    result = Github.upload_asset(owner, repo, release_id, file, label)
    
    assert result is False
    mock_github_session_post.assert_called_once()
    m.assert_called_once_with(file, "rb")
