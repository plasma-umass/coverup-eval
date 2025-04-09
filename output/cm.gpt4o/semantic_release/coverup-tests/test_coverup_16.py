# file semantic_release/hvcs.py:145-166
# lines [145, 146, 147, 158, 159, 160, 161, 163, 164, 165, 166]
# branches []

import pytest
import requests
from requests.exceptions import HTTPError
from unittest.mock import patch, Mock
from semantic_release.hvcs import Github

@pytest.fixture
def mock_github_session(mocker):
    mock_session = mocker.patch('semantic_release.hvcs.Github.session', autospec=True)
    return mock_session

def test_check_build_status_success(mock_github_session):
    mock_response = Mock()
    mock_response.json.return_value = {"state": "success"}
    mock_github_session.return_value.get.return_value = mock_response

    result = Github.check_build_status("owner", "repo", "ref")
    assert result is True

def test_check_build_status_failure(mock_github_session):
    mock_response = Mock()
    mock_response.json.return_value = {"state": "failure"}
    mock_github_session.return_value.get.return_value = mock_response

    result = Github.check_build_status("owner", "repo", "ref")
    assert result is False

def test_check_build_status_http_error(mock_github_session, caplog):
    mock_github_session.return_value.get.side_effect = HTTPError("HTTP Error occurred")

    result = Github.check_build_status("owner", "repo", "ref")
    assert result is False
    assert "Build status check on Github has failed: HTTP Error occurred" in caplog.text
