# file: semantic_release/hvcs.py:126-135
# asked: {"lines": [126, 127, 132, 133, 134, 135], "branches": [[133, 134], [133, 135]]}
# gained: {"lines": [126, 127, 132, 133, 134, 135], "branches": [[133, 134], [133, 135]]}

import os
import pytest
from semantic_release.hvcs import Github, TokenAuth

@pytest.fixture
def clear_env(monkeypatch):
    # Clear the GH_TOKEN environment variable before each test
    monkeypatch.delenv('GH_TOKEN', raising=False)

def test_github_auth_with_token(monkeypatch, clear_env):
    # Set the GH_TOKEN environment variable
    monkeypatch.setenv('GH_TOKEN', 'test_token')
    
    # Call the auth method
    auth = Github.auth()
    
    # Assert that the auth method returns a TokenAuth instance with the correct token
    assert isinstance(auth, TokenAuth)
    assert auth.token == 'test_token'

def test_github_auth_without_token(clear_env):
    # Call the auth method without setting the GH_TOKEN environment variable
    auth = Github.auth()
    
    # Assert that the auth method returns None
    assert auth is None
