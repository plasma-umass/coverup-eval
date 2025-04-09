# file semantic_release/hvcs.py:274-314
# lines [295]
# branches ['294->295']

import pytest
import mimetypes
import os
from unittest.mock import patch, mock_open
from semantic_release.hvcs import Github

@pytest.fixture
def mock_github_session(mocker):
    mock_session = mocker.patch('semantic_release.hvcs.Github.session')
    mock_response = mocker.Mock()
    mock_response.url = "https://uploads.github.com/repos/owner/repo/releases/1/assets"
    mock_response.status_code = 200
    mock_session.return_value.post.return_value = mock_response
    return mock_session

def test_upload_asset_no_content_type(mocker, mock_github_session):
    owner = "owner"
    repo = "repo"
    release_id = 1
    file_path = "testfile.unknown"
    label = "testlabel"

    # Ensure the file exists and can be read
    mocker.patch("builtins.open", mock_open(read_data="file content"))
    mocker.patch("os.path.basename", return_value="testfile.unknown")
    mocker.patch("mimetypes.guess_type", return_value=(None, None))

    result = Github.upload_asset(owner, repo, release_id, file_path, label)

    # Assertions to verify the postconditions
    assert result is True
    mock_github_session.return_value.post.assert_called_once()
    args, kwargs = mock_github_session.return_value.post.call_args
    assert kwargs['headers']['Content-Type'] == "application/octet-stream"

    # Clean up
    mocker.stopall()
