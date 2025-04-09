# file: semantic_release/hvcs.py:118-124
# asked: {"lines": [118, 119, 124], "branches": []}
# gained: {"lines": [118, 119, 124], "branches": []}

import os
import pytest
from semantic_release.hvcs import Github

def test_github_token(monkeypatch):
    # Test when GH_TOKEN is set
    monkeypatch.setenv("GH_TOKEN", "test_token")
    assert Github.token() == "test_token"

    # Test when GH_TOKEN is not set
    monkeypatch.delenv("GH_TOKEN", raising=False)
    assert Github.token() is None
