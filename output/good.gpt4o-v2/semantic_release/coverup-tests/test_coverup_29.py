# file: semantic_release/hvcs.py:137-143
# asked: {"lines": [137, 138, 139, 141, 142, 143], "branches": []}
# gained: {"lines": [137, 138, 139, 141, 142, 143], "branches": []}

import pytest
from requests import Session
from urllib3 import Retry
from semantic_release.hvcs import Github
from semantic_release.helpers import build_requests_session

def test_github_session_with_retry_int(monkeypatch):
    def mock_build_requests_session(raise_for_status=True, retry=True):
        session = Session()
        session.test_attr = (raise_for_status, retry)
        return session

    def mock_auth():
        return ('user', 'pass')

    monkeypatch.setattr('semantic_release.hvcs.build_requests_session', mock_build_requests_session)
    monkeypatch.setattr('semantic_release.hvcs.Github.auth', mock_auth)

    session = Github.session(retry=5)
    assert session.test_attr == (True, 5)
    assert session.auth == ('user', 'pass')

def test_github_session_with_retry_instance(monkeypatch):
    retry_instance = Retry(total=10)

    def mock_build_requests_session(raise_for_status=True, retry=True):
        session = Session()
        session.test_attr = (raise_for_status, retry)
        return session

    def mock_auth():
        return ('user', 'pass')

    monkeypatch.setattr('semantic_release.hvcs.build_requests_session', mock_build_requests_session)
    monkeypatch.setattr('semantic_release.hvcs.Github.auth', mock_auth)

    session = Github.session(retry=retry_instance)
    assert session.test_attr == (True, retry_instance)
    assert session.auth == ('user', 'pass')

def test_github_session_without_raise_for_status(monkeypatch):
    def mock_build_requests_session(raise_for_status=True, retry=True):
        session = Session()
        session.test_attr = (raise_for_status, retry)
        return session

    def mock_auth():
        return ('user', 'pass')

    monkeypatch.setattr('semantic_release.hvcs.build_requests_session', mock_build_requests_session)
    monkeypatch.setattr('semantic_release.hvcs.Github.auth', mock_auth)

    session = Github.session(raise_for_status=False)
    assert session.test_attr == (False, True)
    assert session.auth == ('user', 'pass')
