# file: semantic_release/hvcs.py:493-499
# asked: {"lines": [493, 499], "branches": []}
# gained: {"lines": [493, 499], "branches": []}

import pytest
from unittest.mock import patch
from semantic_release.hvcs import get_domain, get_hvcs

def test_get_domain(monkeypatch):
    class MockHVCS:
        @staticmethod
        def domain():
            return "mockdomain.com"

    monkeypatch.setattr('semantic_release.hvcs.get_hvcs', lambda: MockHVCS())
    
    result = get_domain()
    assert result == "mockdomain.com"
