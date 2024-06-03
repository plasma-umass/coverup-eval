# file semantic_release/hvcs.py:274-314
# lines [274, 275, 276, 277, 291, 293, 294, 295, 297, 298, 299, 300, 301, 302, 304, 307, 308, 311, 312, 313, 314]
# branches ['294->295', '294->297']

import pytest
import os
import mimetypes
from unittest.mock import patch, mock_open
from requests import HTTPError
from semantic_release.hvcs import Github

@pytest.fixture
def mock_github_session(mocker):
    mock_session = mocker.patch('semantic_release.hvcs.Github.session')
    mock_post = mocker.Mock()
    mock_session.return_value.post = mock_post
    return mock_post

def test_github_upload_asset_success(mock_github_session, mocker):
    mock_response = mocker.Mock()
    mock_response.url = "https://uploads.github.com/repos/owner/repo/releases/1/assets"
    mock_response.status_code = 201
    mock_github_session.return_value = mock_response

    mocker.patch("builtins.open", mock_open(read_data=b"file content"))
    mocker.patch("os.path.basename", return_value="file.txt")
    mocker.patch("mimetypes.guess_type", return_value=("text/plain", None))

    result = Github.upload_asset("owner", "repo", 1, "file.txt", "label")

    assert result is True
    mock_github_session.assert_called_once_with(
        "https://uploads.github.com/repos/owner/repo/releases/1/assets",
        params={"name": "file.txt", "label": "label"},
        headers={"Content-Type": "text/plain"},
        data=b"file content"
    )

def test_github_upload_asset_failure(mock_github_session, mocker):
    mock_github_session.side_effect = HTTPError("HTTP Error")

    mocker.patch("builtins.open", mock_open(read_data=b"file content"))
    mocker.patch("os.path.basename", return_value="file.txt")
    mocker.patch("mimetypes.guess_type", return_value=("text/plain", None))

    result = Github.upload_asset("owner", "repo", 1, "file.txt", "label")

    assert result is False
    mock_github_session.assert_called_once_with(
        "https://uploads.github.com/repos/owner/repo/releases/1/assets",
        params={"name": "file.txt", "label": "label"},
        headers={"Content-Type": "text/plain"},
        data=b"file content"
    )
