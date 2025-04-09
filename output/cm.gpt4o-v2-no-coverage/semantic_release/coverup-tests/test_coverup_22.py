# file: semantic_release/hvcs.py:145-166
# asked: {"lines": [145, 146, 147, 158, 159, 160, 161, 163, 164, 165, 166], "branches": []}
# gained: {"lines": [145, 146, 147, 158, 159, 160, 161, 163, 164, 165, 166], "branches": []}

import pytest
import requests
from requests import HTTPError
from unittest.mock import patch, MagicMock
from semantic_release.hvcs import Github
from semantic_release.helpers import LoggedFunction

@pytest.fixture
def mock_logger(mocker):
    return mocker.patch('semantic_release.hvcs.logger')

@pytest.fixture
def mock_session(mocker):
    return mocker.patch('semantic_release.hvcs.Github.session')

@pytest.fixture
def mock_api_url(mocker):
    return mocker.patch('semantic_release.hvcs.Github.api_url')

def test_check_build_status_success(mock_session, mock_api_url, mock_logger):
    mock_api_url.return_value = "https://api.github.com"
    mock_response = MagicMock()
    mock_response.json.return_value = {"state": "success"}
    mock_session.return_value.get.return_value = mock_response

    result = Github.check_build_status("owner", "repo", "ref")
    assert result is True
    mock_session.return_value.get.assert_called_once_with(
        "https://api.github.com/repos/owner/repo/commits/ref/status"
    )

def test_check_build_status_failure(mock_session, mock_api_url, mock_logger):
    mock_api_url.return_value = "https://api.github.com"
    mock_response = MagicMock()
    mock_response.json.return_value = {"state": "failure"}
    mock_session.return_value.get.return_value = mock_response

    result = Github.check_build_status("owner", "repo", "ref")
    assert result is False
    mock_session.return_value.get.assert_called_once_with(
        "https://api.github.com/repos/owner/repo/commits/ref/status"
    )

def test_check_build_status_http_error(mock_session, mock_api_url, mock_logger):
    mock_api_url.return_value = "https://api.github.com"
    mock_session.return_value.get.side_effect = HTTPError("HTTP Error occurred")

    result = Github.check_build_status("owner", "repo", "ref")
    assert result is False
    mock_logger.warning.assert_called_once_with(
        "Build status check on Github has failed: HTTP Error occurred"
    )
