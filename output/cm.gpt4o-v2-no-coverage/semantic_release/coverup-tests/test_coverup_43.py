# file: semantic_release/hvcs.py:274-314
# asked: {"lines": [], "branches": [[294, 297]]}
# gained: {"lines": [], "branches": [[294, 297]]}

import pytest
import os
from unittest.mock import patch, mock_open, MagicMock
from requests import HTTPError
from semantic_release.hvcs import Github

@pytest.fixture
def mock_logger(mocker):
    return mocker.patch('semantic_release.hvcs.logger')

@pytest.fixture
def mock_session(mocker):
    return mocker.patch('semantic_release.hvcs.Github.session')

def test_upload_asset_success(mock_logger, mock_session):
    mock_response = MagicMock()
    mock_response.url = "http://example.com"
    mock_response.status_code = 200
    mock_session.return_value.post.return_value = mock_response

    with patch("builtins.open", mock_open(read_data="data")) as mock_file:
        result = Github.upload_asset("owner", "repo", 1, "file.txt", "label")

    mock_file.assert_called_once_with("file.txt", "rb")
    mock_session.return_value.post.assert_called_once()
    mock_logger.debug.assert_called_once_with(
        "Asset upload on Github completed, url: http://example.com, status code: 200"
    )
    assert result is True

def test_upload_asset_failure(mock_logger, mock_session):
    mock_session.return_value.post.side_effect = HTTPError("Error")

    with patch("builtins.open", mock_open(read_data="data")) as mock_file:
        result = Github.upload_asset("owner", "repo", 1, "file.txt", "label")

    mock_file.assert_called_once_with("file.txt", "rb")
    mock_session.return_value.post.assert_called_once()
    mock_logger.warning.assert_called_once_with(
        "Asset upload file.txt on Github has failed: Error"
    )
    assert result is False

def test_upload_asset_no_content_type(mock_logger, mock_session):
    mock_response = MagicMock()
    mock_response.url = "http://example.com"
    mock_response.status_code = 200
    mock_session.return_value.post.return_value = mock_response

    with patch("builtins.open", mock_open(read_data="data")) as mock_file, \
         patch("mimetypes.guess_type", return_value=(None, None)):
        result = Github.upload_asset("owner", "repo", 1, "file.unknown", "label")

    mock_file.assert_called_once_with("file.unknown", "rb")
    mock_session.return_value.post.assert_called_once()
    mock_logger.debug.assert_called_once_with(
        "Asset upload on Github completed, url: http://example.com, status code: 200"
    )
    assert result is True
