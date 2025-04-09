# file: semantic_release/hvcs.py:137-143
# asked: {"lines": [137, 138, 139, 141, 142, 143], "branches": []}
# gained: {"lines": [137, 138, 139, 141, 142, 143], "branches": []}

import pytest
from requests import Session
from urllib3 import Retry
from semantic_release.hvcs import Github
from semantic_release.helpers import build_requests_session

class MockTokenAuth:
    def __init__(self, token):
        self.token = token

@pytest.fixture
def mock_build_requests_session(mocker):
    return mocker.patch('semantic_release.hvcs.build_requests_session', side_effect=build_requests_session)

@pytest.fixture
def mock_github_auth(mocker):
    return mocker.patch('semantic_release.hvcs.Github.auth', return_value=MockTokenAuth("mock_token"))

def test_github_session_default(mock_build_requests_session, mock_github_auth):
    session = Github.session()
    assert isinstance(session, Session)
    assert session.auth.token == "mock_token"
    mock_build_requests_session.assert_called_once_with(raise_for_status=True, retry=True)

def test_github_session_no_retry(mock_build_requests_session, mock_github_auth):
    session = Github.session(retry=False)
    assert isinstance(session, Session)
    assert session.auth.token == "mock_token"
    mock_build_requests_session.assert_called_once_with(raise_for_status=True, retry=False)

def test_github_session_custom_retry(mock_build_requests_session, mock_github_auth):
    custom_retry = Retry(total=5)
    session = Github.session(retry=custom_retry)
    assert isinstance(session, Session)
    assert session.auth.token == "mock_token"
    mock_build_requests_session.assert_called_once_with(raise_for_status=True, retry=custom_retry)
