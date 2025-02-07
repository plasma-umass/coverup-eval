# file: semantic_release/hvcs.py:274-314
# asked: {"lines": [291, 293, 294, 295, 297, 298, 299, 300, 301, 302, 304, 307, 308, 311, 312, 313, 314], "branches": [[294, 295], [294, 297]]}
# gained: {"lines": [291, 293, 294, 295, 297, 298, 299, 300, 301, 302, 304, 307, 308, 311, 312, 313, 314], "branches": [[294, 295], [294, 297]]}

import mimetypes
import os
import pytest
from requests import HTTPError, Response
from unittest.mock import patch, mock_open
from semantic_release.hvcs import Github
from semantic_release.helpers import LoggedFunction

@pytest.fixture
def mock_logger(mocker):
    return mocker.patch("semantic_release.hvcs.logger")

@pytest.fixture
def mock_session(mocker):
    mock_session = mocker.Mock()
    mocker.patch("semantic_release.hvcs.Github.session", return_value=mock_session)
    return mock_session

def test_upload_asset_success(mock_logger, mock_session):
    mock_response = Response()
    mock_response.status_code = 200
    mock_response.url = "https://uploads.github.com/repos/owner/repo/releases/1/assets"
    mock_session.post.return_value = mock_response

    with patch("builtins.open", mock_open(read_data="data")):
        result = Github.upload_asset("owner", "repo", 1, "file.txt", "label")

    assert result is True
    mock_logger.debug.assert_called_with(
        "Asset upload on Github completed, url: https://uploads.github.com/repos/owner/repo/releases/1/assets, status code: 200"
    )

def test_upload_asset_no_content_type(mock_logger, mock_session):
    mock_response = Response()
    mock_response.status_code = 200
    mock_response.url = "https://uploads.github.com/repos/owner/repo/releases/1/assets"
    mock_session.post.return_value = mock_response

    with patch("builtins.open", mock_open(read_data="data")):
        with patch("mimetypes.guess_type", return_value=(None, None)):
            result = Github.upload_asset("owner", "repo", 1, "file.unknown", "label")

    assert result is True
    mock_logger.debug.assert_called_with(
        "Asset upload on Github completed, url: https://uploads.github.com/repos/owner/repo/releases/1/assets, status code: 200"
    )

def test_upload_asset_http_error(mock_logger, mock_session):
    mock_session.post.side_effect = HTTPError("HTTP Error occurred")

    with patch("builtins.open", mock_open(read_data="data")):
        result = Github.upload_asset("owner", "repo", 1, "file.txt", "label")

    assert result is False
    mock_logger.warning.assert_called_with(
        "Asset upload file.txt on Github has failed: HTTP Error occurred"
    )
