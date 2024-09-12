# file: semantic_release/hvcs.py:365-371
# asked: {"lines": [365, 366, 371], "branches": []}
# gained: {"lines": [365, 366, 371], "branches": []}

import os
import pytest
from semantic_release.hvcs import Gitlab

def test_gitlab_token(monkeypatch):
    # Test when GL_TOKEN is not set
    monkeypatch.delenv('GL_TOKEN', raising=False)
    assert Gitlab.token() is None

    # Test when GL_TOKEN is set
    monkeypatch.setenv('GL_TOKEN', 'test_token')
    assert Gitlab.token() == 'test_token'
