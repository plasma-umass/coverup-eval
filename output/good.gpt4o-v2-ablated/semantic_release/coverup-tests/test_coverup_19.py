# file: semantic_release/hvcs.py:502-508
# asked: {"lines": [502, 508], "branches": []}
# gained: {"lines": [502, 508], "branches": []}

import pytest
from unittest.mock import patch

# Assuming get_hvcs is a function in the semantic_release.hvcs module
from semantic_release.hvcs import get_hvcs

def test_check_token_exists(monkeypatch):
    class MockHVCS:
        @staticmethod
        def token():
            return "mock_token"

    monkeypatch.setattr('semantic_release.hvcs.get_hvcs', lambda: MockHVCS())
    from semantic_release.hvcs import check_token
    assert check_token() is True

def test_check_token_not_exists(monkeypatch):
    class MockHVCS:
        @staticmethod
        def token():
            return None

    monkeypatch.setattr('semantic_release.hvcs.get_hvcs', lambda: MockHVCS())
    from semantic_release.hvcs import check_token
    assert check_token() is False
