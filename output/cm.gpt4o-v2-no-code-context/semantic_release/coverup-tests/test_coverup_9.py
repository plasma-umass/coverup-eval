# file: semantic_release/hvcs.py:126-135
# asked: {"lines": [126, 127, 132, 133, 134, 135], "branches": [[133, 134], [133, 135]]}
# gained: {"lines": [126, 127, 132, 133, 134, 135], "branches": [[133, 134], [133, 135]]}

import pytest
from semantic_release.hvcs import Github, TokenAuth

def test_github_auth_with_token(monkeypatch):
    # Arrange
    test_token = "test_token"
    monkeypatch.setattr(Github, "token", lambda: test_token)
    
    # Act
    auth = Github.auth()
    
    # Assert
    assert isinstance(auth, TokenAuth)
    assert auth.token == test_token

def test_github_auth_without_token(monkeypatch):
    # Arrange
    monkeypatch.setattr(Github, "token", lambda: None)
    
    # Act
    auth = Github.auth()
    
    # Assert
    assert auth is None
