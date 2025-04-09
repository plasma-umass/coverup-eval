# file: semantic_release/hvcs.py:126-135
# asked: {"lines": [126, 127, 132, 133, 134, 135], "branches": [[133, 134], [133, 135]]}
# gained: {"lines": [126, 127, 132, 133, 134, 135], "branches": [[133, 134], [133, 135]]}

import pytest
from semantic_release.hvcs import Github, TokenAuth

@pytest.fixture
def mock_token(monkeypatch):
    def mock_token():
        return "mocked_token"
    monkeypatch.setattr(Github, "token", mock_token)

def test_github_auth_with_token(mock_token):
    auth = Github.auth()
    assert isinstance(auth, TokenAuth)
    assert auth.token == "mocked_token"

def test_github_auth_without_token(monkeypatch):
    def mock_token():
        return None
    monkeypatch.setattr(Github, "token", mock_token)
    auth = Github.auth()
    assert auth is None
