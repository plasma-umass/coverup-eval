# file: semantic_release/hvcs.py:118-124
# asked: {"lines": [118, 119, 124], "branches": []}
# gained: {"lines": [118, 119, 124], "branches": []}

import os
from typing import Optional
import pytest
from semantic_release.hvcs import Github

@pytest.fixture(autouse=True)
def clear_env(monkeypatch):
    # Clear the GH_TOKEN environment variable before each test
    monkeypatch.delenv("GH_TOKEN", raising=False)

def test_github_token_exists(monkeypatch):
    # Set the GH_TOKEN environment variable
    monkeypatch.setenv("GH_TOKEN", "test_token")
    
    # Assert that the token method returns the correct value
    assert Github.token() == "test_token"

def test_github_token_not_exists():
    # Assert that the token method returns None when GH_TOKEN is not set
    assert Github.token() is None
