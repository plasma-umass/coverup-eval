# file: semantic_release/hvcs.py:365-371
# asked: {"lines": [365, 366, 371], "branches": []}
# gained: {"lines": [365, 366, 371], "branches": []}

import os
import pytest
from semantic_release.hvcs import Gitlab

def test_gitlab_token(monkeypatch):
    # Set up the environment variable
    monkeypatch.setenv("GL_TOKEN", "test_token")
    
    # Call the method and assert the expected value
    assert Gitlab.token() == "test_token"
    
    # Clean up by unsetting the environment variable
    monkeypatch.delenv("GL_TOKEN", raising=False)

def test_gitlab_token_not_set(monkeypatch):
    # Ensure the environment variable is not set
    monkeypatch.delenv("GL_TOKEN", raising=False)
    
    # Call the method and assert the expected value
    assert Gitlab.token() is None
