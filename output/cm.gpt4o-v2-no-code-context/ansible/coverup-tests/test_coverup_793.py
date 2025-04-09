# file: lib/ansible/utils/version.py:262-263
# asked: {"lines": [262, 263], "branches": []}
# gained: {"lines": [262, 263], "branches": []}

import pytest
from ansible.utils.version import SemanticVersion

def test_semantic_version_lt(monkeypatch):
    class MockVersion:
        def _cmp(self, other):
            return -1

    version1 = SemanticVersion("1.0.0")
    version2 = MockVersion()

    monkeypatch.setattr(version1, '_cmp', version2._cmp)
    
    assert version1 < version2

def test_semantic_version_not_lt(monkeypatch):
    class MockVersion:
        def _cmp(self, other):
            return 1

    version1 = SemanticVersion("1.0.0")
    version2 = MockVersion()

    monkeypatch.setattr(version1, '_cmp', version2._cmp)
    
    assert not (version1 < version2)
