# file: semantic_release/hvcs.py:493-499
# asked: {"lines": [493, 499], "branches": []}
# gained: {"lines": [493, 499], "branches": []}

import pytest
from semantic_release.hvcs import get_domain, get_hvcs

class MockHVCS:
    @staticmethod
    def domain():
        return "mockdomain.com"

@pytest.fixture
def mock_get_hvcs(monkeypatch):
    monkeypatch.setattr("semantic_release.hvcs.get_hvcs", lambda: MockHVCS())

def test_get_domain(mock_get_hvcs):
    assert get_domain() == "mockdomain.com"
