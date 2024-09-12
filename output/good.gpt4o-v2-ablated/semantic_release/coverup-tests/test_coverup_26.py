# file: semantic_release/hvcs.py:274-314
# asked: {"lines": [274, 275, 276, 277, 291, 293, 294, 295, 297, 298, 299, 300, 301, 302, 304, 307, 308, 311, 312, 313, 314], "branches": [[294, 295], [294, 297]]}
# gained: {"lines": [274, 275, 276, 277, 291, 293, 294, 295, 297, 298, 299, 300, 301, 302, 304, 307, 308, 311, 312, 313, 314], "branches": [[294, 295], [294, 297]]}

import os
import mimetypes
import pytest
from unittest.mock import patch, mock_open, MagicMock
from requests import HTTPError
from semantic_release.hvcs import Github

@pytest.fixture
def mock_github_session(monkeypatch):
    mock_session = MagicMock()
    monkeypatch.setattr(Github, 'session', MagicMock(return_value=mock_session))
    return mock_session

@pytest.fixture
def mock_logger(monkeypatch):
    mock_logger = MagicMock()
    monkeypatch.setattr('semantic_release.hvcs.logger', mock_logger)
    return mock_logger

def test_upload_asset_success(mock_github_session, mock_logger):
    owner = "test_owner"
    repo = "test_repo"
    release_id = 1
    file = "test_file.txt"
    label = "test_label"
    
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.url = "https://uploads.github.com/test_url"
    mock_github_session.post.return_value = mock_response
    
    with patch("builtins.open", mock_open(read_data="file_content")):
        result = Github.upload_asset(owner, repo, release_id, file, label)
    
    assert result is True
    mock_github_session.post.assert_called_once()
    mock_logger.debug.assert_called_once_with(
        f"Asset upload on Github completed, url: {mock_response.url}, status code: {mock_response.status_code}"
    )

def test_upload_asset_http_error(mock_github_session, mock_logger):
    owner = "test_owner"
    repo = "test_repo"
    release_id = 1
    file = "test_file.txt"
    label = "test_label"
    
    mock_github_session.post.side_effect = HTTPError("HTTP Error")
    
    with patch("builtins.open", mock_open(read_data="file_content")):
        result = Github.upload_asset(owner, repo, release_id, file, label)
    
    assert result is False
    mock_github_session.post.assert_called_once()
    mock_logger.warning.assert_called_once_with(
        f"Asset upload {file} on Github has failed: HTTP Error"
    )

def test_upload_asset_no_content_type(mock_github_session, mock_logger):
    owner = "test_owner"
    repo = "test_repo"
    release_id = 1
    file = "test_file.unknown"
    label = "test_label"
    
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.url = "https://uploads.github.com/test_url"
    mock_github_session.post.return_value = mock_response
    
    with patch("builtins.open", mock_open(read_data="file_content")):
        with patch("mimetypes.guess_type", return_value=(None, None)):
            result = Github.upload_asset(owner, repo, release_id, file, label)
    
    assert result is True
    mock_github_session.post.assert_called_once()
    mock_logger.debug.assert_called_once_with(
        f"Asset upload on Github completed, url: {mock_response.url}, status code: {mock_response.status_code}"
    )
    assert mock_github_session.post.call_args[1]['headers']['Content-Type'] == "application/octet-stream"
