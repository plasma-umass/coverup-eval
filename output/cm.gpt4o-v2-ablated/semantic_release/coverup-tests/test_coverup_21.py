# file: semantic_release/hvcs.py:137-143
# asked: {"lines": [137, 138, 139, 141, 142, 143], "branches": []}
# gained: {"lines": [137, 138, 139, 141, 142, 143], "branches": []}

import pytest
from unittest.mock import patch, MagicMock
from requests import Session
from semantic_release.hvcs import Github

@pytest.fixture
def mock_build_requests_session(mocker):
    return mocker.patch('semantic_release.hvcs.build_requests_session')

@pytest.fixture
def mock_github_auth(mocker):
    return mocker.patch('semantic_release.hvcs.Github.auth')

def test_github_session_default(mock_build_requests_session, mock_github_auth):
    mock_session = MagicMock(spec=Session)
    mock_build_requests_session.return_value = mock_session
    mock_github_auth.return_value = ('user', 'token')

    session = Github.session()

    mock_build_requests_session.assert_called_once_with(raise_for_status=True, retry=True)
    mock_github_auth.assert_called_once()
    assert session.auth == ('user', 'token')

def test_github_session_custom_retry(mock_build_requests_session, mock_github_auth):
    mock_session = MagicMock(spec=Session)
    mock_build_requests_session.return_value = mock_session
    mock_github_auth.return_value = ('user', 'token')

    session = Github.session(retry=5)

    mock_build_requests_session.assert_called_once_with(raise_for_status=True, retry=5)
    mock_github_auth.assert_called_once()
    assert session.auth == ('user', 'token')

def test_github_session_no_raise_for_status(mock_build_requests_session, mock_github_auth):
    mock_session = MagicMock(spec=Session)
    mock_build_requests_session.return_value = mock_session
    mock_github_auth.return_value = ('user', 'token')

    session = Github.session(raise_for_status=False)

    mock_build_requests_session.assert_called_once_with(raise_for_status=False, retry=True)
    mock_github_auth.assert_called_once()
    assert session.auth == ('user', 'token')
