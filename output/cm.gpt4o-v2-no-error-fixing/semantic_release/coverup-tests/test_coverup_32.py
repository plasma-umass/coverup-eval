# file: semantic_release/hvcs.py:137-143
# asked: {"lines": [141, 142, 143], "branches": []}
# gained: {"lines": [141, 142, 143], "branches": []}

import pytest
from requests import Session
from urllib3 import Retry
from semantic_release.hvcs import Github
from semantic_release.helpers import build_requests_session

@pytest.fixture
def mock_build_requests_session(mocker):
    return mocker.patch('semantic_release.hvcs.build_requests_session', wraps=build_requests_session)

@pytest.fixture
def mock_github_auth(mocker):
    return mocker.patch('semantic_release.hvcs.Github.auth', return_value=('user', 'pass'))

def test_github_session(mock_build_requests_session, mock_github_auth):
    session = Github.session()
    assert isinstance(session, Session)
    assert session.auth == ('user', 'pass')
    mock_build_requests_session.assert_called_once_with(raise_for_status=True, retry=True)
    mock_github_auth.assert_called_once()

def test_github_session_with_retry_int(mock_build_requests_session, mock_github_auth):
    retry = 5
    session = Github.session(retry=retry)
    assert isinstance(session, Session)
    assert session.auth == ('user', 'pass')
    mock_build_requests_session.assert_called_once_with(raise_for_status=True, retry=retry)
    mock_github_auth.assert_called_once()

def test_github_session_with_retry_instance(mock_build_requests_session, mock_github_auth):
    retry = Retry(total=3)
    session = Github.session(retry=retry)
    assert isinstance(session, Session)
    assert session.auth == ('user', 'pass')
    mock_build_requests_session.assert_called_once_with(raise_for_status=True, retry=retry)
    mock_github_auth.assert_called_once()
