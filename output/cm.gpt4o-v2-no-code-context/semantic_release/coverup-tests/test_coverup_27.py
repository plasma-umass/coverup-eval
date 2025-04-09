# file: semantic_release/hvcs.py:137-143
# asked: {"lines": [137, 138, 139, 141, 142, 143], "branches": []}
# gained: {"lines": [137, 138, 139, 141, 142, 143], "branches": []}

import pytest
from unittest.mock import patch, MagicMock
from semantic_release.hvcs import Github

@pytest.fixture
def mock_build_requests_session(monkeypatch):
    mock_session = MagicMock()
    monkeypatch.setattr('semantic_release.hvcs.build_requests_session', lambda *args, **kwargs: mock_session)
    return mock_session

@pytest.fixture
def mock_github_auth(monkeypatch):
    mock_auth = MagicMock()
    monkeypatch.setattr('semantic_release.hvcs.Github.auth', lambda: mock_auth)
    return mock_auth

def test_github_session(mock_build_requests_session, mock_github_auth):
    session = Github.session()
    assert session == mock_build_requests_session
    assert session.auth == mock_github_auth

def test_github_session_with_params(mock_build_requests_session, mock_github_auth):
    session = Github.session(raise_for_status=False, retry=3)
    assert session == mock_build_requests_session
    assert session.auth == mock_github_auth
