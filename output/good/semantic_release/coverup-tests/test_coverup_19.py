# file semantic_release/hvcs.py:145-166
# lines [145, 146, 147, 158, 159, 160, 161, 163, 164, 165, 166]
# branches []

import pytest
from unittest.mock import Mock
from requests.exceptions import HTTPError
from semantic_release.hvcs import Github

def test_github_check_build_status_success(mocker):
    # Mock the session and the response
    mock_session = mocker.patch.object(Github, 'session', return_value=mocker.Mock())
    mock_response = mocker.Mock()
    mock_response.json.return_value = {"state": "success"}
    mock_session.return_value.get.return_value = mock_response

    # Call the function
    result = Github.check_build_status('owner', 'repo', 'ref')

    # Assert the result is True
    assert result is True

    # Cleanup
    mocker.stopall()

def test_github_check_build_status_failure(mocker):
    # Mock the session and the response
    mock_session = mocker.patch.object(Github, 'session', return_value=mocker.Mock())
    mock_response = mocker.Mock()
    mock_response.json.return_value = {"state": "failure"}
    mock_session.return_value.get.return_value = mock_response

    # Call the function
    result = Github.check_build_status('owner', 'repo', 'ref')

    # Assert the result is False
    assert result is False

    # Cleanup
    mocker.stopall()

def test_github_check_build_status_http_error(mocker):
    # Mock the session and the response
    mock_session = mocker.patch.object(Github, 'session', return_value=mocker.Mock())
    mock_session.return_value.get.side_effect = HTTPError("HTTP Error occurred")

    # Mock the logger
    mock_logger = mocker.patch('semantic_release.hvcs.logger')

    # Call the function
    result = Github.check_build_status('owner', 'repo', 'ref')

    # Assert the result is False
    assert result is False

    # Assert the logger was called
    mock_logger.warning.assert_called_once()

    # Cleanup
    mocker.stopall()
