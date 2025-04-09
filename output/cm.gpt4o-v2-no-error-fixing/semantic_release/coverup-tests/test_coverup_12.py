# file: semantic_release/hvcs.py:126-135
# asked: {"lines": [126, 127, 132, 133, 134, 135], "branches": [[133, 134], [133, 135]]}
# gained: {"lines": [126, 127, 132, 133, 134, 135], "branches": [[133, 134], [133, 135]]}

import os
import pytest
from semantic_release.hvcs import Github, TokenAuth

def test_github_auth_with_token(monkeypatch):
    # Arrange
    test_token = "test_token_value"
    monkeypatch.setenv("GH_TOKEN", test_token)

    # Act
    result = Github.auth()

    # Assert
    assert result is not None
    assert isinstance(result, TokenAuth)
    assert result.token == test_token

def test_github_auth_without_token(monkeypatch):
    # Arrange
    monkeypatch.delenv("GH_TOKEN", raising=False)

    # Act
    result = Github.auth()

    # Assert
    assert result is None
