# file: semantic_release/hvcs.py:502-508
# asked: {"lines": [502, 508], "branches": []}
# gained: {"lines": [502, 508], "branches": []}

import pytest
from unittest.mock import patch
from semantic_release.hvcs import check_token, get_hvcs, Github, Gitlab
from semantic_release.errors import ImproperConfigurationError

@pytest.fixture
def mock_hvcs(monkeypatch):
    class MockHVCS:
        @staticmethod
        def token():
            return "mock_token"

    monkeypatch.setattr(Github, "token", MockHVCS.token)
    monkeypatch.setattr("semantic_release.hvcs.config", {"hvcs": "github"})

def test_check_token_exists(mock_hvcs):
    assert check_token() is True

def test_check_token_not_exists(monkeypatch):
    class MockHVCS:
        @staticmethod
        def token():
            return None

    monkeypatch.setattr(Github, "token", MockHVCS.token)
    monkeypatch.setattr("semantic_release.hvcs.config", {"hvcs": "github"})
    assert check_token() is False

def test_check_token_invalid_hvcs(monkeypatch):
    monkeypatch.setattr("semantic_release.hvcs.config", {"hvcs": "invalid"})
    with pytest.raises(ImproperConfigurationError):
        check_token()
