# file: semantic_release/hvcs.py:145-166
# asked: {"lines": [145, 146, 147, 158, 159, 160, 161, 163, 164, 165, 166], "branches": []}
# gained: {"lines": [145, 146, 147, 158, 159, 160, 161, 163, 164, 165, 166], "branches": []}

import pytest
from unittest.mock import patch, Mock
from requests import HTTPError
from semantic_release.hvcs import Github

@pytest.fixture
def mock_session():
    with patch('semantic_release.hvcs.Github.session') as mock_session:
        yield mock_session

@pytest.fixture
def mock_logger():
    with patch('semantic_release.hvcs.logger') as mock_logger:
        yield mock_logger

def test_check_build_status_success(mock_session):
    mock_response = Mock()
    mock_response.json.return_value = {"state": "success"}
    mock_session.return_value.get.return_value = mock_response

    result = Github.check_build_status("owner", "repo", "ref")
    assert result is True

def test_check_build_status_failure(mock_session):
    mock_response = Mock()
    mock_response.json.return_value = {"state": "failure"}
    mock_session.return_value.get.return_value = mock_response

    result = Github.check_build_status("owner", "repo", "ref")
    assert result is False

def test_check_build_status_http_error(mock_session, mock_logger):
    mock_session.return_value.get.side_effect = HTTPError("HTTP Error")

    result = Github.check_build_status("owner", "repo", "ref")
    assert result is False
    mock_logger.warning.assert_called_once_with("Build status check on Github has failed: HTTP Error")
