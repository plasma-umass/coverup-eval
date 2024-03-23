# file semantic_release/hvcs.py:137-143
# lines [137, 138, 139, 141, 142, 143]
# branches []

import pytest
from unittest.mock import patch
from requests import Session
from semantic_release.hvcs import Github
from semantic_release.hvcs import build_requests_session

@pytest.fixture
def mock_build_requests_session(mocker):
    with patch('semantic_release.hvcs.build_requests_session') as mock:
        mock.return_value = Session()
        yield mock

@pytest.fixture
def mock_github_auth(mocker):
    with patch('semantic_release.hvcs.Github.auth') as mock:
        mock.return_value = ('username', 'token')
        yield mock

def test_github_session(mock_build_requests_session, mock_github_auth):
    session = Github.session()
    assert isinstance(session, Session)
    mock_build_requests_session.assert_called_once_with(raise_for_status=True, retry=True)
    assert session.auth == ('username', 'token')

def test_github_session_with_custom_retry(mock_build_requests_session, mock_github_auth):
    custom_retry = 3
    session = Github.session(retry=custom_retry)
    assert isinstance(session, Session)
    mock_build_requests_session.assert_called_once_with(raise_for_status=True, retry=custom_retry)
    assert session.auth == ('username', 'token')

def test_github_session_without_retry(mock_build_requests_session, mock_github_auth):
    session = Github.session(retry=False)
    assert isinstance(session, Session)
    mock_build_requests_session.assert_called_once_with(raise_for_status=True, retry=False)
    assert session.auth == ('username', 'token')

def test_github_session_without_raise_for_status(mock_build_requests_session, mock_github_auth):
    session = Github.session(raise_for_status=False)
    assert isinstance(session, Session)
    mock_build_requests_session.assert_called_once_with(raise_for_status=False, retry=True)
    assert session.auth == ('username', 'token')
