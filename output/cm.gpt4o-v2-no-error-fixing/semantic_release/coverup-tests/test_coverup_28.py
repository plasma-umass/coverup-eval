# file: semantic_release/hvcs.py:274-314
# asked: {"lines": [291, 293, 294, 295, 297, 298, 299, 300, 301, 302, 304, 307, 308, 311, 312, 313, 314], "branches": [[294, 295], [294, 297]]}
# gained: {"lines": [291, 293, 294, 295, 297, 298, 299, 300, 301, 302, 304, 307, 308, 311, 312, 313, 314], "branches": [[294, 295], [294, 297]]}

import pytest
import mimetypes
import os
from requests import HTTPError
from unittest.mock import patch, mock_open, MagicMock
from semantic_release.hvcs import Github

@pytest.fixture
def mock_github_session():
    with patch('semantic_release.hvcs.Github.session') as mock_session:
        yield mock_session

@pytest.fixture
def mock_logger():
    with patch('semantic_release.hvcs.logger') as mock_logger:
        yield mock_logger

def test_upload_asset_success(mock_github_session, mock_logger):
    mock_response = MagicMock()
    mock_response.url = "http://example.com"
    mock_response.status_code = 200
    mock_github_session.return_value.post.return_value = mock_response

    with patch("builtins.open", mock_open(read_data="data")):
        result = Github.upload_asset("owner", "repo", 1, "file.txt", "label")

    mock_github_session.return_value.post.assert_called_once()
    mock_logger.debug.assert_called_once_with(
        "Asset upload on Github completed, url: http://example.com, status code: 200"
    )
    assert result is True

def test_upload_asset_no_content_type(mock_github_session, mock_logger):
    mock_response = MagicMock()
    mock_response.url = "http://example.com"
    mock_response.status_code = 200
    mock_github_session.return_value.post.return_value = mock_response

    with patch("builtins.open", mock_open(read_data="data")):
        with patch("mimetypes.guess_type", return_value=(None, None)):
            result = Github.upload_asset("owner", "repo", 1, "file.unknown", "label")

    mock_github_session.return_value.post.assert_called_once()
    mock_logger.debug.assert_called_once_with(
        "Asset upload on Github completed, url: http://example.com, status code: 200"
    )
    assert result is True

def test_upload_asset_http_error(mock_github_session, mock_logger):
    mock_github_session.return_value.post.side_effect = HTTPError("HTTP Error")

    with patch("builtins.open", mock_open(read_data="data")):
        result = Github.upload_asset("owner", "repo", 1, "file.txt", "label")

    mock_github_session.return_value.post.assert_called_once()
    mock_logger.warning.assert_called_once_with(
        "Asset upload file.txt on Github has failed: HTTP Error"
    )
    assert result is False
