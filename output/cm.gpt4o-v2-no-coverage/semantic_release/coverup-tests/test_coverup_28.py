# file: semantic_release/hvcs.py:274-314
# asked: {"lines": [274, 275, 276, 277, 291, 293, 294, 295, 297, 298, 299, 300, 301, 302, 304, 307, 308, 311, 312, 313, 314], "branches": [[294, 295], [294, 297]]}
# gained: {"lines": [274, 275, 276, 277, 291, 293, 294, 295, 297, 298, 299, 300, 301, 302, 304, 307, 308, 311, 312, 313, 314], "branches": [[294, 295]]}

import pytest
import os
import mimetypes
from requests import HTTPError, Response
from unittest.mock import patch, mock_open
from semantic_release.hvcs import Github
from semantic_release.helpers import LoggedFunction

# Mock logger
import logging
logger = logging.getLogger("test_logger")

class TestGithub:
    @patch("semantic_release.hvcs.Github.session")
    @patch("builtins.open", new_callable=mock_open, read_data=b"file content")
    @patch("os.path.basename", return_value="testfile.txt")
    def test_upload_asset_success(self, mock_basename, mock_open, mock_session):
        # Mock response
        mock_response = Response()
        mock_response.status_code = 200
        mock_response.url = "https://uploads.github.com/repos/owner/repo/releases/1/assets"
        mock_session().post.return_value = mock_response

        result = Github.upload_asset("owner", "repo", 1, "dummy_path", "label")

        mock_open.assert_called_once_with("dummy_path", "rb")
        mock_session().post.assert_called_once()
        assert result is True

    @patch("semantic_release.hvcs.Github.session")
    @patch("builtins.open", new_callable=mock_open, read_data=b"file content")
    @patch("os.path.basename", return_value="testfile.txt")
    def test_upload_asset_http_error(self, mock_basename, mock_open, mock_session):
        # Mock response to raise HTTPError
        mock_session().post.side_effect = HTTPError("HTTP Error occurred")

        result = Github.upload_asset("owner", "repo", 1, "dummy_path", "label")

        mock_open.assert_called_once_with("dummy_path", "rb")
        mock_session().post.assert_called_once()
        assert result is False

    @patch("semantic_release.hvcs.Github.session")
    @patch("builtins.open", new_callable=mock_open, read_data=b"file content")
    @patch("os.path.basename", return_value="testfile.txt")
    def test_upload_asset_no_content_type(self, mock_basename, mock_open, mock_session):
        # Mock response
        mock_response = Response()
        mock_response.status_code = 200
        mock_response.url = "https://uploads.github.com/repos/owner/repo/releases/1/assets"
        mock_session().post.return_value = mock_response

        with patch("mimetypes.guess_type", return_value=(None, None)):
            result = Github.upload_asset("owner", "repo", 1, "dummy_path", "label")

        mock_open.assert_called_once_with("dummy_path", "rb")
        mock_session().post.assert_called_once()
        assert result is True
