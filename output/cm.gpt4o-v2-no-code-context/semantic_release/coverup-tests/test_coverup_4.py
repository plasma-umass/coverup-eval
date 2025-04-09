# file: semantic_release/hvcs.py:484-490
# asked: {"lines": [484, 490], "branches": []}
# gained: {"lines": [484, 490], "branches": []}

import pytest
from unittest.mock import patch
from semantic_release.hvcs import get_token, get_hvcs

@pytest.fixture
def mock_get_hvcs(monkeypatch):
    class MockHVCS:
        def token(self):
            return "mocked_token"
    
    monkeypatch.setattr("semantic_release.hvcs.get_hvcs", lambda: MockHVCS())

def test_get_token(mock_get_hvcs):
    token = get_token()
    assert token == "mocked_token"
