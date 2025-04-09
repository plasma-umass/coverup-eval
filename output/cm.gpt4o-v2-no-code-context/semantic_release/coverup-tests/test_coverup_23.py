# file: semantic_release/hvcs.py:145-166
# asked: {"lines": [145, 146, 147, 158, 159, 160, 161, 163, 164, 165, 166], "branches": []}
# gained: {"lines": [145, 146, 147, 158, 159, 160, 161, 163, 164, 165, 166], "branches": []}

import pytest
from unittest.mock import patch, Mock
from requests import HTTPError
from semantic_release.hvcs import Github

@pytest.fixture
def mock_github_session(monkeypatch):
    mock_session = Mock()
    monkeypatch.setattr(Github, 'session', lambda: mock_session)
    return mock_session

@pytest.fixture
def mock_github_api_url(monkeypatch):
    monkeypatch.setattr(Github, 'api_url', lambda: 'https://api.github.com')
    return 'https://api.github.com'

def test_check_build_status_success(mock_github_session, mock_github_api_url):
    mock_response = Mock()
    mock_response.json.return_value = {"state": "success"}
    mock_github_session.get.return_value = mock_response

    result = Github.check_build_status('owner', 'repo', 'ref')
    assert result is True
    mock_github_session.get.assert_called_once_with(
        'https://api.github.com/repos/owner/repo/commits/ref/status'
    )

def test_check_build_status_failure(mock_github_session, mock_github_api_url):
    mock_response = Mock()
    mock_response.json.return_value = {"state": "failure"}
    mock_github_session.get.return_value = mock_response

    result = Github.check_build_status('owner', 'repo', 'ref')
    assert result is False
    mock_github_session.get.assert_called_once_with(
        'https://api.github.com/repos/owner/repo/commits/ref/status'
    )

def test_check_build_status_http_error(mock_github_session, mock_github_api_url):
    mock_github_session.get.side_effect = HTTPError("HTTP Error")

    result = Github.check_build_status('owner', 'repo', 'ref')
    assert result is False
    mock_github_session.get.assert_called_once_with(
        'https://api.github.com/repos/owner/repo/commits/ref/status'
    )
