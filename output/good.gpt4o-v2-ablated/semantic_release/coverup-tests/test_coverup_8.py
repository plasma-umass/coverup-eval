# file: semantic_release/hvcs.py:365-371
# asked: {"lines": [365, 366, 371], "branches": []}
# gained: {"lines": [365, 366, 371], "branches": []}

import os
from typing import Optional
import pytest
from semantic_release.hvcs import Gitlab

@pytest.fixture
def clear_env(monkeypatch):
    """Fixture to clear the GL_TOKEN environment variable before and after each test."""
    monkeypatch.delenv("GL_TOKEN", raising=False)
    yield
    monkeypatch.delenv("GL_TOKEN", raising=False)

def test_gitlab_token_exists(monkeypatch, clear_env):
    """Test that Gitlab.token() returns the value of GL_TOKEN if it exists."""
    monkeypatch.setenv("GL_TOKEN", "test_token")
    assert Gitlab.token() == "test_token"

def test_gitlab_token_not_exists(clear_env):
    """Test that Gitlab.token() returns None if GL_TOKEN does not exist."""
    assert Gitlab.token() is None
